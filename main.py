import random

from tictactoe import TicTacToe


class Main:
    def __init__(self) -> None:
        self.player = "X"
        self.tictactoe = TicTacToe()
        self.user_msg = ""
        self.player_msg = ""
        self.played_moves = []

    def start(self):
        self._game_runner()

    def _game_runner(self):
        result = None

        while result != "W" or result != "E":
            if self.player == "X":
                user_input = self._get_input()
            else:
                user_input = self._get_computer_input()

            update_box = self.tictactoe.make_move(user_input, self.player)

            if not update_box:
                self.user_msg = "Invalid Box Choosen. "
                continue
            else:
                self.user_msg = ""
                self.played_moves.append(user_input)
                
            result = self.tictactoe.get_result()

            if result == "W":
                print(f"Player '{self.player}' has WON the Match!")
                break
            elif result == "E":
                print("Nobody wins the match!")
                break
            else:
                self.player = "O" if self.player == "X" else "X"

    def _get_input(self):
        input_num = None

        while not input_num:
            user_input = self.__get_user_input()
            if user_input.isnumeric():
                user_input = int(user_input)
                if not user_input < 0 and not user_input > 9:
                    input_num = user_input
                    break

        return input_num

    def __get_user_input(self):
        print(f"Player: '{self.player}' - {self.user_msg}Please Enter the Box number to Move:\n")

        user_input = input()

        return user_input

    def _get_symbol(self):
        while not self.player:
            self.__symbol_getter()
        self.player_msg = ""

    def __symbol_getter(self):
        print(f"{self.player_msg}Please Choose the Symbol of your choice: \n1. X\n2. O\n\n")
        symbol_map = {
            "1": "X",
            "2": "O"
        }
        symbol = input()

        if symbol_map.get(symbol):
            self.player = symbol_map.get(symbol)
            self.player_msg = "Invalid Symbol Choosed. "

        return

    def _get_computer_input(self):
        computer_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        excess_comp_moves = list(set(computer_moves) - set(self.played_moves))
        computer_move = random.choice(excess_comp_moves)
        print(f"Player: 'Computer'- Chooses '{computer_move}'\n")
        return computer_move





tictactoe = Main()
tictactoe.start()
