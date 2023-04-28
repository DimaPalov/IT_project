import tkinter as tk
import draw
import random

n = 0
m = 0
s = 0
f = 0
graph = []
def createGraph():
    nx = (n-abs(n%2-1))//2
    ny = (m-abs(m%2-1))//2
    graph = [[10**9]*nx*ny for x in range(nx*ny)]
    for i in range(nx*ny):
        if i%nx-1>=0:
            xxx=random.randint(1,10)
            graph[i][i-1]=xxx
            graph[i-1][i]=xxx
        if i%nx+1<nx:
            xxx=random.randint(1,10)
            graph[i][i+1]=xxx
            graph[i+1][i]=xxx
        if i//nx-1>=0:
            xxx=random.randint(1,10)
            graph[i][i-nx]=xxx
            graph[i-nx][i]=xxx
        if i//nx+1<ny:
            xxx=random.randint(1,10)
            graph[i][i+nx]=xxx
            graph[i+nx][i]=xxx
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
        beento.append(u)
        mind = INF
        ans = -1
        for j in range(len(beento)):
            if graph[u][beento[j]]<mind:
                mind = graph[u][beento[j]]
                ans = beento[j]
        if ans!=-1:
            newgraph[ans][u] = 1
            newgraph[u][ans] = 1
        used[u] = True
        for v in range(N): 
            dist[v] = min(dist[v], graph[u][v])
    return newgraph

def onClickCreate():
    global s
    global f
    global graph
    if n>0 and m>0:
        draw.deleteAll(c)
        sf = draw.essentials(root,c,n,m)
        s = sf[0]
        f = sf[1]
        graph = createGraph()
        draw.graph(root,c,n,m,graph)

def onClickSave():
    pass

def onClickOpen():
    pass

def onClickSolve():
    if n!=0 and m!=0:
        nx = (n-abs(n%2-1))//2
        ny = (m-abs(m%2-1))//2
        N = nx*ny
        INF = 10**9;
        predki = [-1]*N
        dist = [INF]*N
        used = [0]*N
        min_v = -1
        min_w = INF
        dist[s[2]] = 0
        G = []
        for i in range(N):
            mas = []
            for j in range(N):
                p = [j,graph[i][j]]
                if p[1]==10**9:
                    p[1] = -1
                if i!=j and p[1]>=0:
                    mas.append(p)
            G.append(mas)
        for _ in range(N):
            min_w=INF
            for i in range(N):
                if used[i]==0:
                    if dist[i]<min_w:
                        min_w = dist[i]
                        min_v = i
            used[min_v] = 1
            for p in G[min_v]:
                v = p[0]
                w = p[1]
                if used[v]==0:
                    thing = dist[v]
                    dist[v] = min(dist[v],dist[min_v]+w)
                    if dist[v]!=thing:
                        predki[v]=min_v
        path = []
        i=f[2]
        while predki[i]!=-1:
            path.append(i)
            i=predki[i]
        path.append(i);
        draw.path(root,c,n,m,s,f,path)

def main():
    global n
    global m
    if width.get().strip().isdigit() and height.get().strip().isdigit() and int(width.get().strip())>4 and int(height.get().strip())>4:
        n = int(width.get().strip())
        m = int(height.get().strip())
    root.after(1,main)

root = tk.Tk()
root.title("Maze generator")
c = tk.Canvas(root, width = 1020, height=870, bg="tan")
c.grid()
draw.frame(c)
#Buttons------------------------------------------------------------------------------------------------------
create = tk.Button(root,text="Generate maze",bg = "tan",activebackground = "tan",command=onClickCreate)
create.place(x=14,y=823)
save = tk.Button(root,text="Save maze",bg = "tan",activebackground = "tan",command=onClickSave)
save.place(x=760,y=823)
save = tk.Button(root,text="Open maze",bg = "tan",activebackground = "tan",command=onClickOpen)
save.place(x=882,y=823)
solve = tk.Button(root,text="Show solution",bg = "tan",activebackground = "tan",command=onClickSolve)
solve.place(x=610,y=823)
#Entries------------------------------------------------------------------------------------------------------
c.create_text(250, 840,font='Arial 10',fill='black',text=("Width of the maze:"))
width = tk.Entry(root,bg = "white",width = 5)
width.place(x=320,y=827)
c.create_text(465, 840,font='Arial 10',fill='black',text=("Height of the maze:"))
height = tk.Entry(root,bg = "white",width = 5)
height.place(x=540,y=827)
#Main---------------------------------------------------------------------------------------------------------
main()
root.mainloop()
