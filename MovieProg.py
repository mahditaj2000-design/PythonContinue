print("Janrs : Horror, Romance, Comedy, History , Adventure , Action")

PeopleNumbre = input("Pleas enter people numbre: ")
PeopleNumbre = int(PeopleNumbre)

PeopleNameList = []
Janr1List = []
Janr2List = []
Janr3List = []

for i in range(PeopleNumbre):
    PeopleName_Janr = input("Pleas enter people name and janr: ")
    PeopleName , Janr1 , Janr2 , Janr3 = PeopleName_Janr.split(" ")
    
    PeopleNameList.append(PeopleName)
    Janr1List.append(Janr1)
    Janr2List.append(Janr2)
    Janr3List.append(Janr3)

Horror = 0
Romance = 0
Comedy = 0
History = 0
Adventure = 0
Action = 0

for Janr in Janr1List + Janr2List + Janr3List:

    if Janr == "Horror":
        Horror += 1
    elif Janr == "Romance":
        Romance += 1
    elif Janr == "Comedy":
        Comedy += 1
    elif Janr == "History":
        History += 1
    elif Janr == "Adventure":
        Adventure += 1
    elif Janr == "Action":
        Action += 1
    

MyList = [("Horror",Horror),("Romance",Romance),("Comedy",Comedy),("History",History),("Adventure",Adventure),("Action",Action)]
MyList.sort(key=lambda x:(-x[1] , x[0]))

for GenrName , Genr in MyList:
    print(f"{GenrName} = {Genr}")
