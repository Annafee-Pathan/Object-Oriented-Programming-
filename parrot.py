class Parrot:
    species = "bird"

    def __init__(self, name, age):  # fixed here
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Blu is a", blu.species)
print("Woo is also a", woo.species)

print(blu.name, "is", blu.age, "years old")
print(woo.name, "is", woo.age, "years old")
