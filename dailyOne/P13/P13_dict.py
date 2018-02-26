# O(N*k)
def longest_substring(s, k):
    if k >= len(s):
        return s

    '''init settings'''
    table = {}  # {current_look, count}
    left = 0  # start point of current candidated string
    max_len = k  # max length of current point

    for i, current_look in enumerate(s):

        if current_look in table:
            table[current_look] = table.get(current_look) + 1  # increment counter if character exist
        else:
            table[current_look] = 1  # Add a new character if not exist

        if len(table) > k:
            max_len = max(max_len, i - left)  # comparing current max VS new candidate

            while len(table) > k:  # reducing counter and move start point to end of candidate
                start_point = s[left]

                if table.get(start_point) is 1:
                    table.pop(start_point)
                else:
                    table[start_point] = table.get(start_point) - 1

                left += 1

    max_len = max(max_len, len(s) - left)  # comparing current max VS new candidate

    return max_len


s = "bbbbbbbbbbbbbccdddddddda"
k = 2
print(longest_substring(s, k))
