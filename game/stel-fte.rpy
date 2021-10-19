#Julian

#Train 1
label stelAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show stella happy with dissolve
    t "Hello."
    ni "I should go talk to Bert instead of her."
    hide stella with dissolve
    call screen midCar with dissolve

#Train 2
label stelAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show stella happy with dissolve
    t "Hello."
    menu:
        "Spend time with Stella?":
            t "Sure, you're cute enough."
            jump stelHang
        "Maybe later":
            hide stella ind with dissolve
            call screen midCar with dissolve

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
        hide stella happy with dissolve
        show stella ind with dissolve
        t "Bonjour Dan."
        n "Uh, bonjar Stella."
        t "Bonj{i}ou{/i}r."
        n "Bonj{i}a{/i}r."
        t "Hmm, not quite."
        t "Regardless, I had a question for you."
        n "For me?"
        t "Yes. As you may know, I have a quite elite team of bodyguards."
        t "However, as you may also know, I have been kidnapped and taken... here."
        t "Clearly, I need a new team of bodyguards."
        n "So, what's the question?"
        hide stella ind
        show stella happy
        t "Well, you're pretty muscular and tough, yes?"
        t "Perhaps you'd make a nice addition to the team."
        n "You want {i}me{/i} to be one of your bodyguards?"
        ni "That's a pretty ironic request considering my history..."
        t "Well, of course you'd have to tryout like everyone else."
        n "Tryout?"
        t "Yes, of course!"
        t "A 2-acre portion of my Montpelier estate is dedicated to my team's training and recruiting."
        ni "Is this chick serious?"
        hide stella happy
        show stella ind
        t "This is, of course, all assuming we make it out of this situation alive."
        hide stella ind
        show stella happy
        t "If I die, there is nobody to guard, haha."
        n "Haha... yeah."
        ni "..."
        t "Hm, perhaps your tryouts can start early."
        n "What?"
        t "If there's any danger on this train, you can have the honor of protecting me."
        n "Umm..."
        t "Don't worry, I'll pay you back."
        ni "Did she just, wink at me?"
        t "Wonderful, thank you Dan."
        n "I don't think I agre-"
        t "What a productive meeting."
        t "Au revoir, Dan!"
        n "Au revwah, Stella?"
        t "Hm, close enough."
        hide stella happy with dissolve
        n "..."
        ni "After a very confusing conversation with Stella, we returned to mingling with the others."





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
    hide stella
    jump postFTEHandler
