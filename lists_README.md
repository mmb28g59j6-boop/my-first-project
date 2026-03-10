# 03_Lists — README (Beginner + Reference)

This page explains **lists** in Python (`list`): how to create them, read items, change items, add/remove items, and loop through them. Lists use square brackets: `[ ]`.

---

## 1) What is a list?

A **list** is an ordered collection of items.

```text id="w9mdzj"
tools = ["VS Code", "Python", "Terminal"]
```

A list can hold:

* strings
* numbers
* booleans
* even other lists (later)

---

## 2) Why lists matter (real-world)

Lists are everywhere in scripting:

* a list of files to process
* a list of users to reset passwords for
* a list of IPs to block
* a list of ticket issues
* words from a sentence (from `split()`)

---

## 3) Indexing (getting an item)

Python starts counting at **0**.

```text id="agqook"
tools = ["VS Code", "Python", "Terminal"]
print(tools[0])   # "VS Code" (first item)
print(tools[1])   # "Python"  (second item)
```

### Negative indexing

`-1` means “last item”.

```text id="3pmf6g"
print(tools[-1])  # "Terminal"
```

---

## 4) Length of a list: `len()`

```text id="dw4p3f"
print(len(tools))   # 3
```

---

## 5) Adding items: `append()`

Adds an item to the end.

```text id="1b23o2"
tools.append("Git")
```

---

## 6) Removing items

### A) `remove(value)`

Removes the first matching value.

```text id="q9zli7"
tools.remove("Python")
```

If the value isn’t found, you get an error.

### B) `pop(index)` (optional but common)

Removes and returns an item.

```text id="d8w9tq"
last_item = tools.pop()     # removes last by default
first_item = tools.pop(0)   # removes item at index 0
```

---

## 7) Updating items (change by index)

```text id="fmlqkc"
tools[1] = "Wireshark"
```

---

## 8) Looping through a list (very important)

Use a `for` loop to process each item.

```text id="3txmmr"
for item in tools:
    print(item)
```

---

## 9) Lists from strings: `split()`

`split()` turns a string into a list of words.

```text id="fp1wke"
sentence = "wifi disconnects often"
words = sentence.split()
print(words)      # ['wifi', 'disconnects', 'often']
print(words[0])   # wifi
```

---

# Quick Cheat Sheet (Lists)

## Create

* `items = []`
* `items = ["a", "b", "c"]`

## Read

* `items[0]` (first)
* `items[-1]` (last)
* `len(items)` (how many)

## Change

* `items[1] = "new value"`

## Add / Remove

* `items.append("x")`
* `items.remove("x")`
* `items.pop()` or `items.pop(0)`

## Loop

* `for x in items:`

---

## Common mistakes (and fixes)

### Mistake A: IndexError (out of range)

```text id="e9i7y9"
tools = ["VS Code"]
print(tools[2])   # ERROR
```

Fix: check `len(tools)` first.

### Mistake B: Confusing “item” vs “index”

* `tools[1]` is the item at position 1
* `1` is the index (second item)

---

## Mini Reference Example (IT Support style)

```text id="6vma3k"
tickets = ["Wi-Fi disconnects", "Printer not found", "Password reset needed"]

tickets.append("Email not syncing")
print("Last ticket:", tickets[-1])

for issue in tickets:
    print("TICKET:", issue)
```

---

## List Comprehensions (Beginner + Definitive)

### What is a list comprehension?

A **list comprehension** is a **one-line shortcut** that:

* loops through items (like a `for` loop)
* optionally filters items (like an `if`)
* builds a **new list**

Think of it as: **“a loop inside square brackets that creates a list.”**

---

### The basic pattern (memorize this)

```text
new_list = [expression for item in iterable]
```

* `iterable` = something you can loop through (list, string, range)
* `item` = the temporary variable name (like `n`, `word`, `ticket`)
* `expression` = what you want to put in the new list

---

### Example 1: Make squares (simple)

```text
nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
```

Result:

* `squares` becomes `[1, 4, 9, 16]`

**Long (beginner) version:**

```text
squares = []
for n in nums:
    squares.append(n * n)
```

---

### The filter pattern (with `if`)

```text
new_list = [expression for item in iterable if condition]
```

### Example 2: Keep only even numbers

```text
evens = [n for n in range(10) if n % 2 == 0]
```

Result:

* `[0, 2, 4, 6, 8]`

**Long version:**

```text
evens = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
```

---

## Understanding the parts (super simple)

### What does `n` mean?

`n` is just a temporary variable name.
It takes each value one-by-one as the loop runs.

You could write:

```text
evens = [number for number in range(10) if number % 2 == 0]
```

Same result. `n` is just shorter.

---

## IT Support examples (very practical)

### Example 3: Keep only urgent tickets (priority 1)

```text
tickets = [
  {"user": "Maria", "priority": 2},
  {"user": "Dano", "priority": 1},
  {"user": "Alex", "priority": 1}
]

urgent = [t for t in tickets if t["priority"] == 1]
```

Result: a list containing only the priority 1 ticket dictionaries.

### Example 4: Extract just the users from urgent tickets

```text
urgent_users = [t["user"] for t in tickets if t["priority"] == 1]
```

Result:

* `["Dano", "Alex"]`

### Example 5: Keep only ERROR/WARN log lines

```text
lines = ["INFO ok", "WARN disk low", "ERROR failed login"]
important = [line for line in lines if line.startswith("WARN") or line.startswith("ERROR")]
```

---

## When to use list comprehensions (Beginner rule)

Use them when:

* it’s **short**
* it’s **easy to read**
* it’s doing one clear thing

Avoid them when:

* the logic is long/complex
* you need multiple steps inside the loop
  In that case, use a normal `for` loop.

---

## Common mistakes

### Mistake 1: Forgetting the brackets

List comprehensions must use `[]`.

### Mistake 2: Trying to cram too much logic

If it gets hard to read, switch to a normal loop.

### Mistake 3: Confusing the output type

A list comprehension always produces a **list**.

---

## Mini Cheat Sheet

* Basic: `[x for x in items]`
* Transform: `[x * 2 for x in items]`
* Filter: `[x for x in items if x > 0]`
* Filter + transform: `[x.upper() for x in words if len(x) > 3]`


--------------------------------------------------

## Lists Self-Test (10)

1. What is a list? Give one example of a list with 3 items.

2. In a list, what index number is the **first** item?

3. If `tools = ["VS Code", "Python", "Terminal"]`, what is:

* `tools[0]`
* `tools[2]`
* `tools[-1]`

4. What does `len(tools)` return for the list above?

5. What does `.append()` do? Where does the new item go?

6. What does `.remove("Python")` do? What happens if `"Python"` is not in the list?

7. What does `.pop()` do? What is the difference between:

* `tools.pop()`
* `tools.pop(0)`

8. How do you change the second item in a list to `"Wireshark"`?

9. Write a `for` loop that prints every item in `tools` with a dash in front of it.

10. If `sentence = "wifi disconnects often"`, what does `sentence.split()` return, and what is `words[1]` after splitting?

-------------------------------------------------------------

# 03_Lists — Quiz (20 Questions)

**Instructions:** Answer in short form.

* **Q1–Q10 = Easy**
* **Q11–Q20 = A bit harder**

---

## Easy (1–10)

1. What is a list in Python?

2. Which brackets do lists use: `()`, `[]`, or `{}`?

3. Create a list named `colors` with 3 items: red, blue, green.

4. If `colors = ["red", "blue", "green"]`, what is `colors[0]`?

5. For the same list, what is `colors[2]`?

6. For the same list, what is `colors[-1]`?

7. What does `len(colors)` return for that list?

8. What does `append()` do?

9. What does `remove()` do?

10. Write a `for` loop that prints every item in `colors`.

---

## Harder (11–20)

11. If `nums = [10, 20, 30, 40]`, what does `nums[1:3]` return? # [20, 30]

12. If `text = "wifi disconnects often"`, what does `text.split()` return?

13. If `words = ["wifi", "disconnects", "often"]`, what is the difference between:

* `words[0]` # (wifi)
* `words[0][2]` # (f)

14. What’s the difference between `pop()` and `remove()`?

15. What happens if you run `colors.remove("purple")` and `"purple"` is not in the list?  # ValueError

16. How do you change the second item in `colors` to `"yellow"`?

17. Write code that creates an empty list named `tickets`, then adds 3 ticket issues using `append()`.

tickets = []
tickets.append("Wifi Disconnects Often")
tickets.append("Printer Not Found")
tickets.append("Email Not Syncing")
print(tickets)

18. Write a loop that prints tickets like this:
    `TICKET #1: <issue>` (numbers should start at 1)

19. Given `tools = ["VS Code", "Python", "Terminal", "Git"]`, write code that prints:

* the first 2 items as a slice
* the last 2 items as a slice

20. Given `nums = [5, 2, 9, 1]`, write code that sorts the list in ascending order.