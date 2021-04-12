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
    b "I woke here a few minutes ago, followed shortly by..."
    show bert sad:
        xcenter .5
        linear 0.3 xcenter .75
    show sam:
        xcenter .25
    $ showchibi("bert", "sam")
    b "Sam, who was passed out over there against the wall."
    s "We need to figure out what's going on... What's your name?"
    m "My name..."
    n "My name is Dan."
    b "Alright Dan, surely you know {i}something{/i} about what's going on?"
    n "...I wish I did. I have no idea how I got here, or where here even is..."
    b "Yeah, same for us two."
    n "Is there an exit?"
    hide sam
    hide bert sad
    blank "I noticed a big steel door behind us."
    show bert sad with dissolve:
        xcenter .75
    show sam with dissolve:
        xcenter .25
    b "There's a door, we haven't tried it since we didn't want to leave you unconscious and alone."
    b "Let's try it now. Be careful though, we don't know what's past here."
    n "..."
    hide sam
    hide bert sad
    ni "We ran to the door and sure enough, it was unlocked."
    scene black
    ni "We were greeted by a very similar room, but many new faces."
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
    hide jenny with moveoutright
    i "Yea-yeah. Sid works."
    j "Do any of you know how you got here?"
    hide sid ind with moveoutleft
    show bert sad with dissolve
    b "The three of us who were in that room have no idea..."
    show bert sad:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with dissolve:
        xcenter .75
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine")
    z "Hey, don't start talking about serious stuff before I've introduced myself!"
    show catherine happy:
        xcenter .75
    c "I'm Catherine, and this is Sesame."
    ses "Mooeowowwwwwwwwwww!"
    hide catherine with moveoutright
    hide bert with moveinleft
    show kaiser ind with dissolve
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser")
    k "I'm Kaiser. I look forward to working with you all to get out of here."
    hide kaiser with moveoutright
    show drac ind with dissolve
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula")
    d "I'm Dracula. I would like to echo Kaiser's sentiment."
    show drac ind:
        xcenter .5
        linear 0.3 xcenter .75
    show sam ind with dissolve:
        xcenter .25
    s "Dracula... like the vampire."
    d "Yes, I'm Dracula."
    s "Somehow I don't think anyone here believes you."
    d "That's fine, the truth is the truth, it doesn't matter to me if you believe it."
    d "Besides, weren't you the one who wanted to skip past pleasantries?"
    d "We are in a potentially very precarious situation, it would seem."
    s "Fine. So that's everyone. Does anyone know how we got here?"
    s "Bert, Dan, and I all have no memories of being brought here."
    hide sam with moveoutleft
    hide drac with moveoutright
    show catherine ind with dissolve
    c "We were in the same situation. We were out on a walk, and next thing we knew, we're knocked out in that dusty room."
    hide catherine with dissolve
    ni "We took turns answering in a circle, and everyone had the same story."
    ni "Some memory of just living our lives, and then suddenly being in this place."
    ni "For me it was being in the prison cell, being told I was about to be let out."
    ni "No memory of losing consciousness or being transported, it just ended there."
    show sam ind with dissolve
    s "Well, looks like no one has any idea what's going on."
    s "Have we explored this building? Is there even anything to explore?"
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show jenny ind with moveinright
    j "Hold up, seems like it's not just the nine of us."
    j "Another group is coming in."
    blank "A kid, woman, and man walked in."
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula", "lauren", "freddy", "shahar")
    hide jenny with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    z "Guessing the rest of you are just as confused and clueless as we are?"
    s "Yeah. We were about to try to find ways out. Your names?"
    o "Lauren."
    hide sam with moveoutleft
    show freddy ind with moveinleft:
        xcenter .25
    o "The kid's name is Freddy, though he goes by Froggy."
    f "H-hi..."
    o "He's a bit shaken up, as I'm sure we all are."
    hide freddy with moveoutleft
    show sam ind with moveinleft:
        xcenter .25
    s "And the... bare-chested guy?"
    hide lauren with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "Name's Shahar lad. The finest pirate on the seven seas!"
    n "..."
    s "..."
    s "Are we sure this isn't some elaborate prank?"
    h "Prank? 'ere's nothing funny or foolish 'bout piracy me boy."
    s "Alright, sure, Shahar the pirate."
    hide shahar with moveoutright
    hide sam with moveoutleft
    ni "We did another round of introductions for the newcomers."
    show sam with dissolve
    s "Okay, unless another group shows up, let's try to look around and find-"
    hide sam with dissolve
    blank "A whirring noise cut Sam off."
    scene bg start2 with fade
    blank "A screen slowly lowered, and everyone's attention turned to it."
    #TODO: Add pretty pictures to help explain game
    scr "Welcome. At this point, everyone should have arrived."
    scr "This screen cannot hear or react to anything you say. Questions will not be answered."
    scr "The game you all have been brought here to play will now be explained."
    scr "There are twelve of you. Eleven were unwillingly chosen to participate."
    scr "The remaining person is the mastermind that organized this game, who will also participate."
    scr "The identity of the mastermind will not be revealed."
    scr "The goal of the game is simple."
    scr "Kill the mastermind."
    scr "The game will be played in rounds."
    scr "Each round, one of you who is not the mastermind will be chosen."
    scr "The chosen individual must kill someone, who they think is the mastermind."
    scr "If they kill the mastermind, the game ends and the remaining participants will be let free."
    scr "If they kill someone who is not the mastermind, the participants will investigate the murder."
    scr "After investigating, the participants will discuss and vote on who they think the murderer is."
    scr "If they vote for the murderer correctly, the murderer will be killed."
    scr "If they vote incorrectly, everyone but the murderer and mastermind will be killed, and the game ends."
    scr "A chip has been planted in each of your heads, capable of killing you instantly."
    scr "This chip will be used to resolve the outcome of the vote."
    ni "Does technology like that really exist?"
    ni "And when did they plant the chip?"
    scr "Each round of the game will take place in a different location."
    scr "The chip will also be used to keep you unconscious as you are transported between locations."
    scr "As proof of this, you will soon be knocked unconscious and transported to the first location, to play the first round of the game."
    ni "...what?"
    ni "How would we even know who to kill?"
    ni "This game... it's so much to process."
    ni "There's no clear path to victory."
    ni "Looking around, it was clear others were just as shocked."
    show shahar mad with dissolve
    b "A... a game where we all have to bloody kill each other?"
    hide shahar with dissolve
    show drac oh with dissolve
    d "This is... inhumane, to say the least."
    d "Surely no one here is capable of murder."
    ni "..."
    hide drac with dissolve
    scr "You may be scared to kill someone who isn't the mastermind."
    scr "You may feel sorry when someone dies."
    scr "But there is one thing you should know before you are transported to the first round of the game."
    scr "Everyone who dies in the course of the game..."
    scr "Their endings are deserved."
    ni "My vision yet again started to fade to black..."
    scene black with fade
