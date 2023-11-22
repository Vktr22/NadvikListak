"""generálj 5 véletlen számot [10,35) között"""

import random
def veletlen():
    list =[]   #a listában mindig azonos típusú adatok legyenek
    i:int = 0
    while i<5:
        szam = random.random()*(35-10)+10
        list.append(szam) # a lista végéhez fűzöm az aktuális elemet
       # list[i] = szam         --> u.a. mint a felette lévő sor
        #print(szam) -- igy irna ki az osszeset lista nelkul, ha az elott iratom ki, mielott az i-t megnovelnem
        i+=1
    return list
listam=veletlen()

"""írjuk ki egymás alá a lista elemeit"""
def lista_kiir(lista):
    for i in range(0,len(lista),1):
        print(f"A lista {i}. eleme: {lista[i]}")

def lista_kiir(lista):
    n:int =0
    while n < len(lista):
        print(f"A lista {n}. eleme: {lista[n]}")
        n += 1

lista_kiir(listam)

"""
---Lista---
indexekkel tudunk az elemeire hivatkozni,
legelső elem indexe a 0,
az utolsó elem indexe len(list-1)( a lista hossza-1)
pythonban az append függvénnyel adunk hozzá egy elemet, mely a lista végére teszi be azt"""

