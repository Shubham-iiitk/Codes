import re
import os
import math
with open("test2.txt") as f:
    List = []
    InputList = []
    list1 =[]
    list2 =[]
    list3 =[]
    list4 =[]

    for line in f:
       List.append(line.split())
    j = len(List)
    for i in range(j):
            s = str(List[i])
            for letters in s:
              if letters == 'I':
                list4.append( List[i])
    for a in range (len(list4)):
          InputList.append(list4[a][0])
    print(InputList)
    for i in range(j):
        k = len(List[i])
        for m in range (k):
             s = str(List[i][0])
             if s.isdigit():
              list1.append(List[i][m])
    n = len(list1)
    for a in range (n):
        b = str(list1[a])
        if b.isdigit():
            list2.append(int(list1[a]))
        for letters in b:
            if letters == '(':
                r = b.index('(')
                g = b[:r]
                list3.append(g)
    dict = {}
    for i in range(len(list2)):
        dict[list2[i]] = list3[i]
    print("in Dictionary form:-", dict)




