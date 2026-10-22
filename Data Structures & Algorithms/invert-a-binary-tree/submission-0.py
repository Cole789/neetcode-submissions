# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # repeat for all nodes if they have children {
            # set temp val to left node
            # set left node to right node
            # set right node to temp val
        # }

        if (root == None):
            return None

        tempVal = root.left
        root.left = root.right
        root.right = tempVal

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        