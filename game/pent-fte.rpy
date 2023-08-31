
screen pentMap():
    modal True
    imagemap:
        ground "ftemap11.png"
        hotspot(249, 356, 381, 300):
            action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentDining", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="pentmapoverlay4.png")
            unhovered Hide("mapPreview")
        # hotspot(629, 356, 288, 177):
        #     action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentBedroom", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
        #     hovered ShowTransient("mapPreview", img="pentmapoverlay1.png")
        #     unhovered Hide("mapPreview")
        # hotspot(818, 510, 46, 40):
        #     action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentBedroom", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
        #     hovered ShowTransient("mapPreview", img="pentmapoverlay1.png")
        #     unhovered Hide("mapPreview")
        # hotspot(914, 357, 267, 176):
        #     action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentStudy", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
        #     hovered ShowTransient("mapPreview", img="pentmapoverlay3.png")
        #     unhovered Hide("mapPreview")
        # hotspot(786, 569, 169, 86):
        #     action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentCellar", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
        #     hovered ShowTransient("mapPreview", img="pentmapoverlay2.png")
        #     unhovered Hide("mapPreview")
        # hotspot(819, 550, 45, 49):
        #     action [Hide("pentDining"), Hide("pentBedroom"), Hide("pentStudy"), Hide("pentCellar"), Show("pentCellar", transition=Dissolve(0.3)), Hide("pentMap"), Hide("mapPreview")]
        #     hovered ShowTransient("mapPreview", img="pentmapoverlay2.png")
        #     unhovered Hide("mapPreview")
    imagemap:
        ground "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("pentMap", transition=Dissolve(0.3)), Hide("mapPreview")]

screen pentDining():
    add "bg pentkitchen2.png"
    add "status.png"
    add Text("{b}Dining Room{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch5.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("pentMap", transition=Dissolve(0.3))]
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
    if ftecounter == 11:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("frogAsk11")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("jennAsk11")]
        imagebutton:
            xpos 20
            ypos 120
            idle "sidchibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("sidAsk11")]
    if ftecounter == 12:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("frogAsk12")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("jennAsk12")]
        imagebutton:
            xpos 20
            ypos 120
            idle "sidchibi.png" at chibizoom
            action [Hide("pentDining", transition = Dissolve(1.0)), Jump("sidAsk12")]

screen pentBedroom():
    add "bg pentbedroom2.png"
    if ftecounter == 11:
        add "ftemap11.png"
    if ftecounter == 12:
        add "ftemap12.png"
    add "status.png"
    add Text("{b}Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch5.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("pentMap", transition=Dissolve(0.3))]
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

screen pentStudy():
    add "bg pentstudy2.png"
    if ftecounter == 11:
        add "ftemap11.png"
    if ftecounter == 12:
        add "ftemap12.png"
    add "status.png"
    add Text("{b}Study{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch5.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("pentMap", transition=Dissolve(0.3))]
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

screen pentCellar():
    add "bg pentcellar2.png"
    if ftecounter == 11:
        add "ftemap11.png"
    if ftecounter == 12:
        add "ftemap12.png"
    add "status.png"
    add Text("{b}Wine Cellar{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch5.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("pentMap", transition=Dissolve(0.3))]
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
