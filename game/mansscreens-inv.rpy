screen mansMapInv():
    #TODO: Gate rooms for FT4
    #TODO: Create secret sesame FTE
    imagemap:
        ground "mansMapoverlay.png"
        hotspot(762, 310, 155, 174):
            action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("kitchenInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay1.png")
            unhovered Hide("mansPreview")
        hotspot(920, 311, 329, 175):
            action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("diningInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(1090, 489, 160, 195):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("garageInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(153, 471, 561, 69):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("hallwayInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(153, 539, 77, 145):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("hallwayInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(152, 310, 156, 157):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("bedroomFLInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(307, 310, 83, 83):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("bedroomFLInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(497, 310, 218, 158):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("bedroomInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(234, 544, 225, 140):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("bedroomInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(463, 543, 251, 141):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("masterBedroom", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(393, 310, 101, 158):
            if ftecounter != 4:
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomFLInv"), Hide("masterBedroom"), Hide("bathroomInv"), Show("bathroomInv", transition=Dissolve(0.3)), Hide("mansMap"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")

    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("mansMapInv", transition=Dissolve(0.3)), Hide("mansPreview")]


screen mans_evidence():
    add "eviscroll"
    modal True

    imagemap:
        ground "evidenceui.png"
        #add "usethis.png" xcenter 800 yalign .9
        hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("mans_evidence", transition=Dissolve(0.3))]
    vbox xalign 0.15 yalign 0.75 spacing 30:
        if mans_evidence[0]:
            textbutton "Shape of the Wound" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[1]:
            textbutton "Blood from the Wound" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[2]:
            textbutton "Damp Clothing" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[3]:
            textbutton "Burns on Stella's Hands" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[4]:
            textbutton "Wires and Hole Under the Sink" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[5]:
            textbutton "Generator" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[6]:
            textbutton "Rope Attached to Generator" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[7]:
            textbutton "Knife Sheath" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if mans_evidence[8]:
            textbutton "Location and the Murderer" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "Stella was seemingly stabbed in the back. The wound is long in one direction but narrow in the other." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "The blood on Stella's back has dried a bit. There's not a lot of blood for how damaging the wound seems, almost as if something was used to seal the wound afterwards." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "A part of Stella's clothes was rather damp around the area she was stabbed in. However, this part wasn't stained, so it seems to have been water rather than blood." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev2 hand.png" xcenter 800 yalign 0.1
            text "Each of Stella's hands had a rectangular burn mark on the palm." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev2 wires.png" xcenter 800 yalign 0.1
            text "During the investigation, we found wires under the sink that entered through a hole in the bathroom wall." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "There was a generator in Jenny's bedroom. We saw the generator in the garage earlier." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "A rope was attached to the handle of the generator. The generator has wheels, so the rope can be used to easily pull it around." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev2 sheath.png" xcenter 800 yalign 0.1
            text "A sheath that Sam found during the party and used to cut the cake. As far as we know, the sheath remained in the kitchen or dining room for the entire party." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "Earlier, we discussed Kaiser's death and concluded the murderer is probably someone who's been in this mansion before." xcenter 800 yanchor 0.0 ypos 330

screen kitchenInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionkitchen.png"
        if mans_extra[0]:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'q' hovered tt.Action("Microwave and Oven")
        else:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'ex' hovered tt.Action("Microwave and Oven")
        if mans_extra[1]:
            hotspot(111, 522, 482, 168) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(273, 206, 169, 145) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(441, 205, 113, 84) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(556, 211, 145, 139) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
        else:
            hotspot(111, 522, 482, 168) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(273, 206, 169, 145) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(441, 205, 113, 84) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(556, 211, 145, 139) action [Hide("frontCarInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
        if mans_extra[2]:
            hotspot(917, 241, 251, 448) action [Hide("kitchenInv"), Jump("mansFridge")] mouse 'q' hovered tt.Action("Fridge and Freezer")
        else:
            hotspot(917, 241, 251, 448) action [Hide("kitchenInv"), Jump("mansFridge")] mouse 'ex' hovered tt.Action("Fridge and Freezer")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

label mansAppliances:
    scene bg mansionkitchen
    $mans_extra[0] = True
    $ statusnt("Kitchen", "bert", ch = 2, sun = 3)
    bi "Hmm... the microwave and oven's digital clocks aren't working like Jenny said."
    bi "But Catherine was still able to cook."
    bi "So the kitchen didn't lose power... did someone mess with them?"
    if False not in mans_extra[0:2]:
        bi "I was able to double check what people said about the kitchen, but I didn't learn much new."
        bi "Maybe I should check elsewhere."
    call screen kitchenInv

label mansCupboards:
    scene bg mansionkitchen
    $mans_extra[1] = True
    $ statusnt("Kitchen", "bert", ch = 2, sun = 3)
    bi "Let me try looking through the cupboards and drawers."
    bi "..."
    bi "Hmm... lots of silverware, fancy glasses, and utensils."
    bi "But no sharp objects, just like Sam said."
    if False not in mans_extra[0:2]:
        bi "I was able to double check what people said about the kitchen, but I didn't learn much new."
        bi "Maybe I should check elsewhere."
    call screen kitchenInv

label mansFridge:
    scene bg mansionkitchen
    $mans_extra[2] = True
    $ statusnt("Kitchen", "bert", ch = 2, sun = 3)
    bi "...I wonder if there's any leftovers in here."
    bi "..."
    bi "Wow, there's a lot of food in the fridge. We could have stayed here for days."
    bi "Unfortunately, dead bodies kind of ruin my appetite..."
    bi "I should check the freezer as well, while I'm here."
    bi "...Huh, it's pretty empty."
    bi "Just an ice cube tray. Guess the homeowner isn't a fan of frozen food."
    if False not in mans_extra[0:2]:
        bi "I was able to double check what people said about the kitchen, but I didn't learn much new."
        bi "Maybe I should check elsewhere."
    call screen kitchenInv

screen diningInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansiondining knife.png"
        if mans_evidence[7]:
            hotspot(829, 524, 138, 27) action [Hide("kitchenInv"), Jump("mansSheath")] mouse 'q' hovered tt.Action("Knife and Sheath")
        else:
            hotspot(829, 524, 138, 27) action [Hide("kitchenInv"), Jump("mansSheath")] mouse 'q' hovered tt.Action("Knife and Sheath")
        if mans_extra[3]:
            hotspot(794, 198, 62, 76) action [Hide("kitchenInv"), Jump("mansSydell")] mouse 'q' hovered tt.Action("Mr. Sydell")
        else:
            hotspot(794, 198, 62, 76) action [Hide("kitchenInv"), Jump("mansSydell")] mouse 'q' hovered tt.Action("Mr. Sydell")

    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Dining Room{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "draculachibi.png" at chibizoom
        action [Hide("diningInv"), Jump("mansDracula")]

label mansSheath:
    scene bg mansiondining knife
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    bi "The knife we used to cut the meatloaf."
    bi "I don't think Stella was stabbed with it."
    bi "After all, it was in the kitchen or dining room for the whole party, and there are multiple accounts of this."
    bi "So it's probably not relevant to the murder."
    bi "The sheath on the other hand..."
    bi "Sam claimed to find it in the middle of the party."
    bi "If Sam was the first person to find it, that means after we found it, it was around us the entire time."
    bi "In that case it wouldn't be relevant to the murder eitehr."
    bi "But maybe someone found the sheath beforehand?"
    bi "I should keep that possibility in mind..."
    if not mans_evidence[7]:
        $mans_evidence[7] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Knife Sheath was added to evidence."
    if False not in mans_evidence[7:8]:
        bi "Hmm... I think that's everything to find here."
        bi "Not that I found much, mostly the sheath and talking to Dracula about stuff I already knew..."
    if False not in mans_evidence:
        bi "Actually, I think I've found most of the major pieces of evidence..."
        bi "At least, enough to start discussing with others."
        bi "Let's go gather everyone."
        jump mansDone
    call screen diningInv

label mansDracula:
    scene bg mansiondining knife
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    show drac ind with dissolve
    d "Hm... unfortunate my ploy didn't work."
    b "Your ploy?"
    d "I was hoping someone would admit to a crime that could be tied to this location."
    d "If so, they would probably be the murderer."
    bi "Oh, he's referring to the conversation we had earlier."
    bi "Back then, we concluded as a group the murderer this round is probably someone who's been in this house before."
    bi "This is the first time we're solving a murder with this information in mind, maybe I should remember it."
    hide drac with dissolve
    if not mans_evidence[7]:
        $mans_evidence[7][1] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Location and the Murderer was added to evidence."
    if False not in mans_evidence[7:8]:
        bi "Hmm... I think that's everything to find here."
        bi "Not that I found much, mostly the sheath and talking to Dracula about stuff I already knew..."
    if False not in mans_evidence:
        bi "Actually, I think I've found most of the major pieces of evidence..."
        bi "At least, enough to start discussing with others."
        bi "Let's go gather everyone."
        jump mansDone
    call screen diningInv

label mansSydell:
    scene bg mansiondining knife
    $mans_extra[3] = True
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    bi "Mr. Sydell's portrait..."
    bi "At this point, I doubt anyone will admit to knowing him."
    bi "Maybe if we catch the murderer and they're feeling nice, they'll tell us about him."
    bi "For now, I think that's our only lead for finding the mastermind..."

screen garageInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansiongarage.png"
        if mans_extra[4]:
            hotspot(836, 191, 442, 414) action [Hide("kitchenInv"), Jump("mansGarage")] mouse 'q' hovered tt.Action("Missing Items")
        else:
            hotspot(836, 191, 442, 414) action [Hide("kitchenInv"), Jump("mansGarage")] mouse 'ex' hovered tt.Action("Missing Items")
        if mans_extra[5]:
            hotspot(214, 179, 563, 348) action [Hide("kitchenInv"), Jump("mansGarageDoor")] mouse 'q' hovered tt.Action("Garage Door")
        else:
            hotspot(214, 179, 563, 348) action [Hide("kitchenInv"), Jump("mansGarageDoor")] mouse 'ex' hovered tt.Action("Garage Door")

    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Garage{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "draculachibi.png" at chibizoom
        action [Hide("garageInv"), Jump("mansGarage")]

label mansGarage:
    scene bg mansiongarage
    $mans_extra[4] = True
    $ statusnt("Garage", "bert", ch = 2, sun = 3)
    show sid ind with dissolve
    b "Sid, you explored around here on the first day, right?"
    b "Do you remember what items were here before that aren't now?"
    i "Let's see, what's missing..."
    i "The clock, for one, and some batteries."
    b "Right, Catherine and Jenny were using the clock because the microwave and oven clocks broke."
    b "And Catherine asked Jenny to grab the batteries for the clock."
    i "The stepstool's gone too."
    b "Sam brought that to the kitchen to search for something to cut the cake with."
    i "The generator's missing. Also some rope."
    if mans_evidence[5]:
        b "Right, I saw the generator and rope in Jenny's room earlier during the investigation."
    else:
        b "...Huh?"
        b "Where did those go?"
        b "I guess I should work on finding them."
    i "Besides that, I think everything's here."
    if mans_evidence[4]:
        b "Huh... Sid, were there not wires in here before?"
        i "Wires? Uh... not that I can remember."
        bi "Interesting... I wonder where the wires I found under the sink came from..."
    b "Okay, that was actually very useful."
    if mans_evidence[5]:
        b "Everything that was in the garage is accounted for, so we don't have to worry about any surprise tools."
    b "Thanks Sid!"
    i "Y-yeah."
    i "Bert... you'll solve this one too, right?"
    bi "Will I?"
    bi "I don't know, but..."
    b "Yeah Sid. I have some theories already, actually."
    i "Oh. Okay, cool..."
    hide sid ind with dissolve
    call screen garageInv

label mansGarageDoor:
    scene bg mansiongarage
    $ statusnt("Garage", "bert", ch = 2, sun = 3)
    if mans_extra[5]:
        b "Hm... maybe the murderer managed to open the garage door, went to a store, and bought a knife!"
        show sid ind with dissolve
        i "That... seems unlikely."
        b "Oh. Yeah, you're right."
        bi "Whoops, didn't realize I said that out loud."
        hide sid ind with dissolve
    else:
        bi "As nice as it would be to think about escaping through here..."
        bi "I don't think this door is going to open anytime soon."
        bi "Have to focus on the investigation for now."
        $mans_extra[5] = True
    call screen garageInv

screen hallwayInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionhallway.png"
        if mans_extra[0]:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'q' hovered tt.Action("Microwave and Oven")
        else:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'ex' hovered tt.Action("Microwave and Oven")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

screen bedroomInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionbedroom.png"
        if mans_extra[0]:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'q' hovered tt.Action("Microwave and Oven")
        else:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'ex' hovered tt.Action("Microwave and Oven")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

screen bedroomFLInv():
    add "bg mansionbedroom.png"
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0 #TODO: Make cases for this
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

screen masterBedroomInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionmasterbedroom.png"
        if mans_extra[0]:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'q' hovered tt.Action("Microwave and Oven")
        else:
            hotspot(444, 289, 109, 174) action [Hide("kitchenInv"), Jump("mansAppliances")] mouse 'ex' hovered tt.Action("Microwave and Oven")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Master Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

screen bathroomInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionbr.png"
        if mans_evidence[4]:
            hotspot(481, 523, 102, 196) action [Hide("bathroomInv"), Jump("mansSink")] mouse 'q' hovered tt.Action("Under the Sink")
        else:
            hotspot(481, 523, 102, 196) action [Hide("bathroomInv"), Jump("mansSink")] mouse 'ex' hovered tt.Action("Under the Sink")
        if mans_evidence[3]:
            hotspot(269, 425, 84, 59) action [Hide("bathroomInv"), Jump("mansHands")] mouse 'q' hovered tt.Action("Stella's Hands")
        else:
            hotspot(269, 425, 84, 59) action [Hide("bathroomInv"), Jump("mansHands")] mouse 'q' hovered tt.Action("Stella's Hands")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

    add "status.png"
    add Text("{b}Bathroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch2.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun3.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    add "stella dead.png" zoom 1.0 xcenter .37 ycenter .8

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("mansMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("mans_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "shaharchibi.png" at chibizoom
        action [Hide("kitchenInv"), Jump("mansHands")]

label mansSink:
    scene bg mansionbr
    $ statusnt("Kitchen", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    if not mans_evidence[4]:
        bi "Hm... I wonder if Stella made any progress stealing the sink handle before she died."
        bi "I doubt it'll lead to anything, but might as well look under there."
        bi "...Huh?"
    show ev2 wires with dissolve
    bi "There's wires under the sink."
    bi "They seem to be attached to the sink, and they're fed through a hole in the wall."
    if mans_evidence[5]:
        bi "I wonder... were they connected to that?"
    else:
        bi "These weren't here last night, are they relevant to the murder?"
    hide ev2 wires with dissolve
    if not mans_evidence[4]:
        $mans_evidence[4] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Wires and Hole Under the Sink was added to evidence."
    if False not in mans_evidence[0:4]:
        bi "Hmm... I found a lot in the bathroom, but I think that's everything."
        bi "Though this has brought up more questions than answers..."
    if False not in mans_evidence:
        bi "Actually, I think I've found most of the major pieces of evidence..."
        bi "At least, enough to start discussing with others."
        bi "Let's go gather everyone."
    call screen garageInv

label mansHands:
    scene bg mansionbr
    $ statusnt("Kitchen", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    if not mans_evidence[3]:
    show shahar mad with dissolve
        b "...Shahar, is that Stella's ring on your finger?"
        h "What? I'm a pirate, I own lots er booty, what makes ye think I stole this one from my good friend?"
        b "So if I check Stella's hands, there will be a ring there."
        h "..."
        b "Okay then, let me look at her hands..."
        b "..."
        b "Yup, there's no ring here."
        h "...I mean, maybe the lass just lost her golden piece at the party?"
        b "Suuuuuuuure."
        h "Hey lad, don't deny a grievin' seafarer a memento of a fallen comrade."
        b "Fine, you can keep the ring..."
        b "..."
        b "Huh?"
        hide shahar with dissolve
    show ev2 hand with dissolve
    bi "These look like burns on her palms..."
    b "Did the killer burn Stella before or after stabbing her?"
    b "Also, they're shaped like rectangles... I wonder why..."
    hide ev2 hand with dissolve
    if False not in mans_evidence[0:4]:
        bi "Hmm... I found a lot in the bathroom, but I think that's everything."
        bi "Though this has brought up more questions than answers..."
    if False not in mans_evidence:
        bi "Actually, I think I've found most of the major pieces of evidence..."
        bi "At least, enough to start discussing with others."
        bi "Let's go gather everyone."
    jump mansDone
    if not mans_evidence[3]:
        $mans_evidence[3] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Burns on Stella's Hands was added to evidence."
    call screen garageInv
