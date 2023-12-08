print('Hi', 'Mike', sep=',', end='.\n')
print('Hi', 'Mike', sep=',', end='.\n')

print(2 + 2)
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

print("i don't know")
print('i dom\'t know')
print('say "i don\'t know"')
print("say \"I don't know\"")
print('Hello \nHow are you')

print(r'C:\name\name')

print("""
line1
line2
line3
""")

print('Hi' * 3)
print('###################')

s = ('aaaaaaaaaaaaaaa'
     'BBBBBBBBBBBBBBB')
print(s)

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[:2])
print(word[2:])
word = 'j' + word[1:]
print(word[0:2])
print(word[:])
n = len(word)
print(n)

s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f's is {x}, {y}, {z}')
print(f's is {z}, {y}, {x}')

name = 'Ryuta'
family = 'Kumagai'
print(f'My name is {name} {family}. Watashi ha {family} {name}')

r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
     print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ' #### '.join(to_split)
print(x)

i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('x =', x)
print('y =', y)
