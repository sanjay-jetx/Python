rows=int(input("enter the row : ")) #6
cols=int(input("enter the col : ")) #5
for row in range(0,rows):
    for col in range(0,cols):
        if (((col == 0 or col == 4) and row!=0) or (row == 0 or row == 3) and (col>0 or col<4)):
            print('*',end=" ")
        else:
            print(end="  ")
    print()