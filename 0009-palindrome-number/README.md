# 0009. Palindrome Number

## Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same forward and backward.

---

## Approach

- If the number is negative, return `False` since negative numbers cannot be palindromes.
- Convert the integer to a string.
- Reverse the string.
- Convert the reversed string back to an integer.
- Compare the reversed number with the original number.
- If they are equal, return `True`; otherwise, return `False`.

---

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

where `n` is the number of digits in the integer.

---

## Example

**Input**

```
121
```

**Output**

```
True
```

---

## Notes

- This solution uses string manipulation to reverse the number.
- It is simple and easy to understand.
- An optimized solution without converting the integer to a string can achieve **O(1)** extra space.

---

## Solution

The Python implementation is available in **`solution.py`**.
