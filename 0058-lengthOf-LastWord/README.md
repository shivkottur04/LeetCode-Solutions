# 0058. Length of Last Word

## Problem Statement

Given a string `s` consisting of words and spaces, return the length of the **last word** in the string.

A word is defined as a maximal substring consisting of non-space characters only.

---

## Approach

- Split the string into a list of words using the `split()` method.
- Find the last word in the list.
- Return the length of the last word using the `len()` function.

---

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

where `n` is the length of the input string.

---

## Example

**Input**

```text
s = "Hello World"
```

**Output**

```text
5
```

---

## Notes

- The `split()` method automatically removes leading, trailing, and multiple consecutive spaces.
- After splitting, the last element of the list is the last word in the string.
- This solution is simple, readable, and works efficiently for all valid inputs.
- An optimized solution can achieve **O(1)** extra space by traversing the string from the end without using `split()`.

---

## Solution

The Python implementation is available in **`solution.py`**.
