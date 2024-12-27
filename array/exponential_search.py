# only works if input is sorted
# Big O speed: O(log n) 

from typing import List

def binary_search(nums: List[str], n: str, left: int, right: int) -> int:
    step = 0

    while left < right:
        step += 1
        mid = int((left+right)/2)

        if nums[mid] == n:
            print("step:", step)
            return mid
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid
    return -1

def exponential_search(arr: List[int], target: int) -> int:
    if arr[0] == target:
        return 0
    
    right = len(arr)
    left = 1

    while left < right and arr[left] < target:
        left *= 2
    
    if arr[left] == target:
        return left

    return binary_search(arr, target, left//2, min(left, right-1))


result = exponential_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42.43], 31)
print(f"Element found at index: {result}")