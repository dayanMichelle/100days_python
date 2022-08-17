# pylint: disable=invalid-name
# Write a program that prompts for a password (the password text is not important) and prompts again until both passwords match, with a limit of three prompts.

password = input("Type a new password: ")
count = 0
while count < 3:
    confirm_password = input("Type a again the password: ")
    if password != confirm_password:
        count += 1
        print("Passwords do not match. Try again")
        if count == 3:
            print("Can't enter your username")
    else:
        print("Register successfully")
        count = 4
        