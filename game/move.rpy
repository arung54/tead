init -2 python:
    class Coordinate:#this one is to manage the hamster's location on the screen
        def __init__(self,x,y,xmin,ymin,xmax,ymax):
            #self explanatory
            self.x,self.y,self.xmin,self.ymin,self.xmax,self.ymax=x,y,xmin,ymin,xmax,ymax
            #whenever possible, xoffset and yoffset will be added to x and y
            #these offset variable are needed because Ren'Py lack Action
            #that let you add to variable
            self.xoffset,self.yoffset=0,0
            return
        #this transform method will be called every few milisecond
        #argument d is the object this transform will act on
        #ignore the time arguments for now, we don't need them
        def transform(self,d,show_time,animate_time):
            #add offset to x and y
            #once added, make these offset 0 again so we don't add multiple times
            self.x+=self.xoffset
            self.y+=self.yoffset
            self.xoffset,self.yoffset=0,0
            #check for boundary
            if self.x<self.xmin:
                self.x=self.xmin
            if self.y<self.ymin:
                self.y=self.ymin
            if self.x>self.xmax:
                self.x=self.xmax
            if self.y>self.ymax:
                self.y=self.ymax
            #finally, set the position of the object
            d.pos=(self.x,self.y)
            #return 0 to ensure that the function is called whenever possible
            return 0
    #create an object to manage out hamster's location
    hamster_coordinate=Coordinate(0.5,0.5,0.05,0.05,0.95,0.95)

#this screen show a hamster and you can move them in 4 direction with arrow key
screen hamster_cage:
    add "map2ui.png"

    #first we add the image of the hamster to the screen
    #an image named "hamster loc" must be defined of course
    #anchor (0.5,0.5) ensure that we will set the value of d.pos above
    #the coordinate will refer to the position of the exact centre of the image
    #at Transform(function=hamster_coordinate.transform) will make
    #the function hamster_coordinate.transform responsible for
    #various properties of the image "hamster loc"
    #these properties are passed in through the d argument
    #this function will be called every few milisecond

    add "hamster loc" anchor (0.5,0.5) at Transform(function=hamster_coordinate.transform)

    #now we add in all the keyboard control
    #here the higher-level keymap is used instead of listening to arrow button directly
    #because some device don't technically have arrow key, such as joystick
    #so instead of "K_LEFT" we use "focus_left" for example
    #we give each of these key event the appropriate Action
    #for example, for left button, we want to set the field
    #hamster_coordinate.xoffset to a negative number
    #SetField do exactly that job

    key "focus_left" action SetField(hamster_coordinate,"xoffset",-0.005)
    key "focus_right" action SetField(hamster_coordinate,"xoffset",+0.005)
    key "focus_up" action SetField(hamster_coordinate,"yoffset",-0.005)
    key "focus_down" action SetField(hamster_coordinate,"yoffset",+0.005)

    #"dismiss" is a whole collection of keys that are use to read dialogue
    #such as spacebar and enter key
    #action Return is use to quit this screen, without it you cannot quit
    #the argument for Return can be anything, it will be return to whatever call the screen

    key "dismiss" action Return("hamster")
