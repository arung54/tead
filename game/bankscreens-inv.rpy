screen bankMapInv():
    modal True
    imagemap:
        ground "map4ui.png"
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("lobbyInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("breakInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("hall1Inv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("hall2Inv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("safeInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("officeInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(460, 273, 108, 78):
            action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("lockerInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
            unhovered Hide("mapPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("bankMapInv", transition=Dissolve(0.3)), Hide("mapPreview")]

screen bank_evidence():
    add "eviscroll"
    modal True

    imagemap:
        ground "evidenceui.png"
        #add "usethis.png" xcenter 800 yalign .9
        hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("bank_evidence", transition=Dissolve(0.3))]
    vbox xalign 0.15 yalign 0.75 spacing 18:
        if bank_evidence[0]:
            textbutton "Bert's Account" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"
        if bank_evidence[1]:
            textbutton "Break Room Door" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"
        if bank_evidence[2]:
            textbutton "Gun" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[3]:
            textbutton "Torn Elastic Belt" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[4]:
            textbutton "Freddy's Account" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[5]:
            textbutton "Lauren's Account" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[6]:
            textbutton "Jenny's Account" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[7]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[8]:
            textbutton "Ammunition" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[9]:
            textbutton "Uniforms in the Lockers" style "button_text" action SetVariable("currEvidence", 9)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev3 guards.png" xcenter 800 yalign 0.1
            text "After the shooting, I chased the uniformed person into the hallway. It was quiet enough in the hallway that I both saw and heard the break room door close. I yanked the door open and found Sam's body in the uniform." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev3 computer.png" xcenter 800 yalign 0.1
            text "The door to the break room stayed open the entire time since I first walked in here." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev3 glue.png" xcenter 800 yalign 0.1
            text "The gun we found in the break room holds up to six bullets at once, and was empty when we found Sam's body." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev3 rules.png" xcenter 800 yalign 0.1
            text "Part of an elastic belt was found attached to ___ in the break room." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Freddy woke up to the sound of six gunshots. He saw me get down to the floor, then saw the uniformed person leave, and me chase after them." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Lauren was searching in the office, left, and was walking towards the guard room when she heard me scream for help. She " xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev3 cleaning.png" xcenter 800 yalign 0.1
            text "Jenny had just finished taking a shower in the guard room. She walked out and saw the safe was open, then heard me yelling. She walked directly to the break room, passing the hallway couch on the way." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev3 closet.png" xcenter 800 yalign 0.1
            text "The closet has two rules: \n1) Return everything to where it once was\n2) Do not leave the supply closet lights on" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev3 body.png" xcenter 800 yalign 0.1
            text "Shahar's corpse was found kneeling, with his forehead resting on a bar of his cell. His forehead is bleeding where it touches the bar, and the blood is running down the bar. No other injuries are visible." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "A number of glass shards were found in front of Shahar's corpse. They look like the glass of the bottles in the vending machine." xcenter 800 yanchor 0.0 ypos 330

screen securityInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg banksecurity rg"
        if bank_evidence[1]:
            hotspot(259, 189, 762, 476) action [Hide("securityInv"), Jump("securityComputer")] mouse 'q' hovered tt.Action("Computer")
        else:
            hotspot(259, 189, 762, 476) action [Hide("securityInv"), Jump("securityComputer")] mouse 'ex' hovered tt.Action("Computer")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Security{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("bankMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("bank_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("bankKitchenInv", transition = Dissolve(1.0)), Jump("bankInvSamSecurity")]

label bankInvSamSecurity:
    scene bg banksecurity
    $ statusnt("Security", "lauren", ch = 3, sun = 1)
    show sam with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide sam with dissolve
    call screen securityInv

label securityComputer:
    scene bg banksecurity
    $ statusnt("Security", "lauren", ch = 3, sun = 1)
    if not bank_evidence[1]:
        li "Hm, looks like a computer the guards can use to control things on this floor."
        li "I should take a look and see what I can do from here."
        li "..."
        li "Okay, first thing is a security camera system."
        li "I can see everyone but Sam and I looking around in the cafeteria."
        li "And I can see..."
        li "None of the other rooms."
        li "Seems like the camera system is limited to the cafeteria."
        li "Weird, you'd think they might want some in the cells."
        li "Okay, what else..."
        li "Huh, what does this program do? It has a list of all the rooms in this floor."
        blank "Click."
        lf "What was that noise?"
        show sam with dissolve
        s "...The lights in the room next to us turned off..."
        lf "Okay, so you can control the lights on the floor from here."
        s "...Yeah..."
        hide sam with dissolve
        li "What else... there's a function called Hot Water Cycling."
        li "Let me click the info button."
        li "It says hot water cycles through the pipes here weekly to clean them out."
        li "You can also schedule a hot water cycle for the future."
        li "Seems like an antiquated way to clean things, but this whole building seems kinda old..."
        li "And lastly, a thermostat feature."
        li "You can control the temperature in all the rooms."
        li "I guess they can't let the patients control their own temperature for safety reasons?"
        li "Well, you can't set the temperature higher than 75 degrees anyway, no way that's killing anyone..."
        li "Let's see, anything else?"
        li "..."
        li "No, can't find anything else I have access to."
        li "So to recap, this computer has security cameras, lights, hot water cycling, and a thermostat."
        li "Maybe one of those is relevant..."
        $bank_evidence[1] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Computer was added to evidence."
        li "Well, this room doesn't have much besides this computer."
        li "I should go look elsewhere."
        call bankDone from _call_bankDone
    else:
        li "Let me recall..."
        li "This computer has security cameras, lights, hot water cycling, and a thermostat."
        li "The camera only sees the cafeteria."
        li "The hot water cycles every week, and you can also schedule cycles."
        li "And the thermostat controls each room individually, but can't go higher than 75 degrees."
        li "As far as I can tell, those are the only features we have access to."
    call screen securityInv
