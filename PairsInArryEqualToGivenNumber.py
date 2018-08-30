ary = [2,1,4,6,5,7,8,9,3,0,5,67,8,9,3,5,9]
number = int(input())
temp = []
for i in ary:
    for j in ary:
        if i + j == number and not temp.__contains__(i):
            print(i,j)
            temp.append(i)
            temp.append(j)