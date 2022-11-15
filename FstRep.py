Str = input()

Str = Str.strip().split()
DicKey = set(Str)

Dic = dict()

for key in DicKey:
    Dic[key] = 0

for word in Str:
    Dic[word] += 1
    if Dic[word] >= 2:
        print(word)
        break
