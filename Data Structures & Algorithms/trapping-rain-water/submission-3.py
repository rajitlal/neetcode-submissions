class Solution:
    def trap(self, height: List[int]) -> int:
       
        if not height:
            return 0

       
        left, right = 0, len(height) - 1
        
       
        leftMax, rightMax = height[left], height[right]
        
        
        totalWater = 0
        
        # Loop until the left and right pointers meet in center
        while left < right:
            # If the maximum height on the left is smaller, we do the left side
            if leftMax < rightMax:
                left += 1  # Move the left pointer one step to the right
                
                # Update the leftMax if the new bar is taller
                leftMax = max(leftMax, height[left])
                
                # The amount of water trapped at the current bar 
                totalWater += leftMax - height[left]
                
            # If the maximum height on the right is smaller or equal, go through  right 
            else:
                right -= 1  # Move the right pointer one step to the left
                
                # Update the rightMax if the new bar is taller
                rightMax = max(rightMax, height[right])
                
                # The amount of water trapped at the current bar
                totalWater += rightMax - height[right]
                
        # Return the total accumulated water
        return totalWater
