
#    image kchibi = Image([Transform(zoom=1.5"kaiserchibi.png", zoom = 3.5)
#    image bchibi = Image("bertchibi.png", zoom = 1.5)
#    image schibi = Image("samchibi.png", zoom = 1.5)
#    image tchibi = Image("stellachibi.png", zoom = 1.5)
#    image ichibi = Image("sidchibi.png", zoom = 1.5)
#    image fchibi = Image("freddychibi.png", zoom = 1.5)
#    image hchibi = Image("shaharchibi.png", zoom = 1.5)
#    image jchibi = Image("jenbychibi.png", zoom = 1.5)
#    image cchibi = Image("catherinechibi.png", zoom = 1.5)
#    image dchibi = Image("draculachibi.png", zoom = 1.5)
#    image ochibi = Image("laurenchibi.png", zoom=1.5)





image splash = "tead.png"
image darken = "welcomescreenblank.png"
define danbox = Image("gui/textbox2.png", yalign=.5)
define bertbox = Image("gui/textbox3.png", yalign=.5)
image behappy = Image("bhappy.png", xcenter=.729, ycenter=.802)
image tracks:
    "tracks1.png"
    pause .05
    "tracks2.png"
    pause .05
    repeat
image ntracks:
    "tracksn1.png"
    pause .05
    "tracksn2.png"
    pause .05
    repeat
define audio.jaws = "jaws.mp3"
image eviscroll:
    contains:
        "evleftx3.png"
        ypos -2.0
        linear 80.0 ypos .01
        repeat
transform blink:
        "eye.png"
        alpha 1.0
        .1
        alpha 0.0
        .2
        alpha 1.0
        .1
        alpha 0.0
        .7
        alpha 1.0
        .1
        alpha 0.0
image debatescroll:
    contains:
        "vineslide.png"
        ypos .2
        xpos -1
        linear 30 xpos .01
        repeat
$ passattempts = 1
##############
#Toggle Dev
##############

init python:
    config.developer = True
    config.debug_sound = True
    renpy.music.register_channel("sfx", loop = False)
    config.menu_include_disabled = True

##############
#Voice Defines
##############

init python:
    def samvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi3.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def fillvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/fill.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def mevoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def bertvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi4.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def dracvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/pencil.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def stellavoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi2.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

###########
#Show Chibi
###########

init python:
    def showchibi(*argv):
        argv = [j + "chibi" for j in argv]
        currchibis = list()
        for i in renpy.get_showing_tags():
            if i.endswith("chibi"):
                currchibis.append(i)

        toremove = list()
        for i in currchibis:
            if i not in argv:
                toremove.append(i)
        toadd = list()
        for i in argv:
            if i not in currchibis:
                toadd.append(i)
        tostay = list()
        for i in argv:
            if i in currchibis:
                tostay.append(i)

        for i in toremove:
            renpy.hide(i)
        renpy.with_statement(Dissolve(1.0))

        y = 20
        for i in tostay:
            renpy.hide(i)
            renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
            y += 50
        renpy.with_statement(Dissolve(0.0))

        for i in toadd:
            renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
            y += 50
        renpy.with_statement(Dissolve(1.0))


    def showchibinofade(*argv):
        argv = [j + "chibi" for j in argv]
        currchibis = list()
        for i in renpy.get_showing_tags():
            if i.endswith("chibi"):
                currchibis.append(i)

        toremove = list()
        for i in currchibis:
            if i not in argv:
                toremove.append(i)
        toadd = list()
        for i in argv:
            if i not in currchibis:
                toadd.append(i)
        tostay = list()
        for i in argv:
            if i in currchibis:
                tostay.append(i)

        for i in toremove:
            renpy.hide(i)

        y = 20
        for i in tostay:
            renpy.hide(i)
            renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
            y += 50

        for i in toadd:
            renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
            y += 50

##################
#Character Defines
##################

define m = Character("Me?", callback=mevoice)
define n = Character("Dan Scagnelli", callback=mevoice, who_color = "FFFFFF")
define ni = Character("{i}Dan Scagnelli{/i}", callback=mevoice, what_italic=True, who_color = "FFFFFF") #Dan Internal, name and text italics
define np = Character("Dan Scagnelli", callback=mevoice, who_color = "FFFFFF", window_background=danbox)
define bi = Character("{i}Bert Kim{/i}", who_color= "78AB46", callback=bertvoice, what_italic = True) #Bert Internal, name and text italics
define bp = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice, window_background=bertbox)
define b = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice)
define s = Character("Sam Lee", who_color= "f3946a", image="sam", callback=samvoice)
define t = Character("Stella Cantoire", who_color= "d4af37", callback=stellavoice)
define d = Character("Dracula?", who_color= "ff9483", callback=dracvoice)
define f = Character("Freddy Ogden", who_color= "76d352", image="frog ind", callback=fillvoice)
define j = Character("Jenny Flowers", who_color= "e50548", callback=fillvoice)
define o = Character("Lauren Palmer", who_color= "fbe55c", callback=fillvoice)
define i = Character("Sid Straits", who_color= "4f90b0", callback=fillvoice)
define h = Character("Shahar Syed", who_color= "dfa64c", callback=fillvoice)
define z = Character("?????", who_color= "FFFFFF", callback=fillvoice)
define c = Character("Catherine Henson", who_color= "b66baa", callback=fillvoice)
define k = Character("Kaiser Maden", who_color= "b07b4c", callback=fillvoice)
define ses = Character("Sesame the cat", who_color= "fbe55c", callback=fillvoice)
define warden = Character("Warden", who_color= "ffffff", callback=fillvoice) #used in chapter 0
define scr = Character("Screen", who_color= "ffffff", what_italic = True, callback=fillvoice) #used in chapter 0
define tut = Character("Tutorial", who_color= "ffffff", what_italic = True, what_color = "00ff00") #used in chapter 0
define blank = Character(" ", what_italic=True, callback=fillvoice) #blank text, always italics

label start:

##################
#Free Time Counters
##################
    python:
        ftecounter = 0
        fte_bert = -2
        fte_sam = -1
        fte_stel = -1
        fte_drac = -1
        fte_frog = -1
        fte_jenn = -1
        fte_laur = -1
        fte_sid = -1
        fte_shah = -1
        fte_cath = -1
        fte_kais = -1

##################
#Trial Variables
##################
        currEvidence = -1
        phase = 0
        statement = -1
        agree = 0
        train_evidence1 = [True, True, True]
        train_evidence2 = [True, True, True]
        train_evidence3 = [True, True, True, True]
        lightscount = 0
        windowcount = 0

###########
#Start jump
###########
    #call screen midCarInv
    jump preinvest
