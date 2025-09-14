def longest_substring_without_repeating(s: str) -> str:
    if not s:
        return ""

    left = 0
    max_length = 0
    start_index = 0
    char_map = {}

    for right, current_char in enumerate(s):
        if current_char in char_map and char_map[current_char] >= left:
            left = char_map[current_char] + 1

        char_map[current_char] = right

        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left

    return s[start_index:start_index + max_length]

# Example usage:
s = "abcabcbb"
print(longest_substring_without_repeating(s))  # Output: "abc"
