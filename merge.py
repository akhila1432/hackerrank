# take a string 
S = "AABCAAADA"
# int is also given  # ignore the comments sujeet
K = 3
# convert the string into list
#list1 = list(s)
# create a empty list  to store the divided 3,3,3 strings
#list2 = []
# finding if  3 is a factorial of length of s  how?
temp = []
len_temp = 0
for item in S:
    len_temp += 1
    if item not in temp:
        temp.append(item)
    if len_temp == K:
        print (''.join(temp))
        temp = []
        len_temp = 0