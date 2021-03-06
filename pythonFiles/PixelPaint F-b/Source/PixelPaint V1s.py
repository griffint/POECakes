#Programmed by pie
#(Tediously) Commented by pie 
#If you are new to pygame or python, read over this program and try to learn something from it

#I give anyone permission modify this code as long as they don't distribute their modified version.
#Anyone can distribute this code as long as they do not claim it as their own.
#|_()|_
#Y('o')Y

#Customised for POE use by Griffin Tschurwald. Thank you pie for the base code!

import pygame, sys, easygui, os

#print pygame.version.ver
fill = False#Remove me!

#Variable storer---------------------------------------------------------------
class storer():
    def __init__(self, newone):#Define all the variables
        self.new = newone #New is the size of the picture
        self.color = [0, 0, 0] #Color is a set of RGB Values
        self.bsize = 5
        self.brushsize = "Small" #Brush size
        self.brush = "Square" #Brush shape
        self.down = False #Bool of whether left mouse button is down
        self.down2 = False #Bool of whether right mouse button is down
        self.loadpic = False #Bool of whether the user is loading a pic, or starting a new one
        self.imagename = "New File"#String of the save location, including extension. used in the caption
        self.saved = True#Bool of whether there have been changes since te last save
        self.bgcolor = [255, 255, 255]#Set of RGB values of the background. Currently not really that useful. ROFL!
        self.toolname = "Basic Drawing"
        self.dropper = False
        self.texton = False
        self.mousepos = [0, 0]
        self.fillcolor = [255, 255, 255]
        self.line = False
        self.linepos = 1
        self.poly = False
        self.pointlist = []
        self.color2 = [255, 255, 255]
        self.dropper2 = False
        self.color3 = [255, 255, 255]
        self.dropper3 = False
        self.color4 = [255, 255, 255]
        self.dropper4 = False
        self.color5 = [255, 255, 255]
        self.dropper5 = False
        self.selectable = [self.dropper5, self.dropper4, self.dropper3, self.dropper2, self.dropper, self.poly, self.line, self.texton, ]
#Color chooser-----------------------------------------------------------------
    def choosecolor(self):
        short = easygui.buttonbox("Would you like to choose a color off a list, or define your own color", title = "Colors", choices = ["List", "Define", "Cancel"])
        if short == "List":
            newcolor = easygui.choicebox("Which color would you like?", title = "Color Menu", choices = ["Red", "Blue", "Brown", "Yellow", "Green", "Purple", "Orange", "Black"])
            #List of colors----------------------------------------------------
            if newcolor == "Red":
                self.color = [255, 0, 0]
            elif newcolor == "Black":
                self.color = [0, 0, 0]
            elif newcolor == "Green":
                self.color = [0, 255, 0]
            elif newcolor == "Blue":
                self.color = [0, 0, 255]
            elif newcolor == "Purple":
                self.color = [148, 0, 160]
            elif newcolor == "Orange":
                self.color = [255, 118, 0]
            elif newcolor == "Yellow":
                self.color = [255, 255, 0]
            elif newcolor == "Brown":
                self.color = [124, 78, 38]
            elif newcolor == None:
                self.choosecolor()
        elif short == "Define":
            msg = "Enter the Red, Green, and Blue values of your color"
            title = "Advanced Color Menu"
            fieldNames = ["Red","Green", "Blue"]
            fieldValues = []
            fieldValues = easygui.multenterbox(msg, title, fieldNames)
            if fieldValues == None:
                self.choosecolor()
            else:
                print fieldValues    
                if '' in fieldValues:
                    easygui.msgbox("All fields must be filled", title = "Input Error")
                else:    
                    if int(fieldValues[0]) > 255 or int(fieldValues[0]) < 0 or int(fieldValues[1]) > 255 or int(fieldValues[1]) < 0 or int(fieldValues[2]) > 255 or int(fieldValues[2]) < 0:
                        easygui.msgbox("All RGB values must be between 0 and 255", title = "Input Error")
                    else:
                        self.color = [int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2])]
        else:
            pass
#Brush Chooser-----------------------------------------------------------------
    def brushchooser(self):
        newbrush = easygui.buttonbox("Which brush would you like?", title = "Brush Menu", choices = ["Big", "Medium", "Small", "Custom", "Cancel"])
        if newbrush == "Cancel":
            pass
        else:
            if newbrush == "Custom":
                newnewbrush = easygui.enterbox("Enter the brush size as a number.", title = "Custom Brush Menu")
                if newnewbrush == None:
                    self.brushchooser()
                else:
                    self.bsize = int(newnewbrush)
            elif newbrush == "Big":
                self.bsize = 25
            elif newbrush == "Medium":
                self.bsize = 15
            elif newbrush == "Small":
                self.bsize = 5
    
    def save(self):
        extensionchoice = easygui.buttonbox("Which file extension would you like to use?", title = 'Select a file extension', choices = ["Bitmap {.bmp}", "Targa {.tga}"])
        if extensionchoice == "Bitmap {.bmp}":
            extension = ".bmp"
        elif extensionchoice == "Targa {.tga}":
            extension = ".tga"
        savelocation = easygui.filesavebox()
        if savelocation == None:
            pass
        else:
            savelocation = os.path.splitext(savelocation)[0]
            pygame.image.save(drawspace, savelocation + extension)
            self.imagename = savelocation + extension
            pygame.display.set_caption("PixelPaint - " + store.imagename)
            self.saved = True
    
    def mainmenu(self):
        menuchoice = easygui.choicebox("Select a task", title = "Main Menu", choices = ["Change Color", "Change Brush", "Save", "Open", "Help", "Tool Menu"])
        if menuchoice == "Save":
            self.save()
        elif menuchoice == "Help":
            easygui.textbox("Help:", title = "Help", text = open("helptext.txt", "r"))
        elif menuchoice == "Change Brush":
            self.brushchooser()
        elif menuchoice == "Change Color":
            self.choosecolor()
        elif menuchoice == "Tool Menu":
            self.toolmenu()
        elif menuchoice == "Open":
            store.loadpic = True
            question = easygui.fileopenbox()
            if question == None:
                self.mainmenu()
            else:
                try:
                    store.pic = pygame.image.load(question)
                    store.new = store.pic.get_size()
                    screen = pygame.display.set_mode([store.new[0]+100, store.new[1]])
                    screen.fill([230, 230, 230])
                    drawspace = pygame.surface.Surface(store.new)
                    drawspace.fill(store.bgcolor)
                except:
                    easygui.msgbox("Not a supported file type. Supported file types are: .jpg, .gif, .png, .bmp, .tga, .pcx, .lbm, .xpm, and  .tif. Please select a different file.", title = "Open Error")
                    self.mainmenu()
    
    def toolmenu(self):
        toolmenu = easygui.buttonbox("Select which tool you want. You are currently using: " + store.toolname, title = "Tool Menu", choices = ["Toggle Color Picker", "Toggle Text Tool", "Toggle Polygon Tool", "No tool", "Cancel"])
        if toolmenu == "No tool":
            self.dropper = False
            self.texton = False
            self.poly = False
            self.toolname = "Basic Drawing"
        elif toolmenu == "Toggle Color Picker":
            self.dropper = True
            self.texton = False
            self.poly = False
            self.toolname = "Color Picker"
        elif toolmenu == "Toggle Text Tool":
            self.texton = True
            self.dropper = False
            self.poly = False
            self.toolname = "Text Tool"
        elif toolmenu == "Toggle Polygon Tool":
            self.poly = True
            self.texton = False
            self.picker = False
            self.toolname = "Polygon Tool"
            
    def drawtext(self):
        self.mousepos = pygame.mouse.get_pos()
        size = easygui.integerbox("Enter the size you want your text:", title = 'Text Tool')
        print size
        if size == None:
            return
        text = easygui.enterbox("What text would you like printed?", title = 'Text Tool')
        print text
        if text == None or text == "":
            return
        Font =  pygame.font.Font("resources/annifont.TTF", size)#From fontfile
        drawtext = Font.render(text, True, self.color)
        print Font.size(text)
        drawspace.blit(drawtext, [self.mousepos[0] - Font.size(text)[0]/2, self.mousepos[1] - Font.size(text)[1]/2])
        self.saved = False
        
    def drawline(self, point_one, point_two, width):
        pygame.draw.line(drawspace, self.color, point_one, point_two, width)
    def deselectall(self):
        for item in self.selectable:
            #print item
            item = False
            #print item
        self.dropper5 = False
        self.dropper4 = False
        self.dropper3 = False
        self.dropper2 = False 
        self.dropper = False
        self.poly = False 
        self.line = False
        self.texton = False
        
msg = "Enter the height and width of your picture"
title = "New file"
fieldNames = ["Height","Width"]
fieldValues = []

store = storer([])#Creates a variable storing object to holds lot of stuff

def newfile():
    store.loadpic = False
    open_or_new = easygui.buttonbox("Welcome to PixelPaint", title = "PixelPaint", choices = ["New File", "Open", "Exit"])
    if open_or_new == "New File":
        store.loadpic = False
        fieldValues = easygui.multenterbox(msg, title, fieldNames)
        if fieldValues == None:
            newfile()
        else:
            try:
                store.new = [int(fieldValues[1]), int(fieldValues[0])]
            except:
                easygui.msgbox("All fields must be filled with whole numbers", title = "Input error")
                newfile()
    elif open_or_new == "Open":
        store.loadpic = True
        question = easygui.fileopenbox()
        if question == None:
            newfile()
        else:
            try:
                store.pic = pygame.image.load(question)
                store.new = store.pic.get_size()
                store.imagename = question
            except:
                easygui.msgbox("Not a supported file type. Supported file types are: .jpg, .gif, .png, .bmp, .tga, .pcx, .lbm, .xpm, and  .tif. Please select a different file.", title = "Open Error")
                newfile()
    elif open_or_new == "Exit":
        sys.exit()

#Sets up the entire program----------------------------------------------------
newfile()
pygame.init()
#Gets the icon and sets it
#pygame.display.set_icon(pygame.image.load("resources/icon.gif"))
#Makes the window and sets the size
if store.new[1] < 300:
    screen = pygame.display.set_mode([store.new[0]+245, store.new[1] + 300 - store.new[1]])
else:
    screen = pygame.display.set_mode([store.new[0]+245, store.new[1]])
screen.fill([230, 230, 230])
drawspace = pygame.surface.Surface(store.new)
drawspace.fill(store.bgcolor)
#If the user decided to load a picture, copy it to the screen
if store.loadpic == True:
    drawspace.blit(store.pic, [0, 0])
#Sets the caption
pygame.display.set_caption("PixelPaint - Press 'h' or go to the assistant for help - " + store.imagename)
#Creates the clock object
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 25)
backimage = pygame.image.load("resources/back.gif")
brushbox = pygame.image.load("resources/brush.gif")
colortext = pygame.image.load("resources/color.gif")
toolbox = pygame.image.load("resources/tools.gif")
menubox = pygame.image.load("resources/menu.gif")
pallette1 = pygame.image.load("resources/pallette1.gif")
paintbox = pygame.image.load("resources/buckets.gif")

#The main loop-----------------------------------------------------------------
while 1:
    clock.tick(30)
    #Checks for events---------------------------------------------------------
    for event in pygame.event.get():
        # if they want to exit, let them exit
        if event.type == pygame.QUIT:
            if store.saved == False:
                exiting = easygui.buttonbox("You have unsaved changes. Quit anyway?", title = 'Unsaved work', choices = ["Yes", "No"])
                if exiting == "Yes":
                    sys.exit()
            else:
                sys.exit()
        elif event.type == pygame.USEREVENT:
            if store.down:
                testoldpos = testpos
                testpos = pygame.mouse.get_pos()
                store.drawline(testoldpos, testpos, store.bsize)
        #Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:#Save menu
                store.save()
                
            elif event.key == pygame.K_c:#Color chooser
                store.choosecolor()
            elif event.key == pygame.K_b:#Brush chooser
                store.brushchooser()
            
            #can't seem to access helptext.txt
            #elif event.key == pygame.K_h:#Help menu
             #   easygui.textbox("Help:", title = "Help", text = open("helptext.txt", "r"))
                
            elif event.key == pygame.K_m:#Main menu
                store.mainmenu()
                
            elif event.key == pygame.K_w:#Random key
                random = easygui.enterbox("Enter your random word", title = "Random Menu")
                if random == None:
                    pass
                elif random == "pie is good":
                    easygui.msgbox("Thanks")
                elif random == "python":
                    pythonlogo = pygame.image.load("resources/file.png")
                    drawspace.blit(pythonlogo, [0,0])
                elif random == "rot":
                    if store.new[0] == store.new[1]:
                        drawspace = pygame.transform.rotate(drawspace, 90)
                    else:
                        easygui.msgbox("This function rotates your image. It is only useable on square images. Sorry!")
                elif random == "scale":
                    temp = pygame.transform.scale(drawspace, [100, 100])
                    drawspace.fill([150, 150, 150])
                    drawspace.blit(temp, [0, 0])
                elif random == "fill":
                    fill = not fill
                elif random == "line":
                    store.line = not store.line
                elif random == "average":
                    store.color = pygame.transform.average_color(drawspace)
                elif random == "polygon":
                    store.poly = not store.poly
                elif random == "Full":
                    pygame.display.set_mode([store.new[0]+245, store.new[1]], pygame.FULLSCREEN)
            elif event.key == pygame.K_n:
                if store.poly == True:
                    store.pointlist = []
            elif event.key == pygame.K_F1:
                if store.dropper2:
                    store.deselectall()
                else:
                    store.deselectall()
                    store.dropper2 = True
                print store.dropper2
                print store.dropper3
                print store.dropper4
                print store.dropper5
            elif event.key == pygame.K_F2:
                if store.dropper3:
                    store.deselectall()
                else:
                    store.deselectall()
                    store.dropper3 = True
                print store.dropper2
                print store.dropper3
                print store.dropper4
                print store.dropper5
            elif event.key == pygame.K_F3:
                if store.dropper4:
                    store.deselectall()
                else:
                    store.deselectall()                    
                    store.dropper4 = True
                print store.dropper2
                print store.dropper3
                print store.dropper4
                print store.dropper5
            elif event.key == pygame.K_F4:
                if store.dropper5:
                    store.deselectall()
                else:
                    store.deselectall()
                    store.dropper5 = True
                print store.dropper2
                print store.dropper3
                print store.dropper4
                print store.dropper5
                        
        #the actual drawing that happens when people hold the mouse down                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] < store.new[0]:
                if store.dropper:
                    store.color = drawspace.get_at(pygame.mouse.get_pos())
                elif store.dropper2:
                    store.color2 = drawspace.get_at(pygame.mouse.get_pos())
                elif store.dropper3:
                    store.color3 = drawspace.get_at(pygame.mouse.get_pos())
                elif store.dropper4:
                    store.color4 = drawspace.get_at(pygame.mouse.get_pos())
                elif store.dropper5:
                    store.color5 = drawspace.get_at(pygame.mouse.get_pos())
                
                elif store.texton:
                    store.drawtext()
                elif fill == True:
                    pixelgrid = pygame.surfarray.array3d(drawspace)
                    #print pixelgrid
                    for i in range(0, len(pixelgrid)):
                        print i
                        for j in range(0, len(pixelgrid[i])):
                            if pixelgrid[i][j] == [255, 255, 255]:
                                print "happy"
                                print
                            else:
                                print j
                            
                    #for pixel in pixelgrid:
                        #for item in pixel:
                            #print item
                            #pie = item
                            #if pie == [255, 255, 255]:
                                #print "FINALLY"
                                #if thingy == store.fillcolor:
                                    #print thingy
                                    #thingy = store.color
                    #pixelgrid = pixelgrid[pixelgrid.index([255, 255, 255])] = store.color
                    #for index in findall(pixelgrid, value):
                        #print "match at", i
                    pygame.surfarray.blit_array(drawspace, pixelgrid)
                    
                elif store.line == True:
                    if store.linepos == 1:
                        line1 = pygame.mouse.get_pos()
                        print line1
                        store.linepos = 2
                    elif store.linepos == 2:
                        line2 = pygame.mouse.get_pos()
                        print line2
                        store.drawline(line1, line2)
                        store.linepos = 1
                elif store.poly == True:
                    store.pointlist.append(pygame.mouse.get_pos())
                    pygame.draw.line(drawspace, store.color, pygame.mouse.get_pos(), pygame.mouse.get_pos(), 1)
                    if len(store.pointlist) > 2:
                        pygame.draw.polygon(drawspace, store.color, store.pointlist, 0)
                        
                else:
                    if event.button == 1:#Left mouse button(draw)
                        store.down = True
                        store.saved = False
                        testpos = pygame.mouse.get_pos()
                                    
                    elif event.button == 3:#Right mouse button(erase)
                        store.down2 = True
                        pygame.draw.rect(drawspace, [255, 255, 255], [pygame.mouse.get_pos()[0]-(store.bsize)/2, pygame.mouse.get_pos()[1]-(store.bsize)/2, store.bsize, store.bsize], 0)
                        store.saved = False
            else:
                if pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>10 and pygame.mouse.get_pos()[1]<60:
                    store.brushchooser()
                elif pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>70 and pygame.mouse.get_pos()[1]<120:
                    store.choosecolor()
                elif pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>130 and pygame.mouse.get_pos()[1]<180:
                    store.toolmenu()
                elif pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>190 and pygame.mouse.get_pos()[1]<240:
                    store.mainmenu()
                elif pygame.mouse.get_pos()[0]>store.new[0]+100 and pygame.mouse.get_pos()[0]<store.new[0]+220 and pygame.mouse.get_pos()[1]>10 and pygame.mouse.get_pos()[1]<130:
                    store.color = screen.get_at(pygame.mouse.get_pos())
                elif pygame.mouse.get_pos()[0]>store.new[0]+105 and pygame.mouse.get_pos()[0]<store.new[0]+120 and pygame.mouse.get_pos()[1]>140 and pygame.mouse.get_pos()[1]<155:
                    store.color = store.color2
                elif pygame.mouse.get_pos()[0]>store.new[0]+125 and pygame.mouse.get_pos()[0]<store.new[0]+140 and pygame.mouse.get_pos()[1]>140 and pygame.mouse.get_pos()[1]<155:
                    store.color = store.color3
                elif pygame.mouse.get_pos()[0]>store.new[0]+145 and pygame.mouse.get_pos()[0]<store.new[0]+160 and pygame.mouse.get_pos()[1]>140 and pygame.mouse.get_pos()[1]<155:
                    store.color = store.color4
                elif pygame.mouse.get_pos()[0]>store.new[0]+165 and pygame.mouse.get_pos()[0]<store.new[0]+180 and pygame.mouse.get_pos()[1]>140 and pygame.mouse.get_pos()[1]<155:
                    store.color = store.color5
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:#Left mouse button(draw)
                store.down = False
            elif event.button == 3:#Right mouse button(erase)
                store.down2 = False
        
    screen.blit(drawspace, [0, 0])
    screen.blit(backimage, [store.new[0], 0])
    screen.blit(brushbox, [store.new[0] + 25, 10])
    pygame.draw.rect(screen, store.color, [store.new[0] + 25, 70, 50, 50], 0)
    pygame.draw.rect(screen, store.color2, [store.new[0] + 105, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color3, [store.new[0] + 125, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color4, [store.new[0] + 145, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color5, [store.new[0] + 165, 150, 15, 15], 0)
    screen.blit(colortext, [store.new[0] + 25, 70])
    screen.blit(toolbox, [store.new[0] + 25, 130])
    screen.blit(menubox, [store.new[0] + 25, 190])
    screen.blit(pallette1, [store.new[0] + 100, 10])
    screen.blit(paintbox, [store.new[0]+ 100, 145])
    pygame.display.flip()#Flips the Buffer