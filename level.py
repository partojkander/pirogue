from curses import window

class Level:
    width = 0
    height = 0

    tile = '.'

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self, screen : window):
        for y in range(0, self.height):
            screen.addstr(y, 0, self.tile * self.width)

    def player_can_move_to(self, x : int, y : int):
        return (0 <= x < self.width and
                0 <= y < self.height)
