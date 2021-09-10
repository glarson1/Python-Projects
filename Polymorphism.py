
#created parent class
class Parent:
    fname = "Gary"
    lname = "Smith"

    def getinfo(self): #here's a function for getting first and last name
        entered_fname = input("What is your first name?: ")
        entered_lname = input("What is your last name?: ")
        if (entered_fname == self.fname and entered_lname == self.lname):
            print("Good to see you again {} {}.".format(entered_fname,entered_lname))
        else:
            print("It is nice to meet you {} {}.".format(entered_fname,entered_lname))



#created child class
class Child1(Parent):
    middial_initial = "M"
    favorite_color = "Green"
    lastname = "Richardson" #lastname is var different than lname but serves same purpose

    def getinfo(self):
        entered_fname = input("Tell me your first name?: ")
        entered_lastname = input("Tell me your last name?: ")#wants lastname instead of lname and output sentence is different
        if (entered_fname == self.fname and entered_lastname == self.lastname): 
            print("Look who's back. {} {}.".format(entered_fname,entered_lastname))
        else:
            print("Welcome new member: {} {}.".format(entered_fname,entered_lastname))


class Child2(Parent):
    fingers = 9
    first = "Jamie"
    nickname = "badger"

    def getinfo(self):
        entered_first = input("first name: ") #wants first instead of fname and output sentence is different
        entered_lname = input("last name: ")
        if (entered_first == self.first and entered_lname == self.lname): 
            print("Welcome back {} {}.".format(entered_first,entered_lname))
        else:
            print("You're a new face {} {}.".format(entered_first,entered_lname))

parent = Parent()
parent.getinfo()

child1 = Child1()
child1.getinfo()

child2 = Child2()
child2.getinfo()

    









        
        
