"""Blackjack, by Al Sweigart al@inventwithpython.com
 The classic card game also known as 21. (This version doesn't have
 splitting or insurance.)
 More info at: https://en.wikipedia.org/wiki/Blackjack
 Tags: large, game, card game"""

import random, sys

# Установим константы
hearts = chr(9829) # Символ 9829 это '♥'.
diamonds = chr(9830)  # Символ 9830 это '♦'.
spades = chr(9824)  # Символ 9824 это '♠'.
clubs =  chr(9827) # Символ 9827 это '♣'.
backside = "backside"


def main()
    pass


def getBet(maxBet):
    # Ваша ставка?
    while True: # Продолжаем спрашивать, пока пользователь не введет валидное число
        print(f"Какова ваша ставка? (1 - {maxBet}, QUIT - для выхода")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Спасибо за игру!")
            sys.exit()
        if not bet.isdecimal(): # Если пользователь не ввел число, спросим снова
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet # Пользователь правильно ввел ставку, функция возвращает ее


def getDeck():
    # Колода из 52 карт (Масть, значение)
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11):
            deck.append(str(rank), suit) # Добавляем нумерованные карты
            for rank in ("J", "Q", "K", "A"): # Валеты, Дамы, Короли, Тузы
                deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayCards(cards): # Выводим карты из списка карт
    rows = ["", "", "", "", ""]
    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)



def getHandValue(dealerHand):
    pass


def displayHands(playerHand, dealerHand, showDealerHand):
    '''Показываем карты игрока и крупье. Прячем первую карту крупье, если showDealerHand - False'''
    print()
    if showDealerHand:
        print("КРУПЬЕ: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("Крупье: ???")
        # Прячем первую крту крупье
        displayCards([BACKSIDE] + dealerHand[1:])
    # Показываем карты игрока
    print("Игрок:", getHandValue(playerHand))
    displayCards(playerHand)