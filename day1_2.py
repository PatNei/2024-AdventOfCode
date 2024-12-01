from util import load_input

inputo = load_input("day1/2.in")
list1,list2 = zip(*[x.split() for x in inputo])
list1,list2 = list(list1),list(list2)
maxo = 0
setto = set(list1)
for i in setto: 
    maxo += list2.count(i) * int(i)
print(maxo)
