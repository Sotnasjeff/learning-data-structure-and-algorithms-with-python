from typing import List

def twoSums(nums: List[int], target: int):
    hasher = {}
    
    for index, value in enumerate(nums):
        if abs(value - target) in hasher:
            return [hasher[abs(value - target)], index]

        hasher[value] = index


print(twoSums([2,7,11,15], 9))
print(twoSums([3,2,4], 6))