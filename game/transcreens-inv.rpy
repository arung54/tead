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

        if train_evidence[2]:
            textbutton "Kaiser, Lauren, Sam, and Shahar's accounts" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

    if currEvidence == 0:
        image "computer.png" xcenter 800 yalign 0.0
        text "The computer used to navigate the train." xcenter 800 yalign 0.3

    if currEvidence == 1:
        image "window.png" xcenter 800 yalign 0.0
        text "Wee woo wee woo.\nThis is a new line but it's longer!" xcenter 800 yalign 0.3

    if currEvidence == 2:
        image "window.png" xcenter 800 yalign 0.0 alpha .4
        text "Kaiser, Lauren, Sam, and Shahar \nsaid they were all in the front car. \n \nLauren said the lights turned \nthey heard the scream, and \nthen went to the bar car." xcenter 800 yalign 0.3

############################### put button locations and jumps here

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

    imagebutton:
        xpos 20
        ypos 70
        idle "kaiserchibi.png"
        action [Jump("trainKaiser")]


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

#################################################### put descriptions here

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

label trainKaiser:
    scene bg trainfront1
    show sam with dissolve
    s "I can't believe someone actually did this..."
    s "One of {i}us{/i} did this."
    show sam:
        linear .3 xcenter .75
    show kaiser ind with moveinleft:
        xcenter .25
    k "For Dan's sake, and our own, we need to keep a calm head."
    b "Agree. The most important thing is finding the culprit."
    b "So the 4 of you were in this car up until... It happened?"
    s "Yeah, Kaiser, Lauren, Shahar, and I were up here."
    s "I don't think any of us left the car for the past hour or so."
    k "We were trying to figure out the computer password."
    k "Of course, to no avail."
    bi "Since there were 4 of them up here together, it's a pretty air-tight alibi."
    hide sam
    hide kaiser ind
    with dissolve
    show lauren ind with dissolve:
        xcenter .25
    show shahar mad with dissolve:
        xcenter .75
    o "This is... Crazy."
    o "I knew this was a mess of a situation from the start, but..."
    o "A murder?! Really?"
    h "Aye. A shame we've lost 'im to Davey Jones."
    b "There will be time to grief, as long as we can figure out who was behind it."
    b "Did any of you notice anything that might be important?"
    o "Hmmm... Not really. Pretty much just what Jenny said."
    o "It went dark, we heard that blood-curdling scream, and we made our way to the bar car."
    b "Hmmm. Okay, thanks."
    hide lauren ind
    hide shahar mad
    with dissolve
    call screen frontCarInv
