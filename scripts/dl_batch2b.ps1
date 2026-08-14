$ft = "h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext"
$ua = @{'User-Agent' = 'Mozilla/5.0'}
$jobs = @(
    @('3795_Chan2025', 'https://mdpi-res.com/d_attachment/sensors/sensors-25-12727/article_deploy/sensors-25-12727.pdf'),
    @('3911_Chen2025', 'https://mdpi-res.com/d_attachment/applsci/applsci-15-06009/article_deploy/applsci-15-06009.pdf'),
    @('3953_Chen2026', 'https://mdpi-res.com/d_attachment/buildings/buildings-16-01982/article_deploy/buildings-16-01982.pdf')
)
foreach ($j in $jobs) {
    $slug, $url = $j
    try {
        Invoke-WebRequest -Uri $url -OutFile "$ft\$slug.pdf" -UseBasicParsing -Headers $ua
        Write-Output "$slug OK $((Get-Item "$ft\$slug.pdf").Length)"
    } catch {
        Write-Output "$slug FAIL $($_.Exception.Message)"
    }
}
