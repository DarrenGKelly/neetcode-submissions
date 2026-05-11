class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for s in strs:
            encodedString += str(len(s)) + "#" + s

        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrings = []

        while (len(s) != 0):
            i = s.index("#")
            size = int(s[:i])
            decodedStrings.append(s[i+1:i + size + 1])
            s = s[i + 1 + size:]

        return decodedStrings