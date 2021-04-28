
label cathAsk0:
    scene bg trainmid
    show catherine happy with dissolve
    c "Here you go Sesame! You can have the turkey from this sandwich."
    ni "I should go talk to Bert."
    call screen midCar


label cathAsk1:
    scene bg trainmid
    show catherine happy with dissolve
    c "Hey Dan!"
    blank "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "Cool!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
            call screen midCar

label cathHang:
    if fte_cath == -1:
        show catherine happy
        c "Hey Dan."
        ses "Mrow!"
        c "Sesame says hi too!"
        n "Hey."
        c ""

        scene black with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."


    $fte_cath += 1
    hide catherine with dissolve
    jump postFTEHandler
