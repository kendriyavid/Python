# ## Access Specifiers
# ## Inheritance
# class emp:
#     name=""
#     def works(self):
#         print("working in CSE")

# class emp1(emp):
#     def display(self):
#         print("my name is ",self.name)
#     def works(self):
#         print("works in IT")

# class emp2(emp):
#     def display(self):
#         print("my name is ",self.name)
#     def works(self):
#         print("works in IT")

# e1 = emp1()
# e1.name = "Rohan"
# e1.works()
# e1.display()

# e1 = emp2()
# e1.name = "Harsh"
# e1.works()
# e1.display()

# ## multilevel inheritance

# # class project1(emp1):
# #     def displayworking(self):
# #         print(self.name,"is working on the project1")
# # p1 = project1()
# # p1.name = "harsh"
# # p1.displayworking()

# ## multiple inheritance

# class project2(emp1,emp2):
#     def displaymanager(self):
#         print(emp1.name,emp2.name)
    
# p2 = project2()
# p2.displaymanager()


# class emp:
#     name=""
#     def empinfo(self):
#         print("emp info is here")

# class dept(emp):
#     def dept_info(self):
#         print("name is",self.name)
#         print("working in CSE")

# class course(dept):
#     def course_info(self):
#         print(self.name,"is taking ML and AI")

# c=course()
# c.name = "Raman"
# c.dept_info()
# c.course_info()
nums = [0,0,1,1,1,1,2,3,3]
i=0
j=0
k=len(nums)-1
while j<k:
    if nums[i]==nums[i+1] and nums[i]==nums[i+2]:
        j=i+2
        while j<len(nums)-1:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            j+=1
        k-=1
        j=i
        

    elif nums[i]==nums[i+1] and nums[i]!=nums[i+2]:
        i = i+2
        j=i
        

    elif nums[i]!=nums[i+1]:
        i+=1
        j=i
        
   
print(nums)
