from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# -------------------------------------------- PASSWORD GENERATOR -------------------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for char in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# -------------------------------------------- SAVE PASSWORD -------------------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email_name.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:

            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except (FileNotFoundError, json.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(new_data, data_file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# -------------------------------------------- UI SETUP -------------------------------------------- #
def search():
    website = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"Not data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

generate_btn = Button(text="Search", command=search)
generate_btn.grid(column=2, row=1, sticky="EW")

label_email_name = Label(text="Email/Username:")
label_email_name.grid(column=0, row=2)

entry_email_name = Entry()
entry_email_name.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_name.insert(0, "dayaara6@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()
