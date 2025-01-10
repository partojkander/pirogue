from curses import window

from room import Room

class Level:
    width = 0
    height = 0
    rooms : list[Room] = []
    tile = '_'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen : window):
        for y in range(0, self.height):
            screen.addstr(y, 0, self.tile * self.width)
        for room in self.rooms:
            room.draw(screen)

    def player_can_move_to(self, x : int, y : int):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:  # Outside of level
            return False
        for room in self.rooms:
            if not room.can_move_to(x, y):   # Collided with room wall
                return False
        return True

    def add_room(self, room : Room):
        self.rooms.append(room)
