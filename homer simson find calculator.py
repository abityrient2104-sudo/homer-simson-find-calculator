import time

print('hey im homer simson and i have calculator')
time.sleep(2)
print('so now enter your name')

name = input()
print('hello', name)
time.sleep(1)
try:
    print(' so what number i need to enter?')
    num1 = int(input())

    print('very good :D')
    time.sleep(1)
    print('so what number 2 i need to enter?')
    num2 = int(input())

except ValueError:
    print('ERROR!!! YOU TYPED LETTERS INSTEAD OF NUMBERS 😡')
    time.sleep(2)
    print('stupid calculator try again')
    exit()

print('what do you want?')
time.sleep(1)
print('+  -  /  *')
symbol = input()

if symbol == '+':
    result = num1 + num2
elif symbol == '-':
    result = num1 - num2
elif symbol == '/':
    if num2 == 0:
        print('ERROR: division by zero 🤯')
        exit()
    result = num1 / num2
elif symbol == '*':
    result = num1 * num2
else:
    print('UNKNOWN SYMBOL 😤')
    exit()

print('RESULT:', result)
time.sleep(0.5)
print('yuhu 🎉')
