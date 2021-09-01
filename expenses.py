for _ in range(int(input())):
    a,b = map(int,input().split())
    if a>1000:
        c= a*b*(10/100)
        print(format(a*b-c,".6f"))
    else:
        print(format(a*b,".6f"))