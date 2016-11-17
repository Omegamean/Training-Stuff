import random
Playing = True

class Board():
    def __init__(self): #Finds the board size, generates the empty board, win condition list and empty spaces list
        self._board_size()
        self.board_state = [[' ' for i in range(self.board_size)] for i in range(self.board_size)]
        self.generate_win_condition()
        self.generate_empty_spaces()
    
    def generate_empty_spaces(self):  #Generate the empty spaces from the board size
        self.empty_spaces = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                self.empty_spaces.append([i,j])

    def generate_win_condition(self): #Generates the win condition set from the board size
        self.win_condition = []

        #Vertical Wins
        for i in range(self.board_size):
            _sub_win_condition = []
            for j in range(self.board_size):
                _sub_win_condition.append([i, j])
            self.win_condition.append(_sub_win_condition)

        #Horizontal Wins
        for i in range(self.board_size):
            _sub_win_condition = []
            for j in range(self.board_size):
                _sub_win_condition.append([j, i])
            self.win_condition.append(_sub_win_condition)

            #Top Left Bottomw Right
        _sub_win_condition = []
        for i in range(self.board_size):
            _sub_win_condition.append([i, i])
        self.win_condition.append(_sub_win_condition)
 
            #Top Right Bottom Left
        _sub_win_condition = []
        for i in range(self.board_size):
            _sub_win_condition.append([i, (self.board_size - 1) - i])
        self.win_condition.append(_sub_win_condition)

    def _board_size(self): #Asks the user what size board they want to play on
        self.board_size = int(input("What board size would you like? (N x N)  "))

    def printboard(self): #Simply prints an empty list into a matrix
        for item in self.board_state:
                print('|'.join(item))

    def check_free_spaces(self): #Checks if there are any empty spaces left on the board
        if self.empty_spaces == []:
            return False
        return True

class Game():
    running = True

    def __init__(self): #Generates the board, then the players, then runs the game
        self.board = Board()
        self._generate_players()
        self.run_game()

    def run_game(self): #Runs the game by printing the board, asking who goes first, then loops the turn function until
        self.board.printboard()  #the end of the game
        self.first_turn()
        while self.running == True:
            self.turn()
            self.board.printboard()
            if self.check_win() == True:
            	break
            if self.check_draw() == True:
            	break
            self.change_player()
        self.end_game()

    def first_turn(self): #Finds out who the user would like to go first
        who_goes_first = input("Who should go first? (1/2)  ")
        if who_goes_first == '1':
            self.current_player = self.p1
        elif who_goes_first == '2':
            self.current_player = self.p2
        else:
            print("That's not a player number...")
            self.first_turn()

    def turn(self): #Checks the current player, makes them do a turn based on what type of player they are then
        if self.current_player.player_type == 'H':  #takes the slot they used out of the empty spaces list
            choices = self.current_player.human_choice()
            if choices in self.board.empty_spaces:
                self.board.board_state[choices[0]][choices[1]] = self.current_player.symbol
                self.board.empty_spaces.remove(choices)

            else:
                print('That space is not available douche. Choose again')
                self.turn()
        else:
            choices = self.current_player.ai_choice()
            if choices in self.board.empty_spaces:
                self.board.board_state[choices[0]][choices[1]] = self.current_player.symbol
                self.board.empty_spaces.remove(choices)
            else:
                self.turn()

    def change_player(self): #Checks which players turn it is and then switches it then tells the next person who's go
        if self.current_player == self.p1: # it is
            self.current_player = self.p2
        else:
            self.current_player = self.p1
        print('It is now ' + self.current_player.name + "'s go")

    def check_draw(self): #Checks the empty spaces list and if there is no empty spaces, it's a draw
        if not self.board.check_free_spaces():
            self.running = False
            print("Well great. That's a draw.")
            return True

    def check_win(self): #Checks the board to see if there is a player symbol in all the spaces of each win condition
        for i in range((self.board.board_size * 2) + 2):
                if all(
                    self.board.board_state[self.board.win_condition[i][j][0]][self.board.win_condition[i][j][1]] 
                    == self.current_player.symbol for j in range(self.board.board_size)
                    ):
                    print(self.current_player.name + " wins! Well done")
                    self.running = False
                    return True

    def end_game(self):  #Tells then to bugger off
        print("Game's over, go home now... Unless...")

    def _player1_assignment(self): #Asks the user to say if player 1 is a human or a robot
        self.player1_type = (input("Is player 1 a human or a robot?  (h for Human or a for Ai)"  )).lower()
        if self.player1_type != 'h' and self.player1_type != 'a':
            self._player1_assignment()

    def _player2_assignment(self): #Asks the user to say if player 2 is a human or a robot
        self.player2_type = (input("Is player 2 a human or a robot? (h for Human or a for Ai)  ")).lower()
        if self.player2_type != 'h' and self.player2_type != 'a':
            self._player2_assignment()

    def _generate_player1(self): #Depending on the choice the user made, generates player1 as a Human or Ai
        if self.player1_type == 'h':  #then assigns the player their range of choices based upon the board size
            self.p1 = HumanPlayer()
        else:
            self.p1 = AiPlayer()
        self.p1.choice_range = self.get_board_size()

    def _generate_player1_symbol(self):  #Asks the user which symbol player 1 wants to be
        player1_symbol = input('What symbol would you like player 1 to be? (X or O)  ')
        if player1_symbol == 'X':
            self.p1.symbol = 'X'
        elif player1_symbol == 'O':
            self.p1.symbol = 'O'
        else:
            _generate_player1_symbol()

    def _generate_player2(self):  #Depding on the choice, generates play2 as a Human or AI and assigns the player
        if self.player2_type == 'h':  #their range of choices based on the board_size
            self.p2 = HumanPlayer()
        else:
            self.p2 = AiPlayer()
        self.p2.choice_range = self.get_board_size()

    def _generate_player2_symbol(self): #Depending on what Player1's symbol is, assigns Player2 their symbol
        if self.p1.symbol == 'X':
            self.p2.symbol = 'O'
        elif self.p1.symbol == 'O':
            self.p2.symbol = 'X'
        
    def _generate_players(self): #Running order to generate the players
        self._player1_assignment()
        self._generate_player1()
        self._generate_player1_symbol()
        self._player2_assignment()
        self._generate_player2()
        self._generate_player2_symbol()

    def get_board_size(self): #Used to get the board size in the board object in order to pass it to the player objects
    	return self.board.board_size

class HumanPlayer():
    def __init__(self): #Asks the person their name to be used in all further communications
        self.name = input('What is your name?  ')
        self.player_type = 'H'

    def _choice_row(self): #Gets the person to choose a row within the range of the board size
        choice= int(input('Pick what row you would like  ')) - 1
        if choice not in range(self.choice_range):
            print("That's not in the right format you douche, try again")
            self._choice_row()
        return choice

    def _choice_column(self): #Gets the person to choose a coloumn witihn the range of the board size
        choice = int(input('Pick what column you would like  ')) - 1
        if choice not in range(self.choice_range):
            print("That's not in the right format you douche, try again")
            self._choice_column()
        return choice

    def human_choice(self): #Returns the persons choices as a list
        return [self._choice_row(), self._choice_column()]

class AiPlayer():
    def __init__(self): #The Ai's name is Cotton Eye Joe, where it came from we don't know and where it goes when
        self.player_type = 'A'  #the game is over is also a mystery
        self.name = 'Cotton Eye Joe'

    def ai_choice(self): #The ai chooses random digits in the choice range and returns them as a list
        x_row = int(random.randrange(self.choice_range))
        y_column = int(random.randrange(self.choice_range))
        return [x_row, y_column]

class StatRecorder(): #This class has nothing really in it at the moment, however the idea is to use it to record
    playing = True  #the stats from the game in order to do some statistical analysis on them

    def play_game(self): #Simply asks the person if they want to play a little game...
        s = input('Would you like to play a game? (y/n)  ')
        if s == 'n':
            print('Okay fine then')
            self.playing = False
        elif s == 'y':
            return
        else:
            print("Hello, <Insert Generic Name>. I want to play a game. Up until now, you have spent your life among the dead, piecing together their final moments. You're good at this because, you, like them, are also dead. Dead on the inside. You identify more with a cold corpse than you do with a living human. I believe you want to join your true family, indeed your only family... In death. The device you're wearing is hooked into your rib cage. By the time this tape is finished, you will have one minute to find a way out. At the end of that minute... You should know better than anyone, what happens then. There is a single key that will unlock the harness, <Insert Generic Name>. It is right in front of you. All you have to do is reach in and take it. But do it quickly, the acid will dissolve the key in a matter of seconds. Make your choice.")
            print('Try again using only (y/n)')
            self.play_game()

Recording = StatRecorder()
Recording.play_game()
while Recording.playing == True:
    game=Game()
    Recording.play_game()

  #Look up py charm community
  