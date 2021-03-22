#Arun

#Train 1
label frogAsk0:
    scene bg trainmid
    show frog happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label frogAsk1:
    scene bg trainmid
    show frog happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Mansion 1
label frogAsk2:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Mansion 2
label frogAsk3:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Mansion 3
label frogAsk4:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Hospital 1
label frogAsk5:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Hospital 2
label frogAsk6:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Hospital 3
label frogAsk7:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Bank 1
label frogAsk8:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar
#Bank 2
label frogAsk9:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

#Bank 3
label frogAsk10:
    menu:
        "Spend time with Froggy?":
            j "Sure!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar

label frogHang:
    #Dan FTE 1
    if fte_frog == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_frog == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_frog == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_frog == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_frog >= 3:
        bi "I enjoyed some time with frog, if only because of his pirate speak."

    $fte_frog += 1
    $ftecounter += 1
    hide frog with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
