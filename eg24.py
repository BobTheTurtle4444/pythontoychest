# This program illustrates inheritance
class Door:
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
class SecurityDoor:

    def __init__(self, number):
        self.door = Door(number, 'closed')

    def open(self):
        self.door.open()

    def __getattr__(self, attr):
        return getattr(self.door, attr)
door1 = Door(1, 'open')
door2 = SecurityDoor(1)
print(door1.status)
print(door2.status)
door2.open()
print(door2.status)
