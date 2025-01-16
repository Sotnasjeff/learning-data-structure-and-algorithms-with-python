from typing import List

def rotate(nums: List[int], k: int) -> None:
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

    

print(rotate([-1,-100,3,99],2))
print(rotate([1,2,3,4,5,6,7],3))