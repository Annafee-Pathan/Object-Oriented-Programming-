class Parrot:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return self.name + " sings " + song
    
    def dance(self):
        return self.name + " is now dancing"

# instantiate the object
blu = Parrot("Blu", 10)

# call our instance methods
print(blu.sing("Happy"))
print(blu.dance())
