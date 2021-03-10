# # def highest_even(li):
# #     a = [10, 2, 3, 4, 8, 11]
# #     print(a.sort())
# highest_even('a')
# Create a new list to storage the even numbers
# Easy to creat a new list and append returned values

def highest_even(conjunto):
    even = []
    for number in conjunto:
        if number % 2 == 0:
            even.append(number)
    return max(even)
# Indentation (Return the result inside of a loop never will go to the next value

print(highest_even([10, 2, 5, 7, 11, 13, 8]))

# print(high_even([10, 2, 3, 4, 8, 11])
# def even_odd(num):
#     return num % 2 == 0
# print(even_odd(50))
# organizar os numeros de forma cresente
# comparar os números
# escolher os 2 ultimos numeros

