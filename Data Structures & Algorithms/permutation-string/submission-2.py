class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1. Edge Case Check
        # If s1 is longer than s2, s2 cannot possibly contain a permutation of s1.
        if len(s1) > len(s2):
            return False
        
        # 2. Base Comparison Setup
        # Sort s1 once. This serves as the reference standard.
        # Any valid permutation of s1, when sorted, must match this exact value.
        s1_sorted = sorted(s1)
        
        # 3. Fixed Window Length
        # A permutation must be the exact same length as s1. 
        # Setting 'k' ensures we only check substrings of length len(s1).
        k = len(s1)
        
        # 4. Optimized Loop Boundary
        # Instead of nested loops, we use a single loop.
        # 'len(s2) - k + 1' stops the loop early enough so the window s2[i : i + k] 
        # doesn't overshoot the end of string s2.
        for i in range(len(s2) - k + 1):
            
            # 5. Extract and Sort the Window
            # Slice a substring of length 'k' starting at index 'i'.
            # Sorting it allows a direct, character-by-character comparison with s1_sorted.
            subStr = sorted(s2[i : i + k])
            
            # 6. Permutation Check
            # If the sorted substring matches the sorted s1, a permutation is found.
            if subStr == s1_sorted:
                return True
                
        # 7. Fallback Return
        # If the loop finishes without finding a match, no valid permutation exists.
        return False
