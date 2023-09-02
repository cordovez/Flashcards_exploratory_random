import random
# random card:
# def terminal_q_and_a(cards):
#     random_card = random.choice(cards)
#     response = input(random_card.question)
    
#     if str(response).lower().strip() == str(random_card.answer).lower().strip():
#         print("CORRECT!")
#     else:
#         print("INCORRECT ---")
#         print(random_card.answer) 
    
def terminal_q_and_a(cards):
        """ test interactivity for using in the terminal """
        for card in cards:
            response = input(card.question)
            if str(response).lower().strip() == str(card.answer).lower().strip():
                print("CORRECT!")
            else:
                print("INCORRECT ---")
            print(card.answer)

