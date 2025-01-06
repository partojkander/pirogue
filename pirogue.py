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

    def run(self, stdscr):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        stdscr.clear()

        k = 0
        y = 0
        while k != ord('q'):
            stdscr.clear()
            self.current_level.draw(stdscr)
            self.player.move(k)

            stdscr.addstr(self.player.y, self.player.x, self.player.character)
            stdscr.refresh()
            y = y + 1
            k = stdscr.getch()

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
