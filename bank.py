import pygame, sys
import os
from pygame.locals import *
import time
from random import *
import shelve
import sounds
import borders
import varsup
import statusup
import mainscreen

def game(avars, asprs, screen):

    class Mnbx(pygame.sprite.Sprite):

        bxt = []
        
        def __init__(self):
            super().__init__()
            box = pygame.image.load("Sprites/Misc/txtbox/box2.png").convert()

            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 0, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 8, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (0, 16, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (8, 16, 8, 8))
            self.bxt.append(image)
            image = pygame.Surface([8, 8]).convert()
            image.set_colorkey((0, 0, 0))
            image.blit(box, (0, 0), (16, 16, 8, 8))
            self.bxt.append(image)

            self.image = self.bxt[0]
            self.rect = self.image.get_rect()

        def update(self):
            self.image = self.bxt[tl]
    
    kr = True

    chngsts = False

    scr = 0

    ret = 1

    tmn = randint(1, 50)
    pmn = []

    cca = 10

    tuts = True
    strt = False
    play = False
    end = 0

    def drbx():
        tile = Mnbx()
        tile.update()
        textbox.blit(tile.image, [tx, ty])

    def drhl():
        global tx
        global tl
        tx = 0
        drbx()
        tl += 1
        while tx < 48:
            tx += 8
            drbx()
        tx = 56
        tl += 1
        drbx()

    def dral():
        global ty
        global tl
        while ty < 16:
            tl = 3
            ty += 8
            drhl()

    tpborder, btborder, borderico = borders.getborders(avars[3][13], 1, 3, 1)

    hn = pygame.image.load("Sprites/Misc/menu/hngs.png").convert()
    hp = pygame.image.load("Sprites/Misc/menu/hpys.png").convert()
    sk = pygame.image.load("Sprites/Misc/menu/scks.png").convert()
    sl = pygame.image.load("Sprites/Misc/menu/slps.png").convert()

    tutimg = pygame.image.load("Sprites/Misc/bg/bankt.png").convert()

    playbk = pygame.image.load("Sprites/Misc/bg/bank.png").convert()

    mons = []
    m = pygame.image.load("Sprites/Misc/obj/bnkmn.png").convert()
    for i in range(4):
        s = pygame.Surface((24, 24))
        s.fill((0, 255, 255))
        s.blit(m, [-(24 * i), 0])
        s.set_colorkey((0, 255, 255))
        mons.append(s)

    ready = pygame.image.load("Sprites/Misc/bg/ready.png").convert()
    go = pygame.image.load("Sprites/Misc/bg/go.png").convert()

    toobad = pygame.image.load("Sprites/Misc/bg/toobad.png").convert()
    good = pygame.image.load("Sprites/Misc/bg/good.png").convert()
    great = pygame.image.load("Sprites/Misc/bg/great.png").convert()
    excellent = pygame.image.load("Sprites/Misc/bg/excellent.png").convert()

    win = pygame.image.load("Sprites/Misc/emo/happy.png").convert()
    cry = pygame.image.load("Sprites/Misc/emo/cry.png").convert()

    money = pygame.image.load("Sprites/Misc/obj/money.png").convert()
    coin = pygame.image.load("Sprites/Misc/menu/gotchipt.png").convert()

    fnt = pygame.font.Font("Sprites/Misc/font/Tama2.ttf", 16)

    textbox = pygame.Surface([240, 64]).convert()
    textbox.fill((0, 255, 255))
    global tl
    global ty
    tl = 0
    ty = 0
    drhl()
    dral()
    tl = 6
    ty = 24
    drhl()
    textbox.set_colorkey((0, 255, 255))

    clock = pygame.time.Clock()

    sound = sounds.imprtsnd(avars)

    anifr = 0

    pygame.time.set_timer(USEREVENT + 1, int(1000 / ((5 * avars[3][3]) + 1)))
    
    if avars[3][3] == 0:
        avars[3][6] = time.strftime("%H:%M")

    while kr:
        if tuts:
            screen.blit(tutimg, [0, 0])
        elif strt:
            screen.blit(playbk, [0, 0])
            if anifr == 16:
                pygame.mixer.stop()
                sound[11].play()
            if anifr < 16:
                screen.blit(ready, [80, 48])
                spr = 3
            else:
                screen.blit(go, [95, 48])
                spr = 5
            screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
        elif play:
            screen.blit(playbk, [0, 0])
            i = 0
            for n in pmn:
                screen.blit(mons[[1, 2, 5, 10].index(n)], [(10 + (28 * i)), 106])
                i += 1
            if end == 0:
                spr = 3 + (anifr % 12 > 5)
                screen.blit(mons[[1, 2, 5, 10].index(cca)], [(10 + (28 * i)), 98])
            else:
                spr = 5 + (2 * (sum(pmn) != tmn))
                screen.blit(fnt.render(("%04d" % (sum(pmn) * 100)), 1, (0, 0, 100)), [172, 34])
            screen.blit(fnt.render(("%04d" % (tmn * 100)), 1, (0, 0, 100)), [30, 34])
            screen.blit(asprs[avars[3][5]][spr], [104, 32])
        else:
            screen.blit(playbk, [0, 0])
            if end == 3:
                screen.blit(money, [88, 106])
                if anifr < 8:
                    spr = 11
                else:
                    if anifr == 8:
                        pygame.mixer.stop()
                        sound[13].play()
                    screen.blit(textbox, [94, 64])
                    mntxt = fnt.render(str(scr * 200), 1, (0, 0, 100))
                    screen.blit(mntxt, [(138 - (mntxt.get_width())), 74])
                    screen.blit(coin, [138, 72])
                    if scr > 0:
                        spr = 5
                    else:
                        spr = 6
                screen.blit(asprs[avars[3][5]][spr], [(124 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (98 + (32 - asprs[avars[3][5]][spr].get_height()))])
            elif end == 4:
                if scr < 4:
                    screen.blit(toobad, [71, 48])
                    sy = 98
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        spr = 6
                    else:
                        spr = 7
                        screen.blit(cry, [56, 90])
                else:
                    if scr < 8:
                        screen.blit(good, [94, 48])
                    elif scr < 12:
                        screen.blit(great, [85, 48])
                    else:
                        screen.blit(excellent, [51, 48])
                    if ((anifr / 12) - (anifr // 12)) < 0.5:
                        sy = 98
                        spr = 4
                    else:
                        sy = 90
                        spr = 5
                        screen.blit(win, [136, 82])
                screen.blit(asprs[avars[3][5]][spr], [(104 + ((32 - asprs[avars[3][5]][spr].get_width()) // 2)), (sy + (32 - asprs[avars[3][5]][spr].get_height()))])
        screen = borders.drawborders(screen, avars, asprs, tpborder, btborder, borderico, fnt, 0, anifr, hn, hp, sk, sl)
        for event in pygame.event.get():
            if event.type == QUIT:
                varsup.updtvrs(avars)
                kr = False
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mp = event.pos
                d = (screen.get_size()[0] // 240)
                mp = ((mp[0] // d), (mp[1] // d))
                pb = event.button
                if pb == 1:
                    if 138 < mp[1] < 158:
                        if 228 < mp[0] < 240:
                            pygame.mixer.stop()
                            sound[4].play()
                            return(avars, ret)
                        elif 212 < mp[0] < 224:
                            pygame.mixer.stop()
                            sound[4].play()
                            ret = 0
                            return(avars, ret)
                    if (24 < mp[1] < 136) and tuts:
                        pygame.mixer.stop()
                        sound[10].play()
                        tuts = False
                        strt = True
                        anifr = -1
                    if (24 < mp[1] < 136) and play and end == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        pmn.append(cca)
                        if len(pmn) == 8:
                            end = 1
                            anifr = 11
                            pygame.mixer.stop()
                            sound[9 + (3 * (sum(pmn) != tmn))].play()
                if pb == 3:
                    if (24 < mp[1] < 136) and play and end == 0:
                        pygame.mixer.stop()
                        sound[2].play()
                        l = [1, 2, 5, 10]
                        a = l.index(cca) - 1
                        if a == -1:
                            end = 1
                            anifr = 11
                            pygame.mixer.stop()
                            sound[9 + (3 * (sum(pmn) != tmn))].play()
                        else:
                            cca = l[a]
            if event.type == USEREVENT + 1:
                if avars[3][3] == 0:
                    avars[3][6] = time.strftime("%H:%M")
                else:
                    avars[3][7] += 1
                    if avars[3][7] == 60:
                        if int(avars[3][6][3:]) != 59:
                            nhour = avars[3][6][:3] + ("%02d" % (int(avars[3][6][3:]) + 1))
                            avars[3][6] = nhour
                        else:
                            nhour = ("%02d" % (int(avars[3][6][:2]) + 1)) + ":00"
                            if nhour == "24:00":
                                nhour = "00:00"
                            avars[3][6] = nhour
                        avars[3][7] = 0
                if len(avars[0]) > 0:
                    avars[0][2] += 1
                if len(avars[1]) > 0:
                    avars[1][2] += 1
                if len(avars[2]) > 0:
                    avars[2][2] += 1
                chngsts = True
        if chngsts:
            avars = statusup.chngsts(avars)
            chngsts = False
        if anifr < 23:
            anifr += 1
        else:
            anifr = 0
            if strt:
                play = True
                strt = False
            elif play and end == 1:
                if sum(pmn) == tmn:
                    end = 0
                    scr += 1
                    tmn = randint(1, 50)
                    pmn = []
                    cca = 10
                if end == 1 or scr == 12:
                    end = 3
                    play = False
                    if (avars[3][2] + (scr * 200)) < 99999:
                        avars[3][2] += (scr * 200)
                    else:
                        avars[3][2] = 99999
                    avars[avars[3][5]][5] += ((scr * 4) // 3)
                    avars[avars[3][5]][6] += ((scr * 2) // 3)
            elif end == 3:
                if scr < 4:
                    pygame.mixer.stop()
                    sound[14].play()
                else:
                    pygame.mixer.stop()
                    sound[1].play()
                end = 4
            elif end == 4:
                ret = 0
                return(avars, ret)
        s = pygame.Surface([240, 160]).convert()
        s.blit(screen, [0, 0])
        s = pygame.transform.scale(s, (screen.get_size()[0], screen.get_size()[1]))
        screen.blit(s, [0, 0])
        clock.tick(16)
        pygame.display.update()
