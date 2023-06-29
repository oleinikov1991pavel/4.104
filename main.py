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
import random
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

#1 Явлется ли число палиндропом
#
# number1 = int(input('Первое число\n'))
# number2 = int(input('Второе число\n'))
#
# def f(number1):
#     number1 = str(number1)
#     return number1 == number2[::-1]

# text = input()
# def is_balanced(text):
#     text = "".join(el for el in text if el in "〈({[]})〉")
#
#     while text:
#         flag = True
#         for el in "〈〉", "()", "{}", "[]":
#             if el in text:
#                 text = text.replace(el, "")
#                 flag = False
#         if flag:
#             return False
#     return True
# print(text)


# s = list(input())
# st = []
# for i in range(len(s)):
#     if s[i] == '(' or s[i] == '{' or s[i] == '[':
#         st.append(s[i])
#         continue
#     if (s[i] == ')' or s[i] == '}' or s[i] == ']') and st:
#         if (st[-1]+s[i] == '()') or (st[-1]+s[i] == '{}') or (st[-1]+s[i] == '[]'):
#             st.pop()
#         else:
#             print('нет')
#             exit()
#     else:
#         print('нет')
#         exit()
# if st == []:
#     print('да')
# else:
#     print('нет')


# someString = 'Hello World from Belajar Python'
# someList = someString.split('')

# someString = '(())(())((((()))()))())'
#
# cntOne = someString.count('(')
# cntTwo = someString.count(')')
#
# print(cntOne == cntTwo)


####### Задача про колличество скобок в строке
# someString = '(())(())((((()))()))())'
# cnt = 0
# isTrue = True
#
# for char in someString:
#     if char == '(':
#         cnt += 1
#     elif char == ')':
#         cnt -= 1
#
# if cnt != 0:
#     isTrue = False
#
#     print(isTrue)


########################################ЗАДАЧИ#####################################################
#ГСЧ Генератор случайных чисел
#
# import random
#
# number = random.randint(1, 10)
# print(number)

# 11.29b

import random

# someList = []
# lenList = 8
#
# for i in range(lenList):
#     result = someList.append(i ** 2)
#     summ = sum(resulte)
#     if result > 9999:
#         print(summ)


# number = 1011121314151617181920212223242526272829303132333435363738394041424344454647484950
#
# k = 15

#2.43


# a = int(input('Первое число\n'))
# b = int(input('Второе число\n'))
#
# if (a % b or b % a) == 0:
#     print('1')
# else:
#     print(a % b or b % a)


# a = int(input())
# b = int(input())
#
# num1 = a % b
# num2 = b % a
# print((num1 * num2) +1)


#5.62

# s = 0
# for i, x in enumerate(class_1, 1):
#     s += x
# print(s / i)
#
# s = 0
# for i, x in enumerate(class_2, 1):
#     s += x
# print(s / i)

#17.7

# list = [12, 15, 13, 17, 18, 19, 35, 36, 58, 45, 47, 88]
# list2 = len(list)
#
# t = []
# for i in range(list2):
#     t.append(list)
# print(sorted(t)[4])

#6.97

# list = [12, 15, 13, 17, 18, 19, 35, 36, 58, 45, 47, 88, 11, 34, 39, 21, 29, 49, 38, 63]
# list2 = len(list)
#
# t = []
# for i in range(len(list)):
#     t.append(list)
# print(sorted(list)[2])


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

# someList = [1, 2, 3, 5, 2, 5, 4, 7]
# isTrue = True
# for index in range(len(someList)):
#     if someList[index] < someList[index -1]:
#         isTrue = False
#         break
#     print(index)


#######################26.06.2023#############################
                # Модульное программирование

# import functions
#
# number1 = 5
# number2 = 10
# result = functions.count_summ_number(number1, number2)
# print(result)

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix1[-1][0])

# lenList = 5
# someList = [''] *lenList
# print(someList)
#
# for index in list(range(lenList)):
#     someList[index] = input()
#
# print(someList)

# import random
#
# lenX = 2
# lenY = 3
# matrix = [[]] * lenX
#
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#     for j in range(lenY):
#         matrix[i][j] = random.randint(1, 9)
#
# for i in range(lenX):
#     print(matrix[i])
########## ДВУМЕРНЫЙ МАССИВ #############
#12.4b
# import random
#
# lenX = int(input('Enter'))
# lenY = int(input('Enter'))
#
# matrix = [[]] * lenX
# for i in range(lenX):
#     matrix[i] = [0] * lenY
#
# for j in range(lenY):
#     matrix[j] = [0] * lenX
#     print(matrix[j])
# print()
# print()
# print()
#
# for i in range(lenX):
#     for j in range(lenY):
#         matrix[i][j] = random.randint(10, 99)
# for i in range(lenX):
#     print(matrix[i])
#
# numberX = int(input())
# numberY = int(input())
#
# print(matrix[numberX][numberY])

#12.35a

import random

lenX = int(input('Enter'))
lenY = int(input('Enter'))

matrix = [[]] * lenX
for i in range(lenX):
    matrix[i] = [0] * lenY

for j in range(lenY):
    matrix[j] = [0] * lenX
    print(matrix[j])
print()
print()
print()

for i in range(lenX):
    for j in range(lenY):
        matrix[i][j] = random.randint(10, 99)
for i in range(lenX):
    print(matrix[i])

summa = 0
cnt = 0
for i in range(lenY):
   if matrix[5][i] % 2 != 0:
       cnt += 1
       summa += matrix[5][i]
       print(summa)

