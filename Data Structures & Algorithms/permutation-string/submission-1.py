class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_sorted = sorted(s1)
        k = len(s1)
        for i in range(len(s2) - k + 1):
            subStr = sorted(s2[i : i + k])
            if subStr == s1_sorted:
                return True
        return False
