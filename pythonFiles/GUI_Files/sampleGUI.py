# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/griffint/.spyder2/.temp.py
"""
from Tkinter import *

root = Tk()

root.title("Simple Graph")

root.resizable(0,0)

points = []

spline = 0

tag1 = "theline"

def point(event):
	c.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black")
	points.append(event.x)
	points.append(event.y)
	return points

def canxy(event):
	print event.x, event.y

def graph(event):
	global theline
	c.create_line(points, tags="theline")
	

def toggle(event):
	global spline
	if spline == 0:
		c.itemconfigure(tag1, smooth=1)
		spline = 1
	elif spline == 1:
		c.itemconfigure(tag1, smooth=0)
		spline = 0
	return spline


c = Canvas(root, bg="white", width=600, height= 600)

c.configure(cursor="crosshair")

c.pack()

widget = Button( text="Upload to Cakebot")
widget.pack(side=LEFT)

widget = Button( text="Start a new drawing")
widget.pack(side=LEFT)

widget = Button( text="Upload a design")
widget.pack(side=RIGHT)

c.bind("<Button-1>", point)

c.bind("<Button-3>", graph)

c.bind("<Button-2>", toggle)

root.mainloop()