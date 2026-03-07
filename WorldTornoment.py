print("Example: Iran - Spain : 2-2")

a = input("Iran - Spain: ")
b = input("Iran - Porteghal: ")
c = input("Iran - Marakesh: ")
d = input("Spain - Porteghal: ")
e = input("Spain - Marakesh: ")
f = input("Porteghal - Marakesh: ")

Teams = {
    "Iran": {"Wins":0 , "Loses":0 , "GoalDifference":0 , "Point":0},
    "Spain": {"Wins":0 , "Loses":0 , "GoalDifference":0 , "Point":0},
    "Portugal": {"Wins":0 , "Loses":0 , "GoalDifference":0 , "Point":0},
    "Marakesh": {"Wins":0 , "Loses":0 , "GoalDifference":0 , "Point":0}
}

IranGoal_a , SpainGoal_a = a.split("-")
IranGoal_b, PortugalGoal_b = b.split("-")
IranGoal_c, MarakeshGoal_c = c.split("-")
SpainGoal_d, PortugalGoal_d = d.split("-")
SpainGoal_e, MarakeshGoal_e = e.split("-")
PortugalGoal_f, MarakeshGoal_f = f.split("-")

# بازی Iran - Spain
IranGoal_a = int(IranGoal_a)
SpainGoal_a = int(SpainGoal_a)

# بازی Iran - Portugal
IranGoal_b = int(IranGoal_b)
PortugalGoal_b = int(PortugalGoal_b)

# بازی Iran - Marakesh
IranGoal_c = int(IranGoal_c)
MarakeshGoal_c = int(MarakeshGoal_c)

# بازی Spain - Portugal
SpainGoal_d = int(SpainGoal_d)
PortugalGoal_d = int(PortugalGoal_d)

# بازی Spain - Marakesh
SpainGoal_e = int(SpainGoal_e)
MarakeshGoal_e = int(MarakeshGoal_e)

# بازی Portugal - Marakesh
PortugalGoal_f = int(PortugalGoal_f)
MarakeshGoal_f = int(MarakeshGoal_f)

Matches = [
    ("Iran" , "Spain" , IranGoal_a , SpainGoal_a),
    ("Iran", "Portugal", IranGoal_b, PortugalGoal_b),
    ("Iran", "Marakesh", IranGoal_c, MarakeshGoal_c),
    ("Spain", "Portugal", SpainGoal_d, PortugalGoal_d),
    ("Spain", "Marakesh", SpainGoal_e, MarakeshGoal_e),
    ("Portugal", "Marakesh", PortugalGoal_f, MarakeshGoal_f)
]

for Team1 , Team2 , Goal1 , Goal2 in Matches:

    if Goal1 > Goal2:
        Teams[Team1]['Wins'] += 1
        Teams[Team2]['Loses'] += 1
        Teams[Team1]['Point'] += 3

    elif Goal2 > Goal1:
        Teams[Team1]['Loses'] += 1
        Teams[Team2]['Wins'] += 1
        Teams[Team2]['Point'] += 3       

    else:
        Teams[Team1]['Point'] += 1       
        Teams[Team2]['Point'] += 1

    Teams[Team2]["GoalDifference"] += (Goal2-Goal1)
    Teams[Team1]["GoalDifference"] += (Goal1-Goal2)   




print(f"Iran Wins: {Teams['Iran']['Wins']} Loses: {Teams['Iran']['Loses']} GoalDifference: {Teams['Iran']['GoalDifference']} Point: {Teams['Iran']['Point']}")
print(f"Spain Wins: {Teams['Spain']['Wins']} Loses: {Teams['Spain']['Loses']} GoalDifference: {Teams['Spain']['GoalDifference']} Point: {Teams['Spain']['Point']}")
print(f"Portugal Wins: {Teams['Portugal']['Wins']} Loses: {Teams['Portugal']['Loses']} GoalDifference: {Teams['Portugal']['GoalDifference']} Point: {Teams['Portugal']['Point']}")
print(f"Marakesh Wins: {Teams['Marakesh']['Wins']} Loses: {Teams['Marakesh']['Loses']} GoalDifference: {Teams['Marakesh']['GoalDifference']} Point: {Teams['Marakesh']['Point']}")
