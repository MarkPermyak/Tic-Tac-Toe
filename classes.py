class TicTacToe:

    def __init__(self, player1, player2, field):
        self.player1 = player1
        self.player2 = player2
        self.field = field
        # получаем на вход имена обоих игроков и поле, на котором будем работать

    def who_is_who(self):
        print(self.player1, "is first and playing X")
        print(self.player2, "is second and playing O")

    def draw_field(self):
        for i in range(3):
            for j in range(3):
                print(self.field[i][j], sep="", end="")
            print("")

    def game_over(self, turn):
        if turn < 10 and TicTacToe.winner(self) == "Draw":
            # если после очередного хода всё ещё ничья,
            # и при этом прошло меньше 10 ходов, то есть остались свободные клетки
            return False
        else:
            return True
            # иначе игра закончилась, то есть наступил game over, возвращаем истину

    def whose_turn(self, turn):
        if turn % 2 == 1:
            print("Now is", self.player1, "Turn")
        else:
            print("Now is", self.player2, "Turn")
            # на нечетных ходах ходит первый, на четных второй

    def nought_turn(self, x, y):
        if self.field[x-1][y-1] == '[ ]':
            self.field[x-1][y-1] = '[O]'
        else:
            return -1

    def cross_turn(self, x, y):
        if self.field[x - 1][y - 1] == '[ ]':
            self.field[x-1][y-1] = '[X]'
        else:
            return -1

    def winner(self):
        s = ''
        # посмотрим на все строки, строчки и на обе диагонали
        # если там есть три одинаковых символа, то кто-то уже выиграл
        for i in range(0, 3):
            for j in range(0, 3):
                s += self.field[i][j]
            if s == '[O][O][O]':
                return self.player2 + " wins"
            else:
                if s == '[X][X][X]':
                    return self.player1 + " wins"
            s = ''
        if s == '':
            # если среди строчек не оказалось, ищем среди столбцов
            for i in range(0, 3):
                for j in range(0, 3):
                    s += self.field[j][i]
                if s == '[O][O][O]':
                    return self.player2 + " wins"
                else:
                    if s == '[X][X][X]':
                        return self.player1 + " wins"
                s = ''
        if s == '':
            # если и среди столбцов не оказалось, ищем среди диагоналей
            d1 = self.field[0][0] + self.field[1][1] + self.field[2][2]
            d2 = self.field[2][0] + self.field[1][1] + self.field[0][2]
            if d1 == '[O][O][O]' or d2 == '[O][O][O]':
                return self.player2 + " wins"
            else:
                if d1 == '[X][X][X]' or d2 == '[X][X][X]':
                    return self.player1 + " wins"
                else:
                    return "Draw"
                    # если нигде не оказалось, то пока ничья
