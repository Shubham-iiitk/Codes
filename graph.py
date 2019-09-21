import re
import os
import math
#from matplotlib import pyplot as plt
#fi = "C:\\Users\\HP\\Desktop\\c17.txt"
from collections import deque
with open("test.txt") as f:
    list0 = []
    list1 =[]
    list2 =[]
    list3 =[]
    list4 =[]
    list5 =[]
    list6=[]
    list7 =[]
    m= 0
    for line in f:
       list0.append(line.split())
    #print(list)
    for i in range (len(list0)):
        for j in range (len(list0[i])):
            string = str(list0[i][j])
            for letters in string :
                for  ch in ['(']:
                    if ch in string:
                        string = string.replace(ch, "")
                        list0[i][j] = string
                for ch in [')']:
                    if ch in string:
                        string = string.replace(ch, "")
                        list0[i][j] = string
                for ch in [',']:
                    if ch in string:
                        string = string.replace(ch, "")
                        list0[i][j] = string
            for letter in 'NADXORT':
                string = string.replace(letter, "")
                list0[i][j]=string
    print(list0)
    for i in range(len(list0)):
         for j in range(len(list0[i])):
            string = str(list0[i][0])
            if string.isdigit() == True :
                m =1
         if m ==1 :
          list1.append(list0[i])
    #print(list1)
    for i in range (len(list1)):
        row = []
        for j in range (len(list1[i])):
            if j ==0:
              list2.append(int(list1[i][j]))
            else :
                if list1[i][j].isdigit() == True:
                   row.append(int(list1[i][j]))
        list3.append(row)
    #print(list2)
    #print(list3)
    dict={}
    for i in range(len(list2)):
     dict[list2[i]] = list3[i]
    print("in Dictionary form:-", dict)
    for i in range (len(list2)):
        for j in range (len(list3[i])):
            row = []
            row.append(list2[i])
            row.append(list3[i][j])
            list4.append(row)
    print(list4)
    for i in range (len(list2)):
        a =int(list2[i])
        for j in range (len(list4)):
            for k in range (len(list4[j])):
                if a == list4[j][0]:
                    list5.append(list4[j][1])
                    break
        list5.append(a)
    #print(list5)


    def Remove(list5):
        final = []
        for items in list5:
            if items not in final:
                final.append(items)
        return final
    print(Remove(list5))




































    #a =0
    #b =0
    #for i in range (len(list4)):
        #for j in range(len(list4[i])):
            #a = int(list4[i][j])
            #list5.append(a)
           # set1 = set(list5)
          #  list5 = list(set1)
         #   break
        #z=0
       # for l in range (1,len(list4[i])):
      #          b = int(list4[i][l])
     #           list6.append(b)
    #print(list5)
    #print(list6)
    #for m in range(len(list5)):
          #   d = int(list5[m])
         #    if d in list6:
       #          pass
      #       else:
     #           list7.append(d)
    #print(list7)












