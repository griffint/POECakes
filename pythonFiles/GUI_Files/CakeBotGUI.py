#Programmed by pie
#(Tediously) Commented by pie
#If you are new to pygame or python, read over this program and try to learn something from it

#I give anyone permission modify this code as long as they don't distribute their modified version.
#Anyone can distribute this code as long as they do not claim it as their own.
#|_()|_
#Y('o')Y

#Customised for POE use by Griffin Tschurwald. Thank you pie for the base code!

import pygame, sys, easygui, os, serial, numpy, time, math

#print pygame.version.ver
fill = False#Remove me!

#===================SERIAL PORT SETUP AND FUNCTIONS===========================================================
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    timeout=5)
    
    
def send( theinput ):
    """
    This function takes as input a string, then sends it through serial to Arduino
    """
    ser.write( theinput )
    print(str(theinput) + " sent to cakebot")
    time.sleep(.5)
    ser.flushOutput()
    ser.flushInput()
  
def send_and_receive( theinput, timeout_time):
    """
    This sends a string to arduino through serial.
    It then waits for a response from Arduino.
    timeout_time is how long it'll wait for a response in seconds
    """
    print("timeout is "+str(timeout_time))
    ser.timeout=timeout_time
    ser.write(theinput)
    print("I sent " + theinput +" to cakebot")
    time.sleep(.8)
    while True:
        
        print("time to send and receive")
        state = ser.readline() #this has a timeout of 10 seconds
        print(state)
        if state == "":
            
            print ("Nothing received dawg")
            easygui.msgbox("No data received from serial. Please consult somone who knows what they're doing.")
            return False
        else:
            print("Yay we got something")
            print(state)
            print("length of result is "+ str(len(state)))
            state = state.replace('\n', '').replace('\r', '')
            return str(state)
    

    
def connectionCheck(): 
    """Tests connection to cakebot using send_and_receive
    doesn't have input, outputs True if succesful, False if not
    """
    result = str(send_and_receive("CON",5))
   
    if result == 'YES':
        print("connected to cakebot")
        return True
    else:
        print("should return false")
        return False

def greenButtonCheck():
    """Tests whether green button is pressed down or up
    returns 'down' if down, 'up' if up
    """
    result = send_and_receive("GB?",5)
    return "GBP"
    if result == "GBP":
        easygui.msgbox("Green button registered as pressed down!")
        return "down"
    elif result == "GBU":
        easygui.msgbox("Green button registered as up...")
        return "up"
    else:
        easygui.msgbox("Something got screwed up while attempting to read the green button")
        pass

def orangeSwitchCheck():
    """
    Tests whether the orange switch is switched to the on or off position
    returns 'off' or 'on'
    """
    result = send_and_receive("OS?",5)
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
    doesn't return anything and doesn't need to wait for feedback from arduino
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
    doesn't return anything and doesn't need to wait for feedback from arduino
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
    doesn't return anything and doesn't need to wait for feedback from arduino
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
    doesn't return anything and doesn't need to wait for feedback from arduino
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
    print("Result of green button check is " +result)
    if result == "up":
        
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testTopStepper()
            if newTest == True:
                return True
            else:
                return False
        elif choices == "Exit":
            return False
    elif result == "down":
        moveLinearStepper(20,1)
        moveLinearStepper(20,0)
        choices = easygui.buttonbox(msg="Is top stepper motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False
            
    else:
        easygui.msgbox("Something is weird with Cakbot")



def testPlatformStepper():
    """This function will test the platform stepper motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    
    if result == "up":
        
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testPlatformStepper()
            if newTest == True:
                return True
            else:
                return False
        elif choices == "Exit":
            return False
    elif result == "down":
        movePlatform(50,1)
        movePlatform(50,0)
        choices = easygui.buttonbox(msg="Is the lazy susan motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False
            
    else:
        easygui.msgbox("Something is weird with Cakbot")

def testTopFroster():
    """This function will test the top frosting motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
        
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testTopFroster()
            if newTest == True:
                return True
            else:
                return False
        elif choices == "Exit":
            return False
    elif result == "down":
        moveTopFroster(5,1)
        moveTopFroster(5,0)
        choices = easygui.buttonbox(msg="Is the top frosting motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False
            
    else:
        easygui.msgbox("Something is weird with Cakbot")

def testSideFroster():
    """This function will test the side frosting motor. It'll return True if the motor works,
    it'll return False if the motor does not. THis does not need any input.
    """
    result = greenButtonCheck()
    if result == "up":
      
        #prompt user to press it here
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newTest = testSideFroster()
            if newTest == True:
                return True
            else:
                return False
        elif choices == "Exit":
            return False
    elif result == "down":
        moveSideFroster(5,1)
        moveSideFroster(5,1)
        choices = easygui.buttonbox(msg="Is the side frosting motor spinning?",choices=["YES","NO"])
        if choices == "YES":
            easygui.msgbox("This motor is working!")
            return True
        if choices == "NO":
            easygui.msgbox("Inspect Cakebot please. Exiting testing routine")
            return False
            
    else:
        easygui.msgbox("Something is weird with Cakbot")

def testAllMotors():
    """
    This tests all 4 motors. It takes no arguments. It will run all 4 motor test functions.
    At the end it will give a status report of what motors worked.
    and return a list of 4 booleans corresponding to top, platform, topfrost, and sidefrost motors being tested
    """
    easygui.msgbox("Press OK to test all motors")
    top = testTopStepper()
    platform = testPlatformStepper()
    topFrost=testTopFroster()
    sideFrost=testSideFroster()
    
    topTestText = "Top Motor not working \n"
    platformTestText = "Platform not working \n"
    topFrostText = "Top froster not working \n"
    sideFrostText = "Side froster not working \n"
    
    if top == True:
        topTestText = "Top Motor working \n"
    
        
    if platform == True:
        platformTestText = "Platform working \n"
    
        
    if topFrost ==True:
        topFrostText = "Top froster working \n"

        
    if sideFrost == True:
        sideFrostText = "Side froster working \n"
    
        
        
    easygui.msgbox(topTestText + platformTestText + topFrostText + sideFrostText + "Exit testing routine")
    return [top,platform,topFrost,sideFrost]

def calibrateTopStepper():
    """
    This will calibrate the stepper motor on top of the cakebot, using the limit switch as a zero reference point. 
    Takes no inputs, returns True if user calibrates, false if something weird goes wrong.
    It moves the stepper bit by bit until it detects the limit switch is depressed
    Correct direction to spin to be determined through manual testing
    returns True if calibrated, False otherwise
    """
    
    result = greenButtonCheck()
    
    if result == "up":
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newResult = calibrateTopStepper()
            if newResult == True:
                return True
            elif newResult == False:
                return False
        elif choices == "Exit":
                return False
            
    elif result == "down":
        result = send_and_receive("CLS",60)
        if result == "LSC":
            easygui.msgbox(msg="Linear Stepper has been calibrated")
            return True
        else:
            easygui.msgbox(msg="Stepper not calibrated")
            return False
            
    
    

def calibratePlatform():
    """
    This will calibrate the platform on top of the cakebot, using the limit switch as a zero reference point. 
    Takes no inputs, returns True if user calibrates, false if something weird goes wrong.
    It moves the stepper bit by bit until it detects the limit switch is depressed
    Correct direction to spin to be determined through manual testing
    returns True if calibrated, False otherwise
    """
    print("calibrating platform")
    result = greenButtonCheck()
    
    if result == "up":
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newResult = calibratePlatform()
            if newResult == True:
                return True
            elif newResult == False:
                return False
        elif choices == "Exit":
                return False
            
    elif result == "down":
        result = send_and_receive("CPS",60)
        if result == "PSC":
            easygui.msgbox(msg="Platform Stepper has been calibrated")
            return True
        else:
            easygui.msgbox(msg="Stepper not calibrated")
            return False

def calibrateTopFroster():
    """
    This will calibrate the frosting motor on top of cakebot, using user input as zero point.
    Takes no inputs, returns True if user calibrates, false if something weird goes wrong.
    It moves the stepper bit by bit until it detects the limit switch is depressed
    Correct direction to spin to be determined through manual testing
    returns True if calibrated, False otherwise
    """
    
    result = greenButtonCheck()
    
    if result == "up":
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newResult = calibrateTopFroster()
            if newResult == True:
                return True
            elif newResult == False:
                return False
        elif choices == "Exit":
                return False
            
    elif result == "down":
        result = send_and_receive("CTF",60)
        if result == "TFC":
            easygui.msgbox(msg="Top froster has been calibrated")
            return True
        else:
            easygui.msgbox(msg="Stepper not calibrated")
            return False

def calibrateSideFroster():
    """
    This will calibrate the frosting motor on top of cakebot, using user input as a 0 point.  
    Takes no inputs, returns True if user calibrates, false if something weird goes wrong.
    It moves the stepper bit by bit until it detects the limit switch is depressed
    Correct direction to spin to be determined through manual testing
    returns True if calibrated, False otherwise
    """
    
    result = greenButtonCheck()
    
    if result == "up":
        choices = easygui.buttonbox(msg="Please press down the green button!",title="Green button checker",choices=["It's pressed!","Exit"])
        if choices == "It's pressed!":
            newResult = calibrateTopStepper()
            if newResult == True:
                return True
            elif newResult == False:
                return False
        elif choices == "Exit":
                return False
            
    elif result == "down":
        result = send_and_receive("CSF",60)
        if result == "SFC":
            easygui.msgbox(msg="Side froster has been calibrated")
            return True
        else:
            easygui.msgbox(msg="Stepper not calibrated")
            return False

def calibrateAll():
    easygui.msgbox("Ready to calibrate all the motors? Press OK when you're ready!")
    top = calibrateTopStepper()
    platform = calibratePlatform()
    topFrost = calibrateTopFroster()
    sideFrost = calibrateSideFroster()
    
    topTestText = "Top Motor not properly calibrated \n"
    platformTestText = "Platform not properly calibrated \n"
    topFrostText = "Top froster not properly calibrated \n"
    sideFrostText = "Side froster not properly calibrated \n"
    
    if top == True:
        topTestText = "Top Motor calibrated \n"
    
        
    if platform == True:
        platformTestText = "Platform calibrated \n"
    
        
    if topFrost ==True:
        topFrostText = "Top froster calibrated \n"

        
    if sideFrost == True:
        sideFrostText = "Side froster calibrated \n"
    
        
        
    easygui.msgbox(topTestText + platformTestText + topFrostText + sideFrostText + "Exit testing routine")
    return [top,platform,topFrost,sideFrost]
    
    
def printOutsideBorder(PlatformCalibrated,TopStepperCalibrated, TopFrostCalibrated): #TODO put arguments in printmenu code
    if PlatformCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate platform motor")
    if TopStepperCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate top stepper motor")
    if TopFrostCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate top frosting motor")
    easygui.msgbox("Looks like you're calibrated fully. Press OK to print an outside border")
    result = send_and_receive("PSB",120)
    if result == "GUD":
        print("border printed")
        easygui.msgbox("Your border should be printed")
    else:
        print("Error with border")
        easygui.msgbox("I think something went wrong with the border")
    
def thetaCalc(x1,y1):
    """
    input x and y should be the basy x,y as measured from top left
    This will calculate and return the angle in degrees of a given x,y point
    as measured from horizontal right. 
    """
    x = x1-400
    print("x into calculation is " +str(x))
    y = 400 - y1
    print("y into calculation is " + str(y))
    print("numpy reveals " + str(numpy.arctan(y/x)))
    if x>0 and y>0:
        #first quadrant, just do arctan
        degreees = math.degrees(math.atan(y/x))
        print(str(math.atan(y/x)))
        print("first quadrant")
    elif x>0 and y<0:
        degreees = math.degrees(math.atan(y/x)) + 360
        print(str(math.degrees(math.atan(y/x)) + 360))
        print("second quadrant")
    elif x<0 and y>0:
        degreees = math.degrees(math.atan(y/x)) + 180
        print("third quadrant")
    elif x<0 and y<0:
        degreees = math.degrees(math.atan(y/x)) +180
        print("fourth quadrant")
    elif x == 0 and y>0:
        degreees = 90
    elif x==0 and y<0:
        degreees = 270
    elif x<0 and y==0:
        degreees = 180
    elif x>0 and y==0:
        degreees = 0
    elif x==0 and y==0:
        degreees = 0
    print("degrees calculated is " +str(degreees))
    return degreees
    
        
        
        

def printDesign(PlatformCalibrated,TopStepperCalibrated, TopFrostCalibrated, SideFrostCalibrated, lineArray):
    """
    this'll print whatever is on the drawing screen
    takes as input an array of line segments which it's supposed to draw
    takes as argument whether it's calibrated or not as True or False
    """
    
    #check for all calibrations
    if PlatformCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate platform motor")
    if TopStepperCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate top stepper motor")
    if TopFrostCalibrated == True:
        pass
    else:
        easygui.msgbox("Please calibrate top frosting motor")
    if SideFrostCalibrated == True:
        pass
    else: 
        easygui.msgbox("Please calibrate side frosting motor")
        
    easygui.msgbox("It appears all your motors are calibrated. Please make sure you're ready to print.")
    previous_radius = 400
    previous_theta = 0;
    i = 0;
    while i<len(lineArray):
        #iterate through all lines, print each one, wait for confirmation before next
        
        #for each line, will need to convert to polar location
        #lineArray has format of [[(x,y),(x1,y1)]]
        
        first_point = lineArray[i]
        
        print("time to print the point at " + str(lineArray[i]))
        
        #gives radius value of this point in terms of pixels from center
        radius_first = ((first_point[0]-400)**2+(400-first_point[1])**2)**(.5)
        print("previous radius was " + str(previous_radius))
        print("new radius is " + str(radius_first))
        #now need to do theta calculations. will need to account for correct quadrant
    
        theta_first = thetaCalc(first_point[0],first_point[1])
        
        #now to calculate how far it needs to move in terms of pixels and degrees
        #to get to the first point
    
        first_move_radius = radius_first - previous_radius
        first_move_theta = theta_first - previous_theta
        if math.fabs(first_move_radius)<2 and math.fabs(first_move_theta)<1:
            print("These steps are too small")   
            i+=1
            continue
        #now convert to actual step values, will need to round to nearest integer
        first_move_rsteps = int(round(first_move_radius*.674))
        print("First move theta is " + str(first_move_theta))
        print int(round(first_move_theta*(.55555555)))
        first_move_tsteps = int(round(first_move_theta*(.5555555)))
        print first_move_tsteps
        
        #now to actually move it, then lay frosting at that point
        #first move the linear stepper
        #a negative rsteps indicates moving inward, which means input of 1
        print("Telling linear stepper to move " + str(first_move_rsteps) + " steps")
        if first_move_rsteps<0:
            moveLinearStepper((-1*first_move_rsteps),1)
        else:
            moveLinearStepper(first_move_rsteps,0)
        time.sleep(10)
        #moving platform. clockwise==negative theta change==input of 1
        print("Telling platform to move " + str(first_move_tsteps) + " steps")
        if first_move_tsteps<0:
            movePlatform((-1*first_move_tsteps),1)
        else:
            movePlatform(first_move_tsteps,0)
        time.sleep(10)
        #then lay down some sweet frosting
        moveTopFroster(2,1)
        time.sleep(10)
        previous_radius = radius_first
        previous_theta = theta_first
        i+=1
        
    easygui.msgbox("Your design should be printed!!!!")
        
     
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
        self.topStepperPosition = 0 #saved as steps from calibration 0
        self.topFrostTested = False
        self.sideFrostTested = False
        self.topStepTested = False
        self.platformTested = False
        
        
        
        
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
        menuchoice = easygui.choicebox("Select a task", title = "Main Menu", choices = ["Print Menu", "Change Brush", "Save", "Open", "Help", "Tool Menu"])
        if menuchoice == "Save":
            self.save()
        elif menuchoice == "Help":
            easygui.textbox("Help:", title = "Help", text = open("helptext.txt", "r"))
        elif menuchoice == "Change Brush":
            self.brushchooser()
        elif menuchoice == "Print Menu":
            self.printmenu()
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
        printmenu = easygui.choicebox("Cakebot Options", title="CakeBot", choices = ["Testing Menu", "Calibration Menu", "Printing help", "Print Your Design!","Print a preset design", "Manual Control"])
        #The Testing menu needs to have lots of tools to check all of our motors
        if printmenu == "Testing Menu":
            
            testmenu = easygui.choicebox("Testing Menu for Cakebot", choices = ["Test connection", "Test Linear Stepper Motor", "Test Lazy Susan Motor","Test top frosting motor","Test side frosting motor", "Test all motors" ])
            if testmenu == "Test connection":
                easygui.msgbox("Press OK to test connection to cakebot")
                connectResult = connectionCheck()
                if connectResult == True:
                    easygui.msgbox("connected to cakebot!!!")
                elif connectResult == False:
                    easygui.msgbox("connection failed")
            if testmenu == "Test Lazy Susan Motor":
                testResult = testPlatformStepper()
                if testResult == True:
                    self.platformTested = True
                else:
                    pass
            if testmenu == "Test Linear Stepper Motor":
                testResult = testTopStepper()
                if testResult == True:
                    self.topStepTested = True
                else:
                    pass
            if testmenu == "Test top frosting motor":
                testResult = testTopFroster()
                if testResult == True:
                    self.topFrostTested = True
                else:
                    pass
            if testmenu == "Test side frosting motor":
                testResult = testSideFroster()
                if testResult == True:
                    self.sideFrostTested = True
                else:
                    pass
            if testmenu == "Test all motors":
                testList = testAllMotors()
                if all(testList) == True:
                    easygui.msgbox("ALl motors succesfully tested")
                    self.platformTested = True
                    self.topStepTested = True
                    self.sideFrostTested = True
                    self.topFrostTested = True
                else:
                    easygui.msgbox("SOmething went wrong with testing. Please test the motors that were listed as not working")
                
        if printmenu == "Calibration Menu":
            calibrationmenu = easygui.choicebox("Calibration Menu for Cakebot", choices = ["Calibrate Platform", "Calibrate Top Stepper", "Calibrate Top Froster", "Calibrate Side Froster", "Calibrate all"])
            if calibrationmenu == "Calibrate Platform":
                calResult = calibratePlatform()
                if calResult == True:
                    self.platformCalibrated = True
                    self.platformPosition = 0
                else:
                    pass
            if calibrationmenu == "Calibrate Top Stepper":
                calResult = calibrateTopStepper()
                if calResult == True:
                    self.topStepCalibrated = True
                    self.topStepperPosition = 0
                else:   
                    pass
            if calibrationmenu == "Calibrate Top Froster":
                calResult = calibrateTopFroster()
                if calResult == True:
                    self.topFrostCalibrated = True
                else:
                    pass
            if calibrationmenu == "Calibrate Side Froster":
                calResult = calibrateSideFroster()
                if calResult == True:
                    self.sideFrostCalibrated = True
                else:
                    pass
            if calibrationmenu == "Calibrate all":
                calibList = calibrateAll()
                if all(calibList) == True:
                    easygui.msgbox("All motors succesfully calibrated")
                    self.platformCalibrated = True
                    self.platformPosition = True
                    self.topStepCalibrated = True
                    self.topStepperPosition = 0
                    self.topFrostCalibrated = True
                    self.sideFrostCalibrated = True
                else:
                    pass
                
        if printmenu == "Printing help":
            easygui.textbox(msg='Here are some helpful tips for cakebot', title='CakeBot Help', text='Ask griffin cause this program is weird', codebox=0)
        if printmenu == "Print Your Design!":
            easygui.msgbox("Printing Sequence Starting when OK pressed")
            printDesign(True,True,True,True, self.drawing_storer)
        if printmenu == "Print a preset design":
            presetmenu = easygui.choicebox("Pick a preset design to print to your cake", choices = ["Outside Border","Wavy Border", "Border Near Center"," Wavy Border Near Center","Spiral"])
                #Need to write code for printing those choices here
            if presetmenu == "Outside Border":
                printOutsideBorder(True,True,True)  #these will need to be false when actually going.
                #code to print an outside border here
            if presetmenu == "Spiral":
                send("SPI")
                
        if printmenu == "Manual Control":
            exitmenu = False
            while exitmenu == False:
                manualmenu = easygui.buttonbox(msg="Manual Control: press buttons to control cakebot", choices = ("Platform Clockwise", "Platform Counterclockwise", "Top Stepper In", "Top Stepper Out", "Top Froster Out", "Top Froster In", "Side Froster Out", "Side Froster In" , "Exit"))
                if manualmenu == "Platform Clockwise":
                    movePlatform(3,1)
                elif manualmenu == "Platform Counterclockwise":
                    movePlatform(3,0)
                elif manualmenu == "Top Stepper In":
                    moveLinearStepper(10,1)
                elif manualmenu == "Top Stepper Out":
                    moveLinearStepper(10,0)
                elif manualmenu == "Top Froster Out":
                    moveTopFroster(1,1)
                elif manualmenu == "Top Froster In":
                    moveTopFroster(30,0)
                elif manualmenu == "Side Froster Out":
                    moveSideFroster(2,1)
                elif manualmenu == "Side Froster In":
                    moveSideFroster(2,0)
                elif manualmenu == "Exit":
                    exitmenu = True
                
                
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
connectionCheck()  #this is here because the first serial comms always fail for some reason
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

paintbox = pygame.image.load("resources/buckets.gif")

#The main loop-----------------------------------------------------------------
while 1:
    clock.tick(30)
    
    
    
    
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
                    
                    if store.drawing_storer[-1] !=testpos:
                        store.drawing_storer.append(testpos)
                        print len(store.drawing_storer)
                        
                elif len(store.drawing_storer) == 0 :
                    store.drawing_storer.append(testpos)
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
    
    screen.blit(paintbox, [store.new[0]+ 100, 145])
    pygame.display.flip()#Flips the Buffer
