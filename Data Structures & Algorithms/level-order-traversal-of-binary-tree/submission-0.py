# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque([root])
        res = []

        if not root:
            return []

        while queue:
            nodes_in_curr_lvl = len(queue)
            curr = []

            for _ in range(nodes_in_curr_lvl):
                node = queue.popleft()

                curr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(curr)
        
        return res