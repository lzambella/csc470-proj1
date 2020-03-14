import sys
import state_machine
import load



def main():
    """
    Loads a machine definition from a directory with the proper text files in it and constructs a FSA from it.

    It then checks the input string against the machine and outputs ACCEPT or REJECT
    """
    directory = sys.argv[1]                 # Set the directory to the first cmd arg
    input_string = sys.argv[2]              # input string for the machine

    final_states = load.loadAcceptStates(directory)                        # List of final states
    initial_state = load.loadInitialState(directory)                          # Initial state of the machine
    states = load.loadStates(directory)                             # List of all possible states
    domain = load.loadDomain(directory)                             # Domain of valid inputs
    transition_table = load.load_transition_table(directory)                       # List of table transitions
    print("Machine sucessfully loaded")

    # Define the FSA
    FSA = state_machine.Finite_State_Automata(states, domain, initial_state, final_states, transition_table)
    # Test the input string
    result_a = FSA.D_Recognize(input_string)
    result_b = FSA.D_Recognize_b(input_string)
    print(f"Input string: {input_string}")
    print(f"Result for D1: {result_a}")
    print(f"Result for D2 and D3: {result_b}")

if __name__ == '__main__':
    main()