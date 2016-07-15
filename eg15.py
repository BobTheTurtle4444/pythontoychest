# This program illustrates the usage of class variables and methods
class Door:
    color = 'brown'

    def __init__(self, number, status):
        self.number = number
        self.status = status

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'
    @classmethod
    def changeColor(cls,color):
        cls.color = color
door1 = Door(1, 'closed')
door2 = Door(1, 'closed')
print(door1.color)
print(door2.color)
Door.changeColor('Red')
print(door1.color)
print(door2.color)
