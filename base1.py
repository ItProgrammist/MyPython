
# n = float(input("Введите кол-во минут: "))
# h = int(n/60)
# n = n % 60
# days = h // 24
# if (days>=1):
#     h = h - 24*days
# print(days,":",h,":",int(n))


# age = (input("Введите возраст: "))
# if age.isdigit():
#     age = int(age)
#     if age >= 18:
#         print("Добро пожаловать в Python!")
#     else:
#         print("Иди учи Scratch!")
# else:
#     age = (input("Введите возраст: "))


n = int(input("Введите год: "))
if (n >= 0):
    if(n%4 == 0 or n%400 == 0) and (n%100 != 0):
        print("YES")
    else:
        print("NO")
else:
    print("Что за год такой?")
