import psutil
import time
import sys

# To test the cpu usage alert working, use commad: `timeout 60s dd if=/dev/zero of=/dev/null &` stress up CPU.


# Configuration
CPU_THRESHOLD = 80.0
CHECK_INTERVAL = 1

def get_cpu_usage():
    """Get current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def check_alert(cpu_usage):
    """Check if CPU usage is too high."""
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT! CPU usage too high: {cpu_usage:.1f}%")

def monitor_cpu():
    """Monitor CPU usage continuously."""
    print("Monitoring CPU... (Press Ctrl+C to stop)")
    
    try:
        while True:
            cpu_usage = get_cpu_usage()
            print(f"CPU Usage: {cpu_usage:.1f}%")
            check_alert(cpu_usage)
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\nStopped monitoring.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()