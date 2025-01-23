# 605. Can Place Flowers

**Difficulty:** Easy

## Problem Description
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`'s and `1`'s:
- `0` means the plot is empty.
- `1` means the plot is not empty.

You are also given an integer `n`, which represents the number of flowers you want to plant. Return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule, and `false` otherwise.

---

## Examples

### Example 1
**Input:**  
```
flowerbed = [1, 0, 0, 0, 1], n = 1
```
**Output:**  
```
true
```
**Explanation:**
- The flowerbed starts as `[1, 0, 0, 0, 1]`.
- You can plant one flower in position 2 (0-indexed): `[1, 0, 1, 0, 1]`.
- Since you only needed to plant 1 flower, the result is `true`.

---

### Example 2
**Input:**  
```
flowerbed = [1, 0, 0, 0, 1], n = 2
```
**Output:**  
```
false
```
**Explanation:**
- The flowerbed starts as `[1, 0, 0, 0, 1]`.
- You can plant one flower in position 2 (0-indexed): `[1, 0, 1, 0, 1]`.
- There is no more space to plant a second flower without violating the no-adjacent-flowers rule.
- The result is `false`.

---

## Constraints
- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent `1`s in the initial flowerbed.
- `0 <= n <= flowerbed.length`.
