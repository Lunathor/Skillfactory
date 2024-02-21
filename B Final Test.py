#Двумерный массив, который будем использовать для нашего игрового поля
field = [[" "] * 3 for i in range(3)]


def board():
    print()
    print("   | 0 | 1 | 2 | ")
    print("  ---------------  ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} |"
        print(row_str)
        print("  ---------------  ")
    print()


board()


# Создаем функцию с помощью которой будем растовлять крестики и нолики на нашем игровом поле
def turn():
    while True:
        cords = input("          Ваш ход: ").split()
        if len(cords) != 2:
            print("Введите две координаты!  ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числа! ")
            continue
        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапозона! ")
            continue
        if field[x][y] != " ":
            print("Клетка занята! ")
            continue
        return x, y


# Выполняем проверку с помощью функции для определения победителя

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False


# Пишем условие с помощью которого программа будет определять кто ходит в данный момент
num = 0
while True:
    num += 1

    board()

    if num % 2 == 1:
        print("Ходит крестик ")
    else:
        print("Ходит нолик ")

    x, y = turn()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if check_win():
        break
    if num == 9:
        print(" Ничья!")
        break

# Выполняем проверку с помощью функции для определения победителя


# Далее идет вариант написанный с небольшой помощью ChatGPT. Из интересного он использовал координаты не от 0 до 2 а от 1 до 3
# Плюс он использовал для этого функцию Try ... except сделав ValueError исключением для программы
# При этой ошибке она не будет остановлена
# def print_board(board):
#     """Функция для вывода игровой доски на экран"""
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)
#
# def player_move(board, player):
#     """Функция для размещения хода игрока на доске"""
#     while True:
#         try:
#             print(f"Ход игрока {player}")
#             row = int(input("Введите строку (1-3): ")) - 1
#             col = int(input("Введите колонку (1-3): ")) - 1
#             if (0 <= row <= 2) and (0 <= col <= 2) and (board[row][col] == " "):
#                 board[row][col] = player
#                 break
#             else:
#                 print("Эта клетка уже занята или введены некорректные координаты. Попробуйте еще раз.")
#         except ValueError:
#             print("Пожалуйста, введите число от 1 до 3.")
#
# def check_win(board):
#     """Функция для проверки победы одного из игроков"""
#     win_combinations = [
#         [board[0][0], board[0][1], board[0][2]],
#         [board[1][0], board[1][1], board[1][2]],
#         [board[2][0], board[2][1], board[2][2]],
#         [board[0][0], board[1][0], board[2][0]],
#         [board[0][1], board[1][1], board[2][1]],
#         [board[0][2], board[1][2], board[2][2]],
#         [board[0][0], board[1][1], board[2][2]],
#         [board[2][0], board[1][1], board[0][2]]
#     ]
#     for combination in win_combinations:
#         if combination.count(combination[0]) == 3 and combination[0] != " ":
#             return True
#     return False
#
# def game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#     moves_count = 0
#     while True:
#         print_board(board)
#         player_move(board, current_player)
#         moves_count += 1
#         if check_win(board):
#             print_board(board)
#             print(f"Игрок {current_player} выиграл!")
#             break
#         if moves_count == 9:
#             print_board(board)
#             print("Ничья!")
#             break
#         current_player = "O" if current_player == "X" else "X"
#
# if __name__ == "__main__":
#     game()