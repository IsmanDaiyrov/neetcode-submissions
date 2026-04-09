# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        level = 1

        if not root:
            return []

        while queue:
            nodes_in_curr_level = len(queue)
            curr = [] # to append curr values in iteration

            for _ in range(nodes_in_curr_level):
                node = queue.popleft()
                curr.append(node.val)

                # append any children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # determine the level
            if level % 2 == 0:
                res.append(curr[::-1])
            else:
                res.append(curr[::1])

            # increment the level
            level += 1

        return res