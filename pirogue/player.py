import curses

class Player:
    x = 0
    y = 0

    character = '@'

    def get_move(self, character) -> (int, int):
        new_x, new_y = self.x, self.y
        c = chr(character)

        if c  == 'j' or character == curses.KEY_DOWN:
            new_y += 1
        elif c == 'k' or character == curses.KEY_UP:
            new_y -= 1
        elif c == 'h' or character == curses.KEY_LEFT:
            new_x -= 1
        elif c == 'l' or character == curses.KEY_RIGHT:
            new_x += 1

        elif c == 'y':
            new_y -= 1
            new_x -= 1
        elif c == 'u':
            new_y -= 1
            new_x += 1
        elif c == 'b':
            new_y += 1
            new_x -= 1
        elif c == 'n':
            new_y += 1
            new_x += 1

        return new_x, new_y

    def set_position(self, x : int, y : int):
        self.x = x
        self.y = y
