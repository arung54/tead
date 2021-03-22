#Arun

#Train 1
label dracAsk0:
    scene bg trainmid
    show drac happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label dracAsk1:
    scene bg trainmid
    show drac happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Mansion 1
label dracAsk2:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Mansion 2
label dracAsk3:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Mansion 3
label dracAsk4:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Hospital 1
label dracAsk5:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Hospital 2
label dracAsk6:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

#Hospital 3
label dracAsk7:
    menu:
        "Spend time with Dracula?":
            j "Sure!"
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen midCar

label dracHang:
    #Dan FTE 1
    if fte_drac == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_drac == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_drac == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_drac == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_drac >= 3:
        bi "I enjoyed some time with drac, if only because of his pirate speak."

    $fte_drac += 1
    $ftecounter += 1
    hide drac with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
