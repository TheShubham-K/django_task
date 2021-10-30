x,y,a,b = map(int, input().split(" "))
sm1 = x + (1/y)
df1 = x- (1/y)
sm2 = y + (1/x)
df2 = y- (1/x)
total_sum = ((sm1**a)*(df1**b))/((sm2**a)*(df2**b))

print("{} ".format(total_sum))