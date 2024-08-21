# #mastermind
# target = int(input("Enter a target (4-digit integer): "))
# guess = int(input("Enter your guess (4-digit integer): "))

# positions = 0
# digits = 0

# if target == guess:
#     print("Congratulations, you just mastered my mind!!")
# else:
#     i = 3
    
#     while i >= 0:
#         j = 3
#         target_digit = (target // 10 ** i) % 10
        
#         while j >= 0:
#             guess_digit = (guess // 10 ** j) % 10
            
#             if target_digit == guess_digit:
#                 if i == j:
#                     positions += 1
#                 else:
#                     digits += 1
            
#             j -= 1
        
#         i -= 1
    
#     if positions == 0:
#         positions = "No positions correct"
#     elif positions == 1:
#         positions = "One position correct"
#     elif positions == 2:
#         positions = "Two positions correct"
#     elif positions == 3:
#         positions = "Three positions correct"
#     elif positions == 4:
#         positions = "Four positions correct"

#     if digits == 0:
#         digits = "no digits correct"
#     elif digits == 1:
#         digits = "one digit correct"
#     elif digits == 2:
#         digits = "two digits correct"
#     elif digits == 3:
#         digits = "three digits correct"
#     elif digits == 4:
#         digits = "four digits correct"
    
#     print(positions, digits, sep=", ")



# #กฎของเก้า
number = int(input())

sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

if sum % 9 == 0:
    print("Yes", sum)
else:
    remainder = sum % 9
    print("No", remainder)


# #ถอดรหัสเด็กงี่เง่า
text = input()
vowels = 'aeiou'
decoded_text = ''
i = 0
while i < len(text):
    if text[i] in vowels:
        decoded_text += text[i]
        i += 3
    else:
        decoded_text += text[i]
        i += 1

print(decoded_text)


# h = int(input("Enter height: "))
# w = int(input("Enter width: "))

# if h <= 0 or w <= 0:
#     print("Invalid input, program terminates.")
# else:
#     stars = ' *' * (w // 2)
#     spaces = '* ' * (w // 2)
#     i = 0
#     while i < h:
#         if i % 2 == 0:
#             print(stars)
#         else:
#             print(spaces)
#         i += 1

# n = int(input("Enter positive integer: "))

# if n <= 1:
#     print("Invalid number.")
# else:
#     divisor = 2
#     while n > 1:
#         if n % divisor == 0:
#             print(divisor)
#             n //= divisor
#         else:
#             divisor += 1

# c = int(input())
# a = 0
# pair = 0

# while a < c:
#     a += 1
#     b = a
    
#     while b < c:
#         b += 1
        
#         if (a**2) + (b**2) == c**2:
#             pair += 1

# print(pair)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

a, b = n1, n2
while b:
    a, b = b, a % b
gcd_result = a

lcm_result = n1 * n2 // gcd_result

print(f'  >> gcd({n1}, {n2}) = {gcd_result:>6}')
print(f'  >> lcm({n1}, {n2}) = {lcm_result:>6}')
