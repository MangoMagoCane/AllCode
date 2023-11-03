import random
import sys

AMOUNT_OF_DECKS = 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]*4*AMOUNT_OF_DECKS

def main():

    while True:
        if not y_n_eval("Do you want to play a game of blackjack?"):
            sys.exit("Okay!")
        if len(cards) < 6:
            sys.exit("All out of cards!")

        random.shuffle(cards)
        dealer_cards, player_cards = [], []
        dealer_score, player_score = 0, 0
    
        for _ in range(2):
            player_score += draw_card(player_cards, player_score)
            dealer_score += draw_card(dealer_cards, dealer_score)

        if player_score == 21:
            print("You won with a blackjack!\n")
            continue
        elif dealer_score == 21:
            print("You lost, dealer had a blackjack\n")
            continue

        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if dealer_score < 17:
            dealer_score += draw_card(dealer_cards, dealer_score)

        if y_n_eval("Do you want to hit?"):
            player_score += draw_card(player_cards, player_score)

        if player_score == dealer_score:
            print("You tied.")
        elif player_score > 21:
            print("You busted.")
        elif dealer_score > 21:
            print('The dealer busted')
        elif player_score > dealer_score:
            print("You won!")
        else:
            print("You lose.")

        print(player_score, player_cards)
        print(dealer_score, dealer_cards)
        print()


def draw_card(hand, total_score):
    cur_card = cards.pop()
    hand.append(cur_card)
    score = cur_card

    for card in hand:
        if card == 11 and (total_score + score) > 21:
            score -= 10
            card = 1

    return score


def y_n_eval(text):
    while True:
        play = input(f"{text} Type 'y' or 'n': ").lower()
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            print("Not a valid response.")


if __name__ == "__main__":
    main()