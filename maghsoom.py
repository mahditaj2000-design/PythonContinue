AdadList = []
PrimeList = [2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29]
CountList = []

for i in range(10):
    AdadNum = input("Pleas enter the numbre: ")
    AdadList.append(int(AdadNum))

for adad in AdadList:

    count = 0

    for prime in PrimeList:

        if adad % prime == 0:

            count += 1

    CountList.append(count)

MaxCount = 0
MaxAdad = 0

for i in range(len(CountList)):

    count = CountList[i]
    Adad = AdadList[i]

    if count > MaxCount:

        MaxCount = count
        MaxAdad = Adad

    elif count == MaxCount:
        
        if Adad > MaxAdad:

            MaxAdad = Adad
    
print(MaxAdad , MaxCount)

