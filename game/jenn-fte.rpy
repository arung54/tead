#Arun

#Train 1
label jennAsk0:
    scene bg trainmid
    show jenny happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label jennAsk1:
    scene bg trainmid
    show jenny happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 1
label jennAsk2:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 2
label jennAsk3:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 3
label jennAsk4:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 1
label jennAsk5:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 2
label jennAsk6:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 3
label jennAsk7:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 1
label jennAsk8:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar
#Bank 2
label jennAsk9:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 3
label jennAsk10:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

label jennHang:
    #Dan FTE 1
    if fte_jenn == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_jenn == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_jenn == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_jenn == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_jenn >= 3:
        bi "I enjoyed some time with Jenny, if only because of his pirate speak."

    $fte_jenn += 1
    $ftecounter += 1
    hide jenny with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
