
label sidAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show sid ind with dissolve
    i "Hmm. I wonder what the password could be..."
    ni "I should go talk to Bert."
    hide sid with dissolve
    call screen midCar with dissolve


label sidAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show sid ind with dissolve
    i "Hey Dan!"
    blank "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Let's do it."
            call sidHang
        "Maybe later":
            hide sid ind with dissolve
    call screen midCar with dissolve

#Mansion 1
label sidAsk2:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 4)
    show sid happy with dissolve
    i "Wow! That bed was so comfy! Can I take it home?!"
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Yeah! Let's chat! I'm so well-rested and energetic!"
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen masterBedroom

#Mansion 2
label sidAsk3:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 1)
    show sid happy with dissolve
    i "First a fancy bed, then a fancy meal... I'm in heaven!"
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Okay, but we better not be late to the meal!"
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen masterBedroom

#Mansion 3
label sidAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show sid happy with dissolve
    i "Normally I'm so hungry... I'm gonna eat so much today!"
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Okay, but don't get mad if my tummy rumbles!"
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen dining

#Hospital 1
label sidAsk5:
    scene bg hospkitchenwindow at bg
    show hospwindowoverlay
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show sid ind at inwindow behind hospwindowoverlay
    i "Aw man... I miss the fancy food... it's like I'm back at home now."
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "I don't know if I want to talk to you after that meal... but fine."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen hospKitchen

#Hospital 2
label sidAsk6:
    scene bg hospkitchenwindow2 at bg
    show hospwindowoverlay2
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show sid ind at inwindow behind hospwindowoverlay2
    i "I usually never make food... I hope it's edible."
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Sure, I'll talk while chopping veggies."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen patientcommons

#Bank 1
label sidAsk8:
    scene bg bankvault
    $ statusnt("Bank Hallway", "bert", ch = 4, sun = 2)
    show sid ind with dissolve
    i "Hm... there's gotta be a way to figure out this safe."
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Okay, but only if you tell me your birthday! ...Or not, it's fine."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen hall with dissolve
#Bank 2
label sidAsk9:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 1)
    show sid ind with dissolve
    i "20/961... is it really that low?"
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Yeah, let's talk about our birthdays! ...Or something else."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen lobby with dissolve

#Bank 3
label sidAsk10:
    scene bg banklobby1
    $ statusnt("Bank Hallway", "bert", ch = 4, sun = 2)
    show sid ind with dissolve
    i "Freddy's so lucky to have rich parents..."
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "I wonder if I can get Freddy to give me money once we're out of here..."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen lobby with dissolve

label sidAsk11:
    scene bg pentkitchen2
    $ statusnt("Dining Room", "bert", ch = 5, sun = 1)
    show sid ind with dissolve
    i "I found a rope! But it's not long enough to reach the ground..."
    bi "Should I talk to Sid?"
    menu:
        "Spend time with Sid":
            i "Sure, but we gotta keep searching."
            call sidHang
        "Maybe later":
            hide sid with dissolve
    call screen pentDining with dissolve

label showSidIndFTE:
    if ftecounter == 5:
        show sid ind at inwindow behind hospwindowoverlay
    elif ftecounter == 6:
        show sid ind at inwindow behind hospwindowoverlay2
    else:
        show sid ind
    return

label showSidMadFTE:
    if ftecounter == 5:
        show sid mad at inwindow behind hospwindowoverlay
    elif ftecounter == 6:
        show sid mad at inwindow behind hospwindowoverlay2
    else:
        show sid mad
    return

label showSidHappyFTE:
    if ftecounter == 5:
        show sid happy at inwindow behind hospwindowoverlay
    elif ftecounter == 6:
        show sid happy at inwindow behind hospwindowoverlay2
    else:
        show sid happy
    return

label showSidSmileFTE:
    if ftecounter == 5:
        show sid smile at inwindow behind hospwindowoverlay
    elif ftecounter == 6:
        show sid smile at inwindow behind hospwindowoverlay2
    else:
        show sid smile
    return

label sidHang:
    if fte_sid >= 3:
        bi "Hm, on second thought, I've talked to Sid plenty... I should talk to someone else."
        hide sid with dissolve
        return

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
        scene bg trainmid with dissolve
        show sid ind with dissolve
        i "Are my arms supposed to feel like jello?"
        n "Yeah! But in a good way."
        i "..."
        n "You'll get used to it if you keep it up."
        i "Wait, I have to do that {i}again?{/i}"
        n "It's the only way to get stronger! We can train together."
        i "D-deal!"
        play sfx "audio/pophearts.mp3" volume .25
        show pophearts:
            xcenter .5
            ycenter .5
        ni "He's a good kid, just... needs a little guidance."
        n "You'll be twice my size before you know it."
        hide pophearts
        i "You bet! Thanks Dan."
        hide sid ind with moveoutright
        ni "I don't have many friends here, and that's okay."
        ni "I'm glad I can be a positive influence on Sid."
        hide screen status_screen
        scene black
        with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."

    if fte_sid == 0:
        i "It’s so strange not being with my family."
        b "It seems like you’re very close to them."
        i "Yeah. This is the first time I’ve ever been away from them."
        i "Normally, my whole life revolves around my family."
        i "Bringing my little sister to school, working at our shop after school, cooking for my parents..."
        i "I know some people here are looking down on me for my record, but..."
        i "Everything {i}bad{/i} I’ve ever done was for them, you got that?"
        i "I just... miss them."
        b "I’m sure they miss you too, Sid."
        b "We’re going to figure this out and get out of here."
        i "Y-yeah! I know we will."
        i "But..."
        i "I’ve also been thinking more about what Dan said to me, before..."
        bi "It looks like he can’t get the words out."
        b "What did he say?"
        i "He told me that I’m still young, which I’m not..."
        i "But also that I can do anything I want with my life."
        i "Travel, do exciting things, meet new people."
        i "But... if I do what I want instead of what my family needs..."
        i "After everything my parents have sacrificed, isn't that selfish?"
        b "I mean... I can't say I've been in your situation before Sid."
        b "But... I'm sure, to some extent, your parents made those sacrifices because they want the best for you."
        i "Yeah..."
        i "But... I don't just want the best for me."
        i "I want the best for {i}us{/i}."
        i "For me, and for my family."
        call showSidMadFTE
        i "The Game Master has no idea who he's up against!"
        i "I'm not just fighting for me, I'm fighting for my family!"
        i "I’m going to give it my all to get out of here, and then keep giving it my all!"
        hide screen status_screen
        scene black
        with fade
        bi "Sid ran off in a hurry."
        bi "He sure is ambitious."
        bi "There's definitely more to him than the \"little punk\" personality he puts on."

    if fte_sid == 1:
        show sid ind
        i "Hey, Bert? I’ve been thinking..."
        i "Maybe you could teach me some things."
        b "Teaching you things? Like what?"
        i "Well I realized how much time I’m wasting with all this."
        i "I’m going to fall behind all my classmates and I won’t be able to support my family if I’m struggling in school."
        bi "Sid’s love for his family really is unrivaled."
        i "So I need you to teach me! Math, science, you name it!"
        i "All that nerdy stuff! You’re a nerd, right?"
        bi "I’ll try to take that as a compliment..."
        b "Sure, let’s do it."
        blank "They spent a long time learning about pre-calculus."
        i "I think I’m starting to get it."
        i "To derive the expression, I slash the exponents and then steal the last term."
        bi "He didn’t have to use the words {i}slash{/i} and {i}steal{/i}, but I think he’s starting to get it."
        i "Hey, Bert?"
        i "Th-thank you."
        b "Of course! It’s what friends are for."
        bi "He had quite a visual reaction to the word \"friends\"."
        bi "Maybe he hasn’t heard it much..."
        i "So um, now that I know how to do derivatives, can I become a big banker?"
        b "Huh?"
        i "Well, I heard that like, recessions happened because big bankers traded derivatives."
        i "And well, they have a lot of money, and with that money I could support my family..."
        b "Oh, that's a different type of derivative."
        i "Oh..."
        b "...But, I bet a lot of those bankers did well in pre-calculus too!"
        call showSidSmileFTE
        i "Oh, yeah, that's right!"
        i "I'm going to become a smart nerdy rich banker!"
        i "Next time you see me, I’ll be like Albert Einstein!"
        hide sid with moveoutleft
        bi "...He ran off, but I'm not exactly sure where to."
        hide screen status_screen
        scene black
        with fade
        bi "Thinking about my conversation with Sid some more..."
        bi "I'm worried I might cause him to gamble on the stock market in a few years."
        bi "It's a good thing there's no internet here..."
        bi "Oh well, I'm glad to help him with his ambitions for his family, in whatever way I can."

    if fte_sid == 2:
        show sid ind
        i "Bert, um, can you teach me some more school stuff?"
        b "Sure, do you want to learn some basic economics?"
        b "After all, you'll need it to become a big banker!"
        i "Oh, I was hoping I could ask you about law instead."
        b "Law?"
        b "Well, you're in high school, so I guess we should start with the amendments..."
        i "Um, not that type of law..."
        i "I was thinking more... lawsuits and stuff."
        b "Lawsuits?"
        b "Like, famous court cases?"
        i "Uh, depends."
        i "Are there any famous court cases about rich people suing poor people?"
        b "Well, none that you'd need to study in high school..."
        b "...Is there a specific lawsuit you have in mind, Sid?"
        i "Well, uh, let's just say I had a friend."
        i "And the friend got sued by a rich company for an innocent mistake."
        i "Is there anything I could do to help that friend?"
        b "I mean... I've heard stories like this."
        b "Big companies suing people for violating their copyright."
        b "Usually not because they want the money, but just to send a message..."
        b "But it's never happened to me or anyone I knew."
        b "And I'm not a lawyer, so I don't know what to tell you."
        i "Oh... well, thanks anyway Bert."
        b "Yeah... is there anything else I can teach you about?"
        i "...Why do people with money get so many advantages?"
        b "Huh?"
        b "I mean... I'm not really sure how to answer that."
        b "Money is power, I don't know if there's much more to it."
        call showSidMadFTE
        i "Grr... this is why I hate adults."
        i "At school, the kids who are cooler or punch harder are the rulers."
        i "But even if you're not one of those two..."
        i "A ragtag misfit like me can survive."
        call showSidIndFTE
        i "...Not that I'm a kid."
        call showSidMadFTE
        i "But adults are so different..."
        i "I thought they'd be more mature, but they're worse than kids."
        i "They're willing to exploit each other and ruin lives for their own greed!"
        b "I mean, it's true that the worst adults are really awful..."
        b "But Sid, I think a lot of adults are good."
        b "It's just that, the people who are good are harder to notice or remember."
        b "It's like, if someone buys you a present you might forget about it in a year."
        b "But if someone's mean to you as a kid, you won't forget for the rest of your life."
        b "Humans are just... wired to focus on negative things, I guess."
        i "Hm..."
        call showSidIndFTE
        i "You may be right... but I still think all adults are punks."
        call showSidHappyFTE
        i "But that doesn't matter, because I'm going to grow up and be the biggest punk of them all!"
        i "My family will walk around like they're cool kids on a schoolyard!"
        i "And it'll all be because of the ass I kick when I get out of here!"
        hide screen status_screen
        scene black
        with fade
        bi "We chatted some more about Sid's plans for world domination."
        bi "In a place where it's easy to give up hope, it's nice to have someone like Sid to remind us to be ambitious."

    $fte_sid += 1
    $persistent.fte_sid = max(persistent.fte_sid, fte_sid)
    hide sid with dissolve
    jump postFTEHandler
