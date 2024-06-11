from tkinter import Tk, Canvas, PhotoImage, Button, Entry, Label, END
from tkinter import messagebox
from random import choice, shuffle 
import json
# from pyperclip import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(1, randint(8, 10))]
    password_list += [choice(numbers) for _ in range(1, randint(2, 4))]
    password_list += [choice(symbols) for _ in range(1, randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    # copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="oops", message="All fields must be filled out")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            with open("saved_user.txt", mode="w") as data_file:
                data_file.write(f"{email}")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ------------------------- SEARCH WEBSITE ---------------------------- #

def find_password():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
        website = website_entry.get().lower()
        searched_email = data[website]['email']
        searched_password = data[website]['password']
    except FileNotFoundError:
        messagebox.showerror("Error", f"No saved websites yet")
    except KeyError:
        messagebox.showerror("Error", f"No saved website: {website_entry.get()}")
    else:
        messagebox.showinfo(f"{website.title()}", f"Email: {searched_email}\n"
                            f"Password: {searched_password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(pady=20, padx=20)


## Widgets

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:", width=15)
user = Label(text="Email/Username:", width=15)
pass_list = Label(text="Password", width=15)
website.grid(column=0, row=1)
user.grid(column=0, row=2)
pass_list.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
user_entry = Entry(width=54)
with open("saved_user.txt", mode="r") as data:
    saved_user = data.read()
user_entry.insert(0, saved_user)
password_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
user_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate = Button(text="Generate Password", width=15, command=generate_password)
add_password = Button(text="Add", width=46, command=save)
search = Button(text="Search", width=15, command=find_password)
generate.grid(column=2, row=3)
add_password.grid(column=1, row=4, columnspan=2)
search.grid(column=2, row=1)


## Main Loop
window.mainloop()

