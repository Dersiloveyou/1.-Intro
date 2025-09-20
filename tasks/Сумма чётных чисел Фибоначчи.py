a = 1
b = 2
total = 0

while a <= 4000000:
    if a % 2 == 0:
        total += a
    temp = a  
    a = b     
    b = temp + b  

print("Сумма чётных чисел Фибоначчи до 4 миллионов --", total)
