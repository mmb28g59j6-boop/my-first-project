# 04_Dictionaries — README (Beginner + Reference)

This page explains **dictionaries** in Python (`dict`): how to create them, read values, add/update keys, loop through them, and how they connect to real IT support data (tickets, users, devices, issues).

Dictionaries use curly braces: `{ }`.

---

## 1) What is a dictionary?

A **dictionary** stores **key → value** pairs.

Think of it like a real “record” with labeled fields:

* key = the label (example: `"user"`)
* value = the data (example: `"Maria"`)

```text id="9krrmh"
ticket = {
  "user": "Maria",
  "issue": "Wi-Fi disconnects",
  "priority": 2
}
```

---

## 2) Why dictionaries matter (real-world)

Dictionaries match how real systems store data:

* tickets (user, issue, priority, status)
* user accounts (username, email, role)
* devices (asset_tag, model, serial)
* log events (timestamp, severity, message)

When you send/receive data from APIs, it’s often dictionary-shaped.

---

## 3) Keys and values (the basics)

* Keys are usually strings like `"user"`, `"issue"`, `"status"`
* Values can be any type: string, int, bool, list, even another dict

Example:

```text id="t5tmdg"
user = {
  "name": "Dano",
  "age": 34,
  "is_student": True
}
```

---

## 4) Getting values from a dictionary (key lookup)

Use square brackets with the key:

```text id="rgn8dj"
print(ticket["user"])      # Maria
print(ticket["priority"])  # 2
```

✅ This is **key lookup** (not list indexing).

### Common error: Key not found

If you do:

```text id="bcdg0j"
ticket["department"]
```

and `"department"` doesn’t exist, you’ll get:

* `KeyError`

---

## 5) Safer lookup with `get()`

`get()` returns `None` (or a default) instead of crashing:

```text id="42g20y"
dept = ticket.get("department")
print(dept)   # None
```

Default value:

```text id="w707lc"
dept = ticket.get("department", "Unknown")
print(dept)   # "Unknown"
```

---

## 6) Adding a new key/value

```text id="m4hznh"
ticket["status"] = "Open"
```

---

## 7) Updating an existing value

```text id="hplzdb"
ticket["priority"] = 1
```

---

## 8) Removing keys

### A) `pop(key)` (safe-ish)

```text id="j8l4il"
ticket.pop("status")
```

### B) `del` (direct)

```text id="cpv8z0"
del ticket["status"]
```

If the key doesn’t exist, `del` will raise `KeyError`.

---

## 9) Checking what keys exist

```text id="ju5h1q"
print(ticket.keys())
print(ticket.values())
print(ticket.items())
```

Check if a key exists:

```text id="jk9zqk"
if "user" in ticket:
    print("user key exists")
```

---

## 10) Looping through a dictionary

### A) Loop through keys (default)

```text id="35zn7k"
for key in ticket:
    print(key)
```

### B) Loop through key/value pairs (most useful)

```text id="e0o8h2"
for key, value in ticket.items():
    print(key, "=", value)
```

---

## 11) Real structure: list of dictionaries (very common)

This is how you store multiple tickets:

```text id="m17an1"
tickets = [
  {"user": "Maria", "issue": "Wi-Fi disconnects", "priority": 2},
  {"user": "Dano",  "issue": "Printer not found", "priority": 1}
]
```

Loop it:

```text id="d6mgwt"
for t in tickets:
    print(f"TICKET user={t['user']} issue={t['issue']} priority={t['priority']}")
```

---

# Quick Cheat Sheet (Dictionaries)

## Create

* `d = {}`
* `d = {"key": "value"}`

## Read

* `d["key"]`
* `d.get("key")` or `d.get("key", default)`

## Add / Update

* `d["new_key"] = value`
* `d["existing_key"] = new_value`

## Remove

* `d.pop("key")`
* `del d["key"]`

## Loop

* `for k in d:`
* `for k, v in d.items():`

## Check existence

* `"key" in d`

---

## Common mistakes (and fixes)

### Mistake A: KeyError

```text id="s1l9xe"
ticket["status"]   # KeyError if missing
```

Fix: use `get()` or check `"status" in ticket`.

### Mistake B: Confusing `[]` meanings

* For a list: `tools[0]` = first item (index)
* For a dict: `ticket["user"]` = value for key "user"

---

## Mini Reference Example (Help Desk ticket)

```text id="e3b8m0"
ticket = {
  "id": 1024,
  "user": "Maria",
  "device": "MacBook Air",
  "issue": "Wi-Fi disconnects",
  "priority": 2,
  "status": "Open"
}

print(f"[WARN] ticket={ticket['id']} user={ticket['user']} issue={ticket['issue']} status={ticket['status']}")
```


# 04_Dictionaries — Quiz (20 Questions)

**Instructions:** Answer in short form.

* **Q1–Q10 = Easy**
* **Q11–Q20 = A bit harder**

---

## Easy (1–10)

1. What is a dictionary in Python?

2. Which brackets do dictionaries use: `()`, `[]`, or `{}`?

3. Create a dictionary named `user` with keys: `"name"` and `"city"`.

4. If `ticket = {"user": "Maria", "priority": 2}`, what is `ticket["user"]`?

5. What happens if you run `ticket["status"]` but `"status"` is not a key in `ticket`?

6. What does `ticket.get("status")` return if `"status"` is missing?

7. Add a new key/value to `ticket`: `"status": "Open"`.

8. Update `ticket["priority"]` to `1`.

9. What does `ticket.keys()` give you (in plain English)?

10. Write a loop that prints each key in `ticket`.

---

## Harder (11–20)

11. What’s the difference between `ticket["status"]` and `ticket.get("status")`?

12. What does `ticket.get("status", "Unknown")` do?

13. How do you check if a key exists in a dictionary (example: `"user"`)?

14. What does `ticket.items()` return (plain English)?

15. Write a loop that prints both key and value like: `key = value`.

16. Remove the key `"status"` from a dictionary using `pop()`.

17. Create a list named `tickets` that contains **two dictionaries**, each with keys `"user"` and `"issue"`.

18. Loop through that `tickets` list and print:
    `TICKET user=<user> issue=<issue>`

19. Given:
    `ticket = {"user": "Maria", "priority": 2, "status": "Open"}`
    Write code that prints `"High Priority"` only if priority is 1.

20. Given:
    `ticket = {"user": "Maria", "priority": 2}`
    Add a key `"tags"` whose value is a list: `["wifi", "urgent"]` and then print the tags list.
