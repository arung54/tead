init:
    transform iconzoom:
        zoom 0.3
    transform chibizoom:
        zoom 1.5

screen trainMapInv():
    modal True
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
    modal True

    imagemap:
        ground "evidenceui.png"
        add "usethis.png" xcenter 800 yalign .9
        hotspot(35, 29, 144, 75) action [Hide("trainEvidence")]
    vbox xalign 0.15 yalign 0.75 spacing 30:
        if train_evidence1[0]:
            textbutton "Login Screen" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[1]:
            textbutton "Front Car Lighting" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[2]:
            textbutton "Front Car Accounts" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[0]:
            textbutton "Bar Car Lighting" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[1]:
            textbutton "Dracula's Account" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[2]:
            textbutton "Catherine's Account" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[0]:
            textbutton "Hanging Object" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[1]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[2]:
            textbutton "Back Car Closet" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[3]:
            textbutton "State of the Body" style "button_text" action SetVariable("currEvidence", 9)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "loginev.png" xcenter 800 yalign 0.1
            text "Something seems different here..." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "lights2ev.png" xcenter 800 yalign 0.1
            text "The ambient light in the front car makes it pertty easy to see, even at night." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "frontaccounts1.png" xcenter 800 yalign 0.1
            text "Kaiser, Lauren, Sam, and Shahar said they were all in the front car. Lauren said the car went dark, but the lights were still on, so they could see what they were doing." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "lightsev" xcenter 800 yalign 0.1
            text "It's dark out, and the lights in the bar car are off." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "dracaccount1" xcenter 800 yalign 0.1
            text "Dracula said the scream we heard while it was dark was somehow 'familiar'." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "catherineaccount1" xcenter 800 yalign 0.1
            text "Catherine said her hand was on the door knob to the back car the whole time it was dark. It was dark, and the scream scared her, so she didn't keep moving." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ringev" xcenter 800 yalign 0.1
            text "We found this hanging outside the back window of the train." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "sidaccount1.png" xcenter 800 yalign 0.1
            text "Sid said he was sleeping in the bed, but was woken up by loud noises and a scream." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "closetev.png" xcenter 800 yalign 0.1
            text "The closet opened easily, but there was nothing inside." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "window.png" xcenter 800 yalign 0.1
            text "A superficial autopsy suggests Dan's cause of death is the large metal rod in his chest, with no other visible injuries. He seemed to have been looking out the window at the time of death." xcenter 800 yanchor 0.0 ypos 330

############################### put button locations and jumps here

screen frontCarInv():
    imagemap:
        ground "bg trainFRONT1.png"
        hotspot(480, 198, 320, 148) action [Hide("frontCarInv"), Jump("trainFrontWindow")]
        hotspot(342, 100, 97, 250) action [Hide("frontCarInv"), Jump("trainComputer")]
        hotspot(830, 94, 107, 255) action [Hide("frontCarInv"), Jump("trainComputer")]
        hotspot(529, 48, 221, 107) action [Hide("frontCarInv"), Jump("trainComputer")]

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

##################################################################################

screen midCarInv():
    imagemap:
        ground "bg notrainMID.png"
        hotspot(379, 366, 40, 105) action [Hide("midCarInv"), Jump("trainlights")]
        hotspot(721, 288, 40, 65) action [Hide("midCarInv"), Jump("trainlights")]
        hotspot(604, 228, 64, 34) action [Hide("midCarInv"), Jump("trainlights")]
        ###
        hotspot(130, 352, 150, 192) action [Hide("midCarInv"), Jump("trainwindows")]
        hotspot(998, 351, 150, 189) action [Hide("midCarInv"), Jump("trainwindows")]
        hotspot(423, 322, 93, 82) action [Hide("midCarInv"), Jump("trainwindows")]
        hotspot(792, 329, 135, 111) action [Hide("midCarInv"), Jump("trainwindows")]
        hotspot(607, 230, 57, 29) action [Hide("midCarInv"), Jump("trainwindows")]
        ###
        hotspot(573, 276, 133, 176) action [Hide("midCarInv"), Jump("trainbar")]
        hotspot(704, 363, 62, 86) action [Hide("midCarInv"), Jump("trainbar")]
        ##
        hotspot(110, 618, 362, 97) action [Hide("midCarInv"), Jump("traincouch")]
        hotspot(252, 514, 212, 102) action [Hide("midCarInv"), Jump("traincouch")]
        hotspot(679, 611, 486, 108) action [Hide("midCarInv"), Jump("traincouch")]
        hotspot(670, 466, 227, 176) action [Hide("midCarInv"), Jump("traincouch")]
        hotspot(881, 512, 131, 128) action [Hide("midCarInv"), Jump("traincouch")]

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
        idle "freddychibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("trainfreddy")]

    imagebutton:
        xpos 20
        ypos 170
        idle "jennychibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("trainjenny")]

    imagebutton:
        xpos 20
        ypos 220
        idle "stellachibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("trainstella")]

    imagebutton:
        xpos 20
        ypos 270
        idle "draculachibi.png" at chibizoom
        action [Hide("midCarInv"), Jump("traindracula")]

##################################################################################

screen backCarInv():
    imagemap:
        ground "bg bodytrainBACK.png"
        hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")]
        ##
        hotspot(606, 167, 97, 77) action [Hide("backCarInv"), Jump("traincoin")]
        ##
        hotspot(602, 287, 113, 246) action [Hide("backCarInv"), Jump("trainbody")]
        ##
        hotspot(732, 19, 147, 66) action [Hide("backCarInv"), Jump("trainrip")]
        ##
        hotspot(322, 377, 131, 315) action [Hide("backCarInv"), Jump("trainwater")]
        ##
        hotspot(456, 353, 125, 164) action [Hide("backCarInv"), Jump("trainbed")]
        ##
        hotspot(773, 334, 111, 156) action [Hide("backCarInv"), Jump("trainbench")]
        hotspot(840, 372, 107, 346) action [Hide("backCarInv"), Jump("trainbench")]

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
        action [Hide("backCarInv"), Jump("trainbackBert")]

    imagebutton:
        xpos 20
        ypos 70
        idle "sidchibi.png" at chibizoom
        action [Hide("backCarInv"), Jump("trainsid")]

    imagebutton:
        xpos 20
        ypos 120
        idle "danchibi.png" at chibizoom
        action [Hide("backCarInv"), Jump("trainbody")]


#################################################### put descriptions here
####################################################
####################################################

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
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call traindone
    call screen frontCarInv

label trainFrontWindow:
    scene bg trainfront1
    $train_evidence1[1] = True
    bi "The train's front window."
    bi "It's pretty dark out, but there's still some light coming through."
    bi "With the computers all on too, you'd think it would stay pretty bright in here."
    bi "Hmmm..."
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call traindone
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
    o "It got darker all of a sudden while we were on the computers, but since the lights were still, it was easy to keep a cool head."
    h "Till we heard that scream..."
    o "Yeah."
    b "Hmmm. Okay, thanks."
    hide lauren ind
    hide shahar mad
    with dissolve
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    if train_evidence1[0] and train_evidence1[1] and train_evidence1[2]:
        bi "I think that's everything to find in this car."
    call traindone
    call screen frontCarInv

label trainmidBert:
    scene bg notrainmid
    show bert sad with dissolve
    bi "What a terrible situation..."
    bi "The best way we can help is by collecting evidence."
    call screen midCarInv

label trainfreddy:
    scene bg notrainmid
    show frog sad with moveinbottom
    f "Shahar said Dan's... swimming with the fishes?"
    f "Why are there fish on the train?"
    bi "..."
    b "Hey, did you see or hear anything weird when it went dark?"
    f "Umm... I don't think so..."
    f "I'm just a frog..."
    f "Sorry..."
    hide frog sad with moveoutbottom
    bi "I guess that's what I expected from him..."
    bi "Technically, I can't confirm where he was when it happened. Which means he... in a crazy world..."
    bi "could have killed Dan."
    bi "Seems unlikely though."
    call screen midCarInv

label trainjenny:
    scene bg notrainmid
    show jenny ind with dissolve
    j "Personally, I don't remember much..."
    j "It got dark, and I called out to you."
    j "I think I reached out looking to grab on to you for balance, but I couldn't find you."
    bi "Hmmm..."
    j "Next thing I know, we can see again, and you're right in front of me."
    hide jenny ind with dissolve
    bi "She was definitely right next to me when it went dark, and when it got bright again."
    bi "The period in-between though, I can't vouch for just yet."
    call screen midCarInv

label trainstella:
    scene bg notrainmid
    show stella ind with dissolve
    t "Well sheesh, that'll sober you up quick."
    b "Stella, do you remember anything that might be useful?"
    b "Or do you have an alibi for what you were doing while it was dark?"
    t "Honestly? Not really. I was right here with you guys, freaking out."
    bi "That is true, she was talking a bunch the whole time."
    t "Dracula was saying something interesting a minute ago though."
    t "He might be more useful than myself."
    hide stella ind with dissolve
    b "Hm?"
    call screen midCarInv

label traincatherine:
    scene bg notrainmid
    $train_evidence2[2] = True
    show catherine ind with dissolve
    c "This is so scary..."
    c "It's like a crappy murder mystery game."
    ses "Mrow!!!"
    b "Catherine, when the lights went out, did you keep walking to the back car?"
    b "I distinctly remember you on your way to say goodnight to Sid and Dan."
    c "No, I stayed in this car. In fact, I held onto the doorknob to the back car the whole time the lights were out."
    c "I was scared of getting lost, and scared from the scream, so I clung to the doorknob and waited it out."
    b "So you would know if somebody went to the back car while the lights were out?"
    c "Nobody did, there's no way they could have."
    ses "Me-ow!"
    b "Hmmm, I see. Thanks Catherine."
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    if False not in train_evidence2:
        bi "I think that's everything important in this car."
    call traindone
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
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    if False not in train_evidence2:
        bi "I think that's everything important in this car."
    call traindone
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
        $train_evidence2[0] = True
        $lightscount += 10
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        if False not in train_evidence2:
            bi "I think that's everything important in this car."
    else:
        b "Hmmm... The lights are still off."
        $ lightscount += 10
    call traindone
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
        $train_evidence2[0] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        if False not in train_evidence2:
            bi "I think that's everything important in this car."
    else:
        b "Hmmm... It's pretty dark out."
        $ windowcount += 10
    call traindone
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

label trainbackBert:
    scene bg bodytrainback
    show bert sad with dissolve
    bi "What a terrible situation..."
    bi "The best way we can help is by collecting evidence."
    call screen backCarInv

label trainrip:
    scene bg bodytrainback
    bi "Well I guess it's a good thing we have this."
    bi "I don't think it's important right now though."
    call screen backCarInv

label trainbed:
    scene bg bodytrainback
    bi "The bed. It's next to the closet, but other than that..."
    bi "I don't think it's very important right now."
    call screen backCarInv

label trainwater:
    scene bg bodytrainback
    bi "There's an old-timey water heater and kettle back here."
    bi "I don't think it's relevant right now."
    call screen backCarInv

label trainbench:
    scene bg bodytrainback
    bi "The bench. I think this is where either Dan or Sid was sleeping."
    call screen backCarInv

label trainsid:
    scene bg bodytrainback
    show sid ind with dissolve
    i "Is he really... dead?"
    b "Yeah, Sid. He's dead."
    b "You should go up to the bar car, you don't have to be back here."
    i "I was just... talking to him. He let me sleep in the bed..."
    i "Why did it have to happen to {i}Dan?{/i}"
    i "Who did this?!"
    b "I'm going to figure it out. But I need your help."
    b "Sid, what were you doing before... this happened?"
    i "I just told you! I was sleeping in the bed. Dan took it last night, so tonight was my turn."
    i "Then I heard someone scream, the window break, and I woke up to... this."
    hide sid ind with dissolve
    bi "Hmmm. It seems like Dan is the only one he really befriended here."
    bi "But it also seems kinda like he killed Dan."
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    $train_evidence3[0] = True
    if False not in train_evidence3:
        bi "I think that's everything important in this car."
    call traindone
    call screen backCarInv

label traincloset:
    scene bg bodytrainback
    bi "The locked closet."
    bi "I might as well try it."
    blank "The closet door opened without any trouble."
    blank "Nothing was inside."
    bi "What?!"
    bi "I thought this closet was locked shut?"
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    $train_evidence3[1] = True
    if False not in train_evidence3:
        bi "I think that's everything important in this car."
    call traindone
    call screen backCarInv

label traincoin:
    scene bg bodytrainback
    bi "The window is cracked from the murder weapon..."
    bi "The culprit must have used a ton of extra force."
    bi "...Hm?"
    bi "There'e something dangling outside the window."
    blank "Bert carefully reached through the cracks in the window and retrieved the object."
    show thering with dissolve
    pause 1
    hide thering with dissolve
    bi "It's a... ring?"
    bi "I'll hold on to this."
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    $train_evidence3[2] = True
    if False not in train_evidence3:
        bi "I think that's everything important in this car."
    call traindone
    call screen backCarInv

label trainbody:
    scene bg bodytrainback
    bi "Dan's body..."
    bi "It's hard to look at."
    bi "But I think it's important for me to at least do a superficial autopsy."
    blank "Bert took a few minutes investigating the body."
    bi "God... there's so much blood."
    bi "I don't there's {i}too{/i} much to take away from that."
    bi "He has no visible wounds other than the metal bar through his chest."
    bi "It seems pretty clear someone skewered him through the back, killing him."
    bi "...Rest in peace, Dan. We'll find out who did this."
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    $train_evidence3[3] = True
    if False not in train_evidence3:
        bi "I think that's everything important in this car."
    call traindone
    call screen backCarInv

label traindone:
     if False not in train_evidence1 and False not in train_evidence2 and False not in train_evidence3:
           bi "Actually... I think that's everything."
           bi "I've searched all 3 cars and talked to everyone who seems like they have something to say."
           bi "Time to call the others and get to the bottom of this."
           #jump elsewhere
     return
