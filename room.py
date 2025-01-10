from curses import window

class Room:
    x_offset : int = None
    y_offset : int = None
    height : int = None
    width : int = None

    floor = '.'
    wall = '#'

    def __init__(self, x_offset, y_offset, height, width):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.height = height
        self.width = width

    def draw(self, screen : window):
        screen.addstr(self.y_offset, self.x_offset, self.wall * self.width)
        for i in range(self.y_offset+1, self.y_offset + self.height-2 ):
            screen.addstr(i, self.x_offset, self.wall + self.floor * (self.width-2) + self.wall)
        screen.addstr(self.y_offset + self.height-2, self.x_offset, self.wall * self.width)

    def is_inside_room(self, x, y):
        return (self.x_offset <= x < self.x_offset + self.width) and \
               (self.y_offset <= y < self.y_offset + self.height-1)

    def can_move_to(self, x, y):
        if not self.is_inside_room(x, y):
            # We don't know that the player _cannot_ move there, so return true
            return True
        if y == self.y_offset or y == self.y_offset + self.height-2:  # In top or bottom wall
            return False
        if x == self.x_offset or x == self.x_offset + self.width-1:   # In left or right wall
            return False

        return True