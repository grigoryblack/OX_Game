board = list(range(1, 10))
    # Функция для отрисовки поля игры
def draw_table(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-"*13)
    # Функция для ввода ответов с различными ограничениями
def get_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Поставьте свой ответ " + player_token + " ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некоректный ввод. Введите число!")
            continue
        if player_answer >= 1 and  player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята!")
        else:
            print("Некоректный ввод! Введите число от 1 до 9.")
    # Функция, которая проверяет наличие выигрыша
def check_winner(board):
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combination:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

    # Пишу главную функцию для запуска игры
def main(board):
    counter = 0
    win = False
    while not win:
        draw_table(board)
        if counter % 2 == 0:
            get_input("X")
        else:
            get_input("O")
        counter += 1
        if counter > 4:
            tmp = check_winner(board)
            if tmp:
                win = True
                print(tmp, "Вы выиграли!")
        if counter == 9:
            print("Ничья")
            break
    draw_table(board)

main(board)



