a=int(input("Введіть номер року "))
if a%4==0 and a%100!=0:
    print("366 днів")
elif a%400==0:
    print("366 днів")
else:
    print("365 днів")