#1.Create a class hierarchy for shapes,
# starting with a base class Shape. Then,
# create subclasses like Circle, Rectangle, and Triangle.
# Implement methods to calculate area and perimeter for each shape.

class Shape:
    def __init__(self, name):
        self.name = name
        self.area = 0
        self.perimeter = 0

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def compute_area(self):
        self.area = 3.14 * self.radius * self.radius

    def compute_perimeter(self):
        self.perimeter = 2 * 3.14 * self.radius

    def __str__(self):
        return f"{self.name} with radius {self.radius} has area {self.area} and perimeter {self.perimeter}"


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def compute_area(self):
        self.area = self.length * self.width

    def compute_perimeter(self):
        self.perimeter = 2 * (self.length + self.width)


    def __str__(self):
        return f"{self.name} with length {self.length} and width {self.width} " \
               f"has area {self.area} and perimeter {self.perimeter}"


class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def compute_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        self.area = (semi_perimeter * (semi_perimeter - self.side1) * (semi_perimeter - self.side2)
                     * (semi_perimeter - self.side3)) ** 0.5

    def compute_perimeter(self):
        self.perimeter = self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"{self.name} with side1 {self.side1}, side2 {self.side2} and side3 {self.side3} " \
               f"has area {self.area} and perimeter {self.perimeter}"


circle = Circle("Circle", 5)
circle.compute_area()
circle.compute_perimeter()
print(circle)

rectangle = Rectangle("Rectangle", 5, 6)
rectangle.compute_area()
rectangle.compute_perimeter()
print(rectangle)

triangle = Triangle("Triangle", 3, 4, 5)
triangle.compute_area()
triangle.compute_perimeter()
print(triangle)





