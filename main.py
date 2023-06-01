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

someString = 'hello world'
print(someString[0])
print(someString[-1])