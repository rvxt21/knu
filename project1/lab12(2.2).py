class Transport():
    def __init__(self,number=None,year=None,type=None):
        if not number:
            self.number=input('Enter number: ')
        else:
            self.number=number
        if not year:
            self.year=input('Enter year: ')
        else:
            self.year=year
        if not type:
            self.type=input('Enter type: ')
        else:
            self.type=type
    def output(self):
        print("Год выпуска:",self.year)
        print("Марка автомобиля:",self.type)
        print("Номер автомобиля:",self.number)
class Bus(Transport):
    def __init__(self,maxspeed=None):
        if not maxspeed:
            self.maxspeed=input('Enter maxspeed: ')
        else:
            self.maxspeed=maxspeed
    def output1(self):
        print("Максимальная скорость:",self.maxspeed)

class Car(Transport):
    def __init__(self,places=None):
        if not places:
            self.places=input('Enter places: ')
        else:
            self.places=places
    def output2(self):
        print("Количество мест:",self.places)

car1=Transport()
car1.output()
car2=Transport(1234,2014)
car2.output()
car3=Bus()
car3.output1()
car4=Bus(123)
car4.output1()