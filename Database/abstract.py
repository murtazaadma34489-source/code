from abc import ABC, abstractclassmethod

# abrtact is animals 

class Animals:
      @abstractclassmethod

      def sound (self):
            pass
      def eat (self):
            pass
      def move(self):
            pass
      
class Dog(Animals):

      def sound (self):
            print("DOG Brank")

      def eat(self):
            print ("Dog is eat flesh")
      def move (self): 
            print("Bog is move is now are show")  

class Cat(Animals):
      
      def sound (self):
          print ("cat meows")
      def eat (self):
            print ("cat is food in them meet are now are that ")
      def move (self):
            print ("cat is move is fast are now in that is for ")         
my_dog=Dog()
my_cat=Cat()
my_dog.sound()
my_dog.eat()
my_cat.sound()
my_cat.eat()
class Person:
      def __init__(self,name):
            self.__name=name
      def get__name(self):
            return self.__name
      def set__name(self,name):
            self.__name=name      

person1=Person("murtaza")  
# in this are used in accesed in privated in attrbutes ingetiing are now are 
print (person1.get__name())
# modify  privates attributes are used in there are now are that is setter in here 
person1.set__name("murtaza")

print (person1.get__name())