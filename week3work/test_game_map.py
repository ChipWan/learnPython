from itertools import chain, cycle
from unittest import TestCase
from unittest.mock import patch, Mock, call

from game_map import GameMap

class TestGameMap(TestCase):
    def setUp(self):
        self.gmap=GameMap(4,3)

    def test_rows(self):
        self.assertEqual(4,self.gmap.rows,"invalid rows")

    def test_cols(self):
        self.assertEqual(3,self.gmap.cols,"invalid cols")

    @patch('random.random',new=Mock(side_effect=chain(cycle([0.3,0.6,0.9]))))
    def test_reset(self):
        self.gmap.reset()
        for i in range(4):
            self.assertEqual(1,self.gmap.get(i,0))
            for j in range(1,3):
                self.assertEqual(0,self.gmap.get(i,j))

    def test_get_set(self):
        self.assertEqual(0,self.gmap.get(0,0),"invalid value")
        self.gmap.set(0,0,1)
        self.assertEqual(1,self.gmap.get(0,0),"invalid value")

    def test_get_neighbor_count(self):
        expected_value=[[8]*3]*4
        self.gmap.cells=[[1]*3]*4
        for i in range(4):
            for j in range(3):
                self.assertEqual(expected_value[i][j],self.gmap.get_neighbor_count(i,j),'%d,%d'%(i,j))
    @patch('game_map.GameMap.get_neighbor_count',new=Mock(return_value=8))
    def test_get_neighbor_count_map(self):
        expected_value=[[8]*3]*4
        self.assertEqual(expected_value,self.gmap.get_neighbor_count_map())

    def test_set_map(self):
        self.assertRaises(TypeError,self.gmap.set_map,{1,2,3})
        self.assertRaises(AssertionError,self.gmap.set_map,[[1]*3]*3)
        self.assertRaises(TypeError,self.gmap.set_map,[['1']*3]*4)
        self.assertRaises(AssertionError,self.gmap.set_map,[[10]*3]*4)

        expected_value=[[1]*3]*4
        self.gmap.set_map(expected_value)
        self.assertEqual(expected_value,self.gmap.cells)

    def test_print_map(self):
        self.gmap.cells=[
            [1,0,1],
            [0,1,1],
            [1,1,1],
            [0,0,0]
        ]
        with patch('builtins.print') as mock:
            self.gmap.print_map()
            mock.assert_has_calls([
                call('1 0 1'),
                call('0 1 1'),
                call('1 1 1'),
                call('0 0 0')
            ])
