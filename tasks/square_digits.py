def square_digits(num):
    string_num = str(num)
    separate = "".join(str(int(digit)**2) for digit in string_num)
    return int(separate)


number = 9119
print(square_digits(number))  
