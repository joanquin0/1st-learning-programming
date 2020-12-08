class Bird:
    def __init__(self):
        print("Bird is the class")

    def info(self):
        print("Bird")

    def swim(self):
        print("Go Bird Swim")
#child Class

class Parrot(Bird):
    def __init__(self):
        super().__init__()
        print("Parrot is the class")

    def info(self):
        print("Parrot")

    def run(self):
        print("Run Boy Faster!")

parro = Parrot()
parro.info()
parro.swim()