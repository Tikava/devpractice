import math_operations
import text_utility
import student

print(math_operations.add(1, 2))
print(math_operations.subtract(1, 2))
print(math_operations.divide(1, 2))
print(math_operations.multiply(2, 3))

text = 'Hello! I am Toilybay! I am 18. Learning Python with devPractice. Thank you!'
print(text_utility.total_words_count(text))
print(text_utility.word_count('!', text))

student = student.Student('Almat', 18)
print(student.get_info())

