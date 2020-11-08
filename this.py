import pygame
def draw_o(a,c):
    pygame.draw.rect(beginning, (200, 0, 0), (a+25, c+25, 50, 50))
def draw_x(a,c):
    pygame.draw.rect(beginning, (0, 0, 200), (a+25,c+25 , 50, 50))
def is_winning(payer):
    if b[0][0] == b[0][1] and b[0][0] == b[0][2] and b[0][0] == payer:
        return payer
    elif b[1][0] == b[1][1] and b[1][0] == b[1][2] and b[1][0] == payer:
        return payer
    elif b[2][0] == b[2][1] and b[2][0] == b[2][2] and b[2][0] ==payer:
        return payer
    elif b[0][0] == b[1][0] and b[0][0] == b[2][0] and b[0][0] ==payer:
        return payer
    elif b[0][1] == b[1][1] and b[0][1] == b[2][1] and b[0][1] ==payer:
        return payer
    elif b[0][2] == b[1][2] and b[0][2] == b[2][2] and b[0][2] == payer:
        return payer
    elif b[0][0] == b[1][1] and b[0][0] == b[2][2] and b[0][0] ==payer:
        return payer
    elif b[0][2] == b[1][1] and b[0][0] == b[2][0] and b[0][2] ==payer:
        return payer
    else:
        return 0
pygame.init()
start =1
position=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0],[0,0,0]]
one_two=1
beginning = pygame.display.set_mode((500, 500))
pygame.display.set_caption('X-O game')
for x in range(3):
    for y in range (3):
        position[x][y]= pygame.draw.rect(beginning, (0, 255, 20), (50 + 150 * x, 50+150*y, 100, 100))
while (start==1):
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             start =0
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = z = pygame.mouse.get_pos()
            #print(mouse)
            for x in range(3):
                for y in range(3):
                    if(z[0]>50 + 150 * x and z[0]<50 + 150 * x+100 and z[1]>50 + 150 * y and z[1]< 50 + 150 * y+100 and b[x][y]==0):
                        #print(here)
                        if(one_two==1):
                            draw_x(50 + 150 * x,50+150*y)
                            one_two=2
                            b[x][y] = 1
                        else:
                            draw_o(50 + 150 * x,50+150*y)
                            one_two=1
                            b[x][y] = 2
    pygame.display.update()

    z=is_winning(1)
    y=is_winning(2)
    if(z==1):
        print("player 1 wins")
        break
    elif(y==2):
        print("player 2 wins")
        break


if (is_winning(1)!=1 and is_winning(2)!=2):
    print("Nooo winner")
pygame.quit()