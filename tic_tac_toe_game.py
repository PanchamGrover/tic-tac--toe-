import random
squares = [1, 2, 3, 4, "X", 6, 7, 8, 9]
board = f"""
+-----+-----+-----+
|  {squares[0]}  |  {squares[1]}  |  {squares[2]}  |
+-----+-----+-----+
|  {squares[3]}  |  {squares[4]}  |  {squares[5]}  |
+-----+-----+-----+
|  {squares[6]}  |  {squares[7]}  |  {squares[8]}  |
+-----+-----+-----+"""

def check_squares(squares , answer):
    answer = int(answer)
    if answer in squares:
        return True
    else:
        print("The square is already occupied try something else.")
        return False

def check_user_input(user_input):
    try:
        if int(user_input) > 0 and int(user_input) <= 9:
            return True
        else:
            print("Please enter a valid number.")
            return False
    except ValueError:
        print("String is not acceptable, Please enter a number.")
        return False
    

print("Hello Welcome To The Tic-Tac-Toe Game.")
print(board)

game_is_on = True

while game_is_on:
    user_input = input("Type your move.")
    if check_user_input(user_input) == False:
        continue
    else:
        if check_squares(squares, answer=user_input) == True:
            board = board.replace(f'{squares[int(user_input) - 1]}',"O")
            squares[int(user_input) - 1] = "O"
            print(squares)
            print(board)


    if squares[0:3] == ["X", "X", "X"] or squares[3:6] == ["X", "X", "X"] or squares[6:] == ["X", "X", "X"]:
        print("COMPUTER WINS.")
        break
    elif squares[::3] == ["X", "X", "X"] or squares[1::3] == ["X", "X", "X"] or squares[2::3] == ["X", "X", "X"]:
        print("COMPUTER WINS.")
        break
    elif squares[0] == ["X"] and squares[4] == ["X"] and squares[8] == ["X"]:
        print("COMPUTER WINS.")
        break
    elif squares[2] == ["X"] and squares[4] == ["X"] and squares[6] == ["X"]:
        print("COMPUTER WINS.")
        break

    elif squares[0:3] == ["O", "O", "O"] or squares[3:6] == ["O", "O", "O"] or squares[6:] == ["O", "O", "O"]:
        print("CONGRATULATIONS YOU WIN.")
        break
    elif squares[::3] == ["O", "O", "O"] or squares[1::3] == ["O", "O", "O"] or squares[2::3] == ["O", "O", "O"]:
        print("CONGRATULATIONS YOU WIN.")
        break
    else:
        result = any(isinstance(x, int) for x in squares)
        if result == False:
            print("ITS A TIE.")
            break
        else:
            pass

    while True:
        computer_move = random.choice(squares)
        if type(computer_move) == int:
            board = board.replace(f'{squares[int(computer_move) - 1]}',"X")
            squares[int(computer_move) - 1] = "X"
            print(squares)
            print(board)
            break
        else:
            continue

    if squares[0:3] == ["X", "X", "X"] or squares[3:6] == ["X", "X", "X"] or squares[6:] == ["X", "X", "X"]:
        print("COMPUTER WINS.")
        break
    elif squares[::3] == ["X", "X", "X"] or squares[1::3] == ["X", "X", "X"] or squares[2::3] == ["X", "X", "X"]:
        print("COMPUTER WINS.")
        break
    elif squares[0] == ["X"] and squares[4] == ["X"] and squares[8] == ["X"]:
        print("COMPUTER WINS.")
        break
    elif squares[2] == ["X"] and squares[4] == ["X"] and squares[6] == ["X"]:
        print("COMPUTER WINS.")
        break

    elif squares[0:3] == ["O", "O", "O"] or squares[3:6] == ["O", "O", "O"] or squares[6:] == ["O", "O", "O"]:
        print("CONGRATULATIONS YOU WIN.")
        break
    elif squares[::3] == ["O", "O", "O"] or squares[1::3] == ["O", "O", "O"] or squares[2::3] == ["O", "O", "O"]:
        print("CONGRATULATIONS YOU WIN.")
        break
    else:
        result = any(isinstance(x, int) for x in squares)
        if result == False:
            print("ITS A TIE.")
            break
        else:
            pass

