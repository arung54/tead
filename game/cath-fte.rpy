
label cathAsk0:
    scene bg trainback
    show catherine happy with dissolve
    c "Achoo! Whew, sure is dusty back here."
    ni "I should go talk to Bert."
    call screen backCar with dissolve


label cathAsk1:
    scene bg trainback
    show catherine happy with dissolve
    c "Hey Dan!"
    blank "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "Cool!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
            call screen backCar with dissolve

label cathHang:
    if fte_cath == -1:
        c "Hey Dan."
        ses "Mrow!"
        c "Sesame says hi too!"
        n "Hey."
        c "This is a really lame situation, right?"
        n "Lame's definitely one way to think about it."
        c "Well, Sesame and I are trying to think about this like a vacation!"
        n "A vacation?"
        c "Yeah!"
        c "After all, we're stuck right now, so we might as well try to enjoy ourselves."
        n "Don't you think the situation is a little... grim to be trying to enjoy yourself?"
        c "Well, maybe!"
        c "But it can't hurt."
        c "I'll mostly just pretend to be sad around everyone else so I don't seem crazy, but..."
        c "Not having to study or work? And getting to hang out on this train?"
        c "Yes please! Sign me up!"
        ses "Mow mrowww!"
        ni "... is she really this happy-go-lucky?"
        show catherine ind
        c "Okay okay, don't get me wrong, I'm a bit worried."
        c "But honestly, I've learned to always take things in stride."
        c "Sesame and I have been through some sticky situations before, and they always work out!"
        n "Sticky situations?"
        c "Nothing as odd as this, but..."
        c "The life-sized foosball match definitely came close!"
        ses "*Sesame seemed to nod in agreement.*"
        n "Wait, what?"
        show catherine happy
        c "Long story!"
        c "Maybe sometime I'll go through the whole thing with you."
        c "Anyway, this has been nice. I'm glad you chose to talk with us."
        n "M-me too."
        scene black with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."


    $fte_cath += 1
    hide catherine with dissolve
    jump postFTEHandler
