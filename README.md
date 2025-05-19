# System Monitoring Tool (Python + Bash)

This is a lightweight system monitoring tool built in Python that tracks CPU, memory, and disk usage and takes action when thresholds are exceeded.

Implemented on Amazon Linux (EC2)

## Features

- Monitors CPU, memory, disk, and uptime
- Logs system metrics every 10 seconds
- Triggers auto-fix scripts (Bash) when:
  - CPU usage > 60%
  - Memory usage > 80%
  - Disk usage > 80%
- Displays live alerts in the terminal
- Logs all events to `system_monitor.log`

## Files

- `monitor.py` – Main Python script
- `restart_dummy.sh` – Bash script to restart dummy service
- `clear_temp.sh` – Bash script to clear temp space
- `system_monitor.log` – Log file (auto-generated through monitoring script)
- `usage_percentage.py` - Printing out the system metrics 
- `README.md` – You’re reading it

## How to Run

```bash
chmod +x restart_dummy.sh
chmod +x clear_temp.sh
python3 monitor.py
python3 usage_percentage.py

## How to view log file

cat system_monitoring.log - lists all the logs
tail -f system_monitoring.log - lists the latest logs only
