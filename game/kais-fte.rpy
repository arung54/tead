#Julian

#Train 1
label kaisAsk0:
    scene bg trainfront1
    show kaiser ind with dissolve
    k "..."
    ni "I should go talk to Bert instead of this guy."
    call screen frontCar

#Train 2
label kaisAsk1:
    scene bg trainfront1
    show kaiser ind with dissolve
    k "..."
    menu:
        "Spend time with Kaiser?":
            k "Oh? Did you have something to say, Dan?"
            jump kaisHang
        "Maybe later":
            hide kaiser ind with dissolve
            call screen frontCar

label kaisHang:
    #Dan FTE 1
    if fte_kais == -1:
        k "Hello."
        n "Uh, hey."
        k "I've never much been one for small talk."
        n "Yeah, same."
        k "..."
        n "..."
        ni "This guy's stone cold..."
        k "Do you want something?"
        n "No, no! I just..."
        n "Figured it can't hurt for everyone to get along."
        n "I don't know, maybe that's foolish."
        k "You're not wrong."
        n "Oh?"
        k "But alas, the effort required for us to form a friendship is..."
        k "Simply too high."
        n "Oh."
        k "Unfortunately I have no such interest."
        k "If you have any questions I'd be willing to answer them though."
        ni "... I thought {i}I{/i} wasn't very personable..."
        show scary with dissolve:
            alpha .5
        ni "Do I have any questions for Kaiser? Ummm..."
        menu:
            ni "Do I have any questions for Kaiser? Ummm..."

            "How old are you?":
                hide scary with dissolve
                n "I'm 27."

            "Any hobbies?":
                hide scary with dissolve
                n "Hmm. Biking."

            "Do you think we'll get out of this alive?":
                hide scary with dissolve
                k "Hm, no."

        k "Anything else?"
        n "Um, no, that's all I guess."
        k "I see. It's been a pleasure."
        hide kaiser ind with dissolve
        ni "\"{i}It's been a pleasure?{/i}\" Is that a dash of personality I hear?!"
        ni "Maybe we did bond, a little bit."
        scene black with fade
        ni "After Kaiser left, I went back to mingling with the others."

    $fte_kais += 1
    hide kaiser with dissolve
    jump postFTEHandler
