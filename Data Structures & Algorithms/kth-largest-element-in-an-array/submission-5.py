class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return False
        return heapq.nlargest(k,nums)[-1]