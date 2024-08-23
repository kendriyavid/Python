## input with


## midterm syllabus
# 2.5 modules upto access specifers

import re
pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,16}$"
password = input("enter the password")
match = re.match(pattern, password)
if match:
    print("redirecting to homepage")
else:
    print("conditions not matched")


# Question
class employee:
    def __init__(self,ename,salary,eid,dept):
        self.emp_name = ename
        self.emp_id = eid
        self.emp_salary = salary
        self.emp_dept = dept

    def Calculatesalary(self):
        print(self.emp_salary)
    
    def DisplayEmp(self):
        print("name: ", self.emp_name )
        print("id: ", self.emp_id )
        print("salary: ", self.emp_salary)
        print("dept: ", self.emp_dept )


e1 = employee("harshdeep",21000,101,"computerscience")
e1.DisplayEmp()