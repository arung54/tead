screen hospMapInv():
    modal True
    imagemap:
        ground "ch3investmap.png"
        hotspot(460, 273, 108, 78):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("securityInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay8.png")
            unhovered Hide("mapPreview")
        hotspot(567, 275, 287, 177):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("guardroomInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay9.png")
            unhovered Hide("mapPreview")
        hotspot(851, 273, 90, 78):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("closetInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay1.png")
            unhovered Hide("mapPreview")
        hotspot(568, 451, 285, 87):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hospKitchenInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay5.png")
            unhovered Hide("mapPreview")
        hotspot(202, 376, 367, 53):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hallwayTLInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay4.png")
            unhovered Hide("mapPreview")
        hotspot(853, 376, 363, 51):
            action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hallwayTRInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("mapPreview")]
            hovered ShowTransient("mapPreview", img="hospmapoverlay4b.png")
            unhovered Hide("mapPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("hospMapInv", transition=Dissolve(0.3)), Hide("mapPreview")]

screen hosp_evidence(in_menu = False):
    add "eviscroll"
    modal True

    imagemap:
        ground "evidenceui.png"
        #add "usethis.png" xcenter 800 yalign .9
        if in_menu:
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("hosp_evidence", transition=Dissolve(0.3)), ShowMenu("preferences")]
        else:
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("hosp_evidence", transition=Dissolve(0.3))]
    vbox xalign 0.15 yalign 0.75 spacing 18:
        if hosp_evidence[0]:
            textbutton "Guards' Accounts" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[1]:
            textbutton "Computer" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[2]:
            textbutton "Bottle of Medical Glue" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[3]:
            textbutton "Rules of the Hospital" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[4]:
            textbutton "Baseball Bat" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[5]:
            textbutton "Stepstool" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[6]:
            textbutton "Cleaning Supplies" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[7]:
            textbutton "Closet Rules" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[8]:
            textbutton "State of the Body" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[9]:
            textbutton "Glass Shards" style "button_text" action SetVariable("currEvidence", 9)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[10]:
            textbutton "Pipe in the Hallway" style "button_text" action SetVariable("currEvidence", 10)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[11]:
            textbutton "Order of the Cells" style "button_text" action SetVariable("currEvidence", 11)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[12]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 12)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev3 guards.png" xcenter 800 yalign 0.1
            text "{size=-2}Sam claims to have woken up before the intercom went off and stared out the door on the guard side of their door until morning. Sam didn't see or hear anything until Lauren showed up to get Sam out of the cell. Lauren claims she left her cell as soon as possible and waited outside Sam's cell." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev3 computer.png" xcenter 800 yalign 0.1
            text "{size=-2}The computer in the security room has several features: \n1) A camera viewing the cafeteria\n2) Controlling the lights\n3) Scheduled cycling of hot water through the plumbing\n4) Changing the temperature throughout the building" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev3 glue.png" xcenter 800 yalign 0.1
            text "The bottle of medical glue in the first aid kit had a bit of residue on the nozzle. According to the instructions, medical glue is used for sealing glue and hardened medical glue can be cleaned up by applying a towel dipped in near-boiling water." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev3 rules.png" xcenter 800 yalign 0.1
            text "{size=-2}The rules of the hospital state: 1) Two guards are appointed every day, 2) During the day, we cannot be in our cells, 3) At night, we must be in our cells, 4) No one may enter another person's cell, 5) Guards/patients must stay on their side, 6) Guards are responsible for feeding patients." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev3 bat.png" xcenter 800 yalign 0.1
            text "The baseball bat was still in the closet and looked like it was in mint condition." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "There is a stepstool in the supply closet, but the highest step is only a few feet off the ground." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev3 cleaning.png" xcenter 800 yalign 0.1
            text "The closet has a number of cleaning supplies, including ammonia, bleach, ethanol, and hydrogen peroxide." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev3 closet.png" xcenter 800 yalign 0.1
            text "The closet has two rules: \n1) Return everything to where it once was\n2) Do not leave the supply closet lights on" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev3 body.png" xcenter 800 yalign 0.1
            text "Shahar's corpse was found kneeling, with his forehead resting on a bar of his cell. His forehead is bleeding where it touches the bar, and the blood is running down the bar. No other injuries are visible." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "A number of glass shards were found in front of Shahar's corpse. They look like the glass of the bottles in the vending machine." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev3 pipes.png" xcenter 800 yalign 0.1
            text "Several pipes run along the ceiling of the hallway where Shahar's body was found, roughly twelve feet off the ground." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 11:
            image "ev3 cells.png" xcenter 800 yalign 0.1
            text "From left to right, the order of the cells is: Lauren, Sam, Dracula, Freddy, Jenny, Bert, Sid, Shahar." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 12:
            image "ev3 sid.png" xcenter 800 yalign 0.1
            text "Sid woke up in the middle of the night with a bad cough. There were no signs of illness prior to today." xcenter 800 yanchor 0.0 ypos 330


screen securityInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospsecurity rg"
        if hosp_evidence[1]:
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
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSamSecurity")]

label hospInvSamSecurity:
    scene bg hospsecurity at bg
    $ statusnt("Security", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide samrg with dissolve
    call screen securityInv

label securityComputer:
    scene bg hospsecurity at bg
    $ statusnt("Security", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[1]:
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
        "Click."
        lf "What was that noise?"
        show samrg ind with dissolve
        s "...The lights in the room next to us turned off..."
        lf "Okay, so you can control the lights on the floor from here."
        s "...Yeah..."
        hide samrg with dissolve
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
        $hosp_evidence[1] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Computer was added to evidence."
        li "Well, this room doesn't have much besides this computer."
        li "I should go look elsewhere."
        call hospDone from _call_hospDone
    else:
        li "Let me recall..."
        li "This computer has security cameras, lights, hot water cycling, and a thermostat."
        li "The camera only sees the cafeteria."
        li "The hot water cycles every week, and you can also schedule cycles."
        li "And the thermostat controls each room individually, but can't go higher than 75 degrees."
        li "As far as I can tell, those are the only features we have access to."
    call screen securityInv

screen closetInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospcloset rg"
        if hosp_evidence[4]:
            hotspot(154, 452, 116, 264) action [Hide("closetInv"), Jump("baseballBat")] mouse 'q' hovered tt.Action("Baseball Bat")
        else:
            hotspot(154, 452, 116, 264) action [Hide("closetInv"), Jump("baseballBat")] mouse 'ex' hovered tt.Action("Baseball Bat")
        if hosp_evidence[5]:
            hotspot(344, 472, 134, 197) action [Hide("closetInv"), Jump("stepstool")] mouse 'q' hovered tt.Action("Stepstool")
        else:
            hotspot(344, 472, 134, 197) action [Hide("closetInv"), Jump("stepstool")] mouse 'ex' hovered tt.Action("Stepstool")
        if hosp_evidence[6]:
            hotspot(240, 154, 328, 221) action [Hide("closetInv"), Jump("cleaningSupplies")] mouse 'q' hovered tt.Action("Cleaning Supplies")
        else:
            hotspot(240, 154, 328, 221) action [Hide("closetInv"), Jump("cleaningSupplies")] mouse 'ex' hovered tt.Action("Cleaning Supplies")
        if hosp_evidence[7]:
            hotspot(722, 152, 319, 298) action [Hide("closetInv"), Jump("closetRules")] mouse 'q' hovered tt.Action("Rules of the Closet")
        else:
            hotspot(722, 152, 319, 298) action [Hide("closetInv"), Jump("closetRules")] mouse 'ex' hovered tt.Action("Rules of the Closet")
        if hosp_extra[0]:
            hotspot(1096, 328, 28, 50) action [Hide("closetInv"), Jump("closetLightSwitch")] mouse 'q' hovered tt.Action("Closet Light Switch")
        else:
            hotspot(1096, 328, 28, 50) action [Hide("closetInv"), Jump("closetLightSwitch")] mouse 'ex' hovered tt.Action("Closet Light Switch")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Closet{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("closetInv", transition = Dissolve(1.0)), Jump("hospInvSamCloset")]

label hospInvSamCloset:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide samrg with dissolve
    call screen closetInv

label baseballBat:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[4]:
        lf "Oh, this must be the baseball bat Bert mentioned."
        if hosp_evidence[7]:
            li "According to the closet rules, it has to be returned to this position, but..."
        lf "It could've been taken out for a bit, right?"
        show samrg ind with dissolve
        s "..."
        li "Sam took the baseball bat, spun it around and looked at it for a bit."
        li "Then, Sam held it by the top, and tapped it against the ground."
        s "..."
        lf "..."
        s "...Seems like it's still in mint condition..."
        lf "How can you tell?"
        s "...New bats make a different sound when you tap them like that..."
        s "...And there's no signs of wear and tear on the outside..."
        lf "Oh. Uh, thanks Sam."
        s "...Yeah..."
        hide samrg with dissolve
        li "That was... helpful."
        li "I want to ask how Sam knows this but..."
        li "Well, there's more important things to worry about right now."
        $hosp_evidence[4] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Baseball Bat was added to evidence."
        if False not in hosp_evidence[4:8]:
            li "I think that's everything interesting in here."
            li "Unless I want to waste time looking at the light switch, but no one would do that, right?"
        call hospDone from _call_hospDone_1
    else:
        li "When Sam checked, it looked like the baseball bat was still in mint condition."
    call screen closetInv

label stepstool:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[5]:
        li "A stepstool..."
        li "It's not that tall. Probably only gets you two feet off the ground?"
        li "I can't think of anything that you would need a stepstool to reach in this place..."
        li "Oh, I guess someone could have found the pasta on the fridge before Dracula if they had it."
        li "Is that what it's for?"
        $hosp_evidence[5] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Stepstool was added to evidence."
        if False not in hosp_evidence[4:8]:
            li "I think that's everything interesting in here."
            li "Unless I want to waste time looking at the light switch, but no one would do that, right?"
        call hospDone from _call_hospDone_2
    else:
        li "A stepstool. It's not that tall, only gets you two or so feet off the ground."
    call screen closetInv

label cleaningSupplies:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[6]:
        li "Let's see, what all is there on this shelf."
        li "Seems to just be a bunch of cleaning supplies."
        li "There's...ammonia, bleach, ethanol, hydrogen peroxide..."
        li "I'm not a chemist, but I'm pretty sure a lot of this stuff is dangerous."
        li "There's quite a few hazard warnings on the containers."
        li "A lot of them also say to avoid mixing them, not just consuming them."
        lf "I'm kind of relieved a murder happened today..."
        lf "If Freddy had to be a guard, I don't know if he'd know not to... well..."
        show samrg ind with dissolve
        s "...Kill himself by drinking those?..."
        lf "...Yes."
        li "Okay, it didn't need to be said like that..."
        hide samrg with dissolve
        $hosp_evidence[6] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Cleaning Supplies was added to evidence."
        if False not in hosp_evidence[4:8]:
            li "I think that's everything interesting in here."
            li "Unless I want to waste time looking at the light switch, but no one would do that, right?"
        call hospDone from _call_hospDone_3
    else:
        li "The shelf has various cleaning supplies. Ammonia, bleach, ethanol, and hydrogen peroxide."
        li "They're all pretty unsafe if you use them the wrong way..."
    call screen closetInv

label closetRules:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[7]:
        li "The closet has rules too?"
        li "What could these possibly be for..."
        li "Okay, the first rule is return everything to where you found it."
        li "So if everyone followed these rules, I can assume no one stole anything from here, I guess?"
        li "The second rule is to leave the lights off."
        if not hosp_extra[0]:
            li "Okay, gotta remember that in case I try turning the lights on."
        li "And... that's it."
        li "Makes sense, it's only a closet, the fact that it has rules is surprising to begin with."
        $hosp_evidence[7] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Closet Rules was added to evidence."
        if False not in hosp_evidence[4:8]:
            li "I think that's everything interesting in here."
            li "Unless I want to waste time looking at the light switch, but no one would do that, right?"
        call hospDone from _call_hospDone_4
    else:
        li "Let's review, the closet rules are..."
        li "Return everything to where you found it, but presumably you can take things out, as long as you return them."
        li "And don't leave the lights on."
    call screen closetInv

label closetLightSwitch:
    scene bg hospcloset at bg
    $ statusnt("Closet", "lauren", ch = 3, sun = 1)
    "Flick."
    li "Hm? The light didn't turn on."
    if hosp_evidence[1]:
        li "Oh, it might be because the computer in the security room controls the lights."
        if hosp_evidence[7]:
            li "That does make the second rule on that sign a bit weird, though..."
        else:
            li "The last person to use the computer must have turned the lights here permanently off."
    else:
        li "I wonder why..."
    $hosp_extra[0] = True
    call screen closetInv

screen guardroomInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospfancy rg"
        if hosp_evidence[2]:
            hotspot(1080, 320, 66, 72) action [Hide("guardroomInv"), Jump("firstaidkit")] mouse 'q' hovered tt.Action("First Aid Kit")
        else:
            hotspot(1080, 320, 66, 72) action [Hide("guardroomInv"), Jump("firstaidkit")] mouse 'ex' hovered tt.Action("First Aid Kit")
        if hosp_evidence[3]:
            hotspot(440, 281, 137, 159) action [Hide("guardroomInv"), Jump("hosprules")] mouse 'q' hovered tt.Action("Rules of the Hospital")
        else:
            hotspot(440, 281, 137, 159) action [Hide("guardroomInv"), Jump("hosprules")] mouse 'ex' hovered tt.Action("Rules of the Hospital")
        if hosp_extra[1]:
            hotspot(152, 458, 459, 256) action [Hide("guardroomInv"), Jump("hospcouches")] mouse 'q' hovered tt.Action("Couches")
        else:
            hotspot(152, 458, 459, 256) action [Hide("guardroomInv"), Jump("hospcouches")] mouse 'ex' hovered tt.Action("Couches")
        if hosp_extra[2]:
            hotspot(1167, 257, 112, 396) action [Hide("guardroomInv"), Jump("vendingmachine")] mouse 'q' hovered tt.Action("Vending Machine")
        else:
            hotspot(1167, 257, 112, 396) action [Hide("guardroomInv"), Jump("vendingmachine")] mouse 'ex' hovered tt.Action("Vending Machine")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Guards' Commons{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("guardroomInv", transition = Dissolve(1.0)), Jump("hospInvSamGuard")]

label hospInvSamGuard:
    scene bg hospfancy at bg
    $ statusnt("Guards' Commons", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide samrg with dissolve
    call screen guardroomInv

label firstaidkit:
    scene bg hospfancy at bg
    $ statusnt("Guards' Commons", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[2]:
        li "A first aid kit."
        li "Not like we can use it to save Shahar at this point..."
        li "Let's see what's inside."
        li "Bandages, over the counter pills, a thermometer..."
        li "None of this seems to have to been used at all."
        li "Good for the people running the hospital, I guess."
        li "Scratch that, this bottle looks like it's been used..."
        li "There's a bit of dried liquid on the tip of the nozzle."
        li "But it's the only thing, a lot of the other items are still in plastic wrappers."
        li "...This might be important, let me read the bottle."
        li "Medical Glue."
        li "Usage: Closing thin wounds."
        li "Directions: Squeeze the wound shut, then apply glue."
        li "Continue to squeeze wound until glue dries."
        li "Peel glue off in two to three days."
        li "Glue has low melting point. Avoid exposing glue to heat while glue remains on wound."
        li "If the glue needs to be removed early, take a towel and dip it in near-boiling water."
        li "Then, apply the towel to the glue. It will melt and the towel will absorb it."
        li "Wash towel afterwards in hot water to remove glue."
        li "...Weird, never heard of this before."
        $hosp_evidence[2] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Bottle of Medical Glue was added to evidence."
        if False not in hosp_evidence[2:4]:
            li "I think that's everything important in here."
            li "There's a lot in this room, but not much that seems out of place..."
        call hospDone from _call_hospDone_5
    else:
        li "The first aid kit. Pretty much the only thing that looks like it's been used is medical glue."
        li "It's used for closing wounds. You can peel it off a few days after applying."
        li "Or, you can use hot water to melt it."
    call screen guardroomInv

label hosprules:
    scene bg hospfancy at bg
    $ statusnt("Guards' Commons", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[3]:
        li "The rules of the hospital..."
        li "They're the same as the ones in the cafeteria."
        li "We spent enough time staring at them on the first day here."
        li "I know them pretty much by heart now, for better or for worse."
        li "Basically..."
        li "Two guards are appointed every day."
        li "We can't be in our cells during the day."
        li "We can't be out of our cells at night."
        li "We can't go into others' cells ever."
        li "Guards can't be on the patients' side and vice-versa."
        li "And guards are responsible for feeding patients."
        li "Hmm... though now that I think about it."
        li "One of these rules raises a lot of questions..."
        $hosp_evidence[3] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Rules of the Hospital was added to evidence."
        if False not in hosp_evidence[2:4]:
            li "I think that's everything important in here."
            li "There's a lot in this room, but not much that seems out of place..."
        call hospDone from _call_hospDone_6
    else:
        li "The rules of the hospital."
        li "I pretty much know them by heart now..."
    call screen guardroomInv

label hospcouches:
    scene bg hospfancy at bg
    $ statusnt("Guards' Commons", "lauren", ch = 3, sun = 1)
    li "After being stuck in the cafeteria for days..."
    li "There's nothing I'd love more than to relax on a soft couch."
    li "...But we don't have time for that."
    $hosp_extra[1] = True
    call screen guardroomInv

label vendingmachine:
    scene bg hospfancy at bg
    $ statusnt("Guards' Commons", "lauren", ch = 3, sun = 1)
    "Flick."
    li "I wish I could tell what soda is what..."
    li "Well, I wish I could have one."
    li "Seems like you need money to get a vending machine."
    li "Almost as if the Game Master is taunting us with our inability to use the vending machine."
    if hosp_evidence[9]:
        li "You know, these bottles kind of look like the glass shards in front of Shahar..."
    $hosp_extra[2] = True
    call screen guardroomInv

screen hallwayTLInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hosphalltopleft rg"
        if hosp_evidence[11]:
            hotspot(330, 225, 130, 425) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'q' hovered tt.Action("Freddy's Cell")
        else:
            hotspot(330, 225, 130, 425) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'ex' hovered tt.Action("Freddy's Cell")
        if hosp_evidence[11]:
            hotspot(636, 301, 63, 235) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'q' hovered tt.Action("Dracula's Cell")
        else:
            hotspot(636, 301, 63, 235) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'ex' hovered tt.Action("Dracula's Cell")
        if hosp_evidence[11]:
            hotspot(773, 336, 24, 150) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'q' hovered tt.Action("Sam's Cell")
        else:
            hotspot(773, 336, 24, 150) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'ex' hovered tt.Action("Sam's Cell")
        if hosp_evidence[11]:
            hotspot(856, 357, 14, 98) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'q' hovered tt.Action("Lauren's Cell")
        else:
            hotspot(856, 357, 14, 98) action [Hide("hallwayTLInv"), Jump("cellorder")] mouse 'ex' hovered tt.Action("Lauren's Cell")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("hallwayTLInv", transition = Dissolve(1.0)), Jump("hospInvSamTL")]

label hospInvSamTL:
    scene bg hosphalltopleft at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide samrg with dissolve
    call screen hallwayTLInv

label cellorder:
    scene bg hosphalltopleft at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[11]:
        li "I sure hope wherever we go next has more comfortable cells."
        li "You know, from this side you can see people in bed and they can see you."
        li "But that's not the case from the patients' side."
        li "I guess that makes sense."
        li "The patients have privacy, but the guards can check in on people in emergencies."
        li "I had the end cell, it was kind of lonely..."
        li "I guess Shahar was on the end too. No one went out of their way to check in on him this morning."
        li "Though I don't remember where everyone else was, to be honest."
        lf "...What was the order of the cells again?"
        show samrg ind with dissolve
        s "...You, me, Dracula, Freddy..."
        s "...And then in the other hall, Jenny, Bert, Sid, and Shahar."
        lf "Oh, yeah. Thanks Sam."
        hide samrg with dissolve
        $hosp_evidence[11] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Order of the Cells was added to evidence."
        call hospDone from _call_hospDone_7
    else:
        li "Let's see, the cell order is..."
        li "Me, Sam, Dracula, Freddy, Jenny, Bert, Sid, Shahar."
    call screen hallwayTLInv

screen hallwayTRInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg shahardead rg"
        if hosp_evidence[8]:
            hotspot(573, 358, 114, 265) action [Hide("hallwayTRInv"), Jump("shaharbody")] mouse 'q' hovered tt.Action("Shahar's Corpse")
        else:
            hotspot(573, 358, 114, 265) action [Hide("hallwayTRInv"), Jump("shaharbody")] mouse 'ex' hovered tt.Action("Shahar's Corpse")
        if hosp_evidence[9]:
            hotspot(553, 623, 174, 63) action [Hide("hallwayTRInv"), Jump("glassshards")] mouse 'q' hovered tt.Action("Shards of Glass")
        else:
            hotspot(553, 623, 174, 63) action [Hide("hallwayTRInv"), Jump("glassshards")] mouse 'ex' hovered tt.Action("Shards of Glass")
        if hosp_evidence[10]:
            hotspot(219, 0, 1060, 52) action [Hide("hallwayTRInv"), Jump("pipe")] mouse 'q' hovered tt.Action("Pipe")
        else:
            hotspot(219, 0, 1060, 52) action [Hide("hallwayTRInv"), Jump("pipe")] mouse 'ex' hovered tt.Action("Pipe")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("hallwayTRInv", transition = Dissolve(1.0)), Jump("hospInvSamTR")]

label hospInvSamTR:
    scene bg shahardead at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve:
        xcenter .25
    lf "Notice anything Sam?"
    s "...Not really..."
    li "...Nothing? Shahar's body doesn't throw you off?"
    hide samrg with dissolve
    call screen hallwayTRInv

label shaharbody:
    scene bg shahardead at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[8]:
        li "Ugh."
        li "I hate dead bodies..."
        li "Poor Shahar. I'll never know if he really thought he was a pirate or if it was an act but..."
        li "If he thought that, it's really sad."
        li "Okay, no more stalling, have to look at him eventually."
        li "He's kneeling and leaning against the bar, as if he fell forward."
        li "Hm... he's only bleeding from the forehead, at the point where his head is leaning against the bar."
        li "I don't really see any wounds or bruises or anything besides that."
        li "That's weird... did one blow to the forehead kill Shahar?"
        $hosp_evidence[8] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "State of the Body was added to evidence."
        if False not in hosp_evidence[8:11]:
            li "I think that's everything..."
            li "It's not a lot though. I'm really confused as to what happened."
            li "But whatever, I'm happy to get away from the corpse."
        call hospDone from _call_hospDone_8
    else:
        li "Shahar's corpse. He has blood on his forehead, where his body is leaning against the bar."
        li "Besides that, I don't see anything out of place."
    call screen hallwayTRInv

label glassshards:
    scene bg shahardead at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[9]:
        li "Huh?"
        li "What's all this glass doing here?"
        li "It looks like the bottles from the vending machine but..."
        li "When I looked earlier, I noticed the vending machine requires cash."
        li "Something I don't think we have."
        li "So why are these there?"
        li "Also... something is weird about the way these shards look."
        li "But I can't quite put my finger on what..."
        $hosp_evidence[9] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Glass Shards was added to evidence."
        if False not in hosp_evidence[8:11]:
            li "I think that's everything..."
            li "It's not a lot though. I'm really confused as to what happened."
            li "But whatever, I'm happy to get away from the corpse."
        call hospDone from _call_hospDone_9
    else:
        li "Glass shards, in front of Shahar's corpse."
        li "They look like the ones from the vending machine."
        li "It's not clear how they got here."
        li "There's also something that bothers me about them..."
    call screen hallwayTRInv

label pipe:
    scene bg shahardead at bg
    $ statusnt("Guards' Hallway", "lauren", ch = 3, sun = 1)
    if not hosp_evidence[10]:
        li "Y'know, I never really noticed these pipes on the ceiling."
        li "The pipe's about twelve feet off the ground..."
        li "I couldn't reach up there if I tried, so I don't think it's relevant, but..."
        li "Can't hurt to remember this, I guess."
        $hosp_evidence[10] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Pipe in the Hallway was added to evidence."
        if False not in hosp_evidence[8:11]:
            li "I think that's everything..."
            li "It's not a lot though. I'm really confused as to what happened."
            li "But whatever, I'm happy to get away from the corpse."
        call hospDone from _call_hospDone_10
    else:
        li "There's a pipe on the ceiling, about twelve feet off the ground."
        li "I don't think it's relevant, but might as well remember it."
    call screen hallwayTRInv

screen hospKitchenInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospkitchen rg"
        if hosp_extra[3]:
            hotspot(595, 318, 135, 256) action [Hide("hospKitchenInv"), Jump("hospfridge")] mouse 'q' hovered tt.Action("Fridge")
        else:
            hotspot(595, 318, 135, 256) action [Hide("hospKitchenInv"), Jump("hospfridge")] mouse 'ex' hovered tt.Action("Fridge")
        if hosp_extra[4]:
            hotspot(247, 455, 267, 260) action [Hide("hospKitchenInv"), Jump("hospstove")] mouse 'q' hovered tt.Action("Stove")
        else:
            hotspot(247, 455, 267, 260) action [Hide("hospKitchenInv"), Jump("hospstove")] mouse 'ex' hovered tt.Action("Stove")
        if hosp_extra[5]:
            hotspot(506, 450, 37, 158) action [Hide("hospKitchenInv"), Jump("hospcabinets")] mouse 'q' hovered tt.Action("Kitchen Storage")
            hotspot(775, 420, 203, 218) action [Hide("hospKitchenInv"), Jump("hospcabinets")] mouse 'q' hovered tt.Action("Kitchen Storage")
        else:
            hotspot(506, 450, 37, 158) action [Hide("hospKitchenInv"), Jump("hospcabinets")] mouse 'ex' hovered tt.Action("Kitchen Storage")
            hotspot(775, 420, 203, 218) action [Hide("hospKitchenInv"), Jump("hospcabinets")] mouse 'ex' hovered tt.Action("Kitchen Storage")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "laurenchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("hosp_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSamKitchen")]
    imagebutton:
        xpos 20
        ypos 70
        idle "windowchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSamKitchen")]
    imagebutton:
        xpos 20
        ypos 120
        idle "jennychibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvJenny")]
    imagebutton:
        xpos 20
        ypos 170
        idle "draculachibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvDracula")]
    imagebutton:
        xpos 20
        ypos 220
        idle "sidchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSid")]
    imagebutton:
        xpos 20
        ypos 270
        idle "freddychibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvFreddy")]
    imagebutton:
        xpos 20
        ypos 320
        idle "bertchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvBert")]

label hospfridge:
    scene bg hospkitchen at bg
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    li "I wish we had time to cook a meal."
    li "I'm so hungry..."
    li "Not that the ingredients in the fridge are very appetizing..."
    li "One can only eat so many tomatoes without getting bored."
    li "Anyway, I don't think the liquid dripping from Shahar's head was tomato juice."
    li "So no need to search the fridge."
    $hosp_extra[3] = True
    call screen hospKitchenInv

label hospstove:
    scene bg hospkitchen at bg
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    li "For what seems like an old mental hospital, this oven is pretty fancy."
    li "...Yet another thing that could harm Freddy if no one was watching him."
    li "I hope he's been doing okay while I've been running around investigating."
    li "Well, the sooner we solve this case, the sooner I can reunite with him."
    $hosp_extra[4] = True
    call screen hospKitchenInv

label hospcabinets:
    scene bg hospkitchen at bg
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    li "Let me see, is there anything in the cabinets..."
    li "Well, there's the bare essentials you'd find a kitchen."
    li "Salt, pepper, ladles.."
    li "Oh, and a knife."
    li "But... I don't think Shahar was stabbed."
    li "Also, if someone walked out of the kitchen with a knife, we might have seen them."
    li "Seems a bit risky..."
    li "Not to mention well..."
    show samrg ind with dissolve
    li "Even if they did try to stab him, it might not have killed him."
    s "...Why are you looking at me like that..."
    lf "Huh? Oh, nothing, just got lost in thought."
    s "...Kay..."
    hide samrg with dissolve
    li "Anyway, I don't think it's worth worrying about the knife in here."
    li "Well, unless we find some other reason to believe a knife is important..."
    $hosp_extra[5] = True
    call screen hospKitchenInv

label hospInvSamKitchen:
    scene bg hospkitchen at bg
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    show samrg ind with dissolve
    lf "Notice anything Sam?"
    s "...Food..."
    li "I guess, ask stupid questions, get stupid answers."
    hide samrg with dissolve
    call screen hospKitchenInv with dissolve

label hospInvJenny:
    scene bg hospkitchen at bg with Dissolve(0.0)
    scene bg hospkitchenwindow
    show hospwindowoverlay
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show jennyrg ind at inwindow behind hospwindowoverlay with dissolve
    lf "Jenny, anything you think we should look at?"
    j "Ooh, is the chess set still in the guard's room?"
    lf "...Chess set?"
    j "Yeah, Bert and I played a game two days ago."
    li "...Or, you could help investigate."
    lf "Yeah, I'll take a look and let you know if it's still there."
    show jennyrg happy at inwindow behind hospwindowoverlay
    j "Really? Thanks Lauren!"
    li "I am {i}not{/i} going to look for a chess set."
    li "Not like Shahar died by choking on a bishop."
    hide jennyrg with dissolve
    call screen hospKitchenInv with dissolve

label hospInvDracula:
    scene bg hospkitchen at bg with Dissolve(0.0)
    scene bg hospkitchenwindow
    show hospwindowoverlay
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show dracrg ind at inwindow behind hospwindowoverlay with dissolve
    d "Greetings Lauren. How goes the investigation?"
    if len([x for x in hosp_evidence if x]) > 5:
        lf "Pretty good, I think I'm at least halfway done?"
        d "Good, I look forward to hearing your report once you're finished."
        lf "Report?"
        d "Well, as the only two people capable of investigating, you and Sam to give a comprehensive report."
        d "That would only be par for the course at any respectable establishment."
        li "...This isn't an establishment, it's a killing game."
        lf "Yeah, we'll tell you everything we see."
        d "Good."
    else:
        lf "Uhh, I only really just started..."
        d "Really? It feels like you've been going at it for a while."
        lf "It's only been a few minutes..."
        d "You must keep a faster pace."
        d "After all, you and Sam are the only ones who can investigate."
        d "And the less time you spend investigating, the more time we can spend deliberating."
        li "We don't know for sure that there's a time limit yet..."
        lf "Yeah, we'll get on it."
        d "Yes, make haste."
    d "In the meantime, as I'm sure you guessed, we haven't found much over here."
    d "It would help if the child were not so exasperated."
    lf "There's four of you. None of you can watch over Freddy while the rest look around?"
    d "Children are beyond me, I'm afraid."
    li "I can't stand talking to this guy."
    lf "I'm gonna go keep investigating."
    d "Yes, good plan."
    hide dracrg with dissolve
    call screen hospKitchenInv with dissolve

label hospInvBert:
    scene bg hospkitchen at bg with Dissolve(0.0)
    scene bg hospkitchenwindow
    show hospwindowoverlay
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show bertrg ind at inwindow behind hospwindowoverlay with dissolve
    b "Hey Lauren. How's the investigation going?"
    lf "It's going. I'm not as used to this as you are."
    lf "Usually I just take care of Freddy and keep him away from the body while you do this..."
    b "Oh. Are we supposed to be doing that?"
    lf "Doing what?"
    b "Uh. I guess keeping Freddy away from the body."
    lf "Um... did he go to check Shahar's cell?"
    b "No, he's just been chilling here with the rest of us."
    lf "...Can you make sure he doesn't go towards Shahar's cell?"
    b "Uh, sure, though it might be hard while we're looking around."
    lf "There's four of you, surely one of you can handle it."
    b "Oh. True."
    li "What I'd give to trade places with him right now..."
    li "I'm sure he'd be happy to do that too..."
    hide bertrg with dissolve
    call screen hospKitchenInv with dissolve

label hospInvFreddy:
    scene bg hospkitchen at bg with Dissolve(0.0)
    scene bg hospkitchenwindow
    show hospwindowoverlay
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show frogrg sad at inwindow behind hospwindowoverlay with dissolve
    f "Lauren... why are you over there?"
    f "When are you gonna come back and play with me?"
    lf "Soon Freddy. I have some important work to do..."
    f "Important work?"
    lf "Uh, remember all those debates we've had since we got here?"
    lf "You know, before we fall asleep and wake up somewhere else."
    lf "We spend a lot of time asking each other questions and stuff like that?"
    f "Oh. Yeah, I remember those."
    lf "Well uh, before the debates, while you and I were playing, the others would usually find stuff for us."
    lf "Stuff we needed to talk about."
    lf "But now it's my turn to do it."
    lf "Taking turns is fair, right Freddy?"
    f "Yeah... Lauren?"
    lf "Yeah?"
    f "Why does no one ever tell me anything?"
    f "It's like the rest of you have secrets and I don't like it."
    f "I... I know what \"murder\" means. I've watched TV, you know."
    f "That's what the superheroes do to the bad guys!"
    li "He's right, we're being dishonest with him by trying to hide the dead bodies."
    li "And then still having him sit through us trying to solve the murders."
    li "And kids catch on to more than we think."
    li "He probably knows someone is dead but knows we don't want to talk to him about it."
    li "Who knows, maybe he's seen a dead body before."
    li "But... I can't let him be like me."
    li "Those weeks after the murder."
    li "No, not weeks. Years."
    li "I wouldn't want him to go through that."
    lf "Freddy, there's some... stuff that kids shouldn't see."
    f "Oh, like when daddy and his nurse locked the door and wouldn't let me in?"
    lf "Uh... not quite."
    lf "Look, you... have a long life ahead of you."
    lf "One you should get to enjoy as much as possible."
    lf "Find lots of frogs, have lots of cake."
    f "I do like cake and frogs."
    lf "Right. You'll have less fun if you see some of the things we're hiding."
    lf "We're old, we don't have our childhood anymore, so we don't need to worry about that."
    lf "Does that make sense?"
    f "...I think so."
    lf "Sorry Freddy, I know it's no fun when others know more than you do."
    f "It's okay... I trust you Lauren."
    f "But you're taking me to a zoo when this is done!"
    lf "Deal."
    hide frogrg with dissolve
    call screen hospKitchenInv with dissolve

label hospInvSid:
    scene bg hospkitchen at bg with Dissolve(0.0)
    scene bg hospkitchenwindow
    show hospwindowoverlay
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show sidrg ind at inwindow behind hospwindowoverlay with dissolve
    if not hosp_evidence[12]:
        i "Oh, *cough* hey Lauren..."
        lf "Hey Sid, everything okay?"
        i "Uh, could be better."
        i "I've had a really bad cough since this morning."
        i "I'm *cough* having trouble breathing, my throat... tastes sweaty?"
        i "It's hard to explain."
        lf "Oh, geez..."
        lf "Let me get you some water."
        lf "..."
        lf "Here you go."
        i "Thanks."
        lf "If you want I can get you something from the first aid kit to help you?"
        i "I-*cough* I'm fine, you need to investigate..."
        lf "This only started today?"
        i "Yeah, I was feeling totally *cough* fine when I went to sleep last night."
        i "Then I woke *cough* up a bit before the alarm went off because I was coughing."
        lf "That's weird... get better soon Sid."
        lf "I'll try to get this investigation moving so we can take care of you as soon as possible."
        i "*cough* Thanks Lauren."
        hide sidrg with dissolve
        li "Hm... it's a bit weird that Sid suddenly started coughing overnight."
        lf "I wonder..."
        $hosp_evidence[12] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        "Sid's Account was added to evidence."
        call hospDone from _call_hospDone_11
    else:
        li "I wonder why Sid suddenly started coughing only today?"
        i "*cough* Hey Lauren..."
        li "Hang in there Sid, we'll get out of here soon."
        hide sidrg with dissolve
    call screen hospKitchenInv with dissolve

label hospDone:
    if False not in hosp_evidence[1:]:
        li "Actually, I'm not really used to this investigating thing but..."
        li "I don't think there's any places left to check."
        li "I guess I should go back and tell everyone what I've found."
        jump trial3a
    return
