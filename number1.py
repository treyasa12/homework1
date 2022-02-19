# Задание 1
name = 'Александра'
print(name)

# Задание 2
age = '19 лет'
print("Меня зовут", name, "\nМне", age)

# Задание 3
print(name + name + name + name + name)

name_five = name * 5
print(name_five)

# Задание 4  + Задание 9
name_user = input("Как тебя зовут? ")
if name_user == str:
    print("Привет,", name_user)
else:
    print("Ошибка: при указании имени используются только буквы")
age_user = input("Сколько тебе лет? ")
if age_user == int:
    print("В любом возрасте есть своя прелесть...")
else:
    print("Ошибка: при указании возраста используются только цифры")

# Задание 5
number = int(input("Скажи еще раз, сколько тебе лет? "))
if number > 18:
    print("Например, во взрослой жизни есть такие увлекательные вещи, как неоплаченные счета, работа, недосып:)")
else:
    print("Например, твоей самой большой проблемой является несделанное дз:)")

# Задание 6
text = name_user[::-1]
print(text)
a = name_user[0:5]
print(a)
b = name_user[1:-1]
print(b)
x = name_user[-3::]
print(x)

# Задание 7
print(len(name_user))
s = 0
m = 1
while number > 0:
    n = number % 10
    s = s + n
    m = m * n
    number = number // 10
print("Сумма:", s)
print("Произведение:", m)

# Задание 8
s1 = name_user
s2 = s1.upper()
print(s2)

s2 = s1.lower()
print(s2)

s2 = s1.capitalize()
print(s2)

s2 = s1.swapcase()
print(s2)

# Задание 10
x = input("Сколько будет 2*2+2? ")
s = 2 * 2 + 2
if x == s:
    print("Молодец!")
else:
    print("С математикой у тебя плоховато")
