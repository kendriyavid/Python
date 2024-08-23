# Implemnetation of trees

# class Node:
#     def __init__(self,key):
#         self.right = None
#         self.left  =None
#         self.val = key

# class BinaryTree(self):
#     def __init__(self):
#         self.root  =None

#     def Append(self,val,node):
#         curr = node
#         if curr.val>val:
#             if curr.left == None:
#                 curr.left = Node(val)
#             else:
#                 Append(val,curr.left)
#         elif curr.val<val:
#             if curr.right == None:
#                 curr.right = Node(val)
#             else:
#                 Append(val,curr.right)
    
#     def Search(self,val):
#         root = self.root
#         search_rec(self,val,root)
    
#     def search_rec(self,val,curr):
#         if curr.val>val:
#             if curr.val == val:
#                 return 1
#             elif curr ==None:
#                 return -1
#             else:
#                 search_rec(val,curr.left)
#         elif curr.val<val:
#             if curr.val == val:
#                 return 1
#             elif curr == None:
#                 return -1
#             else:
#                 search_rec(val,curr.right)


# BINARY TREESclass Node:
# class Node:
#     def __init__(self, val):
#         self.left = None
#         self.val = val
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def append(self, val):
#         self.root = self.recursive_append(self.root, val)

#     def recursive_append(self, node, val):
#         if node is None:
#             return Node(val)
#         if val < node.val:
#             node.left = self.recursive_append(node.left, val)
#         elif val > node.val:
#             node.right = self.recursive_append(node.right, val)
#         return node

#     def recursive_search(self, val):
#         return self.search(val, self.root)

#     def search(self, val, node):
#         if node is None or node.val == val:
#             return node
#         if val < node.val:
#             return self.search(val, node.left)
#         return self.search(val, node.right)

#     def preorder(self,node):
#         if not node:
#             return
#         print(node.val)
#         self.preorder(node.left)
#         self.preorder(node.right)
    
#     def postorder(self,node):
#         if not node:
#             return
#         self.postorder(node.left)
#         self.postorder(node.right)
#         print(node.val)
    
#     def inorder(self,node):
#         if not node:
#             return
#         self.inorder(node.left)
#         print(node.val)
#         self.inorder(node.right)

#     def BFS (self)
# # Example usage:
# tree = BinaryTree()
# tree.append(5)
# tree.append(3)
# tree.append(7)
# tree.append(2)
# tree.append(4)
# n = tree.root
# tree.inorder(n)

## preorder traversal

# result = [0]
# def sfpq(arr,result,n1,n2):
#     if number

# import re
# passw = "Pralay@301"
# pattern = r'^(?=[a-zA-Z0-9])*[a-zA-Z0-9]{8,16}'
# result = re.match(pattern=pattern,string=passw)
# if result:
#     print("successful")
# else:
#     print("nope")

# import re
# pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,16}$"
# password = input("enter the password")
# match = re.search(pattern, password)
# if match:
#     print("redirecting to homepage")
# else:
#     print("conditions not matched")

## POLYMORPHISM


# class bird:
#     def flight(self):
#         print("can fly")
#     def giveeggs(self):
#         print("gives eggs")

# class ostrich(bird):
#     def flight(self):
#         print("cannot fly")

# class sparrow(bird):
#     pass

## inheritance

# class car:
#     def __init__(self):
#         self.name = carname
#         self.company = compname

#     def displayinfo(self):
#         print(self.name)
#         print(self.company)

# class electricvehicle:
#     def __init__(self,name,company,batterysize):
#         super().__init__(name,company)
#         self.batterysize = batterysize
    
## access modifiers
# class person:
#     def __init__(self,name,age,marks):
#         self._name =name
#         self._age = age
#         self.__marks = marks
        
#     def displaystudent(self):
#         print(self.name,self.age,self.marks)

# class student(person):
#     def showmarks(self):
#         print(self.age)

# string = "harshdeepsingh"
# def count(string):
#     dicti = {}
#     for c in string:
#         if c in dicti:
#             dicti[c]+=1
#         elif c not in dicti:
#             dicti[c] = 1
#     return dicti

# print(count(string))

dicti={1:"monday",2:"Tuesday",3:"wednesday",4:"thrsday",5:"friday",6:"saturday"}
userin = int(input("enter number"))
print(dicti[userin])
