ary = [6,2,1,4,6,1,2,5,7,8,9,3,0,5,6,7,5,8,9,3,5,6,1,2]
#ary = [1,2,3,4,2,3,6,7,8,2,3,2,1,4,7,8,8,8,8]
temp = []
for i in ary:
    sum = 0
    for j in ary:
        if i == j :
            sum = sum +1

    if sum == 2 and  not temp.__contains__(i):
        temp.append(i)

print(temp)