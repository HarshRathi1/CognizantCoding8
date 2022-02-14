s=80000
temp=0
ar=4
if s<=0 or ar<1 or ar>5:
    print("Invalid input")
else:
    if ar>=1 and ar<=3:
        temp=s+(s*(10/100))
    elif ar>3 and ar<=4:
        temp = s + (s * (25 / 100))
    elif ar>4 and ar<=5:
        temp = s + (s * (30 / 100))
    print(int(temp))
