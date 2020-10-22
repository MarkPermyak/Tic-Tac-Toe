from classes import TicTacToe


field = [['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]']]
turn = 1
game = TicTacToe()


while not game.game_over(turn, field):
    game.whose_turn(turn)
    turn += 1
    game.draw_field(field)
    x, y = map(int, input().split())
    if turn % 2 == 0:
        game.cross_turn(x, y, field)
    else:
        game.nought_turn(x, y, field)
    game.winner(field)

game.draw_field(field)
print(game.winner(field))
