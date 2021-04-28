#Julian

#Train 1
label samAsk0:
    scene bg trainmid
    show sam happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label samAsk1:
    scene bg trainmid
    show sam happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Mansion 1
label samAsk2:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Mansion 2
label samAsk3:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Mansion 3
label samAsk4:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 1
label samAsk5:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 2
label samAsk6:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 3
label samAsk7:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Bank 1
label samAsk8:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar
#Bank 2
label samAsk9:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Bank 3
label samAsk10:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

label samHang:
    #Dan FTE 1
    if fte_sam == -1:
        h "Y'arr, Dan, what can I do for ye?"

    #Bert FTE 1
    if fte_sam == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_sam == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_sam == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_sam >= 3:
        bi "I enjoyed some time with sam, if only because of his pirate speak."

    $fte_sam += 1
    $ftecounter += 1
    hide sam with dissolve

    if ftecounter == 0:
        jump postFT0

    if ftecounter == 1:
        jump postFT1
