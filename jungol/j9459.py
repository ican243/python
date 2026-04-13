def person(sex, age):
    sex = sex.upper()


    if age >= 20:
        if sex == 'M':
            return "MAN"
        else:
            return "WOMAN"

    else:
        if sex == 'M':
            return 'BOY'
        else:
            return "GIRL"

a, b = input().split()

c = int(b)
result = person(a, c)
print(result)