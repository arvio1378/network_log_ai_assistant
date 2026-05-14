import random
import pandas as pd
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

# =========================
# CONFIG
# =========================
DEVICES = [
    "router1", "router2", "switch1", "switch2", "firewall1"
]

INTERFACES = ["eth0", "eth1", "eth2", "wlan0"]

EVENT_TYPES = [
    "interface_up",
    "interface_down",
    "packet_loss",
    "high_latency",
    "dhcp_failure",
    "dns_timeout",
    "cpu_spike",
    "normal_traffic"
]

SEVERITY_MAP = {
    "interface_up": "INFO",
    "interface_down": "CRITICAL",
    "packet_loss": "WARNING",
    "high_latency": "WARNING",
    "dhcp_failure": "CRITICAL",
    "dns_timeout": "WARNING",
    "cpu_spike": "WARNING",
    "normal_traffic": "INFO"
}

# =========================
# GENERATE SINGLE LOG
# =========================
def generate_log(start_time):
    device = random.choice(DEVICES)
    interface = random.choice(INTERFACES)
    event = random.choices(
        EVENT_TYPES,
        weights=[10, 5, 8, 6, 4, 4, 3, 60]  # normal lebih sering
    )[0]

    severity = SEVERITY_MAP[event]
    timestamp = start_time + timedelta(seconds=random.randint(1, 300))

    ip = fake.ipv4()

    message = ""

    if event == "interface_down":
        message = f"{device} interface {interface} is DOWN"
    elif event == "interface_up":
        message = f"{device} interface {interface} is UP"
    elif event == "packet_loss":
        message = f"High packet loss detected on {device} ({random.randint(5,40)}%)"
    elif event == "high_latency":
        message = f"Latency spike on {device} reaching {random.randint(100,500)}ms"
    elif event == "dhcp_failure":
        message = f"DHCP request failed from client {ip}"
    elif event == "dns_timeout":
        message = f"DNS timeout resolving domain for client {ip}"
    elif event == "cpu_spike":
        message = f"{device} CPU usage at {random.randint(80,100)}%"
    else:
        message = f"{device} normal traffic flow stable"

    log = {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "device": device,
        "interface": interface,
        "event": event,
        "severity": severity,
        "ip": ip,
        "message": message
    }

    return log

# =========================
# GENERATE DATASET
# =========================
def generate_logs(n=1000):
    start_time = datetime.now() - timedelta(days=7)

    logs = []
    for _ in range(n):
        log = generate_log(start_time)
        logs.append(log)

    return pd.DataFrame(logs)

# =========================
# RUN
# =========================
df = generate_logs(2000)

df.to_csv("network_logs.csv", index=False)

print("✅ Dataset generated: network_logs.csv")
print(df.head())