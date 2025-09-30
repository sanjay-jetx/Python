def E_commerce(price,*discount):
    for i in discount:
        price-= price * i
    return price

print(E_commerce(1000,0.1,10))
