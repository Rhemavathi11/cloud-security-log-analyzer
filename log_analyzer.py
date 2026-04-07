from datetime import datetime, timedelta

ip_count = {}

# current time (simulate)
current_time = datetime.strptime("2026-04-07 10:06:00", "%Y-%m-%d %H:%M:%S")

# Read logs
with open("logs.txt", "r") as file:
    logs = file.readlines()

for log in logs:
    parts = log.strip().split(" - ")
    
    timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
    ip = parts[1]
    message = parts[2]

    # check only last 5 minutes
    if current_time - timestamp <= timedelta(minutes=5):
        if "Failed login" in message:
            if ip in ip_count:
                ip_count[ip] += 1
            else:
                ip_count[ip] = 1

print("Recent Failed Login Attempts:")
for ip, count in ip_count.items():
    print(ip, ":", count)

print("\n🚨 Suspicious IPs (last 5 minutes):")
for ip, count in ip_count.items():
    if count > 2:
        print(ip, "→ ALERT!")

# save report
with open("report.txt", "w", encoding="utf-8") as report:
    report.write("Recent Failed Login Attempts:\n")
    for ip, count in ip_count.items():
        report.write(f"{ip} : {count}\n")

    report.write("\n🚨 Suspicious IPs (last 5 minutes):\n")
    for ip, count in ip_count.items():
        if count > 2:
            report.write(f"{ip} → ALERT!\n")

print("\n✅ Report generated with timestamp filtering")