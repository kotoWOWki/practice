from datetime import datetime, date, timedelta

now = datetime.now()

print(f"Дата сегодня {now}")
    
while True:
    try:
        a = input("Введите число и определите через сколько дней будет определенная дата. Для выхода введите:：'0':  ")
        a = int(a)
        custom_date = now + timedelta(days=a)
        if a == 0:
            print("Спасибо за использование программы！ТГК: @pytnproject")
            break
        print(f"Через {a} дней будет — {custom_date}")
    except ValueError:
        print(f"'{a}' не является числом！")
    except OverflowError:
        print(f"'{a}'число слишком длинное!")
        