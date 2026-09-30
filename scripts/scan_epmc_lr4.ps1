# LR4: Europe PMC scan for remaining 58 DOIs -> epmc_scan.json
$work = Get-Content -LiteralPath 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\work_rest.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$res = @()
foreach ($w in $work) {
    $q = [uri]::EscapeDataString('DOI:"' + $w.doi + '"')
    try {
        $r = Invoke-WebRequest -Uri ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={0}&resultType=core&format=json&pageSize=5" -f $q) -UseBasicParsing -TimeoutSec 40 -Headers @{ 'User-Agent'='Mozilla/5.0' }
        $j = $r.Content | ConvertFrom-Json
        $hit = $j.resultList.result | Select-Object -First 1
        if ($hit) {
            $ft = $hit.fullTextUrlList.fullTextUrl
            $pdf = ''; $xml = ''
            foreach ($u in $ft) {
                if ($u.documentStyle -eq 'pdf' -and -not $pdf) { $pdf = $u.url }
                if ($u.documentStyle -eq 'text' -and -not $xml) { $xml = $u.url }
            }
            $res += [pscustomobject]@{row=$w.r; doi=$w.doi; name=$w.name; pmcid=$hit.pmcid; pmid=$hit.pmid; isOA=[string]$hit.isOpenAccess; pdf=$pdf; xml=$xml}
        } else {
            $res += [pscustomobject]@{row=$w.r; doi=$w.doi; name=$w.name; pmcid=''; pmid=''; isOA='no-hit'; pdf=''; xml=''}
        }
    } catch {
        $res += [pscustomobject]@{row=$w.r; doi=$w.doi; name=$w.name; pmcid=''; pmid=''; isOA='ERR'; pdf=''; xml=''; err=($_.Exception.Message.Substring(0,[Math]::Min(80,$_.Exception.Message.Length)))}
    }
    Start-Sleep -Milliseconds 250
}
$res | ConvertTo-Json -Depth 3 | Out-File 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\epmc_scan.json' -Encoding utf8
$pdfs = @($res | Where-Object { $_.pdf }).Count
$xmls = @($res | Where-Object { $_.xml -and -not $_.pdf }).Count
Write-Output ("scanned={0} with_pdf={1} xml_only={2}" -f $res.Count, $pdfs, $xmls)
