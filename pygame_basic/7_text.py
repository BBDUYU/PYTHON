import pygame
pygame.init() #초기화

#화면 크기 설정
screen_width=480 # 가로크기
screen_height=640 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption('Game Project')

#FPS
clock=pygame.time.Clock()

#배경이미지
background=pygame.image.load('C:/Users/tmdwh/OneDrive/Desktop/VSC/PYTHON/pygame_basic/background.png')

#스프라이트 불러오기
character=pygame.image.load('C:/Users/tmdwh/OneDrive/Desktop/VSC/PYTHON/pygame_basic/character.png')
character_size=character.get_rect().size #이미지의 크기를 구함
character_width=character_size[0] #캐릭터의 가로크기
character_height=character_size[1] #캐릭터의 세로크기
character_x_pos=(screen_width / 2) - (character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos=screen_height - character_height #화면 세로크기 가장 아래에 해당하는 곳에 위치 

# 이동할 좌표
character_to_x_LEFT=0
character_to_x_RIGHT=0
to_y=0

# 이동 속도
character_speed=0.6

# 적 캐릭터
enemy=pygame.image.load('C:/Users/tmdwh/OneDrive/Desktop/VSC/PYTHON/pygame_basic/enemy.png')
enemy_size=enemy.get_rect().size #이미지의 크기를 구함
enemy_width=enemy_size[0] #캐릭터의 가로크기
enemy_height=enemy_size[1] #캐릭터의 세로크기
enemy_x_pos=(screen_width / 2) - (enemy_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치
enemy_y_pos=(screen_height/2) - (enemy_height/2) #화면 세로크기 가장 아래에 해당하는 곳에 위치 

# 폰트
game_font=pygame.font.Font(None,40) #폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time=10

# 시간 계산
start_ticks=pygame.time.get_ticks() # 시작 틱을 가져옴



# 이벤트 루프
running=True #게임이 진행중인가
while running:
    dt=clock.tick(60) #게임화면의 초당 프레임수를 설정

    print('fps : '+str(clock.get_fps())) #프레임 출력
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running=False #게임 진행중이 아님

        if event.type==pygame.KEYDOWN: #키가 눌렸는지
            if event.key==pygame.K_LEFT: #왼쪽
                character_to_x_LEFT -= character_speed
            elif event.key==pygame.K_RIGHT: #오른쪽
                character_to_x_RIGHT += character_speed
            elif event.key==pygame.K_UP: #위
                to_y -= character_speed
            elif event.key==pygame.K_DOWN: #아래
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key==pygame.K_LEFT:
                character_to_x_LEFT=0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos += (character_to_x_LEFT+character_to_x_RIGHT)*dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌처리를 위한 rect 업데이트
    character_rect = character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos

    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('충돌')
        running=False

    screen.blit(background,(0,0)) # 배경
    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #적 그리기
    
    #타이머 집어넣기

    #경과시간계산
    elapsed_time=(pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간(ms)을 1000으로 나누어서 초(s)단위로 표시 (ms -> s)
    timer=game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255)) 
    # 출력할 글자, True, 글자 색상
    
    screen.blit(timer,(10,10)) #타이머 그리기

    #만약 시간이 0 이하면 게임종료
    if total_time - elapsed_time <=0:
        print('타임아웃')
        running=False



    pygame.display.update() #게임화면 다시그리기

# 종료되기전 잠시대기
pygame.time.delay(2000) #2초 대기

#게임 종료
pygame.quit