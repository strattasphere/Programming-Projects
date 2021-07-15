
'''
Computer player hand (dealer)
Human player hand (player)
52 deck of cards
Human bank account
The table

1. player places bet
2. player starts with two cards face up
3. dealer starts with two cards, one face down
4. player goes first
5. Player can choose either hit or stay
6. Hit adds a new card and totals up the sum
6.1 If total equals 21, they win and receives bet + matched bet
6.2. if exceeds 21, player is bust and dealer collects bet
7. Stay moves onto the dealers turn
8. Dealer hits cards, 
8.1 if dealer exceeds 21, they bust and player wins
8.2 if dealer equals or is under 21, dealer wins and dealer collects bet
'''


import random

# Global Variables

suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two" : 2, "Three" : 3, "Four" : 4, "Five" : 5, "Six" : 6, "Seven" : 7, "Eight" : 8, "Nine" : 9,
"Ten" : 10, "Jack" : 10, "Queen" : 10, "King" : 10, "Ace" : 11}


class Player():

    def __init__(self):
        
        self.hand = []

class Human(Player):

    def __init__(self,name, balance):
        self.name = name
        self.balance = balance

    def placeBet(self, bank_balance, amount):
        
        bank_balance = bank_balance - amount

        return bank_balance

class Dealer(Player):

    def __init__(self):
        self.name = 'Dealer'

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    
    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

                #print(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def dealCard(self):
        return self.all_cards.pop()

    def hit(self):
        return self.all_cards.pop()

    def __len__(self):
        return self.all_cards

    def __str__(self):
        return self.all_cards

class BankAccount():
    
    def __init__(self, amount):
        self.amount = amount

    def placeBet(self, bank_balance, amount):
        
        bank_balance = bank_balance - amount

        return bank_balance



    # receive winnings

def showCurrentPlayers(player_list):
    for players in player_list:
        print(players)

def createPlayers():

    correct_info = False

    while correct_info == False:
        print("\nPlease enter your name:\n")

        player = input()

        print("\nHow much money do you have to play with?\n")

        bank_balance = int(input())

        print("\nYour name is {0} and you have £{1} to play with, is that correct?\n".format(player, bank_balance))

        print("Type 'yes', if correct, 'no', if you'd like to re-enter your details:\n")

        user_input = input()

        if user_input == 'yes':
            correct_info = True
            player = Human(player, bank_balance)
            break
        elif user_input.lower() == 'no':
            correct_info = False

    return player

def checkHandTotal(player_hand):
    
    total = 0

    for card in player_hand:
        total = total + card.value

    return total

def showCards(player_hand):

    for card in player_hand:
        print(card)

def playAgain():

    player_input = ''

    print("\nWould you like to play again?\n\nType 'yes' or 'no':")

    player_input = input()

    if player_input == 'yes':

        print("\n\tGet ready for the next game!")

        return True
    
    elif player_input == 'no':

        print("\n\tThanks for playing!")

        return False

def aceValue(player_hand, player_hand_value):
    if player_hand_value >= 22 and player_hand[-1].rank == "Ace":
        #print("The IF is working")
    
        x = 1
        
        for card in player_hand[1:]:
            if player_hand[x].rank == "Ace":
                player_hand[x].value = 1
                
            x += 1
        return player_hand
    else:
        pass
        #print("The ELSE is working")

def outOfMoneyCheck(game_player):

    if game_player.balance <= 0:
    
        print("You've run out of money, it's GAME OVER for you!")
    
        return True
    
    elif game_player.balance > 0:
        return False
    
def playBlackjack(): #MAIN PROGRAM FUNCTION

    play_active = True
    # add_players = True
    player_list = []

    hit_it = True
    bet_placed = 0
    
    player_choice = ""

    # CREATE NEW PLAYERS

    print("\nWelcome to the StrattaCasino!\n\nCan you beat our dealer and take home the prize?\n \nFind out below!")
    
    print("\nWho is playing today?")

    print("\nPLAYER 1")

    player1 = createPlayers()

    player_list.append(player1.name)

    print("\nThe current players are:")

    showCurrentPlayers(player_list)

    # FUTURE IMPLEMENTATION OF MORE PLAYERS
    '''
    print("\nAre there any more players? Type 'yes' or 'no':\n")

    more_players = input()
    
    if more_players == 'yes':
        add_players = True

        player_num = 2
    else:
        add_players = False

    while add_players == True:
        
        print("\nPLAYER {}".format(player_num))
        
        new_player = createPlayers()

        player_list.append(new_player.name)  # THIS IS JUST ADDING A STRING TO THE LIST AND NOT THE OBJECT
        
        print("The current players are:")


        showCurrentPlayers(player_list)

        print("\nType 'yes' to add more players, or 'no' to start the game!\n")

        more_input = input()

        if more_input == 'yes':
            player_num += 1
            continue
        elif more_input == 'no':
            add_players = False '''


    # TO THIS POINT, PLAYERS ARE ADDED TO THE ROSTER
    # AND THE GAME RUNS AS NORMAL
    # THE GAME THEN NEEDS TO PLAY FOR EACH ONE
    # AND THEIR HANDS BE SAVED INTO MEMORY
        

    while play_active == True: # while true, the game loops

        dealer_hand_value = 0
        player_hand_value = 0
        dealer_hand = []
        player_hand = []
        deck = Deck() # initialises the deck every round

        deck.shuffle() # shuffles that deck every round

        print("\nYour current balance is: £{0}".format(player1.balance))

        print("\n\nHere are your cards:\n")

        # DEAL THE FIRST TWO PLAYER CARDS

        player_hand.append(deck.dealCard())
        player_hand.append(deck.dealCard())

        showCards(player_hand)

        # check to see if the hand is == 22 and replace value of ACE if yes
        aceValue( player_hand, checkHandTotal(player_hand)) 

        player_hand_value = checkHandTotal(player_hand)

        print("\nThis totals:", player_hand_value)

        print("\nThe number of cards remaining in the deck is:", len(deck.all_cards)) #to check the length of the deck

        print("\nand here are the dealer's cards:\n")

        dealer_hand.append(deck.dealCard())
        dealer_hand.append(deck.dealCard())

        print("The dealer's first card is:", dealer_hand[0])
        print("The dealer's second card is ???")
        
        print('')
        print("The number of cards remaining in the deck is:", len(deck.all_cards)) # to check the length of the deck

        # PLACE BET

        print("What bet would you like to place?\n")
        bet_placed = int(input())

        print("\nYou placed a bet of £{0}".format(int(bet_placed)))

        player1.balance = player1.placeBet(player1.balance, bet_placed)

        print("\nYour remaining bank balance is: £{0}".format(player1.balance))


        print("\nWould you like to hit or stay?")
        print("\nType either 'hit' or 'stay':\n")
        

        while player_hand_value < 21 or hit_it == True:

            player_choice = input()    # USER INPUT HERE

            if player_choice == "hit":
                player_hand.append(deck.dealCard())
                aceValue(player_hand, checkHandTotal(player_hand))
                print("You've chosen to HIT!")
            
            elif player_choice == "stay":
                hit_it = False
                break
                

            player_hand_value = checkHandTotal(player_hand)
        
            print("Your cards are currently:\n")

            for card in player_hand:
                print(card)

            print ("\nAnd they equal: ", player_hand_value)

            if player_hand_value >= 21:
                break

            print("\nWould you like to hit again or stay?")
            

        if player_hand_value == 21:
            print("Congratualtions, you've won!")

            player1.balance += bet_placed*2

            print("Your bank balance is now: £{0}".format(player1.balance))

            play_active = playAgain()
        
        elif player_hand_value > 21:
            print("Oh no! You've gone bust! Better luck next time, pal!")
            
            if outOfMoneyCheck(player1) == False:

                play_activ = playAgain()
            
            else: 
                play_active = False

        else:
            # dealer's turn
            print("\nIt's now the dealer's turn!")
            print("\nThe dealer's cards are: ")
            showCards(dealer_hand)
            dealer_hand_value = checkHandTotal(dealer_hand)
            print("\nThe dealer's total is:", dealer_hand_value)
                

            while dealer_hand_value <= player_hand_value and dealer_hand_value < 21:
                
                dealer_hand.append(deck.dealCard())
                aceValue(dealer_hand, checkHandTotal(dealer_hand))
                dealer_hand_value = checkHandTotal(dealer_hand)
                
                print("\nThe dealer's cards are: ")
                showCards(dealer_hand)

                print("\nThe dealer's total is:", dealer_hand_value)
        
            if dealer_hand_value > 21:
                print("The dealer has bust!\n")
                print("Congratulations! You've won!")

                player1.balance += bet_placed*2

                print("Your bank balance is now: £{0}".format(player1.balance))

                play_active = playAgain()
                
            elif dealer_hand_value > player_hand_value and dealer_hand_value<= 21:
                print("The dealer has won! Better luck next time!\n")

                play_active = outOfMoneyCheck(player1)



def test():
    
    ace_of_spades = Card("Spades", "Ace")
    three_of_clubs = Card("Clubs", "Three")
    ace_of_hearts = Card("Hearts", "Ace")
    two_of_hearts = Card("Hearts", "Two")
    six_of_diamonds = Card("Diamonds", "Six")
    seven_of_diamonds = Card("Diamonds", "Seven")

    

    player_list = [three_of_clubs, seven_of_diamonds, six_of_diamonds, ace_of_spades]

    print(showCards(player_list))

    print(checkHandTotal(player_list))

    player_hand = aceValue(player_list, checkHandTotal(player_list))

    print("After aceValue replacement")

    print(showCards(player_list))

    print(checkHandTotal(player_list))




playBlackjack()

#test()

