init:
    transform customzoom:
        zoom 2.0

init python:
    trainAnswers = [[3, 0], [0, 1]]

label checkEvidence:
    if trainAnswers[phase][0] == statement and trainAnswers[phase][1] == currEvidence:
        b "No, that's wrong!"
        $b(str(currEvidence))
    else:
        b "No, that can't be it... let me think some more."
    if phase == 0:
        hide screen trainTrial0
        call screen trainTrial0


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
        textbutton "Submit Evidence" xalign 1.0 yalign 1.0 action [Hide("trainEvidenceTrial"), Jump("checkEvidence")]

    if currEvidence == 1:
        image "window.png" xalign 1.0 yalign 0.0
        text "The tunnel wasn't visible from the window." xalign 1.0 yalign 0.5
        textbutton "Submit Evidence" xalign 1.0 yalign 1.0 action [Hide("trainEvidenceTrial"), Jump("checkEvidence")]

screen trainTrial0():
    vbox xalign 0.0 spacing 50:
        imagebutton:
            idle "jennychibi.png" at customzoom
        imagebutton:
            idle "kaiserchibi.png" at customzoom
        imagebutton:
            idle "jennychibi.png" at customzoom
        imagebutton:
            idle "kaiserchibi.png" at customzoom
    vbox xalign 0.1 spacing 70:
        textbutton "TEAD is the best game ever!" style "button_text" action [SetVariable("statement", 0)]
        textbutton "No it's not!" style "button_text" action [SetVariable("statement", 1)]
        textbutton "Yes it is, Julian made it!" style "button_text" action [SetVariable("statement", 2)]
        textbutton "No he didn't!" style "button_text" action [SetVariable("statement", 3)]
    if statement >= 0:
        hbox xalign 1.0 yalign statement*0.13 spacing 300:
            textbutton "Refute with Evidence" action Show("trainEvidenceTrial")
            textbutton "Agree" action [SetVariable("currEvidence", -1),  Jump("checkEvidence")]
