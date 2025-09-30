from functools import reduce

nums=[1,3,66,5,22,34,63,234,14]

even=list(filter(lambda i : i%2==0,nums)) #filter

double=list(map(lambda i :i*2,even)) #map

sum=reduce(lambda a,b:a+b,double)

print(even)

print(double)

print(sum)