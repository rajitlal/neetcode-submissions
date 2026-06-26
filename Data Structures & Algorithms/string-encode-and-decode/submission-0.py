class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Find the separator to get the length of the word
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # Move pointer past the '#' to get the actual string
            i = j + 1
            word = s[i : i + length]
            res.append(word)

            # Move the pointer to the start of the next encoded string
            i += length

        return res
