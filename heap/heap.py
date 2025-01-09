import heapq
from typing import List
from collections import Counter

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def _heapify_up(self, index):
        if index == 0:
            return
        
        parent_index = self._parent(index)

        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        size = len(self.heap)

        left = self._left_child(index)
        right = self._right_child(index)

        smallest = index

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(index)
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root


#Leetcode Heap Problem
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]

#Leetcode Heap problem
def topKFrequent(nums: List[int], k: int) -> List[int]:
    dic=Counter(nums)
    heapmax=[[-freq,num] for num,freq in dic.items()]
    heapq.heapify(heapmax)
    list1=[]
    for i in range(k):
        poping=heapq.heappop(heapmax)
        list1.append(poping[1])
    return list1