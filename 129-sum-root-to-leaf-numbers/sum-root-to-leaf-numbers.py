# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, num):
            if not node.left and not node.right:
                return int(num + str(node.val))
            out = 0
            if node.left:
                out += dfs(node.left, num + str(node.val))
            if node.right:
                out += dfs(node.right, num + str(node.val))
            return out   
        return dfs(root, "")