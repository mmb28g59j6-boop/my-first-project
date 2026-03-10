# 07_Functions — README (Comprehensive + Beginner Reference)

Functions let you **reuse code**. Instead of copy/pasting the same logic, you write it once and call it whenever you need it.

Why functions matter in IT/cyber:

* format consistent log lines
* validate user input
* reuse ticket parsing and filtering
* keep scripts organized and readable

---

## 1) What a function is

A function is a named block of code you can run later.

* **Define** with `def`
* **Call** by writing `name(...)`

```text id="1l2p4p"
def greet():
    print("Hello!")

greet()
```

---

## 2) Parts of a function

### A) Function name

A label you choose:

* use snake_case: `build_ticket_log`

### B) Parameters (inputs)

Values a function receives.

```text id="m5q8w1"
def greet(name):
    print("Hello", name)

greet("Dano")
```

* `name` is a **parameter**
* `"Dano"` is an **argument** (the actual value you pass in)

---

## 3) Return values (`return`)

`return` sends a value back to where the function was called.

```text id="o3p2a8"
def add_one(n):
    return n + 1

x = add_one(5)   # x becomes 6
```

### `print` vs `return`

* `print()` displays something
* `return` gives back a value for later use

---

## 4) Default values (optional parameters)

```text id="t2y7m9"
def greet(name="Friend"):
    print("Hello", name)

greet()          # Hello Friend
greet("Dano")    # Hello Dano
```

---

## 5) Scope (local vs global)

Variables inside a function are usually **local** (they exist only in the function).

```text id="p6y3c2"
def demo():
    x = 10
    print(x)

demo()
# print(x)  # NameError (x is local)
```

---

## 6) Returning multiple values

Python can return multiple values (as a tuple).

```text id="g3p8h4"
def stats(a, b):
    return a + b, a * b

total, product = stats(2, 3)
```

---

## 7) Functions + lists/dicts (very common)

Example: format a ticket stored as a dictionary:

```text id="r1n7b8"
def ticket_log(ticket):
    return f"[TICKET] user={ticket['user']} issue={ticket['issue']} priority={ticket['priority']}"
```

Then use it in a loop over many tickets.

---

## 8) Common beginner mistakes (and fixes)

### Mistake A: Forgetting to call the function

Defining does nothing until you call it.

```text id="y9h1z2"
def greet():
    print("Hello")
# greet  (does nothing)
greet()   # correct
```

### Mistake B: Missing required arguments

```text id="a1b2c3"
def greet(name):
    print(name)

greet()   # TypeError
```

Fix: call `greet("Dano")` or use a default.

### Mistake C: Returning vs printing confusion

If you need a value later, use `return`.

---

# Quick Cheat Sheet (Functions)

## Define

* `def name(params):`
* indent the body

## Call

* `name(args)`

## Return

* `return value`

## Defaults

* `def f(x=10):`

## Typical IT use

* build log strings
* validate input
* reuse parsing logic

print("--------------------------")

# 07_Functions — Quiz (20 Questions)

**Instructions:**

* **Q1–Q10 = Easy**
* **Q11–Q20 = Harder**

---

## Easy (1–10)

1. What is a function in Python?

2. What keyword do you use to define a function?

3. What does it mean to “call” a function?

4. Write a function named `greet()` that prints `"Hello"`.

5. What are parameters?

6. What are arguments?

7. What does `return` do?

8. What is the difference between `print()` and `return`?

9. What does this return?

```text
def add_one(n):
    return n + 1
```

10. What happens if you define a function but never call it?

---

## Harder (11–20)

11. What will this print?

```text
def f():
    return 10

print(f())
```

12. What will this print?

```text
def f():
    print(10)

print(f())
```

13. What is a default parameter? Give an example.

14. What is “scope” (local vs global) in simple terms?

15. What error do you get if you call a function without required arguments?

16. Write a function `is_even(n)` that returns True if n is even.

17. Write a function that takes a ticket dictionary and returns a log string like:
    `user=<user> issue=<issue> priority=<priority>`

18. Write a function `count_high_priority(tickets)` that counts how many tickets have priority 1.

19. What’s one benefit of functions for IT scripts?

20. Explain in one sentence why functions help you avoid copy/paste problems.
