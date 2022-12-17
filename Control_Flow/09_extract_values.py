number = "9*666.39=992023{[[[436"
separators = ""

for ch in number:
    if not ch.isnumeric():
        separators += ch

print("Characters: {0}.".format(separators))

values = "".join(ch if ch not in separators else ' ' for ch in number).split()

print([int(val) for val in values])
