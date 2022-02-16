screen hospMapInv():
    modal True
    #TODO: Create secret sesame FTE
    if ftecounter == 5:
        imagemap:
            ground "map3uiGUARD.png"
            hotspot(460, 273, 108, 78):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("securityInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay8.png")
                unhovered Hide("hospPreview")
            hotspot(567, 275, 287, 177):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("guardroomInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay9.png")
                unhovered Hide("hospPreview")
            hotspot(851, 273, 90, 78):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("closetInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay1.png")
                unhovered Hide("hospPreview")
            hotspot(568, 451, 285, 87):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hospKitchenInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay5.png")
                unhovered Hide("hospPreview")
            hotspot(202, 376, 367, 53):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hallwayTLInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay4.png")
                unhovered Hide("hospPreview")
            hotspot(853, 376, 363, 51):
                action [Hide("securityInv"), Hide("guardroomInv"), Hide("closetInv"), Hide("hospKitchenInv"), Hide("hallwayTLInv"), Hide("hallwayTRInv"), Show("hallwayTRInv", transition=Dissolve(0.3)), Hide("hospMapInv"), Hide("hospPreview")]
                hovered ShowTransient("hospPreview", img="hospmapoverlay4b.png")
                unhovered Hide("hospPreview")
    imagemap:
        idle "trainMapoverlayleft.png"
        hotspot(0, 0, 119, 719) action [Hide("hospMapInv", transition=Dissolve(0.3)), Hide("hospPreview")]

screen hosp_evidence():
    add "eviscroll"
    modal True

    imagemap:
        ground "evidenceui.png"
        #add "usethis.png" xcenter 800 yalign .9
        hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("hosp_evidence", transition=Dissolve(0.3))]
    vbox xalign 0.15 yalign 0.75 spacing 30:
        if hosp_evidence[0]:
            textbutton "Sam and Lauren's Account" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[1]:
            textbutton "Security Room" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[2]:
            textbutton "Bottle of Medical Glue" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[3]:
            textbutton "Rules of the Prison" style "button_text" action SetVariable("currEvidence", 3)
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
            textbutton "State of the Body" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[8]:
            textbutton "Glass Shards" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[9]:
            textbutton "Pipes in the Hallway" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if hosp_evidence[10]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "Sam claims to have woken up before the intercom went off and stared out the door on the guard side of his door until morning. Sam didn't see or hear anything until Lauren showed up to get Sam out of the cell. Lauren claims she left her cell as soon as possible and waited outside Sam's cell." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "The security room has several features: \n1) A camera viewing the cafeteria\n2) Controlling the lights\n3) Cycling hot water through plumbing\n4) Changing the temperature throughout the building" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "The bottle of medical glue in the first aid kit had a bit of residue on the nozzle. According to the instructions, medical glue is used for sealing glue and hardened medical glue can be cleaned up by applying a towel dipped in near-boiling water." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "The rules of the prison state \n1) Two guards are appointed every day\n2) During the day, we cannot be in our cells\n3) At night, we must be in our cells\n4) No one may enter another person's cell\n5)Guards cannot be on the patients' side of the floor and vice-versa\n6) Guards are responsible for feeding patients" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "The baseball bat was still in the closet and looked like it was in mint condition." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "There is a stepstool in the supply closet, but the highest step is only a few feet off the ground." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "The closet has a number of cleaning supplies, including ammonia, bleach, ethanol, and hydrogen peroxide." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "Shahar's corpse was found kneeling, with his forehead resting on a bar of his cell. His forehead is bleeding where it touches the bar, and the blood is running down the bar. No other injuries are visible." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "A number of glass shards were found in front of Shahar's corpse." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "Several pipes run along the ceiling of the hallway where Shahar's body was found." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "Sid woke up with a bad cough this morning." xcenter 800 yanchor 0.0 ypos 330


screen securityInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospsecurity.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Security{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

screen closetInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospcloset.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Closet{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

screen guardroomInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospfancy.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Guards' Commons{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

screen hallwayTLInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hosphalltopleft.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

screen hallwayTRInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hosphalltopright 2.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Guards' Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

screen hospKitchenInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg hospkitchen.png"
        if train_evidence3[2]:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'q' hovered tt.Action("Closet")
        else:
            hotspot(484, 104, 70, 230) action [Hide("backCarInv"), Jump("traincloset")] mouse 'ex' hovered tt.Action("Closet")
    add "status.png"
    add Text("{b}Kitchen{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch3.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun1.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

    imagebutton:
        xalign 1.0
        yalign 0.175
        idle "mapicon.png" at iconzoom
        action [Show("hospMapInv", transition=Dissolve(0.3))]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("train_evidence", transition=Dissolve(0.3))]

    imagebutton:
        xpos 20
        ypos 20
        idle "samchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSam")]
    imagebutton:
        xpos 70
        ypos 20
        idle "jennychibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvJenny")]
    imagebutton:
        xpos 70
        ypos 20
        idle "draculachibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvDracula")]
    imagebutton:
        xpos 70
        ypos 20
        idle "sidhibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvSid")]
    imagebutton:
        xpos 70
        ypos 20
        idle "freddychibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvFreddy")]
    imagebutton:
        xpos 70
        ypos 20
        idle "bertchibi.png" at chibizoom
        action [Hide("hospKitchenInv", transition = Dissolve(1.0)), Jump("hospInvBert")]
