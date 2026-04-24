a, b = map(int,input().split())
if a >= 12:
    now = "PM"
    if a >= 13:
        time = a - 12
    else:
        time = a
else:
    now = "AM"
    time = a
print(f"{time:02d} : {b:02d} {now}")


