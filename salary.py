for _ in range(int(input())):
    a=int(input())
    if a>1500:
        hra=500
        da = a*(98/100)
        gross = a+hra+da
        print(gross)
    elif a<1500:
        hra = a*(10/100)
        da=a*(90/100)
        gross = a+hra+da
        print(gross)
    else:
        print(a)