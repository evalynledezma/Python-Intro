# number types
product_id = 123
sale_price = 14.99
tip_percentage = 1/5
new_product = 150

print(sale_price + new_product)


# mathematical operatiors
print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(25 % 5)

print('Exponents')
print(100 ** 42)


#order of operations in python
"""
Please -> Parans ()
Excuse -> Exponents **
My -> Multiplication *
Dear -> Division /
Aunt -> Addition +
Sally -> Subtraction -

8 + 2 * 5 - (9 + 2) ** 2
8 + 2 * 5 - 11 ** 2
8 + 2 * 5 - 121
8 + 10 - 121
-103
"""

calculation = 8 + 2 * 5 - (9 + 2) ** 2

print(calculation)


# assignment operators
total = 100

total = total + 10
total += 10
total -= 10
total *= 2
total /= 10
total //= 10
total **= 2
total %= 2

product_two = 120
product_three = 10

total += product_two
total += product_three

print(total)


# decimal vs float
product_cost = 88.40
commission_rate = 0.08
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.4

product_cost = Decimal(88.40)
commission_rate = Decimal(0.08)
qty = 450

product_cost += (commission_rate * product_cost)
print(product_cost * qty) # 42962.40000000000282883716451


# Convert Between the Integer, Float, Decimal and Complex Numeric Data Types
product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(complex(commission_rate))


# Popular Math Functions
loss = -20.25
product_cost = 89.99

print(abs(loss))
print(math.floor(product_cost))
print(math.ceil(product_cost))
print(abs(math.floor(loss)))
print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5, 2))
print(5 ** 2)


# MANUAL EXPONENT FUNCTION
from functools import reduce

def manual_exponent(num,exp):
  computed_list = [num] * exp
  return(reduce(lambda total, element: total * element, computed_list))

print(manual_exponent(2,3))
print(manual_exponent(10,2))

def some_func(total, element):
  return total * element

  [2,2,2]

  some_func(2,2)
  some_func(4,2)
  8

  # or 

  
#  def manual_exponent(num, exp):
#      computed_list = [num] * exp
#      return (reduce(lambda total, element: total * element, computed_list))
#
#
#  print(manual_exponent(2, 3))
#  print(manual_exponent(10, 2))
#  print(manual_exponent(3, 3))
#  print(manual_exponent(10, 5))

def manual_exponent(num, exp):
    counter = exp - 1
    total = num

    while counter > 0:
        total *= num
        counter -= 1

    return total

print(manual_exponent(2, 3))
print(manual_exponent(10, 2))
print(manual_exponent(3, 3))
print(manual_exponent(10, 5))



