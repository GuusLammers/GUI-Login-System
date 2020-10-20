import csv
import tkinter as tk
from tkinter import *


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Account_Database:
    def __init__(self):
        self.accounts = []
        self.csv_field_names = ["username", "password"]
        self.create_csv()
        self.startup_database()
        pass

    # creates an account and stores it in list accounts
    def create_account(self, username, password):
        self.accounts.append(Account(username, password))

    # checks to see if login information given exists within the database
    def valid_account(self, username, password):
        for account in self.accounts:
            un = account.username
            pw = account.password
            if username == un and password != pw:
                return False
            elif username != un and password == pw:
                return False
            elif username == un and password == pw:
                return True

    # checks if account is valid and if it is logs you in
    def login(self, username, password):
        if self.valid_account(username, password) == True:
            return True
        else:
            return False

    # reads all existing accounts stored in Accounts.csv and stores them as instances of Account in list accounts
    def startup_database(self):
        with open("Accounts.csv", "r") as accounts_csv:
            csv_reader = csv.DictReader(accounts_csv, fieldnames=self.csv_field_names)
            try:
                next(csv_reader)
            except:
                pass
            for row in csv_reader:
                self.accounts.append(Account(row.get("username"), row.get("password")))

    # writes list of all current accounts to csv file
    def shutdown_database(self):
        with open("Accounts.csv", "w") as accounts_csv:
            output_writer = csv.DictWriter(accounts_csv, fieldnames=self.csv_field_names, lineterminator='\n')
            output_writer.writeheader()
            for account in self.accounts:
                output_writer.writerow({"username": account.username, "password": account.password})

    # creates csv file to store existing accounts if it does not already exist
    def create_csv(self):
        with open("Accounts.csv", "a"):
            pass


# GUI methods
def close(r, d):
    d.shutdown_database()
    r.destroy()


def create_account(d, un, pw, label):
    d.create_account(un, pw)
    label.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


def logging_in(d, un, pw, page, invalid):
    if d.login(un, pw):
        invalid.pack_forget()
        page.lift()
    else:
        invalid.forget()
        invalid.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.1)


# start up account database
database = Account_Database()


# GUI
root = tk.Tk()
root.title("Login System")
root.geometry("400x400")


# button and container frame
buttons = Frame(root, bg="grey")
container = Frame(root, bg="grey")
buttons.pack(side="left", fill="both", padx=5, pady=5, expand=False)
container.pack(side="top", fill="both", padx=5, pady=5, expand=True)


# logged in page
logged_page = Frame(container, bg="#d3f5f1")
logged_page.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
logged_label = Label(logged_page, text="You are now logged in!", bg="#d3f5f1", font=40)
logged_label.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.2)


# home page
home_page = Frame(container, bg="#d3f5f1")
home_page.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
home_label = Label(home_page, text="Welcome!", bg="#d3f5f1", font=40)
home_label.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.2)


# login page
login_page = Frame(container, bg="#d3f5f1")
login_page.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

login_un_label = Label(login_page, text="username", bg="#7fb8b1")
login_un_label.place(relx=0.2, rely=0.35, relwidth=0.3, relheight=0.1)
login_pw_label = Label(login_page, text="password", bg="#7fb8b1")
login_pw_label.place(relx=0.2, rely=0.45, relwidth=0.3, relheight=0.1)

login_un_entry = Entry(login_page)
login_un_entry.place(relx=0.5, rely=0.35, relwidth=0.3, relheight=0.1)
login_pw_entry = Entry(login_page)
login_pw_entry.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.1)

invalid_label = Label(login_page, text="Invalid entry, please try again.", bg="#d3f5f1", fg="red")

login_button = Button(login_page, text="login", bg="white", command=lambda: logging_in(database, login_un_entry.get(), login_pw_entry.get(), logged_page, invalid_label))
login_button.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)


# signup page
signup_page = Frame(container, bg="#d3f5f1")
signup_page.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

signup_un_label = Label(signup_page, text="username", bg="#7fb8b1")
signup_un_label.place(relx=0.2, rely=0.35, relwidth=0.3, relheight=0.1)
signup_pw_label = Label(signup_page, text="password", bg="#7fb8b1")
signup_pw_label.place(relx=0.2, rely=0.45, relwidth=0.3, relheight=0.1)

signup_un_entry = Entry(signup_page)
signup_un_entry.place(relx=0.5, rely=0.35, relwidth=0.3, relheight=0.1)
signup_pw_entry = Entry(signup_page)
signup_pw_entry.place(relx=0.5, rely=0.45, relwidth=0.3, relheight=0.1)

created_label = Label(signup_page, text="Account created!", bg="#d3f5f1", fg="green")

signup_button = Button(signup_page, text="sign up", bg="white", command=lambda: create_account(database, signup_un_entry.get(), signup_pw_entry.get(), created_label))
signup_button.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)


# main operational buttons
button_home = Button(buttons, text="Home", command=home_page.lift)
button_login = Button(buttons, text="Login", command=login_page.lift)
button_signup = Button(buttons, text="Sign Up", command=signup_page.lift)
button_exit = Button(buttons, text="Exit", command=lambda: close(root, database))
button_home.pack(fill="x")
button_login.pack(fill="x")
button_signup.pack(fill="x")
button_exit.pack(side="bottom", fill="x")

home_page.lift()

root.mainloop()
