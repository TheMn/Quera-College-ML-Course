numbers = [int(x) for x in input().split()]
numbers.sort()
dict = {}
sum = 0
mod_cnt, mod_val = 0, numbers[0]
for number in numbers:
    sum += number
    dict.setdefault(number, numbers.count(number))
    if dict[number] > mod_cnt:
        mod_cnt = dict[number]
        mod_val = number
avg = sum/len(numbers)
mid = numbers[int(len(numbers)/2)]
if len(numbers) % 2 == 0:
    mid = (mid + numbers[int(len(numbers)/2-1)])/2
print("{avg:.2f}".format(avg=avg), "{mid:.2f}".format(mid=mid), mod_val, sep="\n")
