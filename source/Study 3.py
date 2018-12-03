a = input("").split(" ")
b = input("").split(" ")
for i in range(len(b)):
    if(int(a[1])>int(b[i])):
        print(b[i])