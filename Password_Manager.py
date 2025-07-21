
print("Welcome to the password manager")
print("You have can either ADD PASSWORDS or VIEW THE FILE")

def view():
    password_file = "/Users/apple/Desktop/TechWithHer/Password Manager/password_log.txt"
    with open(password_file, "r") as f:
        for lines in f.readlines():     
           data = lines.rstrip()
           user, pswd = data.split("|")
           print("User: ", user, "| Password: ", pswd)

def inpt():
    password_file = "/Users/apple/Desktop/TechWithHer/Password Manager/password_log.txt"
    name = input("Account Name: ")
    password = input("Password: ")
    with open(password_file, "a") as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("Do you want to add the password or view it? inpt/view, q for exit: ")
    if mode == "q":
        print ("Okay Bye!")
        quit()
    elif mode == "inpt":
        inpt()  
    elif mode == "view":
        view() 
    else:
        print("Invalid mode")
