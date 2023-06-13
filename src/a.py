import pygame
import numpy as np
 
pygame.init()
 
background = pygame.display.set_mode((550, 382)) # 배경 이미지에 맞추어 화면크기 설정함
pygame.display.set_caption('PYGAME_9')
 
# 이미지 파일 준비
image_bg = pygame.image.load('./image/fungo.png')
image_ball = pygame.image.load('./image/ball_small.png')
image_glove = pygame.image.load('./image/glove_small.png')
 
# 배경의 사이즈 가져오기
size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]
 
# glove의 사이즈 가져오기
size_glove_width = image_glove.get_rect().size[0]
size_glove_height = image_glove.get_rect().size[1]
 
# glove의 좌표값 설정하기
x_pos_glove = size_bg_width/2 - size_glove_width/2 # x좌표값 상 중앙
y_pos_glove = size_bg_height - size_glove_height # 맨 아래 (전체 높이에서 이미지 높이 만큼 뺀 값)
 
# 키보드 움직임에 의한 좌표 변수 (양 옆으로만 움직일 것이므로 x좌표만)
to_x = 0
 
# ball의 사이즈 가져오기 (가로, 세로)
size_ball_width = image_ball.get_rect().size[0]
size_ball_height = image_ball.get_rect().size[1]
 
# ball의 좌표값 설정하기
x_pos_ball = size_bg_width/2 - size_ball_width/2 # 가운데
y_pos_ball = 0 # 맨 위
 
# ball의 x,y 축 속도 변수 (좌표에 더해줄 목적)
x_speed_ball = 1
y_speed_ball = 1
 
# 점수 변수 추가 및 폰트 설정
score = 0
score_font = pygame.font.SysFont(None, 50)
 
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN: # 키보드가 눌렸을때
            if event.key == pygame.K_RIGHT:
                to_x = 1
            elif event.key == pygame.K_LEFT:
                to_x = -1
        if event.type == pygame.KEYUP: # 키보드를 뗐을때
            if event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_LEFT:
                to_x = 0
    
    # glove가 화면 밖으로 벗어나지 않도록 제한
    if x_pos_glove < 0:
        x_pos_glove = 0
    elif x_pos_glove > size_bg_width - size_glove_width:
        x_pos_glove = size_bg_width - size_glove_width
    else:
        x_pos_glove += to_x
        
    x_pos_ball += x_speed_ball
    y_pos_ball += y_speed_ball
        
    # x좌표값을 제한하고 speed변수를 음수로 바꿔 방향 전환하기
    if x_pos_ball <= 0:
        x_speed_ball = -x_speed_ball
        x_pos_ball = 0
    elif x_pos_ball >= size_bg_width - size_ball_width:
        x_speed_ball = -x_speed_ball
        x_pos_ball = size_bg_width - size_ball_width
        
    if y_pos_ball <= 0:
        y_speed_ball = -y_speed_ball
        y_pos_ball = 0
    elif y_pos_ball >= size_bg_height-size_ball_height:
        y_speed_ball = -y_speed_ball
        y_pos_ball = size_bg_height-size_ball_height
        
    # ball의 현재 위치를 업데이트 하기위해 이미지의 좌표를 불러와 업데이트
    rect_ball = image_ball.get_rect()
    # ball의 왼쪽 위 가장자리 좌표를 업데이트
    rect_ball.left = x_pos_ball
    rect_ball.top = y_pos_ball
    
    rect_glove = image_glove.get_rect()
    rect_glove.left = x_pos_glove
    rect_glove.top = y_pos_glove
    
    if rect_glove.colliderect(rect_ball): # 객체 충돌 시 랜덤한 곳에서 새로운 공 등장
        x_pos_ball = np.random.randint(550) # 배경화면의 가로길이(550) 중 랜덤한 정수 하나 반환
        y_pos_ball = 0 # 맨 위
        score += 1 # 점수 1점 추가
            
    # 이미지 삽입
    background.blit(image_bg, (0,0))
    background.blit(image_ball, (x_pos_ball, y_pos_ball))
    background.blit(image_glove, (x_pos_glove, y_pos_glove))
    
    # 점수 삽입
    score_text = score_font.render('점수 : {}'.format(str(score)), True, (255,255,255))
    background.blit(score_text, (10,10))
    pygame.display.update()
    
pygame.quit()
