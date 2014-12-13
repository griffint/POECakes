#Programmed by pie
#(Tediously) Commented by pie
#If you are new to pygame or python, read over this program and try to learn something from it

#I give anyone permission modify this code as long as they don't distribute their modified version.
#Anyone can distribute this code as long as they do not claim it as their own.
#|_()|_
#Y('o')Y

#Customised for POE use by Griffin Tschurwald. Thank you pie for the base code!

import pygame, sys, easygui, os, serial, numpy, time

#print pygame.version.ver
fill = False#Remove me!

#===================SERIAL PORT SETUP AND FUNCTIONS===========================================================
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    timeout=0)
    
    
def send( theinput ):
    """
    This function takes as input a string, then sends it through serial to Arduino
    """
    ser.write( theinput )
    while True:
        try:
            time.sleep(0.1)
            break
        except:
            pass
    time.sleep(0.1)
  
def send_and_receive( theinput ):
    """
    This sends a string to arduino through serial.
    It then waits for a response from Arduino.
    """
    ser.write( theinput )
    time.sleep(.1)
    while True:
        try:
            time.sleep(0.2)
            state = ser.readline()
            
            return state
        except:

            pass
    time.sleep(0.1)
    

    
def connectionCheck(): 
    """Tests connection to cakebot using send_and_receive
    doesn't have input, outputs True if succesful, False if not
    """
    result = send_and_receive("CON")
    if result=="YES":
        return True
    else:
        return False

def greenButtonCheck():
    """Tests whether green button is pressed down or up
    returns 'down' if down, 'up' if up
    """
    result = send_and_receive("GB?")
    if result == "GBP":
        return "down"
    elif result == "GBU":
        return "up"
    else:
        pass

def orangeSwitchCheck():
    """
    Tests whether the orange switch is switched to the on or off position
    returns 'off' or 'on'
    """
    result = send_and_receive("OS?")
    if result == "OSO":
        return "off"
    elif result == "OSA":
        return "on"
    else:
        pass

def moveLinearStepper(steps, direction):
    """
    moves the stepper motor that controls linear motion of top froster
    takes as input int 'steps' and int 'direction'
    direction should be 1(inward) or 0(outward)
    """
    if direction == 1:
        send("LSI" + str(steps))
    elif direction == 0:
        send("LSO" + str(steps))
    else:
        pass

def movePlatform(steps,direction):
    """
    moves the stepper motor controlling the movePlatform
    takes as input int 'steps' and int 'direction'
    direction should be 1(clockwise) or 0(counterclockwise)
    """
    if direction == 1:
        send("RPC" + str(steps))
    elif direction == 0:
        send("RPN" + str(steps))
    else:
        pass

def moveTopFroster(time,direction):
    """
    moves the top frosting extruder motor
    int 'time' is how long it'll move for, int direction is direction
    direction should be 0 to retract and 1 to extrude frosting
    """
    if direction == 1:
        send("FTD" + str(time))
    elif direction == 0:
        send("FTU" + str(time))
    else:
        pass

def moveSideFroster(time,direction):
    """
    moves the side frosting extruder motor
    int 'time' is how long it'll move for, int direction is direction
    direction should be 0 to retract and 1 to extrude frosting
    """
    if direction == 1:
        send("FSD" + str(time))
    elif direction == 0:
        send("FSU" + str(time))
    else:
        pass

def testTopStepper():
    """This function will test the top stepper motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
        pass
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testTopStepper()
            if newTest == True:
                return True
            else:
                return False
    elif result == "down":
        moveLinearStepper(20,1)
        moveLinearStepper(20,0)
        choices = easygui.buttonbox(msg="Is the motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False



def testPlatformStepper():
    """This function will test the platform stepper motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
        pass
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testPlatformStepper()
            if newTest == True:
                return True
            else:
                return False
    elif result == "down":
        movePlatform(20,1)
        movePlatform(20,0)
        choices = easygui.buttonbox(msg="Is the motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False

def testTopFroster():
    """This function will test the top frosting motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
        pass
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testTopFroster()
            if newTest == True:
                return True
            else:
                return False
    elif result == "down":
        moveTopFroster(5,1)
        moveTopFroster(5,0)
        choices = easygui.buttonbox(msg="Is the motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False

def testSideFroster():
    """This function will test the side frosting motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
        pass
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testSideFroster()
            if newTest == True:
                return True
            else:
                return False
    elif result == "down":
        moveSideFroster(5,1)
        moveSideFroster(5,1)
        choices = easygui.buttonbox(msg="Is the motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False

def testAllMotors():
    """
    This tests all 4 motors. It takes no arguments. It will run all 4 motor test functions.
    At the end it will give a status report of what motors worked.
    """
    top = testTopStepper()
    platform = testPlatformStepper()
    topFrost=testTopFroster()
    sideFrost=testSideFroster()
    

def calibrateTopStepper():
    pass

def calibratePlatform():
    pass

def calibrateTopFroster():
    pass

def calibrateSideFroster():
    pass

def calibrateAll():
    pass

def printDesign():
    """
    this'll print whatever is on the drawing screen
    """
    
    
# ser.write("23,bottlesj")
# print ser.read(50)
#==============================================================================
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
        self.drawing_storer = []  
        #Cakebot state variables here - save state of things like button presses, direction
        self.topFrostCalibrated = False
        self.sideFrostCalibrated = False
        self.topStepCalibrated = False
        self.platformCalibrated = False
        self.platformPosition = 0 #saves the platforms position in steps from calibration zero. clockwise is positive
        
        
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

#-------This needs to be changed to tip chooser-------------------------------

    def brushchooser(self):
        newbrush = easygui.buttonbox("Which icing tip would you like?", title = "Tip Menu", choices = ["Skinny tip", "Cancel"])
        if newbrush == "Cancel":
            pass
        else:
            if newbrush == "Skinny tip":
                self.bsize = 15
           

   #Preset pattern picker-----------------------------------------------------------------

#----Not sure what this is for or where it's used----------------------

#==============================================================================
#     def presetsChooseer(self):
#         newbrush = easygui.buttonbox("Which preset pattern would you like to draw", title = "Brush Menu", choices = ["Big", "Medium", "Small", "Custom", "Cancel"])
#         if newbrush == "Cancel":
#             pass
#         else:
#             if newbrush == "Custom":
#                 newnewbrush = easygui.enterbox("Enter the brush size as a number.", title = "Custom Brush Menu")
#                 if newnewbrush == None:
#                     self.brushchooser()
#                 else:
#                     self.bsize = int(newnewbrush)
#             elif newbrush == "Big":
#                 self.bsize = 25
#             elif newbrush == "Medium":
#                 self.bsize = 15
#             elif newbrush == "Small":
#                 self.bsize = 5
#==============================================================================



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

    #This defines the cakebot printing menu. Need to put in better testing code
    def printmenu(self):
        printmenu = easygui.choicebox("Cakebot Options", title="CakeBot", choices = ["Testing Menu", "Calibration Menu", "Printing help", "Print Your Design!","Print a preset design"])
        #The Testing menu needs to have lots of tools to check all of our motors
        if printmenu == "Testing Menu":
            testmenu = easygui.choicebox("Testing Menu for Cakebot", choices = ["Test connection", "Test Extruding Motor", "Test Lazy Susan Motor","Test top frosting motor","Test side frosting motor"])
            if testmenu == "Test connection":
                easygui.msgbox("Press OK to test connection to cakebot")
                #test overall connection to cakebot 
        if printmenu == "Calibration Menu":
            #calibration options here
        if printmenu == "Printing help":
            easygui.textbox(msg='Here are some helpful tips for cakebot', title='CakeBot Help', text='', codebox=0)
        if printmenu == "Print Your Design!":
            easygui.msgbox("Printing Sequence Started")
        if printmenu == "Print a preset design":
            presetmenu = easygui.choicebox("Pick a preset design to print to your cake", choices = ["Outside Border","Wavy Border", "Border Near Center"," Wavy Border Near Center"])
                #Need to write code for printing those choices here
            if presetmenu == "Outside Border":
                #code to print an outside border here
                return
                
                
    def drawingToCakebot(self): #this function will take whatever is currently drawn and export it to cakebot to print
        easygui.msgbox("Drawing is now printing!")
        

#    def toolmenu(self):
#        toolmenu = easygui.buttonbox("Select which tool you want. You are currently using: " + store.toolname, title = "Tool Menu", choices = ["Toggle Color Picker", "Toggle Text Tool", "Toggle Polygon Tool", "No tool", "Cancel"])
#        if toolmenu == "No tool":
#            self.dropper = False
#            self.texton = False
#            self.poly = False
#            self.toolname = "Basic Drawing"
#        elif toolmenu == "Toggle Color Picker":
#            self.dropper = True
#            self.texton = False
#            self.poly = False
#            self.toolname = "Color Picker"
#        elif toolmenu == "Toggle Text Tool":
#            self.texton = True
#            self.dropper = False
#            self.poly = False
#            self.toolname = "Text Tool"
#        elif toolmenu == "Toggle Polygon Tool":
#            self.poly = True
#            self.texton = False
#            self.picker = False
#            self.toolname = "Polygon Tool"

#    def drawtext(self):
#        self.mousepos = pygame.mouse.get_pos()
#        size = easygui.integerbox("Enter the size you want your text:", title = 'Text Tool')
#        print size
#        if size == None:
#            return
#        text = easygui.enterbox("What text would you like printed?", title = 'Text Tool')
#        print text
#        if text == None or text == "":
#            return
#        Font =  pygame.font.Font("resources/annifont.TTF", size)#From fontfile
#        drawtext = Font.render(text, True, self.color)
#        print Font.size(text)
#        drawspace.blit(drawtext, [self.mousepos[0] - Font.size(text)[0]/2, self.mousepos[1] - Font.size(text)[1]/2])
#        self.saved = False

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

msg = "Enter the height and width of your Cake Design"
title = "New file"
fieldNames = ["Height","Width"]
fieldValues = []

store = storer([])#Creates a variable storing object to holds lot of stuff

def newfile():
    store.loadpic = False
    open_or_new = easygui.buttonbox("Welcome to CakeBot", title = "CakeBot", choices = ["New File", "Open", "Exit"])
    if open_or_new == "New File":
        store.loadpic = False
        store.new = [int(800), int(800)] #sets the size of the drawing box
        
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
#Sets the caption - changed it to cakebot
pygame.display.set_caption("CakeBot - Press 'h' or go to the assistant for help - " + store.imagename)
#Creates the clock object
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 25)
backimage = pygame.image.load("resources/back.gif")
brushbox = pygame.image.load("resources/brush.gif")
colortext = pygame.image.load("resources/color.gif")

menubox = pygame.image.load("resources/menu.gif")
pallette1 = pygame.image.load("resources/pallette1.gif")
paintbox = pygame.image.load("resources/buckets.gif")

#The main loop-----------------------------------------------------------------
while 1:
    clock.tick(30)
    
    #-------------------------------------------------------------
    #CONTROL CODE FOR CAKEBOT GOES HERE
    #============================================================
    #good spot for reading the serial early and often here
    #will do all codes as 3 chars then a semicolon as a linebreak
    
   
    
    #===========================================================
    #END OF CONTROL CODE FOR CAKEBOT
    #===========================================================
    
    
    #Checks for events---basically user doing anything--------------------------
    for event in pygame.event.get():
        # if they want to exit, let them exit
        if event.type == pygame.QUIT:
            if store.saved == False:
                exiting = easygui.buttonbox("You have unsaved changes. Quit anyway?", title = 'Unsaved work', choices = ["Yes", "No"])
                if exiting == "Yes":
                    sys.exit()
            else:
                sys.exit()
        elif event.type == pygame.USEREVENT: #if anything happens- this occurs often
        
            if store.down: #this happens whenever someone tries to draw 
                testoldpos = testpos
                testpos = pygame.mouse.get_pos()
                #this bit just keeps drawing lines every time mouse if down
                #this might be a good point to store drawing locations along with brush size and type
                store.drawline(testoldpos, testpos, store.bsize)   #(point one, point 2, width)
                if len(store.drawing_storer) >0 :
                    
                    if store.drawing_storer[-1] !=[testoldpos,testpos]:
                        store.drawing_storer.append([testoldpos,testpos])
                        print len(store.drawing_storer)
                        
                elif len(store.drawing_storer) == 0 :
                    store.drawing_storer.append([testoldpos,testpos])
                #check for any duplicates
                
                
        #Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:#Save menu
                store.save()

            elif event.key == pygame.K_c:#Color chooser
                store.choosecolor()

            elif event.key == pygame.K_SLASH:#Cakebot Printing Menu
                store.printmenu()

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
            elif event.key == pygame.K_F5:
                print store.drawing_storer

        #the actual drawing that happens when people hold the mouse down-----
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
                    pixelgrid = pygame.surfarray.array3d(drawspace)#copies pixels from surface to an array
                    
                    #print pixelgrid - the array from the surface
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
      #these control what happens when certain buttons get pressed
      #it looks like mouse pos [0] is the x and pos [1] is the y
            else:
                #new is the image size
                if pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>10 and pygame.mouse.get_pos()[1]<60:
                    store.brushchooser()
                elif pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>70 and pygame.mouse.get_pos()[1]<120:
                    store.choosecolor()
               
                elif pygame.mouse.get_pos()[0]>store.new[0]+25 and pygame.mouse.get_pos()[0]<store.new[0]+75 and pygame.mouse.get_pos()[1]>190 and pygame.mouse.get_pos()[1]<240:
                    store.mainmenu()
                elif pygame.mouse.get_pos()[0]>store.new                                                                                                                                                                                                                                                                                                                [0]+100 and pygame.mouse.get_pos()[0]<store.new[0]+220 and pygame.mouse.get_pos()[1]>10 and pygame.mouse.get_pos()[1]<130:
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

#-----end of checking for events----------------

    screen.blit(drawspace, [0, 0])
    screen.blit(backimage, [store.new[0], 0])
    screen.blit(brushbox, [store.new[0] + 25, 10])
    pygame.draw.rect(screen, store.color, [store.new[0] + 25, 70, 50, 50], 0)
    pygame.draw.rect(screen, store.color2, [store.new[0] + 105, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color3, [store.new[0] + 125, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color4, [store.new[0] + 145, 150, 15, 15], 0)
    pygame.draw.rect(screen, store.color5, [store.new[0] + 165, 150, 15, 15], 0)
    screen.blit(colortext, [store.new[0] + 25, 70])
    
    screen.blit(menubox, [store.new[0] + 25, 190])
    screen.blit(pallette1, [store.new[0] + 100, 10])
    screen.blit(paintbox, [store.new[0]+ 100, 145])
    pygame.display.flip()#Flips the Buffer
