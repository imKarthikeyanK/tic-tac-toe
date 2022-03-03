class TicTacToe:
    def __init__(self) -> None:
        self.board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-'],
        ]

    def make_move(self, index, player_symbol):
        sub_arr, sub_item = self._figure_item(index)

        if not self._validate_move(sub_arr, sub_item):
            return False

        self.board[sub_arr][sub_item] = player_symbol

        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; BOARD ;;;;;;;;;;")
        print(f";;;;;;;;;;;;{self.board[0]};;;;;;;;;;;;;;")
        print(f";;;;;;;;;;;;{self.board[1]};;;;;;;;;;;;;;")
        print(f";;;;;;;;;;;;{self.board[2]};;;;;;;;;;;;;;")
        print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; BOARD ;;;;;;;;;;\n")

        return True

    def _validate_move(self, sub_arr, sub_item):
        if self.board[sub_arr][sub_item] != "-":
            return False

        return True

    def _figure_item(self, index):
        if index <= 3:
            sub_arr = 0
            sub_item = index - 1
        elif index > 3 and index <= 6:
            sub_arr = 1
            sub_item = index  - 4
        else:
            sub_arr = 2
            sub_item = index - 7

        return sub_arr, sub_item

    def get_result(self):
        if len(set([self.board[0][0], self.board[1][0], self.board[2][0]])) == 1 and "-" not in set([self.board[0][0], self.board[1][0], self.board[2][0]]):
            return "W"
        elif len(set([self.board[0][1], self.board[1][1], self.board[2][1]])) == 1 and "-" not in set([self.board[0][1], self.board[1][1], self.board[2][1]]):
            return "W"
        elif len(set([self.board[0][2], self.board[1][2], self.board[2][2]])) == 1 and "-" not in set([self.board[0][2], self.board[1][2], self.board[2][2]]):
            return "W"

        if "-" not in self.board[0] and len(set(self.board[0])) == 1:
            return "W"
        elif "-" not in self.board[1] and len(set(self.board[1])) == 1:
            return "W"
        elif "-" not in self.board[2] and len(set(self.board[2])) == 1:
            return "W"

        if len(set([self.board[0][0], self.board[1][1], self.board[2][2]])) == 1 and "-" not in set([self.board[0][0], self.board[1][1], self.board[2][2]]):
            return "W"
        elif len(set([self.board[0][2], self.board[1][1], self.board[2][0]])) == 1 and "-" not in set([self.board[0][2], self.board[1][1], self.board[2][0]]):
            return "W"

        if "-" not in self.board[0] and "-" not in self.board[1] and "-" not in self.board[2]:
            return "E"

        return False

