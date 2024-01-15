from tkinter import *

root = Tk()
root.title("Futurama Alien Language 1 Decoder")
root.resizable(width=False, height=False)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_images = {}

current_row = 0
current_column = 0

for current_letter in alphabet:
    letter_image = PhotoImage(file=f"./images/letters/{current_letter}.png", width=50, height=50)
    button = Button(image=letter_image,
                    relief=FLAT,
                    command=lambda letter=current_letter: decoded_text.insert(END, letter.upper()))
    button.grid(row=current_row, column=current_column, padx=2, pady=2)
    alphabet_images[current_letter] = letter_image
    if current_column == 12:
        current_row += 1
        current_column = 0
    else:
        current_column += 1

space = Button(text="Space", width=5, height=2, command=lambda: [decoded_text.insert(index=END, chars=" ")])
scruffy = PhotoImage(file="./images/scruffy.png")
clear = Button(image=scruffy, relief=FLAT, 
               command=lambda: decoded_text.delete(index1='1.0', index2=END))
decoded_text = Text(background="white", width=70, height=6, font=("Ariel", 15, "italic"))

space.grid(row=2, column=11)
clear.grid(row=2, column=12)
decoded_text.grid(row=3, column=0, columnspan=13, padx=6, pady=5)

root.mainloop()
