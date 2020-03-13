import unittest
import state_machine

class TestFSA(unittest.TestCase):

    def test_d_recognize(self):
        """
        Test the basic D_Recognize algorithm using the sheep languages discussed in class
        the regex is defined as /^baa+!$/
        """
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

    def test_d_recognize_b(self):
        """
        Tests the second d_recognize function by defining a machine that searches for the sequence "gary" in any string
        """
        states = ["1", "2", "3", "4", "5"]
        domain = ["g", "a", "r", "y"]
        start_state = "1"
        accept_state = ["5"]
        state_table = [("1","g","2"),
                        ("1","a","1"),
                        ("1","r","1"),
                        ("1","y","1"),
                        ("2","a","3"),
                        ("2","g","1"),
                        ("2","r","1"),
                        ("2","y","1"),
                        ("3","r","4"),
                        ("3","g","1"),
                        ("3","a","1"),
                        ("3","y","1"),
                        ("4","y","5"),
                        ("4","g","1"),
                        ("4","a","1"),
                        ("4","r","1"),
                        ("5","g","NULL"),
                        ("5","a","NULL"),
                        ("5","r","NULL"),
                        ("5","y","NULL"),]
        FSA = state_machine.Finite_State_Automata(states,domain,start_state,accept_state,state_table)

        self.assertEqual("ACCEPT", FSA.D_Recognize_b("baaaa baaa gary!"))
        self.assertEqual("REJECT", FSA.D_Recognize_b("lary"))
        self.assertEqual("ACCEPT", FSA.D_Recognize_b("gar gary lary"))
        self.assertEqual("REJECT", FSA.D_Recognize_b("garrrrrry"))
        self.assertEqual("REJECT", FSA.D_Recognize_b("carlin"))
        self.assertEqual("ACCEPT", FSA.D_Recognize_b("asdf&*YR@#UgaryJFES(*FY"))
        self.assertEqual("REJECT", FSA.D_Recognize_b("Gary"))

unittest.main()