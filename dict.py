dict={1:'one',2:'two',3:'three'}

print(dict)  #b4 inserting

dict[4]='four'

print(dict) #after inserting

dict.update({5 :'five'}) #another method

print(dict)
#------------------------------------------#
print(len(dict)) #length of the dict
 
print(dict.get(5)) #get the value

print(dict.keys())
print(dict.items())

print(dict.pop(2))