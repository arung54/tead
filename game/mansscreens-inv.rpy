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
            textbutton "Location and the Murderer" style "button_text" action SetVariable("currEvidence", 7)
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
            text "We think the murderer is someone who's been in the mansion before this game started." xcenter 800 yanchor 0.0 ypos 330

screen kitchenInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionkitchen.png"
        if train_evidence1[1]:
            hotspot(480, 198, 320, 148) action [Hide("frontCarInv"), Jump("trainFrontWindow")] mouse 'q' hovered tt.Action("Front Window")
        else:
            hotspot(480, 198, 320, 148) action [Hide("frontCarInv"), Jump("trainFrontWindow")] mouse 'ex' hovered tt.Action("Front Window")
        if train_evidence1[0]:
            hotspot(342, 100, 97, 250) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'q' hovered tt.Action("Computer")
            hotspot(830, 94, 107, 255) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'q' hovered tt.Action("Computer")
            hotspot(529, 48, 221, 107) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'q' hovered tt.Action("Computer")
        else:
            hotspot(342, 100, 97, 250) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'ex' hovered tt.Action("Computer")
            hotspot(830, 94, 107, 255) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'ex' hovered tt.Action("Computer")
            hotspot(529, 48, 221, 107) action [Hide("frontCarInv"), Jump("trainComputer")] mouse 'ex' hovered tt.Action("Computer")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"

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

screen diningInv():
    add "bg mansiondining.png"
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

screen garageInv():
    add "bg mansiongarage.png"
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

screen hallwayInv():
    add "bg mansionhall.png"
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

screen bedroomInv():
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
    add "bg mansionmasterbedroom.png"
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

screen bathroomInv():
    add "bg mansionmasterbr.png"
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
