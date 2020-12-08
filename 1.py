class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width


newRectangle = Rectangle(22, 33)
print(newRectangle.rectangle_area())
b = int(input("Triangle area base : "))
h = int(input("Triangle area height : "))

area = b * h / 2

print("area = ", area)
