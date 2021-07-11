
label bertAsk0:
    scene bg trainfront1
    show bert happy with dissolve
    b "Sandwiches aren't bad, but I really miss food from home..."
    blank "Should I talk to Bert?"
    menu:
        "Spend time with Bert":
            b "Sure, I guess hanging out will get my mind off how hungry I am."
            jump bertHang
        "Maybe later":
            hide bert with dissolve
            call screen frontCar


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
        n "Basically something meant for sustenance like oats, but boiled."
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
        n "Hey Bert, we talked about the food we'd eat when we get out."
        n "But do you really think we're going to get out?"
        show bert sad
        b "Geez, that's a heavy question to start a conversation with."
        n "Sorry, I'm not good at conversation."
        b "Nah, it's fine. Just a bit of a ramp up from pizza."
        b "But we... kill the mastermind, then we get out, right?"
        ni "He hesitated before the word killed."
        b "Imagine we work together to figure out who the mastermind is."
        b "It'll require some hard honest conversations about ourselves, of course."
        show bert happy
        b "But we could maybe get out in just a few hours if we do!"
        n "How would we be able to identify the mastermind in just a few hours of talking though?"
        n "We don't know their motives for playing this game..."
        n "We don't know how we ended up here..."
        n "We don't even know where we are!"
        show bert sad
        b "You're not wrong."
        b "But not all problems can be solved like a homework problem in a few minutes."
        b "Unless the mastermind picked 12 arbitrary people, there has to be some answer."
        b "We just have to work hard and work together to find it."
        b "The alternative is we just sit around hoping things work out."
        n "Surely it won't be that easy."
        n "If I was running a game like this, I would do everything to disguise myself."
        n "The person running this game has the ability to knock us out at will."
        n "They commandeered this train all by themselves!"
        n "There's no way they would be careless enough to let us find out who they are on day one."
        b "...You're being kind of a bummer right now."
        n "Huh?"
        b "Being pessimistic isn't going to get us out of here."
        b "If we just lay down and accept our fate, then our chances of getting out are smaller."
        b "It feels like you're not looking for sympathy here."
        b "So all you're doing is dragging me down with you."
        n "...That's fair, I guess."
        n "Earlier, you hesitated to say \"killed\""
        b "...You're not very good at pivoting topics, are you?"
        n "Like I said, not good at conversation."
        b "Yeah, I don't like the word killed."
        b "I have a... complicated relationship with murder and things like that."
        b "But I don't really wanna talk about it."
        ni "I think I have may have crossed some lines..."
        b "..."
        n "..."
        n "I guess we should meet up with the others now."
        b "Sure."
        scene black with fade
        ni "I guess I understand Bert better now. Not sure if we're closer, though."

    $fte_bert += 1
    hide bert with dissolve
    jump postFTEHandler
