inp = input("Enter a String:")
lowercase = []
uppercase = []
pstr = ''
for x in inp:
    if x.isupper():
        uppercase.append(x)
    if x.islower():
        lowercase.append(x)
for x in range(len(lowercase)):
    pstr += lowercase[x]
for x in range(len(uppercase)):
    pstr += uppercase[x]
print(pstr)