# If you give your script inputs on the command line, then you use argv or if you want them to input using the keyboard while the script is running, then use input().

from sys import argv
script, firstname, lastname, course = argv

roll_number = input("What is your roll number? ")

print("Roll no. ", roll_number)
print("Welcome ", firstname + ' ' + lastname)
print("Here to attend ", course)
