from typing import List

def canJump(nums: List[int]) -> bool:
    jump = 0
    for n in nums:
        if jump < 0:
            return False
        elif n > jump:
            jump = n
        jump-=1
    
    return True

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))