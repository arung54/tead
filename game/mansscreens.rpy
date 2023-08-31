screen mansionmap():
    modal True
    imagemap:
        if ftecounter == 2:
            ground "ftemap2.png"
        if ftecounter == 3:
            ground "ftemap3.png"
        if ftecounter == 4:
            ground "ftemap4.png"
        hotspot(760, 353, 157, 158):
            action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("kitchen", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="mansionmapoverlay3.png")
            unhovered Hide("mapPreview")
        hotspot(918, 353, 332, 158):
            action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("dining", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="mansionmapoverlay1.png")
            unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(1087, 510, 163, 180):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("garage", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay2.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(151, 496, 562, 65):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("hallway", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay4.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(154, 554, 78, 136):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("hallway", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay4.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(152, 353, 157, 143):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroom", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay6.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(306, 354, 84, 75):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroom", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay6.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(230, 562, 231, 128):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bedroomFL", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay7.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(460, 561, 253, 128):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("masterBedroom", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay8.png")
                unhovered Hide("mapPreview")
        if ftecounter != 4:
            hotspot(393, 355, 101, 141):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("bathroom", transition=Dissolve(0.3)), Hide("mansionmap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="mansionmapoverlay5.png")
                unhovered Hide("mapPreview")

    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("mansionmap", transition=Dissolve(0.3)), Hide("mapPreview")]

screen kitchen():
    add "bg mansionkitchen.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    if ftecounter == 2:
        add "bg nmansiondining.png"
    else:
        add "bg mansiondining.png"
    add "status.png"
    add Text("{b}Dining Room{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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

screen garage():
    add "bg mansiongarage.png"
    add "status.png"
    add Text("{b}Garage{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    add Text("{b}Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    add "bg mansionbedroom1.png"
    add "status.png"
    add Text("{b}Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    add "bg mansionbedroom2.png"
    add "status.png"
    add Text("{b}Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    add Text("{b}Master Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
    add "bg mansionbr.png"
    add "status.png"
    add Text("{b}Bathroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 2:
        add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 3:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 4:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("mansionmap", transition=Dissolve(0.3))]
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
