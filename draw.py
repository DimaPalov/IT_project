import tkinter as tk
import random

everything = []

def essentials(root,c,n,m,start=-1,finish=-1): #draws frame and some parts of the maze
    frame(c)
    n1 = 50/n
    m1 = 40/m
    nx = (n-abs(n%2-1))//2
    ny = (m-abs(m%2-1))//2
    edge = []
    for i in range(n):
        for j in range(m):
            if i%2==1 and j%2==1 and i!=n-1 and j!=m-1:
                thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*i,10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*j,min(n1,m1)*20)
                if (i==1 or j==1 or ((i==n-2 and n%2==1) or (i==n-3 and n%2==0)) or ((j==m-2 and m%2==1) or (j==m-3 and m%2==0))):
                    edge.append([i,j,(j//2)*nx+i//2])
            else:
                thing = drawWallBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*i,10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*j,min(n1,m1)*20)
            everything.append(thing)
    if start==-1 and finish==-1:
        start = random.choice(edge)
        finish = random.choice(edge)
        while start==finish:
            finish = random.choice(edge)
    drawExit(c,n,m,start,finish)
    return [start,finish]

def graph(root,c,n,m,graph): #draws the maze
    n1 = 50/n
    m1 = 40/m
    nx = (n-abs(n%2-1))//2
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j]!=10**9:
                if i-1==j:
                    y = (i//nx)*2 +1
                    x = (i%nx)*2 
                elif i+1==j:
                    y = (i//nx)*2 +1
                    x = (i%nx)*2 +2
                elif i<j:
                    y = (i//nx)*2 +2
                    x = (i%nx)*2 +1
                elif i>j:
                    y = (i//nx)*2
                    x = (i%nx)*2 +1
                thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(x),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(y),min(n1,m1)*20)
                everything.append(thing)

def path(root,c,n,m,s,f,path):
    drawExit(c,n,m,s,f,color="red")
    n1 = 50/n
    m1 = 40/m
    nx = (n-abs(n%2-1))//2
    thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*((path[0]%nx)*2 +1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*((path[0]//nx)*2 +1),min(n1,m1)*20,color="red")
    everything.append(thing)
    for i in range(1,len(path)):
        if path[i]-1==path[i-1]:
            y = (path[i]//nx)*2 +1
            x = (path[i]%nx)*2 
        elif path[i]+1==path[i-1]:
            y = (path[i]//nx)*2 +1
            x = (path[i]%nx)*2 +2
        elif path[i]<path[i-1]:
            y = (path[i]//nx)*2 +2
            x = (path[i]%nx)*2 +1
        elif path[i]>path[i-1]:
            y = (path[i]//nx)*2
            x = (path[i]%nx)*2 +1
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(x),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(y),min(n1,m1)*20,color="red")
        everything.append(thing)
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*((path[i]%nx)*2 +1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*((path[i]//nx)*2 +1),min(n1,m1)*20,color="red")
        everything.append(thing)
        
    
def frame(c): #draws the frame
    c.create_rectangle(0,0,10,870,fill="black")
    c.create_rectangle(1010,0,1020,870,fill="black")
    c.create_rectangle(0,0,1020,10,fill="black")
    c.create_rectangle(0,860,1020,870,fill="black")
    c.create_rectangle(0,810,1020,820,fill="black")

def drawPathBlock(c,x,y,size,color="PaleGreen"): #draws a path square
    thing = c.create_rectangle(x,y,x+size,y+size,fill=color,outline="black")
    return thing

def drawWallBlock(c,x,y,size): #draws a wall square
    thing = c.create_rectangle(x,y,x+size,y+size,fill="green",outline="black")
    return thing

def deleteAll(c): #deletes every element of previous maze
    global everything
    for item in everything:
        c.delete(item)
    everything = []

def drawExit(c,n,m,start,finish,color="PaleGreen"): #draws exits of the maze
    n1 = 50/n
    m1 = 40/m
    if start[0]==1:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]-1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20,color=color)
    elif start[0]==n-2:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20,color=color)
    elif start[0]==n-3:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20,color=color)
        everything.append(thing)
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]+2),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20,color=color)
    elif start[1]==1:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(start[1]-1),min(n1,m1)*20,color=color)
    elif start[1]==m-2:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(start[1]+1),min(n1,m1)*20,color=color)
    elif start[1]==m-3:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(start[1]+1),min(n1,m1)*20,color=color)
        everything.append(thing)
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(start[1]+2),min(n1,m1)*20,color=color)
    everything.append(thing)
    if finish[0]==1:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]-1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20,color=color)
    elif finish[0]==n-2:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20,color=color)
    elif finish[0]==n-3:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20,color=color)
        everything.append(thing)
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]+2),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20,color=color)
    elif finish[1]==1:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(finish[1]-1),min(n1,m1)*20,color=color)
    elif finish[1]==m-2:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(finish[1]+1),min(n1,m1)*20,color=color)
    elif finish[1]==m-3:
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(finish[1]+1),min(n1,m1)*20,color=color)
        everything.append(thing)
        thing = drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(finish[1]+2),min(n1,m1)*20,color=color)
    everything.append(thing)
