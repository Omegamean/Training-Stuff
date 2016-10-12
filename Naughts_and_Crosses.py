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
while board_state != win_condition:
	free_square_player = False
	free_square_computer = False
	while free_square_player == False:
		choice = input('Where would you like to go (type in the form y,z for the coordinates)?').split(',')
		choice[0] = int(choice[0]) - 1
		choice[1] = int(choice[1]) - 1
		if board_state[choice[0][choice[1]]] != '| |':
			print('That is not a valid choice, soz')
		else:
			board_state[int(choice[0])[int(choice[1])]] = '|X|'
			free_square = True
		printboard(board_state)
	if board_state == win_condition:
		break
	else:
		while free_square_computer == False:
			x_coordinate = randrange(0,3)
			y_coordinate = randrage(0,3)
			if board_state[x_coordinate[y_coordinate]] == '| |':
				board_state[x_coordinate[y_coordinate]] = '|O|'
				free_square_computer = True
		printboard(board_state)







