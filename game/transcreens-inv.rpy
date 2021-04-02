init:
    transform iconzoom:
        zoom 0.5

screen trainMapInv():
    imagemap:
        ground "trainmapoverlay.png"
        hotspot(182, 461, 330, 210):
            action [Hide("frontCarInv"), Hide("midCarInv"), Hide("backCarInv"), Show("frontCarInv", transition=Dissolve(0.3)), Hide("trainMapInv")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay1.png")
            unhovered Hide("trainPreview")
        hotspot(542, 462, 330, 210):
            action [Hide("frontCarInv"), Hide("midCarInv"), Hide("backCarInv"), Show("midCarInv", transition=Dissolve(0.3)), Hide("trainMapInv")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay2.png")
            unhovered Hide("trainPreview")
        hotspot(905, 460, 329, 211):
            action [Hide("frontCarInv"), Hide("midCarInv"), Hide("backCarInv"), Show("backCarInv", transition=Dissolve(0.3)), Hide("trainMapInv")]
            hovered ShowTransient("trainPreview", img="trainmapoverlay3.png")
            unhovered Hide("trainPreview")
    imagemap:
        idle "trainmapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("trainMapInv", transition=Dissolve(0.3))]
style button_text:
    color "#fff"

style blue_text:
    color "#00f"

screen trainEvidence():
    add "eviscroll"
    imagemap:
        ground "evidenceui.png"
        hotspot(35, 29, 144, 75) action [Hide("trainEvidence")]
    vbox xalign 0.15 yalign 0.5 spacing 30:
        if train_evidence[0]:
            textbutton "The Computer" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence[1]:
            textbutton "The View From The Front" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

    if currEvidence == 0:
        image "computer.png" xcenter 800 yalign 0.0
        text "The computer used to navigate the train." xcenter 800 yalign 0.3

    if currEvidence == 1:
        image "window.png" xcenter 800 yalign 0.0
        text "Wee woo wee woo.\nThis is a new line but it's longer!" xcenter 800 yalign 0.3

screen frontCarInv():

    imagemap:
        ground "bg trainFRONT1.png"
        hotspot(479, 196, 327, 101) action [Jump("trainFrontWindow")]
        hotspot(547, 266, 185, 85) action [Jump("trainComputer")]

    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "mapicon.png" at iconzoom
        action [Show("trainMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.1
        idle "evidenceicon.png" at iconzoom
        action [Show("trainEvidence", transition=Dissolve(0.3))]


screen midCarInv():
    imagemap:
        ground "bg trainMID.png"

    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "mapicon.png" at iconzoom
        action [Show("trainMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.1
        idle "evidenceicon.png" at iconzoom
        action [Show("trainEvidence", transition=Dissolve(0.3))]

screen backCarInv():
    imagemap:
        ground "bg trainBACK.png"

    imagebutton:
        xalign 1.0
        yalign 0.0
        idle "mapicon.png" at iconzoom
        action [Show("trainMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.1
        idle "evidenceicon.png" at iconzoom
        action [Show("trainEvidence", transition=Dissolve(0.3))]

label trainComputer:
    scene bg trainfront1
    $train_evidence[0] = True
    n "The computer used to navigate the train. I should add this to my list of evidence."
    if train_evidence[0] and train_evidence[1]:
        n "I think that's everything to find in this room"
    call screen frontCarInv


label trainFrontWindow:
    scene bg trainfront1
    $train_evidence[1] = True
    n "You can't see the tunnel from the front window until it's too late. I should remember that."
    if train_evidence[0] and train_evidence[1]:
        n "I think that's everything to find in this room"
    call screen frontCarInv
