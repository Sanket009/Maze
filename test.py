import random
from collections import defaultdict
edges = list()
tree = defaultdict(list)
count = 0

#Generating initial tree and edges
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
                    

randNums = list()
while len(tree) != 1:
    a = random.randint(0,(len(edges)-1))
    
    if a in randNums: continue
    for b in tree:
        for c in tree[b]:
            if c == edges[a][0]: 
                t1 = (b,c)
                break
            break
    for d in tree:
        for e in tree[d]:
            if e == edges[a][1]:
                t2 = (d,e,tree[d])
                break
            break
    if t1[0] == t2[1]: continue
    print(edges)
    for q in t2[2]:
        tree[t1[0]].append(q)
    tree.pop(t2[0],None)
    edges.pop(a)
    randNums.append(a)
    for k in tree:
        print(tree[k])
    print('\n')
    print(len(edges),len(tree) , a )

for key,value in tree.items():
    print(key , ':', value)
