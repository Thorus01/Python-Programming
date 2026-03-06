"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os
from copy import deepcopy
import time	#imports the time module which allows us to delay the program
## to run: type python3 main.py into the terminal


'''
HELPER FUNCTIONS
The following 4 functions (horizontal_win,vertical_win,diagonal_up_win and diagonal_down_win) are functions that are used in the end_of_game function
'''

def check_for_win(board,player):

	"""
	Makes a copy of the board and simulates a move in every column. If piece can be dropped in a column, it then checks if this move results in a win.
	If it does result in a win, this column is returned. If there are two or more columns that would result in a win, the leftmost column is returned. 
	
	If there are no possible winning moves, return 0

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:param player: The current player who will be placing the pieces in the simulation
	:return: 0 if no possible winning moves, 1-7 if there is a possible winning column
	"""


	list_of_boards = [] # creates an empty list which will be filled with deep copies of the original board

	for column_check in range(len(board[0])): # place a token in the first column for the first board, second col for second board, etc

		list_of_boards.append(deepcopy(board)) # duplicate board so we can make turns without affecting the original board
		
		drop_success = drop_piece(list_of_boards[column_check],player,column_check+1)

		if drop_success == True: # if the col we're checking is a valid move
			
			if end_of_game(list_of_boards[column_check])== 1 or end_of_game(list_of_boards[column_check])==2:
				# that's a win 
				return column_check + 1

	return 0 # this will happen if none of the columns resulted in a win

def horizontal_win(board):
	"""
	Checks if a horizontal - win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	for row in range(6): # check every row
		for starting_col in range(4): 
			# start from the LHS of the board and then move across by one column with each iteration

			# make comparisons between 4 consecutive spaces in the board
			if board[row][starting_col] == board[row][starting_col+1] == board[row][starting_col+2] == board[row][starting_col+3]!=0:
				# 4 in a row, player wins 
				winner = board[row][starting_col] # either player 1 or player 2
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0 

def vertical_win(board):
	"""
	Checks if a vertical | win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	for col in range(7): # check every column
		for starting_row in range(3): # start at top row and shift down one with each iteration
			if board[starting_row][col] == board[starting_row+1][col] == board[starting_row+2][col] == board[starting_row+3][col]!=0:
				# 4 in a row, player wins 
				winner = board[starting_row][col] #either player 1 or player 2
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

def diagonal_up_win(board):
	"""
	Checks if a diagonal / win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	# the possible starting positions of a / diagonal win must be in the left 4 columns and the bottom 3 rows
	for start_row in range(3,6): # bottom 3 rows
		for start_col in range(0,4): # left 4 columns

		# move up and right when comparing board elements
			if board[start_row][start_col] == board[start_row-1][start_col+1] == board[start_row-2][start_col+2] ==board[start_row-3][start_col+3]!=0: 
				winner = board[start_row][start_col]
				return winner
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

def diagonal_down_win(board):
	"""
	Checks if a diagonal \ win has occured
	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no one has won this way, 1 if player 1 wins, 2 if player 2 wins
	"""
	# the possible starting positions of a \ diagonal win must be in the left 4 columns and the top 3 rows
	for start_row in range(0,3): # top 3 rows
		for start_col in range(0,4): # left 4 columns

		# move down and right when comparing board elements
			if board[start_row][start_col] == board[start_row+1][start_col+1] == board[start_row+2][start_col+2] ==board[start_row+3][start_col+3]!=0:
				winner = board[start_row][start_col]
				return winner	
	
	# this part of the code is only reached if a winner hasn't already been returned
	return 0

'''
End of helper functions
'''

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list. Elements in the list must be strings for inputs to be valid. 
	:return: The user's input, string.
	"""
	# Implement your solution below
	while True:
		currentResponse = input(prompt) # asks user to input something and saves this as currentResponse

		if currentResponse in valid_inputs: # checks if the input is one of the specified possibilities
			return currentResponse # returns the user's input as a string
		else:
			print("Invalid input, please try again.") # prints message, then continues back to start of while loop
	 


def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# define parameters for our board
	rows = 6
	columns = 7
	defaultValue = 0 # fill the empty board with this value
	board = []
	
	for row_index in range(rows):
		board.append([]) # adds an element (row) to the list 
		for col_index in range(columns):
			board[row_index].append(defaultValue) # adds an element (column) to the list, in the row of the current row_index
	
	return board


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	rows = 6
	columns = 7
	print("========== Connect4 =========")	#prints header and info
	print("Player 1: X       Player 2: O\n")
	print("  1   2   3   4   5   6   7")
	print(" --- --- --- --- --- --- ---")

	for row in range(rows):			#translates all column values into user-facing representations X and O
		for col in range(columns):
			if board[row][col] == 0:
				print(f"|   ",end='')
			elif board[row][col] == 1:
				print("| X ",end='')
			elif board[row][col] == 2:
				print("| O ",end='')

		print("|")
		print(" --- --- --- --- --- --- ---")
	print("=============================")

	return board
	

def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	
	if player>2 or player<1 or column < 1 or column > 7: #validate inputs (player must be 1 or 2, columnn must be 1-7)
		return False

	col_index = column-1; # python indexing starts at 0

	if board[0][col_index]!=0: # checks if the column they have selected is already full, by checking their col against the top row
		return False

	i = 5 # initialise the row index to start at the bottom row (so gravity is implemented)
	while i>=0: # while loop will run 6 times (since there are 6 rows), starts at the bottom row of the board array and moves up
		if board[i][col_index] == 0:
			board[i][col_index] = player # if the space is 'empty', change it to the player number 
			break
		i -=1 # then move up one row
		 
	return True 


def execute_player_turn(player, board): # Task 5
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	
	valid_inputs = ["1", "2", "3", "4", "5", "6", "7"] # the list of allowed inputs (since there are 7 columns and indexing starts at 1)
	prompt = "Player " + str(player) + ", please enter the column you would like to drop your piece into: " # create input prompt to change to match the current player

	while True: # keep going until the player has successfully placed a piece
		desired_column = int(validate_input(prompt,valid_inputs)) # validate the input and convert it to an integer 

		if drop_piece(board,player,desired_column): # check if the column is already full
			return desired_column # if the column is not full, player has successfully placed piece, and their turn is over
		else:
			print("That column is full, please try again.")


def end_of_game(board): # Question 6
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""

	# save the results of all the win checking types (-,|,/,\)
	result  = [horizontal_win(board),vertical_win(board),diagonal_up_win(board),diagonal_down_win(board)]
	
	for i in range(len(result)):
		if result[i]!= 0: # if the result is 1 or 2, then someone has won and we will return the player number
			return result[i]
	

	# check if the board is full
	for col in range(7):
		if board[0][col]== 0:
			# this means the top spot of the column 'col' is empty
			return 0 # the game is not over, there is still at least one empty spot 
	
	# this part of the function is only reached if no one has won, and there are no spaces left in the top row (board is full)
	return 3 # the game is a draw


def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""

	clear_screen()
	board = create_board()
	

	move_counter = 0 # counts the number of successful moves that have taken place
	last_player = 2
	player = 1
	last_dropped_col = 0 # stores what the last move was, for printing purposes

	while True: 

		clear_screen()
		print_board(board)

		if move_counter>0: # print previous turn if there was one
			print(f"Player {last_player} dropped a piece into column {last_dropped_col}")
		
		last_dropped_col = execute_player_turn(player,board)

		# update move count and player variables now that the turn is over
		move_counter+=1 
		last_player = player
		player = move_counter%2 + 1 
		

		if end_of_game(board)==0:
			continue # if game is still going, go back to the start of the while loop
		else:
			# the game is over, store the result so we can print the relevant message to the screen
			result = end_of_game(board)
			break # get out of the while loop, since we don't want any more moves to be played

	# this part of the function is only reached when the game is over 
	clear_screen()
	print_board(board)
	if result == 1:
		print(f"Player 1 wins. Congrats.\n")
	elif result == 2:
		print(f"Player 2 wins. Congrats.\n")
	else:
		print("It's a draw. Nobody wins :/")


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	program_active = True	#initialising variable for loop
	while program_active == True:
		clear_screen()

		print("=============== Main Menu ===============")	#Prints main menu
		print("Welcome to Connect 4!")
		print("1. View Rules")
		print("2. Play a local 2 player game")
		print("3. Play a game against the computer")
		print("4. Exit")
		print("=========================================")

		selected_option = input("Please select an option: ")	#collects selected option
		if selected_option == "1":	#prints the rules and goes back to menu after the user presses enter
			clear_screen()
			print_rules()
			input("Press enter to return")
		elif selected_option == "2":	#starts a 2 player game, reverting to main menu 5 seconds after it ends
			local_2_player_game()
			time.sleep(5)
		elif selected_option == "3":	#starts a game against cpu, reverting to main menu 5 seconds after it ends
			game_against_cpu()
			time.sleep(5)
		elif selected_option == "4":	#exits the program
			exit()


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""

	while True: #initialises cpu_easy
		column = random.randint(1, 7) # a pseudorandom integer between 1 and 7 is chosen to be the column 
		
		if drop_piece(board, player, column):
			return column # returns exactly where the piece was dropped in the board 
		
		# if the chosen column is not a valid play, we will return to the start of the while loop and choose another random column


def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""

	# check if instant win is available for current player
	if check_for_win(board, player)!=0:
		column_to_play = check_for_win(board, player) # stores which column we should play
		drop_piece(board,player,column_to_play)
		return column_to_play
	
	# check if block is required
	elif (check_for_win(board,player%2+1)!=0):	
		column_to_play = check_for_win(board,player%2+1) # stores which column we should play in order to block a potential win for the other player
		drop_piece(board,player,column_to_play)
		return column_to_play 

	else: 
		while True:
			column_to_play = random.randint(1,7) # choose any column to play, keep trying until a token is successfully placed
			if drop_piece(board,player,column_to_play)== True:
				return column_to_play

'''
Extra helper functions 
-> check_for_traps, which is used in cpu_player_hard
-> possible_columns, which is also used in cpu_player_hard
'''

def check_for_traps(board, player):
	"""
	Checks for 'trap' columns
	For explanation on trap columns see: https://www.thesprucecrafts.com/how-to-win-at-connect-four-basic-strategy-tips-412539
	'Never Play Directly Below the Game-Ending Space'

	This function is intended as a helper for cpu_player_hard
	It creates a dummy board and anticipates if any move in the next turn will open up
	a winning or blocking move, then returns a list of such moves so that the AI does not
	fall into any 'traps'

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: a list of columns that the AI should avoid if possible
	"""
	dummyboard = deepcopy(board) #creates a copy of the board to be manipulated without affecting the actual game board
	columns_to_avoid = [None] * 14 #list of 'trap' columns, these are:
	#columns that if added to will allow the other player to win or
	#block the current player from winning
	#the list is 14 long because it must allow for multiple columns to be traps
	#given that this function checks both players, 14 spaces have been allocated

	number_of_columns = 7
	

	for i in range(number_of_columns):
		dummy_column = (i+1) # column that will be checked
		drop_piece(dummyboard, player, dummy_column) #simulates dropping a piece into one column per loop, filling possible trap holes, player doesn't matter
		
		if check_for_win(dummyboard, player)!=0:	#checks if first player will win in the turn following either player dropping at position i
			columns_to_avoid[i] = check_for_win(dummyboard, player)
	
		if (check_for_win(dummyboard,player%2+1)!=0):	#see above comment for second player
			columns_to_avoid[i+number_of_columns] = check_for_win(dummyboard,player%2+1)
		
		dummyboard = deepcopy(board) #resets the dummy board so that previous test drops don't affect win condition testing of new drops

	return columns_to_avoid #returns the list of columns to avoid


def possible_colums(board):
	"""
	Creates a list of all the columns where a token can be successfully dropped

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: a list of columns where the drop would be successful (elements in the list are int)
	"""
	# create deep copy of the board
	dummy_board = deepcopy(board)
	possible_cols = []

	for col in range(1,8):
		if drop_piece(dummy_board,1,col)==True:
			possible_cols.append(col) # add this column to the list of valid options
	
	return possible_cols


def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	
	This method has similarities to medium cpu. It first checks if there is an instant win available and then checks if an instant win is possible for the other player. 

	There are 2 very common starting sequences that lead to a quick win for the medium ai. These have been defined as common_trap1 and common_trap2. The strategy to protect against these specific cases has explicity defined in hard cpu. 

	It also checks for a trap (a move that would result in an instant possible win for the other player). It will save a list of columns to avoid and not place the token in these unless it is absolutely necessary.

	Generally, it will favour placing a token in the middle column. Next, it will favour placing a token in the 3rd and 5th columns. 

	If these are all full, it randomly places the token in any available remaining column. 

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: column chosen upon a successful drop (int)
	"""

	# define 2 very common configuations of the board that result in an easy win for the other player
	common_trap1 =  [
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 2, 0, 0, 0], 
	[0, 0, 0, 1, 1, 0, 0]]

	common_trap2 = [
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 0, 0, 0, 0], 
	[0, 0, 0, 2, 0, 0, 0], 
	[0, 0, 1, 1, 0, 0, 0]]

	# first few lines of cpu_player_hard are exactly the same as cpu_player_medium, since we have to check for instant wins

	# check if instant win is available for current player
	if check_for_win(board, player)!=0:
		column_to_play = check_for_win(board, player)
		drop_piece(board,player,column_to_play)
		return column_to_play
	
	# check if block is required
	elif (check_for_win(board,player%2+1)!=0):
		column_to_play = check_for_win(board,player%2+1)
		drop_piece(board,player,column_to_play)
		return column_to_play
	


	elif board == common_trap1:
		column_to_play = 3 # this is the best way to defend against this trap
		drop_piece(board,player,column_to_play)
		return column_to_play

	elif board == common_trap2:
		column_to_play = 5 # this is the best way to defend against this trap
		drop_piece(board,player,column_to_play)
		return column_to_play		

	else: 
		second_choice = [3,5]
		third_choice = [2,6]
		fourth_choice = [1,7]

		options = possible_colums(board) # get a list of all the available columns
		
		# call check for trap, which returns all the columns that should not be picked
		columns_to_ignore = check_for_traps(board,player)

		# if there's only one option, play it 
		if len(options) == 1:
			column_to_play = options[0]
			drop_piece(board,player,column_to_play)
			return column_to_play


		# go through and try and place tokens from the middle column outwards, skipping columns that are not possible or that are traps
		if 4 in options and 4 not in columns_to_ignore:
			column_to_play = 4
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 3 in options and 3 not in columns_to_ignore:
			column_to_play = 3
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 5 in options and 5 not in columns_to_ignore:
			column_to_play = 5
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 2 in options and 2 not in columns_to_ignore:
			column_to_play = 2
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 6 in options and 6 not in columns_to_ignore:
			column_to_play = 6
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 1 in options and 1 not in columns_to_ignore:
			column_to_play = 1
			drop_piece(board,player,column_to_play)
			return column_to_play

		elif 7 in options and 7 not in columns_to_ignore:
			column_to_play = 7
			drop_piece(board,player,column_to_play)
			return column_to_play

		else: # only reach this point if all of the options are also traps, so just play the first option
			column_to_play = options[0]
			drop_piece(board,player,column_to_play)
			return column_to_play
		
	


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""

	# create board and initialise variables
	board = create_board()
	move_counter = 0
	last_player = 2
	player = 1
	last_dropped_col = 0
	difficulty_levels = {
		'1': cpu_player_easy,
		'2': cpu_player_medium,
		'3': cpu_player_hard
	}
	


	while True:
		# keep asking to select difficulty until the user gives a valid input
		select_difficulty = input('Please select a CPU difficulty from: 1 - EASY, 2 - MEDIUM or 3 - HARD: ')

		if select_difficulty in difficulty_levels:
			if select_difficulty == "1": # easy
				while True:
					# turns follow the same structure as seen in local_2_player_game
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn if there was one
						print(player_move_string)
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	
					# check if the player has won
					result = end_of_game(board) 
					if result!=0: 
						break 

					# execute player 2 (cpu) turn
					player_move_string = "Player " + str(last_player) + " dropped a piece into column " + str(last_dropped_col)
					# save a string with the information about the player's turn. This will be displayed at the start of their next turn. 
					
					# execute computer's turn and update variables
					last_dropped_col = cpu_player_easy(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1


					# check if the computer has won
					result = end_of_game(board)
					if result!=0: 
						break 
				
				# Game is over. Clear screen and print result.  
				clear_screen()
				print_board(board)
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None

			elif select_difficulty == "2": # medium
				while True:
					# turns follow the same structure as seen in local_2_player_game
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn if there was one
						print(player_move_string)
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	
					# check if the player has won
					result = end_of_game(board) 
					if result!=0: 
						break 

					# execute player 2 (cpu) turn
					player_move_string = "Player " + str(last_player) + " dropped a piece into column " + str(last_dropped_col)
					# save a string with the information about the player's turn. This will be displayed at the start of their next turn. 
					
					# execute computer's turn and update variables
					last_dropped_col = cpu_player_medium(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1


					# check if the computer has won
					result = end_of_game(board)
					if result!=0: 
						break 
				
				# Game is over. Clear screen and print result.  
				clear_screen()
				print_board(board)
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None

			elif select_difficulty == "3": # hard
				while True:
					# turns follow the same structure as seen in local_2_player_game
					clear_screen()
					print_board(board)
			
					if move_counter>0: # print previous turn if there was one
						print(player_move_string)
						print(f"Player {last_player} (computer) dropped a piece into column {last_dropped_col}")
					
					# execute player 1's turn
					last_dropped_col = execute_player_turn(player, board)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1
	
					# check if the player has won
					result = end_of_game(board) 
					if result!=0: 
						break 

					# execute player 2 (cpu) turn
					player_move_string = "Player " + str(last_player) + " dropped a piece into column " + str(last_dropped_col)
					# save a string with the information about the player's turn. This will be displayed at the start of their next turn. 
					
					# execute computer's turn and update variables
					last_dropped_col = cpu_player_hard(board, player)
					move_counter+=1
					last_player = player
					player = move_counter%2 + 1


					# check if the computer has won
					result = end_of_game(board)
					if result!=0: 
						break 
				
				# Game is over. Clear screen and print result.  
				clear_screen()
				print_board(board)
				if result == 1:
					print(f"Player 1 wins. Congrats.\n")
					return None
				elif result == 2:
					print(f"Player 2 wins. Congrats.\n")
					return None
				else:
					print("It's a draw. Nobody wins :/")
					return None


		else:
			print('Invalid difficulty selected, please try again: ')


if __name__ == "__main__":
	main()