# 5.Create a class hierarchy for animals,
# starting with a base class Animal.
# Then, create subclasses like Mammal, Bird, and Fish.
# Add properties and methods to represent characteristics
# unique to each animal group.

class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_habitat(self):
        return self.habitat


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_color):
        super().__init__(name, age, habitat)
        self.fur_color = fur_color

    def get_fur_color(self):
        return self.fur_color

    def __str__(self):
        return f"Group MAMMAL Name: {self.name}\n\tAge: {self.age}\n\tHabitat: {self.habitat}\n\tFur color: {self.fur_color}"


class Bird(Animal):
    def __init__(self, name, age, habitat, feather_color):
        super().__init__(name, age, habitat)
        self.feather_color = feather_color

    def get_feather_color(self):
        return self.feather_color

    def __str__(self):
        return f"Group BIRD Name: {self.name}\n\tAge: {self.age}\n\tHabitat: {self.habitat}\n\tFeather color: {self.feather_color}"


class Fish(Animal):
    def __init__(self, name, age, habitat, scale_color):
        super().__init__(name, age, habitat)
        self.scale_color = scale_color

    def get_scale_color(self):
        return self.scale_color

    def __str__(self):
        return f"Group FISH Name: {self.name}\n\tAge: {self.age}\n\tHabitat: {self.habitat}\n\tScale color: {self.scale_color}"


cat = Mammal("Pisiculin", 2, "Terrestrial (aka Pal residence)", "Black and White")
print(cat)

bird = Bird("Donald Duck", 6, "Terrestrial and Aquatic", "White and Blue")
print(bird)

fish = Fish("Nemo", 1, "Aquatic", "Gold")
print(fish)
