init:
    transform exzoom:
        zoom 0.7
    transform cczoom:
        zoom 0.75
    transform evizoom:
        zoom .8
    $ shatter = ImageDissolve("shatter.png", 1.0, 8)
    $ shot = ImageDissolve("shot.png", 1.0, 8)

init python:
    def shatterNoise():
        renpy.music.play("audio/shatter.mp3", channel="sfx")

    def errorNoise():
        renpy.music.play("audio/wrong.wav", channel="sfx", relative_volume = 0.2)

    def startTrainTrial(p1, s1, a1, p2, s2, a2, p3, s3, a3, p4, s4, a4, cS, cE, cL):
        startTrainTrialTimes(p1, s1, a1, 1.0, p2, s2, a2, 1.0, p3, s3, a3, 1.0, p4, s4, a4, 1.0, cS, cE, cL)

    def startTrainTrialTimes(p1, s1, a1, t1, p2, s2, a2, t2, p3, s3, a3, t3, p4, s4, a4, t4, cS, cE, cL):
        renpy.music.play("audio/invest1.wav")
        trialAnimation(p1, s1, t1, p2, s2, t2, p3, s3, t3, p4, s4, t4)
        renpy.transition(Dissolve(1.0))
        renpy.call_screen("trainTrial", pers1 = p1, statement1 = s1, ag1 = a1, pers2 = p2, statement2 = s2, ag2 = a2, pers3 = p3, statement3 = s3, ag3 = a3, pers4 = p4, statement4 = s4, ag4 = a4, corrS = cS, corrE = cE, corrL = cL)


    def trialAnimation(p1, s1, t1, p2, s2, t2, p3, s3, t3, p4, s4, t4):
        _preferences.show_empty_window = False

        renpy.show("makeyourcase")
        renpy.with_statement(Dissolve(1.0))
        renpy.pause(1.0, hard = True)
        renpy.hide("makeyourcase")
        renpy.show("debatescroll")
        renpy.show("debateui")
        renpy.with_statement(Dissolve(1.0))

        renpy.show(p1+"face", at_list=[Position(xalign = 0.06, ypos = 298)], tag = "p1")
        renpy.show("s1", at_list=[Position(xpos=0.375, xanchor=0, ypos=190, yanchor=0)], what = Text(s1, xmaximum = 750))
        renpy.with_statement(moveinbottom)
        renpy.pause(t1, hard = True)

        renpy.show(p2+"face", at_list=[Position(xalign = 0.06, ypos = 425)], tag = "p2")
        renpy.show("s2", at_list=[Position(xpos=0.375, xanchor=0, ypos=317, yanchor=0)], what = Text(s2, xmaximum = 750))
        renpy.with_statement(moveinbottom)
        renpy.pause(t2, hard = True)

        renpy.show(p3+"face", at_list=[Position(xalign = 0.06, ypos = 552)], tag = "p3")
        renpy.show("s3", at_list=[Position(xpos=0.375, xanchor=0, ypos=444, yanchor=0)], what = Text(s3, xmaximum = 750))
        renpy.with_statement(moveinbottom)
        renpy.pause(t3, hard = True)

        renpy.show(p4+"face", at_list=[Position(xalign = 0.06, ypos = 679)], tag = "p4")
        renpy.show("s4", at_list=[Position(xpos=0.375, xanchor=0, ypos=571, yanchor=0)], what = Text(s4, xmaximum = 750))
        renpy.with_statement(moveinbottom)
        renpy.pause(t4, hard = True)

screen shattered(lab):
    modal True
    add "shot.png"
    timer 1.0 action [Show("iGotIt", transition=Fade(0.5, 0.0, 0.5), l = lab), Hide("makeyourcase"), Hide("shattered"), Hide("trainTrial"), Hide("trainEvidenceTrial"), Hide("pickSpot1"), Hide("chooseChar")]

screen iGotIt(l):
    modal True
    add "bg igotitbg.png"
    add "gotit"
    timer 1.5 action[SetVariable("statement", -1), SetVariable("agree", 0), Hide("shattered"), Hide("p1"), Hide("p2"), Hide("p3"), Hide("p4"), Hide("s1"), Hide("s2"), Hide("s3"), Hide("s4"), Hide("debatescroll"), Hide("debateui"), Hide("iGotIt", transition=Dissolve(1.0)), Jump(l)]

screen chooseChar(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5

screen chooseChar2(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup1.png"
        hotspot(623, 63, 310, 616):
            if ans == "kaiser":
                action [Jump(correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(951, 123, 276, 554):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(47, 114, 231, 563):
            if ans == "sam":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(301, 54, 312, 623):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shattered", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5


screen trainEvidenceTrial(s, e, l):
    modal True
    add "eviscroll"
    if s == -1:
        imagemap:
            ground "evidenceuinb.png"
    else:
        imagemap:
            ground "evidenceui.png"
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("trainEvidenceTrial")]
    vbox xalign 0.15 yalign 0.75 spacing 30:
        if train_evidence1[0]:
            textbutton "Login Screen" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[1]:
            textbutton "Front Car Lighting" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[2]:
            textbutton "Front Car Accounts" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[0]:
            textbutton "Bar Car Lighting" style "button_text" action SetVariable("currEvidence", 3)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[1]:
            textbutton "Dracula's Account" style "button_text" action SetVariable("currEvidence", 4)
        else:
            textbutton "-" style "button_text"

        if train_evidence2[2]:
            textbutton "Catherine's Account" style "button_text" action SetVariable("currEvidence", 5)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[0]:
            textbutton "Hanging Object" style "button_text" action SetVariable("currEvidence", 6)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[1]:
            textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 7)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[2]:
            textbutton "Back Car Closet" style "button_text" action SetVariable("currEvidence", 8)
        else:
            textbutton "-" style "button_text"

        if train_evidence3[3]:
            textbutton "State of the Body" style "button_text" action SetVariable("currEvidence", 9)
        else:
            textbutton "-" style "button_text"

    fixed xmaximum 580:
        if currEvidence == 0:
            image "loginev.png" xcenter 800 yalign 0.1
            text "Something seems different here..." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "lights2ev.png" xcenter 800 yalign 0.1
            text "The ambient light in the front car makes it pretty easy to see, even at night." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "frontaccounts1.png" xcenter 800 yalign 0.1
            text "Kaiser, Lauren, Sam, and Shahar said they were all in the front car. Lauren said the car went dark, but the lights were still on, so they could see what they were doing." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "lightsev" xcenter 800 yalign 0.1
            text "It's dark out, and the lights in the bar car are off." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "dracaccount1" xcenter 800 yalign 0.1
            text "Dracula said the scream we heard while it was dark was somehow 'familiar'." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "catherineaccount1" xcenter 800 yalign 0.1
            text "Catherine said her hand was on the door knob to the back car the whole time it was dark. It was dark, and the scream scared her, so she didn't keep moving." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ringev" xcenter 800 yalign 0.1
            text "We found this hanging outside the back window of the train." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "sidaccount1.png" xcenter 800 yalign 0.1
            text "Sid said he was sleeping in the bed, but was woken up by loud noises and a scream." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "closetev.png" xcenter 800 yalign 0.1
            text "The closet opened easily, but there was nothing inside." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "stateofbody1.png" xcenter 800 yalign 0.1
            text "A superficial autopsy suggests Dan's cause of death is the large metal rod in his chest, with no other visible injuries. He seemed to have been looking out the window at the time of death." xcenter 800 yanchor 0.0 ypos 330

    if currEvidence >= 0:
        if (s == statement or s == -1) and e == currEvidence:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(shatterNoise), Show("shattered", lab = l)]#, Hide("trainTrial"), Hide("trainEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

screen pickSpot1:
    imagemap:
        ground "pickthespot1"
        hotspot(0, 0, 1279, 719):
            action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(958, 469, 29, 92):
            action [Function(shatterNoise), Show("shattered", lab = "trial1c")]
    add "wherewasmurderweapon"

#pers = prefix for the ___face.png you want to show
#statement is text that appears on the screen
#ag = 1 if you can agree, -1 if you can refute, and 0 if you can't interact

screen trainTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4, corrS, corrE, corrL):
    modal True
    add "debatescroll"
    add "debateui.png"
    vbox xalign 0.06 ypos 190 spacing 20:
        imagebutton:
            idle pers1+"face.png"
        imagebutton:
            idle pers2+"face.png"
        imagebutton:
            idle pers3+"face.png"
        imagebutton:
            idle pers4+"face.png"
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
        action [Show("train_evidence", transition=Dissolve(0.3))]
    if agree == 1:
        if corrS == statement and corrE == -1:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(shatterNoise), Show("shattered", lab = corrL)]#, Hide("trainTrial"), Hide("trainEvidenceTrial"), Jump(l)]
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
            action [Show("trainEvidenceTrial", transition=Dissolve(0.2), s = corrS, e = corrE, l = corrL)]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04

screen tryAgain:
    modal True
    imagemap:
        ground "tryagain.png"
        hotspot(0, 0, 1279, 719):
             action [SetVariable("mistakes", mistakes+1), Hide("tryAgain", transition=Dissolve(0.2))]
