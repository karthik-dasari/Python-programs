#Python Program to Shuffle Deck of Cards
import itertools, random
cards = ['Spade', 'Heart', 'Diamond', 'Club']
deck = list(itertools.product(range(1, 14), cards))
random.shuffle(deck)
no_of_cards = int(input("How many cards you want to display?: "))
print("You got:")
for i in range(no_of_cards):
    print(deck[i][0], "of", deck[i][1])