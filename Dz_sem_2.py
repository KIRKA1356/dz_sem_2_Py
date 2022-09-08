# # Задача 1

# def sum_of_number():
#     number = list((input("Введите число: ")))
#     for index in range(len(number)):
#         try:
#             number[index] = int(number[index])
#         except ValueError:
#             number[index] = 0
#     sum = 0
#     for i in number:
#         sum = sum + i 
#     print(sum)

# sum_of_number()


# # Задача 2

# def factorial():
#     number = int(input("Введите число, факториал которого хотите узнать: "))
#     list_number = []
#     last_operation = 1
#     for i in range(1, number+1):
#         iteration = last_operation * i
#         last_operation = iteration
#         list_number.append(last_operation)
#     print(list_number)
# factorial()


# # Задача 3

# def polindrom():
#     num = (input("Введите число, полиндром которого хотите узнать:"))
#     while(True):
#         if num == num[::-1]:
#             print(f'{num} является палиндромом вашего числа')
#             break
#         else:  
#             num = int(num) + int(num[::-1])
#             num = str(num)
# polindrom()
        
        
 

# # Задача 4

# import time
# milliseconds = str(round(time.time() * 1000)) 
# milliseconds_2 = int(milliseconds[::-1]) // 100000000000

# number_min = int(input("Введите нижнюю границу предела промежутка: "))
# number_max = int(input("Введите верхнюю границу предела промежутка: "))

# for i in range(1, 10111110):
#     if number_max>=milliseconds_2>=number_min:
#         print(int((milliseconds_2) + i * 0.1))
#         break
#     elif milliseconds_2>number_max: 
#         milliseconds_2 = (milliseconds_2 - 1)
#     elif milliseconds_2<number_min: 
#         milliseconds_2 = (milliseconds_2 + 1)
