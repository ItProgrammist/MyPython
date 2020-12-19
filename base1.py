
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


# n = int(input("Введите год: "))
# if (n >= 0):
#     if(n%4 == 0 or n%400 == 0) and (n%100 != 0):
#         print("YES")
#     else:
#         print("NO")
# else:
#     print("Что за год такой?")

# A = int(input("Enter A: "))
# B = int(input("Entr B: "))

# if A <= B:
#     for i in range(A,B+1,2):
#         print(A," ")
#         A-=-2
# if A>=B:
#     for i in range(A,B-2,-2):
#         print(A," ")
#         A-=2

# n = int(input("Enter n: "))
# count = "1"
# if(n <= 9):
#     for i in range(1,n+1):
#         print(count)
#         count = count+str(i+1)
# else:
#     print("n больше 9")


n = int(input("Enter n: "))
count = " "
count = count*(n-1)
count_2 = "*"

if(n <= 9):
    for i in range(1,n+1):
        print(count,count_2)
        count = count*(n-(i+1))
        count_2 = count_2*(i+1)
else:
    print("n больше 9")
