#n = []
#a = int
#sum = 0

#while a != 0:
    #a = int(input("Enter a number: "))
    #n.append(a)
    
#del n[-1]
#cntSum = len(n)
#for i in range (cntSum):
    #sum = sum + n[i]
#print(n)
#print(f"Total is {cntSum}")
#print(f"Sum is {sum}")

#data = []
#while True:
    #x = input()
    #if x == '':
        #break
    
    #data.append(str(x))
#maxx = max(len(data))
#print(data)
#print(maxx)


#data = []
#summ = 0
#i = 1
#while i <= 20:
    #n = int(input("Enter score: "))
    #if n >= 0 and n <= 20:
        #data.append(n)
        #i += 1
        
    #else:
        #print("Score is out of range.")
        
#print("Original list: ")
#print(data)
#while summ <= 10:
    #print(f"{summ:2} {'*' * data.count(summ)}")
    
    #summ += 1
    
    
#scores = []

#for i in range(20):
    #while True:
        #try:
            #score = int(input(f"Enter score: "))
            #if 0 <= score <= 10:
                #scores.append(score)
                #break
            #else:
                #print("Score is out of range.")
                
#print("Original list:")
#print(scores)

#histogram = [0] * 11 
#for score in scores:
    #histogram[score] += 1
    
#for i, frequency in enumerate(histogram):
    #asterisks = '*' * frequency
    #print(f"{i} {asterisks}")
    
    
#def accum_sum(l):    
    #n = []
    #accum = 0
    
    #for i in l:
        #accum += num
        #n.append(accum)
        
    #return n
    
#input_list = []
#a = int
#while a != 0:
    #a = int(input("Enter a number (0 to end): "))
    #if a < 1 or a > 999:
        #print("Number is out of range.")
    #else:
        #input_list.append[a]
#del a[-1]
        
#result = accum_sum(input_list)
    
#print("Original list:")
#print(input_list)
#print("Accumulative Sum:")
    
#for i in result:
    #print(i)
    
#def remove_duplicates(t):
    #data = []
    #for i in t:
        #if i not in data:
            #data.append(i)
            
    #return data
            
#remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4])

#def find_mode(l):
    #data = []
    #for i in range(0, 11):
        #a = 0
        #for c in l:
            #if c == i:
                #a += 1
                
        #data.append(a)
    #for i in range(0, 11):
        #if data[i] == max(data):
            #print(i)
#input_list = []
#i = 0
#while i <= 20:
    #n = int(input("Enter score: "))
    #if n < 0 or n > 10:
        #print("Score is out of range.")
    #else:
        #input_list.append(n)
        #i += 1
        
#print("-----")
#print("Original list:")
#print(input_list)
#print("Mode of scores:")
#find_mode(input_list)

#n = int(input())
#for i in range(1, n+1):
    #s = (n - i) * ' '
    #star = (2 * i - 1) * '*'
    
    #print(f"|{s}{star}{s}|")
    
#def count_guess_in_target(target, guesses):
    #count = 0
    #for ch in target:
        #if ch in guesses:
            #count += 1
    #return count

#target = input()
#length = len(target)
#guesses = []
#while True:
    #word = input()
    #if word == "0":
        #break
    #if word in guesses:
        #continue
    #guesses.append(word)
    
    
#print(f"{count_guess_in_target(target, guesses)}/{length}")

#r = input()
#s = input()
#count = 0

#for ch in r:
    #if ch in s:
        #count += 1
#print(count)
#if count == 0:
    #print("0.00")
#else:
    #print(f"{100 * count / len(r[1:-1]):.2f}")
    
#text = input()
#r = ""
#vowel = "aeiou"
#count = 0
#for ch in range(len(text)):
    #if count > 0:
        #count -= 1
    #else:
        #if text[ch] in vowel and text[ch:ch+3] == text[ch] + "p" + text[ch]:
            #r += text[ch]
            #count += 2
        #else:
            #r += text[ch]
#print(r)

# s = input()
# sub = input()
# new = input()

# print(s.find(sub))
# print(s.count(sub))
# print(s.replace(sub,new))

# n = input()
# new = ''
# vowel = 'aeiou'
# new_word = n.lower()
# for ch in new_word:
#     if ch in vowel:
#         new += ch.upper()
#     else:
#         new += ch

# print(new)

# word = input()
# l = []
# r = ''
# while True:
#     n = input()
#     if n == "0":
#         break
#     l.append(n)
# for ch in word:
#     if ch in l:
#         r += ch
#     else:
#         r += '-'

# print(r)

# word = input()
# new_word = word.split(",")
# r = ''
# for ch in new_word:
#     new_word += f'"{word}",'
        
        
# print(r)

# text = input()
# text = text.title()
# word = ['-', '_', '=', '.', '$']
# for i in word:
#     text = text.replace(i, '')

# if len(text) > 0:
#     print(f'{text[0].lower()}{text[1:]}')

# text = input()
# text2 = text.split(',')
# new_text = []
# for i in text2:
#     word = f'"{i.strip()}"'
#     new_text.append(word)
# print(','.join(new_text))

# text = input()
# word = ['.']
# for i in word:
#     if i in word:
#         text.replace(i ,'_')
# print(text)

# input_list = []
# while True:
#     line = input()
#     if line == '-1':
#         break
#     input.append(line)

# output = []
# sign = False

# for i in input:
#     if '=' in line:
#         if sign:
#             output[-1] = output[-1].strip()
#         output.append(line)
#         sign = True
#     else:
#         if sign:
#             output[-1] += line

# for i in output:
#     print(line)

#input_lines = []
#while True:
    #line = input()
    #if line == '-1':
        #break
    #input_lines.append(line)

#output_lines = []
#equal_sign = False

#for line in input_lines:
    #if '=' in line:
        #if equal_sign:
            #output_lines[-1] = output_lines[-1].strip()
        #output_lines.append(line)
        #equal_sign = True
    #else:
        #if equal_sign:
            #output_lines[-1] += line

#for line in output_lines:
    #print(line)

# l = []
# r = []
# maxx = 0
# while True :
#     text = input()
#     if text == '-1' :
#         break
#     txt = text.split('=', 1)
#     l.append(txt[0].strip())
#     r.append(txt[1].strip())

# maxx = max([len(x) for x in l])
# for i in range(len(l)) :
#     print(f"{l[i]:>{maxx}} = {r[i]}")

# input_lines = []
# while True:
#     line = input()
#     if line == "-1":
#         break
#     input_lines.append(line)

# output_lines = []

# def format_equation(equation):
#     left, right = equation.split("=")
#     formatted_equation = left.strip() + " = " + right.strip()
#     return formatted_equation

# equation = ""
# for line in input_lines:
#     if "=" in line:
#         if equation:
#             formatted_equation = format_equation(equation)
#             output_lines.append(formatted_equation)
#         equation = line
#     else:
#         equation += line

# if equation: 
#     formatted_equation = format_equation(equation)
#     output_lines.append(formatted_equation)

# for line in output_lines:
#     print(line)

#def file_name(name):
    #name = name.replace(' ', '-')
    #word = ['\\', '/', '*', ':', '|', '"', '<', '>']
    #for i in word:
        #name = name.replace(i, '_')
        
    #last_dot = name.rfind('.')
    #if last_dot != -1:
        #name = name[:last_dot] + '_' + name[last_dot + 1:]
        
    #max_name_length = 15
    #max_extension_lenght = 3
    #if len(name) > max_name_length + max_extension_lenght:
        #name = name[:max_name_length + max_extension_length]
        
    #if last_dot == '-1':
        #return name
    
    #if len(name) - last_dot > max_extension_length + 1:
        #name = name[:last_dot + max_extension_length + 1]
        
    #return name

#user_input = input()

#file_name(user_input)

#text = input()
#symbol = ' \/*:|"<>'
#count = text.count('.')
#newtext = ''
#text = text.replace('.', '_', count - 1)
#for i in text :
    #if i in symbol :
        #newtext += '_'
    #else :
        #newtext += i
#if count != 0 :
    #name, file = newtext.split('.')
    #print(f"{name[:15]}.{file[:3]}")
#else :
    #print(newtext[:15])
    
#def format_and_add_one(data):

    #data = data.replace(",", "")
    
    #decimal_count = data.count(".")
    
    #if decimal_count > 1 or not data.replace(".", "").isdigit():
        #return "ERROR"
    
    #if decimal_count == 0:
        #data += ".00"
        
    #if decimal_count == 1:
        #parts = data.split(".")
        #if len(parts[1]) == 1:
            #data += "0"
    
    #result = float(data) + 1
    #return result

#user_input = input()

#result = format_and_add_one(user_input)

#print(result)

#def filter_sort_factors_3_7 (ls):
    #ls1 = []
    #ls2 = []
    
    #for i in ls:
        #if i <= 0:
            #continue
        #if i % 3 == 0 or i % 7 == 0:
            #ls1.append(i)
        #else:
            #ls2.append(i)
            
    #ls1.sort()
    #ls2.sort(reverse=True)
            
    #return [ls1, ls2]

#numbers = []
#while True:
    #n = input()
    #if n == '':
        #break
    #number = float(n)
    #numbers.append(number)
    
#if len(numbers) > 0 :
    #min_number = min(numbers)
    #count_min = numbers.count(min_number)
    #print(min_number)
    #print(count_min)
    
#def namelist(names):
    #names = ' & '.join(names)
    #result = names.replace(' &', ',',names.count('&') - 1)
    #return result

# numbers = []
# while True:
#     n = input()
#     if n == '' :
#         break
#     number = float(n)
#     numbers.append(number)
    
# min_number = min(numbers)
# count_min = numbers.count(min_number)


# n = int(input())

# def calculate_score(cards):
#     score = 0
#     aces = 0

#     for i in cards:
#         if i == 'A':
#             score += 1
#             aces += 1
#         elif i == 'KQL':
#             score += 10
#         else:
#             score += int(cards)

#     while aces >0 and score + 10 <= 21:
#         score += 10
#         aces -= 1

#     return score

# for i in range(n):
#     cards = input().split()

#     score = calculate_score(cards)

#     if score <= 21:
#         print(score)
#     else:
#         print('busted')


# def check_order(ls):
#     if not ls:
#         return 'The list is empty.'
#     increasing = decreasing = random_order = True
#     value = ls[0]
#     for i in ls[1:]:
#         if i < 0 or i > 100:
#             return 'Number is out of range.'
#         if i > value:
#             decreasing = False
#         if i < value:
#             increasing = False
#         if i != value:
#             random_order = False

#         prev_value = i

#     if increasing:
#         return 'The list is in non-decreasing order.' 
#     if decreasing:
#         return 'The list is in non-increasing order.'
#     if random_order:
#         return 'The list is in random order.'
#     return 'The list is in non-increasing and non-decreasing order.'

# scores = []
# while True:
#     score = int(input('Enter a number (-1 to end): '))
#     if score == -1:
#         break
#     scores.append(score)

# print('-----')
# print('Original list:')
# print(scores)

# result = check_order(scores)
# print(result)

# def check_order(l):
#     if not l:
#         return 'The list is empty.'
#     increasing = decreasing = random = True
#     for i in range(1, len(l)):
#         if l[i] > l[i-1]:
#             decreasing = False
#         if l[i] < l[i-1]:
#             increasing = False
#         else:
#             random = False
#     if increasing and decreasing:
#         return 'The list is in non-increasing and non-decreasing order.'
#     elif increasing:
#         return 'The list is in non-decreasing order.'
#     elif decreasing:
#         return 'The list is in non-increasing order.'
#     else:
#         return 'The list is in random order.'

# l = []
# while True:
#     n = int(input('Enter a number (-1 to end): '))
#     if n == -1:
#         break
#     if n < 0 or n > 100:
#         print('Number is out of range.')
#         continue
#     l.append(n)
# print('-----')
# print('Original list:')
# print(l)
# print(check_order(l))

# fibo
# n = int(input())
# ls = [1,1]
# for i in range(3, n) :
#     fibo = ls[-1] + ls[-2]
#     ls.append(fibo)

# def fibonaci(n):
#     ls = [1,1]
#     for i in range(3,n):
#         fibo = ls[-1] + ls[-2]
#     return fibo
# def sum_even_or_odd (n, text):
#     fib_list = fibonaci(n)
#     if text in ('e', 'E'):
#         result = sum(fib_list[i] for i in range(n + 1)if i % 2 == 0)
#     elif text in ('o', 'O'):
#         result = sum(fib_list[i] for i in range(n + 1) if i % 2 == 1)
#     else:
#         return 'ERROR'
#     return result

# n = int(input())
# text = input()

# print(sum_even_or_odd(n, text))

# def calculate_blackjack_score(cards):
#     total = 0
#     num_aces = 0

#     for i in cards:
#         if i.isdigit():
#             total += int(i)
#         elif i in "JQK":
#             total += 10
#         elif i == "A":
#             num_aces += 1
#             total += 11

#     while num_aces > 0 and total > 21:
#         total -= 10
#         num_aces -= 1

#     return total

# def blackjack_bot(cards):
#     score = calculate_blackjack_score(cards)

#     if score <= 16:
#         return score
#     elif score > 21:
#         return "busted"
#     else:
#         return score

# n = int(input())

# results = []
# for i in range(n):
#     cards = input().split()
#     result = blackjack_bot(cards)
#     results.append(result)

# for result in results:
#     print(result)

# n = int(input())
# type = []

# for i in range(n):
#     types = int(input())
#     type.append(types)

# n = int(input())
# type = []

# for i in range(n):
#     types = int(input())
#     type.append(types)

# amount_to_return = int(input())

# num_notes = [0] * n

# for i in range(n):
#     num_notes[i] = amount_to_return // type[i]
#     amount_to_return -= num_notes[i] * type[i]

# for i in range(n):
#     if num_notes[i] > 0:
#         print(f"{type[i]}: {num_notes[i]}")

# m, n = map(int, input().split())
# p = int(input())

# table = [['*' for i in range(n)] for i in range(m)]

# for i in range(p):
#     x, y = map(int, input().split(','))
#     table[y][x] = 'M'

# for ch in range(m):
#     for ch1 in range(n):
#         if table[y][x] != 'M':
#             count = 0
#             for ch3 in [-1,0,1]:
#                 for ch4 in [-1,0,1]:
#                     if x + ch3 >= 0 and x + ch3 < n and y + ch4 >= 0 and y + ch4 < m and table[y + ch4][x + ch3] == 'M':
#                         count += 1
#             if count > 0:
#                 table[y][x] = str(count)

# for row in table:
#     print(''.join(row))

# str = input()
# ls = str.split('.')
# print(ls)

# str = input()
# strlist = str.split('.')
# ls = [int(i) for i in strlist]
# print(ls)

# x1, y1 = map(float, input().split(','))
# x2, y2 = map(float, input().split(','))

# result_x = x1 + x2
# result_y = y1 + y2
# print(f'{result_x},{result_y}')

# data = []
# while True:
#     str = input()
#     if str == '':
#         break
#     data.append(str)

# n = ''
# result = n.join(data)
# print(result)

# def extract_string(text):
#     ls = []
#     current_group = ''
#     is_digit = text[0].isdigit()
#     for i in text:
#         if i.isdigit() == is_digit:
#             current_group += i
#         else:
#             if is_digit:
#                 ls.append(int(current_group))
#             else:
#                 ls.append(current_group)
#             current_group = i
#             is_digit = not is_digit
#     if is_digit:
#         ls.append(int(current_group))
#     else:
#         ls.append(current_group)
#     return ls

# def fibonaci(n):
#     ls = [1,1]
#     for i in range(3,n):
#         fibo = ls[-1] + ls[-2]
#     return fibo

# def main():
#     n = int(input())
#     ch = input().lower()
#     if n < 0:
#         print('ERROR')
#         return
#     if ch == 'e':
#         result = sum(fibonaci[i] for i in range(0, n+1) if i % 2 == 0)
#     elif ch == 'o':
#         result = sum(fibonaci[i] for i in range(0, n + 1) if i % 2 == 1)
#     else:
#         print('ERROR')
#         return
    
#     print(result)

# main()


# def fibonaci(n):
#     if n < 0:
#         return [1]
#     elif n == 0:
#         return [1]
#     elif n == 1:
#         return [1,1]
#     else:
#         fibo = [1,1]
#         for i in range(2, n+1):
#             fibo.append(fibo[i-1] + fibo[i - 2])
#         return fibo
    
# n = int(input())
# ch = input().lower()
# summ = 0
# if n < 0:
#     print('ERROR')
# if ch == 'e':
#     for i in range(0, n+1):
#         if i % 2 == 0:
#             summ += fibonaci(i)
#     print(summ)
# elif ch == 'o':
#     for i in range(0, n+1):
#         if i % 2 == 1:
#             summ += fibonaci(i)
#     print(summ)
# else:
#     print('ERROR')

# def extract_string(text):
#     ls = []
#     current_group = ''
#     is_digit = text[0].isdigit()
#     for i in text:
#         if i.isdigit() == is_digit:
#             current_group += i
#         else:
#             if is_digit:
#                 ls.append(int(current_group))
#             else:
#                 ls.append(current_group)
#             current_group = i
#             is_digit = not is_digit
#     if is_digit:
#         ls.append(int(current_group))
#     else:
#         ls.append(current_group)
#     return ls

# print( extract_string("1 2 3 4 5 I love you.") )

# def count_char(word):
#     char_count = {}
#     for i in word:
#         if i.isalpha():
#             if i in char_count:
#                 char_count[i.lower()] += 1
#             else:
#                 char_count[i.lower()] = 1
#     return char_count

# print(count_char('Hello, Python'))

# def cloth_size(width_list):
#     size = {'S': 0, 'M': 0, 'L': 0}
#     for i in width_list:
#         if i <= 36:
#             size['S']+=1
#         elif 36 < i <= 44:
#             size['M']+=1
#         else:
#             size['L']+=1
#     return size
# print(cloth_size([50,44,40,48]))

# varible = {}
# n = []
# print('Enter varibles and values')
# while True:
#     values = input()
#     if values == '-1':
#         break


# def find_bigrams(txt):
#     ls = []
#     for i in range(len(txt)-1):
#         bigram = txt[i:i+2]
#         if bigram not in ls:
#             ls.append(bigram)

#         ls.sort()
#     return ls
# txt = input().lower()
# for i in find_bigrams(txt):
#     print(i)

# name1 = input()
# name2 = input()
# volwo = ['a','e','i','o','u']
# if name1[1:] in volwo:
#     name1_part = name1[0:2]
# if name2[:2] in volwo:
#     name2_part = name2[:2]

# sumname = name1_part + name2_part
# print(sumname)

# string = input()
# lenght = len(string)

# output = ''
# if lenght % 2 == 0:
#     for i in range(lenght // 2):
#         output += string[i] + string[lenght - i - 1]
# else:
#     middle = lenght // 2
#     for i in range(middle):
#         output += string[i] + string[lenght - i - 1]
#     output += string[middle]

# print(output)

# txt = input()
# num = int(input())

# lenght = len(txt)
# if num > 0:
#     num_str = txt[-num:] + txt[:-num]
# elif num < 0:
#     num = abs(num)
#     num_str = txt[num:] + txt[:num]
# else:
#     num_str = txt

# print(num_str)

# string = input()
# lenght = len(string)
# if lenght %  2 == 0:
#     middle = lenght // 2
#     reverse = string[middle:] + string[:middle]
# else:
#     middle = lenght // 2
#     reverse = string[middle + 1:] + string[middle] + string[:middle]

# print(reverse)

# def reverse(word):
#     lenght = len(word)
#     if lenght % 2 == 0:
#         middle = lenght // 2
#         first_half = word[:middle]
#         second_half = word[middle:]
#         reverse_word = second_half[::-1] + first_half[::-1]
#     else:
#         middle = lenght // 2
#         first_half = word[::middle]
#         second_half = word[middle + 1:]
#         reverse_word = second_half[::-1] + word[middle] + first_half[::-1]
#     return reverse_word

# word = input()
# print(reverse(word))

# max_sum = 0
# current_sum = 0
# sequnce = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     current_sum += n
#     if current_sum > max_sum:
#         max_sum = current_sum
#         sequnce.append(n)
#     elif current_sum < 0:
#         current_sum = 0
#         sequnce = []

# print(max_sum)

# def name(fathername, mothername):
#     father_parts = fathername.split(" ")
#     mother_parts = mothername.split(" ")
#     father_prefix = father_parts[0]
#     father_suffix = father_parts[1][1:]
#     mother_prefix = mother_parts[1][0]
#     mother_suffix = mother_parts[0]
#     hybrid = father_prefix + mother_suffix
#     return hybrid
# fathername = input()
# mothername = input()

# print(name(fathername, mothername))

# def find_major_scale(scale, n):
#     scale = scale.split(',')
#     scale_lenght = len(scale)
#     note_index = (n) % scale_lenght
#     return scale[note_index]

# scale = input()
# n = int(input())
# print(find_major_scale(scale, n))

def number_word(number):
    if number < 0 or number > 999:
        return 'ERROR'
    if number == 0:
        return 'zero'

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if number < 20:
        return units[number]
    elif number < 100:
        return tens[number // 10] + ('-' + units[number % 10] if number % 10 > 0 else '')
    else:
        hundred_digit = number // 100
        remainder = number % 100
        result = units[hundred_digit] + ' hundred'
        if remainder > 0:
            result += ' and ' + number_word(result)
        return result

number = int(input())
print(number_word(number))
        

