import time

def monitor_log(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            if "ERROR" in line:
                print("Error found:", line.strip())

monitor_log('/path/to/logfile.log')
