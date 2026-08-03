# 0136. Single Number

## Problem
Given a non-empty integer array `nums`, every element appears twice except for one. Find that single element and return it.

## Approach
- Create a dictionary to store the frequency of each element.
- Traverse the array and update the frequency count.
- Iterate through the dictionary and return the element whose frequency is `1`.

## Example

**Input:**
```
nums = [4,1,2,1,2]
```

**Process:**
```
Frequency Dictionary:

4 → 1
1 → 2
2 → 2

Element with frequency 1:
4
```

**Output:**
```
4
```

## Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
