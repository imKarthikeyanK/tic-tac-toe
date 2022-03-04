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

        self._print_board()

        return True

    def _print_board(self):
        print(";;;;;;;;;;;; BOARD ;;;;;;;;;;;;;;;;;")
        for sub_list in self.board:
            print(f";;;;;;;;;;;;{sub_list};;;;;;;;;;;;;;")
        print(";;;;;;;;;;;; BOARD ;;;;;;;;;;;;;;;;;\n")


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
        """
        In the below logic, we are initially transforming the items of board into numbers. 
        If entry is 'X' then we mark it as '1', If entry is 'O' then we mark it as '2'.
        If entry is '-' then we mark it as 'len(sub_list) + 2', so that this value will always be
        greater than the success criteria value.

        While transforming we are calculating the horizontal conditions and also loading the 
        diagonal data points, so that we dont have to run one more for loop for that.

        Only for vertical calcualtion we have kept a separte for loop, since that needs some nesting
        """
        result_board = []
        is_complete = True

        left_right_diag = []
        right_left_diag = []

        for index, sub_list in enumerate(self.board):
            # transforming the board
            new_sub_list = []
            for sub_item in sub_list:
                new_sub_item = len(sub_list) + 2
                if sub_item == 'X':
                    new_sub_item = 1
                elif sub_item == 'O':
                    new_sub_item = 2
                else:
                    # updating this flag to know if the board is complete or not
                    is_complete = False
                
                new_sub_list.append(new_sub_item)
            result_board.append(new_sub_list)

            # calculating horizontal success
            if sum(new_sub_list) == len(new_sub_list) or sum(new_sub_list) == len(new_sub_list) * 2:
                return "W"
            
            # populating data points for diagonal success
            left_right_diag.append(new_sub_list[index])
            right_left_diag.append(new_sub_list[len(new_sub_list) - (index + 1)])

        # calculating the vertical success
        for index in range(len(result_board)):
            vertical_entries = []
            for sub_index in range(len(result_board)):
                vertical_entries.append(result_board[sub_index][index])
            
            if sum(vertical_entries) == len(vertical_entries) or sum(vertical_entries) == len(vertical_entries) * 2:
                return "W"

        # calculating diagonal success
        if sum(left_right_diag) == len(left_right_diag) or sum(left_right_diag) == len(left_right_diag) * 2:
            return "W"
        
        if sum(right_left_diag) == len(right_left_diag) or sum(right_left_diag) == len(right_left_diag) * 2:
            return "W"
        
        # if the board is complete and no success, then 'nobody' wins
        if is_complete:
            return "E"

        return False