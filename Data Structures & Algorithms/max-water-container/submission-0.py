class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # calculate water 
            water = (right - left) * min(height[left], height[right])
            
            # update max if this is the best we've seen
            max_water = max(max_water, water)
            
            # move the shorter bar inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water