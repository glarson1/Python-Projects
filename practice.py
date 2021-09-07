
cars = ["Ford", "Nissan", "Chevy", "Toyota"]

for x in cars:
    print(x)

p = cars.count("Ford") #in the list/array cars, count how many "Ford"

print(p)

cars.sort() #ascending order by default

print(cars)

y = lambda a,b : a * b       #created a function
print(y(2,3))

c1 = "red"
c2 = "purple"


print("I like the colors {}, and {}!".format(c1,c2))

w = format(5, 'b') #b stands for binary. Will then print number 5 in binary (101)
print(w)

def getSum(num1,num2):    #created a function
    answer = num1 + num2    #made variable "answer" equal to num1/2 added together
    print("The answer is {}.".format(answer)) #answer will be printed inside of {}

getSum(2,4) #started this non indented because if it was indented it would still be inside
               #the defining function block. getSum(2,4) will run the function getSum


myAdd = getSum #myAdd can now work as getSum function

myAdd(2,4)

help(print)
