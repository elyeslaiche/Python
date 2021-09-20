# This is a sample Python script.
import numpy as np
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def degreToRadian(degre, minutes, seconde):
    degredecimal = degre + (minutes + seconde / 60) / 60
    degreRad = degredecimal * np.pi / 180
    return degreRad

def radToDegre(rad):
    degre =(int)(rad * 180 // np.pi)
    min =(int)((rad * 180 / np.pi)* 60) % 60
    seconde =(int)((((rad * 180 / np.pi  )* 60) % 60)* 60)% 60
    return degre,min,seconde

def degtofahr(temperature):
    temperature = (temperature * 9/5)+32
    return temperature
# Press the green button in the gutter to run the script.
print(degreToRadian(180,10,40))
print(radToDegre(0.555))
print(degtofahr(10))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
