from tkinter import *

WIDTH = 500
HEIGHT= 300

def button_clicked():
    my_label["text"] = "I got clicked!"
    print(entry_input.get())


window = Tk()
window.title("My First GUI program")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)



my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.grid(row=0, column=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="I'm New!")
new_button.grid(row=0, column=3)

entry_input = Entry(width=20)
entry_input.grid(row=3, column=4)






window.mainloop()