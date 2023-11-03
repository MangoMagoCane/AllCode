from tkinter import *

WIDTH = 200
HEIGHT = 125    
FONT = ("Ariel", 10)


def miles_to_km():
    miles = int(entry_miles.get())
    km["text"] = miles * 1.609


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=20, pady=20)


label_is_equal = Label(text="is equal to", font=FONT)
label_is_equal.grid(row=1, column=0)

entry_miles = Entry(width=5)
entry_miles.grid(row=0, column=1)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(row=0, column=2)

km = Label(text="0", font=FONT)
km.grid(row=1, column=1)

label_km = Label(text="km", font=FONT)
label_km.grid(row=1, column=2)

calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)



window.mainloop()
