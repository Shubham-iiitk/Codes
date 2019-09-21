from  collections import defaultdict
d= {}
for i in range(3):
    key =input("enter the key ")
    values =input("enter the value ")
    d[key]= values
print(d.items())
print(d.keys())
print(d.values())