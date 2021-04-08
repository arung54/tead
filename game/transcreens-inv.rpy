init:
    transform iconzoom:
        zoom 0.5
    transform chibizoom:
        zoom 1.5

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
        if train_evidence1[0]:
            textbutton "The Computer" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[1]:
            textbutton "The View From The Front" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[2]:
            textbutton "Front Car Accounts" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

    if currEvidence == 0:
        image "computer.png" xcenter 800 yalign 0.0
        text "The computer used to navigate the train." xcenter 800 yanchor 0.0 ypos 250

    if currEvidence == 1:
        image "window.png" xcenter 800 yalign 0.0
        text "Wee woo wee woo.\nThis is a new line but it's longer!" xcenter 800 yanchor 0.0 ypos 250

    if currEvidence == 2:
        image "window.png" xcenter 800 yalign 0.0 alpha .4
        text "Kaiser, Lauren, Sam, and Shahar said they were all \n in the front car. \n \nLauren said the lights turned off,they heard the\nscream, and then went to the bar car." xcenter 800 yanchor 0.0 ypos 250

############################### put button locations and jumps here

screen frontCarInv():
    imagemap:
        ground "bg trainFRONT1.png"
        hotspot(480, 198, 320, 148) action [Jump("trainFrontWindow")]
        hotspot(342, 100, 97, 250) action [Jump("trainComputer")]
        hotspot(830, 94, 107, 255) action [Jump("trainComputer")]
        hotspot(529, 48, 221, 107) action [Jump("trainComputer")]

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
        ypos 20
        idle "bertchibi.png" at chibizoom
        action [Hide("frontCarInv"), Jump("trainBert")]

    imagebutton:
        xpos 20
        ypos 70
        idle "kaiserchibi.png" at chibizoom
        action [Hide("frontCarInv"), Jump("trainKaiser")]

    imagebutton:
        xpos 20
        ypos 120
        idle "laurenchibi.png" at chibizoom
        action [Hide("frontCarInv"), Jump("trainKaiser")]

    imagebutton:
        xpos 20
        ypos 170
        idle "samchibi.png" at chibizoom
        action [Hide("frontCarInv"), Jump("trainKaiser")]

    imagebutton:
        xpos 20
        ypos 220
        idle "shaharchibi.png" at chibizoom
        action [Hide("frontCarInv"), Jump("trainKaiser")]

#############

screen midCarInv():
    imagemap:
        ground "bg notrainMID.png"
        hotspot(379, 366, 40, 105) action [Jump("trainlights")]
        hotspot(721, 288, 40, 65) action [Jump("trainlights")]
        hotspot(604, 228, 64, 34) action [Jump("trainlights")]
        ###
        hotspot(130, 352, 150, 192) action [Jump("trainwindows")]
        hotspot(998, 351, 150, 189) action [Jump("trainwindows")]
        hotspot(423, 322, 93, 82) action [Jump("trainwindows")]
        hotspot(792, 329, 135, 111) action [Jump("trainwindows")]
        hotspot(607, 230, 57, 29) action [Jump("trainwindows")]
        ###
        hotspot(573, 276, 133, 176) action [Jump("trainbar")]
        hotspot(704, 363, 62, 86) action [Jump("trainbar")]
        ##
        hotspot(110, 618, 362, 97) action [Jump("traincouch")]
        hotspot(252, 514, 212, 102) action [Jump("traincouch")]
        hotspot(679, 611, 486, 108) action [Jump("traincouch")]
        hotspot(670, 466, 227, 176) action [Jump("traincouch")]
        hotspot(881, 512, 131, 128) action [Jump("traincouch")]

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
        ypos 20
        idle "bertchibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("trainmidBert")]

    imagebutton:
        xpos 20
        ypos 70
        idle "catherinechibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("traincatherine")]

    imagebutton:
        xpos 20
        ypos 120
        idle "draculachibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("traindracula")]


############

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
    $train_evidence1[0] = True
    bi "The train's computer system. Hmmm..."
    bi "Let's take a closer look."
    scene welcomescreendir4
    bi "It looks the same as before, I think."
    bi "Wait - no! There is something different..."
    bi "I should make a mental note of that."
    scene bg trainfront1
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call screen frontCarInv

label trainFrontWindow:
    scene bg trainfront1
    $train_evidence1[1] = True
    bi "The train's front window."
    bi "It's pretty dark out, but there's still some light coming through."
    bi "With the computers all on too, you'd think it would stay pretty bright in here."
    bi "Hmmm..."
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call screen frontCarInv

label trainBert:
    scene bg trainfront1
    show bert sad with dissolve
    bi "What a terrible situation..."
    bi "The best way we can help is by collecting evidence."
    call screen frontCarInv

label trainKaiser:
    scene bg trainfront1
    $train_evidence1[2] = True
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
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call screen frontCarInv

label trainmidBert:
    scene bg notrainmid
    show bert sad with dissolve
    bi "What a terrible situation..."
    bi "The best way we can help is by collecting evidence."
    call screen midCarInv

label traincatherine:
    scene bg notrainmid
    $train_evidence2[0] = True
    show catherine ind with dissolve
    c "This is so scary..."
    c "It's like a crappy murder mystery game."
    ses "Mrow!!!"
    b "Catherine, when the lights went out, did you keep walking to the back car?"
    b "I distinctly remember you on your way to say goodnight to Sid and Dan."
    c "No, I stayed in this car. In fact, I held onto the doorknob to the back car the whole time the lights were out."
    c "I was scared of getting lost if I kept moving, so I clung to the doorknob and waited it out."
    b "So you would know if somebody went to the back car while the lights were out?"
    c "Nobody did, there's no way they could have. The door stayed closed the whole time, I swear to it."
    ses "Me-ow!"
    b "Hmmm, I see. Thanks Catherine."
    if False not in train_evidence2:
        bi "I think that's everything important in this car."
    call screen midCarInv

label traindracula:
    scene bg notrainmid
    $train_evidence2[1] = True
    show drac ind with dissolve
    d "By the way..."
    d "What was that scream we heard?"
    scene black with fade
    blank "AHHHHH!"
    scene bg notrainmid
    show drac ind
    with fade
    b "Hmmm, you're right. It sounded like a woman's voice."
    d "Almost in a... Familiar way."
    b "Well, it had to have been one of us screaming, so it makes sense that it'd be familiar."
    d "Yes, but... Familiar in a {i}different{/i} way."
    d "Regardless. That's all the information I have."
    hide drac ind with dissolve
    b "Hmm..."
    if False not in train_evidence2:
        bi "I think that's everything important in this car."
    call screen midCarInv

label trainlights:
    scene bg notrainmid
    if windowcount > 5:
        b "Wait... The lights are still off."
        b "And it's night time."
        b "But there's still enough light to see, even if it's just a little."
        show jenny ind with moveinleft
        j "So what?"
        b "If the lights are off, and there's no sunlight, but we can still see..."
        b "Then why couldn't we see during the commotion?"
        j "Wow, you're right. That's a good point."
        $train_evidence2[2] = True
        $lightscount += 10
        if False not in train_evidence2:
            bi "I think that's everything important in this car."
    else:
        b "Hmmm... The lights are still off."
        $ lightscount += 10
    call screen midCarInv

label trainwindows:
    scene bg notrainmid
    if lightscount > 5:
        b "Wait... It's night time."
        b "And the lights are still off."
        b "But there's still enough light to see, even if it's just a little."
        show jenny ind with moveinleft
        j "So what?"
        b "If the lights are off, and there's no sunlight, but we can still see..."
        b "Then why couldn't we see during the commotion?"
        j "Wow, you're right. That's a good point."
        $ windowcount += 10
        $train_evidence2[2] = True
        if False not in train_evidence2:
            bi "I think that's everything important in this car."
    else:
        b "Hmmm... It's pretty dark out."
        $ windowcount += 10
    call screen midCarInv

label trainbar:
    scene bg notrainmid
    bi "The train bar."
    bi "I don't think now's the best time to start drinking."
    call screen midCarInv

label traincouch:
    scene bg notrainmid
    bi "Some chairs and couches throughout the bar car."
    bi "I don't think there's anything important about them right now."
    call screen midCarInv
