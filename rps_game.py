import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        self.user_score = 0
        self.comp_score = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

        self.title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Your Score: 0  |  Computer Score: 0", font=("Arial", 12), bg="#f0f0f0")
        self.score_label.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0", fg="blue")
        self.result_label.pack(pady=10)

        self.comp_choice_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
        self.comp_choice_label.pack()

        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Rock", width=12, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Paper", width=12, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Scissors", width=12, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5)

        tk.Button(root, text="Reset Game", command=self.reset_game).pack(pady=10)

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        self.comp_choice_label.config(text=f"Computer chose: {comp_choice}")

        if user_choice == comp_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or                          (user_choice == "Paper" and comp_choice == "Rock") or                          (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win!"
            self.user_score += 1
        else:
            result = "You Lose!"
            self.comp_score += 1

        self.result_label.config(text=result)
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Your Score: {self.user_score}  |  Computer Score: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.result_label.config(text="")
        self.comp_choice_label.config(text="")
        self.update_score()

if __name__ == "__main__":
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()
