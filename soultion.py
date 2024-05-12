f = open("Elf.txt", "r")






first= -1
last = -1
answer = 0
for i in range(1000):
    string = f.readline()
    first = -1
    last = -1

    for x in string:
        if x.isnumeric():
            if first == -1:
                first = x
            else:
                last = x
        if last == -1:
            last = first
        
    final = int(first)*10+ int(last)
    answer = final + answer


print( answer)