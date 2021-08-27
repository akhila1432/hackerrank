(a,b)=map(float,input().split())
if (a%5==0 and b>=(a+0.50)):
    print(b-a-0.50)
else:
    print(b)
