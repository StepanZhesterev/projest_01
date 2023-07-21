# -*- coding: utf-8 -*-
"""complete_task_2_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bUgP55gBqrFhyuWd1-O5kTeq62avGgZo
"""

# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
s="Hi! Hello! !Have a good day!"
def remove_exclamation_marks(s):
  ss=s.split('!')
  return ''.join(ss)
print(remove_exclamation_marks(s))

# Пункт B.
# Удалите восклицательный знак из конца строки.
s= "Hi! Hello!!"
def remove_last_em(s):
  i,j, = 0, len(s)
  while i <j and s[-1] =="!":
    s=s[:-1]
    i+=1
    return s
print(remove_last_em(s))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
 pass