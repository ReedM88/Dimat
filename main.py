import sys
from functools import lru_cache
from collections import Counter
import math

def euklideszi(a, b):
    if a%b == 0:
        return b
    if b == 1:
        return 1
    if b == a:
        return a
    global lnkos
    if b < 0:
        b *= -1
    if a - (a // b) * b != 0:
        lnkos = a - (a // b) * b
    if a - (a // b) * b != 0:
        return euklideszi(b, a - (a // b) * b)
    else:
        return lnkos


def dimatelso(a, valaszto, b):
    lnko = euklideszi(a, b)
    if valaszto == "szam|x":
        return f"Az lkkt {a // lnko}"
    elif valaszto == "x|x":
        return f"Az lkkt {a * b // lnko}"
    elif valaszto == "x|szam":
        lista = []
        for i in range(1, lnko):
            if lnko % i == 0:
                i = str("osztói ±" + str(i))
                lista.append(i)
        return lista


def legkisebb(szam):
    for p in range(2, szam):
        if szam % p == 0:
            break
        else:
            return f"A legkisebb olyan szám, aminek pontosan {szam} db pozitív osztója van: {pow(2, szam)}"
    osztoszam = 0
    for i in range(szam, sys.maxsize):
        if osztoszam == szam:
            return f"A legkisebb olyan szám, aminek pontosan {szam} db pozitív osztója van: {i - 1}"
        else:
            osztoszam = 0
        for j in range(1, 99999):
            if i % j == 0:
                osztoszam += 1


def kongurencia(a, b, mod):
    lnko = euklideszi(a, b)
    uja = a // lnko
    ujb = b // lnko
    modoszto = euklideszi(mod, lnko)
    ujmod = mod // modoszto
    if uja != 1:
        print(f"{uja} ez a x {ujb} ez a nem x")
        if euklideszi(uja, ujb) == 1:
            if ujb % uja == 0:
                ujb = ujb // uja
                uja = uja // uja
                print(f"{uja} x  , {ujb} y")
            else:
                bmaradek = ujb % ujmod
                while ujb % ujmod != bmaradek or ujb % uja != 0:
                    print(uja,ujb)
                    ujb += 1
                    
            ujmod = ujmod // euklideszi(ujmod,euklideszi(uja,ujb))
            ujb = ujb // uja
            uja = uja // uja
            return f"Az x ≡ {ujb} mod({ujmod})"
        else:
            return kongurencia(uja,ujb,ujmod)
    else:
        return f"Az x ≡ {ujb} mod({ujmod})"


def euler(szam):
    szamlalo = 0
    for i in range(1,szam+1,1):
        temp = euklideszi(i,szam)
        if temp != 1:
            szamlalo = szamlalo+1
    return f"{szam-szamlalo}"



def euler_reversed(szam):
    szamok = list()
    szamlalo = 0
    for i in range(1,10000):
        szamlalo = 0
        for l in range(1,i+1):
            if euklideszi(i,l) == 1:
                szamlalo = szamlalo+1
                print(f"Aktuális elem {i} másik elem: {l}")
                if szamlalo > szam:
                    break
            else:
                pass
        if szamlalo == szam:
            szamok.append(i)
    return szamok



@lru_cache(maxsize=2000)
def primtenyezos(szam):
    db = 0
    primtenyezok = list()
    vegleges = list()
    i = 2
    while i<szam+1:
        if szam%i == 0:
            primtenyezok.append(i)
            szam = szam // i
        else:
            i = i+1
    return primtenyezok

def hatvanymaradek(alap,kitevo,mod):
    relativ_prim = math.gcd(alap,mod)
    if relativ_prim == 1:
        uj_kitevo = int(euler(mod))
        kitevo_felbontas = kitevo%uj_kitevo
        if -5<=kitevo_felbontas<=5:
            return kongurencia(int(math.pow(alap,kitevo_felbontas)),relativ_prim,mod)
        else:
            while -5<=kitevo_felbontas>=5:
                kitevo_felbontas -= uj_kitevo
        if kitevo_felbontas <= 0:
            uj_alap = int(math.pow(alap,kitevo_felbontas*(-1)))
        return kongurencia(uj_alap,relativ_prim,mod)
    else:
        return 'Not exist solution.'



def solver(alap,kitevo,mod):
    if (alap % mod < alap):
        if (euklideszi(alap%mod,mod) == 1):
            fi = euler(mod)
            ujkitevo = kitevo % int(fi)
            if (int(ujkitevo) >= alap):
                ujkitevo2 = ujkitevo-fi
                result = pow(alap, ujkitevo2) % mod
                print(f"{alap% mod}^{ujkitevo2} --> {result} mod ({mod})")
            else:
                result = pow(alap,ujkitevo)%mod
                print(f"{alap % mod}^{ujkitevo} --> {result} mod ({mod})")
    else:
        if (euklideszi(alap%mod,mod) == 1):
            fi = euler(mod)
            ujkitevo = kitevo % int(fi)
            if (int(ujkitevo) >= alap):
                ujkitevo2 = int(ujkitevo)-int(fi)
                result = kongurencia(pow(alap,(int(ujkitevo2)*-1)),1,mod)
                print(f"{alap}^{ujkitevo2} --> {result}")
            else:
                result = pow(alap,ujkitevo)%mod
                print(f"{alap}^{ujkitevo} --> {result} mod ({mod})")