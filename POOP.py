class Car:

    def __init__(self, maker, model, year, color):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color

    def movement(self):
        print(self.model + " is moving")

    def drifting(self):
        print(self.model + " is drifting")
        