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
BACKSIDE = "backside"


def main():
    print("""Играем в Блэкджек!
    Правила:
        1. Цель игры — набрать 21 очко или близкую к этому сумму и обыграть Дилера. 
           Если игрок набирает сумму очков, превышающую 21, то его ставка проигрывает.
        2. Короли, Дамы и Валеты - 10 очков
        3. Тузы - 1 или 11 очков (если без туза у Вас <= 10 очков, то Туз - 11 очков, в противном случае - 1 очко
        4. Карты номиналом от 2 до 10 - дают соответствующее количество очков
    Управление:
        (H)it (прим. - 'Ещё') ► взять ещё одну карту
        (S)tand (прим. - 'Достаточно') ► перестать брать карты
        (D)ouble down (прим. - 'повысить ставки') ► доступно на первом ходу, вам нужно будет взять ещё одну карту
    Примечание:
        Дилер(Крупье) перестаёт набирать карты, когда у него уже есть 17 очков
        В случае ничьи (равное количество очков у Дилера и Игрока) Вам возвращается Ваша ставка""")
    money = 5000
    while True:  # Основной игровой цикл
        if money <= 0:
            print("Вы банкрот!")
            print("Как хорошо, что Вы не играли на настоящие деньги!")
            print("Спасибо за игру!")
            sys.exit()
        # Дадим возможность игроку сделать ставку:
        print(f"Деньги: ${money}")
        bet = getBet(money)

        # Дадим дилеру и игроку по две карты из колоды:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Организуем действия игрока:
        print(f"Ставка: ${bet}")
        while True:  # Продолжаем цикл, пока игрок не перестанет брать карты или не произойдет перебор по очкам
            displayHands(playerHand, dealerHand, False)
            print()

            # Не перебрал ли игрок по очкам?
            if getHandValue(playerHand) > 21:
                break

            # Ход игрока:
            move = getMove(playerHand, money - bet)
            if move == "D":
                # Игрок может повысить ставку
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Ваша ставка возрасла на ${additionalBet}")
                print(f"Итоговая ставка: ${bet}")

            if move in ("H", "D"):  # "Ещё" или "Повысить ставки" - игроку дается ещё одна карта
                newCard = deck.pop()
                rank, suit = newCard
                print(f"Вытянули карту {rank} {suit}")
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    # Игрок перебрал
                    continue
            if move in ("S", "D"):  # "Достаточно" или "Повысить ставки" заканчивает ход
                break

        # Дилеру тоже нужно ходить :)
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # Дилер берет карту:
                print("Дилер берет карту...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # Дилер перебрал по очкам
                input("Нажмите ENTER, чтобы продолжить...")
                print("\n\n")

        # Показываем карты:
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

            # Разберемся, игрок победил, проиграл или же случилась ничья
        if dealerValue > 21:
            print(f"Дилер перебрал очков! Вы выиграли {bet}")
            money += bet
            print(f"Теперь у Вас на счету: ${money}")
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("Ваша ставка проиграла!")
            money -= bet
            print(f"Теперь у Вас на счету: ${money}")
        elif playerValue > dealerValue:
            print(f"У Дилера меньше очков, чем у Вас! Вы выиграли {bet}")
            money += bet
            print(f"Теперь у Вас на счету: ${money}")

        elif playerValue == dealerValue:
            print("Ничья! Ваша ставка возвращается к Вам")
        input("Нажмите ENTER, чтобы продолжить... ")
        print("\n\n")


def getBet(maxBet):
    # Ваша ставка?
    while True: # Продолжаем спрашивать, пока пользователь не введет валидное число
        print(f"Какова ваша ставка? (1 - {maxBet}, Q - для выхода)")
        bet = input("> ").upper().strip()
        if bet == "Q" or bet == "q":
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
            deck.append((str(rank), suit)) # Добавляем нумерованные карты
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



def getHandValue(cards):
    """Возвращает, если по-русски, количество очков по картам. Тузы, дамы, валеты и короли - 10 очков
    туз может быть либо 11, либо 1 очко - функция автоматически это определяет"""
    value = 0
    numberOfAces = 0
    # Сейчас будем добавлять "цену" не-тузам
    for card in cards:
        rank = card[0]  # Не забываем, что карты представлены кортежами (старшинство, масть)
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):  # Карты, которые стоят 10 очков
            value += 10
        else:
            value += int(rank)  # Номерные карты дают очки по своему номиналу

    # Переходим к тузам:
    value += numberOfAces  # Добавляем по одному очку за туза
    for i in range(numberOfAces):
        if value + 10 <= 21:  # Если очков, уже имеющихся у игрока <= 10, то туз - это 11 очков.
                              # В противном случае - 1 очко
            value += 10
    return value





def displayHands(playerHand, dealerHand, showDealerHand):
    '''Показываем карты игрока и крупье. Прячем первую карту крупье, если showDealerHand - False'''
    print()
    if showDealerHand:
        print("Дилер: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("Дилер: ???")
        # Прячем первую крту крупье
        displayCards([BACKSIDE] + dealerHand[1:])
    # Показываем карты игрока
    print("Игрок:", getHandValue(playerHand))
    displayCards(playerHand)


def getMove(playerHand, money):
    # Просим игрока сделать ход( H - hit - "Ешё", S - stand - "Достаточно", D - Double down - "удвоить ставки")
    while True:  # Цикл продолжается, пока игрок не введет корректный ход
        moves = ["(H)it", "(S)tand"]  # Определим, какие ходы может сделать игрок
        """На первом ходу игрок так же может удвоить ставки 
        (если у игрока две карты и достаточно денег)"""
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")
            # Побуждаем игрока сходить
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == ("D") and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()