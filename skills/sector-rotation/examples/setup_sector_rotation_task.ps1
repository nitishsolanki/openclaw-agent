$ErrorActionPreference = 'Stop'

$taskName = 'SectorRotationTelegram'
$scriptPath = 'C:\Users\nitis\.openclaw\workspace\skills\sector-rotation\examples\telegram_sector_rotation_job.sh'
$pythonPath = 'C:\Users\nitis\AppData\Local\Programs\Python\Python312\python.exe'

if (-not (Test-Path $scriptPath)) {
    throw "Script not found: $scriptPath"
}

if (-not (Test-Path $pythonPath)) {
    throw "Python not found: $pythonPath"
}

$action = New-ScheduledTaskAction -Execute 'bash.exe' -Argument "-lc 'export TELEGRAM_BOT_TOKEN=\"$env:TELEGRAM_BOT_TOKEN\"; export TELEGRAM_CHAT_ID=\"$env:TELEGRAM_CHAT_ID\"; export PYTHON_BIN=\"$pythonPath\"; $scriptPath'"

$trigger1 = New-ScheduledTaskTrigger -Daily -At '08:15'
$trigger2 = New-ScheduledTaskTrigger -Daily -At '09:15'

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger1,$trigger2 -Force -Description 'Sector rotation Telegram alert at 8:15 ET and 9:15 ET'

Write-Host "Created scheduled task: $taskName"
Write-Host "Next steps: add TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID to the user environment variables, then test the task."
