'''
Developed by Luke Zambella and Gary  for CSC470 Natural Language Processing
'''
class Finite_State_Automata:
    """
    Class containing functions for defining finite state automata and running finite state machines using textual input
    """
    def __init__(self, state_list, domain, start_state, acceptor_states, state_transition_table):
        """
        Initialize an FSA by its own definition

        Parameters ---
        state_list -> List of all possible states
        domain -> Domain of all symbols that the machine can accept
        start_state -> The starting state of the machine
        acceptor_states -> list of states that are defined as the final accepting states
        state_transition_table -> a list of 3-tuples of each state transition in the format (START_STATE, CHARACTER, TRANSITION_TO)

        """

        self.state_list = state_list
        self.domain = domain
        self.start_state = start_state
        self.acceptor_states = acceptor_states
        self.state_transition_table = state_transition_table

    def D_Recognize(self, input_string):
        """
        Recognizes whether the specificed input is described by our FSA
        Goes through each character in the string and checks the state transition table against it
        This algorithm implies that the match is at the beginning of a string

        params---
        input_string -> input string to check

        returns---
        ACCEPT -> If the input is described by the FSA
        REJECT -> if the input is not described by the FSA
        """
        # First set our first state as the current state
        current_state = self.start_state

        for char in input_string:
            # Check if the state is invalid for whatever reason
            if not (current_state in self.state_list):
                return "REJECT"

            # check the transition table for all items in the current state
            # inefficient way
            transitioned = False
            for tup in self.state_transition_table:         # Go through each item of the table and unack into its components as separate vars
                start, c, transition_to = tup
                if current_state == start and char == c:    # Check if there is a match
                    if transition_to == "NULL":             # if there is a match and the input is to a null state, reject it
                        return "REJECT"
                    else:
                        current_state = transition_to       # Update our current state
                        transitioned = True                 # Mark transitioned as true
                        break                               # Break out of the loop

            if not transitioned:                            # If no state transition occurred then the input character was invalid so reject
                return "REJECT"

        # After entire string has been parsed, check if the current state is an acceptor state
        if (current_state in self.acceptor_states):
            return "ACCEPT"
        else:
            return "REJECT"


    def D_Recognize_b(self, input_string):
        """
        Recognizes whether the specificed input is described by our FSA
        Goes through each character in the string and checks the state transition table against it

        This algorithm works on strings where the match may not be at the beginning of the string or there may be characters after the match
        
        params---
        input_string -> input string to check

        returns---
        ACCEPT -> If the input is described by the FSA
        REJECT -> if the input is not described by the FSA
        """
        # First set our first state as the current state
        current_state = self.start_state

        for char in input_string:
            # Check if the state is invalid for whatever reason
            if not (current_state in self.state_list):
                return "REJECT"

            # check the transition table for all items in the current state
            # inefficient way
            transitioned = False
            for tup in self.state_transition_table:         # Go through each item of the table and unack into its components as separate vars
                start, c, transition_to = tup
                if current_state == start and char == c:    # Check if there is a match
                    if transition_to == "NULL":             # if there is a match and the input is to a NULL then RESET the state machine
                        current_state = self.start_state
                        break
                    else:
                        current_state = transition_to       # Update our current state if there is a valid match
                        transitioned = True                 # Mark transitioned as true
                        break                               # Break out of the loop
                    
            if (current_state in self.acceptor_states):     # If we go into an accept state immediately accept (greedy)
                return "ACCEPT"
            if not transitioned:                            # If no state transition then RESET the state machine
                current_state = self.start_state

        # After entire string has been parsed, check if the current state is an acceptor state
        if (current_state in self.acceptor_states):
            return "ACCEPT"
        else:
            return "REJECT"