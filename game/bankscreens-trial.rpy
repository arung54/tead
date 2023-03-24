init python:
    def startBankTrial(p1, s1, a1, p2, s2, a2, p3, s3, a3, p4, s4, a4, cS, cE, cL):
        startBankTrialTimes(p1, s1, a1, 1.0, p2, s2, a2, 1.0, p3, s3, a3, 1.0, p4, s4, a4, 1.0, cS, cE, cL)

    def startBankTrialTimes(p1, s1, a1, t1, p2, s2, a2, t2, p3, s3, a3, t3, p4, s4, a4, t4, cS, cE, cL):
        renpy.music.play("audio/invest1.wav")
        trialAnimation(p1, s1, t1, p2, s2, t2, p3, s3, t3, p4, s4, t4)
        renpy.transition(Dissolve(1.0))
        renpy.call_screen("bankTrial", pers1 = p1, statement1 = s1, ag1 = a1, pers2 = p2, statement2 = s2, ag2 = a2, pers3 = p3, statement3 = s3, ag3 = a3, pers4 = p4, statement4 = s4, ag4 = a4, corrS = cS, corrE = cE, corrL = cL)

screen shatteredBank(lab):
    modal True
    add "shot.png"
    timer 1.0 action [Show("iGotIt", transition=Fade(0.5, 0.0, 0.5), l = lab), Hide("makeyourcase"), Hide("shatteredBank"), Hide("bankTrial"), Hide("bankEvidenceTrial"), Hide("chooseCharBank")]

screen chooseCharBank(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup7dead.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5

screen bankEvidenceTrial(s, e, l):
    modal True
    add "eviscroll"
    if s == -1:
        imagemap:
            ground "evidenceuinb.png"
    else:
        imagemap:
            ground "evidenceui.png"
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("bankEvidenceTrial")]
    vbox xalign 0.15 yalign 0.75 spacing 18:
            textbutton "Bert's Account" style "button_text" action SetVariable("currEvidence", 0)
            textbutton "Break Room Door" style "button_text" action SetVariable("currEvidence", 1)
            textbutton "Gun and Shell" style "button_text" action SetVariable("currEvidence", 2)
            textbutton "Torn Elastic Belt" style "button_text" action SetVariable("currEvidence", 3)
            textbutton "Shells in the Lobby" style "button_text" action SetVariable("currEvidence", 4)
            textbutton "Freddy's Account" style "button_text" action SetVariable("currEvidence", 5)
            textbutton "Lauren's Account" style "button_text" action SetVariable("currEvidence", 6)
            textbutton "Jenny's Account" style "button_text" action SetVariable("currEvidence", 7)
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 8)
            textbutton "The Safe Door" style "button_text" action SetVariable("currEvidence", 9)
            textbutton "Ammunition" style "button_text" action SetVariable("currEvidence", 10)
            textbutton "Uniforms in the Lockers" style "button_text" action SetVariable("currEvidence", 11)
    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev4 bert.png" xcenter 800 yalign 0.1
            text "After the shooting, I chased the uniformed person into the hallway. It was quiet enough in the hallway that I both saw and heard the break room door close. I yanked the door open and found the dead body in the uniform." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev4 door.png" xcenter 800 yalign 0.1
            text "The door to the break room stayed open the entire time since I first walked in here. Nothing seemed out of the ordinary about the door." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev4 gun.png" xcenter 800 yalign 0.1
            text "The gun we found in the break room holds up to six bullets at once, and was empty when we found Sam's body. There was also a single bullet shell lying next to Sam." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev4 belt.png" xcenter 800 yalign 0.1
            if bank_extra[11]:
                text "Part of an elastic belt was found attached to a table leg in the break room. We don't know where the rest of the belt is. A whole elastic belt is long enough to reach from the table leg to the doorknob. When it's tied at both ends, it pulls on the door, but not with enough force to prevent you from opening it. Also, if the door is yanked when the belt is tied at both ends, the belt snaps." xcenter 800 yanchor 0.0 ypos 330
            else:
                text "Part of an elastic belt was found attached to a table leg in the break room. We don't know where the rest of the belt is." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev4 shells.png" xcenter 800 yalign 0.1
            text "There were six shells on the ground in the lobby, near the door to the hallway. They match the shell found by Sam's body." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev4 freddy.png" xcenter 800 yalign 0.1
            text "Freddy woke up to the sound of gunshots. He saw me get down to the floor, then saw the uniformed person leave, and me chase after them." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev4 lauren.png" xcenter 800 yalign 0.1
            text "Lauren was searching in the office, left, and was trying to find people. The safe was closed when she passed by, and she didn't see anyone in the locker room. She walked towards the lobby, passing the couch, and ended up finding me and Jenny because she heard us talking in the break room." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev4 jenny.png" xcenter 800 yalign 0.1
            text "Jenny had just finished taking a shower in the locker room. She walked out and saw the lights had turned green and the safe was open, then heard me yelling. She walked directly to the break room, passing Sid sleeping on the couch on the way." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev4 sid.png" xcenter 800 yalign 0.1
            if bank_extra[12]:
                text "Sid pretended to sleep on the couch when he heard me yell. He went into the safe for a few minutes after he thought Jenny wouldn't see him, found it was mostly empty, then came to the break room afterwards." xcenter 800 yanchor 0.0 ypos 330
            else:
                text "Sid woke up from sleeping on the couch. He saw the green lights, so he walked towards the safe door and saw it was open. However, he heard someone yell from this side of the bank and made his way towards us instead." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev4 sign.png" xcenter 800 yalign 0.1
            text "Even when the combination is entered, if it's shut, the safe door can't be opened from the inside. The door opens and closes electronically, and opens up to a ninety degree angle." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev4 ammo.png" xcenter 800 yalign 0.1
            text "Inside the safe we found bullets in a box. The bullets come in sets of six, and are attached by a piece of metal so that a whole set can quickly be loaded at once. However, the piece of metal prevents you from separating individual bullets." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 11:
            image "ev4 uniform.png" xcenter 800 yalign 0.1
            text "Originally, each locker had one uniform it. When I investigated the locker room after Sam's death, only one of those uniforms was missing." xcenter 800 yanchor 0.0 ypos 330


    if currEvidence >= 0:
        if (s == statement or s == -1) and (e == currEvidence or (type(e) is list and currEvidence in e)):
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(shatterNoise), Show("shatteredBank", lab = l)]#, Hide("bankTrial"), Hide("bankEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

#pers = prefix for the ___face.png you want to show
#statement is text that appears on the screen
#ag = 1 if you can agree, -1 if you can refute, and 0 if you can't interact

screen bankTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4, corrS, corrE, corrL):
    modal True
    add "debatescroll"
    add "debateui.png"
    vbox xalign 0.06 ypos 190 spacing 20:
        imagebutton:
            idle pers1+"face.png" action [SetVariable("statement", 0), SetVariable("agree", ag1)]
        imagebutton:
            idle pers2+"face.png" action [SetVariable("statement", 1), SetVariable("agree", ag2)]
        imagebutton:
            idle pers3+"face.png" action [SetVariable("statement", 2), SetVariable("agree", ag3)]
        imagebutton:
            idle pers4+"face.png" action [SetVariable("statement", 3), SetVariable("agree", ag4)]
    if statement >= 0:
        add "expoint.png" xpos 0.28 ypos 175+127*statement at exzoom
    fixed xmaximum 750:
        textbutton statement1 xpos 0.64 xanchor 0 ypos 190 yanchor 0 style "button_text" action [SetVariable("statement", 0), SetVariable("agree", ag1)]
        textbutton statement2 xpos 0.64 xanchor 0 ypos 317 yanchor 0 style "button_text" action [SetVariable("statement", 1), SetVariable("agree", ag2)]
        textbutton statement3 xpos 0.64 xanchor 0 ypos 444 yanchor 0 style "button_text" action [SetVariable("statement", 2), SetVariable("agree", ag3)]
        textbutton statement4 xpos 0.64 xanchor 0 ypos 571 yanchor 0 style "button_text" action [SetVariable("statement", 3), SetVariable("agree", ag4)]
    imagebutton:
        idle "evidenceicon.png" at evizoom
        xpos 0.398
        yalign 0.0225
        action [Show("bank_evidence", transition=Dissolve(0.3))]
    if agree == 1:
        if corrS == statement and corrE == -1:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(shatterNoise), Show("shatteredBank", lab = corrL)]#, Hide("bankTrial"), Hide("bankEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

    else:
        imagebutton:
            idle "agreegrey.png"
            xpos 0.55
            yalign 0.04

    if agree == -1:
        imagebutton:
            idle "refute.png"
            xpos 0.775
            yalign 0.04
            action [Show("bankEvidenceTrial", transition=Dissolve(0.2), s = corrS, e = corrE, l = corrL)]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04

screen chooseCharBank(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup7dead.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shatteredBank", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5


screen pickSpot8:
    imagemap:
        ground "bg bankbreak4.png"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1055, 61, 67, 610):
            action [Function(shatterNoise), Show("shatteredBank", lab = "trial4o")]

screen pickSpot9:
    imagemap:
        ground "map2ui.png"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1037, 513, 97, 180):
            action [Function(shatterNoise), Show("shatteredBank", lab = "trial4v")]
