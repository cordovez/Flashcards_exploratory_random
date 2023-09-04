from utils.flashcards import Flashcard

def create_cards_from_data(data):
    cards = []
    for item in data :
        for question, answer in item.items():
            question = question
            answer = answer
        cards.append(Flashcard(question, answer))
    return cards