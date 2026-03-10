# 02_Strings — README (Beginner + Reference)

This page is only about **string operations** (the `str` type): indexing, slicing, split, replace, and formatting text.
(Variables/types overview belongs in `variables_README.md`.)

---

## 1) What strings are (quick)

A string is text in quotes:

```text
text = "Hello World"
city = "Sault Ste Marie"
```

---

## 2) Strings are immutable (important)

You can’t “edit” a string in place. Methods return a **new** string.

```text
msg = "WiFi"
print(msg.lower())   # prints "wifi"
print(msg)           # still "WiFi"

msg = msg.lower()    # now msg is changed
print(msg)           # "wifi"
```

---

## 3) Common string tools (you will use these constantly)

### A) Length: `len()`

Counts characters (including spaces):

```text
text = "Hello World"
print(len(text))   # 11
```

### B) Case cleanup

```text
msg = "wiFI is disCoNnEcTiNg"
print(msg.lower())
print(msg.upper())
print(msg.title())
```

### C) Formatting text (best practice): f-strings

Use f-strings to build messages, logs, and ticket notes.

```text
device = "MacBook Air"
issue = "wifi disconnects"
city = "Sault Ste Marie"
log = f"[WARN] device={device} issue={issue} city={city}"
print(log)
```

---

## 4) Indexing (get 1 character)

Indexing uses square brackets `[]`. Python counts from 0.

```text
text = "Hello"
print(text[0])    # H
print(text[1])    # e
print(text[-1])   # o (last character)
```

✅ `text[0]` = first character
✅ `text[-1]` = last character

---

## 5) Slicing (get a piece of a string)

Slicing format:

```text
text[start:end]
```

* includes `start`
* stops before `end`

```text
text = "Hello World"
print(text[0:5])   # Hello
print(text[6:11])  # World
```

Shortcuts:

```text
print(text[:5])    # from start to 5
print(text[6:])    # from 6 to end
```

---

## 6) split() (turn a sentence into words)

`split()` turns a string into a **list** of words.

```text
sentence = "wifi disconnects often"
words = sentence.split()
print(words)        # ['wifi', 'disconnects', 'often']
print(words[0])     # wifi
print(words[2])     # often
```

---

## 7) replace() (swap text inside a string)

```text
sentence = "wifi disconnects often"
fixed = sentence.replace("wifi", "Wi-Fi")
print(fixed)
```

Chain replacements:

```text
alert = "wifi disconnects often"
alert = alert.replace("wifi", "Wi-Fi").replace("often", "a lot")
print(alert)
```

---

## 8) Mini cheat sheet (strings)

### Create

* `"text"` or `'text'`

### Length

* `len(text)`

### Case

* `text.lower()`
* `text.upper()`
* `text.title()`

### Formatting

* `f"{variable}"`

### Index/slice

* `text[0]`, `text[-1]`
* `text[start:end]`

### Split/replace

* `text.split()`
* `text.replace("old", "new")`

---

## 9) Common mistakes (quick fixes)

* **IndexError**: index out of range → check `len(text)`
* Forgetting immutability → store the result: `text = text.lower()`
* Confusing words vs characters:

  * `words[0]` = first word
  * `words[0][2]` = 3rd character of the first word

--------------------------------------------------

Strings Self-Test (10)

What is a string in Python? Give one example.

What does len("Hello World") return, and why?

What is the difference between:

text.upper()

text = text.upper()

What does text[0] mean?
What does text[-1] mean?

If text = "Hello World", what does text[0:5] return?

If text = "Hello World", what does text[6:11] return?

If sentence = "wifi disconnects often", what does:

sentence.split() return?

What does words[2] return after splitting?

What does replace() do?
Example: What is the result of:

"wifi disconnects".replace("wifi", "Wi-Fi")

What is an f-string and what do the curly braces {} do inside it?

Explain the difference between:

words[0]

words[0][2]
(Assume words = ["wifi", "disconnects", "often"])

-------------------------------------------------------------

## Strings Quiz (20 Questions)

**Instructions:** Answer in short form.

* **Q1–Q10 = Easy**
* **Q11–Q20 = Harder**

---

### Easy (1–10)

1. What is a string in Python?

2. Which quotes can you use to make a string?

3. If `city = "Sault Ste Marie"`, what is `type(city)`?

4. What does `len("Hello")` return?

5. If `text = "Hello"`, what does `text[0]` return?

6. If `text = "Hello"`, what does `text[-1]` return?

7. If `text = "Hello World"`, what does `text[0:5]` return?

8. What does `lower()` do?

9. What does `upper()` do?

10. What does this print?

```text
name = "Dano"
age = 34
print(f"{name} is {age}")
```

---

### Harder (11–20)

11. What’s the difference between:

* `msg.lower()`
* `msg = msg.lower()`

12. If `text = "Hello World"`, what does `text[6:]` return?

13. If `text = "Hello World"`, what does `text[:5]` return?

14. If `sentence = "wifi disconnects often"`, what does `sentence.split()` return?

15. If `words = ["wifi", "disconnects", "often"]`, what is `words[1]`?

16. If `words = ["wifi", "disconnects", "often"]`, what is `words[0][2]`?

17. What does this return?

```text
"wifi disconnects".replace("wifi", "Wi-Fi")
```

18. Create an f-string that outputs:
    `[INFO] device=Mac issue=wifi city=Sault`

(Use variables `device`, `issue`, `city`.)

19. What does this print?

```text
text = "ABC"
print(text.lower())
print(text)
```

20. Explain “strings are immutable” in one sentence.
