from collections import deque
from typing import List
import heapq

class Node:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors
    

def cloneGraph(node: Node):
    if not node:
        return node
    
    q = deque([node])

    clones = {}
    clones[node.value] = Node(node.value, [])
    
    while q:
        current = q.popleft()
        current_clone = clones[current.value]

        for n in current.neighbors:
            if n.value not in clones:
                clones[n.value] = Node(n.value, [])
                q.append(n)
            current_clone.neighbors.append(clones[n.value])
    
    return clones[node.value]

def dijkstra(graph, start):
    min_heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    
    return distances


# Dijkstra leetcode problem
def networkDelayTime(times: List[List[int]], n: int, k:int) -> int:
    table = {}

    for t in times:
        if not table.get(t[0]):
            table[t[0]] = {t[1]: t[2]}
        else:
            table[t[0]] [t[1]] = t[2]
    
    distances = {k: 0}
    min_heap = [(0,k)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        row = table.get(current_node)

        if row:
            for key, value, in row.items():
                table_distance = distances.get(key, float('inf'))
                if current_distance + value < table_distance:
                    distances[key] = current_distance + value
                    heapq.heappush(min_heap, (current_distance + value, key))
    
    _max = -1
    if len(distances) < n:
        return _max
    
    for _, v in distances.items():
        _max = max(_max, v)
    
    if _max == 0:
        return -1

    return _max

def canFinish(numCourses:int, prerequisites: List[List[int]]) -> bool:
    table = {i:[] for i in range(numCourses)}

    for a, b in prerequisites:
        table[b].append(a)
    
    state = [0] * numCourses

    def has_cycle(v):
        if state[v] == 1:
            return True
        if state[v] == 2:
            return False
        
        state[v] = 1
        for neighbor in table[v]:
            if has_cycle(neighbor):
                return True
        state[v] = 2
        return False

    for i in range(numCourses):
        if has_cycle(i):
            return False
    
    return True

def numIslands(grid: List[List[str]]) -> int:
	grid_size = len(grid)
	width = len(grid[0])
	
	num_of_island = 0
	for i in range(grid_size):
		for j in range(width):
			if grid[i][j] == '1':
				num_of_island += 1
				dfs(i,j,grid_size, width, grid)
	
	return num_of_island

def dfs (i,j, grid_size, width, grid):
	if i < 0 or i >= grid_size or j < 0 or j >= width or grid[i][j] == '0':
		return
	grid[i][j] = '0'
	dfs(i + 1, j, grid_size, width, grid)
	dfs(i - 1, j, grid_size, width, grid)
	dfs(i, j + 1, grid_size, width, grid)
	dfs(i, j - 1, grid_size, width, grid)

#graph = {
#    'A': {'B':1, 'C':4},
#    'B': {'A':1, 'C':2, 'D':5},
#    'C': {'A':4, 'B':2, 'D':1},
#    'D': {'B':5, 'C':1},
#}
#
#print(dijkstra(graph, 'A'))

times = [[2,1,1],[2,3,1],[3,4,1]]

print(networkDelayTime(times, 4, 2))
grid = [["1","1","1","1","1","0"],
        ["1","1","1","0","0","1"],
        ["1","1","1","0","0","1"],
        ["0","0","0","1","0","0"]
        ]
print(numIslands(grid))