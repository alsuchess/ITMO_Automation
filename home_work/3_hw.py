def compare(a, b):
    if a >= b:
        print(a)
    else:
        print(b)

compare(-55.001, -55.002)

def compare_135(a, b):
    if (a == b + 135) or (b == a + 135):
        print('yes')
    else:
        print('no')

compare_135(125, 260)

def season(a):
    if a in range(1, 3) or (a == 12):
        print('зима')
    elif a in range(3, 6):
        print('весна')
    elif a in range(6, 9):
        print('лето')
    elif a in range(9, 12):
        print('осень')
    else:
        print('введите корректное число')

season(11.3)

def three_numbers(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('yes')
    else:
        print('no')

three_numbers(11, 12, 19)


def five_numbers(numbers: list):
    numbers.sort()

    if numbers[0] > 0:
        print(5)
    elif numbers[0] < 0 and numbers[1] > 0:
        print(4)
    elif numbers[1] < 0 and numbers[2] > 0:
        print(3)
    elif numbers[2] < 0 and numbers[3] > 0:
        print(2)
    elif numbers[3] < 0 and numbers[4] > 0:
        print(1)
    else:
        print(0)


five_numbers([-1, -2, -7, -6, -10])

def days_count(a, b):
    if b in range(1, 13) and a >= 0:
        print((a * 12 + b) * 29)
    else:
        print('введите корректные данные')

days_count(1, 6)

