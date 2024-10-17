#задача 1
def task_1(a: int, b: float, c: str, d: list, e: bool) -> str:
    return f"{a} относится к типу {type(a)},\n" \
           f"{b} относится к типу {type(b)},\n" \
           f"{c} относится к типу {type(c)},\n" \
           f"{d} относится к типу {type(d)},\n" \
           f"{e} относится к типу {type(e)}"

print(task_1(25, 34.001, 'box', [1, 2, 3], 5 == 6))

#задача 2
def task_2(a: list):
    return a[0:3]

print('Первые три числа последовательности Фибоначчи', task_2([1, 2, 3, 5, 8, 13, 21]))

#задача 3

def task_3(a: float) -> float:
    return(f"Квадрат {a} равен {a ** 2}")

print(task_3(1.5))