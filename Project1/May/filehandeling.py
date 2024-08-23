# f=open('document.txt','r')
# print(f.readlines())
# llines=f.readlines()
# for lines in llines:
#     list.
# print(llines)
try:
    f=open('document.txt','x')
except IOError:
    print('exception is')
# f=open('document.txt','r')
# print(f.readline(-1))

# for i in range(1,5):
#     try:
#         with open(f'file{i}','w') as f:
#             f.write(f"hello there this is file number {i}")
#     except:
#         print("erorr occured")
#     finally:
#         print(f'file number{i} created')
#         f.close()