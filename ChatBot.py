import datetime

print("Ardanın Özel Asistanı")

def banasorusor1(cevap):
    print(cevap)

tarih = datetime.datetime.now()
kullaniciadi = input("Kullanıcı Adı:")
kullanicişifre = input("Şifre:")
if kullaniciadi == "arda" and kullanicişifre == "1234":
       print("Hoşgeldiniz Efendim")

else:
       print("Yanlış Şifre")
       quit()
while True:
       banasorusor = input(("Bana soru sorun efendim:")).lower()
       if banasorusor == ("adın ne senin"):
           banasorusor1("Adım Jarvis")

       elif banasorusor == ("saat kaç"):
           print(f'Şuan saat:{tarih}')

       elif banasorusor == ("nasılsın"):
           banasorusor1("İyiyim")

       elif banasorusor == ("bana espri yaparmısın",):
           banasorusor1("En güzel yemek yapan Ceren hangisidir? :TENCERE")

       elif banasorusor == ("görüşürüz",):
           banasorusor1("Görüşürüz", )

       elif banasorusor == ("nerde yaşıyosun",):
           banasorusor1("Ankara")

       elif banasorusor == ("ben nerde okuyorum",):
           banasorusor1("Gölbaşı Anadolu Lisesinde")

       elif banasorusor == ("gelecekde nerde olacaksın"):
           banasorusor1("Yanında")
       elif banasorusor=="çıkmak istiyorum":
           banasorusor1("Çıkılıyor")
           break
       else:
           banasorusor1("Beni daha buna kodlamadın :")






#Gelişim aşamasında Döngüler Fonksiyonlar ve Makine Öğreninimi ile geri dönecek...
#Arda Gündüz
