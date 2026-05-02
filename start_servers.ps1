$rootDir = $PSScriptRoot
Set-Location $rootDir

$backend = Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", ".\venv\Scripts\activate; python -m uvicorn backend.main:app --reload --port 8000" -PassThru
Write-Host "Backend started in new window (PID: $($backend.Id))"

Set-Location "$rootDir\frontend"
$frontend = Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "npm run dev" -PassThru
Write-Host "Frontend started in new window (PID: $($frontend.Id))"

Set-Location $rootDir
Write-Host "Servers started. Close the popup windows to stop them."
Read-Host "Press Enter to finish this script..."
