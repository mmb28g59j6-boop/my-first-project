
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

print("--------------------")

# List Comprehensions — Quiz (20 Questions)

**Instructions:**

* **Q1–Q10 = Easy**
* **Q11–Q20 = Harder**

---

## Easy (1–10)

1. What is a list comprehension (in one sentence)?

2. What brackets do list comprehensions use?

3. In `[n for n in nums]`, what does the first `n` represent?

4. In `[n for n in nums]`, what does `for n in nums` do?

5. What does this create?

```text
nums = [1, 2, 3]
x = [n for n in nums]
```

6. What does this create?

```text
nums = [1, 2, 3]
x = [n * 2 for n in nums]
```

7. What does the `if` part do in a list comprehension?

8. What is the output of:

```text
evens = [n for n in range(6) if n % 2 == 0]
```

9. What does this do?

```text
words = ["WiFi", "OK", "disconnects"]
x = [w.lower() for w in words]
```

10. Why might you prefer a normal `for` loop instead of a list comprehension?

---

## Harder (11–20)

11. What is the output of:

```text
nums = [10, 20, 30, 40]
x = nums[1:3]
```

(Is this a list comprehension or a slice?)

12. Write a list comprehension that creates squares of 1 through 5.

13. Write a list comprehension that keeps only numbers greater than 10 from:
    `nums = [5, 12, 3, 25, 10, 11]`

14. Given:
    `tickets = [{"user":"A","priority":1},{"user":"B","priority":2}]`
    Write a list comprehension that returns only the users.

15. Given:
    `lines = ["INFO ok", "ERROR bad", "WARN low"]`
    Write a list comprehension that keeps only WARN and ERROR lines.

16. Given:
    `words = ["wifi", "ok", "disconnects"]`
    Write a list comprehension that returns word lengths: `[4, 2, 11]`

17. Given:
    `lines = ["ERROR failed login", "ERROR db timeout"]`
    Write a list comprehension that returns:
    `["failed login", "db timeout"]`

18. Write a list comprehension using `range(1, 21)` that returns numbers divisible by 3 and 5.

19. Write a list comprehension that converts:
    `["1", "2", "3"]` into `[1, 2, 3]`

20. Explain (one sentence) why list comprehensions can be harder to read if they get too long.
