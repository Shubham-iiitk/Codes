list1=[]
n=int(input("enter the length of list "))
for i in range (n):
    list1.append(int(input()))
def insertion(l):
    for j in range(1,len(l)):
        k = l[j]
        m=j-1
        while m>=0 and l[m]>k:
            l[m+1]=l[m]
            m=m-1
        l[m+1]=k
    return l
a = insertion(list1)
print(a)



