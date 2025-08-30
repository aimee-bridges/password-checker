#Import the regular expression module
import re

#Load common passwords from a file
def load_common_passwords():
    try:
        #Open the file and read each line into a set
        with open("common_passwords.txt", "r") as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        #If the file doesn't exist, return an empty set
        return set()
