class Card_Data:
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
        


class Flashcard:
    counter = 0
    question = Card_Data()
    answer = Card_Data()

    
    def __init__(self, question, answer, score = 0):
        self.question = question
        self.answer = answer
        self.score = score
        Flashcard.counter += 1
        
    @property
    def score(self):
        """ The user's response score"""
        return self._score
    
    @score.setter
    def score(self, value):
        if value >4:
            raise ValueError("only values 1 - 4 allowed") from None
        try:
            self._score = int(value )
        except ValueError:
            raise ValueError("only values 1 - 4 allowed") from None

