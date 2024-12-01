# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class cl:
    a = 5

ob = cl()
print(ob.a)

ob.a = 0
print(ob.a)

# class attribute not change but a instance attribute set in class attribute