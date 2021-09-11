

#EXAMPLE OF PROTECTED VARIABLE

class exProtected: #created a class named exProtected
    def __init__(self): #defining a function
        self._varProtected = 0 #here is an example of a protected variable which is the same as any other variable but the '_' infront
                                #lets others know not to change

obj = exProtected()           #set object
obj._varProtected = 100
print(obj._varProtected)


#EXAMPLE OF PRIVATE VARIABLE

class regProtected:
    def __init__(self): #all the same as the protected variable example above
        self.__varPriv = 30 # two '_' to show that this will be a private

    def makePriv(self): #created a function
        print(self.__varPriv) #all this function is used for is to print self.varPriv

    def finishPriv(self, private):
        self.__varPriv = private

obj = regProtected() #obj is now regProtected()
obj.makePriv()   #this will print __varPriv which is 30
obj.finishPriv(44) #This is changing __varPriv to 40
obj.makePriv() #were done creating a private var
