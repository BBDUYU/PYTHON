#Quiz) 하늘에서 떨어지는 똥피하기 게임

# 게임 조건
# 1. 캐릭터는 화면가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐, X좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임종료
# 5. FPS는 30으로 고정

# 게임 이미지
# 1. 배경 : 640 * 480 - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - enemy.png

import pygame 
import random
#---------------------------------------------------------- 
pygame.init() #초기화 반드시 해야함

#화면 크기 설정
screen_width=480 # 가로크기
screen_height=640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption('Quiz')

#FPS
clock=pygame.time.Clock()
#----------------------------------------------------------

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트)
#배경만들기
background=pygame.image.load('C:\\Users\\tmdwh\\OneDrive\\Desktop\\VSC\\PYTHON\\pygame_basic\\background.png')

#캐릭터
character=pygame.image.load('C:\\Users\\tmdwh\\OneDrive\\Desktop\\VSC\\PYTHON\\pygame_basic\\character.png')
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width/2)-(character_width/2)
character_y_pos=screen_height - character_height

to_x=0
character_speed=10

#적
enemy=pygame.image.load('C:\\Users\\tmdwh\\OneDrive\\Desktop\\VSC\\PYTHON\\pygame_basic\\enemy.png')
enemy_size=enemy.get_rect().size #이미지의 크기를 구함
enemy_width=enemy_size[0] #캐릭터의 가로크기
enemy_height=enemy_size[1] #캐릭터의 세로크기
enemy_x_pos=random.randint(0,screen_width-enemy_width)
enemy_y_pos=0
enemy_speed=10

# 이벤트 루프
running=True #게임이 진행중인가
while running:
    dt=clock.tick(60) #게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    print('fps : '+str(clock.get_fps())) #프레임 출력
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running=False #게임 진행중이 아님
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_x -=character_speed
            elif event.key==pygame.K_RIGHT:
                to_x +=character_speed
            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0

    # 3. 게임 캐릭터 위치 정의의
    character_x_pos += to_x

    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height:
        enemy_y_pos=0
        enemy_x_pos=random.randint(0,screen_width-enemy_width)
    # 4. 충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('충돌')
        running=False
    
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    pygame.display.update() #게임화면 다시그리기

# 종료되기전 잠시대기
pygame.time.delay(2000) #2초 대기

#게임 종료
pygame.quit