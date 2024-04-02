# Log Anomaly Detector

## Overview
This Python script is designed to monitor specified log files for anomalies, based on a set of customizable rules. It helps in early detection of unusual patterns that could indicate security issues.

## Installation
- Ensure Python 3.6+ is installed on your system.
- Install required packages:
    ```
    pip install watchdog pandas
    ```

## Usage
To start monitoring a log file for anomalies, run:
    ```
    python log_anomaly_detector.py /path/to/your/logfile.log
    ```

## Configuring Rules
Edit the `rules` list in the script to define what patterns to watch for. Each rule is a dictionary with a `pattern` and a `message` key. The `pattern` is a string to look for in the log lines, and the `message` is what to print when the pattern is found.

## Extending
The script can be extended with more sophisticated analysis and alerting mechanisms, such as email notifications or integration with a centralized monitoring system.

## License
This project is licensed under the MIT License.
