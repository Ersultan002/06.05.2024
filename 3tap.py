class Person:
    def __init__(self, name, age,surename):
        self.name=name
        self.age=age
        self.surename=surename

    def my_metod(self):
        

        print("Менің аты жөнім "+self.surename+self.name)
        print("Менің жасым "+self.age)

p1=Person(" Ersultan","17","Mukatay")
p1.my_metod()


class Person2:
    def __init__(self, name, age,surename=""):
        self.name=name
        self.age=age
        self.surename=surename

    def my_metod(self):
        if self.surename:
            print("Менің аты жөнім "+self.surename+self.name)
            print("Менің жасым "+self.age)
        else:
            print("Менің аты жөнім "+self.name)
            print("Менің жасым "+self.age)


        


p1=Person2(" Ersultan","17","Mukatay")
p1.my_metod()

p2=Person2(" Dauren","17")
p2.my_metod()


class Car:
    def __init__(self, mark, model, year):
        self.mark=mark
        self.model=model
        self.year=year

    def my_car(self):
        print(self.mark+self.model+self.year)

p3=Car("Toyota", " Camry ", "2022")
p3.my_car()



