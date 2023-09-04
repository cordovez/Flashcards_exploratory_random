from utils.fretboard import random_string
from utils.major import Major
from utils.create_cards import create_cards_from_data
from utils.terminal_qa import terminal_q_and_a
from models.models import Flashcard, User, Card_Data


STANDARD_TUNING = ["E", "B", "G", "D", "A", "E"]
KEY = "C"
C_MAJOR = Major(KEY)
SCALE = C_MAJOR.scale

people = [{"name": "owen", "username": "ofeeney", "password_hash": "xxxxxx"}, 
          {"name": "juan", "username": "cordovez", "password_hash": "yyyyyy"}]

data = [("what is your name", "juan"), ("how old are you", "old"), 
         ("where do you live", "paris")]

users = []
stack = []


    
def main():

    for person in people:
        users.append(User(person["name"], person["username"], person["password_hash"]))

    for datum in data:
        card = Flashcard(datum[0], datum[1])
        stack.append(card)
        
        
    for user in users:
        print(user.name, user.username, user.password_hash)
        
    for card in stack:    
        print(card.question)
    
    
if __name__ == "__main__":
    main()
