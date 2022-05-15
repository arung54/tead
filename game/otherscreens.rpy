init:
    transform chibizoom2:
        zoom 3.0
    transform shrinkcard:
        xsize 1.0
        linear 0.5 xsize 0.0
    transform growcard:
        xsize 0.0
        linear 0.5 xsize 1.0
    python:
        def hideCards():
            renpy.hide_screen("cardcatf")
            renpy.hide_screen("cardcatftob")
            renpy.hide_screen("cardcatbtof")
            renpy.hide_screen("cardberf")
            renpy.hide_screen("cardberftob")
            renpy.hide_screen("cardberbtof")
            renpy.hide_screen("carddanf")
            renpy.hide_screen("carddanftob")
            renpy.hide_screen("carddanbtof")
            renpy.hide_screen("carddraf")
            renpy.hide_screen("carddraftob")
            renpy.hide_screen("carddrabtof")
            renpy.hide_screen("cardfref")
            renpy.hide_screen("cardfreftob")
            renpy.hide_screen("cardfrebtof")
            renpy.hide_screen("cardjenf")
            renpy.hide_screen("cardjenftob")
            renpy.hide_screen("cardjenbtof")
            renpy.hide_screen("cardkaif")
            renpy.hide_screen("cardkaiftob")
            renpy.hide_screen("cardkaibtof")
            renpy.hide_screen("cardlauf")
            renpy.hide_screen("cardlauftob")
            renpy.hide_screen("cardlaubtof")
            renpy.hide_screen("cardsamf")
            renpy.hide_screen("cardsamftob")
            renpy.hide_screen("cardsambtof")
            renpy.hide_screen("cardshaf")
            renpy.hide_screen("cardshaftob")
            renpy.hide_screen("cardshabtof")
            renpy.hide_screen("cardsidf")
            renpy.hide_screen("cardsidftob")
            renpy.hide_screen("cardsidbtof")
            renpy.hide_screen("cardstef")
            renpy.hide_screen("cardsteftob")
            renpy.hide_screen("cardstebtof")
    image catcardF:
        "cardcatf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image catcardFtoB:
        "cardcatf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardcatb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image catcardBtoF:
        "cardcatb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardcatf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image bercardF:
        "cardberf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image bercardFtoB:
        "cardberf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardberb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image bercardBtoF:
        "cardberb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardberf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dancardF:
        "carddanf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dancardFtoB:
        "carddanf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "carddanb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dancardBtoF:
        "carddanb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "carddanf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dracardF:
        "carddraf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dracardFtoB:
        "carddraf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "carddrab.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image dracardBtoF:
        "carddrab.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "carddraf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image frecardF:
        "cardfref.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image frecardFtoB:
        "cardfref.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardfreb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image frecardBtoF:
        "cardfreb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardfref.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image jencardF:
        "cardjenf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image jencardFtoB:
        "cardjenf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardjenb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image jencardBtoF:
        "cardjenb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardjenf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image kaicardF:
        "cardkaif.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image kaicardFtoB:
        "cardkaif.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardkaib.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image kaicardBtoF:
        "cardkaib.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardkaif.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image laucardF:
        "cardlauf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image laucardFtoB:
        "cardlauf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardlaub.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image laucardBtoF:
        "cardlaub.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardlauf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image samcardF:
        "cardsamf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image samcardFtoB:
        "cardsamf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardsamb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image samcardBtoF:
        "cardsamb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardsamf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image shacardF:
        "cardshaf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image shacardFtoB:
        "cardshaf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardshab.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image shacardBtoF:
        "cardshab.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardshaf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image sidcardF:
        "cardsidf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image sidcardFtoB:
        "cardsidf.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardsidb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image sidcardBtoF:
        "cardsidb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardsidf.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image stecardF:
        "cardstef.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image stecardFtoB:
        "cardstef.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardsteb.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0
    image stecardBtoF:
        "cardsteb.png"
        xzoom 1.0 xanchor 0.5
        linear 0.6 xzoom 0.0
        "cardstef.png"
        xzoom 0.01 xanchor 0.5
        linear 0.6 xzoom 1.0

label postFTEHandler:
    $renpy.jump("postFT"+str(ftecounter))

screen skipFT():
    add "scary.png"
    modal True
    imagemap:
        ground "skipfreetime.png"
        hotspot(739, 388, 294, 182):
            action[Hide("skipFT", transition=Dissolve(0.3))]
        hotspot(262, 386, 293, 185):
            action [Hide("frontCar", transition=Dissolve(0.3)), Hide("midCar", transition=Dissolve(0.3)),
            Hide("backCar", transition=Dissolve(0.3)), Hide("skipFT", transition=Dissolve(0.3)),
            Jump("postFT"+str(ftecounter))]

screen freeTimeCounter():
    imagemap:
        ground "characterscreen.png"
        if pers != "ber":
            hotspot(41, 418, 112, 41):
                action[SetVariable("pers", "ber"), Function(hideCards), Show("cardberf")]
        if pers != "cat":
            hotspot(42, 465, 165, 40):
                action[SetVariable("pers", "cat"), Function(hideCards), Show("cardcatf")]
        if pers != "dan":
            hotspot(42, 515, 98, 35):
                action[SetVariable("pers", "dan"), Function(hideCards), Show("carddanf")]
        if pers != "dra":
            hotspot(41, 561, 139, 37):
                action[SetVariable("pers", "dra"), Function(hideCards), Show("carddraf")]
        if pers != "fre":
            hotspot(42, 607, 131, 33):
                action[SetVariable("pers", "fre"), Function(hideCards), Show("cardfref")]
        if pers != "jen":
            hotspot(43, 655, 120, 33):
                action[SetVariable("pers", "jen"), Function(hideCards), Show("cardjenf")]
        if pers != "kai":
            hotspot(444, 470, 127, 32):
                action[SetVariable("pers", "kai"), Function(hideCards), Show("cardkaif")]
        if pers != "lau":
            hotspot(443, 426, 133, 30):
                action[SetVariable("pers", "lau"), Function(hideCards), Show("cardlauf")]
        if pers != "sam":
            hotspot(445, 512, 108, 36):
                action[SetVariable("pers", "sam"), Function(hideCards), Show("cardsamf")]
        if pers != "sha":
            hotspot(443, 559, 132, 38):
                action[SetVariable("pers", "sha"), Function(hideCards), Show("cardshaf")]
        if pers != "sid":
            hotspot(440, 605, 98, 40):
                action[SetVariable("pers", "sid"), Function(hideCards), Show("cardsidf")]
        if pers != "ste":
            hotspot(440, 653, 127, 36):
                action[SetVariable("pers", "ste"), Function(hideCards), Show("cardstef")]

screen cardcatf():
    imagebutton:
        idle "catcardF" xpos 1000 ycenter 0.5 action[Hide("cardcatf"), Show("cardcatftob")]
screen cardcatftob():
    imagebutton:
        idle "catcardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardcatftob"), Show("cardcatbtof")]
screen cardcatbtof():
    imagebutton:
        idle "catcardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardcatbtof"), Show("cardcatftob")]

screen cardberf():
    imagebutton:
        idle "bercardF" xpos 1000 ycenter 0.5 action[Hide("cardberf"), Show("cardberftob")]
screen cardberftob():
    imagebutton:
        idle "bercardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardberftob"), Show("cardberbtof")]
screen cardberbtof():
    imagebutton:
        idle "bercardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardberbtof"), Show("cardberftob")]

screen carddanf():
    imagebutton:
        idle "dancardF" xpos 1000 ycenter 0.5 action[Hide("carddanf"), Show("carddanftob")]
screen carddanftob():
    imagebutton:
        idle "dancardFtoB" xpos 1000 ycenter 0.5 action[Hide("carddanftob"), Show("carddanbtof")]
screen carddanbtof():
    imagebutton:
        idle "dancardBtoF" xpos 1000 ycenter 0.5 action[Hide("carddanbtof"), Show("carddanftob")]

screen carddraf():
    imagebutton:
        idle "dracardF" xpos 1000 ycenter 0.5 action[Hide("carddraf"), Show("carddraftob")]
screen carddraftob():
    imagebutton:
        idle "dracardFtoB" xpos 1000 ycenter 0.5 action[Hide("carddraftob"), Show("carddrabtof")]
screen carddrabtof():
    imagebutton:
        idle "dracardBtoF" xpos 1000 ycenter 0.5 action[Hide("carddrabtof"), Show("carddraftob")]

screen cardfref():
    imagebutton:
        idle "frecardF" xpos 1000 ycenter 0.5 action[Hide("cardfref"), Show("cardfreftob")]
screen cardfreftob():
    imagebutton:
        idle "frecardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardfreftob"), Show("cardfrebtof")]
screen cardfrebtof():
    imagebutton:
        idle "frecardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardfrebtof"), Show("cardfreftob")]

screen cardjenf():
    imagebutton:
        idle "jencardF" xpos 1000 ycenter 0.5 action[Hide("cardjenf"), Show("cardjenftob")]
screen cardjenftob():
    imagebutton:
        idle "jencardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardjenftob"), Show("cardjenbtof")]
screen cardjenbtof():
    imagebutton:
        idle "jencardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardjenbtof"), Show("cardjenftob")]

screen cardkaif():
    imagebutton:
        idle "kaicardF" xpos 1000 ycenter 0.5 action[Hide("cardkaif"), Show("cardkaiftob")]
screen cardkaiftob():
    imagebutton:
        idle "kaicardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardkaiftob"), Show("cardkaibtof")]
screen cardkaibtof():
    imagebutton:
        idle "kaicardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardkaibtof"), Show("cardkaiftob")]

screen cardlauf():
    imagebutton:
        idle "laucardF" xpos 1000 ycenter 0.5 action[Hide("cardlauf"), Show("cardlauftob")]
screen cardlauftob():
    imagebutton:
        idle "laucardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardlauftob"), Show("cardlaubtof")]
screen cardlaubtof():
    imagebutton:
        idle "laucardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardlaubtof"), Show("cardlauftob")]

screen cardsamf():
    imagebutton:
        idle "samcardF" xpos 1000 ycenter 0.5 action[Hide("cardsamf"), Show("cardsamftob")]
screen cardsamftob():
    imagebutton:
        idle "samcardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardsamftob"), Show("cardsambtof")]
screen cardsambtof():
    imagebutton:
        idle "samcardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardsambtof"), Show("cardsamftob")]

screen cardshaf():
    imagebutton:
        idle "shacardF" xpos 1000 ycenter 0.5 action[Hide("cardshaf"), Show("cardshaftob")]
screen cardshaftob():
    imagebutton:
        idle "shacardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardshaftob"), Show("cardshabtof")]
screen cardshabtof():
    imagebutton:
        idle "shacardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardshabtof"), Show("cardshaftob")]

screen cardsidf():
    imagebutton:
        idle "sidcardF" xpos 1000 ycenter 0.5 action[Hide("cardsidf"), Show("cardsidftob")]
screen cardsidftob():
    imagebutton:
        idle "sidcardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardsidftob"), Show("cardsidbtof")]
screen cardsidbtof():
    imagebutton:
        idle "sidcardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardsidbtof"), Show("cardsidftob")]

screen cardstef():
    imagebutton:
        idle "stecardF" xpos 1000 ycenter 0.5 action[Hide("cardstef"), Show("cardsteftob")]
screen cardsteftob():
    imagebutton:
        idle "stecardFtoB" xpos 1000 ycenter 0.5 action[Hide("cardsteftob"), Show("cardstebtof")]
screen cardstebtof():
    imagebutton:
        idle "stecardBtoF" xpos 1000 ycenter 0.5 action[Hide("cardstebtof"), Show("cardsteftob")]
