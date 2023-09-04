import math
from datetime import date, timedelta
repeat_often = []
repeat_occasionally = []
repeat_rarely = []
learned = [ ]
""" See this video for validating and DRY
https://realpython.com/lessons/validate-input-values/
"""

class Card_Data:
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
        
class CardRepetition:
    def today(self):
        today= date.today()
        return today
    
    def graduated(self, val: bool = False):
        return val
    
    def graduated_interval(self, val: float = 2.5):
        return val
    """only after the the second "good" is pressed. This interval reduces
        every time the card is forgotten by -0.2. So 2.3, 2.1, 1.9, 1.7, 1.5 
        and 1.3 being the lowest.""" 
        
    @property
    def score(self):
        """The user's response score"""
        return self._score
    
    @score.setter
    def score(self, value):
        if value >4:
            raise ValueError("only values 1 - 4 allowed") from None
        try:
            self._score = int(value )
        except ValueError:
            raise ValueError("only values 1 - 4 allowed") from None
    """ If you are returning to cards after a delay
        Hard: (next_show + 20/4) * 1.2 == new next_show
        Good: (next_show + 20/2) * 2.5 == new next_show 
        Easy: (next_show + 20) * 3.25 == new next_show 
        
        self.previous_show = None
        self.next_show = math.ceil(self.previous_show * self.graduated_interval) 
        # maximum 100 years"""

class Flashcard:
    counter = 0
    def __init__(self, question: Card_Data(), answer:Card_Data(), score = 0):
        self.question = question
        self.answer = answer
        self.score = CardRepetition()
        Flashcard.counter += 1
      
class User:
    def __init__(self, name: str, username: str, password_hash: str, ):
        self.name= name
        self.username= username
        self.password_hash= password_hash
        self.stack: list = [] # [FretboardNotes, FretboardTriads] 
    


    # intervals increase by x2.5
    
people = [{"name": "owen", "username": "ofeeney", "password_hash": "xxxxxx"}, 
          {"name": "juan", "username": "cordovez", "password_hash": "yyyyyy"}]

data = [("what is your name", "juan"), ("how old are you", "old"), 
         ("where do you live", "paris")]

users = []

# for person in people:
#     users.append(User(person["name"], person["username"], person["password_hash"]))

# for user in users:
#     print(user.name, user.username, user.password_hash)
# stack = []
# for datum in data:
#     card = Flashcard(datum[0], datum[1])
#     stack.append(card)
    
# for card in stack:    

#     print(card.question)
        