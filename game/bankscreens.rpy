screen bankMap():
    modal True
    imagemap:
        ground "map4ui.png"
        hotspot(307, 477, 184, 215):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("lobby", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay4.png")
            unhovered Hide("mapPreview")
        hotspot(361, 329, 131, 133):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("break", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay1.png")
            unhovered Hide("mapPreview")
        hotspot(491, 330, 57, 364):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("hall", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(547, 331, 489, 56):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("hall", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(674, 379, 53, 316):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("hall", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(674, 644, 361, 49):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("hall", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(987, 330, 49, 363):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("hall", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(569, 387, 105, 112):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("office", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay2.png")
            unhovered Hide("mapPreview")
        hotspot(1035, 512, 100, 182):
            action [Hide("lobby"), Hide("break"), Hide("hall"), Hide("safe"), Hide("office"), Hide("locker"), Show("locker", transition=Dissolve(0.3)), Hide("bankMap"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay3.png")
            unhovered Hide("mapPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("bankMap", transition=Dissolve(0.3)), Hide("mapPreview")]

screen break():
    add "bg bankbreak.png"
    add "status.png"
    add Text("{b}Staff Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 8 or ftecounter == 10:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 9:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("bankMap", transition=Dissolve(0.3))]
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

screen lobby():
    add "bg banklobby1.png"
    add "status.png"
    add Text("{b}Bank Lobby{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 8 or ftecounter == 10:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 9:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("bankMap", transition=Dissolve(0.3))]
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
    if ftecounter == 8:
        imagebutton:
            xpos 20
            ypos 20
            idle "jennychibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("jennAsk8")]
    if ftecounter == 9:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("frogAsk9")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("jennAsk9")]
        imagebutton:
            xpos 20
            ypos 120
            idle "laurenchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("laurAsk9")]
        imagebutton:
            xpos 20
            ypos 170
            idle "samchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("samAsk9")]
        imagebutton:
            xpos 20
            ypos 220
            idle "sidchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("sidAsk9")]
    if ftecounter == 10:
        imagebutton:
            xpos 20
            ypos 20
            idle "laurenchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("laurAsk10")]
        imagebutton:
            xpos 20
            ypos 70
            idle "samchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("samAsk10")]
        imagebutton:
            xpos 20
            ypos 120
            idle "sidchibi.png" at chibizoom
            action [Hide("lobby", transition = Dissolve(1.0)), Jump("sidAsk10")]

screen hall():
    add "bg bankvault.png"
    add "status.png"
    add Text("{b}Bank Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 8 or ftecounter == 10:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 9:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("bankMap", transition=Dissolve(0.3))]
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
    if ftecounter == 8:
        imagebutton:
            xpos 20
            ypos 20
            idle "sidchibi.png" at chibizoom
            action [Hide("hall", transition = Dissolve(1.0)), Jump("sidAsk8")]
    if ftecounter == 10:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("hall", transition = Dissolve(1.0)), Jump("frogAsk10")]
        imagebutton:
            xpos 20
            ypos 70
            idle "jennychibi.png" at chibizoom
            action [Hide("hall", transition = Dissolve(1.0)), Jump("jennAsk10")]

screen office():
    add "bg bankoffice.png"
    add "status.png"
    add Text("{b}Director's Office{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 8 or ftecounter == 10:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 9:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("bankMap", transition=Dissolve(0.3))]
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
    if ftecounter == 8:
        imagebutton:
            xpos 20
            ypos 20
            idle "freddychibi.png" at chibizoom
            action [Hide("hall", transition = Dissolve(1.0)), Jump("frogAsk8")]
        imagebutton:
            xpos 20
            ypos 70
            idle "laurenchibi.png" at chibizoom
            action [Hide("hall", transition = Dissolve(1.0)), Jump("laurAsk8")]

screen locker():
    add "bg banklocker.png"
    add "status.png"
    add Text("{b}Locker Room{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    if ftecounter == 8 or ftecounter == 10:
        add "sun2.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    if ftecounter == 9:
        add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon" at iconzoom
        action [Show("bankMap", transition=Dissolve(0.3))]
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
    if ftecounter == 8:
        imagebutton:
            xpos 20
            ypos 20
            idle "samchibi.png" at chibizoom
            action [Hide("locker", transition = Dissolve(1.0)), Jump("samAsk8")]
