n = int(input("Введите число: "))
summ = 0

while n > 0:
    x = n % 10
    summ = x + summ
    n = n // 10
    
print(summ)