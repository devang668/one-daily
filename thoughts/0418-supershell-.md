\# 一行超级命令，看看自己装了啥

powershell 中使用







Write-Host "`n====== Node.js ======" -F Cyan; if(Get-Command node -EA 0){Write-Host "  Path: $((Get-Command node).Source)"; Write-Host "  Version: $(node -v)"}else{Write-Host "  Not found"}; Write-Host "`n====== npm ======" -F Cyan; if(Get-Command npm -EA 0){Write-Host "  Path: $((Get-Command npm).Source)"; Write-Host "  Version: $(npm -v)"; Write-Host "  Global Dir: $(npm root -g)"; Write-Host "  \[Global Packages]"; npm list -g --depth=0}else{Write-Host "  Not found"}; Write-Host "`n====== Python ======" -F Cyan; if(Get-Command python -EA 0){Write-Host "  Path: $((Get-Command python).Source)"; python --version 2>\&1|ForEach-Object{Write-Host "  $\_"}; if(Get-Command pip -EA 0){Write-Host "  Pip Path: $((Get-Command pip).Source)"}; Write-Host "  Site Packages:"; python -c "import site;\[print('  '+p)for p in site.getsitepackages()]" 2>$null; Write-Host "  \[Pip Packages]"; python -m pip list 2>$null}else{Write-Host "  Not found"}; Write-Host "`n====== Python Virtual Environments ======" -F Cyan; Write-Host "  Scanning..."; $v=@(); @($env:USERPROFILE,"$env:USERPROFILE\\Desktop","$env:USERPROFILE\\Documents","$env:USERPROFILE\\Projects","$env:USERPROFILE\\code","D:\\")|ForEach-Object{if(Test-Path $\_){Get-ChildItem -Path $\_ -Recurse -Filter "pyvenv.cfg" -EA 0 -Depth 5|ForEach-Object{$v+=$\_.DirectoryName}}}; if($v.Count -gt 0){Write-Host "  Found $($v.Count) venv(s):" -F Green; $v|ForEach-Object{Write-Host "    $\_" -F Yellow}}else{Write-Host "  No venvs found"}; Write-Host "`n============================"; Write-Host "Done!" -F Green





