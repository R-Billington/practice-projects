import random

money = 100

#Write your game of chance functions here

#Flips coin and returns winnings or losses
def coin_flip(guess, bet):
    print('Flipping a coin...\n')
    one_or_two = random.randint(1, 2)
    
    if one_or_two == 1:
        coin = 'Heads'
    elif one_or_two == 2:
        coin = 'Tails'
    
    print(f'You called {guess} and bet £{str(bet)}...\n')
    print(f'The coin landed on {coin}.\n')
    
    if guess == coin:
        print(f'You won £{str(bet)}!\n')
        return bet
    else:
        print(f'You lost £{str(bet)}.\n')
        return -bet
    
    
#Rolls two dice and lets player guess if total is odd or even
def cho_han(guess, bet):
    print('Rolling two dice...\n')
    roll_one = random.randint(1, 6)
    print(f'The first dice rolled a {str(roll_one)}\n')
    roll_two = random.randint(1, 6)
    print(f'The second dice rolled a {str(roll_two)}\n')
    total = roll_one + roll_two
    
    if total % 2 == 0:
        result = 'Even'
    else:
        result = 'Odd'
    
    print(f'You guessed {guess} and bet £{str(bet)}...\n')
    print(f'The dice totaled {str(total)}, an {result} number!\n')
        
    if guess == result:
        print(f'You won £{str(bet)}!\n')
        return bet
    else:
        print(f'You lost £{str(bet)}.\n')
        return -bet
    
#Simulates two cards being drawn from a deck, highest wins
def two_card_draw(bet):
    print('Drawing two cards...\n')
    print(f'You bet £{str(bet)}...\n')
    deck = []
    for i in range(2, 15):
        deck.append(i)
        deck.append(i)
        deck.append(i)
        deck.append(i)
        
    player_card_num = deck[random.randint(0, 51)]
    deck.remove(player_card_num)
    opponent_card_num = deck[random.randint(0, 50)]
    
    player_card = card_number_to_name(player_card_num)
    opponent_card = card_number_to_name(opponent_card_num)
    
    print(f'You drew a(n) {str(player_card)}\n')
    print(f'Your opponent drew a(n) {str(opponent_card)}\n')
    
    if player_card_num == opponent_card_num:
        print('It\'s a draw!\n')
        return 0
    elif player_card_num > opponent_card_num:
        print(f'You won £{str(bet)}!\n')
        return bet
    else:
        print(f'You lost £{str(bet)}.\n')
        return -bet
    
#Converts number to picture card name for card draw game
def card_number_to_name(card_number):
    if card_number == 14:
        return 'Ace'
    elif card_number == 11:
        return 'Jack'
    elif card_number == 12:
        return 'Queen'
    elif card_number == 13:
        return 'King'
    else:
        return card_number
    
#Roulette - guess a number or odd/even and returns winnings/losses
def roulette(guess, bet):
    print('Spinning the roulette wheel...\n')
    result = random.randint(0, 36)
    
    if result % 2 == 0:
        odd_or_even = 'Even'
    else:
        odd_or_even = 'Odd'
        
    print('The wheel is spinning...\n')
    print(f'It landed on a {str(result)}!\n')
    
    if guess == 'Odd' or guess == 'Even':
        print(f'You guessed {guess} and bet £{str(bet)}...\n')
        if guess == odd_or_even:
            print(f'You won £{str(bet)}!\n')
            return bet
        else:
            print(f'You lost £{str(bet)}.\n')
            return -bet
    else:
        print(f'You guessed {str(guess)} and bet £{str(bet)}...\n')
        if guess == result:
            print(f'You won £{str(bet * 35)}!\n')
            return bet * 35
        else:
            print(f'You lost £{str(bet)}.\n')
            return -bet
    
    
    
        
#Call your game of chance functions here

money += coin_flip('Heads', 10)

print(f'£{money} left\n')

money += cho_han('Odd', 20)

print(f'£{money} left\n')

money += two_card_draw(15)

print(f'£{money} left\n')

money += roulette(7, 10)

print(f'£{money} left\n')

money += roulette('Odd', 30)

print(f'£{money} left\n')

















