file_name = input()
i = 0
while i < len(file_name):
    c = 0
    character = file_name[i]
    while i < len(file_name) and character == file_name[i]:
        i += 1
        c += 1
    print(character, c, sep="", end="")
