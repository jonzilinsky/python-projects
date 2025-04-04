if True:
    print("True")

if False:
    print("False")

if not False:
    print("not False")

if 1 < 1:
    print("1 < 1 ")
elif 1 <= 1:
    print("1 <= 1")
    print("here")
else:
    print("else 1")

if 1 < 1:
    print("1 < 1")
elif 1 <= 1:
    print("1 <= 1")
elif 2 <= 2:
    print("2 <= 2 ")
else:
    print("else reached")

if 1 > 0 and 0 < 1:
    print("1 > 0 and 0 < 1")

if 1 < 0 and 0 > 1:
    print("1 < 0 and 0 < 1")

if (1 < 0 or 0 < 1) and 1 == 1:
    print("1 < 0 or 0 < 1")

if 0 < 1: print("0 < 1")
print("1 >= 1") if 1 >= 1 else print("1 < 1") #ternary
#same as:
if 1 >= 1:
    print("1 >= 1")
else:
    print("1 < 1")

if 0 > 1:
    print("1")
elif 0 < 1:
    print("2")
else:
    print("3")
#same as:
print("1") if 0 > 1 else print("2") if 0 < 1 else print("3")

