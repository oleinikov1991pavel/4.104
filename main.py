#9.59
# someString = input('Введите строку\n')
# lenString = len(someString)
# index = 0
# cntSymbol = 0
# while index < lenString:
#     if someString[index] == 'o':
#         cntSymbol += 1
#     index += 1
# print(f'Колличество символов "o" в строке: {cntSymbol}')
import shlex

#9.76(b)
# someString = input('Вводим строку\n')
# index = 0
# indexSymbol = 0
# lenString = len(someString)
# while index < lenString:
#     if someString == 'e':
#        indexSymbol = index
#     index += 1
# print(indexSymbol + 1)

########################################################
# Строки
# sym = 'It\'s my house'
# sym1 = 'It\'s my ' + sym
# sym2 =f""""Строка 1
# Строка 3
# {5+6}
# Строка 2 """""
# print()

# print('hi' * 5) - дублирует

# someString = 'hello world'
# print(someString[0])
# print(someString[-1])

# someString = 'Today nice day'
# start = 10
# end = 6
# step = -1
#
# print(someString[start:end:step])

# someString = input('Введите слово\n')
# symbol = input()
# result = someString[:-1] +symbol
# print(result)
################################################################
      #              СПИСКИ

# numbers = [3, 5, 4, 5, 6, 64, 'ergwegr']
# numbers1 = [1, 2, 3]
# result = numbers1 + numbers
# print(result)
# lenList = len(numbers)
# print(lenList)

#1.13
# someList = [37, 0, 50, 46, 34, 46, 0, 13]
# index = int(input('Введите индекс элемента: '))
#
# if index > len(someList):
#     print('индекс выходит за пределы списка')
# else:
#     print(someList[index])


# для вывода с конца списка
# someList = [37, 0, 50, 46, 34, 46, 0, 13]
# print(someList[::-1])

# индекс умножить на 2
# someList = [37, 0, 50, 46, 34, 46, 0, 13]
#
# index = 0
#
# while index < len(someList):
#     someList[index] *= 2
#     index += 1
#
# print(someList)


#11.17(в)

# someList = [37, 0, 50, 46, 34, 46, 0, 13]
#
# index = 0
# firstNumber = someList[0]
#
# while index < len(someList):
#     someList[index] /= firstNumber
#     index += 1
#
# print(someList)


#11.19(a) найти сумму и среднее значение
# someList = [37, 0, 50, 46, 34, 46, 0, 13]
#
# sumNumbers = sum(someList)
# sumNumbers1 = sum(someList) / len(someList)
# print(sumNumbers)
# print(sumNumbers1)


# максимальное и минимальное значение

# someList = [37, 0, 50, 46, 34, 46, 0, 13]

# minNumber = min(someList)
# maxNumber = max(someList)
#
# print(minNumber)
# print(maxNumber)