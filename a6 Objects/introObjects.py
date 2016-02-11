# Name:
# Date:
# This scrip goes through the basic syntax of creating an object.
# Objects can encapsulate many variables and functions into one entitiy.

# Class. class is a special word in python, similar to def. It means you are defining a class.

# use UpperCase letter to define a class name.
class Vehicle():
    # class variables go here. They are the same for every object. You can put as many variables as you need.
    numWheels=4



    # to make an object, we need to create an instance of the class.
    # every function parameter must start with self.
    def __init__(self):
        # Constructor code
        # initialize all of the vairables of each object here.
        self.kind="car"
        self.model=""
        self.make=""
        self.year=2000
        self.colour=""
        self.value=3000



    # a function that belongs to an object is called a method. You can create methods inside the class deficnition.
    # In python the way to create a method is the same as making a function.
    def describe(self):
        desc_str = "%s %s is a %s %s worth $%.2f." % (self.model,self.make, self.colour, self.kind, self.value)
        return desc_str

    def setModelMakeColour(self, model,make,colour):
        self.model=model
        self.make=make
        self.colour=colour

    def paint(self,newColour):
        self.colour=newColour


# test code here
# goals: create an object.
# access its variables. change them, print them to verify
# learn the difference between a class and an object.
# use object methods that you created
# have object methods that use other functions or methods.


zippy=Vehicle()
zippy.colour="red"
veronica=Vehicle()
veronica.model="BMW"

print(zippy.describe())
print(veronica.describe())
