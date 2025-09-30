for row in range(0,7):
    for col in range(0,5):
        if ((col == 0 and row>=0) or (row == 0 and col<4) or ((col>0 and col<4) and row == 4 or row == 6)):
            print('*',end=" ")
        elif(col == 4 and (row!=0 and row!=6)):
            print('*',end=" ")
        else:
            print(end="  ")
    print()
    