# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.counter = 0

        def dfs(root):
            if not root:
                return None

            dfs(root.left)

            self.counter += 1

            if (self.counter == k):
                self.res = root.val

            dfs(root.right)

        dfs(root)
        return self.res
