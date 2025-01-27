from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    left, right = 1,1
    
    for i in range(len(nums)):
        result[i] = left
        left *= nums[i]
    
    for j in range(len(nums) - 1, -1, -1):
        result[j] *= right
        right *= nums[j]
    
    return result
    

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))