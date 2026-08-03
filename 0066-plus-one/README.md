# 0066. Plus One

## Problem
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant. Increment the large integer by one and return the resulting array of digits.

## Approach
- Convert the list of digits into a string.
- Convert the string to an integer.
- Increment the integer by 1.
- Convert the updated integer back to a string.
- Convert each character of the string back into an integer and store it in a list.
- Return the updated list.

## Example

**Input:**
```
digits = [1,2,3]
```

**Process:**
```
[1,2,3]
   ↓
"123"
   ↓
123
   ↓
123 + 1 = 124
   ↓
"124"
   ↓
[1,2,4]
```

**Output:**
```
[1,2,4]
```

## Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
