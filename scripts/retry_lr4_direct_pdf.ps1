$ErrorActionPreference = "Continue"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ss = Join-Path $root "04d_LR4\5. SLR matrix\ss"
$outDir = Join-Path $root "04d_LR4\4. fulltext L2"
$coverage = Get-Content (Join-Path $ss "coverage_lr4.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$corpus = Get-Content (Join-Path $ss "corpus_lr4.json") -Raw -Encoding UTF8 | ConvertFrom-Json
$logPath = Join-Path $ss "direct_pdf_retry_$(Get-Date -Format yyyyMMdd_HHmmss).json"
$results = New-Object System.Collections.Generic.List[object]

function Add-CandidateUrls($doi) {
    $urls = New-Object System.Collections.Generic.List[string]
    if (-not $doi) { return $urls }
    $lower = $doi.ToLowerInvariant()
    $escaped = [uri]::EscapeDataString($doi)
    $urls.Add("https://doi.org/$doi")
    if ($lower.StartsWith("10.1002/")) {
        $urls.Add("https://onlinelibrary.wiley.com/doi/pdfdirect/$doi")
        $urls.Add("https://onlinelibrary.wiley.com/doi/pdf/$doi")
    }
    if ($lower.StartsWith("10.1080/")) {
        $urls.Add("https://www.tandfonline.com/doi/pdf/$doi")
        $urls.Add("https://www.tandfonline.com/doi/epdf/$doi")
    }
    if ($lower.StartsWith("10.1007/")) {
        $urls.Add("https://link.springer.com/content/pdf/$doi.pdf")
    }
    if ($lower.StartsWith("10.1177/")) {
        $urls.Add("https://journals.sagepub.com/doi/pdf/$doi")
    }
    if ($lower.StartsWith("10.1680/")) {
        $urls.Add("https://www.icevirtuallibrary.com/doi/pdf/$doi")
    }
    if ($lower.StartsWith("10.1109/")) {
        $urls.Add("https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=$($doi.Split('.')[-1])")
    }
    if ($lower.StartsWith("10.1061/")) {
        $urls.Add("https://ascelibrary.org/doi/pdf/$doi")
    }
    if ($lower.StartsWith("10.2478/")) {
        $urls.Add("https://sciendo.com/pdf/10.2478/amns-2023-0506")
        $urls.Add("https://sciendo.com/article/10.2478/amns-2023-0506/pdf")
    }
    return $urls
}

function Try-DownloadPdf($url, $dest) {
    $tmp = "$dest.tmp"
    Remove-Item $tmp -ErrorAction SilentlyContinue
    try {
        Invoke-WebRequest -Uri $url -OutFile $tmp -TimeoutSec 45 -MaximumRedirection 8 -Headers @{ "User-Agent"="Mozilla/5.0 LR4 direct PDF retry"; "Accept"="application/pdf,text/html;q=0.8,*/*;q=0.5" }
        if (-not (Test-Path $tmp)) { return @($false, "no file") }
        $bytes = [System.IO.File]::ReadAllBytes($tmp)
        if ($bytes.Length -gt 5000 -and $bytes[0] -eq 0x25 -and $bytes[1] -eq 0x50 -and $bytes[2] -eq 0x44 -and $bytes[3] -eq 0x46) {
            Move-Item -Force $tmp $dest
            return @($true, "saved $($bytes.Length) bytes")
        }
        Remove-Item $tmp -ErrorAction SilentlyContinue
        return @($false, "not pdf $($bytes.Length) bytes")
    } catch {
        Remove-Item $tmp -ErrorAction SilentlyContinue
        return @($false, $_.Exception.Message)
    }
}

$coverage.PSObject.Properties | ForEach-Object {
    $rowId = [int]$_.Name
    $cov = $_.Value
    if ($cov.status -eq "verified") { return }
    $rec = $corpus[$rowId - 1]
    $doi = $cov.doi
    if (-not $doi -and $rec -and $rec.doi) { $doi = $rec.doi }
    $slug = $cov.slug
    if (-not $slug -and $rec -and $rec.slug) { $slug = $rec.slug }
    $dest = Join-Path $outDir ("R{0:D3}_{1}.pdf" -f $rowId,$slug)
    $found = $false
    $attempts = New-Object System.Collections.Generic.List[object]
    foreach($url in (Add-CandidateUrls $doi)) {
        if ($found) { break }
        $res = Try-DownloadPdf $url $dest
        $attempts.Add([pscustomobject]@{ url=$url; ok=$res[0]; message=$res[1] })
        if ($res[0]) { $found = $true; "FOUND R{0:D3}|{1}|{2}" -f $rowId,$slug,$url }
    }
    if (-not $found) { "MISS R{0:D3}|{1}|{2}" -f $rowId,$slug,$doi }
    $results.Add([pscustomobject]@{ row=$rowId; slug=$slug; doi=$doi; found=$found; dest=$(if($found){$dest}else{$null}); attempts=$attempts })
}

$results | ConvertTo-Json -Depth 8 | Set-Content -Path $logPath -Encoding UTF8
"saved $logPath"
