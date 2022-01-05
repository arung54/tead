screen mansMapInv():
    modal True
    #TODO: Gate rooms for FT4
    #TODO: Create secret sesame FTE
    imagemap:
        ground "map2ui.png"
        hotspot(762, 310, 155, 174):
            action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("kitchenInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay3.png")
            unhovered Hide("mansPreview")
        hotspot(920, 311, 329, 175):
            action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("diningInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay1.png")
            unhovered Hide("mansPreview")
        hotspot(1090, 489, 160, 195):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("garageInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay2.png")
            unhovered Hide("mansPreview")
        hotspot(153, 471, 561, 69):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("hallwayInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay4.png")
            unhovered Hide("mansPreview")
        hotspot(153, 539, 77, 145):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("hallwayInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay4.png")
            unhovered Hide("mansPreview")
        hotspot(152, 310, 156, 157):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("bedroomJennInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay6.png")
            unhovered Hide("mansPreview")
        hotspot(307, 310, 83, 83):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("bedroomJennInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay6.png")
            unhovered Hide("mansPreview")
        hotspot(497, 310, 218, 158):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("bedroomInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay6.png")
            unhovered Hide("mansPreview")
        hotspot(234, 544, 225, 140):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("bedroomInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay6.png")
            unhovered Hide("mansPreview")
        hotspot(463, 543, 251, 141):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("masterBedroomInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay6.png")
            unhovered Hide("mansPreview")
        hotspot(393, 310, 101, 158):
                action [Hide("kitchenInv"), Hide("diningInv"), Hide("garageInv"), Hide("hallwayInv"), Hide("bedroomInv"), Hide("bedroomJennInv"), Hide("masterBedroomInv"), Hide("bathroomInv"), Show("bathroomInv", transition=Dissolve(0.3)), Hide("mansMapInv"), Hide("mansPreview")]
            hovered ShowTransient("mansPreview", img="mansMapoverlay5.png")
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
            image "ev2 shape.png" xcenter 800 yalign 0.1
            text "Stella was seemingly stabbed in the back. The wound is long in one direction but narrow in the other." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev2 wound.png" xcenter 800 yalign 0.1
            text "The blood on Stella's back has dried a bit. There's not a lot of blood for how damaging the wound seems, almost as if something was used to seal the wound afterwards." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev2 damp.png" xcenter 800 yalign 0.1
            text "A part of Stella's clothes was rather damp around the area she was stabbed in. However, this part wasn't stained, so it seems to have been water rather than blood." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev2 hand.png" xcenter 800 yalign 0.1
            text "Each of Stella's hands had a rectangular burn mark on the palm." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev2 wires.png" xcenter 800 yalign 0.1
            text "During the investigation, we found wires under the sink that entered through a hole in the bathroom wall." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev2 generator.png" xcenter 800 yalign 0.1
            text "There was a generator in Jenny's bedroom. We saw the generator in the garage earlier." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev2 rope.png" xcenter 800 yalign 0.1
            text "A rope was attached to the handle of the generator. The generator has wheels, so the rope can be used to easily pull it around." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev2 sheath.png" xcenter 800 yalign 0.1
            text "A sheath that Sam found during the party and used to cut the cake. As far as we know, the sheath remained in the kitchen or dining room for the entire party." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev2 location.png" xcenter 800 yalign 0.1
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
            hotspot(111, 522, 482, 168) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(273, 206, 169, 145) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(441, 205, 113, 84) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
            hotspot(556, 211, 145, 139) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'q' hovered tt.Action("Cupboards and Drawers")
        else:
            hotspot(111, 522, 482, 168) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(273, 206, 169, 145) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(441, 205, 113, 84) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
            hotspot(556, 211, 145, 139) action [Hide("kitchenInv"), Jump("mansCupboards")] mouse 'ex' hovered tt.Action("Cupboards and Drawers")
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
            hotspot(829, 524, 138, 27) action [Hide("diningInv"), Jump("mansSheath")] mouse 'q' hovered tt.Action("Knife and Sheath")
        else:
            hotspot(829, 524, 138, 27) action [Hide("diningInv"), Jump("mansSheath")] mouse 'ex' hovered tt.Action("Knife and Sheath")
        if mans_extra[3]:
            hotspot(794, 198, 62, 76) action [Hide("diningInv"), Jump("mansSydell")] mouse 'q' hovered tt.Action("Mr. Sydell")
        else:
            hotspot(794, 198, 62, 76) action [Hide("diningInv"), Jump("mansSydell")] mouse 'ex' hovered tt.Action("Mr. Sydell")

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

    imagebutton:
        xpos 20
        ypos 70
        idle "laurenchibi.png" at chibizoom
        action [Hide("diningInv"), Jump("mansLandF")]

    imagebutton:
        xpos 20
        ypos 120
        idle "freddychibi.png" at chibizoom
        action [Hide("diningInv"), Jump("mansLandF")]

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
    bi "In that case it wouldn't be relevant to the murder either."
    bi "But maybe someone found the sheath beforehand?"
    bi "I should keep that possibility in mind..."
    if not mans_evidence[7]:
        $mans_evidence[7] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Knife Sheath was added to evidence."
    if False not in mans_evidence[7:9]:
        bi "Hmm... I think that's everything to find here."
        bi "Not that I found much, mostly the sheath and talking to Dracula about stuff I already knew..."
    call screen diningInv

label mansDracula:
    scene bg mansiondining knife
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    show drac ind with dissolve
    d "Ah Bert. Are you here to discuss my ploy from earlier?"
    b "Your ploy?"
    d "I was hoping someone would admit to a crime that could be tied to this location."
    d "If so, they would probably be the murderer."
    bi "Oh, he's referring to the conversation we had earlier."
    bi "Back then, we concluded as a group the murderer this round is probably someone who's been in this house before."
    bi "This is the first time we're solving a murder with this information in mind, maybe I should remember it."
    if not mans_evidence[8]:
        $mans_evidence[8] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Location and the Murderer was added to evidence."
    b "Though Dracula, I'm curious..."
    b "You didn't think it would work so easily, right?"
    d "What do you mean?"
    b "Even if people were open to sharing their crimes..."
    b "Wouldn't the murderer be incentivized to lie if they could?"
    d "Well, I'd hope they'd be honest with me since I was honest about my crime."
    b "Honest?"
    d "Yes. Do you not believe I'm a vampire, Bert?"
    bi "This again..."
    bi "I don't really want to try and convince him that his \"crime\" is unbelievable..."
    bi "Maybe it's best if I just leave him for now."
    b "Uh... I guess I believe you..."
    b "Well, let me know if you find anything."
    d "You as well."
    hide drac with dissolve
    if False not in mans_evidence[7:9]:
        bi "Hmm... I think that's everything to find here."
        bi "Not that I found much, mostly the sheath and talking to Dracula about stuff I already knew..."
    call mansDone
    call screen diningInv

label mansLandF:
    scene bg mansiondining knife
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    show lauren ind:
        xcenter .25
    show frog sad:
        xcenter .75
    with dissolve
    b "Hey Lauren, hey Froggy."
    l "Hey Bert."
    b "Froggy doing okay?"
    l "He's a bit shaken up, you know, with the whole, you know..."
    l "...incident."
    f "Is Ms. Stella going to be okay?..."
    l "Probably not Freddy... but it's ok, we'll get through this."
    b "Is it okay if I ask Freddy something?"
    b "In private?"
    l "...fine, but it better not be about you-know-who."
    hide lauren with moveoutleft
    show frog sad:
        xcenter .75
        linear 0.15 xcenter .5
    b "Hey Freddy, I know you're not feeling the best, but can you do me a favor?"
    f "Y... yeah?"
    b "Can you tell me what you heard Dracula and Sam discuss again?"
    f "Y-yeah. Dracula said he uh... expire minted with some uh... words I don't understand."
    b "It was suffocation, fire, and electricity, right?"
    f "Yeah! Those were it."
    bi "Hmm... it seems like Stella died from a stab wound..."
    bi "...so it's unlikely any of those are related to Stella's death."
    bi "But it might be worth remembering this anyway."
    b "Okay, thanks Freddy. You're a real help!"
    f "Oh. Uh... you're welcome Mr. Bert!"
    hide frog with dissolve
    call screen diningInv

label mansSydell:
    scene bg mansiondining knife
    $mans_extra[3] = True
    $ statusnt("Dining Room", "bert", ch = 2, sun = 3)
    bi "Mr. Sydell's portrait..."
    bi "At this point, I doubt anyone will admit to knowing him."
    bi "Maybe if we catch the murderer and they're feeling nice, they'll tell us about him."
    bi "For now, I think that's our only lead for finding the mastermind..."
    call screen diningInv

screen garageInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansiongarage.png"
        if mans_extra[4]:
            hotspot(836, 191, 442, 414) action [Hide("garageInv"), Jump("mansGarage")] mouse 'q' hovered tt.Action("Missing Items")
        else:
            hotspot(836, 191, 442, 414) action [Hide("garageInv"), Jump("mansGarage")] mouse 'ex' hovered tt.Action("Missing Items")
        if mans_extra[5]:
            hotspot(214, 179, 563, 348) action [Hide("garageInv"), Jump("mansGarageDoor")] mouse 'q' hovered tt.Action("Garage Door")
        else:
            hotspot(214, 179, 563, 348) action [Hide("garageInv"), Jump("mansGarageDoor")] mouse 'ex' hovered tt.Action("Garage Door")

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
        idle "sidchibi.png" at chibizoom
        action [Hide("garageInv"), Jump("mansGarage")]

    imagebutton:
        xpos 20
        ypos 70
        idle "samchibi.png" at chibizoom
        action [Hide("garageInv"), Jump("mansSam")]


label mansSam:
    scene bg mansiongarage
    $ statusnt("Garage", "bert", ch = 2, sun = 3)
    show sam with dissolve
    b "Sam, you find anything yet?"
    s "No, everything I found Sid found first."
    s "You talk to him yet?"
    if mans_extra[4]:
        b "Yeah, I have."
        s "Then yeah, have nothing new to tell you, sorry."
        b "Fair enough, good luck with investigating more."
        s "You too."
    else:
        b "Nope, guess I'll talk to him now..."
        s "Alright, see you later."
        hide sam with dissolve
    hide sam with dissolve
    call screen garageInv

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
        ground "bg mansionhall.png"
        if mans_extra[0]:
            hotspot(444, 289, 109, 174) action [Hide("hallwayInv"), Jump("mansAppliances")] mouse 'q' hovered tt.Action("Microwave and Oven")
        else:
            hotspot(444, 289, 109, 174) action [Hide("hallwayInv"), Jump("mansAppliances")] mouse 'ex' hovered tt.Action("Microwave and Oven")
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
        ground "bg mansionbedroom1.png"
        if mans_extra[10]:
            hotspot(186, 410, 181, 222) action [Hide("bedroomInv"), Jump("mansGoAway")] mouse 'q' hovered tt.Action("Nightstand and Flower")
        else:
            hotspot(186, 410, 181, 222) action [Hide("bedroomInv"), Jump("mansGoAway")] mouse 'ex' hovered tt.Action("Nightstand and Flower")
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

label mansGoAway:
    scene bg mansionbedroom
    $ statusnt("Bedroom", "bert", ch = 2, sun = 3)
    if mans_extra[10]:
        bi "Most of the bedrooms seem to have nothing noteworthy in them."
        if mans_evidence[5]:
            bi "Except for Jenny's, that is..."
        call screen bedroomInv
    $mans_extra[10] = True
    bi "Hm... let me check this nightstand."
    bi "...Nope, nothing in here."
    bi "Nothing hidden in the vase either."
    if not mans_evidence[5]:
        bi "I guess to be thorough, I should check the other bedrooms?"
        scene black with dissolve
        scene bg mansionbedroom with dissolve
        $ statusnt("Bedroom", "bert", ch = 2, sun = 3)
        bi "..."
        bi "Nope, nothing in this bedroom either."
        bi "That just leave's Jenny's room..."
        scene black with dissolve
        scene bg mansionbedroom gen with dissolve
        $ statusnt("Bedroom", "bert", ch = 2, sun = 3)
        bi "...Huh?"
        call screen bedroomJennInv

screen bedroomJennInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionbedroom1gen.png"
        if mans_evidence[5]:
            hotspot(50, 538, 93, 95) action [Hide("bedroomJennInv"), Jump("mansGenerator")] mouse 'q' hovered tt.Action("Generator")
        else:
            hotspot(50, 538, 93, 95) action [Hide("bedroomJennInv"), Jump("mansGenerator")] mouse 'ex' hovered tt.Action("Generator")
    add "status.png"
    add Text("{b}Bedroom{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
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

label mansGenerator:
    scene bg mansionbedroom gen
    $ statusnt("Bedroom", "bert", ch = 2, sun = 3)
    if not mans_evidence[5]:
        bi "Huh, what's the generator doing in here?"
        bi "It was in the garage earlier, and as far as I know nothing in the house lost power..."
        bi "So someone must have moved it here for some other reason, right?"
        $mans_evidence[5] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Generator was added to evidence."
        bi "Also... what's up with this rope tied around the handle?"
        bi "..."
        bi "Oh, the generator has wheels."
        bi "So you can use the rope to tug the generator around more easily."
        bi "Hmm..."
        #bi "Though I wonder..."
        #bi "If someone was strong enough to lift the generator upstairs, why would they need the rope?"
        #bi "Hm... I'll have to think about this more."
        $mans_evidence[6] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Rope Attached to Generator was added to evidence."
        bi "I think that's the only interesting thing in this room."
        bi "Though, this is Jenny's room..."
        bi "I don't know if that will end up being important or not, but I should remember that too."
    else:
        bi "Someone moved the generator up here from the garage, but I'm not sure why."
        bi "And they tied a rope around it, maybe to make it easier to move around."
        bi "Hm..."
    call mansDone
    call screen bedroomJennInv

screen masterBedroomInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionmasterbedroom.png"
        if mans_extra[7]:
            hotspot(972, 409, 45, 88) action [Hide("masterBedroomInv"), Jump("mansFlower")] mouse 'q' hovered tt.Action("Flower")
        else:
            hotspot(972, 409, 45, 88) action [Hide("masterBedroomInv"), Jump("mansFlower")] mouse 'ex' hovered tt.Action("Flower")
        if mans_extra[8]:
            hotspot(916, 467, 173, 150) action [Hide("masterBedroomInv"), Jump("mansNightstand")] mouse 'q' hovered tt.Action("Nightstand")
        else:
            hotspot(916, 467, 173, 150) action [Hide("masterBedroomInv"), Jump("mansNightstand")] mouse 'ex' hovered tt.Action("Nightstand")
        if mans_extra[9]:
            hotspot(972, 409, 45, 88) action [Hide("masterBedroomInv"), Jump("mansDrawers")] mouse 'q' hovered tt.Action("Master Bathroom")
        else:
            hotspot(972, 409, 45, 88) action [Hide("masterBedroomInv"), Jump("mansDrawers")] mouse 'ex' hovered tt.Action("Master Bathroom")
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

    imagebutton:
        xpos 20
        ypos 20
        idle "catherinechibi.png" at chibizoom
        action [Hide("masterBedroomInv"), Jump("mansCath")]

label mansCath:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 3)
    show catherine happy with dissolve
    c "Hey Bert!"
    c "It feels so good to be reunited with Sesame after so long."
    b "...hasn't it been less than a day?"
    c "Yeah, it feels like ages ago since I lost saw Sesame!"
    c "How's the investigation going?"
    if len([e for e in mans_evidence]) > 4:
        b "Pretty good, I've already found a lot of evidence."
        c "Oh good! You're gonna solve this one just like the last one, right?"
        b "That's uh... a lot of pressure Catherine."
        c "Oh woops! Okay, I'll get out of your way."
    else:
        b "Hmm, honestly I haven't found too much yet."
        c "Oh no! Do you want help looking around here?"
        b "Yeah, that'd be nice."
        show catherine ind
        c "Oh... I didn't think you'd say yes."
        c "I was hoping to play with Sesame more..."
        b "..."
        b "Yeah, that's fine, I'll do it on my own."
        show catherine happy
        c "Yay! Thanks Bert."
    hide catherine with dissolve
    call screen masterBedroomInv

label mansFlower:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 3)
    bi "Is there anything in this vase?"
    bi "It'd be a convenient place to hide a long skinny \"stabby stick\"."
    bi "..."
    bi "Nope, just water in here."
    $mans_extra[7] = True
    if False not in mans_extra[7:9]:
        bi "Something tells me I'm not going to find anything in this room."
        bi "Maybe I should look elsewhere."
    call screen masterBedroomInv

label mansNightstand:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 3)
    bi "Huh, I wonder if anything's in the nightstand's drawer."
    bi "..."
    bi "It's empty, guess that makes sense."
    bi "Not like any of us have any spare clothes or anything to store."
    bi "And it'd be a bit too simple to try to hide a murder weapon in here..."
    $mans_extra[8] = True
    if False not in mans_extra[7:9]:
        bi "Something tells me I'm not going to find anything in this room."
        bi "Maybe I should look elsewhere."
    call screen masterBedroomInv

label mansDrawers:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 3)
    bi "Huh, I wonder if anything's hidden in the bathroom here?"
    bi "..."
    bi "Nope, nothing of interest here."
    bi "Doesn't even look like the toilet or tub have been used recently."
    bi "I guess it's not exactly very private..."
    $mans_extra[9] = True
    if False not in mans_extra[7:9]:
        bi "Something tells me I'm not going to find anything in this room."
        bi "Maybe I should look elsewhere."
    call screen masterBedroomInv

label mansCatherine:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 3)
    show catherine ind with dissolve
    c "Hey Bert! I'm looking around the master bedroom but it doesn't seem like anything's here."
    c "Oh, I have some spicy information for you though."
    b "Oh?"
    c "You remember how Dracula claimed he doesn't sleep?"
    b "Yeah?"
    c "Turns out he's lying! He actually sleeps, he just waits until people around him are sleeping."
    c "And then he wakes up earlier than we do."
    c "So if you don't wake up in the middle of the night, you can't tell if he was asleep or not!"
    c "But yesterday I woke up in the middle of night because Sesame was making noises..."
    c "And there was Dracula, sleeping on the floor!"
    b "Huh..."
    b "Dracula never left the party though, so it's not likely he committed the murder..."
    b "So... is this useful information?"
    c "I don't know, I just thought it was cute!"
    ses "Mrrr!"
    c "Sesame agrees, even a handsome old man needs his beauty sleep!"
    b "Uh... thanks Catherine... I guess..."
    hide catherine with dissolve
    call screen masterBedroomInv

screen bathroomInv():
    default tt = Tooltip("")

    imagemap:
        ground "bg mansionbr.png"
        if mans_evidence[4]:
            hotspot(325, 523, 155, 194) action [Hide("bathroomInv"), Jump("mansSink")] mouse 'q' hovered tt.Action("Under the Sink")
        else:
            hotspot(325, 523, 155, 194) action [Hide("bathroomInv"), Jump("mansSink")] mouse 'ex' hovered tt.Action("Under the Sink")
        if mans_evidence[3]:
            hotspot(269, 425, 84, 59) action [Hide("bathroomInv"), Jump("mansHands")] mouse 'q' hovered tt.Action("Stella's Hands")
        else:
            hotspot(269, 425, 84, 59) action [Hide("bathroomInv"), Jump("mansHands")] mouse 'ex' hovered tt.Action("Stella's Hands")
        if mans_evidence[0]:
            hotspot(418, 457, 106, 69) action [Hide("bathroomInv"), Jump("mansStella")] mouse 'q' hovered tt.Action("Stab Wound")
        else:
            hotspot(418, 457, 106, 69) action [Hide("bathroomInv"), Jump("mansStella")] mouse 'ex' hovered tt.Action("Stab Wound")
        if mans_extra[6]:
            hotspot(756, 392, 523, 326) action [Hide("bathroomInv"), Jump("mansTub")] mouse 'q' hovered tt.Action("Tub")
        else:
            hotspot(756, 392, 523, 326) action [Hide("bathroomInv"), Jump("mansTub")] mouse 'ex' hovered tt.Action("Tub")

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
        action [Hide("kitchenInv"), Jump("mansShahar")]

    imagebutton:
        xpos 20
        ypos 70
        idle "jennychibi.png" at chibizoom
        action [Hide("kitchenInv"), Jump("mansJenny")]

label mansSink:
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    if not mans_evidence[4]:
        bi "Hm... I wonder if Stella made any progress stealing the sink handle before she died."
        bi "I doubt it'll lead to anything, but might as well look under there."
        bi "...Huh?"
    show ev2 wires with dissolve:
        ycenter .5
        xcenter .5
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
    if False not in mans_evidence[0:5]:
        bi "Hmm... I found a lot in the bathroom, but I think that's everything."
        bi "Though this has brought up more questions than answers..."
    call mansDone
    call screen bathroomInv

label mansHands:
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    if not mans_evidence[3]:
        show shahar mad with dissolve:
            xcenter .75
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
    show ev2 hand with dissolve:
        xcenter .5
        ycenter .5
    bi "These look like burns on her palms..."
    b "Did the killer burn Stella before or after stabbing her?"
    b "Also, they're shaped like rectangles... I wonder why..."
    if not mans_evidence[3]:
        $mans_evidence[3] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Burns on Stella's Hands was added to evidence."
    hide ev2 hand with dissolve
    if False not in mans_evidence[0:5]:
        bi "Hmm... I found a lot in the bathroom, but I think that's everything."
        bi "Though this has brought up more questions than answers..."
    call mansDone
    call screen bathroomInv

label mansShahar:
    if not mans_evidence[3]:
        jump mansHands
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    show shahar mad with dissolve
    h "I can't believe nary a soul would kill Stella."
    h "She fouled no man, her only fault was a liver of gold."
    b "...and the numerous people who worked under her that were probably exploited."
    h "What?"
    b "Nothing..."
    show shahar mad with dissolve
    call screen bathroomInv

label mansTub:
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    bi "As much as I would love to take a relaxing bath and just forget everything happening..."
    bi "Now's not the time."
    $mans_extra[6] = True
    call screen bathroomInv

label mansStella:
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    if not mans_evidence[0]:
        bi "I... I don't want to look at the stab wound too closely, but I probably should."
        bi "Here goes..."
        bi "As expected, it's roughly the shape of a knife, long and thin."
        bi "Not too surprising, but I should keep that in mind."
        $mans_evidence[0] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Shape of the Wound was added to evidence."
        show jenny ind with dissolve:
            xcenter .75
        j "Wait... when Dan was stabbed, the wound was pretty wet, and there was much more blood..."
        j "If it's dry, she's probably wasn't stabbed recently."
        j "Also..."
        j "If there's not that much blood here, does that mean Stella was able to stem the bleeding?"
        show jenny happy
        j "That would be pretty impressive, wow. Right Bert?"
        b "Impressive but... not something to be happy about, necessarily."
        show jenny ind
        j "Oh. Right. Dead body."
        $mans_evidence[1] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Blood from the Wound was added to evidence."
        b "Well uh, got any more useful observations here?"
        j "Bert, feel the back of Stella's suit around the wound."
        j "Not where the blood has seeped into her suit, just outside that area."
        b "Uh... okay..."
        b "..."
        b "Huh."
        b "It's... pretty damp."
        j "Right. But her suit's not stained where you just felt it!"
        j "So something else must have made it wet. Maybe water?"
        b "Hm... why would there be water on Stella's back..."
        $mans_evidence[2] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Blood from the Wound was added to evidence."
        b "Wow Jenny, you figured out a lot."
        j "Hey, you helped us figure out Kaiser's death, we gotta all chip in!"
        bi "Jenny's been so helpful... a killer couldn't be this helpful, right?"
        bi "No... maybe she's a killer masking her true intentions..."
        bi "As much as I want to trust her, I gotta proceed with caution..."
        hide jenny with dissolve
    else:
        bi "The stab wound is long and thin, like a knife wound would be."
        bi "Also, from what Jenny told me..."
        bi "It's likely the wound was formed a while ago, and something stemmed the bleeding."
        bi "Lastly, there's what seems like water on her back but we're not sure why."
    if False not in mans_evidence[0:5]:
        bi "Hmm... I found a lot in the bathroom, but I think that's everything."
        bi "Though this has brought up more questions than answers..."
    call mansDone
    call screen bathroomInv

label mansJenny:
    scene bg mansionbr
    $ statusnt("Bathroom", "bert", ch = 2, sun = 3)
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    show jenny ind with dissolve
    if not mans_evidence[0]:
        bi "She's staring intently at Stella..."
        bi "Maybe I should see what she's looking at?"
    else:
        j "Bert... do you suspect me?"
        j "You trust me after all the things I pointed out right."
        b "Jenny I..."
        b "You, Sam, and Shahar were the only ones to leave the party."
        b "I want to trust you but..."
        j "..."
        show jenny happy with dissolve
        j "Don't worry, I get it."
        j "Things look pretty bad for me right now, huh?"
        j "I trust you to find the truth, and then you'll know it wasn't me."
        j "Go get em, Bert!"
        bi "...Why do I feel like I'm talking to a cheerleader rather than a prime suspect?"
    hide jenny with dissolve
    call screen bathroomInv

label mansDone:
    if False not in mans_evidence:
        bi "Actually, I think I've found most of the major pieces of evidence..."
        bi "At least, enough to start discussing with others."
        bi "Let's go gather everyone."
        jump trial2a
    return
