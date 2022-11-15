Str = input()
words = Str.strip().split()
Nstr = ""

for word in words:
    Nstr += word[0].upper()+word[1:-1]+word[-1].upper()+" "

print(Nstr)