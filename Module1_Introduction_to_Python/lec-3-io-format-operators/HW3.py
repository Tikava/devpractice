name = input("Your name: ")
print("Hello! and Welcome " + name)


grade1 = int(input('Enter first grade: '))
grade2 = int(input('Enter second grade: '))
grade3 = int(input('Enter third grade: '))

if grade1 > grade2 and grade1 > grade3:
    print('Your max grade is: ', grade1)
    if grade2 > grade3:
        print('Your medium grade is: ', grade2)
        print('Your lowest grade is: ', grade3)
    else:
        print('Your medium grade is: ', grade3)
        print('Your lowest grade is: ', grade2)
elif grade2 > grade1 and grade2 > grade3:
    print('Your max grade is: ', grade2)
    if grade1 > grade3:
        print('Your medium grade is: ', grade1)
        print('Your lowest grade is: ', grade3)
    else:
        print('Your medium grade is: ', grade3)
        print('Your lowest grade is: ', grade1)
elif grade3 > grade1 and grade3 > grade2:
    print('Your max grade is: ', grade3)
    if grade1 > grade2:
        print('Your medium grade is: ', grade1)
        print('Your lowest grade is: ', grade2)
    else:
        print('Your medium grade is: ', grade2)
        print('Your lowest grade is: ', grade1)



name = input('Enter your name: ')
phone_number = input('Enter your phone number: ')
email = input('Enter your email address: ')
city = input('Enter your city: ')
print('------------------------')
print('|name: ', name)
print('|phone number: ', phone_number)
print('|email: ', email)
print('|city: ', city)
print('------------------------')
