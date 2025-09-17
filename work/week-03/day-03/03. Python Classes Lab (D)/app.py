# x | o 
class Game:
    def __init__(self):
        self.turn = "X" ## X plays first
        self.winner = None
        self.tie = False
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def display_main_menu(self):
        print("Welcome to Tic-Tac-Toe!") # first line in the game
    def print_board(self):
         # from the lab prompt

        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def is_valid_move(self, choice): # check if move is valid and empty
        choice = choice.lower().strip()
        if choice in self.board and self.board[choice] is None:
            return True
        else:
            return False

    def update_board(self, choice, symbol):# place X or O on board

        self.board[choice] = symbol

    def print_message(self):# show game status
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def switch_turn(self):# change player turn  
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def get_move(self):# ask player for a valid move
        while True:
            choice = input("Enter a valid move (example: A1): ")
            choice = choice.lower().strip()
            if self.is_valid_move(choice):
                return choice
            else:
                print("Invalid move! Please try again.")

    def check_for_winner(self):#find winner
        combos = [
            ['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'],
            ['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'],
            ['a1','b2','c3'], ['c1','b2','a3']
        ]
        for a, b, c in combos:
            v = self.board[a]
            if v is not None and v == self.board[b] == self.board[c]:
                self.winner = v
                return

    def check_for_tie(self): # tie check
        if all(value is not None for value in self.board.values()) and self.winner is None:
            self.tie = True

    def play_game(self):# run the game
        self.display_main_menu()
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            choice = self.get_move()
            self.update_board(choice, self.turn)
            self.check_for_winner()
            self.check_for_tie()
            if not self.winner and not self.tie:
                self.switch_turn()
        self.print_board()
        self.print_message()


if __name__ == "__main__":# run game here
    game = Game()
    game.play_game()

 
