import time
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd

class AnomalyDetector(FileSystemEventHandler):
    def __init__(self, rules):
        self.rules = rules

    def on_modified(self, event):
        if not event.is_directory:
            self.check_for_anomalies(event.src_path)

    def check_for_anomalies(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for rule in self.rules:
                if rule["pattern"] in lines[-1]:
                    print(f"Anomaly detected: {rule['message']}")
                    # Extend for more sophisticated alerting mechanisms

def main():
    parser = argparse.ArgumentParser(description="Monitor log files for anomalies.")
    parser.add_argument('file', type=str, help="Path to the log file to monitor.")
    args = parser.parse_args()

    rules = [
        {"pattern": "ERROR", "message": "Error detected in log."},
        # Define more rules here
    ]

    event_handler = AnomalyDetector(rules=rules)
    observer = Observer()
    observer.schedule(event_handler, path=args.file, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
