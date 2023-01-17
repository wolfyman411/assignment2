inp = input("Enter a String:")
string2 = ''
i = len(inp)-1
while i >= 0:
    string2 += inp[i]
    i -= 1
print(string2)