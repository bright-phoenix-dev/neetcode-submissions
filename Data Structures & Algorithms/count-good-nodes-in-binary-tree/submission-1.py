# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        q = deque()
        q.append((root, -float("inf")))
        while q:
            curr, maxVal = q.popleft()
            if curr.val >= maxVal:
                ans += 1
            if curr.left:
                q.append((curr.left, max(maxVal, curr.val)))
            if curr.right:
                q.append((curr.right, max(maxVal, curr.val)))
        return ans