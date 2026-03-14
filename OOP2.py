class Computer: 
    count = 0                                          
    def __init__(self , Ram , Hard , Cpu , Gpu):
        Computer.count += 1
        self.Ram = Ram
        self.Hard = Hard
        self.Cpu = Cpu
        self.Gpu = Gpu

    def value(self):
        return self.Ram + self.Hard + self.Cpu + self.Gpu
    
    def __del__(self):
        Computer.count -= 1

    def Howmany():
        return Computer.count
   
Pc1 = Computer(16 , 1000 , 8 , 4)

#***********************************************************************************************************************

class Laptop(Computer):  
    def __init__(self, Ram, Hard, Cpu, Gpu , Size):
        super().__init__(Ram, Hard, Cpu, Gpu)
        self.Size = Size

    def value(self):
        return super().value() + self.Size

laptop1 = Laptop(12 , 2000 , 4 , 4 , 13)

del laptop1
del Pc1

print(Computer.Howmany())
