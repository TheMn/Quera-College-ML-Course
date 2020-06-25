def weight(x):
    return ord(x) - 64


def value(s):
    res = 0
    for i in range(len(s)):
        res += weight(s[i]) * (i + 1)
    return res


raw = input()

i = 0
while i < len(raw):
    character = raw[i]
    starting = i
    while i < len(raw) and character.lower() == raw[i].lower():
        i += 1
    print(value(raw[starting:i]), end="")
