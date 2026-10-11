# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(inorder[0])

        hash = {val : idx for idx, val in enumerate(inorder)}

        self.preindex = 0

        def dfs(left, right):
            if left > right:
                return None

            node = TreeNode(preorder[self.preindex])
            index = hash[node.val]
            self.preindex += 1

            node.left = dfs(left, index - 1)
            node.right = dfs(index + 1, right)

            return node
        
        return dfs(0, len(preorder) - 1)