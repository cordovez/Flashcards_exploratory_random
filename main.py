from utils.fretboard import random_string
from utils.major import Major
from utils.create_cards import create_cards_from_data
from utils.terminal_qa import terminal_q_and_a


STANDARD_TUNING = ["E", "B", "G", "D", "A", "E"]
KEY = "C"
C_MAJOR = Major(KEY)
SCALE = C_MAJOR.scale

test_data = [{"what's your name": "juan"}, {"what is your age": 54}, {"city of birth": "Guayaquil"}]
    


    
def main():

    flashcards = create_cards_from_data(test_data)
    terminal_q_and_a(flashcards)
    
    
if __name__ == "__main__":
    main()
