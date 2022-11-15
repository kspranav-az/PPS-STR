Str = input()

if len(Str) < 3:
    print(Str)
else:
    if Str[-3:].lower() == "ing":
        print(Str + "ly")
    else:
        print(Str + "ing")
