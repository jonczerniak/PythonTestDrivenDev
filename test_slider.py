from unittest import TestCase
from slider import Puzzle
puz = Puzzle(3, 3)

class TestPuzzle(TestCase):

    def testInit(self):
        self.assertTrue(puz)

    def testWidth(self):
        self.assertTrue(puz.width == 3)
        self.assertTrue(puz.height == 3)

    def test_get_set_puzzle(self):
        self.assertEqual('1 2 3 4 5 6 7 8 _', puz.get_puzzle(), "testing get puzzle")
        puz_chars = puz.get_puzzle()
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.set_puzzle(puz_chars), "testing set puz")

    def test_puzzle_movements(self):
        puz_chars = puz.get_puzzle()
        puz_array = puz.set_puzzle(puz_chars)

        #test Up
        self.assertEqual([['1','2','3'],['4','5','_'], ['7','8','6']], puz.move_up(puz_array), "testing set puz")
        self.assertEqual([['1','2','_'],['4','5','3'], ['7','8','6']], puz.move_up(puz_array), "testing set puz")
        #test for OOB
        self.assertEqual([['1','2','_'],['4','5','3'], ['7','8','6']], puz.move_up(puz_array), "testing set puz")

        #test Down
        self.assertEqual([['1','2','3'],['4','5','_'], ['7','8','6']], puz.move_down(puz_array), "testing set puz")
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.move_down(puz_array), "testing set puz")
        # test for OOB
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.move_down(puz_array), "testing set puz")

        #test_Left
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','_','8']], puz.move_left(puz_array), "testing set puz")
        self.assertEqual([['1','2','3'],['4','5','6'], ['_','7','8']], puz.move_left(puz_array), "testing set puz")
        #test OOB
        self.assertEqual([['1','2','3'],['4','5','6'], ['_','7','8']], puz.move_left(puz_array), "testing set puz")

        #test Right
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','_','8']], puz.move_right(puz_array), "testing set puz")
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.move_right(puz_array), "testing set puz")
        #test OOB
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.move_right(puz_array), "testing set puz")

        #test Solve
        puz.move_up(puz_array)
        puz.move_left(puz_array)
        self.assertEqual([['1','2','3'],['4','5','6'], ['7','8','_']], puz.solve(), "testing set puz")

        #test Scramble
        self.assertNotEqual([['1','2','3'],['4','5','6'], ['7','8','_']],puz.scramble(),"Testing scramble")

        #test to_s
        self.assertEqual('1 2 3\n4 _ 5\n7 8 6\n', puz.to_s(puz_array))

    #UNCOMMENT TO RUN THE PUZZLE----------------------------------------------------------------------------
    # def test_run_puz(self):
    #     puz.run_puzzle()