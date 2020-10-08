import csv

accounts = []
csv_fields = ["username", "password"]

# when system startsup, load existing accounts stored in csv into accounts dictionary
def load_accounts():
    with open("Accounts.csv", "a"):
        pass
    with open("Accounts.csv", "r") as accounts_csv:
        csv_reader = csv.DictReader(accounts_csv, fieldnames=csv_fields)
        try:
            next(csv_reader)
        except:
            pass
        for row in csv_reader:
            accounts.append({"username": row["username"], "password": row["password"]})

# creates new account and adds it to accounts dictionary
def create_account(username, password):
    accounts.append({"username": username, "password": password})

# checks if account is valid in the system
def valid_account(username, password):
    for account in accounts:
        un = account["username"]
        pw = account["password"]
        if username == un and password != pw:
            print("This account does not exist. Please check your inputs and try again.\n")
            return False
        elif username != un and password == pw:
            print("This account does not exist. Please check your inputs and try again.\n")
            return False
        elif username == un and password == pw:
            return True

# overwrites csv value so new accounts are added
def system_shutdown():
    with open("Accounts.csv", "w") as accounts_csv:
        output_writer = csv.DictWriter(accounts_csv, fieldnames=csv_fields, lineterminator='\n')
        output_writer.writeheader()
        for account in accounts:
            output_writer.writerow(account)

# Startup
run = True
load_accounts()

# Run System
while run:
    action = input("Hi, Welcome to our login service!\n\n  If you have an account and wish to login type 'Y' and press 'Enter'.\n  If you don't have an account type 'N' and press 'Enter'. We'll help you sign up!\n  If you want to leave our service type 'L' and press 'Enter'.\n")

    # login
    if action == "Y":
        logging_in = True
        while logging_in:
            un = input("Enter your Username and press 'Enter'.")
            pw = input("Enter your Password and press 'Enter'.\n")
            if valid_account(un, pw):
                logging_in = False
                logged_in = True
                while logged_in:
                    logout = input("Welcome to our system! Unfortunately our system is not currently up and running.\nTo log out type 'L' and press 'Enter'.\n")
                    if logout == "L":
                        print("Logging out...\n")
                        logged_in = False
                    else:
                        input("The request you entered is not valid, please press 'Enter' and try again!\n")

    # create account
    elif action == "N":
        un = input("Create your Username by typing it in and pressing 'Enter'.")
        pw = input("Create your Password by typing it in and pressing 'Enter'.\n")
        create_account(un, pw)

    # shut system down
    elif action == "L":
        print("Goodbye!")
        system_shutdown()
        run = False

    # invalid entry
    else:
        input("The request you entered is not valid, please press 'Enter' and try again!\n")


