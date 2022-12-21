def validPalindrome(strs: str) -> bool:
    l, r = 0, len(strs) - 1

    while l < r:
        while l < r and not alphanumeric(strs[l]):
            l += 1
        while l < r and not alphanumeric(strs[r]):
            r += 1
        if strs[l].lower() != strs[r].lower():
            return False

        l += 1
        r += 1

    return True


def alphanumeric(self, c):
    return (
        ord('a') <= ord(c) <= ord('z') or
        ord('A') <= ord(c) <= ord('Z') or
        ord('0') <= ord(c) <= ord('9')
    )