from util import load_input

inputo = load_input("day1/2.in")
list1,list2 = zip(*[x.split() for x in inputo])
list1,list2 = list(list1),list(list2)
list1.sort()
list2.sort()
maxo = 0
for i in range(len(list1)):
    maxo += abs(int(list1[i]) - int(list2[i]))
print(maxo)
