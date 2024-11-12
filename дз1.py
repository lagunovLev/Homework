operations = { "+": lambda x, y: x+y, "-": lambda x, y: x-y,
               "/": lambda x, y: x/y, "*": lambda x, y: x*y}
ostalnoe = ""


def calculate(string):
    if string == "":
        return 0
    number1 = 0
    f = string
    if string[0].isdecimal():
        string, number1 = get_number(string)

    if string == "":
        return number1

    if string[0] == "+" or string[0] == "-":
        return operations[string[0]](number1, calculate(string[1:]))

    else:
        r = proisv(f)
        return calculate(str(r) + ostalnoe)


def proisv(string):
    if string == "":
        return 0
    number1 = 0
    f = string
    if string[0].isdecimal():
        string, number1 = get_number(string)

    if string == "":
        return number1

    if string[0] == "*" or string[0] == "/":
        return operations[string[0]](number1, proisv(string[1:]))

    else:
        return number1


def get_number(string):
    if string == "":
        return "", 0
    index = 0
    while index < len(string) and string[index].isdecimal():
        index += 1
    number = int(string[0:index])
    ostalnoe = string[index:]
    return string[index:], number


#print(get_number("375fdfgdg"))

while True:
    #try:
        expression = input("Введите выражение, которое нужно посчитать: ")
        result = calculate(expression)
        print("Результат", result)
    #except:
    #    print("Не удалось посчитать из-за ошибки")


