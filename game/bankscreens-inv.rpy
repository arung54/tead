screen bankMapInv():
    modal True
    if not bank_evidence[8]:
        imagemap:
            ground "map4ui.png"
            hotspot(460, 273, 108, 78):
                action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("breakInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
                unhovered Hide("mapPreview")
            hotspot(460, 273, 108, 78):
                action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Hide("bankMapInv"), Hide("mapPreview"), Jump("bankSid")]
                hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
                unhovered Hide("mapPreview")
    else:
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
            text "Sid woke up from sleeping on the couch. He saw the green light, so he walked towards the safe door and saw it was open. However, he heard someone yell from this side of the bank and made his way towards us instead." xcenter 800 yanchor 0.0 ypos 330

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
        if bank_extra[1]:
            action [Show("bankMapInv", transition=Dissolve(0.3))]
        else:
            action [Hide("breakInv"), Jump("bankStuck")]

    imagebutton:
        xalign 1.0
        yalign 0.275
        idle "evidenceicon.png" at iconzoom
        action [Show("bank_evidence", transition=Dissolve(0.3))]

label bankCorpse:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
            $bank_extra[1] = True
    call screen breakInv

label bankDoor:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
            $bank_extra[1] = True
    call screen breakInv

label bankGun:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
            $bank_extra[1] = True
    call screen breakInv

label bankBelt:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
    if bank_evidence[3]:
        bi "An elastic belt tied to the ___."
        bi "It probably came from a guard uniform."
        bi "But it's torn and this is just one piece... where is the rest?"
    else:
        bi "What is this?"
        bi "It looks like a belt of some sort."
        bi "It's been tied pretty firmly around the ___."
        bi "Hm... but the end of it has been torn off."
        bi "Where'd the other end go?"
        bi "I briefly looked around the room, but I couldn't find the rest of the belt."
        bi "This definitely wasn't here until now, it has to be important..."
        $ bank_evidence[3] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Torn Elastic Belt was added to evidence."
        if False not in bank_evidence[1:3] and not bank_extra[0]:
            bi "Okay, unless some low-quality office snacks were the murder weapon..."
            bi "Pretty sure that's everything important in this room."
            bi "Let's go find the others and start asking them some questions..."
            $bank_extra[1] = True
    call screen breakInv

label bankStuck:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
    bi "This is the first time we might have found the body before the killer had a chance to manipulate the scene."
    bi "I should make sure I look at everything before leaving."
    bi "There's a chance someone will come back and try to hide something while I'm gone."
    call screen breakInv

screen hall1Inv():
    default tt = Tooltip("")
    imagemap:
        ground "bg bankhall1b.png"
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Bank Hallway{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
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


label bankSid:
    scene bg bankbreak2
    statusnt("Bank Hallway", "bert", ch=4, sun=4)
    showchibint("sid")
    with dissolve
    show sid ind with dissolve
    i "Oh, hey Bert."
    i "I thought I heard someone yell over here... what happened?"
    b "Oh... Sam is dead."
    i "What?"
    bi "I told Sid about what happened..."
    bi "This was my third time relaying the sequence of events."
    bi "At this point I could probably give a TEAD Talk on it."
    bi "I mean, TED Talk."
    i "I'm gunna take a look..."
    hide sid with moveoutleft
    show sid ind with moveinright
    i "Jeez, Sam really is dead..."
    i "It looks like it was... um..."
    i "Self-inflicted."
    bi "We were kind of numb to murder at this point, but the word \"suicide\" still beared some gravity with it."
    b "Yeah, that's what it seems like."
    b "But I still want to investigate."
    b "After all, if we settled on our first instincts, we'd have accused you for, well..."
    i "..."
    bi "Hm, maybe that was a sore spot."
    b "...You okay Sid?"
    i "Yeah, it's just weird."
    i "You ever think you hate somebody?"
    i "And then something happens and you realize you didn't really hate them."
    i "You just... didn't really mesh that well."
    i "But you can't go back and undo the way you treated them."
    bi "Sid says this as if this could possibly be referring to anyone but Sam."
    bi "I guess the two did clash quite a bit."
    b "...I can't say I've had that happen to me, no."
    i "Oh..."
    b "But Sid... I think we can at least honor Sam's death by trying to figure out the truth behind it."
    i "I... I guess."
    b "So I need to know..."
    b "What were you up to before you came here?"
    i "Do... do you think I did it?"
    show sid mad
    i "What the hell Bert? I just opened up to you about my feelings!"
    i "And now you're accusing me?"
    b "I never accused you!"
    bi "This would be so much easier with someone here to help me..."
    bi "But again, the only person I can really trust at this point is Freddy."
    b "Sid... I just need all the facts."
    b "And if you think about it, it'd be more suspicious if you didn't tell me what you were up to."
    i "Uh."
    i "Okay, fine, I'll tell you, but I still don't forgive you for accusing me!"
    bi "I never accused you..."
    bi "Oh, what's the point."
    show sid ind
    i "Anyway, um, I was sleeping on the couch."
    i "I woke up, I think because I had a bad dream."
    i "When I looked around, I noticed the red light in the hallway had turned green."
    bi "!"
    i "I thought maybe someone had opened the safe."
    i "So I walked towards it to check it out. The door was open, so I was going to go in."
    i "But then I heard someone yell over here."
    i "So I decided to come here instead in case something happened."
    b "Hm... okay, which way did you walk here from the safe?"
    i "Uh... the faster way. Like, past the office."
    i "I'm not that stupid Bert... I wouldn't take the long way if something had happened."
    b "Gotcha. So woke up, saw the green light was on, walked to the safe, then came here."
    b "And you didn't check out the safe at all?"
    i "That's right."
    $ bank_evidence[8] = True
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    blank "Sid's account was added to evidence."
    b "Okay, thanks Sid, that's helpful to know."
    b "Interesting that the safe is open..."
    i "Do you need help investigating it?"
    i "I really wanna look inside!"
    b "Actually... I need someone I can trust to keep an eye on Lauren and Jenny."
    b "If it wasn't suicide, then they're both suspects."
    bi "What I was omitting here is that Sid was also a suspect."
    bi "Have to placate him a bit if I want him to play along."
    b "Can I trust you to do that Sid?"
    i "Aw, boring..."
    i "Okay, but if you find money in the safe I'm getting half... no, two thirds of it!"
    b "I... sure, you know what Sid, if there's money in the safe you can have all of it."
    i "Score!"
    hide sid with dissolve
    $ showchibint()
    bi "One thing is weird to me about Sid's story..."
    bi "Sid came because he heard someone yell?"
    bi "Freddy and I may have yelled due to the events that happened."
    bi "And Jenny and Lauren were shocked when they saw Sam."
    bi "So maybe he did hear someone yell."
    bi "But that would have been a while ago."
    bi "Did I really finish searching the break room in the time Sid took to walk over here?"
    bi "Anyway, now I know the safe is open. I should probably investigate there at some point."
    bi "Besides that, I still need to interrogate Jenny and Lauren..."
    bi "There's nothing in this hallway that seems interesting, so I should move on."
    call screen hall1Inv with dissolve

screen lobbyInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg banklobby.png"
        if bank_evidence[1]:
            hotspot(0, 0, 1, 1) action [Hide("lobbyInv"), Jump("securityComputer")] mouse 'q' hovered tt.Action("Computer")
        else:
            hotspot(0, 0, 1, 1) action [Hide("lobbyInv"), Jump("securityComputer")] mouse 'ex' hovered tt.Action("Computer")
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

    imagebutton:
        xpos 20
        ypos 170
        idle "sidchibi.png" at chibizoom
        action [Hide("lobbyInv", transition = Dissolve(1.0)), Jump("bankSid2")]

label bankInvFreddy:
    scene bg bankbreak2
    statusnt("Bank Lobby", "bert", ch=4, sun=4)
    show frog sad with dissolve
    if bank_evidence[5]:
        f "...*sniff*"
        f "Bert... *sniff* when can I go home?..."
        b "We're trying our hardest Freddy."
        b "You can help us out by being real strong!"
        f "*sniff* Okay..."
        bi "Freddy's pretty shaken up..."
        bi "I think it's best not to ask him to recall the shooting."
        hide frog with dissolve
    else:
        bi "You know... now that I think about it..."
        bi "No one else besides Freddy saw the uniformed person."
        bi "So I should probably ask him what he remembers."
        b "Hey Freddy..."
        b "I know it wasn't very fun, but can you tell me what you remember about waking up in here earlier?"
        f "Oh..."
        f "Do I have to?"
        f "It was so scary... I just want to go back to sleep."
        b "Freddy, it'll help us out a lot if you can."
        b "And if you help us... uh..."
        bi "Let's see, what would I want if I was a kid..."
        b "I'll buy you the biggest frog toy ever once we get home!"
        show frog ind
        f "B-biggest?"
        f "But... I already have one that's six feet tall and fifty pounds."
        bi "..."
        bi "Maybe I shouldn't have said biggest."
        b "Well... I'll find an even bigger one!"
        f "Even bigger?"
        f "No way..."
        f "Okay, so um..."
        f "I woke up and heard like, BANG BANG BANG."
        f "And my ears really hurt..."
        show frog sad
        f "And... *sniff* I was scared."
        bi "He's starting to tear up..."
        bi "I can feel Lauren glaring at me right now, but this could be important..."
        b "C'mon Freddy, what else? You're a strong kid!"
        bi "Really? That's what I say? It's so generic..."
        f "And... and you fell to the floor and I thought you were hurt..."
        f "Are you okay, Mr. Bert?"
        b "Oh yeah, I was just trying to hide."
        f "Oh... okay."
        f "And then *sniff* I saw the person who made the BANG BANG BANG."
        f "And then they ran away..."
        f "And then... you chased after them *sniff*."
        f "And I was alone and I was scared..."
        f "And..."
        f "I started crying... *sniff*."
        show frog sad:
            xcenter .5
            linear 0.15 xcenter .25
        show lauren ind with moveinright:
            xcenter .75
        l "Freddy, are you okay?"
        l "Is Bert being mean to you?"
        b "Oh, I just was asking Freddy to help the adults out!"
        l "Is that true Freddy?"
        f "Y-yeah..."
        b "You've been a real help Freddy!"
        b "I think I'm done with questioning him, Lauren..."
        l "Good, poor kid's been through enough."
        hide frog
        hide lauren
        with dissolve
        bi "Well, it's nothing I didn't know, but..."
        bi "Knowing Freddy saw everything that went down in here might be useful later."     
        $ bank_evidence[5] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Freddy's Account was added to evidence."
        if False not in bank_evidence[4:7]:
            bi "Okay, I've interrogated everyone."
            bi "I was in this room before the uniformed person ran in here..."
            bi "So besides the shells, I don't think there's too much of importance here."
            call bankDone from _call_bankDone_1
    call screen breakInv

label bankDone:
    if False not in bank_evidence[1:]:
        bi "Okay, I think I've searched this place pretty thoroughly."
        bi "I don't feel like we have much to go off, but I've felt that way every time."
        bi "What's one more miracle at this point?"
        bi "Let's go to the lobby and discuss with the others."
        jump trial4a
    return
