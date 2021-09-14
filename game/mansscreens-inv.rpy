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
    call screen backCarInv

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
    call screen backCarInv

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
    call screen backCarInv

screen diningInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansiondining.png"
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

screen garageInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansiongarage.png"
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
