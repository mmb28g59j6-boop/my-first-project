# 06_Loops — README (Comprehensive + Beginner Reference)

This page explains **loops**, which let you repeat code.

* `for` loops: repeat over items (lists, strings, ranges)
* `while` loops: repeat while a condition stays True

---

## 1) What a loop is

A loop repeats work so you don’t copy/paste the same code 50 times.

Examples in IT:

* process many tickets
* scan many log lines
* check many users/devices

---

## 2) `for` loops (most common)

A `for` loop walks through a collection.

```text id="g6y2p2"
tools = ["VS Code", "Python", "Terminal"]

for tool in tools:
    print(tool)
```

### Looping through a string (character by character)

```text id="q9k3d5"
text = "ABC"
for ch in text:
    print(ch)
```

---

## 3) `range()` (loop a number of times)

`range(n)` goes from 0 up to (not including) n.

```text id="f0m6p3"
for i in range(5):
    print(i)   # 0 1 2 3 4
```

Start/stop/step:

```text id="s1j6k8"
for i in range(1, 6):
    print(i)   # 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)   # 0 2 4 6 8
```

---

## 4) `while` loops

A `while` loop repeats as long as a condition is True.

```text id="p2f4c1"
count = 0
while count < 3:
    print("count:", count)
    count += 1
```

**Important:** If you forget to update the variable, you can create an infinite loop.

---

## 5) `break` and `continue`

### `break` stops the loop completely

```text id="u7h9x1"
for n in [1, 2, 3, 4]:
    if n == 3:
        break
    print(n)
```

### `continue` skips to the next loop turn

```text id="f9b3v6"
for n in [1, 2, 3, 4]:
    if n == 3:
        continue
    print(n)
```

---

## 6) Looping through dictionaries

Loop keys:

```text id="v5k2c6"
ticket = {"user": "Maria", "priority": 2}
for key in ticket:
    print(key)
```

Loop key/value:

```text id="x4d1r7"
for key, value in ticket.items():
    print(key, "=", value)
```

---

## 7) Nested loops (harder, but common)

A loop inside a loop.

Example: scan multiple users, each with multiple tickets.

```text id="n9c2r4"
users = ["Maria", "Dano"]
issues = ["Wi-Fi", "Printer"]

for u in users:
    for issue in issues:
        print(u, issue)
```

---

## 8) Common beginner mistakes

* Forgetting indentation
* Using the wrong variable name
* Infinite `while` loops (forgot to update)
* Off-by-one with `range()` (it stops before the end)

---

# Quick Cheat Sheet (Loops)

## for

* `for item in items:`
* `for i in range(n):`
* `for i in range(start, stop, step):`

## while

* `while condition:`

## control

* `break` stops loop
* `continue` skips iteration

print("-------------------------")

# 06_Loops — Quiz (20 Questions)

**Instructions:** Answer in short form.

* **Q1–Q10 = Easy**
* **Q11–Q20 = Harder**

---

## Easy (1–10)

1. What is a loop in Python?

2. Name the two main loop types in Python.

3. Write a `for` loop that prints each item in `tools = ["VS Code", "Python", "Terminal"]`.

4. What does `range(5)` produce (list the numbers)?

5. What does `range(1, 6)` produce?

6. What does `range(0, 10, 2)` produce?

7. What is the purpose of a `while` loop?

8. What is the most common cause of an infinite `while` loop?

9. What does `break` do in a loop?

10. What does `continue` do in a loop?

---

## Harder (11–20)

11. What will this print?

```text id="3j9qz7"
for i in range(3):
    print(i)
```

12. What will this print?

```text id="2j1b4m"
count = 0
while count < 3:
    print(count)
    count += 1
```

13. Write a `for` loop that prints numbers 10 to 15 using `range()`.

14. Given `tickets = ["Wi-Fi", "Printer", "Email"]`, write code that prints:
    `TICKET #1: Wi-Fi`, `TICKET #2: Printer`, etc. (numbers start at 1).

15. What is the difference between looping over a list vs looping over a string?

16. Given `ticket = {"user": "Maria", "priority": 2}`, write a loop that prints:
    `user = Maria` and `priority = 2`.

17. Write code that counts how many items are in `nums = [1, 2, 3, 4]` using a loop (don’t use `len()`).

18. What will this print?

```text id="6p1tcd"
nums = [1, 2, 3, 4]
for n in nums:
    if n == 3:
        continue
    print(n)
```

19. What will this print?

```text id="1k1nvc"
nums = [1, 2, 3, 4]
for n in nums:
    if n == 3:
        break
    print(n)
```

20. (Nested loops) What will this print?

```text id="l2r0gr"
users = ["Maria", "Dano"]
issues = ["Wi-Fi", "Printer"]

for u in users:
    for issue in issues:
        print(u, issue)
```
