import random, time
BAR = chr(9608)

def main():
    pass


def getProgressBar(progress, total, barWidth=40):
    progressBar = ""
    progressBar += "["

    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars
    progressBar += " " * (barWidth - numberOfBars)
    progressBar += "]"

    percentComplete = round(progress / total * 100, 1)
    progressBar += " " + str(percentComplete) + "%"

    progressBar += " " + str(progress) + "/" + str(total)

    return progressBar