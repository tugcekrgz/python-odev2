#2.ÖDEV 

ogrenciListesi=["Berra Güven","Azra Özdemir","Furkan Yıldız","Ömer Okumuş"]

yeniOgrenci=input("Lütfen listeye eklemek istediğiniz öğrencinin adını ve soyadını giriniz: ")
ogrenciListesi.append(yeniOgrenci)
print(ogrenciListesi)

cikarilacakOgrenci=input("Lütfen listeden çıkarmak istediğiniz öğrencinin adını ve soyadını giriniz:")
ogrenciListesi.remove(cikarilacakOgrenci)
print(ogrenciListesi)


ogrenciListesi.extend(["İrem Bulut","İlayda Pehlivan","Sena Çiçek"])
print(ogrenciListesi)

for ogrenci in ogrenciListesi:
    print(ogrenci)

for ogrenci in ogrenciListesi:
    print(f"{ogrenci}adli öğrencinin numarası{ogrenciListesi.index(ogrenci)}")    
     

ogrenciSayisi=int(input("Listeden silinecek öğrenci sayısını giriniz: "))
i=0

while i<ogrenciSayisi:
   silinecekOgrenciIsmi=input("Silinecek öğrencinin adını ve soyadını giriniz:")
   ogrenciListesi.remove(silinecekOgrenciIsmi)
   print(f"{silinecekOgrenciIsmi} listeden silinmiştir.")
   print(ogrenciListesi)
   i=i+1



