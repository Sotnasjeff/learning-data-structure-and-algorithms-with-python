from collections import deque
from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    
    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif node.data < data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)

        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)

        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)

        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)
    
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = Node(postorder.pop())
        inorder_index = inorder.index(root.data)

        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        return root

    def reverse_binary_tree(self):
        if self.root is None:
            return None

        left = self.reverse_binary_tree(self.root.right)
        right = self.reverse_binary_tree(self.root.left)

        self.root.left = left
        self.root.right = right

    # DFS - Depth First Search - Profundidade
    def dfs_implementation(self, data) -> bool:
        return self._dfs_recursive(self.root, data)
    
    def _dfs_recursive(self, node, data) -> bool:
        if node is None:
            return False
        if node.data == data:
            return True
         
        if self._dfs_recursive(node.left, data):
            return True
        
        if self._dfs_recursive(node.right, data):
            return True
    
    #DFS Leetcode problem
    def hasPathSum(self, root: Node, targetSum: int) -> bool:
        if root is None:
            return False
        
        if not root.right and not root.left and root.val == targetSum:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    
    #BFS - Breadth First Search - Amplitude
    def bfs_implementation(self, data: int) -> bool:
        if self.root is None:
            return False
        
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.data)
            if node.data == data:
                return True

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False
    

    #BFS Leetcode problem
    def levelOrder(self) -> List[List[int]]:
        response = []
        queue = deque()
        queue.append(self.root)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    level.append(node.data)
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)
            if level:
                response.append(level)
                
        return response



my_binary = BinaryTree()
my_binary.insert(8)
my_binary.insert(6)
my_binary.insert(15)
my_binary.insert(4)
my_binary.insert(9)
my_binary.insert(18)
my_binary.insert(3)
my_binary.insert(16)
my_binary.insert(37)

print("pre_order_traversal: ", my_binary.preorder_traversal())
print("in_order_traversal: ", my_binary.inorder_traversal())
print("post_order_traversal: ", my_binary.postorder_traversal())
print("--------------------------------------------------------")
print("bfs", my_binary.bfs_implementation(18))
print("--------------------------------------------------------")
print("dfs", my_binary.dfs_implementation(18))
print()