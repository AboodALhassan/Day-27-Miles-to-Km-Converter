from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.focus()
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=3, row=0)

label2 = Label(text="is equal to ")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)


def miles_to_km():

    miles = entry.get()
    km = float(miles) * 1.61
    km = round(km, 2)
    label3.config(text=f"{km}")


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

window.mainloop()
