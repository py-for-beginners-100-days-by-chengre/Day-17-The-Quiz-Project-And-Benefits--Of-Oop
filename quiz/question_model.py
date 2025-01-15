"""Task 1create a new class called Question,
and that Question class should have an __init()__ method which will initialize two attributes the text and
the answer"""

class Question:
    def __init__(self, question_text, question_answer):
        self.text = question_text
        self.answer = question_answer



"""
Task2
Write a loop to iterate over question_data.
Create question object from each entry in the question_data.
Append eachQuestion object to the question_bank

So what we need to do is we need to be able to bring this question data into the
main.py file. But instead of having a list of dictionaries,
we want a list of question objects.
We know already that we can create a new question object by simply constructing
one from the question and then giving it the required inputs.
But in order to do this inside the main.py file,
we, of course, have to import the question model and we'll also need to import the
data.py. So from the question model
I'm going to import the question class, and from the data file
I'm going to import the question data.
Now that you've got both the question data and the question class,
your goal is to create the question bank.
And once you're done,
it should contain a list of question objects
each being initialized with a question and an answer,
and the data is going to come from these dictionaries from the question data.
So you'll need to think about how you can loop through that question data in
order to create this list of question objects.
Pause the video and give that a go now.        """








"""
Task 3:
create a class called quizbrain,
write an init method
initialize the question number to 0 
initialize the question list to  input
"""


"""

Create a method called next_question inside the QuizBrain.

This method needs to retrieve the item at the current question number from the

question list. And once you have this item,

use the input function to show the user the question text and ask for the

user's answer   




"""







"""

QuizBrain? Your job is to create a new method here

which is going to be called still_has_questions.

And this is going to return a boolean, either true or false.

And depending on that boolean,

we can get our while loop to keep working and keep running and looping,

or we're going to get the loop to stop

once the quiz has run out of questions.
"""






"""
what you're aiming for is to be able to print out the score and the current

question so that you can tell the user 'Your current score is:' and printed out
"""