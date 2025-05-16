import psutil
import subprocess

print("---- SYSTEM MONITOR ----")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory.percent}% of {round(memory.total / 1e+9, 2)} GB")
print(f"Disk Usage: {disk.percent}% of {round(disk.total / 1e+9, 2)} GB")

# Auto-Fixes
if cpu > 70:
    print("⚠️ High CPU Usage! Running dummy restart.")
    subprocess.call(["./restart_dummy.sh"])

if memory.percent > 80:
    print("⚠️ High Memory Usage! (No auto-fix added yet)")

if disk.percent > 80:
    print("⚠️ Disk Almost Full! Running cleanup.")
    subprocess.call(["./clear_temp.sh"])
