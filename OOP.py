class Person:
    count = 0
    def __init__(self, Name, Age, Ghad, Vazn):
        self.Name = Name
        self.Age = Age
        self.Ghad = Ghad
        self.Vazn = Vazn
        Person.count += 1

    def GetName(self):
        print(f"Name is {self.Name}")

    def GetAge(self):
        print(f"{self.Name} is {self.Age}")

    def GetInfo(self):
        print((f"Name: {self.Name} Age: {self.Age} Ghad: {self.Ghad} Vazn: {self.Vazn}"))

    def Haowmany():
        print(Person.count)
        

Mahdi = Person("Mahdi", 25, 178, 90)
Sara = Person("Sara", 23, 160, 58)

Mahdi.GetInfo()
Sara.GetInfo()
Person.Haowmany()
        
        