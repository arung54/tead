init:
    transform exzoom:
        zoom 0.7

init python:
    trainAnswers = [[3, 0], [0, 1]] #This means first trial screen, statement 3, and you want to use evidence 0.
                                    #Second trial screen, statement 0, and you want to use evidence 1.
                                    # Evidence -1 = agree.

label correctTrain:
    if phase == 0:
        b "Dialog after the first argument"
        b "Blah blah blah"
        $ phase += 1
        call screen trainTrial("sid", "This is phase 1 {color=#55f}{/color}", 1,
        "sid", "Statement {color=#f55}1{/color}", -1,
        "sid", "Statement 3", 0,
        "sid", "Statement {color=#55f}1{/color}", 1)
    if phase == 1:
        b "Dialog after second argument"


screen trainEvidenceTrial():
    modal True
    add "eviscroll"
    imagemap:
        ground "evidenceui.png"
        hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("trainEvidenceTrial")]
    vbox xalign 0.15 yalign 0.5 spacing 30:
        if train_evidence1[0]:
            textbutton "The Computer" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[1]:
            textbutton "The View From The Front" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"

        if train_evidence1[2]:
            textbutton "Front Car Accounts" style "button_text" action SetVariable("currEvidence", 2)
        else:
            textbutton "-" style "button_text"
    if currEvidence == 0:
        image "computer.png" xcenter 800 yalign 0.0
        text "The computer used to navigate the train." xcenter 800 yanchor 0.0 ypos 250

    if currEvidence == 1:
        image "window.png" xcenter 800 yalign 0.0
        text "Wee woo wee woo.\nThis\n is\n a\n new\n line\n but it's longer!" xcenter 800 yanchor 0.0 ypos 250

    if currEvidence == 2:
        image "window.png" xcenter 800 yalign 0.0 alpha .4
        text "Kaiser, Lauren, Sam, and Shahar said they were all \nin the front car. \n \nLauren said the lights turned off,they heard the\nscream, and then went to the bar car." xcenter 800 yanchor 0.0 ypos 250

    if currEvidence >= 0:
        if trainAnswers[phase][0] == statement and trainAnswers[phase][1] == currEvidence:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Jump("correctTrain")]
        else:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Show("tryAgain", transition=Dissolve(0.2))]

#pers = prefix for the ___face.png you want to show
#statement is text that appears on the screen
#ag = 1 if you can agree, -1 if you can refute, and 0 if you can't interact

screen trainTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4):
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
    if agree == 1:
        if trainAnswers[phase][0] == statement and trainAnswers[phase][1] == -1:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Jump("correctTrain")]
        else:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Show("tryAgain", transition=Dissolve(0.2))]

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
            action [Show("trainEvidenceTrial", transition=Dissolve(0.2))]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04

screen tryAgain:
    modal True
    imagemap:
        ground "tryagain.png"
        hotspot(0, 0, 1279, 719) action [Hide("tryAgain", transition=Dissolve(0.2))]
