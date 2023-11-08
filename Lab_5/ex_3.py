# 3.Create a base class Vehicle with attributes like
# make, model, and year, and then create subclasses
# for specific types of vehicles like Car, Motorcycle, and Truck.
# Add methods to calculate mileage or towing capacity based on
# the vehicle type.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.mileage = None

    def compute_mileage(self, distance_travelled, fuel_consumed):
        self.mileage = distance_travelled / fuel_consumed

    def compute_towing_capacity(self):

        if self.brand == "Ford":
            if self.model == "Edge":
                return 1500
            elif self.model == "Explorer":
                return 2000
        elif self.brand == "Toyota":
            if self.model == "RAV4":
                return 3500
            elif self.model == "Highlander":
                return 5000
        else:
            return 0

    def __str__(self):
        return f"Car {self.brand} {self.model} {self.year} with mileage {self.mileage}" \
               f" and towing capacity {self.compute_towing_capacity()}"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.mileage = None

    def compute_mileage(self, distance_travelled, fuel_consumed):
        self.mileage = distance_travelled / fuel_consumed

    def __str__(self):
        return f"Motorcycle {self.brand} {self.model} {self.year} with mileage {self.mileage}"


class Truck(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.mileage = None

    def compute_mileage(self, distance_travelled, fuel_consumed):
        self.mileage = distance_travelled / fuel_consumed

    def compute_towing_capacity(self):
        if self.brand == "Ford":
            if self.model == "F-150":
                return 13000
        elif self.brand == "Chevrolet":
            if self.model == "Silverado":
                return 6700
        elif self.brand == "Nissan":
            if self.model == "Titan":
                return 9000
        else:
            return 0

    def __str__(self):
        return f"Truck {self.brand} {self.model} {self.year} with mileage {self.mileage} " \
               f" and towing capacity {self.compute_towing_capacity()}"


car = Car("Toyota", "RAV4", 2019)
car.compute_mileage(100, 10)
print(car)

motorcycle = Motorcycle("Honda", "CBR", 2019)
motorcycle.compute_mileage(400, 30)
print(motorcycle)

truck = Truck("Ford", "F-150", 2019)
truck.compute_mileage(1000, 200)
print(truck)

