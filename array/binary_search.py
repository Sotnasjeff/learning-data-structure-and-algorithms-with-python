from typing import List
# only works if input is sorted
# Big O speed: O(log n) 
# doing binary search using two pointers
def binary_search(nums: List[int], n: int) -> int:
    left, right = 0,len(nums)
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


print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42.43], 7))