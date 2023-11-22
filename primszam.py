def prim1(x:int):
    if x <= 1:
        print("Nem prím szám.")
    elif x == 2:
        print("A 2 prím szám.")
    else:
        oszto_db = 0
        for i in range(2,x-1,1):
            if (x % i == 0):
                oszto_db += 1

        if oszto_db == 0:
            print(f"{x} prím")
        else:
            print(F"{x} nem prím")

def prim2(x:int):
    #optimalizáljuk a lépésszámra
    if x <= 1:
        print("Nem prím szám.")
    elif x == 2:
        print("A 2 prím szám.")
    else:
        i:int = 2
        while i<=x**(1/2) and not (x % i == 0):
            i+=1

"""     if i > x**(1/2):
            print(f"{x} prím")
        else:
            print(F"{x} nem prím")"""
    if i <= x**(1/2):
        print(f"{x} nem prím")
    else:
        print(f"{x} prím szám")