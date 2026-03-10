# 05_if_statements — README (Comprehensive + Beginner Reference)

This page explains **control flow** using `if / elif / else`, comparisons, and logical operators.
Control flow means: **your program can make decisions** instead of running every line the same way.

---

## 1) What `if` does (the idea)

An `if` statement checks a condition:

* If the condition is **True**, Python runs the indented block.
* If **False**, Python skips it.

```text id="h8s1w8"
priority = 1

if priority == 1:
    print("High priority")
```

---

## 2) Indentation is mandatory in Python

Python uses indentation (spaces) to show which lines belong to the `if`.

✅ Correct:

```text id="0b7m8t"
if True:
    print("Runs")
```

❌ Wrong (no indentation):

```text id="g1v7df"
if True:
print("Error")
```

---

## 3) `if / else`

Use `else` for the “otherwise” case:

```text id="1o3xv9"
priority = 2

if priority == 1:
    print("High")
else:
    print("Not high")
```

---

## 4) `if / elif / else` (multiple choices)

Use `elif` for extra checks:

```text id="kfev8u"
priority = 2

if priority == 1:
    print("High")
elif priority == 2:
    print("Medium")
else:
    print("Low")
```

**Rule:** Python checks from top to bottom and runs the **first match**.

---

## 5) Comparison operators (how conditions are built)

These return `True` or `False`:

* `==` equal
* `!=` not equal
* `>` greater than
* `<` less than
* `>=` greater or equal
* `<=` less or equal

Examples:

```text id="8k3x5l"
age = 34
print(age == 34)   # True
print(age != 10)   # True
print(age > 18)    # True
print(age <= 40)   # True
```

---

## 6) Logical operators: `and`, `or`, `not`

### `and` (both must be True)

```text id="u0l7y9"
if failed_logins >= 3 and ip.startswith("192.168"):
    print("Alert")
```

### `or` (either can be True)

```text id="rj3n4e"
if priority == 1 or priority == 2:
    print("Needs fast response")
```

### `not` (flip True/False)

```text id="q1g6xf"
is_online = False
if not is_online:
    print("Device is offline")
```

---

## 7) Membership checks: `in` / `not in`

Works with lists, strings, dictionaries.

```text id="q2o4d1"
tools = ["VS Code", "Python"]
if "Python" in tools:
    print("Installed")
```

For strings:

```text id="9c8c1p"
msg = "wifi disconnects often"
if "wifi" in msg:
    print("Wi-Fi issue")
```

For dictionaries: checks keys

```text id="q9t1bx"
ticket = {"user": "Maria", "priority": 1}
if "user" in ticket:
    print("Has user key")
```

---

## 8) Common IT support decision patterns

### A) Priority-based logging

```text id="t4y1m8"
ticket = {"user": "Maria", "issue": "Wi-Fi", "priority": 1}

if ticket["priority"] == 1:
    print("[WARN] urgent ticket")
else:
    print("[INFO] normal ticket")
```

### B) Safety check before accessing a dict key

```text id="z7b3w2"
if "status" in ticket:
    print(ticket["status"])
else:
    print("No status set")
```

---

## 9) Common beginner mistakes (and fixes)

### Mistake A: Using `=` instead of `==`

* `=` assigns
* `==` compares

❌ Wrong:

```text id="r5x2a0"
if priority = 1:
    print("no")
```

✅ Right:

```text id="e8t1m9"
if priority == 1:
    print("yes")
```

### Mistake B: Comparing different types

`input()` returns text, so convert if needed.

```text id="s2d8c8"
age_text = input("Age: ")
age = int(age_text)
if age >= 18:
    print("Adult")
```

### Mistake C: Indentation errors

Make sure your block is indented consistently (usually 4 spaces).

---

# Quick Cheat Sheet (If Statements)

## Structure

* `if condition:`
* `elif condition:`
* `else:`

## Comparisons

* `== != > < >= <=`

## Logic

* `and` / `or` / `not`

## Useful checks

* `"x" in list_or_string_or_dict`
* `"key" in dict` (checks keys)

print("-------------------------")

# 05_If_Statements — Quiz (20 Questions)

**Instructions:** Answer in short form.

* **Q1–Q10 = Easy**
* **Q11–Q20 = Harder**

---

## Easy (1–10)

1. What is “control flow” in Python?

2. What keyword starts a basic decision statement?

3. Write a simple `if` statement that prints `"Hello"` if `x` equals 5.

4. What does `==` mean?

5. What does `!=` mean?

6. If `age = 20`, is `age >= 18` True or False?

7. What does `else` do?

8. What does `elif` do?

9. What will this print?

```text id="1z6l1p"
priority = 2
if priority == 1:
    print("HIGH")
elif priority == 2:
    print("MEDIUM")
else:
    print("LOW")
```

10. What does indentation mean in an `if` statement?

---

## Harder (11–20)

11. What is the difference between `=` and `==`?

12. What will this print?

```text id="7w4f3t"
x = 10
if x > 5 and x < 20:
    print("IN RANGE")
else:
    print("OUT OF RANGE")
```

13. What will this print?

```text id="7uxy6v"
x = 3
if x == 1 or x == 3:
    print("MATCH")
else:
    print("NO MATCH")
```

14. What does `not` do? Give a simple example.

15. If `ticket = {"user": "Maria"}`, what happens if you run `ticket["priority"]`?

16. How do you safely get `"priority"` from the ticket above without crashing?

17. What does `"wifi" in "wifi disconnects often"` evaluate to (True/False)?

18. What does `"Python" in ["VS Code", "Python", "Terminal"]` evaluate to (True/False)?

19. Write an `if` statement that prints `"ALERT"` if `failed_logins` is 3 or more.

20. Write an `if/elif/else` that prints:

* `"HIGH"` if `priority` is 1
* `"MEDIUM"` if `priority` is 2
* `"LOW"` for anything else
