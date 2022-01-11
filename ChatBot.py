import datetime
import pygame as py
import os
import webbrowser
from turtle import Turtle, Screen
tarih = datetime.datetime.now()
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
print("""
Robot İle Konuş""")

def voicerobot(answer):
    py.mixer.init()
    py.mixer.music.load(answer)
    py.mixer.music.play()


useradd = input("Kullanıcı Adı:")
userpassword = input("Şifre:")
if useradd == "arda" and userpassword == "1234":
    voicerobot("sir.mp3")
else:
    print("Yanlış Şifre ya da Kullanıcı adı")
    quit()
try:

    while True:
       question = input(("Bana soru sorun efendim:")).lower()
       if question == ("adın ne senin"):
           voicerobot("Ad.Jarvis.mp3")

       elif question == ("saat kaç"):
           print(f'Şuan saat:{tarih}')

       elif question == ("nasılsın"):
           voicerobot("iyiyim.mp3")

       elif question == ("bana espri yaparmısın"):
           voicerobot("espri.mp3")

       elif question == ("görüşürüz"):
           voicerobot("Görüşürüz" )

       elif question == ("nerde yaşıyosun"):
           voicerobot("nerdeyasıon.mp3")

       elif question == ("ben nerde okuyorum"):
           voicerobot("okul.mp3")

       elif question == ("gelecekde nerde olacaksın"):
           voicerobot("gelecekte nerde olacaksın.mp3")

       elif question=="çıkmak istiyorum":
           voicerobot("çıkış..mp3")
       elif question=="bana şarkı çal":
           webbrowser.get(chrome_path).open('https://www.youtube.com/watch?v=6xJYQGRHM7c/')
       elif question=="bana resim çiz":
           wn = Screen()
           def tree(length, t):
               if length > 5:
                   t.forward(length)
                   t.right(40)
                   tree(length - 15, t)
                   t.left(80)  # sola dön
                   tree(length - 15, t)
                   t.right(40)
                   t.backward(length)


           t = Turtle()
           t.left(90)
           t.speed(0)
           tree(100, t)
           wn.exitonclick()


           break

    else:
           voicerobot("Beni daha buna kodlamadın :")

except:
    print(f'{question} sorusuna cevap bulununamadı geliştiricim bunu ekleyecektir')
