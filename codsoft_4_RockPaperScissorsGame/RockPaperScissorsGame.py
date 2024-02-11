import tkinter as tk
from tkinter import PhotoImage
import random

def play(user_choice):
    global user_score, computer_score
    choices = ["stone", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "stone" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "stone") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1

    show_images(user_choice, computer_choice)
    update_scores()

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

def show_images(user_choice, computer_choice):
    user_image_label.config(image=image_dict.get(user_choice, default_image))
    computer_image_label.config(image=image_dict.get(computer_choice, default_image))

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    result_label.config(text="")
    user_image_label.config(image=default_image)
    computer_image_label.config(image=default_image)

# Create the main window
root = tk.Tk()
root.title("Stone Paper Scissors Game")

# Set window size
root.geometry("1010x700")
root.resizable(False, False)
root.configure(bg="#1c7050")

# Font Style
font_style = ("Arial", 12, "bold")

# Initialize scores
user_score = 0
computer_score = 0

# Create user score label
user_score_label = tk.Label(root, text=f"Your Score: {user_score}",font=font_style)
user_score_label.grid(row=0, column=0, padx=10, pady=10)

# Create computer score label
computer_score_label = tk.Label(root, text=f"Computer's Score: {computer_score}",font=font_style)
computer_score_label.grid(row=0, column=2, padx=10, pady=10)

# Create image labels
image_dict = {
    "stone": PhotoImage(file="Stone.png"),
    "paper": PhotoImage(file="Paper.png"),
    "scissors": PhotoImage(file="Scissor.png")
}

default_image = PhotoImage(file="Paper.png")

user_image_label = tk.Label(root, image=default_image)
user_image_label.grid(row=1, column=0, padx=10, pady=10)

computer_image_label = tk.Label(root, image=default_image)
computer_image_label.grid(row=1, column=2, padx=10, pady=10)

# Create buttons
stone_button = tk.Button(root, text="Stone", command=lambda: play("stone"),font=font_style)
stone_button.grid(row=2, column=0, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"),font=font_style)
paper_button.grid(row=2, column=1, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"),font=font_style)
scissors_button.grid(row=2, column=2, padx=10, pady=10)


play_again_button = tk.Button(root, text="Play Again", command=reset_game,font=font_style)
play_again_button.grid(row=4, column=0, columnspan=3, pady=10)

# Create result label
result_label = tk.Label(root, text="",bg="#1c7050",fg="#ffffff",font=font_style)
result_label.grid(row=3, column=0, columnspan=3, pady=10)

# Start the main loop
root.mainloop()
