#OOPS= Object Oriented Programming Structure
#Classes, Objects, Attributes, Methods
#Focuses more on real life instances

#Class -> Human
#Objects -> Specific humans -> Shree, Sanjana, John, Matt are objects of Human class with common features
#Attributes -> Features -> example: looks, skin, height, weight, country
#Methods -> Actions -> example: playing, eating for different objects

class Fruits:
    #attributes/features of a class
    def __init__(self, color, taste, shape, preference):
        self.color=color
        self.taste=taste
        self.shape=shape
        self.preference=preference

        
    #class Methods- getters(gets the value) and setters(sets the value to the attribute)

    #getters
    def get_shape(self):
        return self.shape
    
    #setters
    def set_shape(self, new_shape):
        self.shape=new_shape

    #custom methods
    def increase_preference(self):
        self.preference=self.preference+1

    def showFruit(self):
        print("Hello I am a fruit with {},{},{},{}".format(self.color,self.taste,self.shape,self.preference))
    
#creating objects of a class
apple=Fruits("red","sweet sour","circle",3)
apple.showFruit()
print(apple.get_shape())

apple.set_shape("round")
print(apple.get_shape())

apple.increase_preference()
apple.showFruit()

orange=Fruits("orange","sweet","circle",4)
orange.showFruit()
print(orange.get_shape)

orange.set_shape("sphere")
print(orange.get_shape())

orange.increase_preference()
orange.showFruit()