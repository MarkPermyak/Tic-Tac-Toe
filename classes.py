class TicTacToe:

    def draw_field(self, field):
        for i in range(3):
            for j in range(3):
                print(field[i][j], sep="", end="")
            print("")

    def game_over(self, turn, field):
        if turn < 10 and TicTacToe.winner(self, field) == "Draw":
            return False
        else:
            return True

    def whose_turn(self, turn):
        if turn % 2 == 1:
            print("Now is Player 1 Turn")
        else:
            print("Now is Player 2 Turn")

    def nought_turn(self, x, y, field):
        field[x-1][y-1] = '[O]'

    def cross_turn(self, x, y, field):
        field[x-1][y-1] = '[X]'

    def winner(self, field):
        s = ''
        for i in range(3):
            for j in range(3):
                s += field[i][j]
            if s == '[O][O][O]':
                return "Player 2 wins"
            else:
                if s == '[X][X][X]':
                    return "Player 1 wins"
            s = ''
        if s == '':
            for i in range(3):
                for j in range(3):
                    s += field[j][i]
                if s == '[O][O][O]':
                    return "Player 2 wins"
                else:
                    if s == '[X][X][X]':
                        return "Player 1 wins"
            s = ''
        if s == '':
            d1 = field[0][0] + field[1][1] + field[2][2]
            d2 = field[0][0] + field[1][1] + field[2][2]
            if d1 == '[O][O][O]' or d2 == '[O][O][O]':
                return "Player 2 wins"
            else:
                if d1 == '[X][X][X]' or d2 == '[X][X][X]':
                    return "Player 1 wins"
                else:
                    return "Draw"
