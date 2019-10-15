import pygame
from collections import defaultdict
pygame.init()

GameMode = True
margin = 10
gap = 175
win = pygame.display.set_mode((560,560))
pygame.display.set_caption('MazeGeneration')
edges = list()
tree = defaultdict(list)
count = 0

#Generating Edges
for a in range(3):
    for b in range(3):
        tree[count].append((a,b))
        count +=1
        for c in range(-1,2):
            for d in range(-1,2):
                if abs(c) == abs(d) : continue
                flag = (a + c,b + d)
                if ((flag[0] >=0 and flag[0] <=2) and (flag[1] >=0 and flag[1] <=2)):
                    if [flag,(a,b)] in edges: continue
                    edges.append([(a,b),flag])
                    


while GameMode:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameMode = False
    color = (255,255,255)
    #pygame.draw.rect(win,color,((margin + gap)*0 + margin ,(margin + gap)*0 + margin ),gap,gap)


    for row in range(3):
        for column in range(3):
            pygame.draw.rect(win,color,((margin + gap)*column + margin,
                (margin + gap)*row + margin,
                gap,
                gap))
            pygame.display.update()
pygame.quit()
