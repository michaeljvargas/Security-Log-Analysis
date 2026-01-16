# Security-Log-Analysis
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(7)

users = ["mvargas", "rima", "admin", "helpdesk", "guest", "finance1", "finance2"]
ips = ["192.168.1.10", "10.0.0.8", "203.0.113.5", "198.51.100.23", "45.33.32.156", "172.16.0.9"]
locations = ["Salt Lake City, US", "New York, US", "London, UK", "Mexico City, MX", "Berlin, DE", "Unknown"]
devices = ["Windows-10", "MacOS", "iPhone", "Android", "Linux", "Unknown"]

start = datetime.now() - timedelta(days=7)

rows = []
for _ in range(1200):
    ts = start + timedelta(minutes=random.randint(0, 7 * 24 * 60))
    user = random.choice(users)
    ip = random.choice(ips)
    location = random.choice(locations)
    device = random.choice(devices)

    event = "SUCCESS" if random.random() < 0.65 else "FAILED"
    rows.append([ts.strftime("%Y-%m-%d %H:%M:%S"), user, ip, location, device, event])

# Inject brute-force behavior
attack_ip = "45.33.32.156"
target_user = "admin"
attack_start = datetime.now() - timedelta(days=2)

for i in range(80):
    ts = attack_start + timedelta(minutes=i)
    rows.append([
        ts.strftime("%Y-%m-%d %H:%M:%S"),
        target_user,
        attack_ip,
        "Unknown",
        "Linux",
        "FAILED"
    ])

# Success after many failures (high-risk signal)
rows.append([
    (attack_start + timedelta(minutes=81)).strftime("%Y-%m-%d %H:%M:%S"),
    target_user,
    attack_ip,
    "Unknown",
    "Linux",
    "SUCCESS"
])

df = pd.DataFrame(
    rows,
    columns=["timestamp", "username", "source_ip", "location", "device", "event_type"]
)

df.to_csv("data/auth_logs.csv", index=False)

print("Created data/auth_logs.csv with", len(df), "rows")

# End of Security-Log-Analysis
# This script generates synthetic authentication logs for security log analysis.
# The logs include normal user activity as well as simulated brute-force attack patterns.
# The generated logs are saved in a CSV file for further analysis.
