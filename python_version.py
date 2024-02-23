'''
Modify the Cat class in “inClass5” to a Dog Class and add a ‘breed’ as an argument
'''

# creating the Dog class
class Dog:
    # The init method or constructor
    def __init__(self, breed):
        # Instance Variable
        self.breed = breed
        # self.color = "
    # methods
    def setColor(self, color):  # this creates a instances variable
        self.color = color
        # Retrieves instance variable
    def getColor(self):
        return self.color

    def __str__(self):
        return (f'breed: {self.breed}, color: {self.color}')

# create the objects
roger = Dog('pug')
sue = Dog('lab')


# setting the color of the objects through the method setColor
roger.setColor('green')
sue.setColor('pink')


# printing the results
# use the getColor to get the color of the dog which we set before
print(f'roger\'s color is {roger.getColor()}')
print(f'sue\'s color is {sue.getColor()}')
print()
print(f'Dog roger: {roger}')
print(f'Dog sue: {sue}')

'''
Results:
roger's color is green
sue's color is pink

Dog roger: breed: pug, color: green
Dog sue: breed: lab, color: pink

'''
