# LR4: OpenAlex scan for remaining DOIs -> openalex_scan.json
$work = Get-Content -LiteralPath 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\work_final.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$have = @(Get-ChildItem 'H:\phd\6.pjt\LR1\papers\04d_LR4\4. fulltext L2' -Filter '*.pdf' | ForEach-Object { $_.BaseName })
$res = @()
foreach ($w in $work) {
    if ($have -contains $w.name) { continue }
    try {
        $r = Invoke-WebRequest -Uri ("https://api.openalex.org/works/https://doi.org/{0}?mailto=research@example.org" -f $w.doi) -UseBasicParsing -TimeoutSec 40 -Headers @{ 'User-Agent'='Mozilla/5.0' }
        $j = $r.Content | ConvertFrom-Json
        $oa = $j.open_access
        $pdf = ''; $loc = ''
        if ($j.best_oa_location) { $pdf = $j.best_oa_location.pdf_url; $loc = $j.best_oa_location.landing_page_url }
        if (-not $pdf -and $j.primary_location.pdf_url) { $pdf = $j.primary_location.pdf_url }
        $res += [pscustomobject]@{row=$w.r; doi=$w.doi; name=$w.name; is_oa=[string]$oa.is_oa; pdf=$pdf; loc=$loc}
    } catch {
        $res += [pscustomobject]@{row=$w.r; doi=$w.doi; name=$w.name; is_oa='ERR'; pdf=''; loc=''; err=($_.Exception.Message.Substring(0,[Math]::Min(80,$_.Exception.Message.Length)))}
    }
    Start-Sleep -Milliseconds 200
}
$res | ConvertTo-Json -Depth 3 | Out-File 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\openalex_scan.json' -Encoding utf8
$pdfs = @($res | Where-Object { $_.pdf }).Count
Write-Output ("scanned={0} with_pdf={1}" -f $res.Count, $pdfs)
$res | Where-Object { $_.pdf } | ForEach-Object { Write-Output ($_.name + ' | ' + $_.is_oa + ' | ' + $_.pdf.Substring(0,[Math]::Min(110,$_.pdf.Length))) }
