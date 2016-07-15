# This program illustrates the use of classes

class Door:
    def __init__(self, number, status):
        self.number = number
        self.status = status
        print('constructor')

    def open(self):
        self.status = 'open'

    def close(self):
        self.status = 'closed'
door1 = Door(1, 'closed')
door1.open()
print(door1.number)
print(door1.status)
door1.close()
print(door1.number)
print(door1.status)
