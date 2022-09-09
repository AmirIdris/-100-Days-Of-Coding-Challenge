class QuizBrain:

    def __init__(self, question_list ):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)


    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score = self.score + 1
            print("You got the answer")
            print(f"The Correct Answer was {correct_answer}")
            print(f"Your Current score is {self.question_number}/{self.score}")

        else:
            print("Your answer is not correct")
            print(f"The Correct Answer was {correct_answer}")
            print(f"Your Current score is {self.question_number}/{self.score}")



    def next_qustion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
        self.check_answer(user_answer = answer, correct_answer = current_question.answer)
  
            


                


