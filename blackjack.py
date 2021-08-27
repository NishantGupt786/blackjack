import random

player_1 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])
player_2 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])
dealer_1 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])
dealer_2 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])

print('Your cards are:', player_1, "," ,player_2)
print("Dealers first card is", dealer_1)

if player_1 == 'Jack' or player_1 == 'Queen' or player_1 == 'King':
    playercard1 = 10
else:
    playercard1 = player_1

if player_2 == 'Jack' or player_2 == 'Queen' or player_2 == 'King':
    playercard2 = 10
else:
    playercard2 = player_2

if dealer_1 == 'Jack' or dealer_1 == 'Queen' or dealer_1 == 'King':
    dealercard1 = 10
else:
    dealercard1 = dealer_1

if dealer_2 == 'Jack' or dealer_2 == 'Queen' or dealer_2 == 'King':
    dealercard2 = 10
else:
    dealercard2 = dealer_2

stand = input("Do you want another card?(y/n)")
if stand == 'y':
    player_3 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])
    print("Yor third card is", player_3)

    if player_3 == 'Jack' or player_3 == 'Queen' or player_3 == 'King':
        playercard3 = 10
    else:
        playercard3 = player_3

    playertotal = playercard1 + playercard2 + playercard3

elif stand == 'n':
    playertotal = playercard1 + playercard2

else: 
    print('input error')

dealertotal = dealercard1 + dealercard2

print('The dealers 2nd card was', dealer_2)

if dealertotal <= 14:
    dealer_3 = random.choice([1,2,3,4,5,6,7,8,9,10,'Jack', 'Queen', 'King'])
    print('dealer has taken another card, ', dealer_3)

    if dealer_3 == 'Jack' or dealer_3 == 'Queen' or dealer_3 == 'King':
        dealercard3 = 10
    else:
        dealercard3 = dealer_3

    dealertotal += dealercard3

if playertotal > 21 and dealertotal <= 21:
    print('You got busted!')
elif playertotal <= 21 and dealertotal > 21:
    print('Dealer busted!! You win!')
elif playertotal == 21 and dealertotal != 21:
    print('You got BlackJack!!')
elif playertotal != 21 and dealertotal == 21:
    print('Dealer got BlackJack!!')
elif playertotal > 21 and dealertotal > 21:
    print('Both of you got busted!')
elif playertotal <= 21 and dealertotal <= 21 and dealertotal > playertotal:
    print('Dealer is closer to 21! You lose.')
elif playertotal <= 21 and dealertotal <= 21 and dealertotal < playertotal:
    print('You are closer to 21! You win!')
