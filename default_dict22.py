word = ("abced","abcedf","bcde","abcde")
for item in word:
    if len(item)in word:
        print(item.count(item))
         
