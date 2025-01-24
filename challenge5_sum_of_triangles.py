# Python code​​​​​​‌‌​​‌​​​​​‌​‌​​‌‌​​​‌‌​‌‌ below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    if num == 0:
        return 0  # 0^2 = 0
    if num == 1:
        return 1  # 1^2 = 1
    return triangle(num) + triangle(num - 1)


# Second Method

def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    return triangle(num) + triangle(num - 1)