# 0268. Missing Number

## Problem
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## Approach
- Sort the array in ascending order.
- Traverse the sorted array.
- Compare each element with its index.
- If an element does not match its index, return the index as the missing number.
- If all elements match their indices, then the missing number is `n`.

## Example

**Input:**
```
nums = [3,0,1]
```

**Process:**
```
Sort the array

[0,1,3]

Compare index with value:

Index 0 → Value 0 ✔
Index 1 → Value 1 ✔
Index 2 → Value 3 ✘

Missing Number = 2
```

**Output:**
```
2
```

## Complexity
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(1)`
