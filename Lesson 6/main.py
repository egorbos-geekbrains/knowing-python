# Задача № 1
def magic_calc(number: int, step: int = 3):
    if step == 1: return number * 3
    else:
        multiplier = 10
        while (number / multiplier) >= 1:
            multiplier *= 10
        temp = 0
        for i in range(1, step):
            temp += number * pow(multiplier, i)
        return temp + magic_calc(number, step - 1)
    
print("Задача № 1")
number = input("Введите число: ")
print(f"{number} + {number*2} + {number*3} = {magic_calc(int(number))}")