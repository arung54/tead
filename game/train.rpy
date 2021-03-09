label go:

    #jump frontcar1
    #show screen button_overlay
    scene black
    n "{i}Was I... Dreaming?{/i}"
    n "{i}I did tend to get nightmares in there...{/i}"
    n "{i}...{/i}"
    n "{i}Unless...{/i}"
    scene bg trainmid
    show cydney ind
    with fade
    o "Hey - wake up already."
    n "......."
    n "Where are we? How did we get here?"
    show cydney ind:
        xcenter .5
        linear 0.3 xcenter .75
    o "I mean, look around. Where do you think we are?"
    n "It's a... train car."
    hide cydney ind with dissolve
    show sam
    s "A {i}moving{/i} train car too. We're headed somewhere."
    hide sam with dissolve
    blank "I went to check the window."
    image forest run:
        contains:
            "windowviewout.png"
            xpos -9.0
            linear 555.0 xpos 0.0
            repeat
    show forest run
    show windowview
    with fade
    n "Wow..."
    n "There's... Nothing out there."
    hide forest run
    hide windowview
    with fade
    show shahar ind with dissolve
    h "Laddies, it feels like the room is moving!"
    n "That's how trains work."
    n "Have you never been on a train before?"
    h "Blimey, you're right! We {i}are{/i} movin'!"
    hide shahar ind with moveoutright
    n "..."
    show catherine ind
    c "Oh, Dan's finally awake? I think that's everyone then!"
    show catherine ind:
        xcenter .5
        linear 0.3 xcenter .75
    show drac ind:
        xcenter .25
    d "Yes. All 12 of us are here."
    d "13 if you include your... Rodent."
    ses "Mrow!"
    n "..."
    hide catherine ind
    hide drac ind
    with dissolve
    #show screen test

    show sid ind with dissolve
    i "How did we even get here?"
    i "A minute ago we were trapped in that lab."
    n "That's a good question..."
    hide sid ind
    show jenny ind
    j "Maybe we were on the train the whole time?"
    hide jenny ind
    show bert sad
    b "I don't think so... Those rooms were pretty wide."
    b "I don't think they could have fit in a train car."
    b "Dan, what do you think?"
    n "Me? Hmm..."
    menu:
        n "{i}How did we get here?{/i}"

        "Maybe we got on board ourselves.":
            hide bert sad
            show drac ind
            d "I refuse to accept that."
            hide drac ind
            show stella ind
            t "The vampire's right, there's no way we got onboard ourselves."
            t "We'd obviously remember that."
            t "We must have been knocked out and moved here somehow."
            n "But how did they knock all of us out like that?"

        "We must have been moved here.":
            hide bert sad
            show drac ind
            d "Yes, the culprit must have knocked us out and moved us here."
            d "Otherwise we'd remember it."
            hide drac ind
            show stella ind
            t "I don't remember boarding myself, that's for sure."
            t "How did they manage to knock all of us out though?"

    hide stella ind with dissolve
    show kaiser ind with dissolve
    k "It seems obvious enough, yes?"
    n "What do you mean?"
    show kaiser ind:
        xcenter .5
        linear 0.3 xcenter .75
    show cydney ind with moveinleft:
        xcenter .25
    o "Kaiser's right... Think back to what the monitor told us."

    ###FLASHBACK###
    show black
    n "flashback to part about chips in our brain, have to cooperate etc"
    hide black

    n "You think the chips knocked us out somehow?"
    hide kaiser ind
    hide cydney ind
    with dissolve
    show sam with dissolve
    s "It's the only logical explaination."
    s "Either way, I don't think it's worth spending any more time on."
    n "Right. We should start exploring the train."
    show sam:
        xcenter .5
        linear 0.3 xcenter .75
    show bert happy with moveinleft:
        xcenter .25
    b "Maybe we can find the conductor!"
    b "He could stop the train for us."
    s "It's worth a shot."
    b "That's the spirit! Poggers!"
    n "..."
    show sam:
        xcenter .75
        linear 0.3 xcenter .85
    show bert happy:
        xcenter .25
        linear 0.15 xcenter .15
    show frog ind with moveinbottom
    f "Wh-what should I do?"
    f "I'm just a frog..."
    s "I keep forgetting there's a kid here too..."
    hide sam with moveoutright
    hide bert happy with moveoutleft
    show frog ind:
        xcenter .5
        linear .3 xcenter .75
    show cydney ind with moveinleft:
        xcenter .25
    o "We can sit together, buddy. We can just hang out here."
    f "{i}*sniffle*{/i} Okay miss."
    hide frog ind with moveoutright
    show cydney ind:
        linear .3 xcenter .5
    o "I can watch him, I don't want a kid involved in... Whatever this is."
    n "Oh, thanks. I'm not great with kids myself."
    hide cydney ind
###########################################
###############INVESTIGATE#################
###########################################

    show stella ind
    t "I'll check behind the bar."

    hide stella ind with moveoutright
    show bert sad
    b "..."
    hide bert sad
    show bert happy
    b "There might be food back there though, and we're going to need to eat. I'll look with you."

    hide bert happy with moveoutright
    show frog sad
    f "...Ribbit... This is scary..."
    hide frog sad
    show cydney ind
    o "Hey it's ok! I'll stay with you, we can just sit here."
    hide cydney ind
    show frog sad
    f "...Okay."
    hide frog sad with moveoutleft
    show cydney ind
    o "Hehe, I used to baby sit in high school. I'll watch him."
    n "Oh, thank you. I'm not great with kids."

    hide cydney ind with moveoutleft
    show shahar ind
    h "Aye, I'll check the next car. To the front with me!"
    hide shahar ind with moveoutleft
    show sid ind
    i "I'll go with, the uh, pirate. Why is there a pirate here again?"
    hide sid ind with moveoutleft
    show jenny ind
    j "We should probably find out where we're going."
    j "I'm going straight to the front! Nobody try to stop me."
    hide jenny ind with moveoutleft
    show catherine happy
    c "Alright Sesame, we're going exploring!"
    ses "Moewwwwww!"
    hide catherine ind with moveoutleft

    show sam
    s "Okay, the rest of us can check the next car back."
    hide sam
    show drac ind
    d "Very well."
    hide drac ind
    menu:
        n "{i}Should I go with them?{/i}"

        "Yes":
            n "Alright."

        "No":
            n "I might just stay here..."
    show sam with dissolve:
        xcenter .75
    s "Hey, Dan..."
    s "Between you and me, I don't feel particularly comfortable being alone with him."
    show drac ind with moveinleft:
        rotate 45
        xcenter -.1
        ycenter .5
    n "With the, uh, vampire?"
    hide drac ind with moveoutleft
    s "Yeah. It'd be smarter of us to stay in groups of 3 or more."
    n "Agreed. Let's go."

label backcar1:
    scene black
    blank "We made our way one train car back, carefully watching our step between cars."
    show bg trainback with fade
    show sam with dissolve:
        xcenter .5
        linear 0.3 xcenter .75
    s "Hmmm... Seems awfully run down back here."
    hide sam
    show drac ind:
        xcenter .75
    d "It is rather dusty. I'd bet nobody's used this car in decades."
    n "I can barely breath back here, let's crack a window or something."
    hide drac ind
    show sam:
        xcenter .75
    s "It seems like the only window is on the back door."
    hide sam with dissolve
    blank "Sam checked out the back window for just a moment."
    show sam:
        xcenter .75
    s "No such luck - it definitely isn't designed to be opened."
    s "Also, this is the back of the train."
    n "Wait, we're at the backmost car already?"
    hide sam
    blank "Dracula and I checked the window as well."
    blank "Sure enough, the window was riveted on and there was no car behind us."
    show sam:
        xcenter .75
    s "The back door should open, but there's no platform to stand on. Let's wait for the others before doing that."
    s "It doesn't seem like there is anything useful back here, unless you're looking for a stretcher."
    n "Well, we definitely won't be needing that."
    hide sam
    show drac ind:
        xcenter .75
    d "........"
    n "........"
    hide drac ind
    show drac oh:
        xcenter .75
    show sam:
        xcenter .25
    s "Anyway."

    hide drac oh with dissolve

    show sam:
        xcenter .25
        linear 0.3 xcenter .75
    s "We should head back up and tell the others it's a dead end."
    n "Wait, there's a thin closet over there as well."
    n "Maybe there's something useful in it?"
    s "Worth a check."
    hide sam
    blank "Dracula tries to open the closet door, but it doesn't open."
    show drac ind:
        xcenter .75
    d "The door is locked. Maybe one of the others has found a key."
    hide drac ind
    show sam:
        xcenter .75
    s "It's probably only for custodians. Maybe they'd have the key?"
    s "Either way, there's nothing more for us back here."
    m "Yeah, it's getting hard to breath back here as well."

label midcar2:
    scene bg trainmid with fade
    show danchibi:
        zoom 1.5 xpos 20 ypos 20
    show samchibi:
        zoom 1.5 xpos 20 ypos 70
    show cydneychibi:
        zoom 1.5 xpos 20 ypos 120
    show bertchibi:
        zoom 1.5 xpos 20 ypos 170
    show stellachibi:
        zoom 1.5 xpos 20 ypos 220
    show cydney ind
    o "Did you find anything useful?"
    n "Not really. The next car back is the caboose."
    n "We should probably wait for everyone else to come back before going into too much detail."
    hide cydney ind
    show stella drunk
    t "Hey cutie, is there anything harder back there? Maybe some rum?"
    show stella drunk:
        xcenter .5
        linear 0.3 xcenter .75
    show bert sad:
        xcenter .25
    b "Stella might be a little drunk. I tried to tell her not to..."
    t "Anyone need a drink? There's a lot back there, just no ru-"
    hide bert sad
    show sam with dissolve:
        xcenter .25
    s "I don't think you're taking this seriously enough."
    s "Plus, there are kids here. You really shouldn't be getting drunk."
    t "Oh please, you twerps are no fun."
    hide stella drunk with moveoutright
    hide stellachibi with dissolve
    show sam:
        xcenter .25
        linear 0.3 xcenter .5
    s "I can already tell she's going to get on my nerves."
    s "Oh, that should be the others."
    hide sam
    blank "The front train car door opened, and Shahar, Jenny, Sid, and Catherine walked in."
    show jennychibi:
        zoom 1.5 xpos 20 ypos 220
    show shaharchibi:
        zoom 1.5 xpos 20 ypos 270
    show sidchibi:
        zoom 1.5 xpos 20 ypos 320
    show catherinechibi:
        zoom 1.5 xpos 20 ypos 370
    show draculachibi:
        zoom 1.5 xpos 20 ypos 420
    show freddychibi:
        zoom 1.5 xpos 20 ypos 470
    show kaiserchibi:
        zoom 1.5 xpos 20 ypos 520
    show jenny happy
    j "Hey, you guys are back already!"
    show jenny happy:
        xcenter .5
        linear 0.3 xcenter .75
    show drac ind:
        xcenter .25
    d "I cannot say I was particularly impressed by the back car."
    blank "Dracula spent a few minutes explaining the back car to everyone else."
    hide jenny happy with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "So it's a run down little caboose? That's kind of ironic."
    hide drac ind with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "What do you mean 'ironic?"
    s "What did you guys find up ahead?"
    hide sid ind with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "Some of the most amazin' technology me eyes have ever seen!"
    hide sam with moveoutleft
    show catherine happy with moveinleft:
        xcenter .25
    c "Haha! I'm not sure I'd go that far, but I am seeing a trend on this train..."
    c "I think it'd be best if we all just go take a look together."
    ses "mowwww!"
    n "Should we do anything about Stella? She's passed out behind the bar."
    h "A nap might do her some good."
    n "...Okay."
    blank "I hope we don't regret that leaving her here alone."

python:
    '''
    hide catherine happy with dissolve
    hide shahar ind with dissolve
    hide jennychibi with dissolve
    hide shaharchibi with dissolve
    hide samchibi with dissolve
    hide sidchibi with dissolve
    hide catherinechibi
    hide draculachibi
    hide cydneychibi
'''

label frontcar1:
    scene black with fade
    blank "The 11 of us made our way to the front car, leaving only Stella in the middle car."
    show bg trainfront1 with dissolve
    show danchibi:
        zoom 1.5 xpos 20 ypos 20
    show samchibi:
        zoom 1.5 xpos 20 ypos 70
    show cydneychibi:
        zoom 1.5 xpos 20 ypos 120
    show bertchibi:
        zoom 1.5 xpos 20 ypos 170
    show jennychibi:
        zoom 1.5 xpos 20 ypos 220
    show shaharchibi:
        zoom 1.5 xpos 20 ypos 270
    show sidchibi:
        zoom 1.5 xpos 20 ypos 320
    show catherinechibi:
        zoom 1.5 xpos 20 ypos 370
    show draculachibi:
        zoom 1.5 xpos 20 ypos 420
    show freddychibi:
        zoom 1.5 xpos 20 ypos 470
    show kaiserchibi:
        zoom 1.5 xpos 20 ypos 520
    show sam:
        xcenter .5
        linear 0.3 xcenter .8
    s "Wow, you guys were not joking... There are screens everywhere."
    n "There must be over 20 monitors in this train car."
    n "Is that even practical? What are they showing?"
    show kaiser ind:
        xcenter .25
    k "It is quite an interesting setup..."
    k "There is a lot of information, but nothing useful for us."
    hide sam with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "I'm pretty good with technology, for a high schooler at least..."
    i "Let me have a go!"
    k "Good luck."
    hide sid ind with dissolve
    show sidstand with dissolve:
        zoom .9 xcenter .5 ycenter .46
    show bert sad with moveinright:
        xcenter .75
    b "What do you mean by, nothing useful?"
    k "Well, we can see some technical aspects of the train."
    k "For example, I can tell you we're going 143 MPH."
    show sidstand:
        zoom .9 xzoom -1 xcenter .5 ycenter .46
    k "But the controls are all either locked or password protected."
    k "So it seems like we can't stop the train or change the course."
    hide kaiser ind with moveoutleft
    show catherine ind with moveinleft:
        xcenter .25
    c "This is also the front most car, which means..."
    hide bert with moveoutright
    show sam with moveinright:
        xcenter .75
    s "Nobody else is on the train. Damn."
    s "I was hoping we could find someone to help us."
    c "No conductor and no way to control the train ourselves."
    c "To summarize, it's just these 3 train cars."
label showcars:
    scene black with fade
    show bg trainfront1 with fade:
        zoom .9 xcenter .5 ycenter .5
    c "So this is the front car, that we're in right now."
    n "Stuffed to the brim with screens and controls."
    show bg trainmid with fade:
        zoom .9 xcenter .5 ycenter .5
    c "Followed by the bar car behind us."
    k "Which has an... Upscale 1970s aesthetic."
    show bg trainback with fade:
        zoom .9 xcenter .5 ycenter .5
    c "And then the 3rd car, a little caboose."
    d "A run down dusty little mess."
label frontcar2:
    show bg trainfront1 with dissolve:
        zoom 1
    show danchibi:
        zoom 1.5 xpos 20 ypos 20
    show samchibi:
        zoom 1.5 xpos 20 ypos 70
    show cydneychibi:
        zoom 1.5 xpos 20 ypos 120
    show bertchibi:
        zoom 1.5 xpos 20 ypos 170
    show jennychibi:
        zoom 1.5 xpos 20 ypos 220
    show shaharchibi:
        zoom 1.5 xpos 20 ypos 270
    show sidchibi:
        zoom 1.5 xpos 20 ypos 320
    show catherinechibi:
        zoom 1.5 xpos 20 ypos 370
    show draculachibi:
        zoom 1.5 xpos 20 ypos 420
    show freddychibi:
        zoom 1.5 xpos 20 ypos 470
    show kaiserchibi:
        zoom 1.5 xpos 20 ypos 520
    show sidstand with dissolve:
        zoom .9 xcenter .5 ycenter .46
    show catherine ind:
        xcenter .5
        linear 0.3 xcenter .8
    c "We don't have too much to work with here..."
    c "And we still don't know where we're going."
    ses "Mrow..."
    show shahar ind with moveinleft:
        xcenter .25
    h "Arg. I say we crack a window n' make a jump for it!"
    hide catherine ind with moveoutright
    show cydney ind with moveinright:
        xcenter .8
    o "Kaiser just said we're going over 140 MPH."
    o "Feel free to jump out the window if you want to, but there's no way I'm going to."
    h "Ye make a good point."
    h "A hundred knots is nothing to trifle with."
    hide cydney ind
    hide shahar ind
    with dissolve
    show frog sad with moveinbottom:
        xcenter .25
    f "No driver?"
    f "What are we going to do?... I'm scared..."
    n "Yeah, me too kid. We're outta options."
    show jenny ind:
        xcenter .75
    j "What's wrong with you, Dan? He's just a little kid."
    hide jenny ind
    show jenny happy:
        xcenter .75
    j "Hey it's ok Freddy! It's like an adventure."
    j "Come on, let's go back to the other train car and sit down."
    f "Okay."
    hide frog sad with moveoutbottom
    hide jenny happy
    show jenny ind:
         xcenter .75
    j "You punk. We're stuck in here together, you know?"
    j "It wouldn't kill you to be cooperative."
    hide jenny ind with moveoutright
    blank "How can I cooperate after what that screen told us..."
    show sam with moveinleft:
        xcenter .25
    s "In any case..."
    s "We should make a plan."
    s "We can't just sit here and wait to find out where we're going."
    show cydney ind with moveinright:
        xcenter .75
    o "I agree. It's getting late, but we should spend a little more time exploring before calling it a day."
    o "Some of us haven't even seen the back car yet, so we should start there."
    s "Yeah, let's make sure we're staying in groups."
    s "Especially the kids, like Freddy and Sid."
    hide sidstand with dissolve
    show cydney ind:
        xcenter .75
        linear 0.3 xcenter .85
    show sam:
        xcenter .25
        linear 0.15 xcenter .15
    show sid ind with moveinbottom
    i "Hey! Who are you callin' a kid?!"
    i "I'm an honor student and I work 4 hours after school every day!"
    i "I'm a man!"
    s "Oh yeah? Any luck with the controls panel big guy?"
    i "..."
    i "....."
    i "..............."
    i "I'm outta here! You guys suck!"
    hide sid ind with dissolve
    show cydney ind:
        xcenter .85
        linear 0.3 xcenter .75
    show sam:
        xcenter .15
        linear 0.15 xcenter .25
    o "That was a little harsh."
    s "...I'll go after him to apologize."
    s "We can head to the back car together afterwards."
    o "I'll come too."
    hide cydney ind with dissolve
    hide sam with dissolve
    show kaiser ind with dissolve
    k "I'm going as well. I haven't seen the back car yet."
    hide kaiser ind with dissolve
    show bert sad with dissolve
    b "I haven't yet either, but I want to spend a little more time up here first."
    b "This feels like where we'll find the most answers."
    n "I'd like to take a closer look too."
    show bert sad:
        xcenter .5
        linear .3 xcenter .75
    show drac ind with moveinleft:
        xcenter .25
    d "I am quite unfamiliar with everything I'm seeing up here."
    blank "Is this guy really Dracula?"
    d "Perhaps we could talk through some things together?"
    hide bert sad
    show bert happy:
        xcenter .75
    b "Yeah, of course! I just noticed a panel over here that seemed interesting."
    b "It seems like there are a 3 accessible switches."
    n "We probably shouldn't try them haphazardl-"
    b "Let's try them!"
    blank "Bert flipped the first switch."
    play sound "butt.mp3"
    show bg trainfront1:
        alpha .3
    hide drac ind
    show drac oh:
        xcenter .25
    n "So that's the light switch... Thankfully there's still a little sunlight."
    hide drac oh
    show drac ind:
        xcenter .25
    d "Interesting. It seems this car {i}does{/i} control the rest of the train."
    b "Yeah. I think the 3 light switches correspond to the 3 train cars."
    blank "Bert flipped the first switch back."
    play sound "butt.mp3"
    show bg trainfront1:
        alpha 1
    b "We're making progress already! Let's keep looking around."
label frontcar3:
    scene black with fade
    blank "10 minutes pass."
    show bg trainfront1
    show bert sad:
        xcenter .75
    show drac ind:
        xcenter .25
    with fade
    b "Well, it seems like the others were right."
    b "Despite all the stuff up here, it all seems password protected."
    d "I am particularly intrigued by something."
    d "The password screens all have another value shown."
    d "For example,"
    show welcomescreenblank with dissolve
    d "What does 'users: 0' mean?"
    b "Yeah, I was confused about that."
    b "Nobody is logged in, so maybe that's what it means?"
    n "But if we were logged in, we would know it, we wouldn't need it to say 'users: 1'."
    b "Also, what is 'Tead'?"
    b "How am I even supposed to pronounce that? Like read or {i}read?{/i}"
    n "......."
    hide welcomescreenblank with dissolve
    b "Either way, we can't log in, so it doesn't matter much."
    b "We should head back to the bar car and meet up with the others."
    d "Agreed."
    hide bert sad
    hide drac ind
    with dissolve
    n "......"
    n "{i}Now that I'm alone...{/i}"
label passwording:
    show welcomescreenblank with dissolve
    n "{i}Might as well try some passwords.{/i}"
    python:
        password = renpy.input("What could it be?", length=10)
        password = password.strip()

        if not password:
            password = "ERROR"
    play sound "beep.mp3"
    n "{i}I don't think it was [password]...{/i}"
    menu:
        n "{i}Maybe I should try again...{/i}"

        "{i}It can't hurt...{/i}":
            jump passwording

        "{i}I should go meet up with the others...{/i}":
            n "{i}They're probably waiting for me.{/i}"
    hide welcomescreenblank with dissolve
    n "{i}I can come back if I figure it out, but I don't want to take too long up here.{/i}"
label midcar3:
    scene bg trainmid with fade
    show jenny ind with dissolve
    j "Hey, Bert found some food behind the bar!"
    hide jenny ind
    show jenny happy
    j "Hope you don't mind, we started eating without you."
    show jenny happy:
        linear .3 xcenter .75
    show cydney ind:
        xcenter .25
    o "Turkey sandwiches and mixed nuts aren't much, but I'm starving."
    j "Yeah, this our first meal since we've woken up here."
    hide jenny happy
    show jenny ind:
        xcenter .75
    j "I feel a little bad for Catherine..."
    j "She's a vegetarian, so she's only been eating the nuts and bread."
    o "Plus, there's no cat food. Sesame's been eating the turkey from the sandwiches."
    hide cydney ind with dissolve
    show catherine happy with dissolve:
        xcenter .25
    c "Don't worry about us!"
    c "It feels nice to relax and eat for a bit."
    ses "mewmewmewmew!"
    scene black with fade
    n "{i}It feels... Surprisingly nice having a communal meal.{/i}"
    blank "They ate; about an hour passed."
    show bg trainmid with fade
    show kaiser ind with dissolve:
        xcenter .75
    show jenny ind with dissolve:
        xcenter .25
    j "Thankfully there's food on the train. It would have been an even bigger disaster otherwise."
    k "Yes, we got quite lucky there."
    ni "Is it luck?"
    n "Yeah."
    n "Though, I'm not really sure what we do next..."
    j "I feel like we've searched the whole train and found very little..."
    ##hide jenny happy with moveoutright
    ##show kaiser ind with moveinright:
    ##    xcenter .75
    k "Needlessly searching will do no good. We'll just exhaust ourselves."
    k "Maybe we should follow in Stella's footsteps here."
    j "And pass out behind the bar?"
    k "Well, sleep. It is getting late, and we've been at it all day."
    k "Both Freddy and the Pirate guy have already fallen asleep over there."
    k "We should figure out the rest of the sleeping arrangements."
    n "The train is pretty cramped, there definitely aren't 9 more chairs or beds for us."
    hide jenny ind with moveoutleft
    show bert sad with moveinleft:
        xcenter .25
    b "There are 5 more chairs in this car, and then a bed and a bench in the caboose."
    b "So that leaves... 2 people's bed's unaccounted for."
    hide kaiser ind with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "If I may add. Do not worry about my sleeping arrangements."
    d "This is no need."
    n "Why's that?"
    d "I simply do not sleep."
    n "..."
    b "..."
    d "..."
    b "Okay, so only 1 more bed to account for."
    hide drac ind with moveoutright
    show kaiser ind with moveinright:
        xcenter .75
    k "I'm content sleeping on the floor in the front car, if it makes it easier for the young ones."
    n "There's probably an extra blanket or pillow around somewhere."
    k "It is fine. I am used to poor sleeping conditions."
    k "With that taken care of. Goodnight all."
    hide kaiser ind with moveoutright
    b "Well, as long as that's taken care of. G'night Dan!"
    hide bert with moveoutleft
    show sid ind with dissolve:
        xcenter .25
    show sam with dissolve:
        xcenter .75
    i "So, 2 of us 3 are in the back car?"
    s "It's so dusty back there... Maybe we should all just squeeze in here somehow?"
    n "I don't think there's enough space in here. It's just a bar car after all."
    n "I can sleep in the back car, I don't mind."
    show sid ind:
        linear .3 xcenter .35
    i "Me too! I can handle it."
    s "Sid, are you sure? If it's too dusty for you I can sleep back there."
    show sid ind:
        linear .3 xcenter .5
    i "I'm used to sharing 1 bed with my whole family! This is an practically an upgrade!"
    hide sid ind with moveoutleft
    show sam:
        linear .3 xcenter .5
    s "Well, that settles it I guess."
    s "Keep an eye on him back there Dan, I don't want anything bad to happen to the kids."
    n "Anything... bad?"
    s "Goodnight Dan."
    hide sam with dissolve
    n "..."
    scene black with fade
    blank "Dan made his way to the back car."
    show bg trainback with fade
    ni "I forgot how dusty it was back here."
    show sid ind with dissolve
    i "Wow, there's even an old school water kettle back here!"
    n "This is probably where some of the train workers slept."
    n "Hence the bed, kettle, and closet."
    i "That sounds so..."
    hide sid ind
    show sid happy
    i "Exciting!"
    i "I wish I could travel and live on cool trains like this."
    n "Haha! You're still young, Sid, maybe you can one day."
    hide sid happy
    show sid ind
    i "What do you mean, young?"
    i "I work my ass off to take care of my parents!"
    i "You don't know what I've been through."
    n "Hey woah! Don't take it the wrong way."
    n "You're more of a man than I am, bud."
    hide sid ind
    show sid happy
    i "Wa-wait, really? - I mean, hell yeah I am!"
    i "But why do you say that?"
    n "I saw how you tried to figure out the train controls all on your own earlier."
    n "You tried to be the hero."
    hide sid happy
    show sid ind
    i "Th-thanks... I couldn't figure it out though."
    n "Yeah, none of us could figure out the password. We can't do anything without it."
    i "Well, I got to the file directory, but it wouldn't let me open anything up."
    n "What? You got the a file directory? How did you do that?"
    i "I work with computers a lot when I'm helping my dad with the shop."
    i "A lot of computers let you check for files using the \"DIR\" command."
    i "I tried that in the password box and it showed me some of the computer's files."
    n "Sid, you're a genius! What did they show?"
    i "Hehe, it's nothing really..."
    show welcomescreendir with fade
    i "So I typed in \"DIR\" and hit enter."
    show welcomescreendir2 with dissolve
    i "And it showed me something like this."
    i "I couldn't click on any of the files, I could only see names."
    i "I tried to make a mental note of all of them, but..."
    show welcomescreendir2 with dissolve:
        zoom 2
        xcenter .6
        ycenter .4
    i "Only two of them really jumped out to me."
    i "One called \"Participants\" and one called \"Train Route\"."
    hide welcomescreendir
    hide welcomescreendir2
    with fade
    n "Wow... \"Train Route\" would almost definitely be useful."
    i "I'm positive that it would tell us where the train is going, if we could open it."
    n "And... Participants. I wonder if that's about... Us."
    i "Yeah... That's what I was thinking too."
    ni "If it is, maybe that file could tell us why we're all here..."
    ni "Maybe it would tell us who's behind all this."
    i "Afterwards, I noticed something else when I hit Return..."
    show welcomescreendir3 with dissolve
    i "The users went up from 0 to 1."
    n "Wait, so the user counter isn't tracking how many people are currently logged in..."
    n "It's tracking how many people have checked the file directory {i}total.{/i}"
    i "It seems like it."
    hide welcomescreendir3 with dissolve
    n "So we'll know if someone else get's this info from the computer."
    n "Do you think the counter will go up if someone logs in with the password?"
    i "If someone logs in, they can probably reset or change the counter using \"user_counter.exe\"."
    i "So that might not be reliable..."
    n "Got it."
    n "Either way, Sid, this is a huge find!"
    hide sid ind
    show sid happy
    i "Haha, really, it's nothing..."
    n "Let's keep this between you and me for now."
    n "This might come in handy, but I don't think we should share it with everyone just yet."
    i "Yeah... I don't trust some of these people."
    i "The pirate guy and the vampire guy scare me, and that French lady is such a drunk hag."
    hide sid happy
    show sid ind
    n "I'm with you. Let's stick together Sid."
    i "D-deal!"
    n "For now though, let's hit the hay. We can figure out some plans in the morning."
    i "Yeah! I call the bed!"
    hide sid ind with dissolve
label day2:
    scene black with Fade(1.5,0,1)
    blank "8 hours later."
    blank "Im bert!!!!!!!! PISS FART"
