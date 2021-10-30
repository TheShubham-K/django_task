# Recurrsice Method

n = int(input())
x = int(input())
def func(n):
    if(n ==1):
        return 1
    return (1/(x**n))+func(n-1)
sum = func(n);
print("sum: {}".format(sum))