"""
1- Metreyi Cmye Çevirin
2- Cmyi Metreye çevirin

"""
secim = input("Seçim Yapınız:")#Kullancıdan seçim yapmasını istedim
sayi1= int(input("Sayıyı giriniz:"))#Kullanıcıdan sayıyı seçmesini istedim

if secim == "1":#seçim 1 e eşitse metreyi santimetreye çevirmesini söledim
    print(sayi1*100)
elif secim =="2":#seçim 2 e eşitse santimetreyi metreye çevirmesini istedim
    print(sayi1/100)
else:#seçim 1 veya 2 dışında bir değişken ise hata vermesini söledim
    print("Lütfen geçerli bir işlem yapınız")


