def is_palindrome(s):
    if s == "":
        return False
    for i in range(int(len(s)/2)):
        if s[i].lower() != s[-i-1].lower():
            return False
    return True


def normalize(s):
    res = ""
    for c in s:
        if c.isalpha():
            res = res + c
    return res


n = int(input())
flag = False
palindromes = []

for i in range(n):
    line = input().strip().split()
    for word in line:
        word = normalize(word)
        if is_palindrome(word):
            palindromes.append(word)
            flag = True

if flag is True:
    print("Palindrome words in the text are: ", end="")
    for i in range(len(palindromes)-1):
        print(palindromes[i], ", ", sep="", end="")
    print(palindromes[-1])
else:
    print("No palindrome words found :(")
