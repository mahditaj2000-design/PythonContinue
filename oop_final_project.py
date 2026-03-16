import random

class Human:
    def __init__(self , name):
        self.name = name

class FootballPlayer(Human):
    def __init__(self, name , team):
        super().__init__(name)
        self.team = team    
    def __str__(self):
        return f"{self.name} , {self.team}"
        
player_list = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]
t_list = ["A" , "B"]

mylist = []

for i in range(22):
    p_random = random.choice(player_list)
    t_random = random.choice(t_list)
    mylist.append(FootballPlayer(p_random , t_random))
    continue

for i in mylist:
    print(i)
















