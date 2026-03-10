# =========================
# 06_loops.py (BEGINNER)
# =========================

# Loops repeat work.
# Use for-loops to process items.
# Use while-loops to repeat until a condition changes.

print("----- FOR LOOP WITH LIST -----")
tools = ["VS Code", "Python", "Terminal"]

for tool in tools:
    print("TOOL:", tool)

print("----- RANGE LOOP -----")
for i in range(1, 6):
    print("i =", i)

print("----- STRING LOOP (characters) -----")
text = "ABC"
for ch in text:
    print("char:", ch)

print("----- IT EXAMPLE: LOOP THROUGH TICKETS (LIST) -----")
tickets = [
    {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2},
    {"user": "Dano", "issue": "Printer not found", "priority": 1},
    {"user": "Alex", "issue": "Email not syncing", "priority": 3},
]

for t in tickets:
    print(f"TICKET user={t['user']} issue={t['issue']} priority={t['priority']}")

print("----- IF + LOOP (flag urgent) -----")
for t in tickets:
    if t["priority"] == 1:
        print(f"[WARN] urgent ticket for {t['user']}: {t['issue']}")
    else:
        print(f"[INFO] normal ticket for {t['user']}")

print("----- WHILE LOOP (counting) -----")
count = 0
while count < 3:
    print("count:", count)
    count += 1

print("----- BREAK EXAMPLE -----")
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n == 3:
        break
    print("n:", n)

print("----- CONTINUE EXAMPLE -----")
for n in nums:
    if n == 3:
        continue
    print("n:", n)

print("----- EXERCISES (edit the code) -----")

# EX 1: Make a list called names with 3 names and loop through it printing:
# NAME: <name>

# EX 2: Use range() to print numbers 10 to 15

# EX 3: Make a list of 3 ticket issues (strings) and loop through printing:
# TICKET: <issue>

# EX 4: Ask the user for a number with input(), convert it to int,
# and use a while loop to count from 0 up to that number.

# EX 5 (IT style): Using the tickets list above,
# count how many tickets have priority 1 and print the total.