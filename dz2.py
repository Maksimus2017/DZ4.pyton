number_n = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = number_n
while i <= number_n:
    if number_n % i == 0:
        lst.append(i)
        number_n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")