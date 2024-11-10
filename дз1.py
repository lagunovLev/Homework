while True:
    try:
        expression = input("Введите выражение, которое нужно посчитать: ")
        result = eval(expression)
        print("Результат", result)
    except:
        print("Не удалось посчитать из-за ошибки")
