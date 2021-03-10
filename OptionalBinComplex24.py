#Complex number is created from real numbers. Python complex number can be created either using direct assignment statement or by using complex () function.
#Complex numbers which are mostly used where we are using two real numbers. For instance, an electric circuit which is defined by voltage(V) and current(C) are used in geometry, scientific calculations and calculus.

c = 3 +6j
print(type(c))
print(c)
c1 = complex(3,6)
print(type(c1))
print(c1)

#However, complex numbers don’t support comparison operators like <, >, <=, => and it will through TypeError message:
# a = c2 <= c2
# print(type(a))

#Binary numbers can returns the binary value
#Int convert to the base we select, binary 0 and 1 
print(bin(5))
print(int('0b101', 2))




