#Julian

#Train 1
label samAsk0:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show sam happy with dissolve
    s "Hey."
    ni "I should go talk to Bert instead."
    hide sam with dissolve
    call screen frontCar

#Train 2
label samAsk1:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show sam with dissolve
    s "Hey."
    menu:
        "Spend time with Sam?":
            s "Sure, I guess I can talk."
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen frontCar

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
        s "Really?"
        n "What?"
        s "You could have bothered anyone on this train, and you chose me?"
        s "Spare me."
        n "It can't hurt for us to try to get along."
        s "Hm, sounds kinda like it would hurt."
        n "You've got a good sense of humor, ya know."
        s "I'm wasn't really making a joke, I just speak my mind."
        s "No point in beating around the bush, especially in a situation like this."
        ni "Sam's so difficult to open up..."
        n "Though I'm worried you've ostracized some of the others on board."
        s "As if you haven't?"
        n "Well, yeah, but..."
        n "I think that's less by choice. I'm just... not great at conversations."
        n "It's been a while since I've gotten to talk to someone like this."
        s "I can tell, you're super awkward dude."
        ni "..."
        s "Maybe you need a shtick."
        n "A shtick?"
        s "Yeah, like, pretending to have magic, two personalities, or being a robot."
        n "Uhhh, those seem pretty strange."
        s "Well it doesn't have to be extreme, you could try just being funny or something."
        s "Maybe you could be the \"Joke Guy.\""
        n "The \"Joke Guy?\""
        s "Like, picture this: you open the bar car mini-fridge and find a severed arm!"
        s "Perfect time for the Joke Guy to say, \"Someone come give me a hand with this!\""
        ni "..."
        s "I mean, that exact scenario seems unlikely, but you get the idea."
        n "Uh, I'd hope it's unlikely..."
        s "I'm trying to help you here, loner."
        s "Let's try it."
        s "What's your line if Freddy takes off his hoodie and he's been a baby lion this whole time?"
        n "Uhhh...."
        show scary with dissolve:
            alpha .5
        menu:
            n "{i}What's Joke Guy's line?{/i}"

            "WHAT?! You gotta be kitten me!":
                n "... How's that?"
                s "Hmm, you'll get there."

            "Wow! You said you were a frog, but you've been lion the whole time!":
                n "... How's that?"
                s "Hmm, not bad."
        scene black with fade
        ni "After a surprisingly pleasant conversation with Sam, we both went seperate ways."


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
