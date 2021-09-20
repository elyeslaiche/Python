# This is a sample Python script.
import numpy as np
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def degreToRadian(degre, minutes, seconde):
    degredecimal = degre + (minutes + seconde / 60) / 60
    degreRad = degredecimal * np.pi / 180
    return degreRad


# Press the green button in the gutter to run the script.
print(degreToRadian(180,10,40))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
