class Solution:
    def longestConsecutive(self, nums):
        # put all numbers in a set 

        num_set = set(nums)
        
        longest = 0
        
        # loop through every unique number once
        for num in num_set:
            
            # only start building a chain from true starting points
            # a number is a starting point if there's nothing one less than it in the set
            if num - 1 not in num_set:
                
                length = 1  # the number itself counts as length 1
                
                # keep extending the chain as long as the next number exists
                # num + length moves forward each time
                while num + length in num_set:
                    length += 1
                
                # update if this chain is the longest seen so far
                longest = max(longest, length)
        
        return longest