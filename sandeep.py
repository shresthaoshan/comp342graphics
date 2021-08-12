import pygame
wn_height = 500
wn_width = 500

Black = (0,0,0)
Blue = (0,0,255)
cyan = (0,255,255)
Green= (0,255,0)
purple = (255,0,255)
Red= (255,0,0)
white = (255,255,255)
  
pygame.init()
screen = pygame.display.set_mode((wn_width, wn_height))
screen.fill((0,0,0))
pygame.display.set_caption("Liang Line Clipping ALgorithm")
    
# windows coordinates

def line(x1, y1, x2, y2):
	pygame.draw.line(screen,white,(x1,y1),(x2,y2))

def liangBarsky(x1,y1,x2,y2):
    xmin=20
    xmax=300
    ymin=20
    ymax=300
    #our main clipping window 
    line(xmin,ymin, xmax,ymin)
    line(xmax,ymin, xmax,ymax)
    line(xmin,ymin, xmin,ymax)
    line(xmin,ymax, xmax,ymax)
 
    # x1,y1 = (10,10)
    # x2,y2 = (400,160)
   
    dx = x2 - x1
    dy = y2 - y1
    p = [ -dx, dx, -dy, dy]
    q = [x1-xmin, xmax-x1, y1 - ymin, ymax - y1]

    for i in range(4):
        if(p[i] == 0):
            print('line is parallel to ' + i + 'th boundary')
            if(q[i] >= 0 ):
                if(i <2):
                    if (y1 < ymin):
                        y1 = ymin
                    if(y2 > ymax):
                        y2 = ymax
                    pygame.draw.line(screen,white,(x1,y1),(x2,y2))
                if (i>1):
                    if (x1 < xmin):
                        x1 = xmin
                    if (x2 > xmax):
                        x2 = xmax
                    pygame.draw.line(screen,white,(x1,y1),(x2,y2))
    
    t1,t2 = (0,1)

    for i in range(4):
        t = q[i]/p[i]
        if(p[i] < 0):
            if (t1 <= t):
                t1 = t
        else:
            if(t2 > t):
                t2 = t   
    if(t1 < t2):
        xx1 = x1 + t1 * p[1]

        xx2 = x1 + t2 * p[1]

        yy1 = y1 + t1 * p[3]

        yy2 = y1 + t2 * p[3]
        
        # line(xx1, yy1, xx2, yy2)
        pygame.draw.line(screen,Blue,(xx1,yy1),(xx2,yy2))  
        
liangBarsky(10,10,400,160)
liangBarsky(400,160,10,110)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()