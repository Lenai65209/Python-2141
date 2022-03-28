class OwnError(Exception):
    pass


try:
    divisible = float(input("Введите делимое: "))
except ValueError:
    divisible = None
    print("Введены некорректные данные.")
except Exceptionas as err:
    print(err)
try:
    divisor = float(input("Введите делитель: "))
except ValueError:
    divisor = None
    print("Введены некорректные данные.")
except OwnError as err:
    print(err)

else:
    try:
        if divisor == 0:
            raise OwnError("Вы пытаетесь делить на 0!")
        result = divisible / divisor
    except (TypeError, OwnError) as err:
        print(f"{err}. Деление не осуществлено.")
    except Exceptionas as err:
        print(err)
    else:
        print(f"Деление прошло успешно: {divisible} / {divisor} = {result}")
