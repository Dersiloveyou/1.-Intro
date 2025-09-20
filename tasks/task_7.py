print ("First task:")
b = float(input("Введите радиус окружности = "))
b = b * 2
print ("Диаметр окружности = ",b)

print ("Second task")
res = []
for i in range (100,501):
    res.append (i)
print ("Сумма всех целых чисел от 100 до 500 - ",sum(res))


print ("Third task")
agit = []
a = int(input("Введите число а (в промежутке от введенного вами числа до 500) = "))
for i in range (a,501):
    agit.append(i)

print ("Сумма всех целых чисел от введенного вами числа до 500 = ",sum(agit))
    

