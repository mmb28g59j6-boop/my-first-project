# =========================
# 04_Dictionaries.py (BEGINNER)
# =========================

# A DICTIONARY stores key/value pairs.
# Dictionaries use curly braces: { }

ticket = {
    "user": "Maria",
    "issue": "Wi-Fi disconnects",
    "priority": 2,
    "device": "MacBook Air"
}

print("ticket:", ticket)
print("type(ticket):", type(ticket))

print("-----")

# 1) Get values using keys
print("User:", ticket["user"])
print("Issue:", ticket["issue"])
print("Priority:", ticket["priority"])

print("-----")

# 2) Add a new key/value
ticket["status"] = "Open"
print("After adding status:", ticket)

print("-----")

# 3) Update a value
ticket["priority"] = 1
print("After updating priority:", ticket)

print("-----")

# 4) Loop through keys and values
for key, value in ticket.items():
    print(key, "=", value)

print("-----")

# 5) IT example: multiple tickets (list of dictionaries)
tickets = [
    {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2},
    {"user": "Dano", "issue": "Printer not found", "priority": 1},
]

for t in tickets:
    print(f"TICKET user={t['user']} issue={t['issue']} priority={t['priority']}")

 