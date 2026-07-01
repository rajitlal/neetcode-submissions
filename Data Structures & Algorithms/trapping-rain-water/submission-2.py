class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty, no water can be trapped
        if not height:
            return 0

        # Initialize two pointers left and right at the ends of the array
        l, r = 0, len(height) - 1
        
        # Track the tallest bar seen so far from the left and right sides
        leftMax, rightMax = height[l], height[r]
        
        # Variable to store the total amount of trapped water
        res = 0
        
        # Loop until the left and right pointers meet in the middle
        while l < r:
            # If the maximum height on the left is smaller, we process the left side
            if leftMax < rightMax:
                l += 1  # Move the left pointer one step to the right
                
                # Update the leftMax if the new bar is taller
                leftMax = max(leftMax, height[l])
                
                # The amount of water trapped at the current bar is (Max Height - Current Height)
                res += leftMax - height[l]
                
            # If the maximum height on the right is smaller or equal, we process the right side
            else:
                r -= 1  # Move the right pointer one step to the left
                
                # Update the rightMax if the new bar is taller
                rightMax = max(rightMax, height[r])
                
                # The amount of water trapped at the current bar is (Max Height - Current Height)
                res += rightMax - height[r]
                
        # Return the total accumulated water
        return res
