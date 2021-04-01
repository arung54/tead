label go:

    #jump frontcar1
    #show screen button_overlay
    scene black
    play music "audio/rush.mp3"
    ni "Was I... Dreaming?"
    ni "It'd make sense..."
    ni "I did tend to get nightmares in there..."
    ni "..."
    blank "Hey..."
    ni "Huh?"
    blank "HEY!!!"
    scene bg trainmid
    show lauren ind
    with fade
    o "Hey, wake up already."
    o "How'd you manage to stay knocked out even longer than the kid?"
    n "..."
    n "Where are we now?"
    show lauren ind:
        xcenter .5
        linear 0.3 xcenter .75
    o "I mean, look around. Where do you think we are?"
    n "It's a... train car."
    n "And we're {i}moving.{/i}"
    hide lauren ind with dissolve
    show sam
    s "Yeah, we're going somewhere..."
    s "...Or being taken somewhere."
    hide sam with dissolve
    blank "I looked out the window."
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
    ni "There's... Nothing out there."
    ni "Where are we? There are no landmarks anywhere."
    hide forest run
    hide windowview
    with fade
    show shahar ind with dissolve
    h "Laddies, it feels like the whole room is moving!"
    n "That's how trains work."
    n "Have you never been on a train before?"
    h "Blimey, you're right! We {i}are{/i} movin'!"
    hide shahar ind with moveoutright
    n "..."
    show catherine ind
    c "Oh, Dan's finally awake?"
    c "It seems like everyone from that scary room is here."
    show catherine ind:
        xcenter .5
        linear 0.3 xcenter .75
    show drac ind:
        xcenter .25
    d "Yes. All 12 of us are here."
    d "13 if you include the feline."
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
    hide sid ind with dissolve
    show jenny ind with dissolve
    j "Maybe we were on the train the whole time?"
    show jenny ind:
        linear .3 xcenter .75
    show bert sad:
        xcenter .25
    b "I don't think so... Those rooms were pretty wide."
    b "I don't think they could have fit in a train car."
    hide jenny ind with moveoutright
    show bert sad:
        linear .3 xcenter .5
    b "Dan, what do you think?"
    n "Me? Hmm..."
    menu:
        n "{i}How did we get here?{/i}"

        "Maybe we got on board ourselves.":
            n "Maybe we got on board ourselves."
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
            n "We must have been moved here."
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
    n "You know how we got knocked out?"
    n "What do you mean?"
    show kaiser ind:
        xcenter .5
        linear 0.3 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    o "Kaiser's probably right... Think back to what the monitor told us."

    ###FLASHBACK###
    show black
    n "flashback to part about chips in our brain, have to cooperate etc"
    hide black
    o "As terrifying as that is, it seems like the only explaination..."
    n "You really think the chips knocked us out somehow?"
    hide kaiser ind
    hide lauren ind
    with dissolve
    show sam with dissolve
    s "It's the only logical explanation."
    s "Either way, I don't think it's worth spending any more time on."
    s "We're finally all awake, we should try to figure out what's going on."
    n "Right. We should start exploring the train."
    show sam:
        xcenter .5
        linear 0.3 xcenter .75
    show bert happy with moveinleft:
        xcenter .25
    b "Maybe we can find the conductor!"
    b "He could stop the train for us."
    ni "That seems a little optomistic..."
    s "It's worth a shot."
    b "That's the spirit! Poggers!"
    s "It's not like we're going to just sit around here."
    ni "..."
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
    b "It's probably best if Freddy doesn't get involved."
    hide sam with moveoutright
    hide bert happy with moveoutleft
    show frog ind:
        xcenter .5
        linear .3 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    o "We can sit together, buddy. We'll hang out here."
    f "{i}*sniffle*{/i} Okay miss."
    hide frog ind with moveoutright
    show lauren ind:
        linear .3 xcenter .5
    o "I can watch him, I used to babysit in highschool."
    o "I don't want a kid involved in... Whatever this is."
    n "That's probably smart. I'm not great with kids myself."
    o "The rest of you better search every corner of this train though."
    hide lauren ind
###########################################
###############INVESTIGATE#################
###########################################

    show stella happy
    t "Great point Lauren - the whiskey could be hiding anywhere."
    t "I'll check behind the bar."


    hide stella ind with moveoutright
    show bert sad with dissolve
    b "..."
    hide bert sad
    show bert happy
    b "There might be food back there though, and we're going to need to eat. I'll look with you."

    hide bert happy with moveoutright
    show shahar ind
    h "Aye, I'll check the next car up. To the front with me!"
    h "The captain aught to be at the bow!"
    hide shahar ind with moveoutleft
    show sid ind
    i "I'll go with, the uh, pirate. Why is there a pirate here again?"
    hide sid ind with moveoutleft
    show jenny ind
    j "Hmm, I'm going to go with them too. We should probably try to stay in groups."
    j "Plus, going to the front seems like the best way to find out where we're going."
    show jenny ind:
        linear .2 xcenter .6
    show catherine ind with moveinleft:
        xcenter .38
    c "We're coming too!"
    show jenny ind with hpunch
    j "AHHHHH!"
    j "Catherine, your dumb cat just bit me!"
    show catherine happy
    c "Oops! Sorry, that's just Sesame's way of saying he's excited!"
    j "Ow..."
    c "Hehe, sorry! Alright Sesame, we're going exploring!"
    ses "Moewwwwww!"
    ni "..."
    hide jenny ind with moveoutright
    hide catherine ind with moveoutleft

    show sam
    s "Okay, the rest of us can check the next car back."
    s "It looks like it's just the 3 of us."
    hide sam
    show drac ind
    d "Very well."
    hide drac ind
    menu:
        n "{i}Should I go with them?{/i}"

        "Yes":
            n "Alright."

        "No":
            n "Actually, I might just stay here."
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
    s "I'm wary of trusting anybody too much yet, especially after what the monitor said."
    n "Alright. Let's go."

label backcar1:
    scene black
    blank "We made our way one train car back, carefully watching our step between cars."
    show bg trainback with fade
    show sam with dissolve:
        xcenter .5
        linear 0.3 xcenter .75
    s "Hmmm... It seems awfully run down back here."
    s "There's a little cot, a bench, a water tank..."
    n "This must be where the train hands would sleep on long trips."
    hide sam
    show drac ind:
        xcenter .75
    d "I'd bet nobody's used this car in decades, though."
    d "There's dust coating nearly every surface."
    n "Maybe we can open a window or something."
    hide drac ind
    show sam:
        xcenter .75
    s "It seems like the only window is on the back door."
    hide sam with dissolve
    blank "Sam checked out the back window."
    show sam:
        xcenter .75
    s "No such luck - it definitely isn't designed to be opened."
    s "Also, this is the back of the train."
    n "Wait, we're at the backmost car already?"
    hide sam
    blank "Dracula and I checked the window as well."
    blank "Sure enough, the window was riveted on and there was nothing behind us."
    show sam:
        xcenter .75
    s "The back door might open, but there's no platform to stand on. Let's wait for the others before doing that."
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
    n "Yeah, we should go back to the bar car."

label midcar2:
    scene bg trainmid with fade
    show danchibi:
        zoom 1.5 xpos 20 ypos 20
    show samchibi:
        zoom 1.5 xpos 20 ypos 70
    show laurenchibi:
        zoom 1.5 xpos 20 ypos 120
    show bertchibi:
        zoom 1.5 xpos 20 ypos 170
    show stellachibi:
        zoom 1.5 xpos 20 ypos 220
    show lauren ind
    o "Did you find anything useful?"
    n "Not really. The next car back is the caboose."
    n "We should probably wait for everyone else to come back before going into too much detail."
    hide lauren ind
    show stella drunk
    t "Hey cutie, is there anything harder back there? Maybe some rum?"
    show stella drunk:
        xcenter .5
        linear 0.3 xcenter .75
    show bert sad:
        xcenter .25
    b "Hey, woah!"
    b "Stella might be a little drunk. I tried to tell her not to drink, but..."
    t "Anyone need a beer? There's a lot ba-"
    hide bert sad
    show sam with dissolve:
        xcenter .25
    s "I don't think you're taking this seriously enough."
    s "Plus, there are kids here. You really shouldn't be getting drunk."
    t "You don't like alcohol?"
    s "I don't think that's relevant."
    t "Oh please, you twerps are no fun."
    hide stella drunk with moveoutright
    hide stellachibi with dissolve
    show sam:
        xcenter .25
        linear 0.3 xcenter .5
    s "I can already tell she's going to get on my nerves."
    s "Oh, the others are back."
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
    s "What do you mean 'ironic?'"
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
    hide laurenchibi
'''

label frontcar1:
    scene black with fade
    blank "The 11 of us made our way to the front car, leaving only Stella in the middle car."
    show bg trainfront1 with dissolve
    show danchibi:
        zoom 1.5 xpos 20 ypos 20
    show samchibi:
        zoom 1.5 xpos 20 ypos 70
    show laurenchibi:
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
    show laurenchibi:
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
    show lauren ind with moveinright:
        xcenter .8
    o "Kaiser just said we're going over 140 MPH."
    o "Feel free to jump out the window if you want to, but there's no way I'm going to."
    h "Ye make a good point."
    h "A hundred knots is nothing to trifle with."
    hide lauren ind
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
    j "Come on, let's go back to the other train car and find something to play with."
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
    show lauren ind with moveinright:
        xcenter .75
    o "I agree. It's getting late, but we should spend a little more time exploring before calling it a day."
    o "Some of us haven't even seen the back car yet, so we should start there."
    s "Yeah, let's make sure we're staying in groups."
    s "Especially the kids, like Freddy and Sid."
    hide sidstand with dissolve
    show lauren ind:
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
    i "It locked me out after 5 attempts at the password..."
    s "Ha!"
    i "I'm outta here! You guys suck!"
    hide sid ind with dissolve
    show lauren ind:
        xcenter .85
        linear 0.3 xcenter .75
    show sam:
        xcenter .15
        linear 0.15 xcenter .25
    o "That was a little harsh."
    s "...I'll go after him to apologize."
    s "We can head to the back car together afterwards."
    o "I'll come too."
    hide lauren ind with dissolve
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
    play sfx "audio/butt.mp3"
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
    play sfx "audio/butt.mp3"
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
    ni "......"
    ni "Now that I'm alone..."
label passwording:
    play music "audio/invest1.wav" volume .3
    show welcomescreenblank with dissolve
    $ passattempts = 1
    while passattempts < 10:
        $ password = renpy.input("What could it be?", length=10)
        $ password = password.strip()

        if not password:
            $ password = "ERROR"
        play sfx "<from 0 to 1>audio/beep.mp3" volume .5
        ni "I don't think the password is '[password]'..."
        menu:
            ni "Maybe I should try again..."
            "It can't hurt...":
                $ passattempts += 1
                if passattempts > 5:
                    ni "Hmm... The screen froze up."
                    ni "I must have gotten it wrong too many times, it's not letting me enter any more passwords."
                    ni "I guess I should go meet back up with the others."
                    jump donepasswording

            "I should go meet up with the others...":
                jump donepasswording
label donepasswording:
    show bg trainfront1 with fade
    ni "They're probably waiting for me."
    ni "I can come back if I figure it out, but I don't want to take too long up here."
label midcar3:
    play music "audio/invest1.wav" volume .3

    scene bg trainmid with fade
    $ showchibi("dan", "shahar", "stella")
    show jenny ind with dissolve
    j "Hey, Bert found some food behind the bar!"
    hide jenny ind
    show jenny happy
    show behappy
    bp "Epicchamp!"
    hide behappy
    j "Hope you don't mind, we started eating without you."
    show jenny happy:
        linear .3 xcenter .75
    show lauren ind:
        xcenter .25
    o "Turkey sandwiches and mixed nuts aren't much, but I'm starving."
    j "Yeah, this our first meal since we've woken up here."
    hide jenny happy
    show jenny ind:
        xcenter .75
    j "I feel a little bad for Catherine..."
    j "She's a vegetarian, so she's only been eating the nuts and bread."
    o "Plus, there's no cat food. Sesame's been eating the turkey from the sandwiches."
    hide lauren ind with dissolve
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
    j "Get black out drunk and pass out on the floor?"
    k "Well, sleep. It is getting late, and we've been at it all day."
    k "Both Freddy and the Pirate guy have already fallen asleep over there."
    k "We should figure out the rest of the sleeping arrangements."
    n "The train is pretty cramped, there definitely aren't 9 more chairs or beds for us."
    hide jenny ind with moveoutleft
    show bert sad with moveinleft:
        xcenter .25
    b "There are 5 more chairs in this car, and then a bed and a bench in the caboose."
    b "So that leaves... 2 people's beds unaccounted for."
    hide kaiser ind with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "If I may add - Do not worry about my sleeping arrangements."
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
    i "I'm used to sharing 1 bed with my whole family! This is a practically an upgrade!"
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
    n "Haha, you're still young, Sid, maybe you can one day."
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
    n "It's tracking how many people have checked the file directory {i}total?{/i}"
    i "It seems like it."
    hide welcomescreendir3 with dissolve
    n "So we'll know if someone else gets this info from the computer."
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
    play sfx "audio/butt.mp3" volume .5
    show bg trainback:
        alpha .5
    i "Huh?"
    n "Hmm, someone must have hit the light switch."
    n "We found all 3 light switches in the front car earlier."
    i "That should make it a little easier to sleep."
    n "Yeah, let's hit the hay. We can figure out some more plans in the morning."
    i "You can have the bed. I'm fine sleeping on the bench."
    n "Okay, you can have the bed tomorrow night."
    ni "The thought of still being stuck on this train tomorrow night sent chills through my body."
    n "Alright, goodnight Sid."
    hide sid ind with dissolve
label day2:
    scene black
    pause 1
    blank "The next morning..."
    play music "audio/rush.mp3" volume .3 fadein 1.0
    scene bg trainback
    $ showchibi("dan", "sid")
    show chaptericon at topright:
        zoom .4
    show mapicon:
        xcenter .965
        ycenter .12
        zoom .3
    show evidenceicon:
        xcenter .91
        ycenter .12
        zoom .3
    show sid happy with dissolve:
        xcenter .5
        linear .3 xcenter .75
    i "'Morning Dan!"
    n "Huh? Oh, Sid... What time is it?"
    i "No idea, but the sun's up. I'm heading to the bar car to the others."
    hide sid happy with moveoutright
    $ showchibi("dan")
    ni "That kid's got a lot of energy. It must be around 7AM."
    blank "Dan walked to the back window."
    show tracks with dissolve
    ni "Damn... There really isn't anything out there..."
    ni "It'd be a lot easier to be hopeful if there were {i}any{/i} signs of life."
    ni "I might have to take this into my own hands..."
    hide tracks with dissolve
    ni "But for now, I should go meet the others."
    show bg trainmid with fade
    $ showchibi("dan", "bert", "catherine", "lauren", "freddy", "kaiser", "sam", "sid", "stella", "dracula")
    show catherine happy with dissolve:
        xcenter .5
        linear .3 xcenter .75
    c "Gooooooood morning Dan! It's another gorgeous day on the Nowhere Express!"
    show frog ind with moveinleft:
        xcenter .25
    f "Yeah! Gorgeous day!"
    c "Come get your gourmet turkey sandwiches and half-sized cans of soda!"
    f "Soda for breakfast! Wooo!"
    n "How are you guys so peppy?"
    f "Come on sesame, let's go play!"
    ses "Merowwwwww!"
    hide frog ind with moveoutleft
    c "Nothing we can do but try to enjoy ourselves a little!"
    hide catherine happy with moveoutleft
    show sam with dissolve:
        xcenter .5
        linear .3 xcenter .75
    s "She was up late with Freddy making sure he wasn't freaking out too much."
    show bert happy with dissolve:
        xcenter .25
    b "It was pretty heartwarming, to be honest."
    b "I'm glad we're all still staying optomistic."
    b "We're gunna figure this out and get off this train!"
    s "Agreed."
    ni "..."
    s "We should wait for everyone to wake up and have a meeting."
    s "We've explored the train, but we need to figure out a plan."
    b "Let's meet back here in 30 minutes! Break!"
    hide bert happy
    hide sam
    with dissolve
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    ni "I don't particularly want to talk to anyone, but..."
    ni "I should mingle so I don't look suspicious."
   #############
   #FREE TIME ONE
   #############
    show stella ind with dissolve
    t "Oh? So you've got nobody better to chat with?"
    b "Well, we should get to know each other."
    t "Hmph. I don't {i}mind{/i} that, but don't get the wrong idea."
    t "I'm not into younger men."
    b "Oh, I didn't mean like th-"
    hide stella ind
    show stella happy
    t "Okay, okay, you caught me, so I {i}am{/i} into younger men."
    t "But we just met! Wine and wine me a little first, huh?"
    b "Don't you mean wine and {i}dine{/i}?"
    hide stella happy
    show stella bigsmile
    t "Deal!"
    b "Wait, I-"
    t "You're a sweetheart. It's a shame someone like you is stuck in a situation like this."
    hide stella bigsmile
    show stella happy
    t "It's been fun chatting. We should spend some more time together soon."
    hide stella happy with dissolve
    bi "I - what?"
    scene black with fade
    blank "30 minutes had passed, Dan went to meet the others in the bar car."
label midcar4:
    play music "audio/rush.mp3"
    show bg trainmid with fade
    $ showchibi("dan", "bert", "catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "shahar", "sid", "stella", "dracula")
    show bert sad with dissolve:
        xcenter .5
        linear .3 xcenter .75
    b "Alright, I think everyone's here."
    b "It's starting to seem like we've exhausted our resources."
    b "I've searched every inch of this train and feel no closer to finding anything useful."
    show kaiser ind with moveinleft:
        xcenter .25
    k "Or even an indication of where we're going."
    k "I would feel much more secure if we knew our destination."
    n "Yeah..."
    hide bert sad with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "Ummm..."
    j "I feel like we should address the elephant in the room..."
    n "What do you mean?"
    j "Well... Think back to that one message."
    blank "MESSAGE ABOUT HOW amogus"
    j "I think the implication is that whoever planned all this..."
    j "Is one of us."
    hide kaiser ind with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    o "Do you really think the person behind the messages is here right now?"
    hide jenny ind with moveoutright
    show sam with moveinright:
        xcenter .75
    s "I'm worried that Jenny's right."
    s "Otherwise, what's even the point of all this?"
    n "Huh?"
    s "Well, if this is some messed up game for them, they're probably here to watch."
    s "I haven't seen a single camera on board, so if they wanted to enjoy it, that's probably the only way."
    o "They're here to 'Enjoy it?' Sam, you sound a little hysterical..."
    s "We've been kidnapped, basically twice now, and have zero information on what the hell's happening."
    s "I'm stuck on a train with Dracula and a pirate and you're telling me I'm hysterical for being confused?"
    o "..."
    o "Fair enough."
    o "What do you think we should do about it?"
    hide sam with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Sam's right! Shahar and Dracula are suspicious."
    o "I don't think we should start throwing around accusations..."
    hide lauren ind with moveoutleft
    show shahar ind with moveinleft:
        xcenter .25
    h "Aye, I'm a man of 'onor. What are ye worried about, bucko?"
    i "It's the 21st century, why do you talk like that?"
    i "Why do you have an eyepatch?"
    hide sid ind
    show stella bigsmile:
        xcenter .75
    t "Why do you have such chiseled abs?"
    hide stella bigsmile
    show sid ind:
        xcenter .75
    i "Shut up, Stella."
    h "Aye. Ye see, me memory in't too good."
    h "Last I remember, me and me hearties were three sheets to the wind, mindin' our own."
    h "Next minute, I come to in the little crow's next wit' the rest of ye."
    i "I..."
    i "I don't really know what he just said."
    hide shahar ind with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "I find it quite curious that {i}you{/i} called {i}me{/i} suspicious."
    d "As such a little cutpurse yourself, that is."
    show sid happy:
        xcenter .75
        linear .1 xcenter .78
    play sfx "<from 0 to 1>audio/mildshock.mp3" volume .2
    i "Wh-what? Me? No way!"
    d "Oh? I'm sure you'll be happy to empty your pockets then."
    i "I-I-I can't."
    d "Interesting."
    hide sid happy with moveoutright
    show drac ind:
        linear .3 xcenter .5
    d "What a silly coincidence, I put a whiskey shooter in my pocket earlier, but..."
    d "It's just so happen to go missing earlier when Sid and I were alone together in the front car."
    d "Regardless, I've been nothing but productive and friendly since we woke up here yesterday."
    d "I'm sure you all believe me when I say I am just as dumbfounded as the rest of you."
    hide drac ind with dissolve
    show catherine ind with dissolve
    c "Guys, I don't think this is very productive."
    c "Throwing around accusations isn't going to get us anywhere."
    show catherine ind:
        linear .3 xcenter .75
    show jenny ind with moveinleft:
        linear .3 xcenter .25
    j "If one of us is the mole though, it should be our highest priority to figure out who it is."
    c "That's true..."
    c "Maybe we should just... Talk more about ourselves?"
    c "Even if it doesn't help figure out who the mole is, it'd be good to learn more about each other."
    j "Yeah, we're all stuck in here together anyway."
    c "With that said, I don't feel particularly notable..."
    c "I'm just a veterinary student... I like rock climbing... Long walks on the beach..."
    hide catherine ind with moveoutright
    show bert happy with moveinright:
        xcenter .75
    b "As interesting as that stuff is, maybe we should be focused more on... More extreme things."
    hide bert happy
    show bert sad:
        xcenter .75
    b "Reasons why someone might want to kidnap us, for example."
    ni "..."

    #############################################################################################################################################################################

    hide jenny ind with moveoutleft
    show stella ind with moveinleft:
        xcenter .25
    t "Look, darlings... If it helps clear things up, I should probably admit..."
    t "As a wildly successful businesswoman - some might even say the René Laennec of our time - I've inevitably built up a... reputation."
    t "I've done what I had to do to get to the top, and I've made many enemies along the way."
    n "What do you mean, 'done what you had to do'?"
    t "I tore down competition, I burned bridges, you name it."
    t "My methods don't always see eye-to-eye with the law, but, c'est la vie."
    ni "Is this lady for real?"
    b "That... Definitely seems like a reason to have enemies."
    t "It feels oddly freeing to not have my bodyguards and assistants around, saying:"
    t "'Ms. Cantoire! Put down the vodka!' 'Ms. Cantoire, don't put your head out the limousine sunroof!'"
    b "..."
    n "..."
    t "Of course, I am not the mole. It'd be a waste of my time."
    t "I have nothing to gain from... This."
    t "I'm only telling you all this so that you're not surprised when my past inevitably comes up."
    t "And sadly, I have no insight on who it might be."
    hide stella ind with moveoutleft
    b "..."
    b "Well at least she's being open about it."
    show sam with moveinleft:
        xcenter .25
    s "If we're airing out our past, I can go next."
    s "I don't have quite the same pedigree, but..."
    s "I used to sell drugs, mostly to upper-class business people and spoiled rich kids."
    s "I'd like to say I don't regret it, but..."
    s "The drugs weren't always safe."
    b "Not safe? What do you mean?"
    s "A lot of the stuff I moved was untested and highly experimental."
    s "But those dumb suits didn't know that, so they bought it."
    n "Did it ever end up killing anyone?"
    s "Honestly? I don't even know."
    s "That stuff's behind me, and it's hard to think about sometimes, so I try not to."
    s "But I do know I at {i}least{/i} pissed some people off. I wouldn't be surprised if that's part of why I'm here."
    s "It's hard to come to terms with some of this stuff..."
    s "Maybe I deserve this."
    b "Hey, don't say that! No way."
    b "We've all made mistakes, and owning up to it now can help us figure this out."
    b "Any information we can gather is progress."
    b "Does anyone else have anything they want to bring up?"
    ni "..."
    show scary with dissolve:
        alpha .2
    ni "Should... Should I speak up?"
    #play sfx "<from 0 to 3>audio/jaws.mp3" volume .1
    show scary:
        linear .3 alpha .5
    ni "I... Don't think they'd understand."
    show scary:
        linear .3 alpha .8
    ni "This might be my only opportunity though."
    show scary:
        linear .3 alpha .95
    ni "Maybe I should speak up."
    hide scary
    b "I guess I'll go next."
    b "It's not exactly the same as Stella's or Sam's, but..."
    hide sam with moveoutleft
    show bert sad:
        linear 1 xcenter .5
    b "I guess I can't think of anything else."
    b "I was only 17, too. It feels like so long ago but I think about it every day."
    b "I was driving after tutoring, same as always."
    b "It was spring..."
    b "And this lady... She just... Walked out..."
    b "Into the road..."
    ni "He's all choked up."
    show bert sad:
        linear 1 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    o "Alright, we're done with this."
    o "I can't sit by and watch you guys talk about stuff like this."
    o "For all we know our pasts aren't even relevant."
    hide bert sad with moveoutright
    show stella ind with moveinright:
        xcenter .75
    t "If the kid wants to talk, let him."
    t "It can't hurt."
    o "It's clearly a sensative topic for him."
    o "We don't need to make this situation any shittier."
    t "Hmph, just when I thought we were going to get into the juicy stuff..."
    hide stella ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "I don't think we should force anyone to talk about sensative topics, but..."
    j "I am starting to worry we're not getting anywhere."
    j "We could just wait until we get to our destination, but we have no idea how long that'll take."
    o "... Our food supply is starting to run low."
