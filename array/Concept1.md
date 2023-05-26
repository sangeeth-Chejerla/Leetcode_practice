
# python Counter & functions

## Counter

collections.Counter is a subclass of dict class in python that counts the occurrence of elements/items in an iterable object. It takes an iterable (list, tuple, string) as input and returns a dictionary with elements as keys and their count as values.

Example:

```python
from collections import Counter

# list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
result = Counter(a)

print(result)
# Output: Counter({1: 6, 2: 4, 3: 3, 4: 2, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

# string
str = "Hello World"
result = Counter(str)

print(result)
# Output: Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
```

---

## Python split() Method

 split() method in python is used to split a string into a list of substrings based on a delimiter. If no delimiter is specified, whitespace will be considered as the default delimiter.

```python
string = "Python is a popular programming language"

# using whitespace delimiter
result = string.split()

print(result)
# Output: ['Python', 'is', 'a', 'popular', 'programming', 'language']

```
---
