import unittest

from hamcrest import assert_that, equal_to

from .room import Room


class TestRoom(unittest.TestCase):

    def test_is_inside_room(self):
        # given
        room = Room(2, 2, 10, 10)

        # when
        # then
        assert_that(room.is_inside_room(0, 0), equal_to(False))
        assert_that(room.is_inside_room(2, 2), equal_to(True))
        assert_that(room.is_inside_room(7, 7), equal_to(True))
        assert_that(room.is_inside_room(11, 11), equal_to(True))
        assert_that(room.is_inside_room(20, 20), equal_to(False))

    def test_can_move_to(self):
        # given
        room = Room(2, 2, 10, 10)

        # when
        # then
        assert_that(room.can_move_to(2, 2), equal_to(False))
        assert_that(room.can_move_to(2, 11), equal_to(False))
        assert_that(room.can_move_to(11, 2), equal_to(False))
        assert_that(room.can_move_to(11, 11), equal_to(False))

        assert_that(room.can_move_to(3, 3), equal_to(True))
        assert_that(room.can_move_to(3, 10), equal_to(True))
        assert_that(room.can_move_to(10, 3), equal_to(True))
        assert_that(room.can_move_to(10, 10), equal_to(True))

        assert_that(room.can_move_to(100, 100), equal_to(True))

    def test_get_middle_of_room(self):
        # given
        # when
        # then
        assert_that(Room(2, 2, 10, 10).get_middle_of_room(), equal_to((6,6)))
        assert_that(Room(0, 0, 5, 5).get_middle_of_room(), equal_to((2,2)))