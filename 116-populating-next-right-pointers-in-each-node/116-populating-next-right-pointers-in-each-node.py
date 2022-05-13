"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
# https://www.youtube.com/watch?v=68RmOoq-OSs&t=965s
        
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            pre = None
            
            for _ in range(len(queue)):
                
                cur = queue.popleft()
                
                if pre:
                    pre.next = cur # populating
                    
                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)
                    
                pre = cur
                
        return root