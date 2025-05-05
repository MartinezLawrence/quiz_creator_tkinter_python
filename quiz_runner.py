# Quiz Runner

import tkinter as tk
from tkinter import messagebox

class QuizRunner:
    def __init__(self):
        # initialize the main window
        self.window = tk.Tk()
        self.window.title("QuizRunner")

        # create an input for users to enter their name
        self.name_label = tk.Label(self.window, text="Enter your name:")
        self.name-label.pack(pady=10)
        self.name_entry = tk.Entry(self.window, width=40)
        self.name_entry.pack(pady=5)

        # create start quiz button
        self.start_btn = tk.Button(self.window, text="Start Quiz", command=self.initialize_quiz)
        self.start_btn.pack(pady=20)    # display a button to start quiz
        
        # define variable to hold quiz data and state
        self.questions_list = []    # SET questions_list to an empty list
        self.current_question = 0   # SET current_question_index to 0
        self.score = 0              # SET score to 0
        self.user_answers = []      # SET user_answers_list to an empty list

    # load quiz questions from file
    def load_questions(self):
        try:
            with open("quiz_questions.txt", "r") as file:
                content = file.read().split("\n\n")
                for block in content:
                    if not block.strip():
                        continue
                    lines = [line.strip() for line in block.split("\n") if line.strip()]
                    question_data = {
                        'question': lines[0],replace("Question: ", ""),
                        'answers': {
                            'A': lines[1].replace("A: ", ""),
                            'B': lines[2].replace("B: ", ""),
                            'C': lines[3].replace("B: ", ""),
                            'D': lines[4].replace("B: ", ""),
                        },
                        'correct': lines[5].replace("Correct Answer: ", "").lower()
                    }
                    self.questions_list.append(question_data)
                    
        # if questions list is empty then display an error message and exit           
        except FileNotFoundError:
            messagebox.showerror("Error"!, "Quiz questions file not found!")
            self.window.destroy()

    # get the users name from the entry box
    # if user name is empty then display an error message and return



    # remove name input and start button from window
    # hide name label and start button

    # display the first question and options

# FUNCTION load questions
    # try to open the quiz_questions.txt file for reading
    # if file not found then display an error message and return
    # extract questions and options from the file
    # extract correct answers from the file
    # append each question and its options to questions_list
    # return questions_list
 
# create a function to display the current question and options
    # display the question and options in the window from the questions_list
    # show the mupltiple choice options for the current question
    # track if the user selects an option

# if the user clicks next or submit button
    # check if an answer is selected
    # if not selected then display an error message and return
    # otherwise, save the selected answer to user_answers_list

# if there are more questions in the list
    # show the next question and options
    # repeat the process until all questions are answered

# if the last question is answered and the user clicks submit
    # calculate the score based on the correct answers
    # save the user name and their answers and their score to a file
    # display the score and a message to the user
    # close the quiz window

# THATS IT FOR THE PSEUDOCODE
