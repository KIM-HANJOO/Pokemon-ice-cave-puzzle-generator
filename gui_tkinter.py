from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Pokavé")
window.geometry("200x200")

def generate_clicked() :
    gen = map()


class map () :
    def __init__(self) :

        pass

generate_btn = Button(window, text = "GENERATE !", command = generate_clicked)
generate_btn.grid(column = 0, row = 0)

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1)
combo.grid(column = 0, row = 1)




window.mainloop()