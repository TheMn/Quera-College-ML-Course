inp = input().split()
tag = inp[0]
command = inp[1]
sum = 0
if tag == "food":
    if command == "water":
        sum += 0.5
    elif command == "dinner":
        sum += 1.0
    else:
        sum += 10.0
elif tag == "promote":
    if command == "judge":
        sum += 50.0
    elif command == "minister":
        sum += 80.0
    elif command == "governor":
        sum += 100.0
    else:
        sum += 10.0
elif tag == "travel":
    if command == "ground":
        sum += 45.0
    elif command == "sea":
        sum += 58.0
    else:
        sum += 10.0
else:
    sum += 10.0
print("{result:.1f}".format(result=sum))
