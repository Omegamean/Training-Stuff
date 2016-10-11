start_board = [['| |','| |','| |'],['| |','| |','| |'],['| |','| |','| |']]
def printboard(list):
	for l in list:
		print(''.join(l))

name = input('What is your name?')
would_you_like_to_play = input('Hello ' + name + ', would you like to play a game?').lower()
if would_you_like_to_play == 'y':
	print('Okay Let\'s play')
	printboard(start_board)
elif would_you_like_to_play == 'n':
	print('Well fine then')
else:
	print('I\'m sorry Hal, I cannot do that')

print('You go first')
turn = 0
win_condition = 'something'
board_state = []
if board_state != win_condition:
	coordinates = input(print('Where would you like to go (type in the form y,z for the coordinates)?')).split(',')
	start_board = 
