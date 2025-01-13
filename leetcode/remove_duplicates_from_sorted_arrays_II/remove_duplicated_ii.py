from typing import List

def removeDuplicates(nums: List[int]) -> int:
    counter = 0
    my_hash = {v:int(0) for v in nums}

    for _, value in enumerate(nums):
        if my_hash[value] < 2:
            nums[counter] = value 
            counter += 1
        my_hash[value] += 1
    
    print(nums)
    return counter



print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))