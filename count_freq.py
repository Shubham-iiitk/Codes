
# l = list(map(int,input().split()))
# l1 = [0]*11
# for i in range(len(l)):
#     l1[l[i]]+=1
# print(l1)
#

from collections import Counter

l= [1,2,3,1,3,2,4,2,4,2,1]
c= Counter(l)
print(c)






# l = list(input().split())
# m= {}
# for item in l:
#     if item in m:
#         m[item]+=1
#     else:
#         m[item]=1
# print(m)
# for key in m:
#     if key=='1':
#         print(m[key])



