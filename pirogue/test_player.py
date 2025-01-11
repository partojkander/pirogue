import curses
import unittest

from hamcrest import assert_that, equal_to

from .player import Player


class TestPlayer(unittest.TestCase):

    def test_player_get_move(self):
        # given
        player = Player()
        player.set_position(10,10)

        # when
        # then
        assert_that(player.get_move(ord('h')), equal_to((9, 10)))
        assert_that(player.get_move(curses.KEY_LEFT), equal_to((9, 10)))
        assert_that(player.get_move(ord('l')), equal_to((11, 10)))
        assert_that(player.get_move(curses.KEY_RIGHT), equal_to((11, 10)))
        assert_that(player.get_move(ord('j')), equal_to((10, 11)))
        assert_that(player.get_move(curses.KEY_DOWN), equal_to((10, 11)))
        assert_that(player.get_move(ord('k')), equal_to((10, 9)))
        assert_that(player.get_move(curses.KEY_UP), equal_to((10, 9)))

        assert_that(player.get_move(ord('y')), equal_to((9, 9)))
        assert_that(player.get_move(ord('u')), equal_to((11, 9)))
        assert_that(player.get_move(ord('b')), equal_to((9, 11)))
        assert_that(player.get_move(ord('n')), equal_to((11, 11)))

    def test_player_set_position(self):
        # given
        player = Player()
        expected_x, expected_y = 10, 15

        # when
        player.set_position(expected_x, expected_y)

        # then
        assert_that(player.x, equal_to(expected_x))
        assert_that(player.y, equal_to(expected_y))