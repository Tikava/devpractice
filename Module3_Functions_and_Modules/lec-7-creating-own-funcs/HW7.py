def isTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

#print(isTriangle(7, 3, 9))

def celciusToFahrenheit(temperature):
    return (temperature * (9/5)) + 32

def fahrenheitToCelcius(temperature):
    return (temperature - 32) / (9/5)

# while True:
#     temperature = int(input())
#     temperatureInFahrenheit = celciusToFahrenheit(temperature)
#     print(temperatureInFahrenheit)
#     print(fahrenheitToCelcius(temperatureInFahrenheit))

def lcm(a, b):
    return abs(a * b) / gcd(a, b)

def gcd(a, b):
    min = minimum(a, b)
    while min > 1:
        if a % min == 0 and b % min == 0:
            return min
        else:
            min -= 1

def minimum(a, b):
    if a > b:
        return b
    return a

# while True:
#     a = int(input())
#     b = int(input())
#     print('GCD: ', gcd(a, b))
#     print('LCM: ', lcm(a, b))

def monthlyPaymentCalculator(totalAmount, percentage, totalMonthCount):
    amountToReturn = totalAmount * ((100 + percentage) / 100)
    return amountToReturn / totalMonthCount

#print(monthlyPaymentCalculator(5000000, 11, 12))

def isPalindromeNumber(number):
    number = str(number)
    if len(number) <= 1:
        return True
    if number[0] == number[len(number) - 1]:
        return isPalindromeNumber(number[1: len(number) - 1])
    return False

# print(isPalindromeNumber(123321))
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

#print(factorial(5))
