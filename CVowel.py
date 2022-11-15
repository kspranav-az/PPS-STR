Str = input().casefold()

Vowel = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
keys = Vowel.keys()

for ch in Str:
    if ch in keys:
        Vowel[ch] += 1

for key, value in Vowel.items():
    print(key.center(9), "|", str(value).center(7))
