def encode(strs: list[str]) -> str:
    result = ""

    for s in strs:
        result += len(s) + "#" + s

    return result


def decode(strs: str) -> list[str]:
    result, i = [], 0

    while i < len(strs):
        j = i

        while strs[j] != "#":
            j += 1

        len_ = int(strs[i:j])
        result.append(strs[j+1 : j + 1 + len_])
        i = j + 1

    return result

