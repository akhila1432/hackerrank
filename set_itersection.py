N = input()
s1 =set(map(int,input().split()))
M =input()
s2 = set(map(int,input().split()))
s1.intersection_update(s2)
print(len(s1))