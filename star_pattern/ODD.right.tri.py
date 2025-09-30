n=int(input("enter the number :"))
for i in range(n):
    if i%2 == 0:
        continue
    for j in range(i):
        print("*",end=" ")
        i+=2
    print()