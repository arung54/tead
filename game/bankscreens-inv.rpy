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
            textbutton "Gun and Shell" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[3]:
            textbutton "Torn Elastic Belt" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[4]:
            textbutton "Shells in the Lobby" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[5]:
            textbutton "Freddy's Account" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[6]:
            textbutton "Lauren's Account" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[7]:
            textbutton "Jenny's Account" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[8]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[9]:
            textbutton "Sign in the Safe" style "button_text" action SetVariable("currEvidence", 9)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[10]:
            textbutton "Ammunition" style "button_text" action SetVariable("currEvidence", 10)
        else:
            textbutton "-" style "button_text"

        if bank_evidence[11]:
            textbutton "Uniforms in the Lockers" style "button_text" action SetVariable("currEvidence", 11)
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
            text "The gun we found in the break room holds up to six bullets at once, and was empty when we found Sam's body. There was also a single bullet shell lying next to Sam." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev3 rules.png" xcenter 800 yalign 0.1
            text "Part of an elastic belt was found attached to ___ in the break room. We don't know where the rest of the belt is." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "There were six shells on the ground in the lobby, near the door to the hallway." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Freddy woke up to the sound of gunshots. He saw me get down to the floor, then saw the uniformed person leave, and me chase after them." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Lauren was searching in the office, left, and was walking towards the guard room. The safe was closed when she passed by, and she didn't see anyone in the guard room, so she started looking for us. She didn't hear me yell, but she ended up finding me and Jenny because she heard us talking in the break room." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev3 cleaning.png" xcenter 800 yalign 0.1
            text "Jenny had just finished taking a shower in the guard room. She walked out and saw the safe was open, then heard me yelling. She walked directly to the break room, passing the hallway couch on the way." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Sid woke up from sleeping on the couch. He saw the green light and walked towards the safe, but heard someone yell from the break room and made his way towards us instead." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Even when the combination is entered, if it's shut, the safe door can't be opened from the inside." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Inside the safe we found bullets that seem to fit in the gun. The bullets come in sets of six, and are attached by a piece of metal so that they can all be reloaded at once. However, the piece of metal prevents you from separating individual bullets." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 11:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "All but one locker in the guard room had a uniform in it." xcenter 800 yanchor 0.0 ypos 330

screen breakInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg bankbreak2.png"
        if bank_extra[0]:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankCorpse")] mouse 'q' hovered tt.Action("Sam's Corpse")
        else:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankCorpse")] mouse 'ex' hovered tt.Action("Sam's Corpse")
        if bank_evidence[1]:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankDoor")] mouse 'q' hovered tt.Action("Break Room Door")
        else:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankDoor")] mouse 'ex' hovered tt.Action("Break Room Door")
        if bank_evidence[2]:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankGun")] mouse 'q' hovered tt.Action("Gun")
        else:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankGun")] mouse 'ex' hovered tt.Action("Gun")
        if bank_evidence[3]:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankBelt")] mouse 'q' hovered tt.Action("???")
        else:
            hotspot(0, 0, 1, 1) action [Hide("breakInv"), Jump("bankBelt")] mouse 'ex' hovered tt.Action("Torn Elastic Belt")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Bank Lobby{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

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

label bankCorpse:
    scene bg bankbreak2
    if bank_extra[0]:
        bi "Sam's corpse..."
        bi "There's a bullet hole in the temple, consistent with an attempt at suicide."
        bi "But is that really what happened?"
    else:
        $ bank_extra[0] = True
        bi "Sam..."
        bi "Just when you were recovering, just when we had made so much progress together."
        bi "Did you really collapse in that moment?"
        bi "I have a hard time believing that."
        bi "Either something happened that made Sam's mind change in an instant..."
        bi "Or somebody else here is hiding something."
        bi "If I want to survive I need to approach this all as objectively as possible."
        bi "And really, the rational thing is to hope it was a suicide."
        bi "Then no one else has to die."
        bi "But somehow..."
        bi "I find myself wishing it wasn't."
        bi "At least when the murders happened, it was someone trying to survive."
        bi "So if someone gave up like that, without even trying..."
        bi "Even if one less person dies, in a weird way it's sadder."
        bi "..."
        bi "But again, emotions don't really matter right now."
        bi "Let me inspect this corpse in more detail."
        bi "The obvious detail is the bullet hole in the head..."
        bi "...And besides that, I don't really see anything."
        bi "It does look like what I'd imagine a suicide should look like..."
        bi "..."
        bi "Yeah, I've looked over this body three or four times now."
        bi "Maybe this is just a murder where the body doesn't have the answers."
        if False not in bank_evidence[1:3] and not bank_extra[0]:
            bi "Okay, unless some low-quality office snacks were the murder weapon..."
            bi "Pretty sure that's everything important in this room."
            bi "Let's go find the others and start asking them some questions..."
    call screen breakInv

label bankDoor:
    scene bg bankbreak2
    if bank_evidence[1]:
        bi "The door to the break room."
        bi "It's been open this entire time."
    else:
        bi "Hm, nothing is particularly noticeable about the door."
        bi "Though now that I think about it..."
        bi "This door's stayed open the entire time since I ran in here at first."
        bi "Is that important?"
        bi "When I first ran into the hallway, I saw the door close."
        bi "It feels like I should be able to conclude something from that..."
        $ bank_evidence[1] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Break Room Door was added to evidence."
        if False not in bank_evidence[1:3] and not bank_extra[0]:
            bi "Okay, unless some low-quality office snacks were the murder weapon..."
            bi "Pretty sure that's everything important in this room."
            bi "Let's go find the others and start asking them some questions..."
    call screen breakInv

label bankGun:
    scene bg bankbreak2
    if bank_evidence[2]:
        bi "The gun that presumably Sam used to commit suicide."
        bi "It holds six bullets at once, and is empty right now..."
        bi "There's also a shell on the ground next to Sam's head, that matches the gun."
    else:
        bi "The gun..."
        bi "If only we had access to the stuff real detectives have."
        bi "We could look for fingerprints on this thing."
        bi "Anyway... I've never held a gun before."
        bi "I should make sure to point it away from me while I'm looking at it..."
        bi "Hm, how do I open the..."
        bi "The chamber?"
        bi "Or is the tube the bullet fires from the chamber?"
        bi "The... the thing that holds the bullets. How do I open that?"
        blank "Click."
        bi "Oh. That button releases it."
        bi "Hm, the gun appears to hold six bullets."
        bi "It's currently empty. Probably still was a good idea to point it away..."
        bi "Where did this even come from? Was this here the whole time and none of us found it?"
        bi "...Oh?"
        bi "There's a burnt shell on the ground, near-ish Sam's head."
        bi "Let me see..."
        bi "Yeah, the shell seems like it matches the size of the slots for the bullets."
        bi "So I think we can conclude it came from the gun..."
        bi "All this being said, I don't really know if the type of gun or shell really matters..."
        bi "Most guns will kill you if you point them in the right place, right?"
        $ bank_evidence[2] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Gun and Shell was added to evidence."
        if False not in bank_evidence[1:3] and not bank_extra[0]:
            bi "Okay, unless some low-quality office snacks were the murder weapon..."
            bi "Pretty sure that's everything important in this room."
            bi "Let's go find the others and start asking them some questions..."
    call screen breakInv

screen lobbyInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg banklobby1.png"
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
    add "ch4.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "sun4.png" xpos 1165 ypos 55 xanchor 0 yanchor 0
    add "bertchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0

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
        idle "freddychibi.png" at chibizoom
        action [Hide("lobbyInv", transition = Dissolve(1.0)), Jump("bankInvFreddy")]

    imagebutton:
        xpos 20
        ypos 70
        idle "laurenchibi.png" at chibizoom
        action [Hide("lobbyInv", transition = Dissolve(1.0)), Jump("bankInvLauren")]

    imagebutton:
        xpos 20
        ypos 120
        idle "jennychibi.png" at chibizoom
        action [Hide("lobbyInv", transition = Dissolve(1.0)), Jump("bankInvJenny")]

label dummy2:
    scene bg banklobby1
    $ statusnt("Security", "lauren", ch = 3, sun = 1)
    show sam with dissolve
    lf "Notice anything Sam?"
    s "...Not really..."
    li "Talkative as always."
    hide sam with dissolve
    call screen securityInv

label dummy3:
    scene bg banklobby1
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
    call screen breakInv


label bankDone:
    if False not in bank_evidence[1:]:
        bi "Okay, I think I've searched this place pretty thoroughly."
        bi "I don't feel like we have much to go off, but I've felt that way every time."
        bi "What's one more miracle at this point?"
        bi "Let's go to the lobby and discuss with the others."
        jump trial4a
    return
