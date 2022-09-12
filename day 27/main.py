from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result.config(text=f"{km}")


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=200, height=20)
window.config(padx=30, pady=20)

# Entries
miles_input = Entry(width=10)
# Add some text to begin with
miles_input.grid(column=1, row=0)

# Labels
text = Label(text="Miles")
text.grid(column=2, row=0)

# Labels
text = Label(text="is equals to")
text.grid(column=0, row=1)

# Labels
result = Label(text="0")
result.grid(column=1, row=1)

# Labels
text = Label(text="Km")
text.grid(column=2, row=1)


# calls action() when pressed
button = Button(text="Calculte", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
