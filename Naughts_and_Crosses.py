board_state_start = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
win_condition = ()
board_state = board_state_start


def start_game(s):
    while s != 'y':
        if s == 'n':
            print('Okay fine then...')
            s = input('Come ooooooon, please? (y/n)')
        elif s == 'y':
            name = input('What is your name?')
            board_state = board_state_start
        else:
            print('I cannot do that Hal...')
            s = input('Try again using only (y/n)')



def check_win(board_state):
    if board_state in win_condition:
        return True
    else:
        return False

def check_draw():
    if ' ' not in board_state:
        print('Oh dear, looks like there\' no more moves left!')
        would_you_like_to_play = input('Would you like to play again? (y/n)')
        start_game(would_you_like_to_play)


def printboard(list):
    for l in list:
        print('|'.join(l))

def end_game():
    if board_state in win_condition:
        print('Well Done, you won! Good Job')
        would_you_like_to_play = print('Would you like to play again?')



class Player:
    def __init__(self,name):
        self.name = input('What is your name?')
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
    def turn():
        turn = True
        while turn:
            x_row = choice_row()
            y_column = choice_column()
            if board_state[x_row][y_column] == 'X' or board_state[x_row][y_column] == 'O':
                print('Square\'s already full idiot') 
            else:
                board_state[x_row][y_column] = 'X'
                turn = False

        return board_state

class AI:
    def turn():
        turn = True
        while turn:
            x_row = randrange(0,3)
            y_column = randrange(0,3)
            if board_state[x_row][y_column] == 'X' or board_state[x_row][y_column] == 'O':
                print('Square\'s already full idiot') 
            else:
                board_state[x_row][y_column] = 'O'
                turn = False
        return board_state




print('You go first')
turn = 0
win_condition = []
while board_state != win_condition: #While loop that runs throughout the whole function so that if the win condition
    free_square_player = False      #isn't filled then it will loop back to the start in the sequence -> Player turn
    free_square_computer = False    # -> computer turn -> player turn etc until someone has won. Need to add a break for full board

    while free_square_player == False: #This while loop is the players turn
        choice_x = input('Where row would you like to go?')
        while choice_x not in range(1,4):
                 #Turns players input into coordinates
            choice[0] = int(choice[0]) - 1 #these translate the coordinates to 'Computer speak'
            choice[1] = int(choice[1]) - 1
        if board_state[choice[0]][choice[1]] != ' ': #THIS IS WHERE THE FUNCTION STOPS WORKING. I want to change the board_state[i[j]] into an X
            print('That is not a valid choice, soz')
        else:
            board_state[int(choice[0])[int(choice[1])]] = 'X'
            free_square = True
        printboard(board_state)
    if board_state == win_condition:
        break
    else:
        while free_square_computer == False: #While loop for the computer's turn but randomly generates numbers
            x_coordinate = randrange(0,3)
            y_coordinate = randrage(0,3)
            if board_state[x_coordinate[y_coordinate]] == ' ':
                board_state[x_coordinate[y_coordinate]] = 'O'
                free_square_computer = True
        printboard(board_state)
    if board_state == win_condition:
        break
    







