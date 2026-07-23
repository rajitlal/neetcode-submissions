class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        if len(s1) > len(s2):
            return False
        
        s1_sorted = sorted(s1)
        
        # A permutation must be the exact same length as s1. 
        k = len(s1)
        
        
       # Iterate through all valid window starting positions
        for i in range(len(s2) - k + 1):
            
            # Extract the window and sort it alphabetically
            subStr = sorted(s2[i : i + k])
            
            
            # If the sorted substring matches the sorted s1, a permutation is found.
            if subStr == s1_sorted:
                return True
                
       
        return False
