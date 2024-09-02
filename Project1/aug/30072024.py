# ## SEGMENT TREE
# import math
# class solution:
#     def cTree(self,arr,segarr,pos,low,high):
#         mid=(low+high)//2
#         if high==low:
#             segarr[pos]=arr[low]
#             return
#         self.cTree(arr,segarr,2*pos+1,low,mid)
#         self.cTree(arr,segarr,2*pos+2,mid+1,high)
#         segarr[pos]=min(segarr[2*pos+1],segarr[2*pos+2])
    
#     def __init__(self,arr):
#         self.arr=arr
#         self.segarr=[0]*(2**(math.ceil(math.log2(len(n))))-1)
#         self.cTree(arr,segarr)
#         self.lazyarr=[0]*len(self.segarr)
    
#     def _query(self,i,j,low,high,segarr,arr,pos):
#         #total overlap
#         if i<=low and j>=high:
#             return self.segarr[pos]
#         if i>=low or j<=high:
#             return float('inf')
#         mid=(low+high)//2
#         return min(self._query(i,j,low,mid,segarr,arr,2*pos+1),self._query(i,j,mid+1,high,segarr,arr,2*pos+2))
    
#     def _update(self,i,j,low,high,pos,delta):
#         if low>high:
#             return
#        ## nodecheck
#         if self.lazyarr[pos]!=0:
#             self.segarr[pos]+=self.lazyarr[pos]
#             if low!=high:
#                 self.lazyarr[2*pos+1]=self.lazyarr[pos]
#                 self.lazyarr[2*pos+2]=self.lazyarr[pos]
#             self.lazyarr[pos]=0

#         ## total overlap
#         if i>=low and j<=high:
#             self.segarr[pos]+=delta
#             if high!=low:
#                 self.lazyarr[2*pos+1]+=delta
#                 self.lazyarr[2*pos+2]+=delta

#         ## noverlap
#         if i<=low or j>=high:
#             return

#         ## partial overlap
#         mid=(high+low)//2
#         self._update(i,j,low,mid,2*pos+1,delta)
#         self._update(i,j,mid+1,high,2*pos+2,delta)
#         segarr[pos]=min(self._update(i,j,low,mid,pos,delta),self._update(i,j,mid+1,high,pos,delta))

#     def update(self,i,j,delta):
#         self._update(i,j,0,len(self.arr)-1,0,delta)
#     def query(self,i,j):
#         return self._query(i,j,0,len(self.arr)-1,segarr,arr,0)

## Segment Tree
# import math
# class solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.segarr=[0]*((2*(1<<(math.ceil(math.log2(len(arr))))))-1)
#         self.n=len(self.arr)
#         self.lazyarr=[0]*len(self.segarr)
    
#     def initiaize(self,high,low,pos):
#         if high==low:
#             self.segarr[pos]=self.arr[pos]
#             return
#         mid=(high+low)//2
#         self.initiaize(self,mid,low,2*pos+1)
#         self.initiaize(self,high,mid+1,2*pos+2)
#         self.segarr[pos]=min(segarr[2*pos+1],segarr[2*pos+2])

#     def _query(self,i,j,high,low,pos):
#         if high==low:
#             return 
#         ## noverlap
#         if i>high and j<low:
#             return float('inf')
#         ## total overlap:
#         if i<=high and j>=low:
#             return segarr[pos]
#         mid=(high+low)/2
#         return min(self._query(i,j,mid,low,2*pos+1),self._query(i,j,high,mid+1,2*pos+2))
    
#     def _update(self,i,j,low,high,pos):
#         if self.lazyarr[pos]!=0:
#             self.segarr[pos]+=self.lazyarr[pos]
#             if high!=low:
#                 self.segarr[2*pos+1]=self.lazyarr[pos]
#                 self.segarr[2*pos+2]=self.lazyarr[pos]
#             self.lazyarr[pos]=0
        
#         ## Noverlap:
#         if 


#     def update(self,i,j):


#     def query(self,i,j):
#         return self._query(i,j,len(self.arr)-1,0)


# arr=list(map(int,input().split()))
# nq=int(input())
# for _ in range(nq):
#     i,j=map(int,input().split())


## Sparsetable

# class solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.k=math.ceil(math.log2(len(self.arr)))
#         self.sparsetable=[[0]*(k+1) for _ in range(len(self.arr))]

#     def initiaize(self):
#         for i in range(n):
#             self.sparsetable[i][0]=self.arr[i]
        
#         i=0
#         for j in range(n):
#             while i+(1<<j)<=n:
#                 self.sparsetable[i][j]=min(self.sparsetable[i][j-1],self.sparsetable[i+(1<<j)][j-1])
#             i+=1
        
#     def query(self,i,j):
#         width=j-i+1
#         k=math.floor(math.ceil(math.log2(width)))
#         return min(self.sparsetable[i][j-1],self.sparsetable[i+(1<<j)+1][j-1])

## Range sum segment tree
# import math

# class Solution:
#     def __init__(self, arr):
#         self.arr = arr
#         self.n = len(arr)
#         self.segarr = [0] * (2 * (1 << (math.ceil(math.log2(self.n)))) - 1)
#         self.initialize(0, self.n - 1, 0)

#     def initialize(self, low, high, pos):
#         if low == high:
#             self.segarr[pos] = self.arr[low]
#             return
#         mid = (low + high) // 2
#         self.initialize(low, mid, 2 * pos + 1)
#         self.initialize(mid + 1, high, 2 * pos + 2)
#         self.segarr[pos] = self.segarr[2 * pos + 1] + self.segarr[2 * pos + 2]
        
#     def _query(self, i, j, low, high, pos):
#         if i > high or j < low:
#             return 0
#         if i <= low and j >= high:
#             return self.segarr[pos]
#         # Partial overlap
#         mid = (low + high) // 2
#         left_query = self._query(i, j, low, mid, 2 * pos + 1)
#         right_query = self._query(i, j, mid + 1, high, 2 * pos + 2)
#         return left_query + right_query
    
#     def query(self, i, j): 
#         if i < 0 or j >= self.n or i > j:
#             raise ValueError("Invalid query range")
#         return self._query(i, j, 0, self.n - 1, 0)


num=1020
arr=[]
nn=0
while num>0:
    rem=num%10
    if rem==0:
        rem=5
    num=num//10
    arr.append(rem)
arr.reverse()
print(arr)
# num=1020
# print(num)

# print(num//10)
# num=num//10
# print(num//10)