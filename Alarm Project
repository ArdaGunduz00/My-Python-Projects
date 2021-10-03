import pygame
import sys
import time
from datetime import datetime
import pytz

pygame.init()
boyut = (1280,720)
Turkey= pytz.timezone
font =pygame.font.SysFont("Helvetica",80)
tarihText= font.render("Şu an saat",1,(255,0,0),(0,0,0))
pencere = pygame.display.set_mode(boyut)

alarmH = int(input("Alarm saatini giriniz:"))
alarmM = int(input("Alarm dakikasını giriniz:"))

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    datetime_Turkey = datetime.now(Turkey)
    saat = datetime_Turkey.hour
    dakika = datetime.Turkey.minute
    saniye = datetime.Turkey.second
    tarihText = font.render("{}:{}:{}".format(saat, dakika, saniye), 1, (0, 0, 255), (0, 0, 0))

    if alarmH == saat and alarmM == dakika:
        pygame.mixer.music.load("alarm.mp3")
        pygame.mixer.music.play()
        break
    pencere.blit(tarihText, (0, 0))
    pygame.display.update()
