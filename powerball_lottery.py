# Цикл while с пользовательским вводом и "защитой от дурака":
# Необходимо, чтобы игрок ввел 5 неповторяющихся чисел в диапазоне от 1 до 69 включительно
import random
jackpot = "$1.586 billion!"

print(f"""Лотерейный билет американской лотереи PowerBall стоит $2. В данной симуляции Джекпот составляет: {jackpot}
 На самом деле, размер Джекпота не важен, ведь шансы на его выигрыш составляют 1 к 292,201,338.
 Данная симуляция дает Вам возможность испытать радость игры без траты денег!""")

while True:
    print("Введите 5 неповторяющихся чисел от 1 до 69 через пробел: ")
    print("(Например: 4 8 15 16 23)")
    response = input("> ")
    # Проверим, что пользователь ввел 5 строк
    numbers = response.split()
    if len(numbers) != 5:
        print("Пожалуйста, введите 5 чисел, разделенных пробелом!")
        continue

    # Преобразуем введенные строки в целые числа:
    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print("Пожалуйста, введите числа. Например: 23 25 62 38 22")
        continue

    # Проверим, что введенные числа находятся в диапазоне между 1 и 69 включительно:
    for i in range(5):
        if not (1 <= numbers[i] <= 69):
            print("Все числа должны быть в пределах от 1 до 69!")
            continue

    # Проверим, что введенные числа уникальны (используем множества):
    if len(set(numbers)) != 5:
        print("Числа не должны повторяться!")
        continue

    break

while True:
    print("Введите одно число-Powerball (от 1 до 26)")
    response = input("> ")

    # Переведем строку в число безопасным образом:
    try:
        powerball = int(response)
    except ValueError:
        print("Пожалуйста, введите число! (Например: 2, 8 или 26")
        continue

    # Проверим, что число находится в диапазоне от 1 до 26 включительно:
    if not (1 <= powerball <= 26):
        print("Числа должны быть в пределах от 1 до 26!")
        continue
    break

# Сколько раз вы хотели бы сыграть?
while True:
    print("Сколько раз Вы хотели бы сыграть? Максимально 1000000 раз!")
    response = input("> ")

    # Проверяем, чтобы пользователь не ввел абракадабру!
    try:
        numPlays = int(response)
    except ValueError:
        print("Пожалуйста, введите число! Например 2000 или 100000")
        continue

    # Проверяем, что число находится в пределах от 1 до 1000000:
    if not (1 <= numPlays <= 1000000):
        print("Количество игр может быть от 1 до 1000000")
        continue
    break

# Запускаем симуляцию!
price = "$" + str(2 * numPlays)
print(f"Цена купленных билетов: ${price}")
print("Не переживайте! Мы уверены, что Вы отыграетесь!")
print("Нажмите ENTER, чтобы продолжить... ")

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
    # Выигрышными номерами будут...
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerball = random.randint(1, 26)

    # Выводим выигрывающие номера:
    print("Выигрывают номера: ", end="")
    allWinningNums = ""
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + " "
    allWinningNums += "и " + str(winningPowerball)
    print(allWinningNums.ljust(21), end="")
    if (set(numbers) == set(winningNumbers)) and powerball == winningPowerball:
        print()
        print("Вы выиграли в PowerBall Lottery! Наши поздравления!")
        print(f"Ваш выигрыш составляет: {jackpot}")
        print("Если бы это случилось в реальной жизни, Вы бы стали миллиардером!")
        break
    else:
        print("Вы проиграли!")

print("Вы потратили на билеты:", price)
print("Спасибо за игру!")

