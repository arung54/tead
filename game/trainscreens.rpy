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
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("frontCar", transition=Dissolve(0.3)), Hide("trainMap")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay1.png")
            unhovered Hide("trainPreview")
        hotspot(542, 462, 330, 210):
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("midCar", transition=Dissolve(0.3)), Hide("trainMap")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay2.png")
            unhovered Hide("trainPreview")
        hotspot(905, 460, 329, 211):
            action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Show("backCar", transition=Dissolve(0.3)), Hide("trainMap")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay3.png")
            unhovered Hide("trainPreview")
    imagemap:
        idle "trainmapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("trainMap", transition=Dissolve(0.3))]

screen frontCar():
    add "bg trainFRONT1.png"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "map"
        action [Show("trainMap", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "sidchibi.png" at chibizoom
            action [Hide("frontCar"), Jump("sidAsk0")]
    if ftecounter == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "sidchibi.png" at chibizoom
            action [Hide("frontCar"), Jump("sidAsk1")]

screen midCar():
    add "bg trainMID.png"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "map"
        action [Show("trainMap", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png" at chibizoom
            action [Hide("midCar"), Jump("bertAsk0")]
        imagebutton:
            xpos 20
            ypos 70
            idle "catherinechibi.png" at chibizoom
            action [Hide("midCar"), Jump("cathAsk0")]
    if ftecounter == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png" at chibizoom
            action [Hide("midCar"), Jump("bertAsk1")]
        imagebutton:
            xpos 20
            ypos 70
            idle "catherinechibi.png"
            action [Hide("midCar"), Jump("cathAsk1")]

screen backCar():
    add "bg trainBACK.png"
    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "map"
        action [Show("trainMap", transition=Dissolve(0.3))]
