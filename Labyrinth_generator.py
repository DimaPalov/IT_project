import tkinter as tk
import draw
import random

n,m = map(int,input().split())
root = tk.Tk()
root.title("Maze generator")
c = tk.Canvas(root, width = 1020, height=870, bg="tan")
c.grid()
draw.essentials(root,c,n,m)
nx = (n-abs(n%2-1))//2
ny = (m-abs(m%2-1))//2
graph = [[10**9]*nx*ny for x in range(nx*ny)]
for i in range(nx*ny):
    if i%nx-1>=0:
        graph[i][i-1]=random.randint(1,10)
    if i%nx+1<nx:
        graph[i][i+1]=random.randint(1,10)
    if i//nx-1>=0:
        graph[i][i-nx]=random.randint(1,10)
    if i//nx+1<ny:
        graph[i][i+nx]=random.randint(1,10)
#print(graph)
newgraph = [[10**9]*nx*ny for x in range(nx*ny)]
N = nx*ny
INF = 10**9
dist = [INF]*N 
dist[0] = 0 
used = [False]*N
beento = []
for i in range(N): 
    min_dist = INF 
    for j in range(N): 
        if not used[j] and dist[j] < min_dist: 
            min_dist = dist[j] 
            u = j
    mind = INF
    ans = 1
    for j in range(len(beento)):
        if graph[u][beento[j]]<mind:
            mind = graph[u][beento[j]]
            ans = beento[j]
    #print(ans,u)
    newgraph[ans][u] = 1
    used[u] = True
    beento.append(u)
    for v in range(N): 
        dist[v] = min(dist[v], graph[u][v])
#print(graph)
draw.graph(root,c,n,m,newgraph)
root.mainloop()
