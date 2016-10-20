board_state_start = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
win_condition = ()
board_state = board_state_start
s = None

win_condition = [
	#Horizontal Wins
	[board_state[0][0], board_state[0][1], board_state[0][2]],
	[board_state[1][0], board_state[1][1], board_state[1][2]],
	[board_state[2][0], board_state[2][1], board_state[2][2]],

	#Vertical Wins
	[board_state[0][0], board_state[1][0], board_state[2][0]],
	[board_state[0][1], board_state[1][1], board_state[2][1]],
	[board_state[0][2], board_state[1][2], board_state[2][2]],

	#TR BL
	[board_state[0][0], board_state[1][1], board_state[2][2]],

	#TL BR
	[board_state[0][2], board_state[1][1], board_state[2][0]]
]

class Game():
    def start_game(self):
	    s = input('Would you like to play a game? (y/n)  ')
        if s == 'n':
            print('Okay fine then...')
            start_game(self)
        elif s == 'y':
            board_state = board_state_start
            start_game(self)
        else:
            print('I cannot do that Hal...')
            print('Try again using only (y/n)')
           start_game(self)

def check_win(board_state):
    if board_state in win_condition:
        return True
    else:
        return False

def check_draw():
    if ' ' not in board_state:
        print('Oh dear, looks like there\'s no more moves left!')
        start_game(would_you_like_to_play)


def printboard(list):
    for l in list:
        print('|'.join(l))

def end_game():
    if board_state in win_condition:
        print('Well Done, you won! Good Job')
        would_you_like_to_play = print('Would you like to play again?')



class Player1:
    def __init__(self,name, symbol):
        self.name = input('What is your name?')
        self.symbol = 'X'
        # self.symbol = input('Which symbol would you like? (X/O)')

    def choice_row():
        x=()
        while x not in range(3):
            x= int(input('Pick what row you would like') - 1)
            if x not in range(3):
                print('That\'s not in the right format you douche, try again')
        return x

    def choice_column():
        y=()
        while y not in range(3):
            y= int(input('Pick what column you would like') - 1)
            if y not in range(3):
                print('That\'s not in the right format you douche, try again')
                y = ()
        return y

    def turn(self):
        x_row = choice_row()
        y_column = choice_column()
        if board_state[x_row][y_column] == 'X' or board_state[x_row][y_column] == 'O':
            print('Square\'s already full idiot') 
            turn(self)
        else:
            board_state[x_row][y_column] = self.symbol
            return board_state

class AI():
	def __init__(self, symbol):
		self.symbol = 'O'
    def turn(self):
        x_row = randrange(3)
        y_column = randrange(3)
        if board_state[x_row][y_column] == 'X' or board_state[x_row][y_column] == 'O':
            turn(self)
        else:
            board_state[x_row][y_column] = self.symbol
            return board_state



  # Start the game here with asking the name and then getting into the start game function #
  #Commit the Player1 turn function #
  #Check win condition #
  #Have AI or Player2 do their turn #
  #Check win condition #
  #Repeat until win condition is in there or board is full #
  #Ask if they would like to play again, then ask if they would like to player against a second player or AI again #
  







