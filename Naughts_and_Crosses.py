board_state = [['| |','| |','| |'],['| |','| |','| |'],['| |','| |','| |']]
def printboard(list):
	for l in list:
		print(''.join(l))


def TurnX(Player):
	coordinates = input('Where would you like to go (type in the form y,z for the coordinates)?').split(',')
	if board_state[coordinates[0]][coordinates[1]] == 'X' or board_state[coordinates[0]][[coordinates[1]] == 'O':
		print('Sorry, that square is occupied - try again')
		TurnX(Player)
	else:
		board_state[coordinates[0]][coordinates[1]] = 'X'

		
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
win_condition = 'something'





