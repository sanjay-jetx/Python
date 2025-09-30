import math
def primenumber(num):
    if num <= 1: 
        print("It is not a prime number")
        return

    is_prime = True
    for i in range(2,math.ceil(num/2)+1): 
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

num = int(input("Enter the number: "))
primenumber(num)
