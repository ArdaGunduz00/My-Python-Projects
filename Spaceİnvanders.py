import pygame
import os
import random
pygame.font.init()
WIDTH=750
HEIGHT=600

WIN=pygame.display.set_mode((WIDTH, HEIGHT))#Burda Pencerenin boyutunu belirttik

#Imagelerı Yuklemek

BACKGROUND=pygame.image.load(os.path.join("assets","background_space.png"))#Arka Plan
#savaş gemisi
BATTLE_SHİP=pygame.image.load(os.path.join("assets", "mission_ship.png"))
#DÜŞMAN GEMİLERİ
RED_ENEMY_SHİP=pygame.image.load(os.path.join("assets", "enemy_ship_red.png"))
BLUE_ENEMY_SHİP=pygame.image.load(os.path.join("assets", "enemy_ship_blue.png"))
GREEN_ENEMY_SHİP=pygame.image.load(os.path.join("assets", "enemy_ship_green.png"))
#LAZERLER
PLAYER_LAZER=pygame.image.load(os.path.join("assets", "blue_rocket.png"))
#DÜŞMAN LAZER
LASER01=pygame.image.load(os.path.join("assets", "laser01.png"))
LASER02=pygame.image.load(os.path.join("assets", "laser02.png"))
LASER03=pygame.image.load(os.path.join("assets", "laser03.png"))
class Laser():
    def __init__(self,x,y,img):
        self.x = x
        self.y=y
        self.img=img

    def move(self,velocity):
        self.y -=velocity

    def draw(self,window):
        window.blit(self.img,(self.x,self.y,))



class Ship():
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
        self.ship_img=None
        self.lazer_img=None
        self.lasers=[]

    def shoot(self):
        laser=Laser(self.x,self.y,self.lazer_img)
        self.lasers.append(laser)

    def MoveLasers(self,velocity):
        for laser in self.lasers:
            laser.move(velocity)
            

    def draw(self,window):# Sayfada yazdırıyıoruz
        window.blit(self.ship_img,(self.x ,self.y))
        for laser in self.lasers:
            laser.draw(window)


    def get_witdh(self):
        return self.ship_img.get_witdth()
    def get_height(self):
        return self.ship_img.get_height()

class PlayerShip(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img=BATTLE_SHİP
        self.lazer_img= PLAYER_LAZER

class EnemyShip(Ship):
    COLOR_MAP= {
        "red":[RED_ENEMY_SHİP,LASER01],
        "blue":[BLUE_ENEMY_SHİP,LASER02],
        "green":[GREEN_ENEMY_SHİP,LASER03]

    }
    def __init__(self,x,y,color,heatlh=100):
        super().__init__(x,y,heatlh)
        self.ship_img,self.lazer_img = self.COLOR_MAP[color]

    def move(self,velocity):
        self.y += velocity




def main():
    enemies=[]
    enemy_velocity=0#Hızı
    laser_velocity=3
    enemy_length=0#Sayısı
    run= True
    FPS=75
    player_velocity=5
    level=0
    main_font=pygame.font.SysFont("Calibri",30)
    level_label= main_font.render(f"Level:{level}",1,(255,255,255))

    clock=pygame.time.Clock()
    player= PlayerShip(350,450)

    def draws():
        WIN.blit(BACKGROUND,(0,0))
        player.draw(WIN)
        for enemy in enemies:
            enemy.draw(WIN)
        level_label= main_font.render(f"Level:{level}",1,(255,255,255))
        WIN.blit(level_label,(600,10))

        pygame.display.update()


    while run:
        clock.tick(FPS)#fps değeriini verdik
        draws()
        if len(enemies)==0:
            enemy_velocity+=1
            enemy_length+=5
            level+=1
            for i in range(enemy_length): #rastele bi şekilde enemy olusturduj
             enemy=EnemyShip(random.randrange(1,700),random.randrange(-1500,-100),random.choice(["red","blue","green"]))
             enemies.append(enemy)#olusturduklarımızı enemiese ekledik



        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run= False

        keys=pygame.key.get_pressed()#Klavye tuşları ile gemimizi hareket ettiyirouz

        if keys[pygame.K_LEFT] and player.x>0:
            player.x-=player_velocity
        if keys[pygame.K_RIGHT] and player.x<650:
            player.x+=player_velocity
        if keys[pygame.K_UP] and player.y>0:
            player.y-=player_velocity
        if keys[pygame.K_DOWN]and player.y<500:
            player.y+=player_velocity
        if keys[pygame.K_SPACE]:
            player.shoot()
        

        for enemy in enemies: # BURDA DÖNGÜYE SOKARAK DÜŞMAN GEMİLERİ AŞAĞIYA GETİRDİK
            enemy.move(enemy_velocity)
            if enemy.y > HEIGHT:
                enemies.remove(enemy)

        player.MoveLasers(laser_velocity)

    
main()
