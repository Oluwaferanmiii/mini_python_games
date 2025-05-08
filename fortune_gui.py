import tkinter as tk
import random

# Funny fortune list
fortunes = [
    "A syntax error in time saves nine.",
    "Beware of the segfault in your heart.",
    "Today is a good day to refactor your life.",
    "Love is like recursion – beautiful but dangerous if unchecked.",
    "You will meet someone special... in your Git history.",
    "Try again after a full system reboot (including emotions).",
    "The compiler of fate has no backspace key.",
    "Your destiny has been deprecated.",
    "Documentation is the real MVP.",
    "Commit early, commit often, regret always."
]

# Function to display random fortune


def crack_cookie():
    fortune = random.choice(fortunes)
    fortune_label.config(text=fortune)


# Create GUI window
root = tk.Tk()
root.title("🥠 Pythonic Fortune Cookie")
root.geometry("500x300")
root.config(bg="#fff8dc")  # Light cookie color

# Fortune label
fortune_label = tk.Label(root, text="Click the cookie to reveal your fortune!",
                         wraplength=400, font=("Comic Sans MS", 14), bg="#000000", justify="center")
fortune_label.pack(pady=50)

# Button to "crack the cookie"
crack_button = tk.Button(root, text="🥠 Crack Cookie", command=crack_cookie,
                         font=("Helvetica", 16, "bold"), bg="#deb887", fg="black", padx=20, pady=10)
crack_button.pack()

# Run the app
root.mainloop()
