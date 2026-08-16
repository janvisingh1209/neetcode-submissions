class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0  # Left pointer for sliding window
        max_freq = 0  # Track the most frequent character count in the window
        res = 0  # Result: max length of valid window
        count = {}  # Dictionary to count characters in the current window

        for right in range(len(s)):  # Right pointer of the window
            count[s[right]] = count.get(s[right], 0) + 1  #counts occurence of letter
            max_freq = max(max_freq, count[s[right]])

            # If the number of letters to change exceeds k, shrink the window
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update result with the current valid window length
            res = max(res, right - left + 1)

        return res

        