def lapindrome(a):
    n = len(a)
    if n%2:
        n = n // 2
        return sorted(a[:n]) == sorted(a[n+1:])
    else:
        n = n // 2
        return sorted(a[:n]) == sorted(a[n:])

for _ in range(int(input())):
    a = input()
    if lapindrome(a):
        print('YES')
    else:
        print('NO')