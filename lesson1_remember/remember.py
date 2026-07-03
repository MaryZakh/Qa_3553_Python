from pickletools import string4

age = 25
name = 'Ivan'


# int - целые числа
# float - дробные
# str - строки
# bool - логический


said = "She said 'Hello'"
print(said)

my_string = '''This is a multy-line string.
We`ve wrapped the text to the next line'''
print(my_string)

raw_string = r"C:\Program Files\Marii\Python"
print(raw_string)

s1 = "Hello world"
print(type(s1))
s2 = 5
print(type(s2))
s3 = False
print(type(s3))
s4 = 3.8
print(type(s4))
#***********************************
s1 = 'Zeleno'
s2 = 'glazka'
s3 = s1+s2
print(s3)

s1 = 'Zeleno'
s2 = 'glazka'
s3 = s2+s1
print(s3)

#join()
words = ["Hello", "World", "and", "Python"]
result = "---".join(words)
print(result)
#**************************************
st = 'ab' * 7
print(st)

st = 35*'*'
print(st)
#************************************
s1 = 'Moshe Pupkin'
s2 = 'Vasya'

if s2 in s1:
    print('User Vasya is in our database')
else:
    print('User Vasya not in the DB')

st = 'a'
if st=='a' or st=='b' or st=='c' or st=='d':
    print('YES')

if st in 'abcd':
    print('YES')

#****************************
#len()

ln = len('Zelenoglazka')
print(ln)

s1 = 'Zelenoglazka'
print(len(s1))
#*****************************
#P Y T H O N
#0 1 2 3 4 5

st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])
#print(st[6])

# P  Y  T  H  O  N
#-6 -5 -4 -3 -2 -1

#****************************************
#my_string[start:end]
#P Y T H O N
#0 1 2 3 4 5
print(st[0:3])
print(st[2:5])
print(st[4:6])
print(st[:10])
print("*****")

my_string = "Hello World!"
every_second_char = my_string[::2]
print(every_second_char)
from_second = my_string[1::2]
print(from_second)
my_substring = my_string[1:10:3]
print(my_substring)

reversed_string = my_string[::-1]
print(reversed_string)
