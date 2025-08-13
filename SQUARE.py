'''
5. Function
Write a function calculate_square(number) that takes a number as an argument and returns its square.
'''
for i in range(5):
    def calculate_square(number):
        return number ** 2


    num = int(input("Enter a number: "))
    print(calculate_square(num))
