screen hospMap():
    modal True
    #TODO: Create secret sesame FTE
    if ftecounter == 5:
        imagemap:
            ground "map3uiGUARD.png"
            hotspot(460, 273, 108, 78):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("security", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay8.png")
                unhovered Hide("mapPreview")
            hotspot(567, 275, 287, 177):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("guardroom", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay9.png")
                unhovered Hide("mapPreview")
            hotspot(851, 273, 90, 78):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("closet", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay1.png")
                unhovered Hide("mapPreview")
            hotspot(568, 451, 285, 87):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("hospKitchen", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay5.png")
                unhovered Hide("mapPreview")
            hotspot(202, 376, 367, 53):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("hallwayTL", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay4.png")
                unhovered Hide("mapPreview")
            hotspot(853, 376, 363, 51):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("hallwayTR", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay4b.png")
                unhovered Hide("mapPreview")
    else:
        imagemap:
            ground "map3uiPRISONER.png"
            hotspot(203, 568, 365, 47):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("hallwayBL", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay3.png")
                unhovered Hide("mapPreview")
            hotspot(851, 569, 367, 49):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("hallwayBR", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay3b.png")
                unhovered Hide("mapPreview")
            hotspot(566, 535, 289, 122):
                action [Hide("security"), Hide("guardroom"), Hide("closet"), Hide("hospKitchen"), Hide("hallwayTL"), Hide("hallwayTR"), Hide("hallwayBL"), Hide("hallwayBR"), Hide("patientcommons"), Show("patientcommons", transition=Dissolve(0.3)), Hide("hospMap"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="hospmapoverlay2.png")
                unhovered Hide("mapPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("hospMap", transition=Dissolve(0.3)), Hide("mapPreview")]

screen security():
    add "bg hospsecurity.png"
    add "status.png"
    add Text("{b}Security{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen closet():
    add "bg hospcloset.png"
    add "status.png"
    add Text("{b}Closet{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen guardroom():
    add "bg hospfancy.png"
    add "status.png"
    add Text("{b}Guards' Commons{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen hallwayTL():
    add "bg hosphalltopleft.png"
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen hallwayTR():
    add "bg hosphalltopright.png"
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen hallwayBR():
    add "bg hosphallbotright.png"
    add "status.png"
    add Text("{b}Patients' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen hallwayBL():
    add "bg hosphalltopleft.png"
    add "status.png"
    add Text("{b}Patients' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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

screen hospKitchen():
    add "bg hospkitchen.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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
    if ftecounter == 5:
        imagebutton:
            xpos 20
            ypos 20
            idle "jennychibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("jennAsk5")]
        imagebutton:
            xpos 70
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("dracAsk5")]
        imagebutton:
            xpos 70
            ypos 70
            idle "sidchibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("sidAsk5")]
        imagebutton:
            xpos 70
            ypos 120
            idle "shaharchibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("shahAsk5")]
        imagebutton:
            xpos 70
            ypos 170
            idle "laurenchibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("laurAsk5")]
        imagebutton:
            xpos 70
            ypos 220
            idle "freddychibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("frogAsk5")]
        imagebutton:
            xpos 70
            ypos 270
            idle "samchibi.png" at chibizoom
            action [Hide("hospKitchen", transition = Dissolve(1.0)), Jump("samAsk5")]

screen patientcommons():
    add "bg hospkitchen.png"
    add "status.png"
    add Text("{b}Cafeteria{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("hospMap", transition=Dissolve(0.3))]
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
    if ftecounter == 6:
        imagebutton:
            xpos 70
            ypos 70
            idle "draculachibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("dracAsk6")]
        imagebutton:
            xpos 70
            ypos 20
            idle "sidchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("sidAsk6")]
        imagebutton:
            xpos 20
            ypos 20
            idle "laurenchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("laurAsk6")]
        imagebutton:
            xpos 20
            ypos 70
            idle "freddychibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("frogAsk6")]
        imagebutton:
            xpos 20
            ypos 120
            idle "jennychibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("jennAsk6")]
        imagebutton:
            xpos 20
            ypos 170
            idle "shaharchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("shahAsk6")]
        imagebutton:
            xpos 20
            ypos 220
            idle "samchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("samAsk6")]
    if ftecounter == 7:
        imagebutton:
            xpos 70
            ypos 20
            idle "draculachibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("dracAsk7")]
        imagebutton:
            xpos 20
            ypos 20
            idle "laurenchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("laurAsk7")]
        imagebutton:
            xpos 20
            ypos 70
            idle "freddychibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("frogAsk7")]
        imagebutton:
            xpos 20
            ypos 120
            idle "jennychibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("jennAsk7")]
        imagebutton:
            xpos 20
            ypos 170
            idle "shaharchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("shahAsk7")]
        imagebutton:
            xpos 20
            ypos 220
            idle "samchibi.png" at chibizoom
            action [Hide("patientcommons", transition = Dissolve(1.0)), Jump("samAsk7")]
