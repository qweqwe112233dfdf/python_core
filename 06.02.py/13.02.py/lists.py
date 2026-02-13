





#-----------------------------
#str - послідовність символів
#range - генератор послідовності чисел
#type - інформація про інший тип даних

#intType = type(10)
#
#print(intType.__name__)
#print(type(intType))
'''
counter = 0
while counter < 10:
    print(counter)
    counter += 1

for i in range(10):
    print(i)

for symbol in "text":
    print(symbol)
'''
'''
collection = list() #функція - конструктор
collection = []

print(type(collection)) # <class 'list'>

items = [10, 12.3, 'text', True] # погана практика

'''
'''
fruits = ['avocado', 'apple', 'orange', 'lemon', 'pear']

fruits.append('ananas')
print(', '.join(fruits))
fruits.extend(['mandarin', 'grapefruit'])
print(', '.join(fruits))

fruits.insert(4, 'mango')
print(', '.join(fruits))

fruits.pop(5)
print(', '.join(fruits))

fruits.append('lemon')
print(', '.join(fruits))
fruits.remove('lemon')
print(', '.join(fruits))

fruits.clear()
print(fruits)
print(len(fruits))
'''
'''
print('П`ятниця')
print('кафе "Птах"')
'''
'''
# list[start:end:step]



print(fruits[0])
print(fruits[1])
print(fruits[1:2])
print(fruits[:3])
print(fruits[2:])
print(fruits[1:4:2])
print(fruits[::2])

print(fruits[-1])
print(fruits[-1:-3:-2])
print(fruits[::-1])

#print(fruits[100])

#string = 'text'
#string[2] = 'u'

print(fruits)
fruits[1] = 'mango' # apple -> mango
print(fruits)


fruits_count = len(fruits)
print(fruits_count)

counter = 0
while counter < len(fruits):
    print(fruits[counter])
    counter += 1

for fruit in fruits:
    print(fruit)
'''
'''
names = input('введіть список імен через кому: ')
print(type(names))
names = names.split()
print(type(names))
print(names)

names = ', '.join(names)
print(names)
print(type(names))
'''
'''
numbers = [10, 3, -5, 0, 0, 9, -10, -12, 1]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)
'''

fruits = ['apple', 'mango', 'pamelo', 'pineapple', 'apple']
colors = ('red', 'green')

(red, green, blue, pink) = colors
print(red)
print(green)
print(blue)
print(pink)

'''
fruits_tuple = tuple(fruits)
print(fruits_tuple)
print(type(fruits_tuple))
#fruits_tuple.remove('apple')
fruits_tuple[3] = 'kiwi'
print(fruits_tuple)

fruits_tuple = ('kiwi', 'pamelo')
print(fruits_tuple)

list2d = [ 
    [1,2,3], 
    [4,5,6] ]

print(list2d[0])
print(list2d[0][1])

for i in list2d:
    for j in i:
        print(j, end=' ')
    print()
'''
'''
apple_count = fruits.count('apple')
print(apple_count)


apple_index = fruits.index('apple')
print(apple_index)

#banana_index = fruits.index('banana')

print(fruits)
fruits.sort()
print(fruits)

fruits.reverse()

list1 = [2,3,4]
list2 = [5,6,7]

result = list1 + list2
print(result)
'''
