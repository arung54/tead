screen trainMap():
    imagemap:
        ground "trainMAP.png"
        hotspot(25, 19, 396, 278) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("frontCar", transition=Dissolve(0.3))]
        hotspot(22, 329, 450, 148) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("frontCar", transition=Dissolve(0.3))]
        hotspot(447, 20, 394, 276) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("midCar", transition=Dissolve(0.3))]
        hotspot(471, 327, 425, 147) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("midCar", transition=Dissolve(0.3))]
        hotspot(867, 21, 391, 280) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("backCar", transition=Dissolve(0.3))]
        hotspot(909, 320, 315, 157) action [Hide("frontCar"), Hide("midCar"), Hide("backCar"), Hide("trainMap"), Show("backCar", transition=Dissolve(0.3))]
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Hide("trainMap", transition=Dissolve(0.3))]

screen frontCar():
    add "bg trainFRONT1.png"
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3))]
    if ftecounter == 0:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png"
            action [Jump("bertAsk0")]

screen midCar():
    add "bg trainMID.png"
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3))]

screen backCar():
    add "bg trainBACK.png"
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3))]
