ary = [2,1,4,6,5,7,8,9,3,0,5,67,8,9,3,5,]
largest = ary[0]
smallest = ary [0]

for i in ary:
    if largest < i:
        largest = i
    if smallest > i:
        smallest = i

print(largest)
print(smallest)