# 0137. Single Number II

## Problem
Given a non-empty array of integers `nums`, every element appears **three times** except for one, which appears **exactly once**. Find and return that single element.

## Approach
- Use a hash map (dictionary) to count the frequency of each element.
- Traverse the array and store the occurrence of each number.
- Return the element whose frequency is `1`.

## Example

**Input:**
```
nums = [2, 2, 3, 2]
```

**Frequency Count:**
```
2 → 3
3 → 1
```

**Output:**
```
3
```

## Time Complexity
**O(n)**

## Space Complexity
**O(n)**
