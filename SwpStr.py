str1 = input()
str2 = input()

str1, str2 = list(str1), list(str2)

str1[0], str1[1],\
str2[0], str2[1] = str2[1], str2[0],\
                   str1[1], str1[0]

Str = "".join(str1), "".join(str2)

print(" ".join(Str))
