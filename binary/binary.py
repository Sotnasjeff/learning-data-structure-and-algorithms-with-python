from typing import List
#binary shift right and left
#128 64 32 16 8 4 2 1 
# _  _  _  _  _ _ _ _

print(5>>1)
print(5<<3)

# AND 1 + 1 = 1, 0 + 1 = 0, 0 + 0 = 0
# OR 1 + 1 = 1, 1 + 0 = 1, 0 + 1 = 1, 0 + 0 = 0
# XOR 0 + 1 = 1, 1 + 1 = 0, 0 + 0 = 0
# simbol XOR: ^

def missingNumber(nums: List[int]) -> int:
    x = 0
    for num in nums:
        x ^= num

    for i in range(len(num) + 1):
        x ^= i
    
    return x

def numberOfSteps(num: int) -> int:
    steps = 0
    while num > 0:
        if num & 1:
            num -= 1
        else:
            num>>=1
        steps += 1
    return steps

def hammingWeight(self, n: int) -> int:
    counter = 0
    for i in range(32):
        if (n >> i) & 1:
            counter += 1
        
    return counter

def countBits(self, n: int) -> List[int]:
    my_list = [0] * (n + 1)
    for i in range(1, n + 1):
        my_list[i] = my_list[i >> 1] + (i & 1)
    return my_list