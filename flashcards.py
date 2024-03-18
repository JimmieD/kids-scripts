import tkinter as tk
from random import choice, randint

# Generate all combinations of numbers from 1 to 10 for both addition and subtraction
numbers = range(1, 11)
operations = ['+', '-']

def generate_flashcard():
    # Randomly choose two numbers and an operation
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    operation = choice(operations)
    
    # Ensure the result of subtraction is not negative
    if operation == '-':
        num1, num2 = max(num1, num2), min(num1, num2)
    
    # Update the flashcard text
    flashcard_text.set(f"{num1} {operation} {num2} = ")

def on_key_press(event):
    if event.keysym == 'space':
        generate_flashcard()

# Set up the GUI
root = tk.Tk()
root.title("Math Flashcards")

# Flashcard text
flashcard_text = tk.StringVar()
flashcard_text.set("Press spacebar for a new flashcard")

# Display the flashcard
flashcard_label = tk.Label(root, textvariable=flashcard_text, font=('Helvetica', 96))
flashcard_label.pack(padx=20, pady=20)

# Bind the spacebar key to the function
root.bind('<KeyPress-space>', on_key_press)

# Start the GUI
root.mainloop()
