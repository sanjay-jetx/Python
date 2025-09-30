for row in range(0,6):
    for col in range(0,5):
        if( (row==0 or row == 5 or row == 2)  and col>0) or (col == 0 and row == 1) or (col == 4 and row == 3):
            print('*',end="  ")
        else:
            print(end="   ")
    print()    