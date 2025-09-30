employee={}
def  add_employee(employee_id,employee_name,salary,department):
    employee[employee_id]={
        "Name"=employee_name,
        "department"=department,
        "salary"=salary
    } 
    print(employee,"added successfully")

def view_employee():
    if employee:
        for employee_id,employee_details in employee.items():
            print("ID :",employee_id)
            print("details :",employee_details)
    else:
        print("No employee added ")
    

# main menu function

def main():
    
    while True:
        
        print("Welcome to the employee database")
        
        print("1. add the employee")
        print("2.view employee")
        print("3.update employee")
        print("4.delete")
        print("5.save to file")
        print("6.load the file")
        print("7.exit")
        
        
        choice=int(input("enter your choice : "))
        if choice == "1":
            employee_id=int(input("enter the id"))
            employee_name=input("enter the name")
            department=int(input("enter the dept"))
            salary=int(input("enter the salary"))
            add_employee(employee_id,employee_name,salary,department)
        elif choice == "2":
            view_employee()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "7":
            pass