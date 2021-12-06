import sys
import re
import string

def open_file():
    try:
        return open("lab4.txt")
    except FileNotFoundError:
        print("Файлу з необхідними даними не існує. Введіть необхідні дані у файл lab4.txt\nПриклад:")
        exit()

file = open_file()
lines = []

for line in file:
    lines.append(re.split(';', re.sub('\n', '', line)))

for line in lines:
    for i in range(0, len(line)):
        line[i] = float(line[i])



print("Вхідні дані:")
print("Koef   A   B   C   D   E")
for line in lines: print("%.2f  %2d  %2d  %2d  %2d  %2d" % (line[0],line[1],line[2],line[3],line[4],line[5]))
print("\nОбчислені параметри в залежності від коефіцієнтів:")
print("Koef    A     B     C     D     E")
sumOfColumns=[0,0,0,0,0]
for line in lines:
    print("%.2f  %1.2f  %1.2f  %1.2f  %1.2f  %1.2f" % (line[0], line[0] * line[1], line[0] * line[2], line[0] * line[3], line[0] * line[4], line[0] * line[5]))
    sumOfColumns[0] += line[0] * line[1]
    sumOfColumns[1] += line[0] * line[2]
    sumOfColumns[2] += line[0] * line[3]
    sumOfColumns[3] += line[0] * line[4]
    sumOfColumns[4] += line[0] * line[5]

print("      %1.2f  %1.2f  %1.2f  %1.2f  %1.2f" % (sumOfColumns[0], sumOfColumns[1], sumOfColumns[2], sumOfColumns[3], sumOfColumns[4]))
print("Найкращий вибір: ", sumOfColumns.index(max(sumOfColumns))+1 , chr(65 + sumOfColumns.index(max(sumOfColumns))))
