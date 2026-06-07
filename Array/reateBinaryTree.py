# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        track = {}
        children = set()
        for parent, child, is_left in descriptions:
            if parent not in track:
                track[parent] = TreeNode(parent)
            if child not in track:
                track[child] = TreeNode(child)
            children.add(child)
            if is_left == 1:
                track[parent].left = track[child]
            else:
                track[parent].right = track[child]
        for key in track:
            if key not in children:
                return track[key]
        






        
