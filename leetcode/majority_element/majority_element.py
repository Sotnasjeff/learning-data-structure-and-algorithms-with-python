from typing import List

def majorityElement(nums: List[int]) -> int:
    my_hash_map = {}
    aux = 0
    result = 0

    for _, value in enumerate(nums):
        if value not in my_hash_map:
            my_hash_map[value] = 1
        else:
            my_hash_map[value] += 1
    

    for key, val in my_hash_map.items():
        if val > aux:
            aux = val
            result = key
    
    return result

def majorityElement2(nums: List[int]) -> int:
    nums.sort()
    counter, aux, result, left, right = 0,0,0,0,0
    while right <= len(nums)-1:
        if nums[left] == nums[right]:
            counter += 1
        else:
            if counter > aux:
                aux = counter
                result = nums[left]
            counter = 0
            left = right
        right += 1

    if right == len(nums) and counter >= aux:
        result = nums[left]

    return result

print(majorityElement2([2,2,1,1,1,2,2]))