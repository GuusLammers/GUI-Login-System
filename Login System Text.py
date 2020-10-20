import csv

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

# Startup
account_database = Account_Database()
run = True

# Run System
while run:
    action = input("Hi, Welcome to our login service!\n\n  If you have an account and wish to login type 'Y' and press 'Enter'.\n  If you don't have an account type 'N' and press 'Enter'. We'll help you sign up!\n  If you want to leave our service type 'L' and press 'Enter'.\n")

    # login
    if action == "Y":
        logging_in = True
        while logging_in:
            un = input("Enter your Username and press 'Enter'.")
            pw = input("Enter your Password and press 'Enter'.\n")
            if account_database.login(un, pw):
                logging_in = False
                logged_in = True
                while logged_in:
                    logout = input("Welcome to our system! Unfortunately our system is not currently up and running.\nTo log out type 'L' and press 'Enter'.\n")
                    if logout == "L":
                        print("Logging out...\n")
                        logged_in = False
                    else:
                        input("The request you entered is not valid, please press 'Enter' and try again!\n")
            else:
                print("This account doesn't exist. Please check your inputs and try again.\n")

    # create account
    elif action == "N":
        un = input("Create your Username by typing it in and pressing 'Enter'.")
        pw = input("Create your Password by typing it in and pressing 'Enter'.\n")
        account_database.create_account(un, pw)

    # shut system down
    elif action == "L":
        print("Goodbye!")
        account_database.shutdown_database()
        run = False

    # invalid entry
    else:
        input("The request you entered is not valid, please press 'Enter' and try again!\n")
