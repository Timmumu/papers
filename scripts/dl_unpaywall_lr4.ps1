# LR4: download the 38 Unpaywall OA PDFs into 4. fulltext L2, verify %PDF magic
$scan = Get-Content -LiteralPath 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\unpaywall_scan.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$miss = Get-Content -LiteralPath 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\missing_pdfs.json' -Raw -Encoding UTF8 | ConvertFrom-Json
$slugByRow = @{}
foreach ($m in $miss) { $slugByRow[[int]$m.row] = $m.slug }
$outDir = 'H:\phd\6.pjt\LR1\papers\04d_LR4\4. fulltext L2'
$log = @()
$ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
foreach ($s in $scan) {
    if (-not $s.pdf) { continue }
    $name = ('R{0:D3}_{1}.pdf' -f [int]$s.row, $slugByRow[[int]$s.row])
    $dst = Join-Path $outDir $name
    if (Test-Path $dst) { $log += "$name`tSKIP-exists"; continue }
    try {
        Invoke-WebRequest -Uri $s.pdf -OutFile $dst -UseBasicParsing -TimeoutSec 90 -Headers @{ 'User-Agent' = $ua } -MaximumRedirection 6
        $fi = Get-Item $dst
        $head = [System.IO.File]::ReadAllBytes($fi.FullName)[0..3]
        $magic = [System.Text.Encoding]::ASCII.GetString($head)
        if ($magic -eq '%PDF' -and $fi.Length -gt 15000) { $log += "$name`tOK`t$($fi.Length)" }
        else { $log += "$name`tBAD-magic($magic)`t$($fi.Length)"; Remove-Item $dst -Force }
    } catch {
        $log += "$name`tFAIL`t$($_.Exception.Message.Substring(0,[Math]::Min(90,$_.Exception.Message.Length)))"
        if (Test-Path $dst) { Remove-Item $dst -Force }
    }
    Start-Sleep -Milliseconds 400
}
$log | Out-File 'H:\phd\6.pjt\LR1\papers\04d_LR4\5. SLR matrix\ss\unpaywall_dl_log.txt' -Encoding UTF8
$ok = @($log | Where-Object { $_ -match '^R\d+\S*\tOK' }).Count
$bad = @($log | Where-Object { $_ -notmatch '^R\d+\S*\tOK' }).Count
Write-Output ("downloaded_ok={0} other={1}" -f $ok, $bad)
$log | Where-Object { $_ -notmatch '\tOK' } | ForEach-Object { Write-Output $_ }
