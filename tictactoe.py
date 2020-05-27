import random, time

def main():
    
    while True:
        board = [" "] * 9
        user = player_input()
        user1 = choose_first()
        print(f"{user1} goes first")
        time.sleep(1)
        user2 = user
        if user == user1:
            if user1 == 'X':
                user2 = 'O'
            else:
                user2 = 'X'
        count = 0
        while True:
            currentUser = user1
            if count%2 != 0:
                currentUser = user2
            
            display_board(board)
            
            position = player_choice(board, currentUser)
            place_marker(board, currentUser, position)
            
            if win_check(board, currentUser):
                display_board(board)
                print(f"{currentUser} has won the game")
                break
            elif full_board_check(board):
                print("This match is a tie")
                break
            
            count += 1
            
        if not replay():
            print("Thanks for playing!")
            break

def display_board(board):
    count = 0
    print('\n'*100)
    for i in board:
        if count % 3 == 0:
            print("\n------")
            print(i,end = "|")
        else:
            print(i,end = "|")
        count += 1
    print("\n------")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == 'X':
        return 'X'
    else:
        return 'O'

def place_marker(board, marker, position):
        board[position] = marker

def win_check(board, mark):
    if (board[0] == mark) and (board[1] == mark) and (board[2] == mark):
        return True
    elif (board[3] == mark) and (board[4] == mark) and (board[5] == mark):
        return True
    elif (board[6] == mark) and (board[7] == mark) and (board[8] == mark):
        return True
    elif (board[0] == mark) and (board[4] == mark) and (board[8] == mark):
        return True
    elif (board[2] == mark) and (board[4] == mark) and (board[6] == mark):
        return True
    elif (board[0] == mark) and (board[3] == mark) and (board[6] == mark):
        return True
    elif (board[1] == mark) and (board[4] == mark) and (board[7] == mark):
        return True
    elif (board[2] == mark) and (board[5] == mark) and (board[8] == mark):
        return True
    return False

def choose_first():
    first = random.randint(0,1)
    if first == 0:
        return 'X'
    return 'O'

def space_check(board,position):
    if board[position] == " ":
        return True
    return False

def full_board_check(board):
    if " " in board:
        return False
    return True

def player_choice(board, user):
    while True:
        print(f"{user} turn: ")
        position = int(input("Enter a position between 1 to 9: "))
        position -= 1
        available = space_check(board, position)
        if available:
            return position
        else:
            print("Enter a valid position to proceed")

def replay():
    user_input = input("Would you like to play again? ")
    if user_input.upper() == 'Y' or user_input.upper() == 'YES':
        return True
    return False

if __name__ == "__main__":
    main()