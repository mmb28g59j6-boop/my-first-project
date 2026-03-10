# 01_Variables — README (Beginner + Overview)

This page is the **overview** of variables and the core syntax you’ll see everywhere.
Detailed deep-dives live in:

* `strings_README.md` (02_Strings)
* `lists_README.md` (03_Lists)
* `dictionaries_README.md` (04_Dictionaries)

---

## 1) What a variable is

A **variable** is a name that stores a value.

```text id="3jil5k"
age = 34
```

**Important:** `=` means **assign** (store a value), not “equals” like math.

---

## 2) The core beginner value types

These are the main types you’ll use constantly:

### `str` (text)

```text id="oav7b1"
city = "Sault Ste Marie"
```

### `int` (whole numbers)

```text id="9b0y8o"
priority = 2
```

### `float` (decimals)

```text id="lq5gik"
price = 19.99
```

### `bool` (True/False)

```text id="ve4p5z"
is_online = True
```

### `None` (no value yet)

```text id="x1nho4"
result = None
```

---

## 3) Naming variables (rules + style)

### Rules

* Start with a letter or `_`
* Use letters, numbers, underscores only
* No spaces
* Case-sensitive (`age` ≠ `Age`)

✅ Good:

```text id="4s2v4q"
first_name = "Dano"
ticket_priority = 2
```

❌ Bad:

```text id="xv2u14"
my name = "no"    (spaces not allowed)
my-name = "no"    (hyphen not allowed)
2name = "no"      (can't start with number)
```

### Style (recommended)

Use **snake_case**:

```text id="qlnntj"
failed_login_count = 3
```

### Constants (convention)

Not enforced, but common:

```text id="t7x4fl"
MAX_RETRIES = 3
```

---

## 4) Printing values: `print()`

`print()` shows values in the terminal.

```text id="e8pob8"
print("Age:", age)
```

Commas in `print()` let you print multiple things.

---

## 5) Checking types: `type()`

```text id="om5f0c"
print(type(age))
```

---

## 6) Updating variables (reassignment)

You can change a variable:

```text id="72eu0d"
points = 5
points = points + 1
```

Short form:

```text id="pzx8ch"
points += 1
```

---

## 7) Input starts as text: `input()`

`input()` always returns a string (`str`), so convert for math:

```text id="nq28qz"
user_age = int(input("Enter your age: "))
print(user_age + 1)
```

---

## 8) Bracket meanings (quick reference)

* `()` function call / grouping math
  Example: `print(...)`, `(2 + 3) * 4`
* `[]` list / indexing / slicing
  Example: `tools[0]`, `tools[0:2]`
* `{}` dictionary / set / f-string placeholders
  Example: `{"user": "Maria"}`, `f"{age}"`

(Details live in the topic READMEs.)

---

# Quick Cheat Sheet (Variables)

## Common patterns

* Assign: `x = 10`
* Print: `print(x)`
* Type: `type(x)`
* Update: `x = x + 1` or `x += 1`
* Input + convert: `int(input("..."))`, `float(input("..."))`

## Common beginner errors

* **NameError**: variable used before defined
* **TypeError**: mixing types (like `"5" + 5`)
* **ValueError**: converting bad input (like `int("abc")`)

--------------------------------------------------

# 01_Basics — Variables (Python)

This section explains what variables are, how Python stores values, and the core syntax you’ll see everywhere: `=`, `print()`, `type()`, `f""`, `{}`, `[]`, `()`.

---

## 1) What a variable is

A **variable** is a *name* that points to a value.

Example:

* `age` is the variable name
* `34` is the value

```text
age = 34
```

**Important:** In Python, `=` means **assign** (store), not “equals” like math class.

---

## 2) The main beginner data types (what variables can hold)

### String (`str`) — text

Text is always inside quotes:

```text
name = "Dano"
birth_date = "April 29, 1991"
```

### Integer (`int`) — whole number

```text
age = 34
priority = 2
```

### Float (`float`) — decimal number

```text
price = 19.99
hours = 1.5
```

### Boolean (`bool`) — True/False

```text
is_student = True
is_online = False
```

### None (`NoneType`) — no value yet

Use when you don’t have a value yet:

```text
middle_name = None
```

---

## 3) Naming variables (rules + best practice)

### Rules (must follow)

* Must start with a **letter** or `_`
* Can include letters, numbers, `_`
* **No spaces**
* Case-sensitive (`age` ≠ `Age`)

✅ Good:

```text
first_name = "Dano"
ticket_priority = 2
```

❌ Bad:

```text
2name = "no"     (can't start with a number)
my-name = "no"   (hyphen not allowed)
my name = "no"   (spaces not allowed)
```

### Style (recommended)

Use **snake_case**:

```text
failed_login_count = 3
```

### “Constants” (convention)

Python doesn’t truly lock constants, but people use ALL_CAPS to signal “do not change”:

```text
MAX_RETRIES = 3
```

---

## 4) Printing and parentheses `()`

### `print()` is a function call

Parentheses `()` mean “call/run the function”.

```text
print("Age:", age)
```

* Commas inside `print()` print multiple items separated by spaces.

---

## 5) Checking types with `type()`

```text
print(type(age))
```

Examples:

* `<class 'int'>`
* `<class 'str'>`

---

## 6) Reassignment (changing a variable)

Variables can be updated:

```text
points = 5
points = 8
points = points + 2
```

---

## 7) f-strings and curly braces `{}` (formatted text)

An f-string is a string that can insert variables.

```text
print(f"{name} is {age} years old.")
```

* `f"..."` turns formatting on
* `{name}` inserts the value of `name`
* `{age}` inserts the value of `age`
* You can also put expressions inside `{}`:

```text
print(f"Next year: {age + 1}")
```

---

## 8) Input always starts as text (string)

`input()` always returns a `str`:

```text
user_age = input("Enter your age: ")
```

So if you need math, convert it:

```text
user_age = int(user_age)
print(user_age + 1)
```

Convert to float when needed:

```text
hours = float(input("Hours studied: "))
```

---

## 9) The 3 bracket types: `()`, `[]`, `{}` (what they mean)

### Parentheses `()`

Use for:

* Function calls: `print(...)`, `type(...)`, `input(...)`
* Grouping math: `(2 + 3) * 4`
* Tuples (later): `(10, 20)`

### Square brackets `[]`

Use for:

* Lists: `tools = ["VS Code", "Python"]`
* Indexing: `tools[0]` (first item)
* Slicing: `tools[0:2]`

### Curly braces `{}`

Use for:

* Dictionaries (key/value): `{"user": "Maria", "priority": 2}`
* Sets (unique values): `{1, 2, 3}`
* f-string placeholders: `f"{name}"` (this is formatting, not a dictionary)

---

# Quick Cheat Sheet (copy/reference)

## Common types

* `str`  → `"text"`
* `int`  → `34`
* `float`→ `19.99`
* `bool` → `True` / `False`
* `None` → `None`

## Common patterns

* Assign: `x = 10`
* Print: `print(x)`
* Type: `type(x)`
* Format text: `f"{x}"`
* Input: `input("...")` → convert with `int()` or `float()`

## Common beginner errors

* **NameError**: using a variable before it exists
* **TypeError**: mixing types (example: `"5" + 5`)
* Fix by converting types: `int("5")`, `str(5)`

---

## Mini Reference Examples

### Example 1: Basic variables

```text
name = "Dano"
age = 34
print(f"{name} is {age}.")
```

### Example 2: Input + conversion

```text
num = int(input("Enter a number: "))
print(num + 10)
```

### Example 3: List + index

```text
tools = ["VS Code", "Python", "Terminal"]
print(tools[0])
```

### Example 4: Dictionary + key

```text
ticket = {"user": "Maria", "issue": "Wi-Fi", "priority": 2}
print(ticket["issue"])
```