import numpy as np

def daysElapsed(day, month):
    d = np.array([31,28,31,30,31,30,31,31,30,31,30,31])
    return int(np.sum(d[:month - 1])) + day

day = int(input("Enter day: "))
month = int(input("Enter month: "))
print(daysElapsed(day, month))
