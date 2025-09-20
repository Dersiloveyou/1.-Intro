kilo = int(input("Колво километров = "))
metr = int(input("Колво метров = "))
kilom = kilo * 1000

if kilom < metr:
    print ("Наименьшее", kilo)
else:
    print ("Наименьшее",metr)
