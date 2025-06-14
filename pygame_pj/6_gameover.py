import pygame 
import os
#---------------------------------------------------------- 
pygame.init() #초기화 반드시 해야함

#화면 크기 설정
screen_width=640 # 가로크기
screen_height=480 # 세로크기
screen=pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption('Pang')

#FPS
clock=pygame.time.Clock()
#----------------------------------------------------------

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트)
cureent_path=os.path.dirname(__file__) #현재 파일의 위치반환
image_path=os.path.join(cureent_path,'images') #images폴더위치 반환

# 배경
background=pygame.image.load(os.path.join(image_path,'background.png'))

# 스테이지
stage=pygame.image.load(os.path.join(image_path,'stage.png'))
stage_size=stage.get_rect().size
stage_height=stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기위해 사용

# 캐릭터 만들기
character=pygame.image.load(os.path.join(image_path,'character.png'))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(screen_width/2) - (character_width/2)
character_y_pos=screen_height-character_height-stage_height

character_to_x_LEFT=0
character_to_x_RIGHT=0
character_speed=5

# 무기 만들기
weapon=pygame.image.load(os.path.join(image_path,'weapon.png'))
weapon_size=weapon.get_rect().size
weapon_width=weapon_size[0]

# 무기는 한번에 여러번 발사 가능
weapons=[]

# 무기 이동속도
weapon_speed=10

# 공 만들기 (4개 크기에 대해 따로 처리)
ball_images=[
    pygame.image.load(os.path.join(image_path,'ballon1.png')),
    pygame.image.load(os.path.join(image_path,'ballon2.png')),
    pygame.image.load(os.path.join(image_path,'ballon3.png')),
    pygame.image.load(os.path.join(image_path,'ballon4.png'))
]

# 공 크기에 따른 스피드
ball_speed_y = [-18, -15, -12, -9]

# 공 정보
balls = []

# 최초로 발생하는 큰 공
balls.append({
    'pos_x' : 50,
    'pos_y' : 50,
    'img_idx' : 0, # 공의 이미지 인덱스
    'to_x' : 3, # 공의 x축 이동방향
    'to_y': -6, # 공의 y축 이동방향
    'init_spd_y' : ball_speed_y[0] # y 최초 속도
})

# 사라질 무기, 공 정보 저장변수
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)
# 게임 시간
total_time = 100
start_tick = pygame.time.get_ticks() # 시작시간

# 게임종료 메시지 / 타임아웃 / 미션완료
game_result = 'Game Over'

#게임 시작 메시지
start='Game Start'




# 이벤트 루프
running=True #게임이 진행중인가

start_msg = game_font.render(start,True,(255,255,0))
start_msg_rect = start_msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(start_msg,start_msg_rect)
pygame.display.update()

pygame.time.delay(2000)

while running:
    dt=clock.tick(60) #게임화면의 초당 프레임수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    #print('fps : '+str(clock.get_fps())) #프레임 출력
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가
            running=False #게임 진행중이 아님
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: #캐릭터를 왼쪽으로
                character_to_x_LEFT -= character_speed
            elif event.key==pygame.K_RIGHT: #캐릭터를 오른쪽으로
                character_to_x_RIGHT += character_speed
            elif event.key==pygame.K_SPACE: #무기 발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                character_to_x_LEFT=0
            elif event.key == pygame.K_RIGHT:
                character_to_x_RIGHT=0

    # 3. 게임 캐릭터 위치 정의의
    character_x_pos += character_to_x_LEFT+character_to_x_RIGHT

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width

    # 무기 위치 조정
    weapons=[ [w[0],w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로

    # 천장에 닿은 무기 없애기
    weapons=[ [w[0],w[1]] for w in weapons if w[1] > 0] # y좌표가 0보다 큰 것만 리스트, 즉 천장에 닿는 순간 무기가 리스트에서 빠짐 

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls): # 리스트를 순회하며 몇 번째 인지 알려주며 해당하는 값을 가져옴 
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']

        ball_size = ball_images[ball_img_idx].get_rect().size # ball_img_idx에 해당하는 크기를 가져옴
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 공 가로 위치
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val['to_x'] = ball_val['to_x'] * -1 # 공이 벽에 닿았을 때 공 이동위치 변경
        
        # 공 세로 위치
        if ball_pos_y >= screen_height-stage_height-ball_height:
            ball_val['to_y'] = ball_val['init_spd_y'] #스테이지에 튕겨서 올라가는 처리
        else: # 그 외에는 속도를 증가
            ball_val['to_y'] += 0.5
        
        ball_val['pos_x'] += ball_val['to_x']
        ball_val['pos_y'] += ball_val['to_y']

    # 4. 충돌처리

    # 캐릭터 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls): # 리스트를 순회하며 몇 번째 인지 알려주며 해당하는 값을 가져옴 
        ball_pos_x = ball_val['pos_x']
        ball_pos_y = ball_val['pos_y']
        ball_img_idx = ball_val['img_idx']
        
        # 공 rect정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌체크
        if character_rect.colliderect(ball_rect):
            running = False
            break
        # 공과 무기 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons): # 리스트를 순회하며 몇 번째 인지 알려주며 해당하는 값을 가져옴 
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # 공과 무기 충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당무기 없애기 위한 값 설정
                ball_to_remove = ball_idx 

                # 가장 작은크기의 공이 아니라면 다음 단계의 공으로 나누기
                if ball_img_idx < 3:
                    # 현재 공 크기 정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]


                    #왼쪽으로 튕기는 공
                    balls.append({
                        'pos_x' : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        'pos_y' : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        'img_idx' : ball_img_idx + 1, # 공의 이미지 인덱스
                        'to_x' : -3, # 공의 x축 이동방향
                        'to_y': -6, # 공의 y축 이동방향
                        'init_spd_y' : ball_speed_y[ball_img_idx+1] # y 최초 속도
                        })
                    #오른쪽으로 튕기는 공
                    balls.append({
                        'pos_x' : ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        'pos_y' : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        'img_idx' : ball_img_idx + 1, # 공의 이미지 인덱스
                        'to_x' : 3, # 공의 x축 이동방향
                        'to_y': -6, # 공의 y축 이동방향
                        'init_spd_y' : ball_speed_y[0] # y 최초 속도
                        })

                break
        else: #계속 게임 진행
            continue #안쪽 for문 조건이 맞지않으면 continue
        break # 안쪽 for문에서 break를 만나면 실행 2중 for문 한번에 탈출

        # for 바깥조건:
            # 바깥동작
            # for 안쪽조건:
                # 안쪽동작
                # if 충돌:
                    # break
            # else:
                # continue
            # break

    # 충돌된 공 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove] 
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 모든 공을 없앤 경우 게임종료
    if len(balls)==0:
        game_result='Mission Complete'
        running=False

    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x=val['pos_x']
        ball_pos_y=val['pos_y']
        ball_img_idx=val['img_idx']
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    # 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000 # ms -> s
    timer = game_font.render('Time : {}'.format(int(total_time - elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))

    
    
    

    # 시간초과
    if total_time - elapsed_time <= 0:
        game_result = 'Time Over'
        running = False
    
    pygame.display.update() #게임화면 다시그리기
    


#게임오버 메시지
msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg,msg_rect)
pygame.display.update()

pygame.time.delay(2000)

#게임 종료
pygame.quit