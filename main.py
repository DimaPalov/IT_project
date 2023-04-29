import tkinter as tk
import draw
import random
import struct
import math

n = 0
m = 0
s = 0
f = 0
graph = []
everything = []
other = []

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
    global n
    global m
    if width.get().strip().isdigit() and height.get().strip().isdigit() and int(width.get().strip())>4 and int(height.get().strip())>4:
        n = int(width.get().strip())
        m = int(height.get().strip())
    if n>0 and m>0:
        draw.deleteAll(c)
        sf = draw.essentials(root,c,n,m)
        s = sf[0]
        f = sf[1]
        graph = createGraph()
        draw.graph(root,c,n,m,graph)

def Open():
    global s
    global f
    global n
    global m
    global graph
    global everything
    global other
    name = other[0].get()
    with open("data/"+name+".maze", 'rb') as file:
        for i in range(4):
            data = file.read(1)
            s = struct.unpack('<B', data)
        size = file.read(4)
        size = struct.unpack('<i', size)[0]-40
        start = file.read(4)
        s1 = struct.unpack('<i',start)[0]
        start = file.read(4)
        s2 = struct.unpack('<i',start)[0]
        start = file.read(4)
        s3 = struct.unpack('<i',start)[0]
        finish = file.read(4)
        f1 = struct.unpack('<i',finish)[0]
        finish = file.read(4)
        f2 = struct.unpack('<i',finish)[0]
        finish = file.read(4)
        f3 = struct.unpack('<i',finish)[0]
        n1 = file.read(4)
        n = struct.unpack('<i',n1)[0]
        m1 = file.read(4)
        m = struct.unpack('<i',m1)[0]
        s = [s1,s2,s3]
        f = [f1,f2,f3]
        graph = [[10**9]*int(math.sqrt(size)) for x in range(int(math.sqrt(size)))]
        for i in range(int(math.sqrt(size))):
            for j in range(int(math.sqrt(size))):
                data = file.read(1)
                num = struct.unpack('<B',data)[0]
                if num==255:
                    graph[i][j]=10**9
                else:
                    graph[i][j] = num
        draw.deleteAll(c)
        draw.essentials(root,c,n,m,s,f)
        draw.graph(root,c,n,m,graph)
    for item in everything:
        c.delete(item)
    everything = []
    for item in other:
        item.destroy()
    other = []

def onClickOpen():
    global everything
    global other
    for item in everything:
        c.delete(item)
    everything = []
    for item in other:
        item.destroy()
    other = []
    thing = c.create_rectangle(360,300,660,450,fill="Wheat",outline="black")
    text = c.create_text(510, 320,font='Arial 10',fill='black',text=("Write the name of the maze:"))
    entry = tk.Entry(root,bg = "white",width = 20)
    entry.place(x=397,y=350)
    send = tk.Button(root,text="Open maze",bg = "tan",activebackground = "tan",command=Open)
    send.place(x=388,y=400)
    cancell = tk.Button(root,text="Cancel",bg = "tan",activebackground = "tan",command=Cancel)
    cancell.place(x=545,y=400)
    everything = [thing,text]
    other = [entry,send,cancell]
    
def Save():
    global everything
    global other
    name = other[0].get()
    nx = (n-abs(n%2-1))//2
    ny = (m-abs(m%2-1))//2
    with open("data/"+name+".maze", 'wb') as file:
        m1 = struct.pack('<B',ord("m"))
        a1 = struct.pack('<B',ord("a"))
        z1 = struct.pack('<B',ord("z"))
        e1 = struct.pack('<B',ord("e"))
        file.write(m1)
        file.write(a1)
        file.write(z1)
        file.write(e1)
        size = struct.pack('<i', 40+nx*ny*nx*ny)
        file.write(size)
        start = struct.pack('<i',s[0])
        file.write(start)
        start = struct.pack('<i',s[1])
        file.write(start)
        start = struct.pack('<i',s[2])
        file.write(start)
        finish = struct.pack('<i',f[0])
        file.write(finish)
        finish = struct.pack('<i',f[1])
        file.write(finish)
        finish = struct.pack('<i',f[2])
        file.write(finish)
        n1 = struct.pack('<i',n)
        file.write(n1)
        m1 = struct.pack('<i',m)
        file.write(m1)
        for i in range(nx*ny):
            for j in range(nx*ny):
                if graph[i][j]==10**9:
                    num = struct.pack('<B',255)
                else:
                    num = struct.pack('<B',graph[i][j])
                file.write(num)
    for item in everything:
        c.delete(item)
    everything = []
    for item in other:
        item.destroy()
    other = []

def Cancel():
    global everything
    global other
    for item in everything:
        c.delete(item)
    everything = []
    for item in other:
        item.destroy()
    other = []
    
def onClickSave():
    global everything
    global other
    for item in everything:
        c.delete(item)
    everything = []
    for item in other:
        item.destroy()
    other = []
    thing = c.create_rectangle(360,300,660,450,fill="Wheat",outline="black")
    text = c.create_text(510, 320,font='Arial 10',fill='black',text=("Write the name of the maze:"))
    entry = tk.Entry(root,bg = "white",width = 20)
    entry.place(x=397,y=350)
    send = tk.Button(root,text="Save maze",bg = "tan",activebackground = "tan",command=Save)
    send.place(x=388,y=400)
    cancell = tk.Button(root,text="Cancel",bg = "tan",activebackground = "tan",command=Cancel)
    cancell.place(x=545,y=400)
    everything = [thing,text]
    other = [entry,send,cancell]

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

root = tk.Tk()
root.title("Maze generator")
c = tk.Canvas(root, width = 1020, height=870, bg="Wheat")
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
root.mainloop()
