#Julian

#Train 1
label stelAsk0:
    scene bg trainmid
    show sam happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label stelAsk1:
    scene bg trainmid
    show sam happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Stella?":
            j "Sure!"
            jump stelHang
        "Maybe later":
            hide stella with dissolve
            call screen midCar

#Mansion 1
label stelAsk2:
    menu:
        "Spend time with Stella?":
            j "Sure!"
            jump stelHang
        "Maybe later":
            hide stella with dissolve
            call screen midCar

#Mansion 2
label stelAsk3:
    menu:
        "Spend time with Stella?":
            j "Sure!"
            jump stelHang
        "Maybe later":
            hide stella with dissolve
            call screen midCar

#Mansion 3
label stelAsk4:
    menu:
        "Spend time with Stella?":
            j "Sure!"
            jump stelHang
        "Maybe later":
            hide stella with dissolve
            call screen midCar

label stelHang:
    #Dan FTE 1
    if fte_stel == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_stel == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_stel == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_stel == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_stel >= 3:
        bi "I enjoyed some time with sam, if only because of his pirate speak."

    $fte_stel += 1
    $ftecounter += 1
    hide stella with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
