board_state = [['| |','| |','| |'],['| |','| |','| |'],['| |','| |','| |']]
def printboard(list):
	for l in list:
		print(''.join(l))
	


		
name = input('What is your name?')
would_you_like_to_play = input('Hello ' + name + ', would you like to play a game?').lower()
if would_you_like_to_play == 'y':
	print('Okay Let\'s play')
	printboard(board_state)
elif would_you_like_to_play == 'n':
	print('Well fine then')
else:
	print('I\'m sorry Hal, I cannot do that')

print('You go first')
turn = 0
win_condition = []
while board_state != win_condition: #While loop that runs throughout the whole function so that if the win condition
	free_square_player = False      #isn't filled then it will loop back to the start in the sequence -> Player turn
	free_square_computer = False    # -> computer turn -> player turn etc until someone has won. Need to add a break for full board

	while free_square_player == False: #This while loop is the players turn
		choice = input('Where would you like to go (type in the form y,z for the coordinates)?').split(',') #Turns players input into coordinates
		choice[0] = int(choice[0]) - 1 #these translate the coordinates to 'Computer speak'
		choice[1] = int(choice[1]) - 1
		if board_state[choice[0][choice[1]]] != '| |': #THIS IS WHERE THE FUNCTION STOPS WORKING. I want to change the board_state[i[j]] into an X
			print('That is not a valid choice, soz')
		else:
			board_state[int(choice[0])[int(choice[1])]] = '|X|'
			free_square = True
		printboard(board_state)
	if board_state == win_condition:
		break
	else:
		while free_square_computer == False: #While loop for the computer's turn but randomly generates numbers
			x_coordinate = randrange(0,3)
			y_coordinate = randrage(0,3)
			if board_state[x_coordinate[y_coordinate]] == '| |':
				board_state[x_coordinate[y_coordinate]] = '|O|'
				free_square_computer = True
		printboard(board_state)
	if board_state == win_condition:
		break
	







