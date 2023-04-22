import tkinter as tk
import random

def essentials(root,c,n,m):
    drawFrame(c)
    n1 = 50/n
    m1 = 40/m
    edge = []
    for i in range(n):
        for j in range(m):
            if i%2==1 and j%2==1 and i!=n-1 and j!=m-1:
                drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*i,10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*j,min(n1,m1)*20)
            else:
                drawWallBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*i,10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*j,min(n1,m1)*20)
            if (i==0 or ((i==n-1 and n%2==1) or (i==n-2 and n%2==0)) or ((j==m-1 and m%2==1) or (j==m-2 and m%2==0)) or j==0) and (i%2==1 or j%2==1) and (i!=n-1 or j!=m-1 or i!=n-2 or j!=m-2):
                edge.append([i,j])
    start = random.choice(edge)
    finish = random.choice(edge)
    while start==finish:
        finish = random.choice(edge)
    print(start)
    print(finish)
    if start[0]==0:
        realstart = [start[0]+1,start[1]]
    elif start[0]==n-1 or start[0]==n-2:
        realstart = [start[0]-1,start[1]]
    if start[1]==0:
        realstart = [start[0],start[1]+1]
    elif start[1]==m-1 or start[1]==m-2:
        realstart = [start[0],start[1]-1]
    print(realstart)
    drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*start[0],10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20)
    if n%2==0 and ((start[0]==n-1 and n%2==1) or (start[0]==n-2 and n%2==0)):
        drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*start[1],min(n1,m1)*20)
    elif m%2==0 and ((start[1]==m-1 and m%2==1) or (start[1]==m-2 and m%2==0)):
        drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(start[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(start[1]+1),min(n1,m1)*20)
    drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*finish[0],10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20)
    if n%2==0 and ((finish[0]==n-1 and n%2==1) or (finish[0]==n-2 and n%2==0)):
        drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]+1),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*finish[1],min(n1,m1)*20)
    elif m%2==0 and ((finish[1]==m-1 and m%2==1) or (finish[1]==m-2 and m%2==0)):
        drawPathBlock(c,10+(1000-min(n1,m1)*20*n)//2+min(n1,m1)*20*(finish[0]),10+(800-min(n1,m1)*20*m)//2+min(n1,m1)*20*(finish[1]+1),min(n1,m1)*20)

def drawFrame(c):
    c.create_rectangle(0,0,10,820,fill="black")
    c.create_rectangle(1010,0,1020,820,fill="black")
    c.create_rectangle(0,0,1020,10,fill="black")
    c.create_rectangle(0,810,1020,820,fill="black")

def drawPathBlock(c,x,y,size):
    c.create_rectangle(x,y,x+size,y+size,fill="PaleGreen",outline="black")

def drawWallBlock(c,x,y,size):
    c.create_rectangle(x,y,x+size,y+size,fill="green",outline="black")    
