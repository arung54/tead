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
                action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("officeInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
                unhovered Hide("mapPreview")
            hotspot(460, 273, 108, 78):
                action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("lockerInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
                hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
                unhovered Hide("mapPreview")
            hotspot(460, 273, 108, 78):
                if not bank_extra[9]:
                    action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Hide("bankMapInv"), Hide("mapPreview"), Jump("safeFirst")]
                    hovered ShowTransient("mapPreview", img="bankmapoverlay8.png")
                    unhovered Hide("mapPreview")
                else:
                    action [Hide("lobbyInv"), Hide("breakInv"), Hide("hall1Inv"), Hide("hall2inv"), Hide("safeInv"), Hide("officeInv"), Hide("lockerInv"), Show("safeInv", transition=Dissolve(0.3)), Hide("bankMapInv"), Hide("mapPreview")]
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
            textbutton "The Safe Door" style "button_text" action SetVariable("currEvidence", 9)
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
            text "After the shooting, I chased the uniformed person into the hallway. It was quiet enough in the hallway that I both saw and heard the break room door close. I yanked the door open and found the dead body in the uniform." xcenter 800 yanchor 0.0 ypos 330

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
            text "There were six shells on the ground in the lobby, near the door to the hallway. They match the shell found by Sam's body." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Freddy woke up to the sound of gunshots. He saw me get down to the floor, then saw the uniformed person leave, and me chase after them." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "Lauren was searching in the office, left, and was trying to find people. The safe was closed when she passed by, and she didn't see anyone in the locker room. She walked towards the lobby, passing the couch, and ended up finding me and Jenny because she heard us talking in the break room." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev3 cleaning.png" xcenter 800 yalign 0.1
            text "Jenny had just finished taking a shower in the locker room. She walked out and saw the lights had turned green and the safe was open, then heard me yelling. She walked directly to the break room, passing Sid sleeping on the couch on the way." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Sid woke up from sleeping on the couch. He saw the green lights, so he walked towards the safe door and saw it was open. However, he heard someone yell from this side of the bank and made his way towards us instead." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Even when the combination is entered, if it's shut, the safe door can't be opened from the inside. The door opens and closes electronically, and opens up to a ninety degree angle." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Inside the safe we found bullets that seem to fit in the gun. The bullets come in sets of six, and are attached by a piece of metal so that they can all be reloaded at once. However, the piece of metal prevents you from separating individual bullets." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 11:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "Originally, each locker had one uniform it. When I investigated the locker room after Sam's death, only one of those uniforms was missing. " xcenter 800 yanchor 0.0 ypos 330

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
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
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
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    $ showchibint("sid")
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
            hotspot(0, 0, 1, 1) action [Hide("lobbyInv"), Jump("bankShells")] mouse 'q' hovered tt.Action("Bullet Shells")
        else:
            hotspot(0, 0, 1, 1) action [Hide("lobbyInv"), Jump("bankShells")] mouse 'ex' hovered tt.Action("Bullet Shells")
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

label bankShells:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    if bank_evidence[4]:
        b "There are six bullet shells on the floor by the door to the hallway."
        b "This is where the person in the uniform was standing, and they match the shell I found near Sam..."
        b "So they probably were from when Freddy and I were shot at."
    else:
        b "Are these..."
        show jenny ind with dissolve
        j "Find something Bert?"
        b "Yeah, these look like bullet shells..."
        j "Oh... well, you did say you were shot at, right?"
        b "Yeah, and the person in the uniform was standing about here when they shot at us..."
        j "So this is probably the \"leftovers\" from that shooting."
        b "I guess so..."
        bi "I picked one up and took a closer look."
        b "It looks like one that was near Sam's body."
        j "Hm... I mean, that makes sense if Sam was the one that shot at you."
        j "Then the same gun and bullets would have been used for both shootings."
        b "That's one possibility, but I don't know if it's the only explanation."
        j "What other explanations are there?"
        b "I'm not sure yet..."
        j "Hm... okay, Jenny brainstorm time!"
        hide jenny with moveoutleft
        bi "Jenny went and sat down with a serious look on her face..."
        bi "It'd be nice if she solved the case for us, but I won't count on it."
        bi "Anyway..."
        bi "There are six shells on the floor here."
        bi "The gun I found near Sam could hold six bullets..."
        bi "Did the shooter run away because they had to reload?"
        $ bank_evidence[4] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Shells in the Lobby was added to evidence."
        if False not in bank_evidence[4:7]:
            bi "Okay, I've interrogated everyone."
            bi "I was in this room before the uniformed person ran in here..."
            bi "So besides the shells, I don't think there's too much of importance here."
            call bankDone from _call_bankDone_1
    call screen breakInv

label bankInvFreddy:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    with dissolve
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
            call bankDone from _call_bankDone_2
    call screen breakInv

label bankInvLauren:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    with dissolve
    show lauren ind with dissolve
    if bank_evidence[6]:
        l "You're done investigating already?"
        b "Oh, no, not yet..."
        b "Just wanted to confirm what you told me earlier."
        b "You were searching in the office, then you finished and went looking for people."
        b "You walked past the safe, which was still closed, and checked the locker room."
        b "Then you walked past the couch towards the lobby, and heard us talking."
        l "And that's when I found you guys and saw the body, yup."
        l "Your memory's good Bert... I guess that's why you're doing the investigation."
        bi "Well... that and no one else above the age of ten could be trusted."
        hide lauren with dissolve
    else:
        b "Hey Lauren."
        l "Hey Bert."
        b "I wanted to ask you what you were up to since I last saw you."
        l "You mean... in the break room?"
        b "No, before that..."
        b "When you left to go search, Jenny went to go take a shower."
        b "From then, until you ran into Jenny and I in the break room."
        l "Oh, right."
        l "Well, I was searching in the director's office..."
        l "Just trying to find anything that could be helpful, really."
        bi "I guess Lauren doesn't know how extensively Sam searched that room."
        bi "I won't belittle her efforts by telling her."
        l "After some time I gave up and decided to look for people."
        l "So I went to the locker room since I knew Jenny might be in there."
        b "Was the safe open when you walked by?"
        l "No, it wasn't open."
        b "Hm... okay."
        l "Anyway, I didn't find anyone in the locker room."
        l "I also knew Sid liked napping on the couch in the hall, so I checked it out."
        l "But he wasn't there."
        l "So I figured everyone had gathered on this side of the building."
        l "I made my way over here, then heard you and Jenny talking in the break room."
        l "And well, you know what happened from there."
        b "Hm, okay. Let me recap to make sure I got this right."
        l "You were in the office, walked to the locker room, didn't find anyone, then came here."
        b "The safe was closed when you passed, and Sid wasn't on the couch when you looked."
        l "Yup, that's right."
        $ bank_evidence[6] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Lauren's Account was added to evidence."
        b "Alright, thanks Lauren."
        l "No problem. I'm going to go back to making sure Freddy's ok..."
        hide lauren with dissolve
        bi "Hm... something strikes me as odd about what Lauren told me, but I can't quite tell what..."
        if False not in bank_evidence[4:7]:
            bi "Okay, I've interrogated everyone."
            bi "I was in this room before the uniformed person ran in here..."
            bi "So besides the shells, I don't think there's too much of importance here."
            call bankDone from _call_bankDone_3
    call screen breakInv

label bankInvJenny:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    with dissolve
    show jenny happy with dissolve
    if bank_evidence[7]:
        j "Heya Bert!"
        j "I mean, uh, sheriff!"
        b "Hey Jenny, just want to make sure I remember your story correctly."
        b "You left the locker room, saw the safe was open, were going to wake up Sid..."
        b "Then you heard me yell and came to the break room."
        j "Yessir!"
        bi "I don't know if I'll get much more out of her while she's in \"deputy mode\"..."
        hide jenny with dissolve
    else:
        j "Bert! Your deputy is here!"
        j "Status update! I've been keeping lookout sir!"
        b "...What?"
        j "Teehee, I was thinking, well, you're kind of like our sheriff."
        j "So I was thinking like... well, I'm your deputy."
        j "And that means I should be speaking to you like a deputy would!"
        b "I... I'm flattered, I think?"
        b "Anyway, I wanted to ask what you were up to before we met in the break room."
        j "Starting from when?"
        b "Uh, I guess from when you were with the rest of us and then went to the locker room."
        show jenny ind
        j "Bert! You want to know what I was doing in the locker room?"
        b "..."
        show jenny happy
        j "Just pulling your leg!"
        j "Hmm okay, I finished taking a shower."
        j "I walked out of the locker room into the hall and I saw the lights had turned green."
        j "And that the safe door was open!"
        j "I also saw Sid taking a nap on the couch."
        j "I thought maybe I'd wake him and we could check it out together."
        j "You know, safety in numbers."
        j "And also he might yell at me if I didn't tell him..."
        j "But then I heard you yelling."
        j "I figured something must have happened..."
        j "So I left Sid to enjoy his nap while the adults handled everything!"
        bi "Jenny calling herself an adult and implying Sid isn't is an..."
        bi "Interesting statement to make."
        show jenny ind
        j "And uh, yeah, that's when I ran into you."
        j "Oh, and I figured out who the Game Master is."
        b "What?"
        j "Kidding! Just making sure you're paying attention."
        b "Oh..."
        bi "Not going to lie, part of me believed her..."
        bi "Maybe a good thing. It means I still have hope."
        b "Okay, so to summarize..."
        b "You left the locker room, saw the safe was open, were going to wake up Sid..."
        b "Then you heard me yell and came to the break room."
        j "Yep!"
        $ bank_evidence[7] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Jenny's Account was added to evidence."
        b "Alright, thanks Jenny."
        j "Yes sir sheriff sir!"
        b "...I don't know if deputies talk like they're in the military."
        j "Oh... that's a good point."
        hide jenny with dissolve
        bi "It's convenient that Jenny claims Sid was asleep when she passed him..."
        bi "Is she trying to make an alibi for herself using a sleeping witness?"
        if False not in bank_evidence[4:7]:
            bi "Okay, I've interrogated everyone."
            bi "I was in this room before the uniformed person ran in here..."
            bi "So besides the shells, I don't think there's too much of importance here."
            call bankDone from _call_bankDone_4
    call screen breakInv

label bankSid2:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    with dissolve
    show sid ind with dissolve
    b "Hey Sid."
    i "Hey Bert."
    i "You here to bring me my money?"
    b "Uh... not quite."
    b "Just wanted to make sure I remembered what you told me earlier."
    i "You don't suspect me, do you?"
    bi "Maybe if I just don't acknowledge the question he won't get mad."
    b "So you woke up, saw the light was green, and went to check the safe door was open."
    b "Then you heard someone scream, and you came to the break room and ran into me."
    i "Yeah, that's right."
    b "Great, thanks Sid, you're being really helpful!"
    i "Yeah, yeah, just don't forget about the money you owe me."
    bi "The money I owe {i}if{/i} we find any in the safe..."
    hide sid with dissolve
    call screen breakInv

screen hall2Inv():
    default tt = Tooltip("")
    imagemap:
        ground "bg bankhall3.png"
        if bank_extra[2]:
            hotspot(0, 0, 1, 1) action [Hide("hall2inv"), Jump("bankCouch")] mouse 'q' hovered tt.Action("Hallway Couch")
        else:
            hotspot(0, 0, 1, 1) action [Hide("hall2inv"), Jump("bankCouch")] mouse 'ex' hovered tt.Action("Hallway Couch")
        if bank_extra[3]:
            hotspot(0, 0, 1, 1) action [Hide("hall2inv"), Jump("bankLights")] mouse 'q' hovered tt.Action("Green Wall Lights")
        else:
            hotspot(0, 0, 1, 1) action [Hide("hall2inv"), Jump("bankLights")] mouse 'ex' hovered tt.Action("Green Wall Lights")
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

label bankCouch:
    scene bg banklobby
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "That's the couch Sid was sleeping on."
    bi "Maybe it's the fact that I only slept for a little bit and then had to investigate..."
    bi "But it does look really comfortable to sleep on."
    bi "Surely I have time for a nap, right?"
    bi "..."
    bi "No, I need to keep moving."
    bi "Plus, it'd be less than ideal if the others caught me napping on the job."
    $ bank_extra[2] = True
    call screen hall2Inv

label bankLights:
    scene bg banklobby
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "The lights on the wall..."
    bi "They were red before I tried to sleep."
    bi "Now they're green."
    bi "The safe is also open, so presumably that's why..."
    bi "But I guess there's no way to know for sure."
    bi "Well, we could re-lock the safe."
    bi "But there might be crucial evidence in there..."
    bi "For now, I'll assume the lights indicate the safe is open."
    $ bank_extra[3] = True
    call screen hall2Inv

screen officeInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg bankoffice.png"
        if bank_extra[4]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankShelves")] mouse 'q' hovered tt.Action("Office Shelves")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankShelves")] mouse 'ex' hovered tt.Action("Office Shelves")
        if bank_extra[5]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankDesk")] mouse 'q' hovered tt.Action("Desk")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankDesk")] mouse 'ex' hovered tt.Action("Desk")
        if bank_extra[6]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankCabinet")] mouse 'q' hovered tt.Action("Filing Cabinets")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankCabinet")] mouse 'ex' hovered tt.Action("Filing Cabinets")
        if bank_extra[7]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankPhotos")] mouse 'q' hovered tt.Action("Photos")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankPhotos")] mouse 'ex' hovered tt.Action("Photos")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Director's Office{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
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

label bankShelves:
    scene bg bankoffice
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "It's a nice set of shelves for displaying objects."
    bi "But unless the bank director's photo of a random skyscraper is crucial to this case..."
    bi "I don't think there's anything important here."
    $ bank_extra[4] = True
    call screen officeInv

label bankDesk:
    scene bg bankoffice
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "Sam spent a lot of time searching in this room, including the desk."
    bi "So it's probably not worth looking at every single file again."
    bi "But I should at least make sure there's nothing hidden here..."
    bi "..."
    bi "I took a look in each of the drawers, but I didn't see anything noticeable."
    $ bank_extra[5] = True
    call screen officeInv

label bankCabinet:
    scene bg bankoffice
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "There's a good chance we didn't find every piece of info in these filing cabinets..."
    bi "And there's also a good chance if I spent a week looking through them I still would miss something."
    bi "Who even needs a filing cabinet this big when Koogle Drive exists?"
    bi "Anyway..."
    bi "I looked through all the cabinets quickly, but didn't see anything out of the ordinary."
    $ bank_extra[6] = True
    call screen officeInv

label bankPhotos:
    scene bg bankoffice
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "Offices always have photos on the wall."
    bi "They're kind of cool to look at the first time but after that..."
    bi "It's still a bank, it's always going to be at least a little bit dreary."
    $ bank_extra[7] = True
    call screen officeInv

screen lockerInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg banklocker.png"
        if bank_evidence[11]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankLockers")] mouse 'q' hovered tt.Action("Lockers")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankLockers")] mouse 'ex' hovered tt.Action("Lockers")
        if bank_extra[8]:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankBathrooms")] mouse 'q' hovered tt.Action("Bathrooms")
        else:
            hotspot(0, 0, 1, 1) action [Hide("officeInv"), Jump("bankBathrooms")] mouse 'ex' hovered tt.Action("Bathrooms")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Locker Room{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
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

label bankBathroom:
    scene bg banklocker
    $ statusnt("Locker Room", "bert", ch=4, sun=4)
    with dissolve
    bi "I guess I need to search the bathrooms..."
    scene black with dissolve
    bi "I checked them out, but couldn't find anything."
    scene bg banklocker
    $ statusnt("Locker Room", "bert", ch=4, sun=4)
    with dissolve
    bi "Makes sense that there's nothing in there."
    bi "Jenny would have been in here."
    bi "So either she's the murderer or she might have bumped into someone hiding stuff in here."
    bi "Hopefully no one flushed something important..."
    if bank_evidence[11] and not bank_extra[8]:
        bi "There's not a whole lot in this room... I think I've checked everything."
        bi "Time to go to the next location."
        call bankDone from _call_bankDone_5
    $ bank_extra[8] = True
    call screen lockerInv

label bankLockers:
    scene bg banklocker
    $ statusnt("Locker Room", "bert", ch=4, sun=4)
    with dissolve
    if bank_evidence[11]:
        bi "When Jenny and I came here earlier, every locker had a uniform in it."
        bi "Now, one is missing, the one on Sam's body."
    else:
        bi "The lockers..."
        bi "Thankfully I have all the keys."
        bi "Otherwise, there could be lots of evidence hidden in them that we'd never find."
        bi "Jenny took a bit of a risk having me be the one to hold on to them..."
        bi "Though I guess if a locker was locked and I suddenly didn't have one of the keys, it would be obvious I did it."
        bi "Anyway, I should look through them to be sure."
        bi "..."
        bi "When Jenny and I were first in here, each locker had a guard uniform."
        bi "Now, one of those is missing, the one Sam is wearing."
        bi "Does that mean Sam was in the locker room at some point?"
        $ bank_evidence[11] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Uniforms in the Lockers was added to evidence."
        if bank_extra[8]:
            bi "There's not a whole lot in this room... I think I've checked everything."
            bi "Time to go to the next location."
            call bankDone from _call_bankDone_6
    call screen lockerInv

label firstSafe:
    $ bank_extra[9] = True
    scene bg bankvault3
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    bi "Wow... it is open."
    bi "Who opened it?"
    bi "As far as I know, no one that's alive has been in here..."
    bi "Did Sam open it before dying?"
    bi "Or is someone lying?"
    bi "Also, that note said..."
    bi '"The vault contains not only a substantial fortune, but also the true secrets of this game."'
    bi "It's so empty... there's no way I don't find everything in here in just a few minutes, right?"
    bi "Am I going to unlock the answers we've been looking for?"
    bi "I guess regardless, I'd better get in there and start searching..."
    call screen safeInv with dissolve


screen safeInv():
    default tt = Tooltip("")
    imagemap:
        ground "bg banksafe1.png"
        if bank_extra[10]:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankSafeCabinet")] mouse 'q' hovered tt.Action("Filing Cabinet")
        else:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankSafeCabinet")] mouse 'ex' hovered tt.Action("Filing Cabinet")
        if bank_evidence[9]:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankSign")] mouse 'q' hovered tt.Action("Sign on the Wall")
        else:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankSign")] mouse 'ex' hovered tt.Action("Sign on the Wall")
        if bank_evidence[10]:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankBox")] mouse 'q' hovered tt.Action("Box of Ammunition")
        else:
            hotspot(0, 0, 1, 1) action [Hide("safeInv"), Jump("bankBox")] mouse 'ex' hovered tt.Action("Box")
    if tt.value != "":
        frame:
            xalign 0.5
            yalign 0.0
            text "{i}"+tt.value+"{/i}"
    add "status.png"
    add Text("{b}Safe{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
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

label bankSafeCabinet:
    scene bg banksafe1
    $ statusnt("Safe", "bert", ch=4, sun=4)
    with dissolve
    bi "Another filing cabinet."
    bi "Hopefully this one isn't full of papers that I have to read through."
    bi "If only Shahar was here... lawyers are good at reading through pages of boring text, right?"
    bi "..."
    bi "Huh?"
    bi "This drawer's empty."
    bi "...So is this one."
    bi "In fact, all of them are."
    bi "Maybe there was money in here and someone took it?"
    bi "But then where is the money now? Unless it was like, ten dollars, it would be hard to hide."
    bi "I guess unless I find another clue related to this cabinet, best not to worry about it for now."
    if not bank_extra[10] and False not in bank_extra[9:10]:
        bi "Well, I wasn't wrong about the safe not having much to search."
        bi "Though, I'm wishing I found pretty much anything else in here..."
        bi "Evidence, a secret of the game..."
        bi "Oh well."
    $ bank_extra[10] = True
    call screen safeInv with dissolve

label bankSign:
    scene bg banksafe1
    $ statusnt("Safe", "bert", ch=4, sun=4)
    with dissolve
    if bank_evidence[9]:
        b "The sign on the safe says you can't unlock it from the inside."
        b "Jenny and I tested that and it's true."
        b "Also, we learned that the door opens and closes electronically once you pull or push it."
        b "And when it opens, it opens to a ninety degree angle."
    else:
        $ bank_evidence[9] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "The Safe Door was added to evidence."
        if bank_extra[10] and False not in bank_extra[9:10]:
            bi "Well, I wasn't wrong about the safe not having much to search."
            bi "Though, I'm wishing I found pretty much anything else in here..."
            bi "Evidence, a secret of the game..."
            bi "Oh well."
            call bankDone from _call_bankDone_7
    call screen lockerInv

label bankDone:
    if False not in bank_evidence[1:]:
        bi "Okay, I think I've searched the whole bank pretty thoroughly."
        bi "I don't feel like we have much to go off, but I've felt that way every time."
        bi "What's one more miracle at this point?"
        bi "Let's go to the lobby and discuss with the others."
        jump trial4a
    return
