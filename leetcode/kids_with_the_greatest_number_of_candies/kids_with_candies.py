from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    _max = max(candies)
    result = []
    for _, value in enumerate(candies):
        if value + extraCandies >= _max:
            result.append(True)
        else:
            result.append(False)
    
    return result