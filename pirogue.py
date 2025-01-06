import curses
from curses import wrapper

from level import Level
from player import Player

class Pirogue:

    player : Player = None
    current_level : Level = None

    def __init__(self):
        self.player = Player()
        pass

    def run(self, screen):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        screen.clear()

        k = 0
        y = 0
        while k != ord('q'):
            screen.clear()
            self.current_level.draw(screen)
            new_x, new_y = self.player.get_move(k)
            if (self.current_level.player_can_move_to(new_x, new_y)):
                self.player.set_position(new_x, new_y)

            screen.addstr(self.player.y, self.player.x, self.player.character)
            screen.refresh()
            y = y + 1
            k = screen.getch()

        curses.endwin()

    def set_level(self, current_level : Level):
        self.current_level = current_level


def main(stdscr):
    p = Pirogue()
    l = Level(50, 20)
    p.set_level(l)
    p.run(stdscr)

if __name__ == '__main__':
    wrapper(main)
