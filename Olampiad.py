PeopleNumbre = input("Pleas enter people numbre: ")

InformationList = []

for Information in range(int(PeopleNumbre)):
    PeopleInformation = input("Pleas enter people information: ")
    a = PeopleInformation.split(".")
    a[1] = a[1].capitalize()

    InformationList.append(a)

InformationList.sort(key=lambda x:x[1])

for People in InformationList:
    if People[0] == 'f':
        print(f"{People[0]} {People[1]} {People[2]}")

for People in InformationList:
    if People[0] == 'm':
        print(f"{People[0]} {People[1]} {People[2]}")


