Sentence = input("enter the sentence: ")

AllWords = Sentence.split()

CleanWord = []

for Word in AllWords:
    CleanWord.append(Word.strip(".,"))



CleanNumberdWord = []

for i in range(len(CleanWord)):
    a = (i+1 , CleanWord[i])
    CleanNumberdWord.append(a)

for i in CleanNumberdWord:
    if i[1][0].isupper():
        print(i[0] , i[1])