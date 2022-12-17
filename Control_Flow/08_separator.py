num = "9.39:392//9821,,e333"
num_set = ""
ch_set = ""

for ch in num:
    if ch.isnumeric():
        num_set += ch

    else:
        ch_set += ch

print("Number set: {0}.".format(num_set))
print("Character set: {0}.".format(ch_set))