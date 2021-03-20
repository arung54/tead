
label sidAsk0:
    scene bg trainfront
    show sid ind with dissolve
    i "I feel like I'm so close to getting this password...Focus, Sid, focus!"
    ni "I should go talk to Bert."
    call screen frontCar


label sidAsk1:
    scene bg trainfront
    show sid ind with dissolve
    i "Hey Dan!"
    blank "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Let's do it."
            jump sidHang
        "Maybe later":
            hide sid ind with dissolve
            call screen midCar

label sidHang:
    if fte_sid == -1:
        n "What's up Sid?"
        i "Hmm... well..."
        i "I was just thinking about what you said last night."
        i "You called me 'more of a man than you are.'"
        i "D-did you really mean that?"
        i "I mean, look how big and strong you are... I'm just..."
        n "Being a man isn't about muscles or height."
        n "It's about making tough decisions and protecting those around you."
        i "Is that what you do?"
        n "I'm not as good at is as I'd like..."
        n "But I try my best, and I know that you do too."
        n "That's why I called you a man."
        i "It doesn't seem like the others think that."
        i "They think I'm just some street kid."
        n "You shouldn't worry about what others think of you Sid."
        i "Maybe you're right, but..."
        i "I still want to big muscles like you!"
        ni "..."
        n "Alright, well what are you waiting for?"
        n "Let's do some pushups!"
        i "O-okay!"
        scene black with dissolve
        n "One, two, three, 28! One, two three, 29! One, two, three, 30!"
        i "I can't feel my arms!"
        n "Keep going! You're doing great!"
        blank "They worked out for a while."
        scene bg trainfront with dissolve
        show sid ind with dissolve
        i "Are my arms supposed to feel like jello?"
        n "Yeah! But in a good way."
        i "..."
        n "You'll get used to it if you keep it up."
        i "Wait, I have to do that {i}again?{/i}"
        n "It's the only way to get stronger! We can train together."
        i "D-deal!"
        ni "He's a good kid, just... Needs a little guidance."
        n "You'll be twice my size before you know it."
        i "You bet! Thanks Dan."
        hide sid ind with moveoutright
        ni "I don't have many friends here, and that's okay."
        ni "I'm glad I can be a positive influence on Sid."
        scene black with fade
        ni "I went back to see the others."


    if fte_sid == 0:
        i "It’s so strange not being with my family."
        b "It seems like you’re very close to them."
        i "Yeah. This is the first time I’ve ever been away from them."
        i "Normally, my whole life revolves around my family."
        i "Bringing my little sister to school, working at our shop after school, cooking for my parents…"
        i "I know some people here are looking down on me for my record, but…"
        i "Everything {i}bad{/i} I’ve ever done was for them, you got that?"
        i "I just… Miss them."
        b "I’m sure they miss you too, Sid."
        b "We’re going to figure this out and get out of here."
        i "Y-yeah! I know we will."
        i "But…"
        i "I’ve also been thinking more about what Dan said to me, before…"
        bi "It looks like he can’t get the words out."
        b "What did he say?"
        i "He told me that I’m still young - which I’m not - but also that I can do anything I want with my life."
        i "Travel, do exciting things, meet new people."
        i "I want that. I want that!"
        i "For me, and for my family."
        i "When I get out of here, I’m going to give it my all!"
        blank "Sid ran off in a hurry."
        bi "He sure is ambitious."
        bi "At least he’s opening up a little bit."


        scene black with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."

    if fte_sid == 1:
        i "Hey, Bert? I’ve been thinking…"
        i "Maybe you could teach me some things."
        b "Teaching you things? Like what?"
        i "Well I realized how much time I’m wasting with all this."
        i "I’m going to fall behind all my classmates and I won’t be able to support my family if I’m struggling in school."
        bi "Sid’s love for his family really is unrivaled."
        i "So I need you to teach me! Math, science, you name it!"
        i "All that nerdy stuff! You’re a nerd, right?"
        bi "I’ll try to take that as a compliment…"
        b "Sure, let’s do it."
        scene black with dissolve
        blank "They spent a long time learning about pre-calculus."
        i "I think I’m starting to get it."
        i "To derive the expression, I slash the exponents and then steal the last term."
        bi "He didn’t have to use the words {i}slash{/i} and  {i}steal{/i}, but I think he’s starting to get it."
        i "Hey, Bert?"
        i "Th-thank you."
        b "Of course! It’s what friends are for."
        bi "He had quite a visual reaction to the word ‘friends’."
        bi "Maybe he hasn’t heard it much…"
        i "Next time you see me, I’ll be like Albert Einstein!"
        blank "He ran off in a hurry."
        hide sid ind
        bi "I feel like we’re growing closer… Slowly."

    $fte_sid += 1
    $ftecounter += 1
    hide sid ind with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after free time 2
