
import random
class Dungeon:
    def __init__(self):
        self.newDungeon = []
        self.width = 0
        self.height = 0

    def get_dim(self):
        while True:
            try:
                self.width = int(input("Enter the width of the dungeon: "))
                self.height = int(input('Enter the height of the dungeon: '))
            except ValueError:
                continue
            else:
                break

    def pop_dungeon(self):
        self.get_dim()
        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append('w')
            self.newDungeon.append(row)
    def gen_rooms(self):
        roomlocations = []
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            testlocation = [y, x]
            if testlocation in roomlocations:
                continue
            else:
                roomlocations.append(testlocation)
                break
        self.newDungeon[roomlocations[0][0]] [roomlocations[0][1]] = 'r'
    def print_dungeon(self):
        for y in range(0, self.height):
            for x in range(0, self.width ):
                print(self.newDungeon[y][x], end="")
            print(end='\n')


newDungeon = Dungeon()
print(newDungeon)
newDungeon.pop_dungeon()
newDungeon.gen_rooms()
newDungeon.print_dungeon()
