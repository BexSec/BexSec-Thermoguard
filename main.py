import psutil

# Threshold Constants
CPU_WARNING = 70.0
CPU_CRITICAL = 85.0

# Ingest live CPU data (interval=1 waits 1 second to measure usage)
live_cpu = psutil.cpu_percent(interval=1)

print(f"Current CPU Usage: {live_cpu}%")

# Our alert logic
if live_cpu >= CPU_CRITICAL:
    print("ALERT: CRITICAL CPU SPIKE DETECTED")
elif live_cpu >= CPU_WARNING:
    print("WARNING: Elevated CPU usage")
else:
    print("STATUS: System Normal")
