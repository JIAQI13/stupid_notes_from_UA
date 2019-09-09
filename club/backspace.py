instring=input()
outstring=""

# for c in instring:
#     if c=="<":
#         outstring=outstring[:-1]
#     else:
#         outstring+=c
# print(outstring)
for c in instring:
    if c=="<":
        outstring.pop()
    else:
        outsring.append(c)
print("".join(outstring))
