# 0007. Reverse Integer

## Problem Statement

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

## Approach

- Store the original number to preserve its sign.
- Convert negative numbers to positive before reversing.
- Reverse the digits using string slicing.
- Convert the reversed string back to an integer.
- Check whether the reversed number is within the 32-bit signed integer range.
- Restore the negative sign if the original number was negative.

## Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

where `n` is the number of digits in the integer.

## Example

**Input**

```
123
```

**Output**

```
321
```

## Solution

The Python implementation is available in **`solution.py`**.
