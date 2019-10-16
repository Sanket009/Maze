import pygame
import random
from collections import defaultdict
pygame.init()

GameMode = True
margin = 5
gap = 30
win = pygame.display.set_mode((600,600))
pygame.display.set_caption('MazeGeneration')
win.fill((255,255,255))
edges = list()
tree = defaultdict(list)
count = 0
randNums = list()

#Generating initial tree and edges
for a in range(20):
    for b in range(20):
        tree[count].append((a,b))
        count +=1
        for c in range(-1,2):
            for d in range(-1,2):
                if abs(c) == abs(d) : continue
                flag = (a + c,b + d)
                if ((flag[0] >=0 and flag[0] <=19) and (flag[1] >=0 and flag[1] <=19)):
                    if [flag,(a,b)] in edges: continue
                    edges.append([(a,b),flag])


for row in range(20):
    for column in range(20):
        color = (247,230,69)
        pygame.draw.rect(win,color,((gap)*column,
                (gap)*row,
                gap,
                gap))
        pygame.display.update() 

#Main Algorithm Goes here 
while len(tree) > 1:
    a = random.randint(0,(len(edges)-1))
    for b in tree:
        for c in tree[b]:
            if c == edges[a][0]: 
                t1 = (b,c)
                break
    for d in tree:
        for e in tree[d]:
            if e == edges[a][1]:
                t2 = (d,e,tree[d])
                break
    if t1[0] == t2[0]: continue
    print(edges[a])
    print('\n')
    for q in t2[2]:
        tree[t1[0]].append(q)
    tree.pop(t2[0],None)
    edges.pop(a)
    randNums.append(a)
'''    for k in tree:
        print(tree[k])
    
    print(len(edges),len(tree) , a )
    print('\n')
for key,value in tree.items():
    print(key , ':', value)

print(edges)
'''
while GameMode:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameMode = False
    for a in edges:
        color = (0,0,0)
        row = a[0][0]
        column = a[0][1]
        if abs(a[0][0] - a[1][0]) == 1:

            pygame.draw.rect(win,color,((gap)*column ,
                (gap)*row ,
                30,
                5))
            pygame.display.update()

        elif abs(a[0][1] - a[1][1]) == 1:
            pygame.draw.rect(win,color,((gap)*column,
                (gap)*row,
                5,
                30))
            pygame.display.update()
            
pygame.quit()
