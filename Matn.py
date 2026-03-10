Sentence = input("enter the sentence: ")

AllWords = Sentence.split()

NumberdWord = []

for i in range(len(AllWords)):
    a = (i+1 , AllWords[i])
    NumberdWord.append(a)

for i in NumberdWord:
    index = NumberdWord.index(i)
    if index + 1 < len(NumberdWord):
        if i[1].endswith("."):
            NumberdWord.pop(index + 1)

for i in NumberdWord:
    if i[1][0].isupper():
        if NumberdWord.index(i) > 0:
            print(f"{i[0]} {i[1].strip(".")}")
        
