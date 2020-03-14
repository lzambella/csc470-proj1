import unittest
import state_machine
import load as load_func

class TestFSA(unittest.TestCase):

    def test_d_recognize(self):
        """
        Test the basic D_Recognize algorithm using the sheep languages discussed in class
        the regex is defined as /^baa+!$/
        """
        print("Testing D_recognize")
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
        print("Testing D_recognize_b")
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

    def test_load_file(self):
        """
        Runs file loading functions using the default machine
        """
        print("Testing file loading")
        directory = "alpha_email_recognizer"
        state_list = load_func.loadStates(directory)
        domain = load_func.loadDomain(directory)
        start_state = load_func.loadInitialState(directory)
        accept_states = load_func.loadAcceptStates(directory)
        transition_table = load_func.load_transition_table(directory)
        FSA = state_machine.Finite_State_Automata(state_list, domain, start_state, accept_states, transition_table)

        self.assertEqual("ACCEPT", FSA.D_Recognize("foobar@gmail.com"))
        self.assertEqual("REJECT", FSA.D_Recognize(" foobar@gmail.com"))
        self.assertEqual("REJECT", FSA.D_Recognize("foobar@@gmail.com"))
        self.assertEqual("ACCEPT", FSA.D_Recognize("foo.bar@gmail.co.uk"))
        self.assertEqual("REJECT", FSA.D_Recognize("FOOBAR@GMAIL.COM"))
        self.assertEqual("ACCEPT", FSA.D_Recognize("foo.....bar@gmail.com"))

        self.assertEqual("ACCEPT", FSA.D_Recognize_b("The email is foobar@gmail.com"))
        self.assertEqual("ACCEPT", FSA.D_Recognize_b("foobar@gmail.com is the email"))
        self.assertEqual("ACCEPT", FSA.D_Recognize_b("Send me an email at foobar@gmail.com thanks"))
        self.assertEqual("REJECT", FSA.D_Recognize_b("My email is foobar@@gmail.com"))

unittest.main()