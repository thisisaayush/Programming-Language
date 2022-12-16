def my_solutions(s: str, t: str)-> bool:
    return sorted(s) == sorted(t)

s = "hello"
t = "elloh"

print(my_solutions(s,t))