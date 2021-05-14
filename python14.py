num=int(input())
max_value=num%10
min_value=num%10
max_count=min_count=0
while num:
    r=num%10
    num//=10
    if max_value<r:
        max_value=r
        max_count=1
    elif r==max_value:
        max_count+=1
    elif min_value>r:
        min_value=r
        min_count=1
    elif r==min_value:
        min_count+=1
print('minimum value:',min_value,'\nmaximum value:',max_value)
print('no. of min values:',max_count,'\nno. of max values:',min_count)
