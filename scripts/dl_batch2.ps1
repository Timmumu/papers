$ft = "h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext"
$ua = @{'User-Agent' = 'Mozilla/5.0'}
$jobs = @(
    @('3662_Armijo2024', 'https://mdpi-res.com/d_attachment/sensors/sensors-24-02115/article_deploy/sensors-24-02115.pdf'),
    @('3842_Aragon2025', 'https://mdpi-res.com/d_attachment/applsci/applsci-15-01557/article_deploy/applsci-15-01557.pdf'),
    @('3828_Arhrib2026', 'https://mdpi-res.com/d_attachment/buildings/buildings-16-02433/article_deploy/buildings-16-02433.pdf'),
    @('4028_Araujo2025', 'https://revistaingenieriaconstruccion.uc.cl/index.php/ric/article/download/98028/73118')
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
