import tkinter as tk
import os
import random

# http://www.tysto.com/uk-us-spelling-list.html

# Split british.txt into a list
british = open(os.path.join(os.path.dirname(__file__),
               ".txt"), "r").read().split("\n")

# Split american.txt into a list
american = open(os.path.join(os.path.dirname(__file__),
                "answer.txt"), "r").read().split("\n")


def generate():
    global americanword
    americanword = random.choice(american)
    word.config(text=americanword)


def process(entered):
    britishword = british[american.index(americanword)]
    if entered == britishword:
        correct.pack_forget()
        window.config(bg="#98FB98")  # light green
        window.after(1000, lambda: window.config(bg="#F5F5F5"))  # white
    else:
        window.config(bg="#FFC0CB")  # light pink
        correct.pack(pady=5)
        correct.config(text=f"Incorrect! The correct answer is {britishword}.")
        window.after(1000, lambda: window.config(bg="#F5F5F5"))  # white
    input.delete(0, 'end')  # clear input field after submission
    generate()


window = tk.Tk()
window.title("American-British")
window.geometry("400x200")
window.config(bg="#F5F5F5")  # white

word = tk.Label(window, font=("Arial", 16), bg="#F5F5F5")
word.pack()

input = tk.Entry(window, font=("Arial", 12), bg="#FFFFFF")  # white
input.pack(pady=5)

correct = tk.Label(window, font=("Arial", 12), bg="#F5F5F5")
correct.pack(pady=5)

generate()

input.bind("<Return>", (lambda event: process(input.get())))

window.mainloop()
