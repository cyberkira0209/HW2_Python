a=int(input("Введіть переше число "))
b=int(input("Введіть друге число "))
c=int(input("Введіть третє число "))
if a<b and a>c:
    print(a)
elif a>b and a<c:
    print(a)
elif b<a and b>c:
    print(b)
elif b>a and b<c:
    print(b)
elif c>a and c<b:
    print(c)
else:
    print(c)
