import curses

class Player:
    x = 0
    y = 0

    character = '@'

    def move(self, character):
        c = chr(character)

        if c in (curses.KEY_DOWN, 'j'):
            self.y += 1
        elif c in (curses.KEY_UP, 'k'):
            self.y -= 1
        elif c in (curses.KEY_LEFT, 'h'):
            self.x -= 1
        elif c in (curses.KEY_RIGHT, 'l'):
            self.x += 1

        elif c == 'y':
            self.y -= 1
            self.x -= 1
        elif c == 'u':
            self.y -= 1
            self.x += 1
        elif c == 'b':
            self.y += 1
            self.x -= 1
        elif c == 'n':
            self.y += 1
            self.x += 1

    def set_position(self, x : int, y : int):
        self.x = x
        self.y = y
