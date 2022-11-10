import os
import sys, time

try:
    import bext
except ImportError:
    print("Модуль bext нужно заранее установить")
    print("Как это сделать, читай на")
    print("https://pypi.org/project/Bext/")
    sys.exit()

print("Запускаем радугу!")
print("Нажмите: CTRL-C для выхода")
time.sleep(3)

indent = 0
indentIncreasing = True

try:
    while True:
        print(" " * indent, end="")
        bext.fg("red")
        print("##", end="")
        bext.fg("yellow")
        print("##", end="")
        bext.fg("green")
        print("##", end="")
        bext.fg("blue")
        print("##", end="")
        bext.fg("cyan")
        print("##", end="")
        bext.fg("purple")
        print("##")

        if indentIncreasing:
            indent += 1
            if indent == 60:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

        time.sleep(0.03)

except KeyboardInterrupt:

    sys.exit()
