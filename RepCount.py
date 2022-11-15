Str = input()
Dic = {}

for ch in set(Str):
    Dic[ch] = 0

for ch in Str:
    Dic[ch] += 1

for key, value in Dic.items():
    if value > 1:
        print(key.center(9), "|", str(value).center(7))
