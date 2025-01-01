from typing import List
# Worst scenario in time complexity: O(n²)
# space complexity: O(1)
def bubble_sort(arr: List[int]) -> List[int]:
    size = len(arr)
    for _ in arr:
        is_sorted = True
        print(arr)
        for i in range(size - 1):
            if arr[i] > arr[i+1]:
                is_sorted = False
                arr[i+1], arr[i] = arr[i], arr[i+1]
        if is_sorted:
            return arr
    return arr


print(bubble_sort([2,59,8,2,1,4,2,5,36,8,9,11,52]))