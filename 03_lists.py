# =========================
# 03_Lists.py (BEGINNER)
# =========================

# A LIST is a collection of items stored in order.
# Lists use square brackets: [ ]

tools = ["VS Code", "Python", "Terminal"]
print("tools:", tools)
print("type(tools):", type(tools))

print("-----")

# 1) Indexing (getting one item)
# Python starts counting at 0
print("First tool:", tools[0])
print("Second tool:", tools[1])
print("Last tool:", tools[-1])

print("-----")

# 2) Length (how many items)
print("Number of tools:", len(tools))

print("-----")

# 3) Add items
tools.append("Git")
print("After append:", tools)

print("-----")

# 4) Remove items
tools.remove("Python")
print("After remove:", tools)

print("-----")

# 5) Update an item (change by index)
tools[1] = "Wireshark"
print("After update:", tools)

print("-----")

# 6) Loop through a list
print("Looping through tools:")
for item in tools:
    print("-", item)

print("-----")

# 7) split() creates a list of words
sentence = "wifi disconnects often"
words = sentence.split()
print("words:", words)
print("First word:", words[0])
print("Third word:", words[2])

print("-----")

# 8) IT support example: list of ticket issues
tickets = [
    "Wi-Fi disconnects",
    "Printer not found",
    "Password reset needed"
]
print("tickets:", tickets)
print("First ticket:", tickets[0])

print("-----")
print("EXERCISES (do these by editing the code)")
print("-----")

# EX 1: Add a new ticket to tickets using append()
# tickets.append("Email not syncing")

# EX 2: Print the last ticket using [-1]

# EX 3: Change the second ticket to "Email not syncing"

# EX 4: Loop through tickets and print each one like:
# TICKET: <issue>

# EX 5: Make a new list named numbers with 3 numbers and print:
# - the list
# - the first number
# - how many numbers total



# =========================
# MINI EXERCISES (DO THEM)
# =========================

# 1) Create a list named apps with 3 apps you use (strings) and print it.

# 2) Print the first and last item from apps using [0] and [-1].

# 3) Add one more app using append(), then print the updated list.

# 4) Remove one app using remove(), then print the updated list.

# 5) Loop through apps and print:
# APP: <name>