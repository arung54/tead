init:
    transform chibizoom2:
        zoom 3.0

label postFTEHandler:
    if ftecounter == 0:
        jump postFT0

    if ftecounter == 1:
        jump postFT1

screen skipFT():
    modal True
    imagemap:
        ground "skipfreetime.png"
        hotspot(739, 388, 294, 182):
            action[Hide("skipFT", transition=Dissolve(0.3))]
            if ftecounter == 0:
                hotspot(262, 386, 293, 185):
                    action [Hide("frontCar", transition=Dissolve(0.3)), Hide("midCar", transition=Dissolve(0.3)),
                    Hide("backCar", transition=Dissolve(0.3)), Hide("skipFT", transition=Dissolve(0.3)),
                    Jump("postFTE0")]
            if ftecounter == 1:
                hotspot(262, 386, 293, 185):
                    action [Hide("frontCar", transition=Dissolve(0.3)), Hide("midCar", transition=Dissolve(0.3)),
                    Hide("backCar", transition=Dissolve(0.3)), Hide("skipFT", transition=Dissolve(0.3)),
                    Jump("postFTE1")]

screen freeTimeCounter():
    modal True
    imagebutton:
        idle "goback.png"
        xalign 1.0
        yalign 1.0
        action [Hide("freeTimeCounter", transition=Dissolve(0.3))]
    if ftecounter < 2:
        vbox xalign 0.18 yalign 0.5 spacing 50:
            image "bertchibi.png" at chibizoom2
            image "catherinechibi.png" at chibizoom2
            image "draculachibi.png" at chibizoom2
            image "freddychibi.png" at chibizoom2
            image "jennychibi.png" at chibizoom2
            image "kaiserchibi.png" at chibizoom2
        vbox xalign 0.27 yalign 0.5 spacing 62:
            if fte_bert <= -2:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_cath <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_drac <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_frog <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_jenn <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_kais <= -1:
                image "emptyheart"
            else:
                image "fullheart"
        vbox xalign 0.34 yalign 0.5 spacing 62:
            if fte_bert <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_cath <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_drac <= 0:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_frog <= 0:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_jenn <= 0:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_kais <= 0:
                image "emptyheart"
            else:
                image "fullheart"
        vbox xalign 0.41 yalign 0.5 spacing 62:
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
        vbox xalign 0.68 yalign 0.11 spacing 50:
            image "laurenchibi.png" at chibizoom2
            image "samchibi.png" at chibizoom2
            image "shaharchibi.png" at chibizoom2
            image "sidchibi.png" at chibizoom2
            image "stellachibi.png" at chibizoom2
        vbox xalign 0.77 yalign 0.15 spacing 62:
            if fte_laur <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_sam <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_shah <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_sid <= -1:
                image "emptyheart"
            else:
                image "fullheart"
            if fte_stel <= -1:
                image "emptyheart"
            else:
                image "fullheart"
        vbox xalign 0.84 yalign 0.15 spacing 62:
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
        vbox xalign 0.91 yalign 0.15 spacing 62:
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
            image "emptyheart"
