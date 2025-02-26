from util import *

inputo = load_input("day2/2.in")
unsafe = 0
print(len(inputo))
for record in inputo:
    record = [int(x) for x in record.split()]
    isDescending = record[0] > record[-1]
    isViolated = 0 
    for idx in range(0,len(record)-1): 
        print("idx: ",idx)
        idx,idx2,idx3 = min(idx,len(record)-1),min(idx+1,len(record)-1),min(idx+2,len(record)-1)
        i,j,k = int(record[idx]),int(record[idx2]),int(record[idx3])
        diff = abs(i-j)
        diffnext = abs(i-k)
        print(i,j,k)
        if (diff < 1 or diff > 3 ):
            isViolated += 1
            if (isViolated > 0 and diffnext < 1 or diffnext > 3):
                isViolated += 1
                continue 
            else:
                continue

        if(isDescending and i > j):
            print("its ok desc")
            continue
        if (not isDescending and i < j):
            print("its ok asc")
            continue
        if (isViolated < 1 and isDescending and i > k):
            print("violated and ok desc")
            continue
        if (isViolated < 1 and not isDescending and i < k):
            print("violated and ok asc")
            continue
        print("Violation we get here") 
        isViolated += 1
    print(record)

    print("violation count: ",isViolated)
    print()
    if (isViolated > 1):
        unsafe += 1
print(len(inputo) - unsafe)
