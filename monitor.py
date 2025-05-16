import psutil
import subprocess
import time
import datetime
import os

LOG_FILE = "system_monitor.log"

def log(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    return (datetime.datetime.now() - boot_time)

def monitor_system():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        uptime = get_uptime()

        # Print live metrics to terminal
        print("----- SYSTEM METRICS -----")
        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")
        print(f"Disk Usage: {disk}%")
        print(f"System Uptime: {uptime}")
        print("--------------------------")

        # Log metrics
        log(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}% | Uptime: {uptime}")

        cpu_alert = memory_alert = disk_alert = False

        # CPU Alert
        if cpu > 60:
            print("\a")
            print("ALERT: High CPU usage detected! Restarting dummy service...")
            log("High CPU usage! Running dummy restart.")
            try:
                subprocess.call(["./restart_dummy.sh"])
                log("Dummy process restarted.")
            except Exception as e:
                log(f"Failed to restart process: {e}")
            cpu_alert = True

        # Memory Alert
        if memory > 80:
            print("\a")
            print("ALERT: High Memory usage!")
            log("High Memory Usage!")
            memory_alert = True

        # Disk Alert
        if disk > 80:
            print("\a")
            print("ALERT: Disk Almost Full! Running cleanup...")
            log("Disk Almost Full! Running cleanup.")
            try:
                subprocess.call(["./clear_temp.sh"])
                log("Temp cleanup script executed.")
            except Exception as e:
                log(f"Failed to run cleanup script: {e}")
            disk_alert = True

        # Healthy System Message
        if not (cpu_alert or memory_alert or disk_alert):
            print("System is healthy. All metrics within normal range.")
            log("System is healthy.")

        time.sleep(10)

if __name__ == "__main__":
    monitor_system()
