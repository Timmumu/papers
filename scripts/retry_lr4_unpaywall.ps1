param(
    [string]$Email = "lr4@example.com"
)

$ErrorActionPreference = "Continue"
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$ss = Join-Path $root "04d_LR4\5. SLR matrix\ss"
$coveragePath = Join-Path $ss "coverage_lr4.json"
$corpusPath = Join-Path $ss "corpus_lr4.json"
$outPath = Join-Path $ss "unpaywall_retry_$(Get-Date -Format yyyyMMdd_HHmmss).json"

$coverage = Get-Content $coveragePath -Raw -Encoding UTF8 | ConvertFrom-Json
$corpus = Get-Content $corpusPath -Raw -Encoding UTF8 | ConvertFrom-Json
$results = New-Object System.Collections.Generic.List[object]

$coverage.PSObject.Properties | ForEach-Object {
    $rowId = [int]$_.Name
    $cov = $_.Value
    if ($cov.status -eq "verified") { return }

    $rec = $corpus[$rowId - 1]
    $doi = $cov.doi
    if (-not $doi -and $rec -and $rec.doi) { $doi = $rec.doi }
    if (-not $doi) {
        $results.Add([pscustomobject]@{ row=$rowId; slug=$cov.slug; status=$cov.status; doi=$null; is_oa=$null; oa_status=$null; pdf=$null; landing=$null; error="no DOI" })
        return
    }

    $url = "https://api.unpaywall.org/v2/$doi?email=$Email"
    try {
        $j = Invoke-RestMethod -Uri $url -TimeoutSec 30 -Headers @{ "User-Agent"="Mozilla/5.0 LR4 retry" }
        $pdf = $null
        $landing = $null
        if ($j.best_oa_location) {
            $pdf = $j.best_oa_location.url_for_pdf
            $landing = $j.best_oa_location.url
        }
        $results.Add([pscustomobject]@{ row=$rowId; slug=$cov.slug; status=$cov.status; doi=$doi; is_oa=$j.is_oa; oa_status=$j.oa_status; pdf=$pdf; landing=$landing; error=$null })
        "R{0:D3}|{1}|oa={2}|status={3}|pdf={4}|landing={5}" -f $rowId,$cov.slug,$j.is_oa,$j.oa_status,$pdf,$landing
    } catch {
        $results.Add([pscustomobject]@{ row=$rowId; slug=$cov.slug; status=$cov.status; doi=$doi; is_oa=$null; oa_status=$null; pdf=$null; landing=$null; error=$_.Exception.Message })
        "R{0:D3}|{1}|ERR|{2}" -f $rowId,$cov.slug,$_.Exception.Message
    }
}

$results | ConvertTo-Json -Depth 8 | Set-Content -Path $outPath -Encoding UTF8
"saved $outPath"
