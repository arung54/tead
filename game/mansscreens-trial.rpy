init python:
    def startMansionTrial(p1, s1, a1, p2, s2, a2, p3, s3, a3, p4, s4, a4, cS, cE, cL):
        startMansionTrialTimes(p1, s1, a1, 1.0, p2, s2, a2, 1.0, p3, s3, a3, 1.0, p4, s4, a4, 1.0, cS, cE, cL)

    def startMansionTrialTimes(p1, s1, a1, t1, p2, s2, a2, t2, p3, s3, a3, t3, p4, s4, a4, t4, cS, cE, cL):
        renpy.music.play("audio/invest1.wav")
        trialAnimation(p1, s1, t1, p2, s2, t2, p3, s3, t3, p4, s4, t4)
        renpy.transition(Dissolve(1.0))
        renpy.call_screen("mansionTrial", pers1 = p1, statement1 = s1, ag1 = a1, pers2 = p2, statement2 = s2, ag2 = a2, pers3 = p3, statement3 = s3, ag3 = a3, pers4 = p4, statement4 = s4, ag4 = a4, corrS = cS, corrE = cE, corrL = cL)

screen shatteredMans(lab):
    modal True
    add "shot.png"
    timer 1.0 action [Show("iGotIt", transition=Fade(0.5, 0.0, 0.5), l = lab), Hide("makeyourcase"), Hide("shatteredMans"), Hide("mansionTrial"), Hide("mansionEvidenceTrial"), Hide("pickSpot2"), Hide("pickSpot3"), Hide("pickSpot4"), Hide("chooseCharMansion")]

screen chooseCharMansion(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup3dead.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5

screen mansionEvidenceTrial(s, e, l):
    modal True
    add "eviscroll"
    if s == -1:
        imagemap:
            ground "evidenceuinb.png"
    else:
        imagemap:
            ground "evidenceui.png"
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("mansionEvidenceTrial")]
    vbox xalign 0.15 yalign 0.75 spacing 30:
        textbutton "Shape of the Wound" style "button_text" action SetVariable("currEvidence", 0)
        textbutton "Blood from the Wound" style "button_text" action SetVariable("currEvidence", 1)
        textbutton "Damp Clothing" style "button_text" action SetVariable("currEvidence", 2)
        textbutton "Burns on Stella's Hands" style "button_text" action SetVariable("currEvidence", 3)
        textbutton "Wires and Hole Under the Sink" style "button_text" action SetVariable("currEvidence", 4)
        textbutton "Generator" style "button_text" action SetVariable("currEvidence", 5)
        textbutton "Rope Attached to Generator" style "button_text" action SetVariable("currEvidence", 6)
        textbutton "Knife Sheath" style "button_text" action SetVariable("currEvidence", 7)
        textbutton "Location and the Murderer" style "button_text" action SetVariable("currEvidence", 8)

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

    if currEvidence >= 0:
        if (s == statement or s == -1) and (e == currEvidence or (type(e) is list and currEvidence in e)):
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(shatterNoise), Show("shatteredMans", lab = l)]#, Hide("mansionTrial"), Hide("mansionEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

#pers = prefix for the ___face.png you want to show
#statement is text that appears on the screen
#ag = 1 if you can agree, -1 if you can refute, and 0 if you can't interact

screen mansionTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4, corrS, corrE, corrL):
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
        action [Show("mansion_evidence", transition=Dissolve(0.3))]
    if agree == 1:
        if corrS == statement and corrE == -1:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(shatterNoise), Show("shatteredMans", lab = corrL)]#, Hide("mansionTrial"), Hide("mansionEvidenceTrial"), Jump(l)]
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
            action [Show("mansionEvidenceTrial", transition=Dissolve(0.2), s = corrS, e = corrE, l = corrL)]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04

screen pickSpot2:
    imagemap:
        ground "bg mansionbr.png"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(272, 444, 79, 41):
            action [Function(shatterNoise), Show("shatteredMans", lab = "trial2q")]

screen pickSpot3:
    imagemap:
        ground "map2ui.png"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(309, 394, 81, 74):
            action [Function(shatterNoise), Show("shatteredMans", lab = "trial2v")]

screen pickSpot4:
    imagemap:
        ground "map2ui.png"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(758, 306, 160, 179):
            action [Function(shatterNoise), Show("shatteredMans", lab = "trial2z")]
