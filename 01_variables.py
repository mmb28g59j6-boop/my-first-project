# =========================
# variables.py (BEGINNER)
# =========================

# 1) A variable is a name that stores a value.
name = "Dano"
birth_date = "April 29, 1991"
age = 34
is_student = True
favorite_app = "VS Code"

print("Name:", name)
print("Birth date:", birth_date)
print("Age:", age)
print("Student:", is_student)
print("Favorite app:", favorite_app)

print("-----")

# Practice: using variables + math + f-strings
age_next_year = age + 1
print("Next year I will be:", age_next_year)
print(f"I was born on {birth_date} and I am {age} years old.")

print("-----")

# 2) Python has different "types" of values.
# int = whole number, float = decimal, str = text, bool = True/False

score = 10          # int
price = 19.99       # float
city = "Sault Ste Marie"    # str
is_online = False   # bool

print("score =", score, "type =", type(score))
print("price =", price, "type =", type(price))
print("city  =", city,  "type =", type(city))
print("online=", is_online, "type =", type(is_online))

print("-----")

# 3) You can change (reassign) a variable.
points = 5
print("points before:", points)

points += 1 
print("points after +1:", points)

points += 1
print("points after +1 again:", points)

print("-----")

# 4) Math with variables
double_age = age * 2
print("double_age:", double_age)

# 5) Combining text with variables
# Best way: f-strings
print(f"{name} is {age} years old and lives in {city}.")

print("-----")

# 6) Getting user input (input is always TEXT at first)
user_age = input("Enter your age: ")
print("You typed:", user_age)
print("Type of user_age is:", type(user_age))

# Convert text to a number
user_age = int(user_age)
print("Next year you will be:", user_age + 1)

print("-----")

# 7) Small practice: ticket example (IT support style)
user = "Maria"
issue = "Wi-Fi disconnects"
priority = 2

print(f"TICKET -> user: {user}, issue: {issue}, priority: {priority}")


print("----- EXTRA BASICS -----")

# Naming style (snake_case)
user_name = "Dano"

# Constant convention (not enforced, but common)
MAX_RETRIES = 3

# None means "no value yet"
middle_name = None
print("middle_name:", middle_name, "type:", type(middle_name))

# Containers preview (you'll learn these next)
tools = ["VS Code", "Python", "Terminal"]          # list []
ticket = {"user": user, "issue": issue}           # dict {}
print("First tool:", tools[0])
print("Ticket user:", ticket["user"])

