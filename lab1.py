mark = int(input())
if 90 <= mark and mark <= 100:
    print("A")
elif 75 <= mark and mark <= 89:
    print("B")
elif 60 <= mark and mark <= 74:
    print("C")
elif 40 <= mark and mark <= 59:
    print("D")
elif 0 <= mark and mark <= 39:
    print("F")
else:
    print("Invalid mark")
