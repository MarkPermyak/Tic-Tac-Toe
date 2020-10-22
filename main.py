from classes import TicTacToe

name1, name2 = map(str, input().split())

field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]
# начальное поле

game = TicTacToe(name1, name2, field)

game.who_is_who()
# кто за кого играет

turn = 1
while not game.game_over(turn):
    game.whose_turn(turn)
    # кто ходит
    turn += 1
    game.draw_field()
    x, y = map(int, input().split())
    # вводим номер строки (нумерация сверху вниз) и номер столбца (нумерация слева направо)
    symbol = str(input())
    # вводим то, что хотим вставить в клетку
    if symbol == 'X':
        if game.cross_turn(x, y) != -1:
            game.cross_turn(x, y)
        else:
            print("Turn is invalid: occupied cell")
            # если ввели допустимый символ, но клетка уже занята
            turn -= 1
            # отнимаем один ход, так как его, по сути, и не было
    else:
        if symbol == 'O':
            if game.nought_turn(x, y) != -1:
                game.nought_turn(x, y)
            else:
                print("Turn is invalid: occupied cell")
                turn -= 1
        else:
            print("Turn is invalid: invalid character")
            # если вввели недопустимый символ
            turn -= 1
    game.winner()
    # проверяем, не выйграл ли уже кто-нибудь

game.draw_field()
print(game.winner())
