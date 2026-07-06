class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int: 
        seen = set() 
        left = 0 
        longest = 0 
        for right in range(len(s)): 
            # shrink window from left while duplicate exists 
            while s[right] in seen: 
                seen.remove(s[left]) 
                left += 1 
            # add current character to window 
            seen.add(s[right]) 
            # update longest if current window is bigger 
            longest = max(longest, right - left + 1) 
        return longest