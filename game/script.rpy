
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


# scream ONLY heard in mid car


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

image btracks:
    "tracksb1.png"
    pause .05
    "tracksb2.png"
    pause .05
    repeat

image turning:
    "trainturn1.png"
    pause .05
    "trainturn2.png"
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
define slowdissolve = Dissolve(2.0)
image debatescroll:
    contains:
        "vineslide.png"
        ypos .2
        xpos -1
        linear 30 xpos .01
        repeat

image bg debatescroll:
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
    renpy.music.register_channel("sfx", mixer = "sfx", loop = False)
    config.menu_include_disabled = True
    config.layers = [ 'background', 'master', 'transient', 'screens', 'overlay', '1', '2', '3', '4' ]
    renpy.music.set_volume(0.3)

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
            renpy.sound.play("audio/voi5deep_1.mp3")
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
    def kaiservoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi2.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def frogvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def laurenvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi6calm_1.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def jennyvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi7chirpy.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

init python:
    def stellavoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("audio/voi8stella.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

###########
#Show Chibi
###########

init python:
    def statusnt(name, person, ch, sun):
        sunlist = [Position(xpos=1165, xanchor=0, ypos=55, yanchor=0)]
        chibilist = [Position(xpos=1225, xanchor=0, ypos=55, yanchor=0)]
        chapterlist = [Position(xpos=1095, xanchor=0, ypos=65, yanchor=0)]
        renpy.show("status")
        renpy.show(name = "location", what = Text("{b}"+name+"{/b}"), at_list = [Position(xpos=1055, xanchor=0, ypos=5, yanchor=0)])
        renpy.show("ch"+str(ch), at_list = chapterlist)
        if sun == 1:
            renpy.show("sun1", at_list = sunlist)
        if sun == 2:
            renpy.show("sun2", at_list = sunlist)
        if sun == 3:
            renpy.show("sun3", at_list = sunlist)
        if sun == 4:
            renpy.show("sun4", at_list = sunlist)
        if person == "dan":
            renpy.show("danchibi2", at_list = chibilist)
        if person == "bert":
            renpy.show("bertchibi2", at_list = chibilist)

    def scenent(bg, name, person, ch, sun):
        sunlist = [Position(xpos=1165, xanchor=0, ypos=55, yanchor=0)]
        chibilist = [Position(xpos=1225, xanchor=0, ypos=55, yanchor=0)]
        chapterlist = [Position(xpos=1095, xanchor=0, ypos=65, yanchor=0)]
        renpy.scene()
        renpy.show(bg)
        renpy.show("status")
        renpy.show(name = "location", what = Text("{b}"+name+"{/b}"), at_list = [Position(xpos=1055, xanchor=0, ypos=5, yanchor=0)])
        renpy.show("ch"+str(ch), at_list = chapterlist)
        if sun == 1:
            renpy.show("sunup", at_list = sunlist)
        if sun == 2:
            renpy.show("sunout", at_list = sunlist)
        if sun == 3:
            renpy.show("sundown", at_list = sunlist)
        if sun == 4:
            renpy.show("sungone", at_list = sunlist)
        if person == "dan":
            renpy.show("danchibi2", at_list = chibilist)
        if person == "bert":
            renpy.show("bertchibi2", at_list = chibilist)

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


    def showchibint(*argv):
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

define m = Character("Me?", callback=fillvoice, who_color = "FFFFFF")
define mi = Character("Me?", callback=fillvoice, what_italic=True, who_color = "FFFFFF")
define n = Character("Dan Scagnelli", callback=fillvoice, who_color = "FFFFFF")
define ni = Character("{i}Dan Scagnelli{/i}", callback=fillvoice, what_italic=True, who_color = "FFFFFF") #Dan Internal, name and text italics
define np = Character("Dan Scagnelli", callback=mevoice, who_color = "FFFFFF", window_background=danbox)
define bi = Character("{i}Bert Kim{/i}", who_color= "78AB46", callback=bertvoice, what_italic = True) #Bert Internal, name and text italics
define bp = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice, window_background=bertbox)
define b = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice)
define s = Character("Sam Lee", who_color= "f3946a", image="sam", callback=samvoice)
define t = Character("Stella Cantoire", who_color= "d4af37", callback=stellavoice)
define d = Character("Dracula?", who_color= "ff9483", callback=dracvoice)
define f = Character("Freddy Ogden", who_color= "76d352", image="frog ind", callback=frogvoice)
define j = Character("Jenny Flowers", who_color= "e50548", callback=jennyvoice)
define l = Character("Lauren Palmer", who_color= "fbe55c", callback=laurenvoice)
define o = Character("Lauren Palmer", who_color= "fbe55c", callback=laurenvoice)
define i = Character("Sid Straits", who_color= "4f90b0", callback=fillvoice)
define h = Character("Shahar Syed", who_color= "dfa64c", callback=fillvoice)
###
define z = Character("?????", who_color= "FFFFFF", callback=fillvoice)
define zs = Character("?????", who_color= "f3946a", image="sam", callback=samvoice)
define zc = Character("?????", who_color= "b66baa", callback=fillvoice)
define zt = Character("?????", who_color= "d4af37", callback=stellavoice)
define zd = Character("?????", who_color= "ff9483", callback=dracvoice)
define zf = Character("?????", who_color= "76d352", callback=frogvoice)

define c = Character("Catherine Henson", who_color= "b66baa", callback=fillvoice)
define k = Character("Kaiser Maden", who_color= "b07b4c", callback=kaiservoice)
define ses = Character("Sesame the cat", who_color= "fbe55c", callback=fillvoice)
define warden = Character("Warden", who_color= "ffffff", callback=mevoice) #used in chapter 0
define scr = Character("Screen", who_color= "ffffff", what_italic = True, callback=mevoice) #used in chapter 0
define tut = Character("{i}Tutorial{/i}", who_color= "ffffff", what_italic = True, what_color = "00ff00") #used in chapter 0
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
        train_evidence1 = [False, False, False]
        train_evidence2 = [False, False, False]
        train_evidence3 = [False, False, False, False]
        lightscount = 0
        windowcount = 0

###########
#Start
###########
    jump go
