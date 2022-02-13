screen hospMap():
    modal True
    #TODO: Create secret sesame FTE
    if ftecounter == 5:
        imagemap:
            ground "map3uiGUARD.png"
            hotspot(470, 325, 105, 111):
                action [Hide("security"), Hide("guardroom"), Show("security", transition=Dissolve(0.3)), Hide("hospMap"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay8.png")
                unhovered Hide("hospPreview")
            hotspot(574, 327, 285, 109):
                action [Hide("security"), Hide("guardroom"), Show("guardroom", transition=Dissolve(0.3)), Hide("hospMap"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay9.png")
                unhovered Hide("hospPreview")
            hotspot(859, 328, 91, 61):
                action [Hide("security"), Hide("guardroom"), Show("closet", transition=Dissolve(0.3)), Hide("hospMap"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay9.png")
                unhovered Hide("hospPreview")
    else:
        imagemap:
            ground "map3uiPRISONER.png"
            hotspot(470, 325, 105, 111):
                action [Hide("kitchen"), Hide("dining"), Hide("garage"), Hide("hallway"), Hide("bedroom"), Hide("bedroomFL"), Hide("masterBedroom"), Hide("bathroom"), Show("kitchen", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay3.png")
                unhovered Hide("hospPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("hospMap", transition=Dissolve(0.3)), Hide("hospPreview")]

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
