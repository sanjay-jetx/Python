# input = student_report("Sanjay", 85, 90, 75, 95, age=21, college="Panimalar", sport="Cricket")
def student_report(Name,*marks,**details):
    total=0
    print("Name",Name)
    for i in range (0,len(marks)):
        total+= marks[i]
    print("total",total)
    for i,j in details.items():
        print(i,j)
    

student_report("Sanjay", 85, 90, 75, 95, age=21, college="Panimalar", sport="Cricket")