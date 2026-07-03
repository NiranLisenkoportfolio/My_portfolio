import tkinter as tk
from tkinter import ttk
import sqlite3

"""In this project I will be creating a todo list for myself as It's a good project to work on"""
program_on = True
my_tasks = []


"""Testing to see if this works"""

while program_on:
    question = input("Do you want to add a task?(yes/no): ").lower()
    if question == "yes":
        new_task = input("Please enter your task: ")
        my_tasks.append(new_task)
    elif question == "no":
        question2 = input("Do you want to cross of a task?(yes/no): ")
        if question2 == "yes":
            print(my_tasks)
            removed_task = input("please pick the task you want to remove, make sure you have no spelling errors: ")
            if removed_task in my_tasks:
                my_tasks.remove(removed_task)
            else:
                print("Sorry, the task you entered is not in the list, please try again.")
            
    else:
        error_prompt = input("You didn't enter a valid value, do you want to try again?(y/n): ")
        if error_prompt == 'y':
            continue
        elif error_prompt == "n":
            program_on = False
        else:
            print("Something isn't working on our end or yours, please try again later.")
            program_on = False
    
    another_go = input("Do you want to end the program?(yes/no): ")
    if another_go == "yes":
        program_on = False
    elif another_go == "no":
        continue
    else:
        print("You got an error message, so we will just keep the progam on, if you want to quit then force quit it on your computer.")

print("Thanks for playing, hope you come back soon. ")




""" 
Here is what I need to imporve:
I should probably add in a GUI, actual database so that it wouldn't reset everything later, and that's all that comes to mind so far.
"""