init:
    transform chibizoom2:
        zoom 3.0
    transform heartzoom:
        zoom 4.5

screen freeTimeCounter():
    imagebutton:
        idle "goback.png"
        xalign 1.0
        yalign 1.0
        action [Hide("freeTimeCounter")]
    if ftecounter < 2:
        vbox xalign 0.1 yalign 0.5 spacing 50:
            image "bertchibi.png" at chibizoom2
            image "catherinechibi.png" at chibizoom2
            image "draculachibi.png" at chibizoom2
            image "freddychibi.png" at chibizoom2
            image "jennychibi.png" at chibizoom2
            image "kaiserchibi.png" at chibizoom2
        vbox xalign 0.2 yalign 0.5 spacing 50:
            if fte_bert <= -2:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_cath <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_drac <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_frog <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_jenn <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_kais <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
        vbox xalign 0.3 yalign 0.5 spacing 50:
            if fte_bert <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_cath <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_drac <= 0:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_frog <= 0:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_jenn <= 0:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_kais <= 0:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
        vbox xalign 0.4 yalign 0.5 spacing 50:
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
        vbox xalign 0.6 yalign 0.11 spacing 50:
            image "laurenchibi.png" at chibizoom2
            image "samchibi.png" at chibizoom2
            image "shaharchibi.png" at chibizoom2
            image "sidchibi.png" at chibizoom2
            image "stellachibi.png" at chibizoom2
        vbox xalign 0.7 yalign 0.11 spacing 50:
            if fte_laur <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_sam <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_shah <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_sid <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
            if fte_stel <= -1:
                image "emptyheart" at heartzoom
            else:
                image "fullheart" at heartzoom
        vbox xalign 0.8 yalign 0.11 spacing 50:
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
        vbox xalign 0.9 yalign 0.11 spacing 50:
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
            image "emptyheart" at heartzoom
