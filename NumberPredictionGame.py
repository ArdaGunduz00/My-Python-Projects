import random
print("""
Sayı bulma oyunu
""")


sayıtahmin=random.randint(0,20)
can=10

while can>0:

    sayı=int(input("sayı giriniz:"))

     

    if sayı==sayıtahmin:
            print("Tebrikler")
            break
    elif sayı>sayıtahmin:
            can-=1
            print("Aşağı Gel","Kalan can:",{can}) 
    elif sayı<sayıtahmin:
            can-=1
            print(f"Yukarı Gel","Kalan can:",{can}) 

    if can==0:
        print("kaybettiniz")
        break
