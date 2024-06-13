import tkinter
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(1, random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(1, random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(1, random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = website_entry.get()
    use = user_entry.get()
    passw = password_entry.get()

    if site == "" or passw == "":
        messagebox.showinfo(title="oops", message="All fields must be filled out")
    else:
        entry_text = f"You entered:\n\nWebsite:\n    {site}\nUser/Email:\n" \
                f"    {use}\nPassword:\n    {passw}\n\nSave this entry?"
        confirm = messagebox.askokcancel(title=site, message=entry_text)
        if confirm:
            with open("data.txt", mode="a") as data:
                data.write(f"{site} | {use} | {passw}\n")
            with open("saved_user.txt", mode="w") as data:
                data.write(f"{use}")

            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password manager")
window.config(pady=20, padx=20)


## Widgets

# Logo
canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = tkinter.Label(text="Website:")
user = tkinter.Label(text="Email/Username:")
pass_list = tkinter.Label(text="Password")
website.grid(column=0, row=1)
user.grid(column=0, row=2)
pass_list.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=54)
website_entry.focus()
user_entry = tkinter.Entry(width=54)
with open("saved_user.txt", mode="r") as data:
    saved_user = data.read()
user_entry.insert(tkinter.END, saved_user)
password_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
user_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

# Buttons
generate = tkinter.Button(text="Generate Password", command=generate_password)
add_password = tkinter.Button(text="Add", width=45, command=save)
generate.grid(column=2, row=3)
add_password.grid(column=1, row=4, columnspan=2)


## Main Loop
window.mainloop()
