def minion_game(string):
    # your code goes here
 vowels = 'AEIOU'
 ks1 = 0
 ss2 = 0
 for i in range(len(s)):
    if s[i] in vowels:
        ks1 += (len(s)-i)
    else:
        ss2 += (len(s)-i)

 if ks1 > ss2:
    print ("Kevin", ks1)
 elif ks1 < ss2:
    print ("Stuart", ss2)
 else:
    print ("Draw")
if __name__ == '__main__':
    s = input("type any string? ")
    minion_game(s)