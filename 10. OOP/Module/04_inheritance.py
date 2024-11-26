# base class
class Animal:
    def eat(self):
        print("I can eat!")

    def sleep(self):
        print("I can sleep!")

# derived class
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")

# create object of the Dog class
dog1 = Dog()

# calling members of the base calss
dog1.eat()
dog1.sleep()

# calling memeber of the derrived class
dog1.bark()
