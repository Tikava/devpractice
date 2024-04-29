email = 'wavoleniu@gmail.com'
symbolIdx = email.index('@')
name = email[:symbolIdx]
print(name)


eq1 = '5 + 5'
symbol = eq1[2]
a = int(eq1[0])
b = int(eq1[-1])
if symbol == '+':
    print(a + b)
elif symbol == '-':
    print(a - b)
elif symbol == '*':
    print(a * b)
elif symbol == '/':
    print(a / b)
else:
    print("Couln't recognize symbol")
