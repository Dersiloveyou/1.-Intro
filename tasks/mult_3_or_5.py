number = 60

if number <= 0:
    result = 0
else:
    total = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    result = total

print(result)
