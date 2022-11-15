Str = input()

Str = Str.strip().split()
DicKey = set(Str)

Dic = dict()

for key in DicKey:
    Dic[key] = 0

for word in Str:
    Dic[word] += 1
    
for key, value in Dic.items():
    print(key.center(9),"|", str(value).center(5))