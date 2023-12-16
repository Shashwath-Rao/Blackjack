import random

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def remove_one(self):
        return self.deck.pop(0)


def print_some(computer, player):
    print("Dealer Hand: ")
    print('"Not Shown"', computer[1], sep='\n')
    print()
    print("Player Hand: ")
    print(player[0], player[1], sep='\n')
    print()
    players_total(player)


def print_all(computer, player):
    print("Dealer's Hand: ")

    for card in range(len(computer)):
        print(computer[card])

    print()
    dealers_total(computer)
    print("Player's Hand: ")

    for card in range(len(player)):
        print(player[card])

    print()
    players_total(player)


def dealers_total(computer):
    print(f"Dealer's Total: {check_ace(computer)}")
    print()


def players_total(player):
    print(f"Player's Total: {check_ace(player)}")
    print()


def check_ace(hand):
    ace_count = 0
    ace_adjusted_total = 0

    for card in range(len(hand)):
        ace_adjusted_total += hand[card].value

        if hand[card].value == 11:
            ace_count += 1

    if ace_adjusted_total > 21 and ace_count > 0:
        for card in range(ace_count):
            ace_adjusted_total -= 10
        return ace_adjusted_total

    else:
        return ace_adjusted_total


def hit(computer_cards, player_cards, player_deck):

    while True:
        a1 = check_ace(player_cards)

        if a1 <= 21:
            player_cards.append(player_deck.pop(0))
            return player_cards
        else:
            player_lose(computer_cards, player_cards)
            break


def hit_stand(computer_cards, player_cards, player_deck):
    global playing

    while True:
        hs = input("Do you want to hit or stand! (h or s): ")

        if hs == 's':
            playing = True
            break

        elif hs == 'h':
            player_cards = hit(computer_cards, player_cards, player_deck)

            if check_ace(player_cards) <= 21:
                print_all(computer_cards, player_cards)

            else:
                player_lose(computer_cards, player_cards)
                break

        else:
            print("Please enter correct value: ")
            continue


def play_dealer(computer_cards, player_cards, computer_deck):

    while True:
        comp_total = check_ace(computer_cards)
        player_total = check_ace(player_cards)

        if comp_total > player_total:
            player_lose(computer_cards, player_cards)
            break

        elif comp_total <= 17:
            computer_cards.append(computer_deck.pop(0))

            if check_ace(computer_cards) <= 21:
                print_all(computer_cards, player_cards)

            else:
                dealer_lose(computer_cards, player_cards)
                break

        elif comp_total == player_total:
            print_all(computer_cards, player_cards)
            print("It's a tie!!!")
            break

        else:
            dealer_lose(computer_cards, player_cards)
            break


def player_lose(computer_cards, player_cards):
    global playing
    print_all(computer_cards, player_cards)
    print("Player has lost!")
    print("Dealer has won!!!")
    print(f"Total chips remaining: {100 - chip}")
    playing = False


def dealer_lose(computer_cards, player_cards):
    global playing
    print_all(computer_cards, player_cards)
    print("Dealer has lost!")
    print("Player has won!!!")
    print(f"Total chips remaining: {chip + 100}")
    playing = False


def chip_bet():

    while True:
        bet = int(input("Welcome to Blackjack please enter your bet (1 to 100): "))

        if 1 <= bet <= 100:
            return bet

        else:
            print("Please enter a value between 1 and 100 !!!")


def run_logic():

    deck = Deck()
    deck.shuffle()

    computer_deck = []
    player_deck = []

    com_cards = []
    player_cards = []

    for x in range(26):
        computer_deck.append(deck.remove_one())
        player_deck.append(deck.remove_one())

    com_cards.extend([computer_deck.pop(0), computer_deck.pop(1)])
    player_cards.extend([player_deck.pop(0), player_deck.pop(1)])

    print_some(com_cards, player_cards)
    hit_stand(com_cards, player_cards, player_deck)

    if playing:
        play_dealer(com_cards, player_cards, computer_deck)


while True:

    chip = chip_bet()
    run_logic()

    if input("Do you want to continue to play BlackJack (y or n): ") == 'n':
        print("Game Over")
        break
