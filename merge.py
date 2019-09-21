
list1 = list(map (int,input().split()))
print(list1)

def merge(list1):
   if len(list1)>1:
       mid = len(list1)//2
       leftlist = list1[:mid]
       rightlist= list1[mid:]
       merge(leftlist)
       merge(rightlist)
       i,j,k=0,0,0

       while i<len(leftlist)and j<len(rightlist):
           if leftlist[i]<rightlist[j]:
               list1[k]=leftlist[i]
               i =i+1
           else :
               list1[k]=rightlist[j]
               j =j+1
           k =k+1
       while i<len(leftlist):
           list1[k]=leftlist[i]
           i=i+1
           k=k+1
       while j<len(rightlist):
           list1[k]=rightlist[j]
           j=j+1
           k=k+1
merge(list1)
print("sorted list is", list1)
print("enter the number to be searched")
x = int(input())
def binarysearch(list2,l,r,n):
    if r>=l:
        mid = l+(r-l)//2
        if list2[mid]==n:
            return mid
        elif list2[mid]<n:
            return binarysearch(list2, mid+1, r, n)
        else:
            return binarysearch(list2, l, mid-1, n)
    else:
        return -1
I= binarysearch(list1,0,len(list1)-1,x)
print("index position of that number is", I)







