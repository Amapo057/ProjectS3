# pyinstaller -w -F .\GG\Sosu.py
## -n RunGame.exe -icon=.\GG\icon.png
import pygame
from random import randrange

# 정지스프라이트
City = (pygame.image.load('City.png'))
eSprite1 = (pygame.image.load('EM/0021.png'))
eSprite2 = (pygame.image.load('EM2/0021.png'))
mainScreen = (pygame.image.load('startscreen.png'))
bulletSprite = (pygame.image.load('Bullet.png'))
msSprite = (pygame.image.load('Ms.png'))
icon = (pygame.image.load('icon.png'))
# 화면설정
winSize = winWidth, winHeight = 1920, 1080
win = pygame.display.set_mode(winSize)
pygame.display.set_caption("RunGame")
pygame.display.set_icon(icon)
# 파이게임 초기화
pygame.init()
pygame.mixer.init()
# 화면 주기 설정
clock = pygame.time.Clock()
fps = 30
# 글꼴 설정
font = pygame.font.SysFont("arial", 50, True, True)
# 스프라이트 크기
mSize = (432, 432)
bSize = (800, 800)
# 스프라이트 불러오기
# 달리기
cRunning =      [pygame.image.load('Char/0001.png'),
                pygame.image.load('Char/0002.png'),
                pygame.image.load('Char/0003.png'),
                pygame.image.load('Char/0004.png'),
                pygame.image.load('Char/0005.png'),
                pygame.image.load('Char/0006.png'),
                pygame.image.load('Char/0007.png'),
                pygame.image.load('Char/0008.png'),
                pygame.image.load('Char/0009.png'),
                pygame.image.load('Char/0010.png'),
                pygame.image.load('Char/0011.png'),
                pygame.image.load('Char/0012.png'),
                pygame.image.load('Char/0013.png'),
                pygame.image.load('Char/0014.png'),
                pygame.image.load('Char/0015.png'),
                pygame.image.load('Char/0016.png'),
                pygame.image.load('Char/0017.png'),
                pygame.image.load('Char/0018.png'),
                pygame.image.load('Char/0019.png'),
                pygame.image.load('Char/0020.png'),
                pygame.image.load('Char/0021.png')]
# 공격
cAttacking =    [pygame.image.load('AT/0022.png'),
                pygame.image.load('AT/0023.png'),
                pygame.image.load('AT/0024.png'),
                pygame.image.load('AT/0025.png'),
                pygame.image.load('AT/0026.png'),
                pygame.image.load('AT/0027.png'),
                pygame.image.load('AT/0028.png'),
                pygame.image.load('AT/0029.png'),
                pygame.image.load('AT/0030.png'),
                pygame.image.load('AT/0031.png'),
                pygame.image.load('AT/0032.png'),
                pygame.image.load('AT/0033.png'),
                pygame.image.load('AT/0034.png'),
                pygame.image.load('AT/0035.png'),
                pygame.image.load('AT/0036.png'),
                pygame.image.load('AT/0037.png'),
                pygame.image.load('AT/0038.png'),
                pygame.image.load('AT/0039.png'),
                pygame.image.load('AT/0040.png'),
                pygame.image.load('AT/0041.png'),
                pygame.image.load('AT/0042.png')]
# 막기
cParrying1 =    [pygame.image.load('PR/0044.png'),
                pygame.image.load('PR/0045.png'),
                pygame.image.load('PR/0046.png'),
                pygame.image.load('PR/0047.png'),
                pygame.image.load('PR/0048.png'),
                pygame.image.load('PR/0049.png'),
                pygame.image.load('PR/0050.png'),
                pygame.image.load('PR/0051.png'),
                pygame.image.load('PR/0052.png'),
                pygame.image.load('PR/0053.png'),
                pygame.image.load('PR/0054.png'),
                pygame.image.load('PR/0055.png'),
                pygame.image.load('PR/0056.png'),
                pygame.image.load('PR/0057.png'),
                pygame.image.load('PR/0058.png'),
                pygame.image.load('PR/0059.png'),
                pygame.image.load('PR/0060.png'),
                pygame.image.load('PR/0061.png'),
                pygame.image.load('PR/0062.png'),
                pygame.image.load('PR/0063.png'),
                pygame.image.load('PR/0064.png')]
# 막기2
cParrying2 =    [pygame.image.load('PR2/0088.png'),
                pygame.image.load('PR2/0089.png'),
                pygame.image.load('PR2/0090.png'),
                pygame.image.load('PR2/0091.png'),
                pygame.image.load('PR2/0092.png'),
                pygame.image.load('PR2/0093.png'),
                pygame.image.load('PR2/0094.png'),
                pygame.image.load('PR2/0095.png'),
                pygame.image.load('PR2/0096.png'),
                pygame.image.load('PR2/0097.png'),
                pygame.image.load('PR2/0098.png'),
                pygame.image.load('PR2/0099.png'),
                pygame.image.load('PR2/0100.png'),
                pygame.image.load('PR2/0101.png'),
                pygame.image.load('PR2/0102.png'),
                pygame.image.load('PR2/0103.png'),
                pygame.image.load('PR2/0104.png'),
                pygame.image.load('PR2/0105.png'),
                pygame.image.load('PR2/0106.png'),
                pygame.image.load('PR2/0107.png'),
                pygame.image.load('PR2/0108.png')]
# 점프
cJumping =      [pygame.image.load('JP/0066.png'),
                pygame.image.load('JP/0067.png'),
                pygame.image.load('JP/0068.png'),
                pygame.image.load('JP/0069.png'),
                pygame.image.load('JP/0070.png'),
                pygame.image.load('JP/0071.png'),
                pygame.image.load('JP/0072.png'),
                pygame.image.load('JP/0073.png'),
                pygame.image.load('JP/0074.png'),
                pygame.image.load('JP/0075.png'),
                pygame.image.load('JP/0076.png'),
                pygame.image.load('JP/0077.png'),
                pygame.image.load('JP/0078.png'),
                pygame.image.load('JP/0079.png'),
                pygame.image.load('JP/0080.png'),
                pygame.image.load('JP/0081.png'),
                pygame.image.load('JP/0082.png'),
                pygame.image.load('JP/0083.png'),
                pygame.image.load('JP/0084.png'),
                pygame.image.load('JP/0085.png'),
                pygame.image.load('JP/0086.png')]
# 적1 공격
e1Attacking =   [pygame.image.load('EM/0001.png'),
                pygame.image.load('EM/0002.png'),
                pygame.image.load('EM/0003.png'),
                pygame.image.load('EM/0004.png'),
                pygame.image.load('EM/0005.png'),
                pygame.image.load('EM/0006.png'),
                pygame.image.load('EM/0007.png'),
                pygame.image.load('EM/0008.png'),
                pygame.image.load('EM/0009.png'),
                pygame.image.load('EM/0010.png'),
                pygame.image.load('EM/0011.png'),
                pygame.image.load('EM/0012.png'),
                pygame.image.load('EM/0013.png'),
                pygame.image.load('EM/0014.png'),
                pygame.image.load('EM/0015.png'),
                pygame.image.load('EM/0016.png'),
                pygame.image.load('EM/0017.png'),
                pygame.image.load('EM/0018.png'),
                pygame.image.load('EM/0019.png'),
                pygame.image.load('EM/0020.png'),
                pygame.image.load('EM/0021.png')]
# 적2 공격
e2Attacking =   [pygame.image.load('EM2/0001.png'),
                pygame.image.load('EM2/0002.png'),
                pygame.image.load('EM2/0003.png'),
                pygame.image.load('EM2/0004.png'),
                pygame.image.load('EM2/0005.png'),
                pygame.image.load('EM2/0006.png'),
                pygame.image.load('EM2/0007.png'),
                pygame.image.load('EM2/0008.png'),
                pygame.image.load('EM2/0009.png'),
                pygame.image.load('EM2/0010.png'),
                pygame.image.load('EM2/0011.png'),
                pygame.image.load('EM2/0012.png'),
                pygame.image.load('EM2/0013.png'),
                pygame.image.load('EM2/0014.png'),
                pygame.image.load('EM2/0015.png'),
                pygame.image.load('EM2/0016.png'),
                pygame.image.load('EM2/0017.png'),
                pygame.image.load('EM2/0018.png'),
                pygame.image.load('EM2/0019.png'),
                pygame.image.load('EM2/0020.png'),
                pygame.image.load('EM2/0021.png'),]
# 보스
Boss =          [pygame.image.load('BS/0001.png'),
                pygame.image.load('BS/0002.png'),
                pygame.image.load('BS/0003.png'),
                pygame.image.load('BS/0004.png'),
                pygame.image.load('BS/0005.png'),
                pygame.image.load('BS/0006.png'),
                pygame.image.load('BS/0007.png'),
                pygame.image.load('BS/0008.png'),
                pygame.image.load('BS/0009.png'),
                pygame.image.load('BS/0010.png'),
                pygame.image.load('BS/0011.png'),
                pygame.image.load('BS/0012.png'),
                pygame.image.load('BS/0013.png'),
                pygame.image.load('BS/0014.png'),
                pygame.image.load('BS/0015.png'),
                pygame.image.load('BS/0016.png'),
                pygame.image.load('BS/0017.png'),
                pygame.image.load('BS/0018.png'),
                pygame.image.load('BS/0019.png'),
                pygame.image.load('BS/0020.png'),
                pygame.image.load('BS/0021.png'),
                pygame.image.load('BS/0022.png'),
                pygame.image.load('BS/0023.png'),
                pygame.image.load('BS/0024.png'),
                pygame.image.load('BS/0025.png'),
                pygame.image.load('BS/0026.png'),
                pygame.image.load('BS/0027.png'),
                pygame.image.load('BS/0028.png'),
                pygame.image.load('BS/0029.png'),
                pygame.image.load('BS/0030.png'),
                pygame.image.load('BS/0031.png'),
                pygame.image.load('BS/0032.png'),
                pygame.image.load('BS/0033.png'),
                pygame.image.load('BS/0034.png'),
                pygame.image.load('BS/0035.png'),
                pygame.image.load('BS/0036.png'),
                pygame.image.load('BS/0037.png'),
                pygame.image.load('BS/0038.png'),
                pygame.image.load('BS/0039.png'),
                pygame.image.load('BS/0040.png'),
                pygame.image.load('BS/0041.png'),
                pygame.image.load('BS/0042.png'),
                pygame.image.load('BS/0044.png'),
                pygame.image.load('BS/0045.png'),
                pygame.image.load('BS/0046.png'),
                pygame.image.load('BS/0047.png'),
                pygame.image.load('BS/0048.png'),
                pygame.image.load('BS/0049.png'),
                pygame.image.load('BS/0050.png'),
                pygame.image.load('BS/0051.png'),
                pygame.image.load('BS/0052.png'),
                pygame.image.load('BS/0053.png'),
                pygame.image.load('BS/0054.png'),
                pygame.image.load('BS/0055.png'),
                pygame.image.load('BS/0056.png'),
                pygame.image.load('BS/0057.png'),
                pygame.image.load('BS/0058.png')]
# 보스 공격1
BossAttack1 =   [pygame.image.load('BA/0059.png'),
                pygame.image.load('BA/0060.png'),
                pygame.image.load('BA/0061.png'),
                pygame.image.load('BA/0062.png'),
                pygame.image.load('BA/0063.png'),
                pygame.image.load('BA/0064.png'),
                pygame.image.load('BA/0065.png'),
                pygame.image.load('BA/0066.png'),
                pygame.image.load('BA/0067.png'),
                pygame.image.load('BA/0068.png'),
                pygame.image.load('BA/0069.png'),
                pygame.image.load('BA/0070.png'),
                pygame.image.load('BA/0071.png'),
                pygame.image.load('BA/0072.png'),
                pygame.image.load('BA/0073.png'),
                pygame.image.load('BA/0074.png'),
                pygame.image.load('BA/0075.png'),
                pygame.image.load('BA/0076.png'),
                pygame.image.load('BA/0077.png'),
                pygame.image.load('BA/0078.png'),
                pygame.image.load('BA/0079.png'),
                pygame.image.load('BA/0080.png'),
                pygame.image.load('BA/0081.png'),
                pygame.image.load('BA/0082.png'),
                pygame.image.load('BA/0083.png'),
                pygame.image.load('BA/0084.png'),
                pygame.image.load('BA/0085.png'),
                pygame.image.load('BA/0086.png'),
                pygame.image.load('BA/0087.png'),
                pygame.image.load('BA/0088.png'),
                pygame.image.load('BA/0089.png'),
                pygame.image.load('BA/0090.png'),
                pygame.image.load('BA/0091.png'),
                pygame.image.load('BA/0092.png'),
                pygame.image.load('BA/0093.png'),
                pygame.image.load('BA/0094.png'),
                pygame.image.load('BA/0095.png'),
                pygame.image.load('BA/0096.png'),
                pygame.image.load('BA/0097.png'),
                pygame.image.load('BA/0098.png'),
                pygame.image.load('BA/0099.png'),
                pygame.image.load('BA/0100.png'),
                pygame.image.load('BA/0101.png'),
                pygame.image.load('BA/0102.png'),
                pygame.image.load('BA/0103.png'),
                pygame.image.load('BA/0104.png'),
                pygame.image.load('BA/0105.png'),
                pygame.image.load('BA/0106.png'),
                pygame.image.load('BA/0107.png'),
                pygame.image.load('BA/0108.png'),
                pygame.image.load('BA/0109.png'),
                pygame.image.load('BA/0110.png'),
                pygame.image.load('BA/0111.png'),
                pygame.image.load('BA/0112.png'),
                pygame.image.load('BA/0113.png'),
                pygame.image.load('BA/0114.png'),
                pygame.image.load('BA/0115.png'),]
# 보스 공격2
BossAttack2 =   [pygame.image.load('BA2/0059.png'),
                pygame.image.load('BA2/0060.png'),
                pygame.image.load('BA2/0061.png'),
                pygame.image.load('BA2/0062.png'),
                pygame.image.load('BA2/0063.png'),
                pygame.image.load('BA2/0064.png'),
                pygame.image.load('BA2/0065.png'),
                pygame.image.load('BA2/0066.png'),
                pygame.image.load('BA2/0067.png'),
                pygame.image.load('BA2/0068.png'),
                pygame.image.load('BA2/0069.png'),
                pygame.image.load('BA2/0070.png'),
                pygame.image.load('BA2/0071.png'),
                pygame.image.load('BA2/0072.png'),
                pygame.image.load('BA2/0073.png'),
                pygame.image.load('BA2/0074.png'),
                pygame.image.load('BA2/0075.png'),
                pygame.image.load('BA2/0076.png'),
                pygame.image.load('BA2/0077.png'),
                pygame.image.load('BA2/0078.png'),
                pygame.image.load('BA2/0079.png'),
                pygame.image.load('BA2/0080.png'),
                pygame.image.load('BA2/0081.png'),
                pygame.image.load('BA2/0082.png'),
                pygame.image.load('BA2/0083.png'),
                pygame.image.load('BA2/0084.png'),
                pygame.image.load('BA2/0085.png'),
                pygame.image.load('BA2/0086.png'),
                pygame.image.load('BA2/0087.png'),
                pygame.image.load('BA2/0088.png'),
                pygame.image.load('BA2/0089.png'),
                pygame.image.load('BA2/0090.png'),
                pygame.image.load('BA2/0091.png'),
                pygame.image.load('BA2/0092.png'),
                pygame.image.load('BA2/0093.png'),
                pygame.image.load('BA2/0094.png'),
                pygame.image.load('BA2/0095.png'),
                pygame.image.load('BA2/0096.png'),
                pygame.image.load('BA2/0097.png'),
                pygame.image.load('BA2/0098.png'),
                pygame.image.load('BA2/0099.png'),
                pygame.image.load('BA2/0100.png'),
                pygame.image.load('BA2/0101.png'),
                pygame.image.load('BA2/0102.png'),
                pygame.image.load('BA2/0103.png'),
                pygame.image.load('BA2/0104.png'),
                pygame.image.load('BA2/0105.png'),
                pygame.image.load('BA2/0106.png'),
                pygame.image.load('BA2/0107.png'),
                pygame.image.load('BA2/0108.png'),
                pygame.image.load('BA2/0109.png'),
                pygame.image.load('BA2/0110.png'),
                pygame.image.load('BA2/0111.png'),
                pygame.image.load('BA2/0112.png'),
                pygame.image.load('BA2/0113.png'),
                pygame.image.load('BA2/0114.png'),
                pygame.image.load('BA2/0115.png'),]
# 페이드인
fadein      =   [pygame.image.load('FadeIn/0001.png'),
                pygame.image.load('FadeIn/0002.png'),
                pygame.image.load('FadeIn/0003.png'),
                pygame.image.load('FadeIn/0004.png'),
                pygame.image.load('FadeIn/0005.png'),
                pygame.image.load('FadeIn/0006.png'),
                pygame.image.load('FadeIn/0007.png'),
                pygame.image.load('FadeIn/0008.png'),
                pygame.image.load('FadeIn/0009.png'),
                pygame.image.load('FadeIn/0010.png'),
                pygame.image.load('FadeIn/0011.png'),
                pygame.image.load('FadeIn/0012.png'),
                pygame.image.load('FadeIn/0013.png'),
                pygame.image.load('FadeIn/0014.png'),
                pygame.image.load('FadeIn/0015.png')]
# 글자
endText = font.render("You Died", True, (200,20,60), (0,0,0))
clearText = font.render("You Win!", True, (255,255,255), (0,0,0))
tryagain = font.render("Try again?", True, (255,255,255), (0,0,0))
press = font.render("Press Any Button", True, (255,255,255), (0,0,0))
stage1Text = font.render("Stage 1", True, (255,255,255), (0,0,0))
stage2Text = font.render("Stage 2", True, (255,255,255), (0,0,0))
warningText = font.render("WARNING", True, (200,20,60), (0,0,0))
# 스프라이트 크기변경
cRunning = [pygame.transform.scale(image, mSize) for image in cRunning]
cAttacking = [pygame.transform.scale(image, mSize) for image in cAttacking]
cParrying1 = [pygame.transform.scale(image, mSize) for image in cParrying1]
cParrying2 = [pygame.transform.scale(image, mSize) for image in cParrying2]
e1Attacking = [pygame.transform.scale(image, mSize) for image in e1Attacking]
e2Attacking = [pygame.transform.scale(image, mSize) for image in e2Attacking]
cJumping = [pygame.transform.scale(image, mSize) for image in cJumping]
Boss = [pygame.transform.scale(image, bSize) for image in Boss]
BossAttack1 = [pygame.transform.scale(image, bSize) for image in BossAttack1]
BossAttack2 = [pygame.transform.scale(image, bSize) for image in BossAttack2]
eSprite1 = pygame.transform.scale(eSprite1, mSize)
eSprite2 = pygame.transform.scale(eSprite2, mSize)
bulletSprite = pygame.transform.scale(bulletSprite, (70, 35))

# 사운드
backgroundMusic = pygame.mixer.Sound("Sound/music1.wav")
bossMusic = pygame.mixer.Sound("Sound/bsmusic.wav")
shootSound = pygame.mixer.Sound("Sound/Shoot.wav")
attackSound = pygame.mixer.Sound("Sound/knife.wav")
parrySound = pygame.mixer.Sound("Sound/parry.wav")
backgroundMusic.set_volume(0.2)
bossMusic.set_volume(0.3)
shootSound.set_volume(0.1)
attackSound.set_volume(0.1)
parrySound.set_volume(0.1)

run = True
attack = False
parry = False
rParry = False
sAttack = False
sParry = False
success = False

jump = False
sJump = False
yUp = True
yDown = False

enemy1 = True
enemy2 = False
e1Attack = True
e2Attack = False
shootting1 = False
shootting2 = False
shootting3 = False
shootting1_2 = False
shoottingMs = False

printStartscreen = True
runStart = False
startFade = False
end = False
stage1 = False
stage2 = False
stage3 = False
clear = False

walkCount = 0
enemyCount1 = 0
enemyCount2 = 0
shoot1 = 0
shoot2 = 0
#스프라이트 위치설정
xChar = 10
xEnemy1 = winWidth
xEnemy2 = winWidth
y = 650
yJump = y
yHigh = 450
hitBox = 340
killCount = 0

xCity1 = 0
xCity2 = winWidth * 2
xSpeed = 25

shootCount1 =0
shootCount2 = 0
shootCount3 = 0
shootCount4 = 0
shootCount5 = 0
yShoot = y+70
tShoot = 30
speedShoot = 45
fade = 0

# 스프라이트 그리기
def printSprite():
    global xCity1, xCity2
    global walkCount, sAttack, sParry, sJump, yJump, yHigh, yUp, yDown, rParry
    global xEnemy1, xEnemy2

# 배경 스프라이트 출력
    win.blit(City,(xCity1, 0))
    win.blit(City,(xCity2, 0))
    xCity1 -= xSpeed
    xCity2 -= xSpeed
    if xCity1 <= -winWidth * 2:
        xCity1 = 0
        xCity2 = winWidth * 2
# 캐릭터 스프라이트
    if walkCount >= 21:
        walkCount = 0
    if attack:
        if walkCount == 0:
            attackSound.play(0)
        win.blit(cAttacking[walkCount],(xChar, y))
        walkCount += 1
        if walkCount == 3:
            sAttack = True
        elif walkCount == 11:
            sAttack = False
    elif parry:
        if walkCount == 0:
            if randrange(2):
                rParry = True
            else:
                rParry = False
        if rParry:
            win.blit(cParrying1[walkCount],(xChar, y))
        else:
            win.blit(cParrying2[walkCount],(xChar, y))
        walkCount += 1
        if walkCount == 3:
            sParry = True
        elif walkCount == 15:
            sParry = False
    elif jump:
        win.blit(cJumping[walkCount],(xChar, yJump))
        walkCount += 1
        if yUp:
            yJump -= 20
        if yDown:
            yJump += 25
        if yJump <= yHigh:
            yUp = False
            yDown = True
        if walkCount == 3:
            sJump = True
        elif walkCount == 17:
            sJump = False
    elif run:
        win.blit(cRunning[walkCount],(xChar, y))
        walkCount += 1
# 적 스프라이트 출력
    if stage3:
        startBoss()
    if stage3 == False:    
        if enemy1:
            if xEnemy1 > xEnemy2:
                if xEnemy1 - xEnemy2 <= 700:
                    xEnemy1 += 700
            sEnemy1()
        if enemy2:
            if xEnemy2 > xEnemy1:
                if xEnemy2 - xEnemy1 <= 700:
                    xEnemy2 += 700
            sEnemy1_2()

# 적 스프라이트1
def sEnemy1():
    global sAttack, success, hitBox, killCount
    global enemy2, enemyCount1, winWidth
    global xEnemy1, e1Attack, e2Attack
    global shoot1, shootting1, shootting2, shootting3

# 공격주기 카운트
    shoot1 += 1
    if xEnemy1 >= winWidth:
        shoot1 = 0
        if stage2:
            if randrange(2):
                e1Attack = True
                e2Attack = False
            else:
                e1Attack = False
                e2Attack = True
# 스프라이트 출력
    if shoot1 < tShoot:
        if e1Attack:
            win.blit(eSprite1, (xEnemy1, y))
        if e2Attack:
            win.blit(eSprite2, (xEnemy1, y))
#스프라이트위치변경
    xEnemy1 -= xSpeed
    if xEnemy1 <= 0:
        xEnemy1 = winWidth
# 공격 스프라이트 출력
    if shoot1 >= tShoot:
        if e1Attack:
            win.blit(e1Attacking[enemyCount1], (xEnemy1, y))
        if e2Attack:
            win.blit(e2Attacking[enemyCount1], (xEnemy1, y))
        enemyCount1 += 1
        if e2Attack:
            if shoot1 == tShoot + 7:
                shootting2 = True
            if shoot1 == tShoot + 14:
                shootting3 = True
        if shoot1 == tShoot+18:
            shoot1 = 0
            enemyCount1 = 0
    if shoot1 == tShoot:
        shootting1 = True
        enemy2 = True
    if shootting1:
        sShoot1()
    if shootting2:
        sShoot2()
    if shootting3:
        sShoot3()
# 공격 받는 조건
    if xEnemy1 <= hitBox:
        if sAttack:
            if randrange(3) == 1:
                xEnemy1 = 2100
            elif randrange(3) == 2:
                xEnemy1 = 2500
            else:
                xEnemy1 = 2800
            killCount += 1
            sAttack = False
            success = True
        endGame(xEnemy1)

# 적 스프라이트1_2
def sEnemy1_2():
    global sAttack, success, hitBox, killCount
    global enemy2, enemyCount2, winWidth, xEnemy1, xEnemy2, e1_2Attack
    global shoot2, shootting1_2

# 공격주기 카운트
    shoot2 += 1
    if xEnemy2 >= winWidth:
        shoot2 = 0
# 스프라이트 출력
    if shoot2 < tShoot:
        win.blit(eSprite1, (xEnemy2, y))
#스프라이트위치변경
    xEnemy2 -= xSpeed
    if xEnemy2 <= 0:
        xEnemy2 = winWidth
# 공격 스프라이트 출력
    if shoot2 >= tShoot:
        win.blit(e1Attacking[enemyCount2], (xEnemy2, y))
        enemyCount2 += 1
        if shoot2 == tShoot+18:
            shoot2 = 0
            enemyCount2 = 0
    if shoot2 == tShoot:
        shootting1_2 = True
    if shootting1_2:
        sShoot1_2()
# 공격 받는 조건
    if xEnemy2 <= hitBox:
        if sAttack:
            if randrange(3) == 1:
                xEnemy2 = 2100
            elif randrange(3) == 2:
                xEnemy2 = 2500
            else:
                xEnemy2 = 2800
            killCount += 1
            sAttack = False
            success = True
        endGame(xEnemy2)

# 보스 스프라이트
def startBoss():
    global sAttack, success, hitBox, killCount
    global enemyCount1, xEnemy1, enemy1, enemy2, e2Attack
    global shoot1, shootting1, shootting2, shootting3, shoottingMs

    shoot1 += 1
    if xEnemy1 == winWidth:
        xEnemy1 = 1200
    if enemy1:
        if xEnemy1 <= 1200:
                xEnemy1 += xSpeed
    if enemyCount1 == 57:
        if enemy1:
            enemy1 = False
            if randrange(2):
                enemy2 = True
            else:
                e2Attack = True
        else:
            enemy2 = False
            e2Attack = False
            enemy1 = True
        enemyCount1 = 0
    if enemy1:    
        win.blit(Boss[enemyCount1],(xEnemy1, y-300))
    if enemy2:
        win.blit(BossAttack1[enemyCount1],(xEnemy1, y-300))
        if enemyCount1 >= 18:
            xEnemy1 -= xSpeed
            if enemyCount1 == 30:
                shootting1 = True
            if enemyCount1 == 35:
                shootting2 = True
            if enemyCount1 == 40:
                shootting3 = True
    if e2Attack:
        win.blit(BossAttack2[enemyCount1], (xEnemy1, y-300))
        if enemyCount1 >= 18:
            xEnemy1 -= xSpeed
            if enemyCount1 == 25:
                shoottingMs = True
    
    if enemy1 == False:
        if xEnemy1 <= hitBox:
                if sAttack:
                    killCount += 1

    if shootting1:
        sShoot1()
    if shootting2:
        sShoot2()
    if shootting3:
        sShoot3()
    if shoottingMs:
        sMs()
    enemyCount1 += 1  

# 총알1
def sShoot1():
    global sParry, success
    global speedShoot, shootCount1, shootting1
    if shootCount1 == 0:
        shootSound.play(0)

# x좌표 지정
    shootCount1 += 1
    xShoot = xEnemy1 - speedShoot * shootCount1
# 스프라이트 출력
    win.blit(bulletSprite, (xShoot, yShoot))
# 피격 판정
    if xShoot <= hitBox + 20:
        if sParry:
            sParry = False
            success = True
            shootCount1 = 0
            shootting1 = False
            parrySound.play(0)
        endGame(xShoot)
# 총알2
def sShoot2():
    global sParry, success
    global speedShoot, shootCount2, shootting2
    if shootCount2 == 0:
        shootSound.play(0)
# x좌표 지정
    shootCount2 += 1
    xShoot = xEnemy1 - speedShoot * shootCount2
# 스프라이트 출력
    win.blit(bulletSprite, (xShoot, yShoot))
# 피격 판정
    if xShoot <= hitBox + 20:
        if sParry:
            sParry = False
            success = True
            shootCount2 = 0
            shootting2 = False
            parrySound.play(0)
        endGame(xShoot)
# 총알3
def sShoot3():
    global sParry, success
    global speedShoot, shootCount3, shootting3
    if shootCount3 == 0:
        shootSound.play(0)
# x좌표 지정
    shootCount3 += 1
    xShoot = xEnemy1 - speedShoot * shootCount3
# 스프라이트 출력
    win.blit(bulletSprite, (xShoot, yShoot))
# 피격 판정
    if xShoot <= hitBox + 20:
        if sParry:
            sParry = False
            success = True
            shootCount3 = 0
            shootting3 = False
            parrySound.play(0)
        endGame(xShoot)

# 총알1_2
def sShoot1_2():
    global sParry, success
    global speedShoot, shootCount4, shootting1_2
    if shootCount4 == 0:
        shootSound.play(0)
# x좌표 지정
    shootCount4 += 1
    xShoot = xEnemy2 - speedShoot * shootCount4
# 스프라이트 출력
    win.blit(bulletSprite, (xShoot, yShoot))
    if xShoot <= hitBox + 20:
        if sParry:
            sParry = False
            success = True
            shootCount4 = 0
            shootting1_2 = False
            parrySound.play(0)
        endGame(xShoot)

# 미사일
def sMs():
    global sJump, success
    global speedShoot, shootCount5, shoottingMs, yShoot
    if shootCount5 == 0:
        shootSound.play(0)

# x좌표 지정
    shootCount5 += 0.7
    xShoot = xEnemy1 - speedShoot * shootCount5
    if yShoot <= 900:
        yShoot += xSpeed
# 스프라이트 출력
    win.blit(msSprite, (xShoot, yShoot))
    if xShoot <= hitBox + 20:
        if sJump == False:
            endGame(xShoot)
    if xShoot <= 0:
        shootCount5 = 0
        shoottingMs = False
        yShoot = y + 70
        success = True

# 로비화면
def startScreen():
    global printStartscreen, runStart, startFade, fade, run, stage1

    win.blit(mainScreen,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                    run = False
        if event.type == pygame.KEYDOWN:
            startFade = True
    if startFade:
        printFadein()
        if fade == 14:
            printStartscreen = False
            runStart = True
            stage1 = True
            startFade = False
            fade = 0
            backgroundMusic.play(-1)

# 메인 게임
def main():
    global run, attack, parry, walkCount, success
    global jump, yUp, yDown, yJump

# 키입력시 행동
    key = pygame.key.get_pressed()
    if attack == False:
        if parry == False:
            if jump == False:
                if key[pygame.K_z]:
                    walkCount = 0
                    attack = True
                if key[pygame.K_x]:
                    walkCount = 0
                    parry = True
                if key[pygame.K_c]:
                    walkCount = 0
                    jump = True
    if success:
        if key[pygame.K_z]:
            walkCount = 0
            attack = True
            success = False
        if key[pygame.K_x]:
            walkCount = 0
            attack = False
            parry = True
            success = False
        if key[pygame.K_c]:
            walkCount = 0
            attack = False
            parry = False
            jump = True
# 스프라이트를 다 출력하면 행동 종료
    if walkCount == 21:
        attack = False
        parry = False
        jump = False
        yUp = True
        yDown = False
        yJump = y
        success = False

    printSprite()

def printFadein():
    global fade
    win.blit(fadein[fade],(0,0))
    if fade < 14:
        fade += 1

def resetCount():
    global killCount, stage1, stage2, stage3, fade, clear
    global enemyCount1, enemyCount2, xEnemy1, xEnemy2, e1Attack, e2Attack, yShoot
    global shootCount1, shootCount2, shootCount3, shootCount4, shootCount5
    global shootting1, shootting2, shootting3, shootting1_2, shoottingMs
    global enemy1, enemy2, xCity1, xCity2

    enemyCount1 = 0
    enemyCount2 = 0
    xEnemy1 = winWidth
    xEnemy2 = winWidth + 500
    xCity1 = 0
    xCity2 = winWidth * 2
    shootCount4 = 0
    killCount = 0
    fade = 0
    enemy1 = True
    enemy2 = False
    stage1 = False
    stage2 = False
    stage3 = False
    shootting1 = False
    shootting2 = False
    shootting3 = False
    shootting1_2 = False
    shoottingMs = False
    shootCount1 = 0
    shootCount2 = 0
    shootCount3 = 0
    shootCount4 = 0
    shootCount5 = 0
    yShoot = y + 70
    e1Attack = True
    e2Attack = False
    clear = False

def endGame(a):
    global end, runStart
    if a <= hitBox - 150:
        end = True
        runStart = False

while run:
    print(killCount)
    clock.tick(fps)
    if printStartscreen:
        startScreen()

    if runStart:
        main()

    if stage1:
        if killCount == 0:
            win.blit(stage1Text,(900,100))
        if killCount >= 15:
            startFade = True
            if startFade:
                printFadein()
                if fade >= 14:
                    resetCount()
                    stage2 = True
                    startFade = False 
    if stage2:
        if killCount == 0:
            win.blit(stage2Text,(900,100))
        if killCount >= 17:
            backgroundMusic.fadeout(500)
            startFade = True
            if startFade:
                printFadein()
                if fade >= 14:
                    bossMusic.play(-1)
                    resetCount()
                    stage2 = False
                    stage3 = True
                    startFade = False
    if stage3:
        if killCount == 0:
            win.blit(warningText,(900,100))
        if killCount >= 17:
            end = True
            clear = True

    # 마지막 화면
    if end:
        printFadein()
        backgroundMusic.stop()
        bossMusic.stop()
        if fade >= 14:
            runStart = False
            if clear == False:
                win.blit(endText,(900,300))
            else:
                win.blit(clearText,(900,300))
            win.blit(tryagain,(900,600))
            win.blit(press,(830,700))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    printStartscreen = True
                    pygame.init()
                    end = False
                    resetCount()

    # 창 닫으면 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()