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
        self.question_label = tk.Label(self.window, text="Question:")
        self.question_label.pack()
        self.question_entry = tk.Text(self.window, height=5, width=50)
        self.question_entry.pack()

        # answer A
        self.answer_a_label = tk.Label(self.window, text="Answer A:")
        self.answer_a_label.pack()
        self.answer_a_entry = tk.Entry(self.window, width=50)
        self.answer_a_entry.pack()

        # answer B
        self.answer_b_label = tk.Label(self.window, text="Answer B:")
        self.answer_b_label.pack()
        self.answer_b_entry = tk.Entry(self.window, width=50)
        self.answer_b_entry.pack()

        # answer C
        self.answer_c_label = tk.Label(self.window, text="Answer C:")
        self.answer_c_label.pack()
        self.answer_c_entry = tk.Entry(self.window, width=50)
        self.answer_c_entry.pack()

        # answer D
        self.answer_d_label = tk.Label(self.window, text="Answer D:")
        self.answer_d_label.pack()
        self.answer_d_entry = tk.Entry(self.window, width=50)
        self.answer_d_entry.pack()

        # correct answer
        self.correct_answer_label = tk.Label(self.window, text="Correct Answer (a, b, c, d):")
        self.correct_answer_label.pack()
        self.correct_answer_entry = tk.Entry(self.window, width=10)
        self.correct_answer_entry.pack()
        
        # add buttons for "save question" 
        self.save_button = tk.Button(self.window, text="Save Question", command=self.save_question)
        self.save_button.pack()

        # add button for "exit program" 
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.pack()

    # second is save question function
    # check if all fields are filled and choices are in a, b, c, d
    def save_question(self):
        question = self.question_entry.get("1.0", tk.END).strip()
        answer_a = self.answer_a_entry.get()
        answer_b = self.answer_b_entry.get()
        answer_c = self.answer_c_entry.get()
        answer_d = self.answer_d_entry.get()
        correct_answer = self.correct_answer_entry.get().lower()
    
        # if input is valid, save the question and answers to a file
        if question and answer_a and answer_b and answer_c and answer_d and correct_answer in ['a', 'b', 'c', 'd']: 
            with open("quiz.txt", "a") as file:
                file.write(f"Question: {question}\n")
                file.write(f"A: {answer_a}\n")
                file.write(f"B: {answer_b}\n")
                file.write(f"C: {answer_c}\n")
                file.write(f"D: {answer_d}\n")
                file.write(f"Correct Answer: {correct_answer}\n\n")

            # after saving, clear all fields for the next question
            self.question_entry.delete("1.0", tk.END)
            self.answer_a_entry.delete(0, tk.END)
            self.answer_b_entry.delete(0, tk.END)
            self.answer_c_entry.delete(0, tk.END)
            self.answer_d_entry.delete(0, tk.END)
            self.correct_answer_entry.delete(0, tk.END)

            # after saving, display a success message to the user
            messagebox.showinfo("Success!", "Question saved successfully!")

        # if input is invalid, show an error message
        else:
            messagebox.showerror("Error", "Please fill all fields and ensure the correct answer is one of a, b, c, or d.")

    # mainloop function to keep the window open
    def run(self):
        self.window.mainloop()

# fourth is the main function to run the program
if __name__ == "__main__":
    quiz_creator = QuizCreator()
    quiz_creator.run()
