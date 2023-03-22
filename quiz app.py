import random
import tkinter as tk

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0
        
    def get_question(self):
        return self.questions[self.question_index]
    
    def check_answer(self, user_answer):
        if user_answer == self.questions[self.question_index].answer:
            self.score += 1
            return "Correct!"
        else:
            return "Wrong!"
        
    def next_question(self):
        self.question_index += 1
    
    def has_more_questions(self):
        return self.question_index < len(self.questions)
        
# create questions
question_prompts = [
    "What is the largest mammal?\n(a) Elephant\n(b) Blue Whale\n(c) Giraffe\n\n",
    "What is the fastest land animal?\n(a) Cheetah\n(b) Lion\n(c) Elephant\n\n",
    "What is the only continent without any native reptiles?\n(a) Africa\n(b) Antarctica\n(c) Asia\n\n",
    "What is the largest bird in the world?\n(a) Ostrich\n(b) Eagle\n(c) Penguin\n\n",
    "What is the smallest mammal in the world?\n(a) Elephant Shrew\n(b) Bat\n(c) Mouse\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "a")
]

# set up GUI
root = tk.Tk()
root.title("Animal Quiz")

score_label = tk.Label(root, text="Score: 0")
score_label.pack()

question_label = tk.Label(root, text="")
question_label.pack()

answer_entry = tk.Entry(root)
answer_entry.pack()

feedback_label = tk.Label(root, text="")
feedback_label.pack()

def next_question():
    if my_quiz.has_more_questions():
        my_quiz.next_question()
        question_label.config(text=my_quiz.get_question().prompt)
        answer_entry.delete(0, tk.END)
        feedback_label.config(text="")
    else:
        show_result()

def check_answer():
    user_answer = answer_entry.get().strip().lower()
    if user_answer != "":
        feedback = my_quiz.check_answer(user_answer)
        feedback_label.config(text=feedback)
        score_label.config(text=f"Score: {my_quiz.score}")
        answer_entry.delete(0, tk.END)

def show_result():
    score_percent = int((my_quiz.score / len(my_quiz.questions)) * 100)
    result_text = f"You got {my_quiz.score} out of {len(my_quiz.questions)} questions correct ({score_percent}%)."
    question_label.config(text=result_text)
    answer_entry.pack_forget()
    check_button.pack_forget()
    next_button.pack_forget()

my_quiz = Quiz(questions)
question_label.config(text=my_quiz.get_question().prompt)

check_button = tk.Button(root, text="Check Answer", command=check_answer)
check_button.pack()

next_button = tk.Button(root, text="Next Question", command=next_question)
next_button.pack()

root.mainloop()
