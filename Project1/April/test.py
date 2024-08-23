# string= input("enter")
# def ispal(string):
#     lenght=len(string)
#     for i in range(0,lenght//2):
#         if string[i]!=string[lenght-i-1]:
#             return False
#     return True
# bool= ispal(string)
# print(bool)

# Program 2

# l1 = [1,2,3,4,5]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# l2 = [1,2,3,4,5]
# def listeq(l1,l2):
#     len1=len(l1)
#     len2 = len(l2)
#     if l1!=l2:
#         return False
#     for i in range (len1):
#         if l1[i] != l2[i]:
#             return False
#     return True
# print(listeq(l1,l2))

## 21bce10807


import re
pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,16}$"
passwo     
# class Employee:
#     def __init__(self,ename,eid,esalary,edept):
#         self.emp_name = ename
#         self.emp_id = eid
#         self.emp_salary = esalary
#         self.emp_department = edept
#     def calculateSalary(self,salary,hours_worked):
#         overtime=0
#         if hours_worked>50:
#             overtime = hours_worked-50
#             overtimeamt = (overtime*(salary/50))
#         total = salary+overtime
#         return total
#     def print_details(self):
#         print("name:",self.emp_name)
#         print("empid",self.emp_id)
#         print('salary',self.emp_salary)
#         print('department',self.emp_department)
# e1= Employee("Adams","e7876",'50000',"accounting")
# e1.print_details()
