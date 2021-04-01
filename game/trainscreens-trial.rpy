init:
    transform exzoom:
        zoom 0.7

init python:
    trainAnswers = [[3, 0], [0, 1]]

label checkEvidenceTrain:
    if trainAnswers[phase][0] == statement and trainAnswers[phase][1] == currEvidence:
        b "No, that's wrong!"
        $b(str(currEvidence))
    else:
        b "No, that can't be it... let me think some more."
    if phase == 0:
        hide screen trainTrial
        call screen trainTrial


screen trainEvidenceTrial():
    add "scary.png"
    vbox xalign 0.0 spacing 30:
        if train_evidence[0]:
            textbutton "The Computer" style "button_text" action SetVariable("currEvidence", 0)
        else:
            textbutton "-" style "button_text"

        if train_evidence[1]:
            textbutton "The View From The Front" style "button_text" action SetVariable("currEvidence", 1)
        else:
            textbutton "-" style "button_text"
        textbutton "Go Back" action Hide("trainEvidenceTrial")

    if currEvidence == 0:
        image "computer.png" xalign 1.0 yalign 0.0
        text "The computer used to navigate the train." xalign 1.0 yalign 0.5
        textbutton "Submit Evidence" xalign 1.0 yalign 1.0 action [Hide("trainEvidenceTrial"), Jump("checkEvidenceTrain")]

    if currEvidence == 1:
        image "window.png" xalign 1.0 yalign 0.0
        text "The tunnel wasn't visible from the window." xalign 1.0 yalign 0.5
        textbutton "Submit Evidence" xalign 1.0 yalign 1.0 action [Hide("trainEvidenceTrial"), Jump("checkEvidenceTrain")]

screen trainTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4):
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
    textbutton statement1 xpos 0.38 ypos 220 style "button_text" action [SetVariable("statement", 0), SetVariable("agree", ag1)]
    textbutton statement2 xpos 0.38 ypos 347 style "button_text" action [SetVariable("statement", 1), SetVariable("agree", ag2)]
    textbutton statement3 xpos 0.38 ypos 474 style "button_text" action [SetVariable("statement", 2), SetVariable("agree", ag3)]
    textbutton statement4 xpos 0.38 ypos 601 style "button_text" action [SetVariable("statement", 3), SetVariable("agree", ag4)]
    if agree == 1:
        imagebutton:
            idle "agree.png"
            xpos 0.55
            yalign 0.04
            action [Hide("trainTrial"), SetVariable("currEvidence", -1), Jump("checkEvidenceTrain")]
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
            action [Show("trainEvidenceTrial")]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04
