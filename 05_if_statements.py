# =========================
# 05_if_statements.py (BEGINNER)
# =========================

# if / elif / else lets your code make decisions

priority = 2

if priority == 1:
    print("HIGH priority ticket")
elif priority == 2:
    print("MEDIUM priority ticket")
else:
    print("LOW priority ticket")

print("-----")

# Comparisons
age = 34
print(age == 34)   # equals
print(age != 10)   # not equal
print(age > 18)    # greater than
print(age >= 34)   # greater or equal
print(age < 50)    # less than

print("-----")

# IT example using a dictionary
ticket = {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 1}

if ticket["priority"] == 1:
    print(f"[WARN] urgent ticket for {ticket['user']}: {ticket['issue']}")
else:
    print(f"[INFO] normal ticket for {ticket['user']}: {ticket['issue']}")

print("-----")

# Combine conditions with and/or
failed_logins = 4
ip = "192.168.1.45"

if failed_logins >= 3 and ip.startswith("192.168"):
    print(f"[ALERT] suspicious activity from {ip} ({failed_logins} fails)")