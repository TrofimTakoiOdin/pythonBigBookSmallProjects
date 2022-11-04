import random, time
BAR = chr(9608)

def main():
    print("Симуляция шкалы загрузки")
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        bytesDownloaded += random.randint(0, 100)

        barStr = getProgressBar(bytesDownloaded, downloadSize)

        print(barStr, end="", flush=True)

        time.sleep(0.3)

        print("\b" * len(barStr), end="", flush=True)
    print(barStr)


def getProgressBar(progress, total, barWidth=40):
    progressBar = ""  # Наша шкала - строка
    progressBar += "["  # Начало строки

    # Убедимся, что ещё не всё загрузилось
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Вычисляем количество "квадратиков" для шкалы: Количество загр. байтов делим на общее количество байтов, умножаем на ширину шкалы
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars # Добавляем "квадратики" к шкале
    progressBar += " " * (barWidth - numberOfBars)  # Пустое место к шкале тоже необходимо добавить, иначе просто шкала будет расширяться
    progressBar += "]"  # Конец шкалы

    # Вычисляем процент выполнения
    percentComplete = round(progress / total * 100, 1)
    progressBar += " " + str(percentComplete) + "%"  # Добавляем проценты

    progressBar += " " + str(progress) + "/" + str(total)  # Добавляем прогресс/общ кол

    return progressBar


if __name__ == "__main__":
    main()