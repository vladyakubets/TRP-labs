import sys
import re
import string

def print_example():
   print("Приклад:\n700;200;0.75;-60;0.25\n180;150;0.75;-50;0.25\n0.8;0.2;0.85;0.15") 

def open_file():
    try:
        return [open("lab2.txt"), 5]
    except FileNotFoundError:
        print("Файлу з необхідними даними не існує. Введіть необхідні дані у файл lab2.txt\nПриклад:")
        print_example()
        exit()


[file, years] = open_file()
lines = []
benefits = []

for line in file:
    if (not (line and not line.isspace()) or len(lines) >= 3): continue

    lines.append(re.split(';', re.sub('\n', '', line)))

if len(lines) != 3: 
    print("Повинно бути три рядка данних!")
    print_example()
    exit()

if len(lines[0]) != 5 or len(lines[1]) != 5 or len(lines[2]) != 4:
    print("невірний формат даних у файлі")
    print_example()
    exit()

print("Вхідні дані:")
A = { 'M1': float(lines[0][0]), 'D1': float(lines[0][1]), 'P1': float(lines[0][2]), 'D2': float(lines[0][3]), 'P2': float(lines[0][4]) }
B = { 'M2': float(lines[1][0]), 'D1': float(lines[1][1]), 'P1': float(lines[1][2]), 'D2': float(lines[1][3]), 'P2': float(lines[1][4]) }
C = { 'P3': float(lines[2][0]), 'P4': float(lines[2][1]), 'P1': float(lines[2][2]), 'P2': float(lines[2][3]) }

print("A:", A)
print("B:", B)
print("C:", C)

print("\nОбрахунок задачі A:")
EVM_A = A['P1'] * A['D1'] * years + A['P2'] * A['D2'] * years - A['M1'];
print("EVM(A) =", A['P1'], '*', A['D1'], '*', years, '+', A['P2'], '*', A['D2'], '*', years, '-', A['M1'], '=', EVM_A)

print("\nОбрахунок задачі B:")
EVM_B = B['P1'] * B['D1'] * years + B['P2'] * B['D2'] * years - B['M2'];
print("EVM(B) =", B['P1'], '*', B['D1'], '*', years, '+', B['P2'], '*', B['D2'], '*', years, '-', B['M2'], '=', EVM_B)

print("\nОбрахунок задачі C:")
EVM_A1 = C['P1'] * A['D1'] * (years - 1) + C['P2'] * A['D2'] * (years - 1) - A['M1']
EVM_B1 = C['P1'] * B['D1'] * (years - 1) + C['P2'] * B['D2'] * (years - 1) - B['M2']
print("EVM(A1) =", C['P1'], '*', A['D1'], '*', years - 1, '+', C['P2'], '*', A['D2'], '*', years - 1, '-', A['M1'], '=', EVM_A1)
print("EVM(B1) =", C['P1'], '*', B['D1'], '*', years - 1, '+', C['P2'], '*', B['D2'], '*', years - 1, '-', B['M2'], '=', EVM_B1)

EVM_MAX = max([EVM_A1, EVM_B1])
print("Найкраще значення: ", EVM_MAX)

EVM_C = (EVM_A1 + EVM_B1) * C['P3']
print("EVM(C) =","(",EVM_A1, '+', EVM_B1,")", '*', C['P3'], '=', EVM_C)

letters = ['A', 'B', 'C']
bestSolution = max([EVM_A, EVM_B, EVM_C])

print("\nНайкраще рішення з усіх варіантів { A:", EVM_A, ',', "B:", EVM_B, ',', "C:", EVM_C, "} - це", letters[[EVM_A, EVM_B, EVM_C].index(bestSolution)], '{', bestSolution, '}')
