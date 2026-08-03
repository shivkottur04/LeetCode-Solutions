# 0088. Merge Sorted Array


## Problem
You are given two sorted integer arrays `nums1` and `nums2`, along with two integers `m` and `n`, representing the number of valid elements in each array. Merge `nums2` into `nums1` as one sorted array. The final sorted array should be stored in `nums1` in-place.

## Approach
- Replace the extra spaces in `nums1` (starting from index `m`) with all elements of `nums2`.
- Sort the updated `nums1` array.
- Since the function modifies `nums1` in-place, no value is returned.

## Example

**Input:**
```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
```

**Process:**
```
nums1[m:] = nums2

[1,2,3,2,5,6]

Sort the array

[1,2,2,3,5,6]
```

**Output:**
```
[1,2,2,3,5,6]
```

## Complexity
- **Time Complexity:** `O((m+n) log(m+n))`
- **Space Complexity:** `O(1)`
