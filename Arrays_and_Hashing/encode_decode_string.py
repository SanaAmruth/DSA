class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(list(map(lambda x: str(len(x))+'#'+x, strs)))

    def decode(self, s: str) -> List[str]:
        i = 0
        L = []
        while i < len(s):
            # Extract length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # Directly parse the length
            i = j + 1  # Move past the `#`
            
            # Extract the word
            word = s[i:i + length]
            L.append(word)
            i += length  # Move to the next encoded string
        
        return L