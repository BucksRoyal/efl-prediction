def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None


print(division(12, 2))  # 6.0
print(division(12, 0))  # None
