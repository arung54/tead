
default persistent.parallax = True
define config.gl2 = True
init python:
    import time

############################################################################# LIVE2D DEFINES ##################

image drac = Live2D("Resources/drac", base=.999, loop=True,  top=-.05,seamless=True) #good format
define drac = Character("drac")
image bert = Live2D("Resources/bert", base=.999, loop=True, top=-.05, seamless=True)
define bert = Character("bert")
image jenny = Live2D("Resources/jenny", base=.999, loop=True, top=-.05, seamless=True)
define jenny = Character("jenny")
image shahar = Live2D("Resources/shahar", base=.999, loop=True, top=-.05, seamless=True)
define shahar = Character("shahar")
image frog = Live2D("Resources/frog", base=.999, loop=True, top=-.05, seamless=True)
define frog = Character("frog")
image frog2 = Live2D("Resources/frog2", base=.999, loop=True, top=-.05, seamless=True)
define frog2 = Character("frog2")
image dan = Live2D("Resources/dan", base=.999, loop=True, top=-.05, seamless=True)
define dan = Character("dan")
image stella = Live2D("Resources/stella", base=.999, loop=True, top=-.05, seamless=True)
define stella = Character("stella")
image lauren = Live2D("Resources/lauren", base=.999, loop=True, top=-.05, seamless=True)
define lauren = Character("lauren")
image kaiser = Live2D("Resources/kaiser", base=.999, loop=True, top=-.05, seamless=True)
define kaiser = Character("kaiser")
image sam = Live2D("Resources/sam", base=.999, loop=True, top=-.05, seamless=True)
define sam = Character("sam")
image sid = Live2D("Resources/sid", base=.999, loop=True, top=-.05, seamless=True)
define sid = Character("sid")
image catherine = Live2D("Resources/catherine", base=.999, loop=True, top=-.05, seamless=True)
define catherine = Character("catherine")
image catherine2 = Live2D("Resources/catherine2", base=.999, loop=True, top=-.05, seamless=True)
define catherine2 = Character("catherine2")
image shadowyfigure = Live2D("Resources/shadowyfigure", base=.999, loop=True, seamless=True)
define shadowyfigure = Character("shadowyfigure")


############### RED GREEN COLORBLIND VERSIONS OF EVERYTHING!!!!!!!!!!!!!!!!!!!!

image dracrg = Live2D("Resources/dracrg", base=.999, loop=True, top=-.05, seamless=True) #good format
define dracrg = Character("dracrg")
image bertrg = Live2D("Resources/bertrg", base=.999, loop=True, top=-.05, seamless=True)
define bertrg = Character("bertrg")
image frogrg = Live2D("Resources/frogrg", base=.999, loop=True, top=-.05, seamless=True)
define frogrg = Character("frogrg")
image jennyrg = Live2D("Resources/jennyrg", base=.999, loop=True, top=-.05, seamless=True)
define jennyrg = Character("jennyrg")
image samrg = Live2D("Resources/samrg", base=.999, loop=True, top=-.05, seamless=True)
define samrg = Character("samrg")
image sidrg = Live2D("Resources/sidrg", base=.999, loop=True, top=-.05, seamless=True)
define sidrg = Character("sidrg")
image heads = Live2D("Resources/heads", base=.999, loop=True, top=-.05, seamless=True) #good format
define heads = Character("heads")

############### SEPIAAAAAAAAAAAAAAA!!!!!!!!!

image dracsep = Live2D("Resources/dracsep", base=.999, loop=True, top=-.05, seamless=True) #good format
define dracsep = Character("dracsep")
image bertsep = Live2D("Resources/bertsep", base=.999, loop=True, top=-.05, seamless=True)
define bertsep = Character("bertsep")
image jennysep = Live2D("Resources/jennysep", base=.999, loop=True, top=-.05, seamless=True)
define jennysep = Character("jennysep")
image shaharsep = Live2D("Resources/shaharsep", base=.999, loop=True, top=-.05, seamless=True)
define shaharsep = Character("shaharsep")
image frogsep = Live2D("Resources/frogsep", base=.999, loop=True, top=-.05, seamless=True)
define frogsep = Character("frogsep")
image dansep = Live2D("Resources/dansep", base=.999, loop=True, top=-.05, seamless=True)
define dansep = Character("dansep")
image stellasep = Live2D("Resources/stellasep", base=.999, loop=True, top=-.05, seamless=True)
define stellasep = Character("stellasep")
image laurensep = Live2D("Resources/laurensep", base=.999, loop=True, top=-.05, seamless=True)
define laurensep = Character("laurensep")
image kaisersep = Live2D("Resources/kaisersep", base=.999, loop=True, top=-.05, seamless=True)
define kaisersep = Character("kaisersep")
image samsep = Live2D("Resources/samsep", base=.999, loop=True, top=-.05, seamless=True)
define samsep = Character("samsep")
image sidsep = Live2D("Resources/sidsep", base=.999, loop=True, top=-.05, seamless=True)
define sidsep = Character("sid")
image catherinesep = Live2D("Resources/catherinesep", base=.999, loop=True, top=-.05, seamless=True)
define catherinesep = Character("catherinesep")

############################################################################# LIVE2D DEFINES ##################
init python:
    config.keymap['game_menu'].remove('mouseup_3')

init python:
    # Define function to open the menu
    def show_simple_menu():
        renpy.show_screen("simple_menu")
        renpy.restart_interaction()

    # Add key to 'open_pause_menu', this case is 'a' on keyboard
    config.keymap["open_simple_menu"] = ["mouseup_3"]
    config.underlay.append(renpy.Keymap(open_simple_menu=show_simple_menu))

#label simple_menu:
#    call screen simple_menu


image darken = "welcomescreenblank.png"
define danbox = Image("gui/textbox2.png", yalign=.5)
define bertbox = Image("gui/textbox3.png", yalign=.5)
image behappy = Image("bhappy.png", xcenter=.729, ycenter=.802)
image hamster loc:
    "bertfrlgb.png"
    pause .1
    "bertfrlg2b.png"
    pause .1
    "bertfrlgb.png"
    pause .1
    "bertfrlg3b.png"
    pause .1
    repeat


image poptear = anim.Filmstrip("poptear.png", (300,300), (5,2), .1, loop=False)
image popmad = anim.Filmstrip("popmad.png", (300,300), (5,2), .125, loop=False)
image poprace = anim.Filmstrip("poprace.png", (300,300), (2,1), .05, loop=True)
image popham = anim.Filmstrip("popham.png", (300,300), (2,1), .15, loop=True)#ycenter .205, xcenter is -.013
image poprain = anim.Filmstrip("popcloud3.png", (300,300), (5,2), .075, loop=True)
image pophearts = anim.Filmstrip("pophearts.png", (300,300), (5,2), .075, loop=False)
image popwow = anim.Filmstrip("popwow.png", (300,300), (5,2), .085, loop=False)#ycenter .25, xcenter   , zoom .75
image pophuh = anim.Filmstrip("pophuh.png", (300,300), (5,2), .085, loop=False)#ycenter .25, xcenter -.1, zoom .75

image danjumping = anim.Filmstrip("danjumpingfilm.png", (40,64), (2,1), .4, loop=True)#ycenter .25, xcenter -.1, zoom .75

############## FISHING

image fishingrod:
    contains:
        "fishrod2.png"
        zoom 2
        pause 1
        "fishrod1.png"
        zoom 2
        pause 1
        "fishrod2.png"
        zoom 2
        pause 1
        "fishrod3.png"
        zoom 2
        pause 1
        repeat
image fishingrodhooked:
    contains:
        "fishrod4.png"
        zoom 2
        pause .1
        "fishrod5.png"
        zoom 2
        pause .1
        repeat
image danfish:
    contains:
        "dansit1.png"
        zoom 2
        pause 3
        "dansit2.png"
        zoom 2
        pause .05
        "dansit1.png"
        zoom 2
        pause 7
        "dansit2.png"
        zoom 2
        pause .05
        "dansit1.png"
        zoom 2
        pause .05
        "dansit2.png"
        zoom 2
        pause .05
        repeat

################ MOVING BACKGROUNDS

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

image bg dandieslide:
    contains:
        "dandieepic.png"
        xcenter .5
        ycenter .9
        zoom 1.3
        linear 9 ycenter .35 zoom 1
        pause 5
        repeat

image bg stelladieslide:
    contains:
        "stelladieepic.png"
        xcenter .5
        ycenter -.3
        zoom 2.1
        linear 10 ycenter .4 zoom 1.2
        pause 3

image bg shahardieslide:
    contains:
        "shahardieepic.png"
        xcenter .5
        ycenter 1.2
        zoom 1.3
        linear 7 ycenter .2 zoom 1
        pause 3

image bg samdieslide:
    contains:
        "samdieepic.png"
        xcenter .7
        ycenter 1.2
        zoom 2
        linear 7 ycenter .7 xcenter .5 zoom .8
        pause 3

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

image menubgscroll:
    contains:
        "menubg.png"
        xpos -1.0
        linear 70.0 xpos 0.0
        repeat
image menubgscroll2:
    contains:
        "menuscroll.png"
        xpos -1.0
        linear 30.0 xpos 0.0
        repeat
image bg flashback:
    contains:
        "spinbg.png"
        xcenter .5 ycenter .5
        rotate 0
        linear 40 rotate 360
        repeat
        "vinegar.png"
image bg reflecting:
    contains:
        "reflecting.png"
        xcenter .5 ycenter .5
        rotate 0
        linear 40 rotate 360
        repeat
        "vinegar.png"
transform inwindow:
    truecenter zoom .8
    yalign .45

#show expression AlphaMask("testerdog", At("sid ind")) as mask
#transform wiggle:
#    linear .05 ypos+=################################################################################################ frontcar bgs
image bg frontcar5:
    "bg bertmap1.png"
    pause .5
    "bg bertmap2.png"
    pause .5
    "bg bertmap3.png"
    pause .5
    repeat

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

image gotit:
    contains:
        "igotitfg.png"
        xpos .25
        linear 2 xpos .0

init python:
    grey_images = {}
    sep_images = {}
    rg_images = {}
    blend = 0.6
    for i in renpy.display.image.images:
        try:
            grey_im_name = i + ('greyscale',)
            grey_images[grey_im_name] = im.Grayscale(renpy.display.image.images[i])
        except:
            pass
        try:
            sep_im_name = i + ('sepia',)
            sep_images[sep_im_name] = im.Sepia(renpy.display.image.images[i])
        except:
            pass
        try:
            rg_im_name = i + ('rg',)
            rg_images[rg_im_name] = im.MatrixColor(renpy.display.image.images[i],
                        [blend, 1-blend, 0.0, 0.0, 0.0,
                         1-blend, blend, 0.0, 0.0, 0.0,
                         0.0, 0.0, 1.0, 0.0, 0.0,
                         0.0, 0.0, 0.0, 1.0, 0.0 ])
        except:
            pass
    for i in grey_images:
        renpy.image(i, grey_images[i])
    for i in sep_images:
        renpy.image(i, sep_images[i])
    for i in rg_images:
        renpy.image(i, rg_images[i])
    def replacement_show(name, *args, **kwargs):
        print(name)
        live = False
        for element in name:
            if element.endswith('rg') or element.endswith('sep'):
                    live = True
                    break
        if live:
            renpy.show(name, *args, **kwargs)
        elif getattr(renpy.store, 'greyscale', False):
            renpy.show(name+('greyscale',), *args, **kwargs)
        elif getattr(renpy.store, 'sep', False):
            renpy.show(name+('sepia',), *args, **kwargs)
        elif getattr(renpy.store, 'rg', False):
            renpy.show(name+('rg',), *args, **kwargs)
        else:
            renpy.show(name, *args, **kwargs)
    config.show = replacement_show

$ passattempts = 1
##############
#Toggle Dev
##############

init python:
        noside = False
        dan = False
        laur = False
        mood = "happy"
        cat = False
init python:
    config.developer = True
    config.debug_sound = False
    renpy.music.register_channel("sfx", mixer = "sfx", loop = False)
    config.menu_include_disabled = False
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

screen killuser:
    key "mousedown_3" action Hide("nonexistent_screen")
    key "mousedown_1" action Hide("nonexistent_screen")
    key "mouseup_3" action Hide("nonexistent_screen")
    key "mouseup_1" action Hide("nonexistent_screen")

screen showchibis(chibis):
    for i in range(len(chibis)):
        add chibis[i] xpos 20 ypos 20+50*i at chibizoom

screen status_screen(location, chibi, chapter, sun):
    add "status.png"
    if sun is not None:
        add sun xpos 1165 xanchor 0 ypos 55 yanchor 0
    if chibi is not None:
        add chibi xpos 1225 xanchor 0 ypos 55 yanchor 0
    add chapter xpos 1095 xanchor 0 ypos 65 yanchor 0
    text "{b}"+location+"{/b}" xpos 1055 xanchor 0 ypos 5 yanchor 0


init python:
    def statusnt(name, person, ch, sun):
        # sunlist = [Position(xpos=1165, xanchor=0, ypos=55, yanchor=0)]
        # chibilist = [Position(xpos=1225, xanchor=0, ypos=55, yanchor=0)]
        # chapterlist = [Position(xpos=1095, xanchor=0, ypos=65, yanchor=0)]
        # renpy.show("status")
        # renpy.show(name = "location", what = Text("{b}"+name+"{/b}"), at_list = [Position(xpos=1055, xanchor=0, ypos=5, yanchor=0)])
        chapter = "ch"+str(ch)
        if sun > 0:
            sun = "sun"+str(sun)
        else:
            sun = None
        if person == "dan" or person == "bert" or person == "lauren":
            chibi = person + "chibi2"
        else:
            chibi = None
        renpy.show_screen("status_screen", location=name, chibi=chibi, chapter=chapter, sun=sun)

        # renpy.show("ch"+str(ch), at_list = chapterlist)
        # if sun == 1:
        #     renpy.show("sun1", at_list = sunlist)
        # if sun == 2:
        #     renpy.show("sun2", at_list = sunlist)
        # if sun == 3:
        #     renpy.show("sun3", at_list = sunlist)
        # if sun == 4:
        #     renpy.show("sun4", at_list = sunlist)
        # if person == "dan":
        #     renpy.show("danchibi2", at_list = chibilist)
        # if person == "bert":
        #     renpy.show("bertchibi2", at_list = chibilist)
        # if person == "lauren":
        #     renpy.show("laurenchibi2", at_list = chibilist)

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
        renpy.show_screen("showchibis", chibis=argv)
        # currchibis = list()
        # for i in renpy.get_showing_tags():
        #     if i.endswith("chibi"):
        #         currchibis.append(i)
        #
        # toremove = list()
        # for i in currchibis:
        #     if i not in argv:
        #         toremove.append(i)
        # toadd = list()
        # for i in argv:
        #     if i not in currchibis:
        #         toadd.append(i)
        # tostay = list()
        # for i in argv:
        #     if i in currchibis:
        #         tostay.append(i)
        #
        # for i in toremove:
        #     renpy.hide(i)
        #
        # y = 20
        # for i in tostay:
        #     renpy.hide(i)
        #     renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
        #     y += 50
        #
        # for i in toadd:
        #     renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, y))])
        #     y += 50


    def showchibiwindow(inlist, outlist):
        inchibi = [j + "chibi" for j in inlist]
        outchibi = [j + "chibi" for j in outlist]
        currchibis = list()
        for i in renpy.get_showing_tags():
            if i.endswith("chibi"):
                currchibis.append(i)

        toremove = list()
        for i in currchibis:
            if i not in inchibi + outchibi:
                toremove.append(i)
        toadd = list()
        for i in inchibi + outchibi:
            if i not in currchibis:
                toadd.append(i)
        tostay = list()
        for i in inchibi + outchibi:
            if i in currchibis:
                tostay.append(i)

        for i in toremove:
            renpy.hide(i)

        yin = 20
        yout = 20
        for i in tostay:
            renpy.hide(i)
            if i in inchibi:
                renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, yin))])
                yin += 50
            if i in outchibi:
                renpy.show(i, at_list = [Transform(zoom=1.5, pos=(70, yout))])
                yout += 50

        for i in toadd:
            if i in inchibi:
                renpy.show(i, at_list = [Transform(zoom=1.5, pos=(20, yin))])
                yin += 50
            if i in outchibi:
                renpy.show(i, at_list = [Transform(zoom=1.5, pos=(70, yout))])
                yout += 50

##################
#Character Defines
##################
image side bert = ConditionSwitch(
'noside', 'blank',
'mood==\"happy\" and laur', 'lhappy', 'mood==\"ind\" and laur', 'lind',
'mood==\"sigh\" and laur', 'lsigh', 'mood==\"smile\" and laur', 'lsmile',
'mood==\"happy\" and dan', 'dhappy', 'mood==\"ind\" and dan', 'dind',
'mood==\"sad\" and dan', 'dsad', 'mood==\"mad\" and dan', 'dmad',
'mood==\"shock\" and dan', 'dshock',
'mood==\"happy\" and not cat', 'bhappy', 'mood==\"ind\" and not cat', 'bind',
'mood==\"sad\" and not cat', 'bsad', 'mood==\"shock\" and not cat', 'bshock',
'mood==\"happy\" and cat', 'bchappy', 'mood==\"ind\" and cat', 'bcind',
'mood==\"sad\" and cat', 'bcsad', 'mood==\"shock\" and cat', 'bcshock', xalign=0.13, yalign=0.9)
image side notbert = ConditionSwitch(
'noside', 'blank',
'mood==\"happy\" and laur', 'ldhappy', 'mood==\"ind\" and laur', 'ldind',
'mood==\"sigh\" and laur', 'ldsigh', 'mood==\"smile\" and laur', 'ldsmile',
'mood==\"happy\" and dan', 'ddhappy', 'mood==\"ind\" and dan', 'ddind',
'mood==\"sad\" and dan', 'ddsad', 'mood==\"mad\" and dan', 'ddmad',
'mood==\"shock\" and dan', 'ddshock',
'mood==\"happy\" and not cat', 'bdhappy', 'mood==\"ind\" and not cat', 'bdind',
'mood==\"sad\" and not cat', 'bdsad', 'mood==\"shock\" and not cat', 'bdshock',
'mood==\"happy\" and cat', 'bcdhappy', 'mood==\"ind\" and cat', 'bcdind',
'mood==\"sad\" and cat', 'bcdsad', 'mood==\"shock\" and cat', 'bcdshock', xalign=0.13, yalign=0.9)
#image side dan = ConditionSwitch('mood==\"happy\"', 'dhappy', 'mood==\"ind\"', 'dind',
#'mood==\"sad\"', 'sad', 'mood==\"mad\"', 'dmad', xalign=0.13, yalign=0.9)
#image side dan = ConditionSwitch('mood==\"happy\"', 'dhappy', 'mood==\"ind\"', 'dind',
#'mood==\"sad\"', 'sad', 'mood==\"mad\"', 'dmad', xalign=0.13, yalign=0.9)

define m = Character("Me?", callback=fillvoice, who_color = "FFFFFF", image="bert")
define mi = Character("Me?", callback=fillvoice, what_italic=True, who_color = "FFFFFF", image="bert")
define n = Character("Dan Scagnelli", callback=fillvoice, who_color = "FFFFFF", image="bert")
define ni = Character("Dan Scagnellii", callback=fillvoice, what_italic=True, who_color = "FFFFFF", image="bert") #Dan Internal, name and text italics
define np = Character("Dan Scagnelli", callback=mevoice, who_color = "FFFFFF", window_background=danbox, image="bert")
define bi = Character("Bert Kimi", who_color= "78AB46", callback=bertvoice, what_italic = True, image="bert") #Bert Internal, name and text italics /// use {i}Bert Kim{/i} if text
define li = Character("Lauren Palmeri", who_color= "fbe55c", callback=laurenvoice, what_italic = True, image="bert")
define lf = Character("Lauren Palmer", who_color= "fbe55c", callback=laurenvoice, image="bert") #First person Lauren
define bp = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice, window_background=bertbox, image="notbert")
define bt = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice, image="notbert") #Third person Bert
define b = Character("Bert Kim", who_color= "#78AB46", callback=bertvoice, image="bert")
define s = Character("Sam Lee", who_color= "f3946a", image="notbert", callback=samvoice)
define t = Character("Stella Cantoire", who_color= "d4af37", callback=stellavoice, image="notbert")
define d = Character("Dracula", who_color= "ff9483", callback=dracvoice, image="notbert") #Changed fromv Dracula?
define dr = Character("Ivan Nepomniachtchi", who_color= "ff9483", callback=dracvoice, image="notbert")
define f = Character("Freddy Ogden", who_color= "76d352", image="notbert", callback=frogvoice)
define j = Character("Jenny Flowers", who_color= "e50548", callback=jennyvoice, image="notbert")
define l = Character("Lauren Palmer", who_color= "fbe55c", callback=laurenvoice, image="notbert")
define o = Character("Lauren Palmer", who_color= "fbe55c", callback=laurenvoice, image="notbert")
define i = Character("Sid Straits", who_color= "4f90b0", callback=fillvoice, image="notbert")
define h = Character("Shahar Syed", who_color= "dfa64c", callback=fillvoice, image="notbert")
###
define z = Character("Question", who_color= "FFFFFF", callback=fillvoice, image="notbert") #changed from ?????
define zg = Character("Questiong", who_color= "999999", callback=fillvoice, image="notbert")
define zb = Character("Questionb", who_color= "000099", callback=fillvoice, image="notbert")
define zs = Character("Questions", who_color= "f3946a", callback=samvoice, image="notbert")
define zc = Character("Questionc", who_color= "b66baa", callback=fillvoice, image="notbert")
define zt = Character("Questiont", who_color= "d4af37", callback=stellavoice, image="notbert")
define zd = Character("Questiond", who_color= "ff9483", callback=dracvoice, image="notbert")
define zf = Character("Questionf", who_color= "76d352", callback=frogvoice, image="notbert")
define zi = Character("Questioni", who_color= "4f90b0", callback=fillvoice, image="notbert")
define zr = Character("Questionr", who_color= "4f90b0", callback=fillvoice, image="notbert")
define zh = Character("Questionh", who_color= "b66baa", callback=fillvoice, image="notbert")
define sy = Character("Questionsy", who_color= "f3946a", callback=samvoice, image="notbert")
define syc = Character("Questionsyc", who_color= "b66baa", callback=fillvoice, image="notbert")
define syci = Character("Questionsyci", who_color= "b66baa", callback=fillvoice, image="notbert")


define c = Character("Catherine Henson", who_color= "b66baa", callback=fillvoice, image="notbert")
define k = Character("Kaiser Maden", who_color= "b07b4c", callback=kaiservoice, image="notbert")
define ses = Character("Sesame the cat", who_color= "fbe55c", callback=fillvoice, image="notbert")
define warden = Character("Warden", who_color= "ffffff", callback=mevoice, image="notbert") #used in chapter 0
define scr = Character("Screen", who_color= "ffffff", what_italic = True, callback=mevoice, image="notbert") #used in chapter 0
define tut = Character("Tutorial", who_color= "ffffff", what_italic = True, what_color = "00ff00") #used in chapter 0
define intercom = Character("Intercom", what_italic=True, callback=fillvoice, image="notbert") #blank text, always italics
define blank = Character("blank", what_italic=True, callback=fillvoice) #blank text, always italics /// used to " ", changed to the word blank for image use

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
        pers = ""

##################
#Trial Variables
##################
        currEvidence = -1
        phase = 0
        statement = -1
        agree = 0
        train_evidence1 = [True, True, True]
        train_evidence2 = [True, True, True]                #made all of these true from false LOL
        train_evidence3 = [True, True, True, True]
        train_extra = [False, False, False, False, False, False]
        mans_evidence = [True] * 9
        hosp_evidence = [False] * 13
        bank_evidence = [True] + [False] * 11
        mans_extra = [False] * 11
        hosp_extra = [False] * 6
        bank_extra = [False] * 20
        lightscount = 0
        windowcount = 0
        mistakes = 0

########## julian trying shit area

transform parallax:
    perspective True
    subpixel True
    zpos -18
    function moving_camera

transform paralloff:
    perspective True
    subpixel True
    zpos 0
    function fixed_camera

camera at parallax

python:
    def moving_camera(trans, st, at):
        if persistent.parallax:
            x, y = renpy.display.draw.get_mouse_pos()
            trans.xoffset = (x - config.screen_width / 2) *.02    # make this = 0 to turn off parallax
            trans.yoffset = (y - config.screen_height / 2) *.02   # make this = 0 to turn off parallax
        else:
            trans.xoffset = 0
            trans.yoffset = 0
        return 0

python:
    def fixed_camera(trans, st, at):
        if persistent.parallax:
            x, y = renpy.display.draw.get_mouse_pos()
            trans.xoffset = (x - config.screen_width / 2) *.0    # make this = 0 to turn off parallax
            trans.yoffset = (y - config.screen_height / 2) *.0   # make this = 0 to turn off parallax
        else:
            trans.xoffset = 0
            trans.yoffset = 0
        return 0

transform bg:
    truecenter()
    zzoom True
    zpos -200

###########
#Start
###########
camera at parallax
$dan = False
stop music #"audio/haunted.mp3" fadeout 1.0
jump testwindow
