#Arun

#Train 1
label laurAsk0:
    scene bg trainmid
    show lauren happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label laurAsk1:
    scene bg trainmid
    show lauren happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Mansion 1
label laurAsk2:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Mansion 2
label laurAsk3:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Mansion 3
label laurAsk4:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 1
label laurAsk5:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 2
label laurAsk6:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 3
label laurAsk7:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Bank 1
label laurAsk8:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar
#Bank 2
label laurAsk9:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Bank 3
label laurAsk10:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

label laurHang:
    #Dan FTE 1
    if fte_laur == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_laur == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_laur == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_laur == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_laur >= 3:
        bi "I enjoyed some time with Lauren, if only because of his pirate speak."

    $fte_laur += 1
    $ftecounter += 1
    hide lauren with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
