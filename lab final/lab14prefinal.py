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


