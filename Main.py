import string, random, tkinter as tk 

window = tk.Tk()
window.title("Letter Guessing Game")
window.geometry("500x200")
window.resizable(False, False)

choices = list(string.ascii_lowercase)



title_label = tk.Label(window, text="Welcome to my Letter Guessing Game!",
                       font=("Arial",16),
                        fg="Blue",
                        width=35,
                        height=0
                       )

objective_label = tk.Label(window, text="Your objective is to guess the correct letter.",
                        font=("Arial",14),
                        fg="Blue",
                        width=50,
                        height=0
                       )

guess_status = tk.Label(window, text="You have 5 guesses remaining.",
                        font=("Arial",12),
                        fg="Red",
                        width=50,
                        height=0
                       )

letter_entry = tk.Entry(window)

generatedNumber = random.randint(0,25)
chosenLetter= choices[generatedNumber]
print(chosenLetter)


guesses = 5
def on_enter(_):
    global guesses
    print(guesses)
    if guesses == 0:
        return
    print("Check 1")
    user_input = letter_entry.get()
    if len(user_input) == 1 and user_input.isalpha():
        print("Check 2")
        user_input = user_input.lower()
        if user_input == chosenLetter:
            print("Check 3A")
            title_label.config(text="You win!", fg = "Green")
            objective_label.config(text="Woohoo!", fg = "Green")
            guess_status.config(text="Your guess was correct!", fg = "Green")
        else:
            print("Check 3B")
            guesses -= 1
            guess_status.config(text=f"You have {guesses} guesses remaining.")
            if guesses == 0:
                title_label.config(text="You lose!", fg = "Red")
                objective_label.config(text="Boohoo!", fg = "Red")
                guess_status.config(text="Your guesses were all wrong!", fg = "Red")



letter_entry.bind("<Return>", on_enter)
title_label.pack(pady=10)
objective_label.pack(pady=5)
letter_entry.pack(pady=10)
guess_status.pack(pady=5)
window.mainloop()