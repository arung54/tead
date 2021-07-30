#Arun

#Train 1
label dracAsk0:
    scene bg trainback
    show drac happy with dissolve
    d "I wish it were slightly less bright in this train..."
    ni "I should go talk to Bert instead of this guy."
    call screen backCar

#Train 2
label dracAsk1:
    scene bg trainback
    show drac happy with dissolve
    d "Hello Dan, would you like to speak?"
    menu:
        "Spend time with Dracula?":
            d "Very well. Not as if I have other plans."
            jump dracHang
        "Maybe later":
            hide drac with dissolve
            call screen backCar

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
        n "So um... your name's not actually Dracula right?"
        d "No, it is Dracula."
        n "No last name?"
        d "If I had a full name I wanted you to know, I would have told you it."
        n "Your parents named you Dracula?"
        d "No, I took on the name after returning from death."
        n "You know Dracula's from a book, right?"
        d "If there is a book that resembles my life, that is purely coincidence."
        d "It's like those disclaimers at the start of movies."
        d "That or someone has written a book about my life without my permission."
        n "The book took place like, a hundred years ago."
        n "You're not going to tell me you're over a hundred years old, right?"
        d "What is that so hard to believe?"
        n "Humans rarely live past being a hundred."
        d "Yes, I'm not human."
        d "Admittedly, I was human at one point, and continue to maintain a young human appearance."
        d "And as I told you earlier, I've returned from death."
        d "So it shouldn't be shocking if I lived a normal human life and then another life after that."
        n "You understand how serious the situation we're in is, right?"
        n "Our lives are on the line."
        n "Putting on this whole charade at a time like this?"
        n "It seems immature for someone of your... age."
        d "It seems more immature of you to assume that this is a charade."
        d "And if it were a charade, to assume it served no purpose."
        n "No, I'm pretty sure in most parts of the world pretending to be a vampire is more immature."
        d "We can agree to disagree."
        d "I assure you, Dan, I fully intend to do everything in my power to help us escape."
        d "And I hope that you are approaching the situation with the same resolve."
        d "But if you are, I don't think conversations like this are making progress in any meaningful way."
        d "I will not be taking further questions on this line of thought."
        n "...got it."
        n "So uh... got any hobbies?"
        d "Maybe I should rephrase. I will take no further questions about myself and my life."
        n "What am I supposed to talk to you about then?"
        d "Let's brainstorm escape plans. That seems to be the most prudent use of time."
        n "Sheesh, was just trying to get to know you better."
        d "If we both make it out alive, we will have plenty of time for that."
        scene black with fade
        ni "Guess Dracula and I just need to agree to coexist peacefully..."
        ni "Or maybe just not talk to each other."

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
    hide drac with dissolve
    jump postFTEHandler
