"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        hash = {} #old and new nodes
        
        def dfs(node):
            if node in hash: #if already in hash, theres a clone
                return hash[node]

            replica = Node(node.val)
            hash[node] = replica #mapping old node to the copy

            #make copies for all neighbors
            for n in node.neighbors: 
                replica.neighbors.append(dfs(n))
            return replica

        return dfs(node) if node else None


        
        