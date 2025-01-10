from typing import List

def removeElement(nums: List[int], val: int) -> int:
    counter = 0

    for _, value in enumerate(nums):
        if value != val:
            nums[counter] = value
            counter += 1

    return counter


print(removeElement([2],3))