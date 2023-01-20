#sample inputs
roman_numeral = 'MMMCCCXCIX'
roman_numeral_1 = 'DCXLV'

def romanToInt(s):
     
        s = s.upper()
        length = len(s)
        validated = []
        roman_value = 0
        roman_numeral_digits = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        for i, digit in enumerate(s):
            if i not in validated:
                digit_value = roman_numeral_digits[digit]
                if not(i == length - 1):
                    next_digit = s[i+1]
                    next_digit_value = roman_numeral_digits[next_digit]
    
                    if digit_value < next_digit_value:
                        resolved_value = next_digit_value - digit_value
                        roman_value += resolved_value
                        validated.append(i+1)
                        continue
                roman_value += digit_value
                validated.append(i)

        return roman_value


print(romanToInt(roman_numeral))
