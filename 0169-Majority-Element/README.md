# 0169. Majority Element

## Problem
Given an array `nums` of size `n`, return the **majority element**.

The majority element is the element that appears **more than ⌊n / 2⌋ times**. You may assume that the majority element always exists in the array.

## Approach
- Use a hash map (dictionary) to count the frequency of each element.
- Traverse the array and update the count of every number.
- Iterate through the hash map and return the element whose frequency is greater than `n / 2`.

## Example

**Input:**
```
nums = [2, 2, 1, 1, 1, 2, 2]
```

**Frequency Count:**
```
1 → 3
2 → 4
```

Since `2` appears more than `7 / 2 = 3.5` times, it is the majority element.

**Output:**
```
2
```

## Time Complexity
**O(n)**

## Space Complexity
**O(n)**
