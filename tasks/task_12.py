print ("Если вы хотите перевести килобайты в байты введите - 1")
print ("Если вы хотите перевести байты в килобайты введите - 2")
print ("Что вы хотите сделать ?")
a = int(input())
if a != 1 and a != 2:
    print("Вы ввели неправильное значени, перезапустите программу")
    exit()


n = int(input("Введите число = "))
def kilo(n):
    return n // 1024
    


def bat(n):
    return n * 1024
    

if a == 1:
    ans = kilo(n)
    print (ans)
    

if a == 2:
    anwer = bat(n)
    print (anwer)


