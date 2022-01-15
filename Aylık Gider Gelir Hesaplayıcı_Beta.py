print("Aylık Gider Gelir Hesaplayıcı")
while True:
    months=[]
    month=input("Ay giriniz:")
    if month=="q":
        break
    months.append(month)
    try:
        salary=int(input("Maaş giriniz:"))
        extra_salary=int(input("Ekstra maaş giriniz:"))
        electric=int(input("Elektirik faturası giriniz:"))
        naturalgas=int(input("Doğal gaz faturası giriniz:"))
        rent=int(input("Kira giriniz"))
        shoppping_expensives=int(input("Market Alışverişinizi giriniz:"))
        bank_debt=int(input("Banka borcunuzu giriniz:"))
        revennue=salary+extra_salary
        expense=electric+naturalgas+rent+shoppping_expensives+bank_debt
        result=revennue-expense
    except ValueError:
        print("Sayısal Bir değer giriniz")
        break

    print(f'{month} ayında elinizde kalan para ya da kalmayan para {result} ')


