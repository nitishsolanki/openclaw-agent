$ErrorActionPreference = 'Stop'
$workspace = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$project = Join-Path $workspace 'ai-trading-agent'
$artifact = Join-Path $workspace 'python_candidates.json'
$gh = 'C:\Program Files\GitHub CLI\gh.exe'
$python = 'C:\Users\nitis\AppData\Local\Programs\Python\Python314\python.exe'

$runs = & $gh run list --workflow market-pages.yml --status success --limit 10 --json databaseId,createdAt,event | ConvertFrom-Json
$run = $runs | Where-Object { $_.event -in @('schedule', 'workflow_dispatch') } | Select-Object -First 1
if (-not $run) { throw 'No successful scheduled or manual market-report run found.' }
if (([DateTime]$run.createdAt).ToLocalTime().Date -ne (Get-Date).Date) {
    throw "Latest successful market scan $($run.databaseId) is not from today."
}

if (Test-Path $artifact) { Remove-Item -LiteralPath $artifact -Force }
& $gh run download $run.databaseId --name python-candidates --dir $workspace
if (-not (Test-Path $artifact)) { throw "GitHub run $($run.databaseId) did not provide python_candidates.json." }

Push-Location $workspace
try { & $python (Join-Path $project 'scripts\paper_autotrader.py') }
finally { Pop-Location }
