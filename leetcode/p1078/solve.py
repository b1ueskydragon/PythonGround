class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> [str]:
        res = []
        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
        return res

    # DP, skip larger
    def findOcurrences_(self, text: str, first: str, second: str) -> [str]:
        thirds = []
        chunk = f"{first} {second}"
        chunk_size = len(chunk)
        start_pos = text.find(chunk)  # if not, -1

        while start_pos + 1:  # hasNext char
            text = text[start_pos + chunk_size + 1:]
            space_pos = text.find(" ")
            if space_pos > -1:
                thirds.append(text[:space_pos])
            else:
                if text != '':
                    thirds.append(text)
            start_pos = text.find(chunk)

        return thirds
