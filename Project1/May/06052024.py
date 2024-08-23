# import mysql.connector
# cnx = mysql.connector.connect(user='root', password='PRALAY@301',
#                               host='127.0.0.1',
#                               database='dbms')
# mycursor = cnx.cursor()
# alter_query = "ALTER TABLE dept ADD COLUMN namew VARCHAR(30), ADD COLUMN salary DECIMAL(10,2)"
# mycursor.execute(alter_query)
# add_values = [
#     ("d1", "cs", "e101", "John Doe", 50000.00),
#     ("d2", "ec", "e102", "Jane Smith", 60000.00),
#     ("d3", "me", "e103", "David Johnson", 55000.00)
# ]
# insert_query = "INSERT INTO dept (did, dname, eid, namew, salary) VALUES (%s, %s, %s, %s, %s)"
# mycursor.executemany(insert_query, add_values)
# cnx.commit()
# mycursor.close()
# cnx.close
# import heapq
# nums = [1,1,1,1,2,2,3]
# k=2
# dicti={}
# for i in nums:
#     if i not in dicti:
#         dicti[i]=1
#     else:
#         dicti[i]+=1
# print(dicti.items())
# narr=list(dicti.items())
# heapq.heapify(narr)
# for i in range(k):
#     print(heapq.heappop(narr))

# ## reorganize string
# import heapq
# s='aaabc'
# dicti={}
# for i in s:
#     if i not in dicti:
#         dicti[i]=1
#     else:
#         dicti[i]+=1
# ns=[]
# heapq.heapify(ns)
# for c,freq in dicti.items():
#     heapq.heappush(ns,(-freq,c))

# fp,vp=None,None
# result=' '
# while ns or prev is None:
#     fc,vc=heapq.heappop(ns)
#     if vp==vc:
#         fp,vp=fc,vc
#         fc,vc=heapq.heappop(ns)
#     result+=vc
#     fc+=1
#     if fc<0:
#         heapq.heappush(ns,(fc,vc))
#     heapq.heappush(ns,(fp,vp))
# print(result)
# import heapq
# tasks=["A","A","A","B","B","B"]
# dicti={}
# ntasks=[]
# heapq.heapify(ntasks)
# for i in tasks:
#     if i not in dicti:
#         dicti[i]=1
#     else:
#         dicti[i]+=1
# for alph,freq in dicti.items():
#     heapq.heappush(ntasks,[-freq,0,alph])
# k=2
# print(ntasks)
# result=[]
# mid=[]
# while ntasks or mid:
#     if not ntasks:
#         result.append(-1)
#         for i in ntasks:
#             i[1]+=1
#     curr=heapq.heappop(ntasks)
#     print(curr,"current")
#     if curr[1]==0:
#         result.append(curr[2])
#         curr[1]=k
#         curr[0]+=1
#         if curr[0]<0:
#             mid.append(curr)
#         for i in mid:
#             heapq.heappush(ntasks,i)
#     else:
#         curr[1]-=1
#         mid.append(curr)
# print( (result))

# arr=[1,3,4,2]
# stack=[]
# resarr=[0]*len(arr)
# for i in range(len(arr)-1,-1,-1):
#     while stack and stack[-1]<arr[i]:
#         stack.pop()
#     if not stack:
#         resarr[i]=-1
#     else:
#         resarr[i]=stack[-1]
#     stack.append(arr[i])
# print(resarr)
# subarr=[4,1,2]
# for i in range(len(subarr)):
#     for j in range(len(arr)):
#         if arr[j]==subarr[i]:
#             print(subarr[i],"::",resarr[j])

def dfs(s,start,mid):
    if len(mid)==len(s):
        print(int(''.join(mid)))
        return
    elif start>len(s):
        return
    for i in range(0,len(s)):
        if s[i] not in mid:
            mid.append(s[i])
            dfs(s,i+1,mid)
            mid.pop()

dfs('123456',0,[])