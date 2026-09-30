# LR4: scan Unpaywall for all missing PDFs, write unpaywall_scan.json
$miss = Get-Content -LiteralPath 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\missing_pdfs.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$res = @()
foreach ($m in $miss) {
    $doi = $m.doi
    if (-not $doi) { $res += [pscustomobject]@{row=$m.row; is_oa='NO-DOI'; pdf=''; url=''; note=''}; continue }
    try {
        $r = Invoke-WebRequest -Uri ("https://api.unpaywall.org/v2/{0}?email=research@example.org" -f $doi) -UseBasicParsing -TimeoutSec 30 -Headers @{ 'User-Agent'='Mozilla/5.0' }
        $j = $r.Content | ConvertFrom-Json
        $pdf = ''; $url = ''; $note = ''
        foreach ($loc in $j.oa_locations) {
            if (-not $pdf -and $loc.url_for_pdf) { $pdf = $loc.url_for_pdf }
            if (-not $url -and $loc.url) { $url = $loc.url }
        }
        if (-not $pdf -and $j.best_oa_location.url_for_pdf) { $pdf = $j.best_oa_location.url_for_pdf }
        if (-not $url -and $j.best_oa_location.url) { $url = $j.best_oa_location.url }
        if (-not $pdf -and $j.is_oa) { $note = 'OA but no direct pdf url' }
        $res += [pscustomobject]@{row=$m.row; is_oa=[string]$j.is_oa; pdf=$pdf; url=$url; note=$note}
    } catch {
        $res += [pscustomobject]@{row=$m.row; is_oa='ERR'; pdf=''; url=''; note=('ERR: ' + $_.Exception.Message.Substring(0, [Math]::Min(80, $_.Exception.Message.Length)))}
    }
    Start-Sleep -Milliseconds 250
}
$res | ConvertTo-Json -Depth 3 | Out-File 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\unpaywall_scan.json' -Encoding utf8
$oa = @($res | Where-Object { $_.is_oa -eq 'True' }).Count
$pdfs = @($res | Where-Object { $_.pdf }).Count
Write-Output ("scanned={0} is_oa={1} with_pdf_url={2}" -f $res.Count, $oa, $pdfs)
