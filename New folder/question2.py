n = int(input())
sum =0
for x in range(1,n+1):
    if(1&x):
        sum = (x**2)+1
    else:
        sum = (x**2)-1
    print("{} ".format(sum),end="")