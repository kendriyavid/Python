# ## POLYMORPHISM
# class emp1:
#     def __init__(self,eid,ename):
#         self.eid = eid 
#         self.ename = ename
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in cse")

# class emp2:
#     def __init__(self,eid,ename):
#         self.eid = eid
#         self.ename = ename
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in IT")
 
# class emp3:
#     def __init__(self,eid,ename):
#         self.eid = eid
#         self.ename = ename
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in HE")

# e1 = emp1(101,"Raman")
# e2 = emp2(102,"Ram")
# e3 = emp3(103,"Roshan")

# for x in (e1,e2,e3):
#     x.works()
    
################################################################


# class emp:
#     def __init__(self,eid,ename):
#         self.eid = eid 
#         self.ename = ename
#     def  works(self):
#         print("details")

# class emp1(emp):
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in CSE")

# class emp2(emp):
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in IT")

# class emp3(emp):
#     def  works(self):
#         print(self.eid,"name is ", self.ename)
#         print("works in ME")


# e1 = emp1(101,"Raman")
# e2 = emp2(102,"Ram")
# e3 = emp3(103,"Roshan")

# for x in (e1,e2,e3):
#     x.works()


#################################################################

# class course1:
#     def type(self):
#         print("LTP")
#     def credit(self):
#         print(4)

# class course2:
#     def type(self):
#         print("LP")
#     def credit(self):
#         print(3)


# class course3:
#     def type(self):
#         print("P")
#     def credit(self):
#         print(2)

# def show(self):
#     self.type()
#     self.credit()

# c1 = course1()
# c2 = course2()
# c3 = course3()

# show(c1)
# show(c2)
# show(c3)


# class project(pname, poc, budget):
#     show()
#     print(pname,poc,budget)

# class

## REMOVE DUPLICATES 2

# nums=[0,0,1,1,1,1,2,3,3]
# count =0
# i=0
# while i<len(nums)-1:
#     if nums[i]==nums[i+1]:
#         count+=1
#         if count<2:
#             i+=1            
#         else:
#             nums.pop(i)
#             count-=1
#     else:
#         count = 0
#         i+=1
# print(nums)

