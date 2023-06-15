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


############### 15.06.2023


# numbers = list(map(int, input().split()))
#
# print(numbers)
# numbers.append(12)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.insert(1, 2)
# print(numbers)
# numbers.remove(15)
# print(numbers)


# someString = 'Hello World from main.py'
# someList = someString.split(' ')
# print(someList)


# someList = ['Hello World from main.py']
# someString = '+'.join(someList)
# print(someString)

# someList = ['Hello', 'World', 'from', 'main.py']
#
# for word in someList:
#     print(word)


# someString = 'Hello World from mainpy file'
# someList = someString.split()
# for word in someList:
#     if len(word) > 4:
#         print(word)

# someString = 'Hello World from mainpy file'
# someList = someString.split()
# index = 0
# for word in someList:
#     if len(word) <=4:
#         del someList[index]
#     index += 1
#
# print(someList)


# someString = 'Hello World from mainpy file'
# someList = someString.split()
# result = []
# for word in someList:
#     if len(word) > 4:
#         result.append(word)
# print(result)

#11.73

# somelist = [4, 7, 8, 3, 34, 15]
# resultList1 = []
# resultList2 = []
#
# for item in somelist:
#     if item % 2 == 0:
#         resultList1.append(item)
#     if item % 10 == 5:
#         resultList2.append(item)
# print(resultList1)
# print(resultList2)
# print(len(resultList1))
# print(len(resultList2))

#11.82

# someList = [4, 7, 8, 3, 34, 15]
# result1 = []
#
# for item in someList:
#     if item > 10:
#         result1.append(item)
# print(result1)
# print(sum(result1) / len(result1))

#11.197

# someList = [34, 5, 6, 34, 78, 56, 12, 0, 8]
# print(someList.count(2) != 0)


# someRange = list(range(3, 10, 4))
# print(someRange)

# someList = ['hello', 'world', 'this', 'is', 'a', 'list']
#
# for index in range(len(someList)):
#     print(index, someList[index])


# 0 hello
# 1 world
# 2 this
# 3 is
# 4 a
# 5 list
#
# Process finished with exit code 0

#заменить четное число 0 !!!

# someList = [34, 5, 6, 34, 78, 56, 12, 0, 8]
# for index in range(len(someList)):
#     if someList[index] % 2 == 0:
#         someList[index] = 0
# print(someList)


#11.209

someList = [1, 2, 3, 5, 2, 5, 4, 7]
isTrue = True
for index in range(len(someList)):
    if someList[index] < someList[index -1]:
        isTrue = False
        break
    print(index)