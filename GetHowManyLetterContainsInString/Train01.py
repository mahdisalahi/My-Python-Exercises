myText = input('Enter your text: ')

counterDic = dict()

for letter in myText:
    counterDic[letter] = counterDic.get(letter, 0) + 1

