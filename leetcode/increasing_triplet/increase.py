from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    min1 = float('inf')
    min2 = float('inf')
    for n in nums:
        if n <= min1:
            min1 = n
        elif n <= min2:
            min2 = n
        else:
            return True
    
    return False

print(increasingTriplet([1,2,3,4,5]))
print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([2,1,5,0,4,6]))
