from typing import List
# Worst scenario in time complexity: O(n²)
# Great and Average scenario in time complexity: O(n log n)
# worst space complexity: O(n)
def quick_sort_recursive(arr: List[int], left: int, right: int) -> List[int]:
    if left < right:
        print(arr[left:right+1])
        pi = partition(arr, left, right)
        quick_sort_recursive(arr, left, pi-1)
        quick_sort_recursive(arr, pi+1, right)
    
    return arr

    
def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1

from typing import List



arr = [1,5,8,2,6,3,5,4,81]
print(quick_sort_recursive(arr, 0, len(arr) -1))

