def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

    [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def check_winner(board):
    # Sprawdzenie wierszy i kolumn
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
        
    # Sprawdzenie przekątnych
    if board[0][0]  == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print(print_board(board))
        print(f"Gracz {current_player}, wybierz wiersz i kolumnę (0, 1 lub 2), oddzielając spacją: ")
        input_valid = False
        while not input_valid:
            user_input = input().split()
            if len(user_input) == 2 and all(x.isdigit() for x in user_input):
                row, col = map(int, user_input)
                if 0 <= row < 3 and 0 <= col < 3:
                    if board[row][col] == " ":
                        input_valid = True
                    else:
                        print("To pole jest już zajęte. Spróbuj ponownie.")
                else:
                    print("Współrzędne poza zakresem. Wprowadź liczby od 0 do 2.")
            else:
                print("Nieprawidłowy ruch. Wprowadź dwie liczby oddzielone spacją.")

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Gracz {winner} wygrywa!")
            break
        if is_draw(board):
            print_board(board)
            print("Remis!")
            break

        current_player = "0" if current_player == "X" else "X"

        

        

# map(function, iterable_object):
# function - funkcja, którą chcesz zastosować do każdego elementu iterowalnego obiektu. Może to być funkcja zdefiniowana przez użytkownika lub wbudowana
# iterable_object - jeden lub więcej iterowalnych obiektów, na których funkcja zostanie zastosowana


tic_tac_toe()

