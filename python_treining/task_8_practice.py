def alsu_list(a: list, b):
    a.append(b)
    return a

print(alsu_list([1, 'box', '8'], 'test'))

def sum_list(a: list) -> int:
    result = 0
    for elem in a:
        result = result + elem
    return result


print(sum_list([1, 2, 3, 4, 5]))

