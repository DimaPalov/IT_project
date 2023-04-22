import tkinter as tk
import draw

n,m = map(int,input().split())
root = tk.Tk()
root.title("Labyrinth generator")
c = tk.Canvas(root, width = 1020, height=820, bg="tan")
c.grid()
draw.essentials(root,c,n,m)
root.mainloop()
