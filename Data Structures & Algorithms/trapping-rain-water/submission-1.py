class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0 
        l_max = height[l]
        r = len(height) - 1
        r_max = height[r]
        while l <= r: 
            if l_max < r_max:
                while l <= r and height[l] <= l_max:
                    result += l_max - height[l]
                    l += 1
                l_max = height[l]
            else: 
                while l <= r and height[r] <= r_max:
                    result += r_max - height[r]
                    r -= 1
                r_max = height[r] 
        return result 