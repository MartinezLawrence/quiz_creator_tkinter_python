# quiz creator program using tkinter in python
# this program will create a quiz file with questions and answers
# and save it to a file the user can also load an existing quiz file 

# first is initialize the GUI
import tkinter as tk
from tkinter import messagebox 

# create a window with fields
class QuizCreator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Creator 6969")
    
        # question
        self.question_label = tk.Label(self.window, text="Question: ")
        self.question_label.pack()
        self.question_entry = tk.Text(self.window, height=5, width=50)
        self.question_entry.pack()

        # answer A
        # answer B
        # answer C
        # answer D
        # correct answer
    # add buttons for "save" "question" and "exit"

# second is save question function'
    # this is where input validation occurs
        # check if all fields are filled out
        # check if the correct answer is one of the options

    # save data
        # if input is valid, save the question and answers to a file 

    # clear fields
        # after saving, clear all fields for the next question

    # display success message
        # after saving, display a success message to the user

# third is exit program
    # this will close the program when the user clicks the exit button

# fourth is the main loop
    # this will run the program and keep it open until the user exits