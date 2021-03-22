#Julian

#Train 1
label kaisAsk0:
    scene bg trainmid
    show kaiser happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert instead of this guy."
    call screen midCar

#Train 2
label kaisAsk1:
    scene bg trainmid
    show kaiser happy with dissolve
    h "Hey Dan!"
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump kaisHang
        "Maybe later":
            hide kaiser with dissolve
            call screen midCar

label kaisHang:
    #Dan FTE 1
    if fte_kais == -1:
        h "Y'arr, Dan, what can I do for ye?"

    $fte_kais += 1
    $ftecounter += 1
    hide kaiser with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
