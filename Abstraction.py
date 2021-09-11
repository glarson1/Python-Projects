from abc import ABC, abstractmethod #have to import ABC to get abstractmethod

class person(ABC):
    def howOld(self, age): #regular method
        print("Your age is: ",age)

    @abstractmethod #abstract method
    def ageYears(self, age):
        pass

class displayAge(person): #inherits from person
    def ageYears(self, age):
        print('You are {} years old'.format(age))

obj = displayAge()   #created an object
obj.howOld("45")
obj.ageYears("45")
        
    




        


