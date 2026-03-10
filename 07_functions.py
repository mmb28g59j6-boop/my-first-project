# =========================
# 07_functions.py (BEGINNER)
# =========================

print("----- 1) BASIC FUNCTION -----")

def greet():
    print("Hello!")

greet()

print("----- 2) FUNCTION WITH PARAMETER -----")

def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Dano")
greet_name("Maria")

print("----- 3) FUNCTION THAT RETURNS A VALUE -----")

def add_one(n):
    return n + 1

result = add_one(34)
print("add_one(34) =", result)

print("----- 4) DEFAULT PARAMETER -----")

def greet_with_default(name="Friend"):
    print(f"Hello, {name}!")

greet_with_default()
greet_with_default("Dano")

print("----- 5) IT EXAMPLE: BUILD A TICKET LOG LINE -----")

def build_ticket_log(user, issue, priority):
    return f"[TICKET] user={user} issue={issue} priority={priority}"

log1 = build_ticket_log("Maria", "Wi-Fi disconnects", 2)
log2 = build_ticket_log("Dano", "Printer not found", 1)

print(log1)
print(log2)

print("----- 6) FUNCTION THAT TAKES A DICTIONARY -----")

def ticket_log(ticket):
    return f"[TICKET] user={ticket['user']} issue={ticket['issue']} priority={ticket['priority']}"

ticket_a = {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2}
ticket_b = {"user": "Dano", "issue": "Printer not found", "priority": 1}

print(ticket_log(ticket_a))
print(ticket_log(ticket_b))

print("----- 7) USE A FUNCTION IN A LOOP -----")

tickets = [
    {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2},
    {"user": "Dano", "issue": "Printer not found", "priority": 1},
    {"user": "Alex", "issue": "Email not syncing", "priority": 3},
]

for t in tickets:
    print(ticket_log(t))

print("----- 8) EXERCISES (edit the code) -----")

# EX 1: Write a function named multiply(a, b) that returns a * b.
# Print multiply(3, 4)

# EX 2: Write a function named is_urgent(priority) that returns True if priority == 1 else False.
# Test it with 1 and 2.

# EX 3: Write a function named format_log(severity, message) that returns:
# "[SEVERITY] message=<message>"
# Example: format_log("INFO", "Wi-Fi ok")

# EX 4: Using the tickets list above, write a function named count_urgent(tickets)
# that returns how many tickets have priority 1.

# EX 5: Write a function named safe_get(ticket, key, default)
# that returns ticket[key] if the key exists, otherwise returns default.