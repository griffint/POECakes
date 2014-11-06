# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/griffint/.spyder2/.temp.py
"""

from TKinter import Tk,BOTH
from ttk import Frame, Button, Style

class Example(Frame):
    
    def __init__(self, parent):
        
        self.parent = parent 
        self.initUI():
            
    def initUI(self):
        
        self.parent.title("Cake Decorating")
        self.style = Style()
        self.style.theme_use("alt")
        
        self.pack(fill=BOTH, expand = 1)
        
        cakeUploadButton = Button(self, text="Upload Cake Design")
        cakeUploadButton.place(x=100,y=100)  
        
        
def main():
    root = Tk()
    root.geometry("1000x700+500+300")
    app =Example(root)
    root.mainloop()