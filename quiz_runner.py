# Quiz Runner

# pseudocode for quiz runner

# initialize the main window and the user interface elements
# make the title of the program "QuizRunner"

# create an input for users to enter their name
# display a label "Enter your name:"
# display an entry box for the user to input their name

# create start quiz button
# display a button to start quiz

# define variable to hold quiz data and state
# SET questions_list to an empty list
# SET current_question_index to 0
# SET score to 0
# SET user_answers_list to an empty list

# FUNCTION initialize_quiz()
    # get the users name from the entry box
    # if user name is empty then display an error message and return

    # load quiz questions from file 
    # if questions list is empty then display an error message and return

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
