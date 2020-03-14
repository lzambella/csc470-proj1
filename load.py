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
    return transition_table