'''
Author:      Anneliese Hall
Date:        3/23/26 
Assignment:  Tic Tac Toe Project 
Course:      CPSC1050
Lab Section: 001
'''
def play(playing, game_board, turn_count, user_input):
# Prompt Players to Play 
# Print out the game start & example
    while playing:
        print("Let's play Tic-Tac-Toe!")
        print("When prompted, enter desired row and column numbers")
        print("Example: 1 3")
# List of all tics and toes 
        example_list = [["|","_","|","_","|","X","|"],["|","_","|","_","|","_","|"],["|","_","|","_","|","_","|"]]
        for row in example_list:
            print(*row)

# Print out the blank game board and prompt user
        print("Let's play!")
        print("Player X starts!")
        for row in game_board:
            print(*row) 

        turn_count = 1
# while no one has winned or tied, 
# the board keeps updating until a tie or a win is reached. 
# after each update the turn count increases to signal the next turn
        while (check_for_win(game_board) == False) and (check_tie(game_board) == False):
            update_board(user_input, turn_count, game_board) 
            turn_count += 1 

# after a win or tie has been reached 
        print("Do you want to play again? Y or N")
        decide = input()

# user input(str) is validated or a Y or N answer 
        quick_check = False 

        while quick_check == False:
            if decide not in ["Y","N"]:
                print("Please enter valid input: Y or N")
                print("Do you want to play again? Y or N")
                decide = input()
                quick_check = False
            else:
                quick_check = True

# the playing value is set to true or false to signal the end of the game
        if decide == "N":
            quick_check = True 
            playing = False 

# resets all tracking objects 
        elif decide == "Y":
            quick_check = True
            turn_count = 1
            user_input = ""
            game_board = [["|","_","|","_","|","_","|"],["|","_","|","_","|","_","|"],["|","_","|","_","|","_","|"]]
            playing = True
            check_tie(game_board) == False 
            check_for_win(game_board) == False




 



def update_board(user_input, turn_count, game_board):
    # Prompt and take player input and update and print game board accordingly
    # Prompt players multiple times, alternating players appropriately
    '''
    while loop to ask player x and player o for input 
    
    uses count to switch between the two players 

    while loop ends when check_for_win is true (bool)

    uses nested functions to check for valid inputs 

    X = odd
    O = even 

    '''
# player X or O prompt?
    if turn_count % 2 != 0: 
        print("Enter row and column for player X")
    else: 
        print("Enter row and column for player O")

# User input 
    user_input = input().split()

# check that the number is valid
# still in str format so user_input is used so .isdigit() can be used
    while validate3(user_input) == False:
        print("Please enter valid row and col numbers from 1 to 3:")
        user_input = input().split()

# once integer is validated, the string user_input is turned into a small list of integers
    turn = [int(i) for i in user_input]

# makes sure input is valid and for an empty space
    while validate1(turn) == False:
        print("Please enter valid row and col numbers from 1 to 3:")
        user_input = input().split()

# nested while loop to re-check the integer status of number or not number because we are reprompting the user if its wrong again
        while validate3(user_input) == False:
            print("Please enter valid row and col numbers from 1 to 3:")
            user_input = input().split()
        turn = [int(i) for i in user_input]

# validate2() checks if the spot is full or not 
# another nested loop is used for the same as stated purpose in the previous validate1() call
    while validate2(game_board, turn) == False:
        print("That spot is full!")
        print("Please enter valid row and col numbers from 1 to 3:")
        user_input = input().split()
        while validate3(user_input) == False:
            print("Please enter valid row and col numbers from 1 to 3:")
            user_input = input().split()
        turn = [int(i) for i in user_input]
                    
    # turns the validated input into a translated object that the orignial game_board can understand and for simplicity later 
    row = turn[0] - 1 # the row 
    col = turn[1] * 2 - 1 # the placement 
    # actually replaces the empty space with "X" or "O"
    # utilizes the 2D list gameboard 
    if turn_count % 2 != 0: #odd
        game_board[row][col] = "X"
        for row in game_board:
            print(*row)
    else:
        game_board[row][col] = "O"
        for row in game_board:
            print(*row)




def validate1(turn):
# to check if the input is in bounds
# uses turn parameter (list) of (int)s
# utlizizes the 1D list that is turn to check if both numbers in the list are either a 1, 2, or 3

    if (turn[0]  in [1,2,3]) and (turn[1] in [1,2,3]):
        return True
    else:
        return False



def validate2(game_board, turn):
# to check if the input choose a spot that was not empty
# uses turn parameter (int)
# see gameboard parameter (2D list)

# redefines row and col so a value error doesn't pop up 
    row = int(turn[0]) - 1
    col = int(turn[1]) *2 - 1

    if game_board[row][col] == "_":
        return True
    else: 
        return False 



def validate3(user_input):
# to check if the user_input is a number
# uses user_input parameter (str)
# uses built in function .isdigit() that works on strings only, which is why user_input (str) is used
 
    if not user_input[0].isdigit() or not user_input[1].isdigit():
        return False  
    else:
        return True

    



def check_for_win(game_board):
# nested functions
# - check rows 
# - check collumns
# - check diagonals 
# if one of the above is a win, then it returns true to the function
    if (check_rows(game_board) == True) or (check_collumns(game_board) == True) or (check_diagonals(game_board) == True): 
        return True
    else:
        return False 



def check_rows(game_board):
# checks rows for a win
# for loop used to iterate through each list in the 2d list 
    for row in game_board:
        if (row[1] == row[3] == row[5]) and (row[1] == "X"):
            print("Player X WINS!")
            return True 
        if (row[1] == row[3] == row[5]) and (row[1] == "O"):
            print("Player O WINS!")
            return True
        if (row[1] == row[3] == row[5]) and (row[1] != "O") or (row[1] == row[3] == row[5]) and (row[1] != "X"):    
            return False


def check_collumns(game_board):
# checks collumns 
# also uses for loop but for the collumn to stop
    for col in [1, 3, 5]:
        if (game_board[0][col] == game_board[1][col] ==game_board[2][col]) and (game_board[0][col] == "X"):
            print("Player X WINS!")
            return True
        if (game_board[0][col] == game_board[1][col] ==game_board[2][col]) and (game_board[0][col] == "O"):
            print("Player O WINS!")
            return True
        if ((game_board[0][col] == game_board[1][col] ==game_board[2][col]) and (game_board[0][col] != "X")) and ((game_board[0][col] == game_board[1][col] ==game_board[2][col]) and (game_board[0][col] != "O")):
            return False

def check_diagonals(game_board):

# left to right Diagonal
    if (game_board[0][1] == game_board[1][3] == game_board[2][5]) and (game_board[0][1] == "X"):
        print("Player X WINS!")
        return True

    elif (game_board[0][1] == game_board[1][3] == game_board[2][5]) and (game_board[0][1] == "O"):
        print("Player O WINS!")
        return True 

# right to left Diagonal 
    if (game_board[0][5] == game_board[1][3] == game_board[2][1]) and (game_board[0][5] == "X"):
        print("Player X WINS!")
        return True

    elif (game_board[0][5] == game_board[1][3] == game_board[2][1]) and (game_board[0][5] == "O"):
        print("Player O WINS!")
        return True 
    
    else:
        return False 

    

        
def check_tie(game_board):
# checks for ties
# nested for loop
    for row in game_board:
        for placement in [1, 3, 5]:
            if row[placement] == "_":
                return False 

    print("It's a TIE!") 
    return True






if __name__ == "__main__":
    
    turn_count = 1
    user_input = ""
    game_board = [["|","_","|","_","|","_","|"],["|","_","|","_","|","_","|"],["|","_","|","_","|","_","|"]]
    check_for_win(game_board) == False 
    check_tie(game_board) == False
    playing = True
    
    play(playing, game_board, turn_count, user_input)
    







