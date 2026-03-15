ghad_list_A = []
age_list_A = []
vazn_list_A = []
ghad_list_B = []
age_list_B = []
vazn_list_B = []

class A:
    count = 0
    def __init__(self , ageA , ghadA , vaznA):
        self.ageA = ageA 
        self.ghadA = ghadA
        self.vaznA = vaznA
        A.count += 1
        age_list_A.append(self.ageA)
        ghad_list_A.append(self.ghadA)
        vazn_list_A.append(self.vaznA)

class B:
    count = 0
    def __init__(self , ageB , ghadB , vaznB):
        self.ageB = ageB 
        self.ghadB = ghadB
        self.vaznB = vaznB
        B.count += 1
        age_list_B.append(self.ageB)
        ghad_list_B.append(self.ghadB)
        vazn_list_B.append(self.vaznB) 

howmany_A = input("enter howmany A students: ")
howmany_B = input("howmany B students: ")

for i in range(int(howmany_A)):
    ageA = input("enter your A student age: ")
    ghadA = input("enter your A student ghad: ")
    vaznA = input("enter your A student vazn: ")
    A_student = A(int(ageA) , int(ghadA) , int(vaznA))
for i in range(int(howmany_B)):
    ageB = input("enter your B student age: ")
    ghadB = input("enter your B student ghad: ")
    vaznB = input("enter your B student vazn: ")
    B_student = B(int(ageB) , int(ghadB) , int(vaznB))

jame_age_A = 0
for i in age_list_A:
    jame_age_A = jame_age_A + i
jame_ghad_A = 0
for i in ghad_list_A:
    jame_ghad_A += i
jame_vazn_A = 0
for i in vazn_list_A:
    jame_vazn_A += i
jame_age_B = 0
for i in age_list_B:
    jame_age_B += i
jame_ghad_B = 0
for i in ghad_list_B:
    jame_ghad_B += i
jame_vazn_B = 0
for i in vazn_list_B:
    jame_vazn_B += i

average_age_A = jame_age_A / int(howmany_A)
average_ghad_A = jame_ghad_A / int(howmany_A)
average_vazn_A = jame_vazn_A / int(howmany_A)
average_age_B = jame_age_B / int(howmany_B)
average_ghad_B = jame_ghad_B / int(howmany_B)
average_vazn_B = jame_vazn_B / int(howmany_B)

print(average_age_A)
print(average_ghad_A)
print(average_vazn_A)
print(average_age_B)
print(average_ghad_B)
print(average_vazn_B)

if average_ghad_A > average_ghad_B or average_vazn_A < average_vazn_B:
    print("A")
elif average_ghad_A < average_ghad_B or average_vazn_B < average_vazn_A:
    print("B")
else:
    print("same")