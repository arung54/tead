#Arun

#Train 1
label frogAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show frog sad with dissolve
    f "I miss my mom..."
    ni "I should go talk to Bert instead of this kid."
    hide frog with dissolve
    call screen midCar

#Train 2
label frogAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show frog sad with dissolve
    f "I wish there was another kid here..."
    menu:
        "Spend time with Froggy?":
            f "O-okay mister..."
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
        n "So um..."
        n "Uh..."
        f "..."
        ni "Why did I choose to spend my time talking to a kid?"
        ni "It's been years since I talked to adult civilians, much less kids."
        n "So uh... what's with the frog thing?"
        f "The... frog thing?"
        n "Yeah like... you're wearing a frog costume, and you like being called Froggy."
        f "Oh..."
        show frog ind
        f "Well, I really like frogs!"
        f "My favorite is the poison dart frog!"
        f "It's deadly but has really pretty colors."
        f "Some other frogs evolved to have similar skin to poison dart frogs."
        f "That way, even though they're not poisonous they look like they are."
        f "So predators will leave them alone."
        f "Did you know toads are also frogs?"
        f "Most people think toads and frogs are like alligators and crocodiles."
        f "Alligators and crocodiles are in different families genetically."
        f "Whereas toads and frogs exist in the same genetic families."
        f "Basically it's a toad if its skin is more warty and less slimy."
        f "There's a famous urban myth about frogs that's false!"
        f "It's called the boiling frog."
        f "The myth says a frog placed in boiling water will jump out immediately."
        f "But a frog placed in warm water that heats up gradually will boil to death."
        f "The moral of the story is to be way of seemingly small changes that turn into big ones."
        f "But really, frogs will just jump out of boiling water."
        n "Have you tested this theory on your own?"
        f "What? No!"
        f "I'd never a harm an innocent frog like that."
        n "Maybe that's a good lesson for us. Maybe we're the frogs in water."
        n "Even if things feel \"warm\" now they may become boiling later."
        f "That seems like something for adults to think about, not kids like me."
        ni "...so much for trying to relate."
        f "There's a pair of frogs that once mated for four months straight!"
        f "Though my parents don't want me to learn much about that right now."
        f "They say when I'm older I can."
        f "Some frogs swallow their tadpoles until they become frogs!"
        scene black with fade
        ni "Freddy went on for what felt like hours."
        ni "I didn't learn a lot about Freddy, but I think I learned a lot about frogs?"
        ni "Nothing that'll help us get out, unless the Game Master is a frog..."

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
    hide frog with dissolve
    jump postFTEHandler
