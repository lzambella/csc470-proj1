def main():
    f0 = open('startState.txt','r')
	initial_state = f0.read()
	print("Starting State: " + initialState)
	f0.close()

	f1 = open('states.txt','r')
	count0 = 0
	accept_state = []
	while True: 
		count0 += 1
	  
		# Get next line from file 
		line0 = f1.readline();
	  
		# if line is empty 
		# end of file is reached 
		if not line0: 
			break
		accept_state.append(line0) 
		print("State{}: {}".format(count0, line0.strip())) 
	f1.close()

	f2 = open('alphabet.txt','r')
	count1 = 0
	domain = []
	while True: 
		count1 += 1
	  
		# Get next line from file 
		line1 = f2.readline();
	  
		# if line is empty 
		# end of file is reached 
		if not line1: 
			break
		domain.append(line1)
	f2.close()

	f3 = open('transitionTable.txt','r')
	count2 = 0
	a,b,c = ("","","")
	transition_function = []
	while True: 
		count2 += 1
	  
		# Get next line from file 
		line2 = f3.readline();
	  
		# if line is empty 
		# end of file is reached 
		if not line2: 
			break
		line2.split(",")
		transition_function.append(line2)
	f3.close()

	f4 = open('finalState.txt','r')
	final_state = f4.read()
	print("Final State: " + finalState)
	f4.close()


if __name__ == '__main__':
    main()
