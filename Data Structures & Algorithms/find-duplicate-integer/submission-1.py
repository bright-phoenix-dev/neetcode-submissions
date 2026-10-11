class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)+1
        mem = [False]*(n+1)
        for i in nums:
            if mem[i]==False:
                mem[i] = True
            else:
                return i
        
