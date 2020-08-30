import random

#chooses a random card and removes it from the cards list
def randomCard(cards):
    card = random.choice(cards)
    cards.remove(card)
    return card
    
#converts each playing card to its point value
def cardNumber(cards, numcards):
    for card in cards:
        if (card == 'Q' or card == 'J' or card == 'K'):
            numcards.append(10)
        #ace card is set at value of 11 for now; aceUpdate function takes account of that
        elif (card == 'A'):
            numcards.append(11) 
        #number cards value are determined through string slicing
        else:
            card = int(card[:-1])
            numcards.append(card)

#alters the value of ace card based on whether the total value is over 21
def aceUpdate(total, cards, numcards):
    if (total > 21 and ("A" in cards)):
        for x in numcards:
            if (x == 11): 
                numcards.remove(x)
                numcards.append(1)
            if (sum(numcards) < 21):
                break
            

#plays introduction sequence where user is given the option for instructions
print("Welcome to Blackjack!")
ans = input("Would you like the instructions?(yes/no): ").lower().strip()
if(ans == "yes" or ans == "y"):
    print()

    print("You are tasked with beating the dealer’s hand total, without exceeding 21.\nThe following card values hold true in Blackjack:\n-Face cards are valued at 10\n-Aces are valued at 1 or 11\n-Cards 2-10 retain their face value")

    print("\nFor this game: A = Ace, J = Jack, Q = Queen, K = King,\nc = Clubs, h = Hearts, s = Spades, d = Diamonds, e.x. 8c is 8 of clubs")
    print('\n"BUSTED" means that the total of your cards is over 21.\n"BLACKJACK" means that you recieved a total of 21 with\nyour first two cards and automatically win!')

    print('\n"HIT" means you want another card and "STAND" means you are\nfinished and want no more cards.')
    input("Enter to continue...")

print()


#loop allows game to re-run
while True:        
    #list of the deck of cards
    cards = ['A', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h',
                 'A', '2s' , '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s',
                 'A', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c',
                 'A', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d',
                 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K',
                 'K', 'K', 'K']
    
    #a list of player cards is created where two random cards are appended to it       
    playercards = []
    for i in range (2):
        playercards.append(randomCard(cards))
    
    #a separate list containing the point value of the player's cards    
    numplayercards = []
    cardNumber(playercards, numplayercards)
    
    print('Your cards:' + ' ' + " ".join(map(str, playercards)))
    
    #if the point total equals 21, it's blackjack
    total = sum(numplayercards)
    if (total == 21):
            print ("BLACKJACK!")

    #player's loop sequence if they hit or stand
    while True:
        #updates possible ace card before total is calculated
        aceUpdate(total, playercards, numplayercards)
        
        #sums point value list to find total
        total = sum(numplayercards)
        if (total == 21):
            break
        if (total > 21):
            print ("BUSTED!")
            total = "BUST"
            break
        
        #player chooses to HIT or STAND; if functions employed
        choice = input("Choose to HIT or STAND: ").lower()
        if (choice == "hit" or choice == "h"):
            card = randomCard(cards)
            playercards.append(card)
            numplayercards = []
            cardNumber(playercards, numplayercards)
            total = sum(numplayercards)
            print ("Card: " + card)
        elif (choice == "stand" or choice == "s"):
            break
        else:
            print ("Invalid input, try again")
            print ()
        print()
        
    #similar sequence of algorithms occurs for the automated dealer
    dealercards = []
    for i in range (2):
        dealercards.append(randomCard(cards))
    numdealercards = []
    cardNumber(dealercards, numdealercards)
    while True:
        dealertotal = sum(numdealercards)
        #if the dealer's point total is under 16, they continue to hit
        if (dealertotal >= 16):
            if (dealertotal > 21):
                dealertotal = "BUST"
            break
        dealercards.append(randomCard(cards))
        numdealercards = []
        cardNumber(dealercards, numdealercards)
        dealertotal = sum(numdealercards)
        aceUpdate(dealertotal, dealercards, numdealercards)
        
    print()         
    print('Your cards: ' + " ".join(map(str, playercards)))
    print('Dealer cards: ' + " ".join(map(str, dealercards)))

    #compares totals to determine winner
    if (total == "BUST" and dealertotal == "BUST"):
        print ("YOU DRAW.")
    elif (total == "BUST"):
        print ("YOU LOSE!")
    elif (dealertotal == "BUST"):
        print ("YOU WIN!")
    elif (dealertotal == total):
        print ("YOU DRAW.")
    elif (dealertotal > total):
        print ("YOU LOSE!")
    elif (total > dealertotal):    
        print ("YOU WIN!")
    print()
    ans = input("Would you like to play again?(y/n): ").lower().strip()
    if(ans == "n"):
        break
    print()
