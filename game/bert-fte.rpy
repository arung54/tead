
label bertAsk0:
    scene bg trainmid
    show bert happy with dissolve
    b "Sandwiches aren't bad, but I really miss food from home..."
    blank "Should I talk to Bert?"
    menu:
        "Spend time with Bert":
            b "Sure, I guess hanging out will get my mind off how hungry I am."
            jump bertHang
        "Maybe later":
            hide bert with dissolve
            call screen midCar


label bertAsk1:
    scene bg trainmid
    show bert happy with dissolve
    b "Hey Dan! Want to chat some more?"
    blank "Should I talk to Bert?"
    menu:
        "Spend time with Bert":
            b "Cool! I'll try not to talk about food this time."
            jump bertHang
        "Maybe later":
            hide bert with dissolve
            call screen midCar

label bertHang:
    if fte_bert == -2:
        b "I don't know what it is, but I've really been craving pizza."
        b "Pizza with pineapple and pepperoni. And some garlic bread on the side."
        n "Why pineapple on pizza though?"
        b "Hmm... it adds a nice sweet yet acidic flavor that compliments the meat and cheese."
        n "Won't thinking about food in this much detail just make you hungrier?"
        b "I guess so?"
        b "But at the same time, if I'm thinking about food I'm not freaking out."
        b "And thinking about what I miss from home gives me motivation to work to get out."
        n "That's... a rather optimistic take, I guess."
        b "C'mon, surely you miss your old life too!"
        b "Tell me, what will your first meal be when you get out?"
        n "Don't you mean {i}if{/i} I get out?"
        show bert sad
        b "C'mon, answer the question."
        n "I don't think you're gonna like my answer."
        b "Try me. Maybe you'll be surprised."
        n "Honestly, I haven't had anything but gruel in... years."
        b "...gruel?"
        n "Basically something meant for sustenance like oatmeal but boiled."
        b "Oh... why did you only eat that?"
        n "It's not like I had a choice."
        b "..."
        n "Yeah... again, didn't think you were gonna like my answer."
        b "Well, it's not the best answer, but I think I at least learned something about you."
        show bert happy
        b "And that's a positive in its own way!"
        ni "I'm envious of his optimism..."
        ni "...it won't do much good to be on bad terms with everyone, so maybe I'll try to play along."
        n "...though in my childhood I really liked deep dish pizza."
        b "Oh?"
        n "Yeah. our local pizza place sold thin crust by the pizza and deep dish by the slice."
        n "I couldn't finish a whole pizza by myself and I liked weird toppings."
        n "So I'd get deep dish so I could eat it without sharing."
        b "Weird toppings?"
        n "I loved anchovies as a kid."
        n "These days... I've wisened up a bit."
        b "Understandable. I imagine after eating gruel that much salt is shocking."
        n "..."
        show bert sad
        b "...Sorry, probably shouldn't have brought that up again."
        n "No, it's fine."
        show bert happy
        b "Still, thanks for talking to me!"
        b "It'll only help us work together in the future!"
        scene black with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."


    if fte_bert == -1:
        b ""

    $fte_bert += 1
    $ftecounter += 1
    hide bert with dissolve

    if ftecounter - 1 == 0:
        call screen frontCar #replace w/ jump to free time 2
