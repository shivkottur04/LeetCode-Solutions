# 0026. Remove Duplicates from Sorted Array

## Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be maintained.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique elements, while the remaining elements are not important.

---

## Approach

- Convert the given array into a **set** to remove all duplicate elements.
- Convert the set back into a list.
- Sort the list to restore the original ascending order.
- Copy the unique sorted elements back into the original array.
- Return the number of unique elements.

---

## Complexity Analysis

- **Time Complexity:** O(n + k log k)
- **Space Complexity:** O(k)

where:
- `n` = size of the input array
- `k` = number of unique elements

---

## Example

**Input**

```text
nums = [1,1,2,2,3]
```

**Output**

```text
k = 3
nums = [1,2,3,_,_]
```

---

## Notes

- This solution removes duplicates using a **set**, making it easy to implement.
- The unique elements are sorted before copying them back into the original array.
- Although this solution produces the correct output, it uses **O(k)** extra space.
- The optimal LeetCode solution uses the **Two Pointer** technique, achieving **O(n)** time complexity and **O(1)** extra space.

---

## Solution

The Python implementation is available in **`solution.py`**.
