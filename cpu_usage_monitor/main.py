import psutil
import time
import sys

# Threshold percentage
CPU_THRESHOLD = 80.0
# Time interval between checks (in seconds)
CHECK_INTERVAL = 1

def monitor_cpu():
    print("Monitoring CPU usage... (Press Ctrl+C to stop)")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)

            if cpu_usage > CPU_THRESHOLD:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage:.2f}%")

            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred during CPU monitoring: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()
