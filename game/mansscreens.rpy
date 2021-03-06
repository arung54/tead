screen mansMap():
    #TODO: Gate rooms for FT4
    #TODO: Create secret sesame FTE
    imagemap:
        ground "mansMapoverlay.png"
        hotspot(762, 310, 155, 174):
            action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("kitchen", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay1.png")
            unhovered Hide("mansPreview")
        hotspot(920, 311, 329, 175):
            action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("dining", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(1090, 489, 160, 195):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("garage", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(153, 471, 561, 69):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("hallway", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(153, 539, 77, 145):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("hallway", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(152, 310, 156, 157):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroomFL", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(307, 310, 83, 83):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroomFL", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(497, 310, 218, 158):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroom", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(234, 544, 225, 140):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroom", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(463, 543, 251, 141):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("masterBedroom", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(393, 310, 101, 158):
            if ftecounter != 4:
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bathroom", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")

    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("mansMap", transition=Dissolve(0.3)), Hide("mansPreview")]

screen kitchen():
    add "bg mansionkitchen.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
    if ftecounter == 2:
        imagebutton:
            xpos 20
            ypos 20
            idle "catherinechibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("cathAsk2")]
        imagebutton:
            xpos 20
            ypos 70
            idle "shaharchibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("shahAsk2")]
        imagebutton:
            xpos 20
            ypos 120
            idle "stellachibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("stelAsk2")]
    if ftecounter == 3:
        imagebutton:
            xpos 20
            ypos 20
            idle "catherinechibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("cathAsk3")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("jennAsk3")]
        imagebutton:
            xpos 20
            ypos 120
            idle "samchibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("samAsk3")]
    if ftecounter == 4:
        imagebutton:
            xpos 20
            ypos 20
            idle "catherinechibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("cathAsk4")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("kitchen", transition = Dissolve(1.0)), Jump("jennAsk4")]

screen dining():
    add "bg mansiondining.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
    if ftecounter == 3:
        imagebutton:
            xpos 20
            ypos 20
            idle "shaharchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("shahAsk3")]
        imagebutton:
            xpos 20
            ypos 70
            idle "stellachibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("stelAsk3")]
    if ftecounter == 4:
        imagebutton:
            xpos 20
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("dracAsk4")]
        imagebutton:
            xpos 20
            ypos 70
            idle "freddychibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("frogAsk4")]
        imagebutton:
            xpos 20
            ypos 120
            idle "laurenchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("laurAsk4")]
        imagebutton:
            xpos 20
            ypos 170
            idle "samchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("samAsk4")]
        imagebutton:
            xpos 20
            ypos 220
            idle "shaharchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("shahAsk4")]
        imagebutton:
            xpos 20
            ypos 270
            idle "sidchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("sidAsk4")]
        imagebutton:
            xpos 20
            ypos 320
            idle "stellachibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("stelAsk4")]
        imagebutton:
            xpos 20
            ypos 370
            idle "sidchibi.png" at chibizoom
            action [Hide("dining", transition = Dissolve(1.0)), Jump("sidAsk4")]

screen garage():
    add "bg mansiongarage.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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

screen hallway():
    add "bg mansionhall.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
    if ftecounter == 2:
        imagebutton:
            xpos 20
            ypos 20
            idle "jennychibi.png" at chibizoom
            action [Hide("hallway", transition = Dissolve(1.0)), Jump("jennAsk2")]

screen bedroom():
    add "bg mansionbedroom.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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

screen bedroomFL():
    add "bg mansionbedroom.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
    if ftecounter == 2:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("bedroomFL", transition = Dissolve(1.0)), Jump("frogAsk2")]
        imagebutton:
            xpos 20
            ypos 70
            idle "laurenchibi.png" at chibizoom
            action [Hide("bedroomFL", transition = Dissolve(1.0)), Jump("laurAsk2")]
    if ftecounter == 3:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("bedroomFL", transition = Dissolve(1.0)), Jump("frogAsk3")]
        imagebutton:
            xpos 20
            ypos 70
            idle "laurenchibi.png" at chibizoom
            action [Hide("bedroomFL", transition = Dissolve(1.0)), Jump("laurAsk3")]

screen masterBedroom():
    add "bg mansionmasterbedroom.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
    if ftecounter == 2:
        imagebutton:
            xpos 20
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("masterBedroom", transition = Dissolve(1.0)), Jump("dracAsk2")]
        imagebutton:
            xpos 20
            ypos 70
            idle "samchibi.png" at chibizoom
            action [Hide("masterBedroom", transition = Dissolve(1.0)), Jump("samAsk2")]
        imagebutton:
            xpos 20
            ypos 120
            idle "sidchibi.png" at chibizoom
            action [Hide("masterBedroom", transition = Dissolve(1.0)), Jump("sidAsk2")]
    if ftecounter == 3:
        imagebutton:
            xpos 20
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("masterBedroom", transition = Dissolve(1.0)), Jump("dracAsk3")]
        imagebutton:
            xpos 20
            ypos 70
            idle "sidchibi.png" at chibizoom
            action [Hide("masterBedroom", transition = Dissolve(1.0)), Jump("sidAsk3")]

screen bathroom():
    add "bg mansionmasterbr.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansMap", transition=Dissolve(0.3))]
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
