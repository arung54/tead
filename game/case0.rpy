label start:
    scene black
    warden "Dan Scagnelli, wake up."
    m "No... don't want to wake up for another day of this"
    warden "Dan Scagnelli, wake up. That is an order."
    m "Urgh..."
    scene bg phall with dissolve 2.0
    warden "Dan Scagnelli, do not make me repeat myself."
    n "I'm up, I'm up. Just getting used to the light."
    ni "I realized how dumb I sounded, light was barely filtering into the cell."
    ni "Seems like it's only sundown now."
    n "What time is it? Why am being woken up so early?"
    warden "Dan Scagnelli. You're being let go."
    n "Huh?"
    warden "Your sentence ends today."
    n "I... I thought I was stuck here for a few more years?"
    warden "I don't know what to tell you, just following orders."
    warden "There's someone waiting for you out front, don't make them wait."
    ni "The warden handed me my civilian clothes."
    ni "I could barely remember how long it had been since I last wore these."
    ni "After I'd changed, he unlocked the cell, cuffed me and we made our way out."
    scene bg pfront with fade
    ni "A stranger was there to greet me."
    ni "I wish I knew who it was, but they had concealed their face."
    ni "Surely no reasonable prison would let someone like this bail a prisoner out?"
    n "Who are you?"
    z "Don't worry about that for now. Let's get going."
    n "Why did you do this for me?"
    z "Questions later, when we're in the car."
    z "Here's a sandwich, eat it, you'll want some energy where we're headed."
    n "Which is?"
    z "Questions in the car."
    n "Surely you can explain while we're walking."
    z "That's not really a good way to talk to someone who got you out. Eat while walking."
    ni "I started eating."
    ni "The stranger pushed me when they saw I was standing still."
    z "I said eat while walking."
    ni "What was so urgent that it needed me to be pulled out of prison and rushed to a car?"
    ni "We headed outside, and for the first time in ages I was excited to see the glorious sun and greenery."
    scene black
    ni "Like a poorly edited TV show, my vision faded to black as we stepped outside."
    ni "Only it never faded back to light."
    ni "I lost vision, there was something tingling in my mouth."
    ni "Was there something in the food?"
    ni "My thoughts started to fade slowly. The last thing I can remember thinking..."
    ni "Whoever this is, they aren't here to save me."

    play sfx "audio/heartbeat.mp3"
    pause 1.0
    play sfx "audio/heartbeat.mp3"
    pause 1.0

    scene black
    blank "....."
    blank "........."
    blank "If I just ran, I would've gotten out."
    blank "A shame, really."
    show bg start with fade:
        alpha .1
    m "{i}Where... Where am I?{/i}"
    m "{i}I can't... remember how I got here...{/i}"
    m "{i}My head is throbbing...{/i}"
    m "{i}I see some people laying down over there.{/i}"
    m "{i}Or are they... bodies?{/i}"

    scene black
    m "........"
    m "{i}I think I passed out again...{/i}"
    m "{i}Have to... get up...{/i}"
    scene bg start
    m "{i}.....!{/i}"
    z "It looks like he's awake."
    show sam with dissolve
    z "Hey - are you alright?"
    m "Who are you? Where am I?"
    hide sam
    show bert sad with dissolve
    z "I guess that means he doesn't know anything more than we do."
    b "You can call me Bert."
    $ showchibi("bert")
    b "I woke here a few minutes ago, followed shortly by,"
    show bert sad:
        xcenter .5
        linear 0.3 xcenter .75
    show sam:
        xcenter .25
    $ showchibi("bert", "sam")
    b "Sam, who was passed out over there agianst the wall."
    s "We need to figure out what's going on... What's your name?"
    m "My name..."
    n "My name is Dan."
    b "Alright Dan, surely you know {i}something{/i} about what's going on?"
    n "...I wish I did. I have no idea how I got here, or where here even is..."
    n "Is there an exit?"
    hide sam
    hide bert sad
    blank "I noticed a big steel door behind us."
    blank "The doorknob wouldn't turn, and there's no key hole."
    show bert sad with dissolve:
        xcenter .75
    show sam with dissolve:
        xcenter .25
    s "Yeah, the door won't budge. Even scarier than that though,"
    s "I think that's one way glass along the wall..."
    b "I've been trying to whisper, there's a chance someone is watching us."
    n "Well? What the hell are we going to do then?"
    n "Are we just stuck in here like animals?"
    play sound "beep.mp3"
    centered "{size=+30}BEEP!{/size}"
    play sound "butt.mp3"
    centered "{size=+30}CLICK!{/size}"
    n "What was that?"
    s "Quick, check the door!"
    b "Be careful! We don't know what's past here."
    n "..."
    hide sam
    hide bert sad
    blank "We ran to the door and sure enough, it was unlocked."
    scene black
    blank "We were greeted by a very similar room, but many new faces."
    scene bg startmeet
    $ showchibi("bert", "sam")
    show sam with dissolve
    s "Let's just get all the pleasantries out of the way."
    s "Everyone, introduce yourselves and if you know anything. I'm Sam."
    hide sam
    $ showchibi("bert", "sam", "stella")
    show stella ind
    t "Certainly. I am Stella Cantoire, you may know of me from the Cantoire Group."
    show stellachibi:
        zoom 1.5 xpos 20 ypos 116
    t "I dont know how I got here, but I have work to do, so let's finish up whatever this is quickly."
    show stella ind:
        xcenter .5
        linear 0.3 xcenter .75
    $ showchibi("bert", "sam", "stella", "sid")
    show sid ind:
        xcenter .25
    z "I... Don't think it's our choice, ma'am? Where even are we?"
    t "Don't you dare call me ma'am, I'm young enough to be your sister. Hmph."
    hide stella ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    $ showchibi("bert", "sam", "stella", "sid", "jenny")
    j "I'm Jenny. Your nametag says Sid, can we call you that?"
    show jennychibi:
        zoom 1.5 xpos 20 ypos 164
    i "Yea-yeah. Sid works."
    show sidchibi:
        zoom 1.5 xpos 20 ypos 212
    hide jenny ind
    show jenny happy:
        xcenter .75
    j "Not sure where we are though! It's kinda exciting, right?"
    j "Like an escape room!"
    hide jenny happy with moveoutright
    i "..."
    hide sid ind with moveoutleft
    show bert sad with dissolve
    b "I mean, maybe, but we still have no idea how we ended up here..."
    n "Yeah, it's more worrying than exciting."
    show bert sad:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with dissolve:
        xcenter .75
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine")
    c "I'm Catherine, and this is Sesame."
    show catherinechibi:
        zoom 1.5 xpos 20 ypos 260
    ses "Mooeowowwwwwwwwwww!"
    c "I agree, Sesame. We're scared, what's going on?"
    c "We were out on a walk, and next thing we knew, we're knocked out in a dusty room."
