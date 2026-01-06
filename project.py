num=int(input("Enter number  "))
temp=num
count=0
while temp>0:
    temp//=10
    count+=1
print(count)