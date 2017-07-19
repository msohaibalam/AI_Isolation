"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        self.setUp()
        self.game.apply_move((0, 0))
        self.game.apply_move((0, 1))
        minimax_player = game_agent.MinimaxPlayer()
        v = minimax_player.minimax(self.game, 5)
        self.assertTrue(v in [(2, 1), (1, 2)])

    def test_max_value(self):
        self.setUp()
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        minimax_player = game_agent.MinimaxPlayer()
        v = minimax_player.max_value(self.game, 1)
        self.assertEqual(v, 7.0)

    def test_smallGame(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2, width=2, height=3)
        self.game.apply_move((0, 0))
        self.game.apply_move((0, 1))
        minimax_player = game_agent.MinimaxPlayer()
        v = minimax_player.minimax(self.game, 50)
        self.assertEqual(v, (2, 1))

    def test_alphabeta(self):
        reload(game_agent)
        mygame = isolation.Board('Player1', 'Player2', width=9, height=9)
        mygame._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41, 38]
        # self.assertEqual(game_agent.AlphaBetaPlayer().alphabeta(mygame, 2), (3, 2))
        print(mygame.to_string())

    def test_my_alphabeta(self):
        reload(game_agent)
        mygame = isolation.Board('Player1', 'Player2', width=9, height=9)
        mygame._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 32]
        # self.assertEqual(game_agent.AlphaBetaPlayer().alphabeta(mygame, 1), (6, 5))
        print(mygame.to_string())


if __name__ == '__main__':
    unittest.main()
