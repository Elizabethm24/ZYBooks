# 20 Questions with learning
# Prof. O & CPTR-215
# 2023-12-06 first draft

from abc import ABC, abstractmethod

class KnowledgeBase(ABC):
    @abstractmethod
    def play(self):
        pass

class KnowNothing(KnowledgeBase):
    def play(self):
        new_item = input("I don't know anything yet. What were you thinking of? ")
        print(f"Yay, I know what {new_item} is now!")
        return Answer(new_item)

class Answer(KnowledgeBase):
    def __init__(self, answer: str):
        self.answer = answer
    def play(self):
        response = input(f"Were you thinking of {self.answer}? ").upper()[0]
        if response == 'Y':
            print(f"I'm so smart! I guessed that you were thinking of {self.answer}.")
        else:
            new_answer_text = input("I give up! What were you thinking of? ")
            new_question = input(f"Teach me a yes/no question I can use to distinguish between {self.answer} and {new_answer}: ")
            print(f"When I'm thinking of {new_answer} and I ask:\n{new_question}")
            new_yes_no = input("Is the correct answer Yes, or No? ").upper()[0]
            new_answer = Answer(new_answer_text)
            if new_yes_no == 'Y':
                return Question(new_question, new_answer, self)
            else:
                return Question(new_question, self, new_answer)

if __name__ == "__main__":
    kb = KnowNothing()
    while True:
        input("Think of something and I'll guess it. Press Enter when ready.")
        kb = kb.play()