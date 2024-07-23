import psutil

# Define thresholds (adjust these values as per your requirements)
CPU_THRESHOLD = 80  # Percentage
MEMORY_THRESHOLD = 80  # Percentage
DISK_THRESHOLD = 90  # Percentage
PROCESS_THRESHOLD = 500  # Number of processes

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print("CPU usage is above threshold! Alert.")
        # You can add additional actions here, like sending an alert message.

# Function to check memory usage
def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    print(f"Current Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        print("Memory usage is above threshold! Alert.")
        # You can add additional actions here, like sending an alert message.

# Function to check disk usage
def check_disk_usage():
    disk_usage = psutil.disk_usage('/').percent
    print(f"Current Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        print("Disk usage is above threshold! Alert.")
        # You can add additional actions here, like sending an alert message.

# Function to check number of running processes
def check_running_processes():
    process_count = len(psutil.pids())
    print(f"Current Number of Running Processes: {process_count}")
    if process_count > PROCESS_THRESHOLD:
        print("Number of running processes is above threshold! Alert.")
        # You can add additional actions here, like sending an alert message.

# Main function to call all health checks
def main():
    print("Starting system health checks...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    print("Health checks completed.")

# Execute main function
if __name__ == "__main__":
    main()
