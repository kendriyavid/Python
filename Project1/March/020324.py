## Recursion

## PROGRAM FOR CALCULATOR


# x = int(input(" enter the first number "))
# y = int(input(" enter the second number "))
# # ops = input(" enter the operation to be done " )


# if ops== "+" or "addition":
#     print( x+y)
# elif ops=="-" or "substraction":
#     print(x-y)
# elif ops=="*" or "multiplication":
#     print(x*y)
# elif ops=="/" or  "division":
#     print(x/y)
# elif ops=="&":
#     print(a&b)
# elif ops=="or":
#     if x<0 or y<0:
#         print("-ve")
#     else:
#         print("positive")
# elif ops=="~":

## nor
# print(~x)

# print(x^y)


# # shift operator
# print(x>>1)


## access specifiers public private


class emp:
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename

    def __display(self):
        print(self.eid)
        print(self.ename)

e = emp(101,"raman")
e__display