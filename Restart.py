Str = input("Enter the string : ")

ch1 = "r"
ch2 = "$"


i = Str.find(ch1)

str1 = Str[:i+1]
str2 = Str[i + 1:]

print(str1 + str2.replace(ch1, ch2, str2.count(ch1)))
