"""3)	Пользователь вводит текст, состоящий из слов, разделенных пробелами.
В словах, начинающихся на «А» заменить эту букву на «аa». В полученном текст подсчитать
количество слов, начинающихся на «p». Буквы латинские"""
import re

test_string="dsfs Asds das pfdfs pfdsf"

result=re.sub(pattern=r"(A)", repl="aa", string=test_string)
count_word=len(re.findall(pattern=r"\bp\w+", string=test_string))

print(result)
print(count_word)
