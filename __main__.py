import sys
import state_machine

def loadDomain(directory):
    """
    Loads the FSA domain from the specified directories' 'alphabet.txt'
    """
    domain = []
    f2 = open(f'{directory}/alphabet.txt','r')
    count1 = 0
    while True:
        count1 += 1

        # Get next line from file
        line1 = f2.readline().strip()

        # if line is empty
        # end of file is reached
        if not line1:
                break
        domain.append(line1)
    f2.close()
    return domain

def loadStates(directory):
    """
    Loads the state list from states.txt
    """
    states = []
    f1 = open(f'{directory}/states.txt','r')
    count0 = 0
    while True:
        count0 += 1

        # Get next line from file
        line0 = f1.readline().strip()

        # if line is empty
        # end of file is reached
        if not line0:
                break
        states.append(line0)
        #print("State{}: {}".format(count0, line0.strip()))
    f1.close()
    return states


def loadAcceptStates(directory):
    """
    Loads the accept states from finalState.txt
    """
    final_states = []
    f4 = open(f'{directory}/finalState.txt','r')
    buffer = f4.readlines()
    for line in buffer:
        final_states.append(line.strip())
    f4.close()
    return final_states

def loadInitialState(directory):
    """
    Loads the initial state
    """
    f0 = open(f'{directory}/startState.txt','r')
    initial_state = f0.readline().strip()
    f0.close()
    return initial_state


def load_transition_table(directory):
    """
    Loads the transition table into a list of tuples in the format ('current state', 'input', 'transition state')
    """
    transition_table = []
    f3 = open(f'{directory}/transitionTable.txt','r')
    count2 = 0
    while True:
        count2 += 1

        # Get next line from file
        line2 = f3.readline().strip()

        # if line is empty
        # end of file is reached
        if not line2:
                break
        splitstr = line2.split(",")

        transition_table.append((splitstr[0].strip('"'), splitstr[1].strip('"'), splitstr[2].strip('"\n')))
    f3.close()
    
    print(f"{transition_table}")
    return transition_table


def main():
    """
    Loads a machine definition from a directory with the proper text files in it and constructs a FSA from it.

    It then checks the input string against the machine and outputs ACCEPT or REJECT
    """
    directory = sys.argv[1]                 # Set the directory to the first cmd arg
    input_string = sys.argv[2]              # input string for the machine

    final_states = loadAcceptStates(directory)                        # List of final states
    initial_state = loadInitialState(directory)                          # Initial state of the machine
    states = loadStates(directory)                             # List of all possible states
    domain = loadDomain(directory)                             # Domain of valid inputs
    transition_table = load_transition_table(directory)                       # List of table transitions
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