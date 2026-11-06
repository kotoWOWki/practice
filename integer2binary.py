while True:
    try:
        nums = []
        s = input("Введите целое число (Для выхода введите -1): ")
        n = int(s)
    except ValueError:
        print(f"{s} не является числом. Попробуйте заново!")
        continue 
    if n == -1 or n == 0:
        break
    while n > 0:    
        rem = n % 2
        if rem % 2 == 0:
            nums.append(0)
        else:
            nums.append(1)
        n = n // 2
        
    print(f"Число в двоичном виде: {''.join(map(str, reversed(nums)))}")