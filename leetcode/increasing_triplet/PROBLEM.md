# [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)

**Difficulty:** Medium  
**Topics:** Arrays  
**Companies:** (if applicable)

Given an integer array `nums`, return `true` _if there exists a triple of indices_ `(i, j, k)` _such that_ `i < j < k` _and_ `nums[i] < nums[j] < nums[k]`. If no such indices exist, return `false`.

## **Example 1**

```python
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
```

## **Example 2**

```python
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
```

## **Example 3**

```python
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
```

## **Constraints**
- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`