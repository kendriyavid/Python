from abc import ABC, abstractmethod
# class emp(ABC):
#     def works (self):
#         pass

# class emp1(emp):
#     def works(self):
#         print("works in cse")

# class emp2(emp):
#     def works(self):
#         print("works in IT")

# class emp3(emp):
#     def works(self):
#         print("works in HE")

#     e1 = emp1()
#     e1.works()
#     e2 = emp2()
#     e2.works()
#     e3 = emp3()
#     e2.works()


# TAKE CLASS SHAPE 2 METHODS ABSTRACT METHOD INIT DRAW METHOD

# class shape():
#     def __init__(self,shapename):
#         self.shapename = shapename

#     def draw(self,shapename):
#         pass

# class circle(shape):
#     def __init__(self):
#         super().__init__(circle)
#     def draw(self):
#         print("drawing circle")


# class triangle(shape):
#     def __init__(self):
#         super().__init__(triangle)
#     def draw(self):
#         print("drawing traingle")

        
# c1 = circle()
# c1.draw()

# t1 = triangle()
# t1.draw()


# class emp1(ABC):
#     def works(self):
#         pass

# class emp2(ABC):
#     def works (self):
#         pass
# class dept(emp1,emp2):
#     def works1 (self):
#         print("works in ME")
#     def works2 (self):
#         print("works in He")

# d = dept()
# d.works1()
# d.works2()

# class polygon(ABC):
#     ABC.@abstractmethod
#     def display():
#         pass

# class triangle(polygon):
#     def display1(self):
#         print("3 sides")

# t = triangle()
# t.display1()

# p1 = polygon()
# p1.display()


class emp(ABC):
    @abstractmethod
    def project1(self):
        pass
    
    @abstractmethod
    def project2(self):
        pass

class project_details(emp):
    def project1(self):
        return "project name is HTML5"
    
    def project2(self):
        return "Marketing"
    
pd = project_details()
print(pd.project1())
print(pd.project2())