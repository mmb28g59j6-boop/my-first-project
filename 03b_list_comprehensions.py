# =========================
# 03b_List_Comprehensions.py (BEGINNER)
# =========================

# A list comprehension is a one-line shortcut to build a new list.
# It combines:
# - a loop
# - (optional) an if filter
# - the output list in [brackets]

print("----- 1) BASIC COMPREHENSION (copy values) -----")
nums = [1, 2, 3, 4]
copy_nums = [n for n in nums]
print("nums:", nums)
print("copy_nums:", copy_nums)

print("----- 2) TRANSFORM VALUES -----")
squares = [n * n for n in nums]
print("squares:", squares)

print("----- 3) FILTER VALUES (keep only evens) -----")
evens = [n for n in range(10) if n % 2 == 0]
print("evens:", evens)

print("----- 4) STRINGS: CLEAN + FILTER -----")
words = ["WiFi", "OK", "disconnects", "ERR", "printer"]
lower_long_words = [w.lower() for w in words if len(w) >= 4]
print("lower_long_words:", lower_long_words)

print("----- 5) IT EXAMPLE: FILTER TICKETS -----")
tickets = [
    {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2},
    {"user": "Dano", "issue": "Printer not found", "priority": 1},
    {"user": "Alex", "issue": "Email not syncing", "priority": 1},
    {"user": "Sam", "issue": "VPN setup", "priority": 3},
]

urgent_tickets = [t for t in tickets if t["priority"] == 1]
print("urgent_tickets:", urgent_tickets)

print("----- 6) IT EXAMPLE: EXTRACT FIELDS -----")
urgent_users = [t["user"] for t in tickets if t["priority"] == 1]
print("urgent_users:", urgent_users)

print("----- 7) LOG EXAMPLE: KEEP IMPORTANT LINES -----")
lines = [
    "INFO user logged in",
    "WARN disk space low",
    "ERROR failed login attempt",
    "INFO file uploaded",
    "ERROR database timeout",
]
important_lines = [line for line in lines if line.startswith("WARN") or line.startswith("ERROR")]
print("important_lines:", important_lines)

print("----- EXERCISES (DO THESE) -----")
# Do these one at a time: edit -> save -> run

# EX 1 (easy): Make a list called names with 3 names.
# Use a list comprehension to make a new list called upper_names with all names uppercase.

# EX 2 (easy): From nums = [1,2,3,4,5,6], build a list of only odd numbers.

# EX 3 (easy): From words = ["wifi", "ok", "disconnects", "err"], build a list of words with length >= 3.

# EX 4 (medium): From tickets above, build a list called p2_or_less that keeps tickets with priority 1 or 2.

# EX 5 (medium): From tickets above, build a list called issues that contains only the "issue" text from all tickets.

# EX 6 (harder): From lines above, build a list called error_messages that contains ONLY the text after "ERROR ".
# Example: "ERROR failed login attempt" -> "failed login attempt"

# EX 7 (harder): Make a list called lengths that contains the length of each issue string in tickets.
# Example: len("Wi-Fi disconnects") ...

# EX 8 (harder): From tickets above, build a list of users for tickets where the issue contains "Wi-Fi" (case sensitive).

# EX 9 (harder): From nums = range(1, 21), build a list of numbers divisible by 3 AND divisible by 5.

# EX 10 (harder): Using urgent_tickets, build a list of log lines like:
# "[WARN] user=<user> issue=<issue>"

print("------------------------")

 