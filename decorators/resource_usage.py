import psutil
import os

# Get the process ID of the current notebook
pid = os.getpid()

# Get the process object
proc = psutil.Process(pid)

# Get CPU usage
cpu_usage = proc.cpu_percent(interval=1)

memory_info = proc.memory_info().rss

# Convert memory usage to gigabytes
memory_usage_gb = memory_info / (1024 ** 3)

print(f"Memory Usage: {memory_usage_gb:.2f} GB")

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_info}")
