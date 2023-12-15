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

x = 20
y = x
y = 5
print(id(x))
print(id(y))
print(x)
print(y)

x = ['a', 'b']
y = x
print(id(x))
print(id(y))
print(x)
print(y)

num_touple = (10, 20)
print(num_touple)

x, y = num_touple
print(x, y)

x, y = (10, 20)
print(x, y)

min, max = 0, 100
print(min, max)

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)

x= {'a':10}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a':1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)


# l = [
#      ['apple' : 100],
#      ['banana' : 200],
#      ['orange' : 300],
# ] リストの場合は中身を確認するプログラムを書く必要がある

fruits = {
     'apple' : 100,
     'banana' : 200,
     'orange' : 300,
}
# 中身（キー）がわかっていつものであれば{}を使って方が中身の確認が早い

print(fruits['apple'])

# 共通の物を調べる際は集合型を使うと良い
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
# set()でリスト型[]から集合型{}へキャストしている
kind = set(f)
print(kind)

s = 'aaaaaaa' \
     + 'bbbbbbbb'
print(s)

# バックスラッシュで1行が長くなった場合の改行が可能となる
x = 1 + 1 + 1 + 1 + 1 + 1\
     + 1 + 1 + 1
# 基本的には80文字で次の行に行くルールがある
# バックスラッシュ以外でもカッコで囲むやり方もある
print(x)

x = 10

if x < 0:
     print('negative')
elif x == 0:
     print('zero')
elif x == 10:
     print(10)
else:
     print('positive')

a = 5
b = 10

if a > 0:
     print('a is positive')
     if b > 0:
          print('b is positive')

# 論理演算子は基本的にJavaと同じ
# and と　or はそのまま記述

y = [1, 2, 3]
x = 1

if x in y:
     print('in')

if 100 not in y:
          print('not in')

a = 1
b = 2

# 数字での使用は好ましくない
if not a == b:
     print('Not epual')

is_ok = True

if is_ok: # == Trueとあえて比較しなくて良い:
     print('Hello')

if not is_ok:
     print('Good by')

# 値が入っていればTrueを返す
# False,o,o.o,(),{},[],set()はfalseを返す
is_ok = 0
if is_ok:
     print('Hello')
else:
     print('No')

is_ok = 'abcdefg'
if is_ok:
     print('Hello')
else:
     print('No')

# 変数の値を空にする場合
is_empty = None
print(is_empty)
print(type(is_empty))

if is_empty is None:
     print('None!')

#値の判定
print(1 == True)
# オブジェクトの判定
# print(1 is True)

count = 0

while count < 5:
     print(count)
     count += 1

count = 0
while True:
     if count >= 5:
          break

     if count == 2:
          count += 1
          continue

     print(count)
     count += 1

count =0

while count < 5:
     print(count)
     count += 1
else:
     print('Done')
