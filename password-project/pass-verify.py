'''
Name: Daniel Nguyen
Date: March 23, 2025
Purpose: 
'''

# Notes: Have to figure out how to work with the hashed password and successfully storing it
#        inside a secure csv file

import hashlib as hsl
import getpass as gp
import re
import os
import csv
import pwinput as pw

# Prompt welcome menu with options
# 1. Register
# 2. Login
# 3. Exit 

# Register:
# Ask for username / password
# Hash password
# Store username and hashed password in a csv file

# Login:
# Ask for username and password
# Hash entered password and compare to stored hash

def main():
    welcome_menu()

def welcome_menu():
    user_answer = 0
    while user_answer != 3: # Continue asking until user exits
        print('Welcome! Choose option 1-3: ' +
            '\n1. Register ' +
            '\n2. Login ' +
            '\n3. Exit ')
        
        user_answer = int(input('Enter: '))

        if user_answer == 1:
            register()
        elif user_answer == 2:
            login()
        elif user_answer == 3:
            print('Exiting. ')
            quit(0) 

def register():
    username = input('Enter your username: ').strip(' ')
    hashed_pw = check_password_strength() # Prompt user to enter password
    save_credentials(username, hashed_pw) # Save credentials once password is valid 
    print(f'Registration successful!' +
          f'\nWelcome, {username}! ')

def login():
    correct_credentials = False

    while True: # Continue to prompt user to enter username and password
        username = input('Enter your username: ').strip(' ')    # Check if username exists in user_credentials file
        pw = input('Enter password: ')
     
    # If not -> error message username does not exist, please register
    # If yes -> check if password is correct (how do I check if a password entered is the same as the hashed password in csv file?)
    # If password if not correct -> error message and reprompt to enter password until password is correct
    # Only give the user 5 attemps before locking them out -> Error message reached limit 
    # If all is correct -> Welcome message

def check_password_strength():
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'                                                               # 8 characters minimum, at least 1 lower case letter,
                                                                                                                                # at least one uppercase letter, at least 1 digit, & 
                                                                                                                                # 1 special character
    try:
        password = pw.pwinput(prompt='Enter your password: ', mask='•')

        if re.fullmatch(pattern, password):
            hashed_pw = hash_password(password) # Call hash function and pass username's password   
            print('Valid password! ')            
            return hashed_pw
        # print('Valid password. ')  
        else:
            print('Invalid password. ')

    except ValueError as e:
        print(e)
    
def hash_password(password):
    encoded_password = password.encode('utf-8')                                                                                 # Encode the password into bytes before hashing
    hashed_password = hsl.sha256(encoded_password)                                                                              # Hash the encoded_password

    return hashed_password

def save_credentials(username, hashed_pw):
    try:            
        if not os.path.exists('user_credentials.csv'):                                                                          # Check if the file exists using os library 
            with open('/Users/danielnguyen/Documents/Coding/Python/password-project/user_credentials.csv', 'w') as file:        # If it does not, open it in 'w' mode 
                file.write('Username, Hashed-PW\n')                                                                             # Write the header
        with open('/Users/danielnguyen/Documents/Coding/Python/password-project/user_credentials.csv', 'r') as file:            # Check if the username exists in csv file by opening and reading the csv file
            lines = file.readlines() # Read each line != null
            username_exists = False # Initialize flag
            for line in lines: # Check column uesrname while loop through each line and split the comma delimiter 
                fields = line.split(',') 
                name = fields[0]
                if name == username:    # If username matches input username, set flag username_exists = True
                    username_exists = True  # After loop ends, check if username_exists = True 
            if username_exists == True: # If True, print error
                print('ERROR: Username already exists. ')   # Else, write and append in csv file 
            else:
                with open('/Users/danielnguyen/Documents/Coding/Python/password-project/user_credentials.csv', 'a') as file:     # With open() automatically closes file afteward
                    file.write(f'{username},{hashed_pw}\n')                                                                      # write() method only takes in a single string

    except FileNotFoundError:
        print('ERROR: File not found. ')

def load_credentials(username, pw):
    try:
        with open('/Users/danielnguyen/Documents/Coding/Python/password-project/user_credentials.csv', 'r') as file: # Open user_credentials file 

main()