# Sector Rotation Schedule

Use the sector-rotation skill at these times each trading day:

- 8:15 ET
- 9:15 ET

## Windows Task Scheduler setup

Use the helper in the examples folder:

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\nitis\.openclaw\workspace\skills\sector-rotation\examples\setup_sector_rotation_task.ps1"
```

## Example cron equivalent

```cron
15 8,9 * * 1-5 /path/to/your/telegram-sector-rotation-job.sh
```

## Notes

- `15 8,9` = 8:15 and 9:15.
- `* * 1-5` = Monday through Friday.
- If your system runs in a different timezone, convert ET to the machine's local timezone before scheduling.
- In Windows, the task scheduler uses the machine local timezone; if you are not in ET, adjust the scheduled run times accordingly.
- The job will still print the alert locally if the Telegram bot token or chat ID is not yet configured.

## Why this schedule

This creates a very early market pulse and a second confirmation check when the market has had more time to react to opening moves.
