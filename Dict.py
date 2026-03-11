n = input("Pleas enter howmany words in there: ")
TedadWords = int(n)

Dict = []

for i in range(TedadWords):
    Dict.append(input("Pleas enter dict word: ").split())

Sentence = input("Pleas enter the sentence you want me to translate: ").split()

for i in Sentence:
    Found = False

    for ii in Dict:
        if i in ii:
            print(ii[0] , end=" ")
            Found = True
            break
    if Found == False:
        print(i , end=" ")

        
 



