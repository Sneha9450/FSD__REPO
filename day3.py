Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> empty_list=[]
>>> print(empty_list)
[]
>>> 
>>> colors=['red','blue','green']
>>> new color=colors
SyntaxError: invalid syntax
>>> 
>>> colors=['red','blue','green']
>>> new_color=colors
>>> print(colors)
['red', 'blue', 'green']
>>> new_color[0]="black"
>>> print(colors)
['black', 'blue', 'green']
>>> 
>>> 
>>> numbers=[10,20,30,40,50]
>>> numbers.append(99)
>>> print(numbers)
[10, 20, 30, 40, 50, 99]
>>> numbers.extend("end")
>>> print(numbers)
[10, 20, 30, 40, 50, 99, 'e', 'n', 'd']
