##JALANKAN CODE DARI TERMINAL DAN KETIK = 
##C:/Users/Lenovo/AppData/Local/Programs/Python/Python313/python.exe labirint.py


import pygame
pygame.init()


""" MEMBUAT JENDELA / SCENE """
SCENE_LEBAR = 700
SCENE_TINGGI = 500
SCENE = pygame.display.set_mode((SCENE_LEBAR, SCENE_TINGGI))
pygame.display.set_caption("INI GAME LABRIN COBA")
WARNA_BIRU = (35, 142, 173)
SCENE.fill(WARNA_BIRU)
GAMBAR_SCENE = pygame.image.load("Latarr.png")
FPS = pygame.time.Clock()


""" MEMBUAT CLASS SPRITE """
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, nama_gambar, lebar, tinggi, x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(nama_gambar),(lebar, tinggi))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        SCENE.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, nama_gambar, lebar, tinggi, x, y, x_speed, y_speed):
        super().__init__(nama_gambar, lebar, tinggi, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        ## membatasi gerakan KIRI KANAN tetap di dalam layar
        if self.rect.x >= 0 and self.x_speed < 0 or self.rect.x <= SCENE_LEBAR - 50 and self.x_speed > 0 :
            self.rect.x += self.x_speed
        TERSENTUH = pygame.sprite.spritecollide(self, GRUP_DINDING, False)
        if self.x_speed > 0:
            for dinding in TERSENTUH:
                self.rect.right = min(self.rect.right, dinding.rect.left)
        elif self.x_speed < 0:
            for dinding in TERSENTUH:
                self.rect.left = max(self.rect.left, dinding.rect.right)
        ## membatasi gerakan ATAS BAWAH tetap di dalam layar
        if self.rect.y >= 0 and self.y_speed < 0 or self.rect.y <= SCENE_TINGGI - 50 and self.y_speed > 0 :
            self.rect.y += self.y_speed
        TERSENTUH = pygame.sprite.spritecollide(self, GRUP_DINDING, False)
        if self.y_speed > 0: # turun
            for dinding in TERSENTUH:
                self.rect.bottom = min(self.rect.bottom, dinding.rect.top)
        elif self.y_speed < 0: # naik ke atas
            for dinding in TERSENTUH:
                self.rect.top = max(self.rect.top, dinding.rect.bottom)


    def tembak(self):
        peluru = Bullet("peluru.png", 20, 10, self.rect.centerx, self.rect.centery, 20)
        GRUP_PELURU.add(peluru)

class Enemy(GameSprite):
    def __init__(self, nama_gambar, lebar, tinggi, x, y, y_speed, arah="ke atas"):  #tambahkan x_speed jika ingin bergerak kiri kanan
        super().__init__(nama_gambar, lebar, tinggi, x, y)
        # self.x_speed = x_speed
        self.y_speed = y_speed
        self.arah = arah
        # self.ARAH = ARAH
    def update(self):
        # if self.rect.x < 600:
        #     self.ARAH = "ke kanan"
        # if self.rect.x > SCENE_LEBAR-50:
        #     self.ARAH = "ke kiri"

        # if self.ARAH == "ke kanan":  ##membuat pergerakan
        #     self.rect.x += self.x_speed
        # else:
        #     self.rect.x -= self.x_speed

        if self.rect.y < 80 :
            self.arah = "ke bawah"
        if self.rect.y > 450:
            self.arah = "atas"

        if self.arah == "ke bawah":  ##membuat pergerakan
            self.rect.y += self.y_speed
        else:
            self.rect.y -= self.y_speed


class Bullet(GameSprite):
    def __init__(self, nama_gambar, lebar, tinggi, x, y, x_speed):
        super().__init__(nama_gambar, lebar, tinggi, x, y)
        self.x_speed = x_speed
    def update(self):
        self.rect.x += self.x_speed
        if self.rect.x > SCENE_LEBAR:
            self.kill()



""" MEMBUAT OBJEK GAME """
dinding1 = GameSprite("tembok.png", 470, 50, 100, 0)
dinding2 = GameSprite("tembok.png", 200, 50, 400, 270)
dinding3 = GameSprite("tembok.png", 500, 50, 0, 120)
dinding4 = GameSprite("tembok.png", 50, 400, 570, 0)
dinding5 = GameSprite("tembok.png", 50, 80, 360, 270)
dinding6 = GameSprite("tembok.png", 120, 50, 250, 300)
dinding7 = GameSprite("tembok.png", 50, 120, 215, 230)
dinding8 = GameSprite("tembok.png", 180, 50, 85, 230)
dinding9 = GameSprite("tembok.png", 90, 65, 320, 150) 
dinding10 = GameSprite("tembok.png", 30, 320, 0, 150)
dinding11 = GameSprite("tembok.png", 620, 40, 0, 470)
pemain = Player("bombb.png", 50, 50, 10, 10, 0, 0)
musuh = Enemy("musuh.png", 50, 50, 630, 350, 20)
peluru = Bullet("peluru.png", 20, 10, 20, 10, 5)
harta = GameSprite("logoebo.png", 50, 60, 630, 10)
gambar_menang = pygame.transform.scale(pygame.image.load("menang.png"),(SCENE_LEBAR, SCENE_TINGGI))
GAMBAR_SCENE = pygame.transform.scale(pygame.image.load("Latarr.png"), (SCENE_LEBAR, SCENE_TINGGI))


""" MEMBUAT FONT TULISAN"""
pygame.font.init()
FONT = pygame.font.SysFont("jokerman", 50)
warna_hitam = (0, 0, 0)
TULISAN_MENANG = FONT.render("YOU WIN!!!", True, warna_hitam)
FONTK = pygame.font.SysFont("jokerman", 50)
TULISAN_KALAH = FONT.render("YOU LOSE!!!", True, warna_hitam)

"""MEMBUAT GRUP DINDING"""
GRUP_DINDING = pygame.sprite.Group() ##membuat grup
GRUP_DINDING.add(dinding1) ##tambahkan ke grup
GRUP_DINDING.add(dinding2) ##tambahkan ke grup
GRUP_DINDING.add(dinding3)
GRUP_DINDING.add(dinding4)
GRUP_DINDING.add(dinding5) ##tambahkan ke grup
GRUP_DINDING.add(dinding6) ##tambahkan ke grup
GRUP_DINDING.add(dinding7)
GRUP_DINDING.add(dinding8)
GRUP_DINDING.add(dinding9)
GRUP_DINDING.add(dinding10)
GRUP_DINDING.add(dinding11)


""" GRUP MUSUH """
GRUP_MUSUH = pygame.sprite.Group()
GRUP_MUSUH.add(musuh)

""" GRUP PELURU """
GRUP_PELURU = pygame.sprite.Group()

""" MEMBUAT LOOP GAME """
GAME_SELESAI = False ## artinya game belum selesai
GAME_HIDUP = True ## artinya game sedang berjalan
while GAME_HIDUP:
    if GAME_SELESAI == False: 
        SCENE.blit(GAMBAR_SCENE, (0, 0))
        # dinding1.reset()
        # dinding2.reset() 
        GRUP_DINDING.draw(SCENE)
        GRUP_PELURU.draw(SCENE)
        pygame.sprite.groupcollide(GRUP_PELURU, GRUP_DINDING, True, False) ## tabrakan antar grup
        pygame.sprite.groupcollide(GRUP_PELURU, GRUP_MUSUH, True, True)
        harta.reset() ## tampilkan harta
        pemain.reset() ## tampilkan pemain
        pemain.update() ## membuat pemain bergerak
        GRUP_PELURU.update()
        GRUP_MUSUH.draw(SCENE)
        GRUP_MUSUH.update()
        ## kondisi menang
        if pygame.sprite.collide_rect(pemain, harta):
            #SCENE.blit(gambar_menang, (0, 0)) ## menampilkan gambar ketika sudah menang
            SCENE.blit(TULISAN_MENANG, (200, 200)) ## menampilkan tulisan ketika sudah menang
            GAME_SELESAI = True ## artinya permainan selesai 

        if pygame.sprite.spritecollide(pemain, GRUP_MUSUH, True):
            SCENE.blit(TULISAN_KALAH, (200, 200))
            GAME_SELESAI = True

            
    FPS.tick(60)
    pygame.display.update()


    """ EVENT HANDLER UNTUK QUIT """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_HIDUP = False ## artinya game berhenti
        """ EVENT HANDLER UNTUK PERGERAKAN PEMAIN """
        kecepatan = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pemain.tembak()
            if event.key == pygame.K_w: ## ke atas
                pemain.y_speed -= kecepatan
            elif event.key == pygame.K_s: ## kebawah
                pemain.y_speed += kecepatan
            elif event.key == pygame.K_a: ## ke kiri
                pemain.x_speed -= kecepatan
            elif event.key == pygame.K_d: ## ke kanan
                pemain.x_speed += kecepatan
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w: ## ke atas
                pemain.y_speed = 0
            elif event.key == pygame.K_s: ## kebawah
                pemain.y_speed = 0
            elif event.key == pygame.K_a: ## ke kiri
                pemain.x_speed = 0
            elif event.key == pygame.K_d: ## ke kanan
                pemain.x_speed = 0