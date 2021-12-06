import numpy as np
import math

def getFile():
    text = []
    with open("data1.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))

        
    for i in range(len(text)):
        text[i] = text[i].split(" ")

    for i in range(0, len(text)):
        for j in range(0, len(text[i])):
            text[i][j] = int(text[i][j])
    return text

def walds_maxmin_model(matrix):
    minOfRows = []
    print(matrix)
    for row in matrix:
        print(row,min(row))
        minOfRows.append(min(row))

    maxValue = max(minOfRows)
    print("Найменший елемент кожного рядка:", minOfRows)
    print("найбільший елемент серед найменших:", maxValue)
    print("Критерій: ",minOfRows.index(maxValue) + 1)

def laplace_criterion(matrix):
    sumOfRows = []
    for row in matrix:
        sumOfRows.append(sum(row)/len(row))
        row_elements = []
        for el in row:
            row_elements.append(el/3)
        print(row_elements)

    maxValue = max(sumOfRows)
    print("Сума поділених значень кожного рядка", sumOfRows)
    print("Максимальний елемент:", maxValue)
    print("Cтратегія", sumOfRows.index(maxValue) + 1)

def hurwitz_criterion(matrix, coefficient):
    minOfRows = []
    maxOfRows = []
    for row in matrix:
        minOfRows.append(min(row))
        maxOfRows.append(max(row))
        result = []
    for i in range(len(minOfRows)):
        result.append(coefficient * minOfRows[i] + (1 - coefficient) * maxOfRows[i])

    print("Coefficient:", coefficient)
    print("Мінімальні елементи кожного рядка:", minOfRows)
    print("Мксимальні елементи кожного рядка:", maxOfRows)
    print("Обраховані значення:", result)
    print("Стратегія: ",result.index(max(result))+1)

def bayes_laplace_criterion(matrix, coefficients):
    result = [0 for x in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i] += coefficients[j]* matrix[i][j]

    print("Коефіцієнти:", coefficients)
    print("Обраховані значення: ", result)
    print("Стратегія: ",result.index(max(result)) + 1)

  
if __name__ == '__main__':
    text = getFile()

    print("\nКритерій Вальда:")
    walds_maxmin_model(text)

    print("\nКритерій Лапласа:")
    laplace_criterion(text)

    print("\nКритерій Гурвіца:")
    hurwitz_criterion(text, 0.5)

    print("\nКритерій Баєса-Лапласа:")
    bayes_laplace_criterion(text,[0.5, 0.35, 0.15])
