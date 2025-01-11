import unittest

from hamcrest import assert_that, equal_to

from .room import Room
from .level import Level


class TestLevel(unittest.TestCase):

    def test_player_can_move_to(self):
        # given
        level = Level(10, 10)
        room = Room(1, 1, 3, 3)
        level.add_room(room)

        # when
        # then
        assert_that(level.player_can_move_to(0, 0), equal_to(True))  # Outside room
        assert_that(level.player_can_move_to(9, 9), equal_to(True))  # Outside room
        assert_that(level.player_can_move_to(1, 1), equal_to(False)) # In wall
        assert_that(level.player_can_move_to(1, 3), equal_to(False)) # In wall
        assert_that(level.player_can_move_to(3, 1), equal_to(False)) # In wall
        assert_that(level.player_can_move_to(2, 2), equal_to(True)) # Inside room
        assert_that(level.player_can_move_to(-1, -1), equal_to(False))     # Not inside level
        assert_that(level.player_can_move_to(12, 12), equal_to(False))    # Not inside level
