import tkinter as tk
from tkinter import messagebox
import random
import snake_water_gun as game_logic

class SnakeWaterGunGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Water Gun Game")
        self.root.geometry("600x650")
        self.root.configure(bg="#f0f0f0")

        # Game State
        self.choices = {1: "Snake", -1: "Water", 0: "Gun"}

        # UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Snake Water Gun", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        title_label.pack(pady=20)

        # Instructions
        instruction_label = tk.Label(self.root, text="Choose your weapon:", font=("Helvetica", 14), bg="#f0f0f0")
        instruction_label.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=20)

        self.btn_snake = tk.Button(button_frame, text="Snake", font=("Helvetica", 12), command=lambda: self.play_round(1), width=10, bg="#4CAF50", fg="white")
        self.btn_snake.grid(row=0, column=0, padx=10)

        self.btn_water = tk.Button(button_frame, text="Water", font=("Helvetica", 12), command=lambda: self.play_round(-1), width=10, bg="#2196F3", fg="white")
        self.btn_water.grid(row=0, column=1, padx=10)

        self.btn_gun = tk.Button(button_frame, text="Gun", font=("Helvetica", 12), command=lambda: self.play_round(0), width=10, bg="#f44336", fg="white")
        self.btn_gun.grid(row=0, column=2, padx=10)

        # Result Display
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.details_label = tk.Label(self.root, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.details_label.pack(pady=5)

        # Canvas for Animations
        self.canvas = tk.Canvas(self.root, width=600, height=350, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)

    def play_round(self, user_choice):
        # Clear previous animations/text
        self.canvas.delete("all")

        computer_choice = game_logic.get_computer_choice()
        result = game_logic.determine_winner(user_choice, computer_choice)

        user_choice_str = self.choices[user_choice]
        computer_choice_str = self.choices[computer_choice]

        self.details_label.config(text=f"You chose: {user_choice_str} | Computer chose: {computer_choice_str}")

        if result == 0:
            self.result_label.config(text="It's a Draw!", fg="gray")
        elif result == 1:
            self.result_label.config(text="You Won!", fg="green")
            self.animate_win()
        else:
            self.result_label.config(text="You Lost!", fg="red")
            self.animate_loss()

    def animate_win(self):
        # Draw balloon
        # Canvas width is 600, height is 350
        # Start at bottom center
        x_center = 300
        y_start = 350

        # Balloon body
        balloon = self.canvas.create_oval(x_center - 30, y_start, x_center + 30, y_start + 80, fill="yellow", outline="orange")
        # Ribbon
        ribbon = self.canvas.create_line(x_center, y_start + 80, x_center, y_start + 150, fill="red", width=2)

        # Group them or move both
        self.move_balloon(balloon, ribbon)

    def move_balloon(self, balloon, ribbon):
        # Check if items exist (might have been deleted if new game started)
        if not self.canvas.bbox(balloon):
            return

        # Move up by 5 pixels
        self.canvas.move(balloon, 0, -5)
        self.canvas.move(ribbon, 0, -5)

        # Get current coordinates
        coords = self.canvas.coords(balloon)
        # coords is [x1, y1, x2, y2]
        if coords and coords[1] > -100: # Still on screen (with some margin)
            self.root.after(30, lambda: self.move_balloon(balloon, ribbon))
        else:
            # If off screen, delete
             if self.canvas.bbox(balloon):
                 self.canvas.delete(balloon)
             if self.canvas.bbox(ribbon):
                 self.canvas.delete(ribbon)

    def animate_loss(self):
        quotes = [
            "Don't give up!",
            "Believe in yourself!",
            "Failure is the condiment that gives success its flavor.",
            "It does not matter how slowly you go as long as you do not stop.",
            "Keep pushing forward!",
            "Every failure is a step to success."
        ]
        quote = random.choice(quotes)

        text_id = self.canvas.create_text(300, 175, text=quote, font=("Helvetica", 14, "italic"), fill="#333333", width=500, justify="center")

        self.animate_text_float(text_id, 0)

    def animate_text_float(self, text_id, step):
         if not self.canvas.bbox(text_id):
            return

         if step < 60: # Run for 3 seconds (50ms * 60 = 3000ms)
            self.canvas.move(text_id, 0, -1)
            # Optional: Change color to fade
            self.root.after(50, lambda: self.animate_text_float(text_id, step + 1))
         else:
            self.canvas.delete(text_id)

if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeWaterGunGame(root)
    root.mainloop()
