class LongestSubStringWORepeating:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # update start when the character is in used
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used[char] = index

        return max_length


instance = LongestSubStringWORepeating()
longest_substring = instance.lengthOfLongestSubstring("ebdafba")
print(longest_substring)
