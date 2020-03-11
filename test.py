import unittest
import state_machine

class TestFSA(unittest.TestCase):

    def test_d_recognize(self):
        states = ["1", "2", "3", "4"]
        domain = ["b", "a", "!"]
        start_state = "1"
        accept_state = ["4"]
        state_table = [("1", "b", "2"),
                       ("2", "a", "3"),
                       ("3", "a", "3"),
                       ("3", "!", "4")]
        FSA = state_machine.Finite_State_Automata(states, domain, start_state, accept_state, state_table)
        
        self.assertEqual("ACCEPT", FSA.D_Recognize("baaaa!"))
        self.assertEqual("REJECT", FSA.D_Recognize("gary"))
        self.assertEqual("REJECT", FSA.D_Recognize("baaaaaaaa"))
        self.assertEqual("ACCEPT", FSA.D_Recognize("baa!"))

unittest.main()