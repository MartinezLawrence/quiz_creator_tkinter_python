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
        self.aswer_a_label = tk.Label(self.window, text="Answer A: ")
        self.aswer_a_label.pack()
        self.question_entry = tk.Text(self.window, height=5, width=50)
        self.question_entry.pack()

        # answer B
        self.answer_b_label = tk.Label(self.window, text="Answer B: ")
        self.answer_b_label.pack()
        self.answer_b_entry = tk.Text(self.window, height=5, width=50)
        self.answer_b_entry.pack()

        # answer C
        self.answer_c_label = tk.Label(self.window, text="Answer C: ")
        self.answer_c_label.pack()
        self.answer_c_entry = tk.Text(self.window, height=5, width=50)
        self.answer_c_entry.pack()

        # answer D
        self.answer_d_label = tk.Label(self.window, text="Answer D: ")
        self.answer_d_label.pack()
        self.answer_d_entry = tk.Text(self.window, height=5, width=50)
        self.answer_d_entry.pack()

        # correct answer
        self.correct_answer_label = tk.Label(self.window, text="Correct Answer (a, b, c, d): ")
        self.correct_answer_label.pack()
        self.correct_answer_entry = tk.Entry(self.window, width=10)
        self.correct_answer_entry.pack()
        
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