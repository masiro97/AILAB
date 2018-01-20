import pygame, evol, random, time

pygame.init()
screenx = 400 # x 크기
screeny = 300 # y크기
blackx = 100 # 블랙돌 시작 위치
blacky = 150
bspeed = 50
hcount = 0 #잡힌 개수
wspeed = 50
whitex = 300
whitey = 100
screen = pygame.display.set_mode((screenx,screeny))
count1 = 0 #이동 경로
count2 = 0
obnum = 20 # 한세대 개체수
generation = 0
gennum = 20 #유전자 갯수
frame = 0.1
bmove = 0
av = 0
wcolor = [255,255,255]
gen = evol.maker(obnum,gennum)
hitlist = []
average = []
mutchance = 30 #단위는 %

def goodness(list):
    rullet = random.randrange(1,101)
    list2 = []
    for i in list:
        list2.append(i)
    list2.sort
    list2.reverse()

    mother = list.index(list2[0])
    father = list.index(list2[1])

    return [mother,father]

while 1:
    #백돌 움직임{
    if gen[count1][count2]==0 and whitey-20>=0:
        whitey -= wspeed
    if gen[count1][count2]==1 and whitey+20<=screeny:
        whitey += wspeed
    if gen[count1][count2]==2 and whitex-20>=0:
        whitex -= wspeed
    if gen[count1][count2]==3 and whitex+20<=screenx:
        whitex += wspeed
    #}백돌 움직임

    #흑돌움직임{
    if whitey<blacky:
        bmove = 0
    if whitey>blacky:
        bmove = 1
    if whitex<blackx:
        bmove = 2
    if whitex>blackx:
        bmove = 3
    if bmove==0 and blacky-20>=0:
        blacky -= bspeed
    if bmove==1 and blacky+20<=screeny:
        blacky += bspeed
    if bmove==2 and blackx-20>=0:
        blackx -= bspeed
    if bmove==3 and blackx+20<=screenx:
        blackx += bspeed
    #}흑돌움직임
    #그리기{
    screen.fill((180,180,180))
    for i in range(0,int((screenx/50))+1):
        pygame.draw.line(screen,[0,0,0],(i*50,0),(i*50,screeny),2)
    for i in range(0,int((screeny/50))+1):
        pygame.draw.line(screen,[0,0,0],(0,i*50),(screenx,i*50),2)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                frame = 0
            if i.key == pygame.K_DOWN:
                frame = 0.1
    if blackx == whitex and blacky == whitey:
        wcolor = [255,0,0]
        hcount += 1

    else:
        wcolor = [255,255,255]
    pygame.draw.circle(screen,[0,0,0],(blackx,blacky),20,0)
    pygame.draw.circle(screen,wcolor,(whitex,whitey),20,0)
    #}그리기

    count2 += 1
    distance = ((blackx - whitex) ** 2 + (blacky - whitey) ** 2) ** 0.5
    average.append(distance)
    #개체교체{
    if count2 == gennum:
        count2 = 0
        count1 += 1
        blackx = 100
        blacky = 150
        whitex = 300
        whitey = 100
        for i in average:
            av += i
        av = float(av)/gennum
        hitlist.append(av)
        av = 0
        average = []
        print (hcount)
        hcount = 0
    #}개체교체
    #세대교체{
    if count1 == obnum:
        count1 = 0
        father = gen[goodness(hitlist)[0]]
        mother = gen[goodness(hitlist)[1]]
        gen = evol.evol([father,mother],obnum,gennum,mutchance,2)
        generation += 1

        print('%dGENERATION'%generation)
        hitlist = []
    #}세대교체

    time.sleep(frame)
    pygame.display.update()
