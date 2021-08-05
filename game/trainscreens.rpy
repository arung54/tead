init:
    image map:
        "mapicon.png"
        zoom 0.3

screen trainPreview(img):
    add img pos (25, 20)

##############################################


screen trainMap():
    imagemap:
        ground "trainmapoverlay.png"
        hotspot(182, 461, 330, 210):
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("frontCar", transition=Dissolve(0.3)), Hide("trainMap"), Hide("trainPreview")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay1.png")
            unhovered Hide("trainPreview")
        hotspot(542, 462, 330, 210):
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("midCar", transition=Dissolve(0.3)), Hide("trainMap"), Hide("trainPreview")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay2.png")
            unhovered Hide("trainPreview")
        hotspot(905, 460, 329, 211):
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("backCar", transition=Dissolve(0.3)), Hide("trainMap"), Hide("trainPreview")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay3.png")
            unhovered Hide("trainPreview")
    imagemap:
        idle "trainmapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("trainMap", transition=Dissolve(0.3)), Hide("trainPreview")]

screen frontCar():
    add "bg trainFRONT1.png"
    add "status.png"
    add Text("{b}Front Car{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch1.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "danchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("trainMap", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "hearticon" at iconzoom
        action [Show("freeTimeCounter", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.375
        idle "skipicon" at iconzoom
        if ftecounter > 0:
            action [Show("skipFT", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("bertAsk0")]
        imagebutton:
            xpos 20
            ypos 70
            idle "kaiserchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("kaisAsk0")]
        imagebutton:
            xpos 20
            ypos 120
            idle "shaharchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("shahAsk0")]
        imagebutton:
            xpos 20
            ypos 170
            idle "samchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("samAsk0")]
    if ftecounter == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("bertAsk1")]
        imagebutton:
            xpos 20
            ypos 70
            idle "kaiserchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("kaisAsk1")]
        imagebutton:
            xpos 20
            ypos 120
            idle "shaharchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("shahAsk1")]
        imagebutton:
            xpos 20
            ypos 170
            idle "samchibi.png" at chibizoom
            action [Hide("frontCar", transition = Dissolve(1.0)), Jump("samAsk2")]

screen midCar():
    add "bg trainMID.png"
    add "status.png"
    add Text("{b}Bar Car{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch1.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "danchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("trainMap", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "hearticon" at iconzoom
        action [Show("freeTimeCounter", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.375
        idle "skipicon" at iconzoom
        if ftecounter > 0:
            action [Show("skipFT", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "jennychibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("jennAsk0")]
        imagebutton:
            xpos 20
            ypos 70
            idle "stellachibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("stelAsk0")]
        imagebutton:
            xpos 20
            ypos 120
            idle "laurenchibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("laurAsk0")]
        imagebutton:
            xpos 20
            ypos 170
            idle "freddychibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("frogAsk0")]
        imagebutton:
            xpos 20
            ypos 220
            idle "sidchibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("sidAsk0")]
    if ftecounter == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "jennychibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("jennAsk1")]
        imagebutton:
            xpos 20
            ypos 70
            idle "stellachibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("stelAsk1")]
        imagebutton:
            xpos 20
            ypos 120
            idle "laurenchibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("laurAsk1")]
        imagebutton:
            xpos 20
            ypos 170
            idle "freddychibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("frogAsk1")]
        imagebutton:
            xpos 20
            ypos 220
            idle "sidchibi.png" at chibizoom
            action [Hide("midCar", transition = Dissolve(1.0)), Jump("sidAsk1")]

screen backCar():
    add "bg trainBACK.png"
    add "status.png"
    add Text("{b}Caboose{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch1.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "danchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("trainMap", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "hearticon" at iconzoom
        action [Show("freeTimeCounter", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 0.375
        idle "skipicon" at iconzoom
        if ftecounter > 0:
            action [Show("skipFT", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("backCar", transition = Dissolve(1.0)), Jump("dracAsk0")]
        imagebutton:
            xpos 20
            ypos 70
            idle "catherinechibi.png" at chibizoom
            action [Hide("backCar", transition = Dissolve(1.0)), Jump("cathAsk0")]
    if ftecounter == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("backCar", transition = Dissolve(1.0)), Jump("dracAsk1")]
        imagebutton:
            xpos 20
            ypos 70
            idle "catherinechibi.png" at chibizoom
            action [Hide("backCar", transition = Dissolve(1.0)), Jump("cathAsk1")]
