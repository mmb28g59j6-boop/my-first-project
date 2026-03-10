# =========================
# 02_Strings.py (BEGINNER)
# =========================

# Strings are TEXT in quotes: "..." or '...'
text = "Hello World"
city = "Sault Ste Marie"
course = "Python Fundamentals"

print("text:", text)
print("city:", city)
print("course:", course)
print("type(text):", type(text))

print("-----")

# 1) Length (how many characters)
print("Length of text:", len(text))

# 1) Example of Counting Characters of Sault Ste Marie
print("City length:", len(city))

print("-----")

# 2) Upper/lower (common cleanup)
print(text.upper())
print(text.lower())

# 2) Example Fix capitalization
msg = "wiFI is disCoNnEcTiNg"
print(msg.lower())

print("-----")

# 3) Combine strings
first = "Dano"
last = "Ruttan"
full_name = first + " " + last
print("Full name:", full_name)

print("-----")

# 4) f-strings (best way to combine text + variables)
age = 34
print(f"{full_name} is {age} years old and lives in {city}.")

print("-----")

# 5) Indexing (getting characters) 0 = first character
print("First character of text:", text[0])
print("Last character of text:", text[-1])

# 5) Example of indexing 1st and 3rd character of text
print(text[0])
print(text[2])

print("-----")

# 6) Slicing (getting part of a string)
print("First 5 characters:", text[0:5])  # Hello

# 6) Example of Slicing
print(text[6:11])

print("-----")

# 7) split() turns a string into a list of words
sentence = "wifi disconnects often"
words = sentence.split()
print("words:", words)

# 7) Example of Split first word and third
words = sentence.split()
print("First word:", words[0])
print("Third word:", words[2])


print("-----")

# 8) replace() swaps text (very common)
fixed = sentence.replace("wifi", "Wi-Fi")
print("fixed sentence:", fixed)

# 8) Example of Replace Multiple Words
alert = "wifi disconnects often"
alert = alert.replace("wifi", "Wi-Fi").replace("often", "a lot")
print(alert)

# 9) Builld a IT Log message with f_string
device = "MacBook Air"
issue = "wifi disconnects"
log = f"[INFO] device={device} issue=wifi city={city}"
print(log)

# Upgrade 9) (add severity + ticket number)
severity = "WARN"
ticket_id = 1024
log = f"[{severity}] ticket={ticket_id} device={device} issue={issue} city={city}"
print(log)