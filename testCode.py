

mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    Lst = []
    for i in color_list:
        msg = "{} {} {}".format(name,mySentence,i)
        Lst.append(msg)
    return Lst



def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("You need to provide your name!")
        elif name == 'Sally':
            print('Sally, you may not use this software.')
        else:
            go = False
    Lst = color_function(name)
    for i in Lst:
        print(i)


get_name()
