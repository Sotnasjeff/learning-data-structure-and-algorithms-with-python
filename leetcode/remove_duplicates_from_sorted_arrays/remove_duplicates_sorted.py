from typing import List

def removeDuplicates(nums: List[int]) -> int:
    my_hash = {}
    counter = 0
    for i in range(len(nums)):
        if nums[i] in my_hash:
            continue
        else:
            my_hash[nums[i]] = True
            nums[counter] = nums[i]
            counter += 1
    
    return counter


print(removeDuplicates([1,1,2]))