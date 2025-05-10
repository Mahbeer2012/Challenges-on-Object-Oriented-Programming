import random

class FruitQuiz:
    # Create a constructor
    def __init__(self):

        # Create a dictionary of fruits as keys and color as value
        self.fruits = {'apple':'red',
                       'orange':'orange',
                       'watermelon':'green',
                       'banana':'yellow'}

# function for the quiz, here a fruit will be chosen randomly
def quiz(self):
    while(True):

        fruit, colour = random.choice(list(self.fruits.items()))

        print("what is the colour of {}".format(fruit))
        user_answer = input()

        if(user_answer.lower() == colour):
            print("correct answer")
        else:
            print("wrong answer")

        option = int(input("enter 0 , if you want to play again otherwise enter 1:"))
        if (option):
            break
        print("welcome to fruit quiz")
        fq = FruitQuiz()
        fq.quiz()
              