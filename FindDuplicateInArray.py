ary = [1,3,4,6,3,7,8,9,1,6,1]
temp = []
output = []
for i in ary:
    if temp.__contains__(i):
        if not (output.__contains__(i)):
            output.append(i)

       # print(i)
    else:
       temp.append(i)
print(sorted(output))