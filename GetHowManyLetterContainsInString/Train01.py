myText = input('Enter your text: ')

counterDic = dict()

# add letter as key in dictionary
for letter in myText:
    counterDic[letter] = counterDic.get(letter, 0) + 1

# print letters and the number of repetitions
for key in list(counterDic.keys()):
    print("%s appeared %s times" % (key, counterDic[key]))