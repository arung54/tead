
image splash = "tead.png"
image darken = "welcomescreenblank.png"

##############
#Toggle Dev
##############

init python:
    config.developer = True

##############
#Voice Defines
##############

init python:
    def samvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("voi3.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def fillvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("fill.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def mevoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("voi.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def bertvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("voi4.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def dracvoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("pencil.mp3")
        elif event == "slow_done":
            renpy.sound.stop()
init python:
    def stellavoice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play("voi2.mp3")
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


##################
#Character Defines
##################

define m = Character("Me?", callback=mevoice)
define n = Character("Dan Scagnelli", callback=mevoice, who_color = "FFFFFF")
define ni = Character("{i}Dan Scagnelli{/i}", callback=mevoice, what_italic=True, who_color = "FFFFFF") #Dan Internal, name and text italics
define bi = Character("{i}Bert Kim{/i}", who_color= "#78AB46", callback=bertvoice, what_italics=True) #Bert Internal, name and text ite
define b = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice)
define s = Character("Sam Lee", who_color= "f3946a", image="sam", callback=samvoice)
define t = Character("Stella Cantoire", who_color= "#d4af37", callback=stellavoice)
define d = Character("Dracula?", who_color= "ff9483", callback=dracvoice)
define f = Character("Freddy Ogden", who_color= "76d352", image="frog ind", callback=fillvoice)
define j = Character("Jenny Flowers", who_color= "e50548", callback=fillvoice)
define o = Character("Cydney Palmer", who_color= "fbe55c", callback=fillvoice)
define i = Character("Sid Straits", who_color= "4f90b0", callback=fillvoice)
define h = Character("Shahar Syed", who_color= "dfa64c", callback=fillvoice)
define z = Character("?????", who_color= "#FFFFFF", callback=fillvoice)
define c = Character("Catherine Henson", who_color= "b66baa", callback=fillvoice)
define k = Character("Kaiser Maden", who_color= "b07b4c", callback=fillvoice)
define ses = Character("Sesame the cat", who_color= "fbe55c", callback=fillvoice)
define blank = Character(" ", what_italic=True, callback=fillvoice) #blank text, always italics

###########
#Start jump
###########


label start:

##################
#Free Time Counters
##################
    $ ftecounter = 0
    $ fte_bert = 0
    $ fte_sam = 0
    $ fte_stell = 0
    $ fte_drac = 0
    $ fte_fred = 0
    $ fte_jenn = 0
    $ fte_laur = 0
    $ fte_sid = 0
    $ fte_shah = 0
    $ fte_cath = 0
    $ fte_kais = 0
    $ train_evidence = [False, False, False, False, False, False]

    jump midcar3
