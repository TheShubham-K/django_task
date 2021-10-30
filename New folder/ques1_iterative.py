# iteravtive method

n,x = map(int, input().split(" "))
def func(n,x):
    sum1=1
    for i in range(1,n+1):
        sum1 += (1/(x**i))
    return sum1
sum = func(n,x);
print("sum: {}".format(sum))