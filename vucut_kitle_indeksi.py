boy = int(input("Boyunuzu Giriniz : "))
kilo = int(input("Kilonuzu Giriniz : "))
vki = kilo / ((boy/100)**2)

print("Vücut Kitle İndeksiniz {}".format(round(vki,2)))
print("Durumunuz : \n")

if vki <=18.5:
    print("Zayif")
    print("{} kilogram almanız gerekiyor".format(round(18.5*((boy/100)**2)-kilo,2)))
elif vki <=24.9:
    print("\t\tNormal")
elif vki<=29.9:
    print("Fazla kilolu")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo-24.9*((boy / 100) ** 2)),2))
elif vki<=39.9:
    print("Obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
else:
    print("Aşırı obez")
    print("{} kilogram vermeniz gerekiyor".format(round(kilo - 24.9 * ((boy / 100) ** 2)), 2))
    
