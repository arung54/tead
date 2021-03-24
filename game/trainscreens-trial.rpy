init:
    transform customzoom:
        zoom 2.0

screen trainTrial1():
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
            textbutton "Refute with Evidence"
            textbutton "Agree"
