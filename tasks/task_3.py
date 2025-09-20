number = int(input("Число от 0 до 9 = "))
mass = [0,1,2,3,4,5,6,7,8,9]
for i in mass:
    if number >= 0 and number < 10:
        print(f"{number} * {i} =",number*i)
    else:
        print ("Введите число от 0 до 9!")
        break

        
