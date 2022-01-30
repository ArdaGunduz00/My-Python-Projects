import speedtest

st=speedtest.Speedtest()
while True:
    option=int(input("""Seçenek Seçiniz
    1) İndirme Hızı
  
    2) Yükleme Hızı
  
    3) Hepsi
1
    """))
    if option==1:
        print(st.download())
    elif option==2:
        print(st.upload())
    elif option==3:
        print(st.download,st.upload)
    else:
        print("Geçerli bir numara giriniz")
