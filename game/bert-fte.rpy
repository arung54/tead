
label bertAsk0:
    scene bg trainfront1
    show bert happy with dissolve
    b "Our situation's pretty dire, but snacks can get me through anything!"
    blank "Should I talk to Bert?"
    menu:
        "Spend time with Bert":
            b "Snacks are better with company!"
            jump bertHang
        "Maybe later":
            hide bert with dissolve
            call screen frontCar

label bertHang:
    if fte_bert == 0:
        b "Man I'm really enjoying this pizza!"
        n "Uh... you're not eating anything right now."
        b "It's so good! Deep dish with tons of meats."
        n "Are you delirious? Should I get you some water or something?"
        b "Yeah, some water to wash down this pizza would be great!"
        n "...alright, I'll go get you some"
        scene black with fade
        ni "For my own safety, I didn't go back to give him water."
    $fte_bert += 1
    $ftecounter += 1
    hide bert with dissolve

    if ftecounter == 1:
        call screen frontCar
