import gettext
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendMail(toMail,subject,content):
    fromMail="Example Gmail"
    server=smtplib.SMTP("smtp.gmail.com",587)


    server.starttls()

    server.login(fromMail,'Gmail Password')

    message = MIMEMultipart('alternative')
    message['Subject']= subject

    htmlContent = MIMEText(content,'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()

    )
    server.quit()


url1 ="https://www.trendyol.com/sony/playstation-5-825-gb-dijital-surum-turkce-menu-eurasia-garantili-ps5-p-81980476"


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

page=requests.get(url1, headers=headers)

htmlpage=BeautifulSoup(page.content,'html.parser')

producTittle=htmlpage.find("h1",class_="pr-new-br").getText()

price = htmlpage.find("span",class_="prc-slg").getText()
imagage = htmlpage.find("img",class_="base-product-image")

convertedprice = float(price.replace(",",".").replace("TL",""))

if(convertedprice <=9099):
    print("Product Price Reduce")
    htmlcontent="""\
      <html>
      <head></head>
      <h3>{0}</h3>
      <br/>
      {1}
      <p>Product Url: {2}</p>
      </body>
      </html>
    
    
    """.format(producTittle,image,url1)
    sendMail("Example Gmail"," Product Price Reduce",htmlcontent)
print(convertedprice)
