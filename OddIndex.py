Str = input()

i = 0
n = len(Str)
Nstr = ""

while i < n:
    if i % 2 == 0:
        Nstr += Str[i]
    i += 1

print(Nstr)