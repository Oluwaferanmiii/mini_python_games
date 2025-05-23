import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.player_symbol = None
        self.opponent_symbol = None
        self.current_player = None
        self.board = [""] * 9
        self.buttons = []

        self.status_label = tk.Label(root, text="", font=('Arial', 14))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()
        self.reset_button = tk.Button(
            root, text="Reset", command=self.reset_game, font=('Arial', 12))
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

        self.choose_symbol_popup()

    def choose_symbol_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Choose Your Symbol")
        popup.geometry("250x100")
        tk.Label(popup, text="Player 1: Choose your symbol").pack(pady=10)

        def choose(symbol):
            self.player_symbol = symbol
            self.opponent_symbol = "O" if symbol == "X" else "X"
            self.current_player = self.player_symbol
            self.status_label.config(
                text=f"Player {self.current_player}'s turn")
            popup.destroy()

        tk.Button(popup, text="X", width=10, command=lambda: choose(
            "X")).pack(side=tk.LEFT, padx=20)
        tk.Button(popup, text="O", width=10, command=lambda: choose(
            "O")).pack(side=tk.RIGHT, padx=20)

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=('Arial', 20), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(button)

    def make_move(self, index):
        if self.current_player is None:
            return  # Wait until player chooses symbol

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                self.status_label.config(
                    text=f"Player {self.current_player} wins!")
                messagebox.showinfo(
                    "Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                self.status_label.config(text="It's a draw!")
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = self.player_symbol if self.current_player == self.opponent_symbol else self.opponent_symbol
                self.status_label.config(
                    text=f"Player {self.current_player}'s turn")

    def check_win(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = self.player_symbol
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL)
        self.status_label.config(text=f"Player {self.current_player}'s turn")


# Launch game
if __name__ == "__main__":
    app = tk.Tk()
    game = TicTacToe(app)
    app.mainloop()
