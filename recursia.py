


def longest_unique(s):
    current = ""
    longest = ""

    for ch in s:
        if ch in current:
            current = ch      # начинаем заново
        else:
            current += ch     # добавляем символ

        if len(current) > len(longest):
            longest = current

    return longest, 'legkii'
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0
    best_sub = ""

    for right in range(len(s)):
        # если символ уже есть — сдвигаем левую границу
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_sub = s[left:right + 1]

    return max_len, best_sub


print(longest_unique('abcdeajz'))
print(longest_unique_substring('abcdeajz'))