def anagram(s: str, t: str)-> bool:
    return sorted(s) == sorted(t)

s = "hello"
t = "elloh"

print(anagram(s,t))