from typing import List


a = "hrtthk" # string taken
list1= list((a)) # converted string to list
set1 = set((list1)) # converted list to set
list2 = list((set1))
list3 = []
for x in list2:
    list3.append((list1.count(x)))
    print(list3)
Max_count=max(list3)
for index in range(len(list3)):
    if list3[index]==Max_count:
        print(list2[index],list3[index])


