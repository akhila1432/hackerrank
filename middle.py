list = [1,3,7,"this",3,"that",7]

if int(len(list))<2:
  middle = 1                                    #// if it has less than 2 entries, the first entry is the middle one.

elif int(len(list)) %2 == 0 :
  middle = int(len(list)/2)

else: 
  middle = int((len(list)/2) - 1)

print(list[middle])