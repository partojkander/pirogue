import curses
from curses import wrapper

from pirogue.level import Level
from pirogue.player import Player
from pirogue.room import Room

class Pirogue:

    player : Player = None
    current_level : Level = None

    def __init__(self):
        self.player = Player()

    def run(self, screen):
        self.set_player_starting_position()
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
            if self.current_level.player_can_move_to(new_x, new_y):
                self.player.set_position(new_x, new_y)

            screen.addstr(self.player.y, self.player.x, self.player.character)
            screen.refresh()
            y = y + 1
            k = screen.getch()

        curses.endwin()

    def set_level(self, current_level : Level):
        self.current_level = current_level

    def set_player_starting_position(self):
        self.player.set_position(*self.current_level.rooms[0].get_middle_of_room())

def main(stdscr):
    p = Pirogue()
    l = Level(50, 20)
    room = Room(2, 2, 5, 5)
    l.add_room(room)
    p.set_level(l)
    p.run(stdscr)

if __name__ == '__main__':
    wrapper(main)
