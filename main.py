import random


def draw_card(card, card2, card3):
    lines = [
        [f'┌─────────┐'],
        [f'│{card}        │'],
        [f'│         │'],
        [f'│   / \   │'],
        [f'│   \ /   │'],
        [f'│         │'],
        [f'│        {card}│'],
        [f'└─────────┘']
    ]
    lines2 = [
        [f'┌─────────┐'],
        [f'│{card2}        │'],
        [f'│         │'],
        [f'│   / \   │'],
        [f'│   \ /   │'],
        [f'│         │'],
        [f'│        {card2}│'],
        [f'└─────────┘']
    ]
    lines3 = [
        [f'┌─────────┐'],
        [f'│{card3}        │'],
        [f'│         │'],
        [f'│   / \   │'],
        [f'│   \ /   │'],
        [f'│         │'],
        [f'│        {card3}│'],
        [f'└─────────┘']
    ]

    if card == 10:
        lines = [
            [f'┌─────────┐'],
            [f'│{card}       │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│       {card}│'],
            [f'└─────────┘']
        ]
    if card2 == 10:
        lines2 = [
            [f'┌─────────┐'],
            [f'│{card2}       │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│       {card2}│'],
            [f'└─────────┘']
        ]
    if card3 == 10:
        lines3 = [
            [f'┌─────────┐'],
            [f'│{card3}       │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│       {card3}│'],
            [f'└─────────┘']
        ]

    if card == 11 or card == 1:
        lines = [
            [f'┌─────────┐'],
            [f'│A        │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│        A│'],
            [f'└─────────┘']
        ]
    if card2 == 11 or card2 == 1:
        lines2 = [
            [f'┌─────────┐'],
            [f'│A        │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│        A│'],
            [f'└─────────┘']
        ]
    if card3 == 11 or card3 == 1:
        lines3 = [
            [f'┌─────────┐'],
            [f'│A        │'],
            [f'│         │'],
            [f'│   / \   │'],
            [f'│   \ /   │'],
            [f'│         │'],
            [f'│        A│'],
            [f'└─────────┘']
        ]

    if card == 0:
        lines = [
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f'']
        ]
    if card2 == 0:
        lines2 = [
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f'']
        ]
    if card3 == 0:
        lines3 = [
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f''],
            [f'']
        ]

    for a in range(0 , 8):
        print(f"{lines[a][0]} {lines2[a][0]} {lines3[a][0]}")


def win_condition(ai_sum, user_sum):
    if user_sum < 22 and ai_sum > 21:
        return True
    if user_sum > ai_sum and user_sum < 22:
        return True
    elif user_sum == ai_sum:
        return 2
    else:
        return False

def percentage_ask_card(percent):
    br = random.randint(0,99)
    if percent > br:
        return True
    else:
        return False
def deal_cards(score, played, rounds, percent):
    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_card3 = 0
    ai_card1 = random.choice(cards)
    user_sum = user_card1 + user_card2
    print(f"You got: {user_card1} , {user_card2} ({user_sum})")
    draw_card(user_card1, user_card2, 0)
    print(f"Opponent got: {ai_card1}\n")
    draw_card(ai_card1, 0, 0)
    #q = input("do you want to draw one more card? (y/yes)\n")
    if percentage_ask_card(percent):
        user_card3 = random.choice(cards)



    user_sum = user_sum + user_card3

    if user_card1 == 11 and user_sum > 21:
        user_card1 -= 10
        user_sum -= 10
    if user_card2 == 11 and user_sum > 21:
        user_card2 -= 10
        user_sum -= 10
    if user_card3 == 11 and user_sum > 21:
        user_card3 -= 10
        user_sum -= 10
    ai_card2=random.choice(cards)
    ai_sum = ai_card1 + ai_card2
    ai_card3 = 0
    if ai_sum < 17:
        ai_card3 = random.choice(cards)
    ai_sum = ai_sum + ai_card3
    result = win_condition(ai_sum, user_sum)

    if user_card3 > 0:
        print(f"\nSum of your cards is: {user_sum} ({user_card1} + {user_card2} + {user_card3})")
        draw_card(user_card1, user_card2, user_card3)
    else:
        print(f"Sum of your cards is: {user_sum} ({user_card1} + {user_card2})")
        draw_card(user_card1,user_card2,0)
    if ai_card3 > 0:
        print(f"Sum of opponents cards is: {ai_sum} ({ai_card1} + {ai_card2} + {ai_card3})")
        draw_card(ai_card1,ai_card2,ai_card3)
    else:
        print(f"Sum of opponents cards is: {ai_sum} ({ai_card1} + {ai_card2})")
        draw_card(ai_card1,ai_card2,0)

    if result == True:
        print("\nYOU WIN")
        score[0] = score[0] + 1
    elif result == 2:
        print("\nDRAW")
        score[1] = score[1] + 1
    else:
        print("\nYOU LOSE")
        score[2] = score[2] + 1
    win_percentage = round((score[0] / (score[0] + score[1] + score[2])) * 100, 2)
    print(f"Score: {score[0]}/{score[1]}/{score[2]} (W/D/L) Win percentage: {win_percentage}%\n")
    rounds = rounds - 1
    if rounds > 0:
        return [True, rounds]
    else:
        return [False, rounds]



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
a = [True, 0]
score = [0, 0, 0] # W/D/L
played = 0
rounds = 0
percent = 0

rounds = int(input("How many rounds of playing"))
percent = int(input("Percentage of drawing third card"))
while a[0]:
    a = deal_cards(score, played, rounds, percent)
    rounds = a[1]
