param([string]$JsonPath)
$j = Get-Content $JsonPath -Raw | ConvertFrom-Json
$c = $j.content
$title = $j.title
$key = $j.item_key
Write-Output "TITLE: $title"
Write-Output "KEY: $key"
Write-Output "LEN: $($c.Length)"
Write-Output "PAGES: $($j.indexed_pages)/$($j.total_pages)"
Write-Output ""

# Find common section headers
$markers = @('abstract','Abstract','Introduction','1. Introduction','2. ','3. ','4. ','5. ','6. ','7. ',
             'Methodology','Method','Methods','Materials and methods','Results','Findings','Discussion',
             'Conclusion','Conclusions','Concluding','Related work','Background','Literature review','Limitations')
$hits = @()
foreach ($m in $markers) {
  $idx = 0
  while (($idx = $c.IndexOf($m, $idx)) -ge 0) {
    # Look at preceding char to filter mid-word matches
    $prev = if ($idx -gt 0) { $c[$idx-1] } else { "`n" }
    if ($prev -eq "`n" -or $prev -eq ' ' -or $prev -eq "`r") {
      $hits += [PSCustomObject]@{Pos=$idx; Marker=$m}
    }
    $idx++
  }
}
$hits = $hits | Sort-Object Pos | Group-Object Pos | ForEach-Object { $_.Group[0] }

foreach ($h in $hits) {
  $snip = $c.Substring($h.Pos, [Math]::Min(1100, $c.Length - $h.Pos))
  Write-Output "===== POS=$($h.Pos) MARKER='$($h.Marker)' ====="
  Write-Output $snip
  Write-Output ""
}
