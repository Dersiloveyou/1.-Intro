month = int(input("Введте номер месяца - "))
year = int(input("Введите год - "))

mes = ["0", "31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
if month == 2 and year % 4 == 0 and (year % 400 == 0 or year % 100 !=0):
    print ("29")

else:
    if month == 1:
        print (mes[1])
    elif month == 2:
        print (mes[2])
    elif month == 3:
        print (mes[3])
    elif month == 4:
        print (mes[4])
    elif month == 5:
        print (mes[5])
    elif month == 6:
        print (mes[6])
    elif month == 7:
        print (mes[7])
    elif month == 8:
        print (mes[8])
    elif month == 9:
        print (mes[9])
    elif month == 10:
        print (mes[10])
    elif month ==11:
        print (mes[11])
    elif month == 12:
        print (mes[12])
        
