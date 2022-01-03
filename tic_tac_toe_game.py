# Tic-Tac-Toe

# --------------------------------------------------------------------------------------
# Function Definitions

# Outputs board to screen
def DisplayBoard():
    print("")
    print("")
    for i in range(0, 8, 3):
        print(board[i] + '|' + board[i + 1] + '|' + board[i + 2])
        print("-------")



# Ensures player has entered valid input, then returns selected board position
def CollectInput():
    i = ' '
    invalid_input = True
    valid_board_positions = []
    user_input = ' '

    # Construct a list of valid untaken board positions
    for i in board:
        if (i != 'X' or i != 'O'):
            valid_board_positions.append(i)

    # Collect user selected board position
    while (invalid_input == True):
        selected_board_position = input('Player ' + whose_turn + ', please enter your selected board position: ')

        if (selected_board_position in valid_board_positions):
            invalid_input = False

    return selected_board_position


def HasPlayerWon():
    wc = [whose_turn, whose_turn, whose_turn]

    # Check horizontal, vertical, and diagnonal rows
    if ((board[0:3] == wc) or (board[3:6] == wc) or (board[6:9] == wc)
            or (board[0:7:3] == wc) or (board[1:8:3] == wc) or (board[2:9:3] == wc)
            or (board[0:9:4] == wc) or (board[2:7:2] == wc)):
        return True
    else:
        return False


def AnnounceWinner():
    print("Player " + whose_turn + " Wins.")

k = int(input("Enter the number you want to play how many times : "))
for x in range(k):
    # --------------------------------------------------------------------------------------
    # Variable Declarations
    board = ['0', '1', '2',
             '3', '4', '5',
             '6', '7', '8']
    game_over = False
    whose_turn = 'X'

    # --------------------------------------------------------------------------------------
    # Execution
    DisplayBoard()  # Initially Display an Empty Board

    while (not game_over):

        selected_board_position = '9'

        # Collect Input
        selected_board_position = CollectInput()

        # Update Board
        board[int(selected_board_position)] = whose_turn

        # Display board
        DisplayBoard()

        # Did the most recent move cause the player to win?
        game_over = HasPlayerWon()

        # If not, then switch player
        if (not game_over):
            if (whose_turn == 'X'):
                whose_turn = 'O'
            else:
                whose_turn = 'X'

    AnnounceWinner()