def count_bus(n):
    res = 0
    for i in range(n+1):
        res += i*(i+1)/2
    return int(res)

n = int(input())
dict = {}
for i in range(n):
    x = input()
    if x in dict:
        dict[x] = dict[x] + 1
        print(count_bus(dict[x]))
    else:
        dict.setdefault(x, 0)
        print(0)
