arr=[8,4,3,5,1,6,2,7]

a=[1,3,5,7]
b=[2,4,6,8]
c=[]
i=0
j=0


while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1

print(i,j)

while i < len(a):
    c.append(a[i])
    i+=1

while j < len(b):
    c.append(b[j])
    j+=1

print(c)
