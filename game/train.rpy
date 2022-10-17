label trainGo:

    $dan = True
    $mood="ind"
    #jump frontcar1
    #show screen button_overlay
    scene black
    play music "audio/rush.mp3" fadein 1.0
    ni "Was I... dreaming?"
    ni "It'd make sense..."
    ni "I did tend to get nightmares in there..."
    ni "..."
    z "Hey..." #Arunj: Change speaker to ???
    ni "Huh?"
    $mood = "shock"
    z "HEY!!!"
    scene bg trainmid at bg
    $statusnt("???", "dan", ch = 1, sun = 3)
    show lauren ind
    $ showchibint("bert", "catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "shahar", "sid", "stella", "dracula")
    with fade
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .4
        ycenter .25
        zoom .75
    o "Hey, wake up already."
#   camera at parallax
    o "How'd you manage to stay knocked out even longer than the kid?"
    hide popwow
    n "Where are we now?"
    show lauren ind:
        xcenter .5
        linear 0.3 xcenter .75
    o "I mean, look around. Where do you think we are?"
    $ statusnt("Bar Car", "dan", ch = 1, sun = 3)
    with dissolve
    n "It's a... train car."
    o "And we're {i}moving.{/i}"
    n "Wow, really?"
    hide lauren ind with moveoutright
    show sam ind with moveinleft
    $mood = "mad"
    s "I mean, take a look for yourself, genius."
    s "We're going somewhere..."
    $mood = "ind"
    s "...Or being taken somewhere."
    hide sam with dissolve
    blank "Dan walked over to the window."
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
    ni "There's... nothing out there."
    ni "Where are we? There are no landmarks anywhere."
    ni "It's like the middle of a desert."
    hide forest run
    hide windowview
    with fade
    show shahar ind with dissolve
    h "Laddies, is it just me, or does it feels like the whole room is moving?"
    n "That's how trains work."
    n "Have you never been on a train before?"
    h "Blimey, yer right! We {i}are{/i} movin'!"
    h "It be like a land boat!"
    hide shahar ind
    with moveoutright
    n "..."
    show catherine ind with dissolve
    c "Oh, Dan's finally awake?"
    c "It seems like everyone from that scary place is here."
    show catherine ind:
        xcenter .5
        linear 0.3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "Yes. All 12 of us are here."
    d "13 if you include the feline."
    c "Excuuuse meee, please don't talk about King Sesame like that."
    ses "Mrow!"
    n "..."
    hide catherine ind
    hide drac ind
    with moveoutright
    show sid ind with moveinleft
    i "How did we even get here?"
    i "A minute ago we were trapped in that weird place."
    n "That's a good question..."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .55
        ycenter .275
        zoom .75
    i "Next thing I know, I'm waking up to some pirate poking me on a train."
    i "Seriously, what's with that guy..."
    hide poptear
    hide sid with moveoutright
    show jenny ind with moveinleft
    j "Maybe we were on the train the whole time?"
    j "And just got moved to a different train car?"
    show jenny ind:
        xcenter .5
        linear .3 xcenter .75
    show bert ind with dissolve: ###########################
        xcenter .25
    bt "I don't think so... Those rooms were pretty wide."
    bt "I don't think they could have fit in any reasonable train car."
    hide jenny ind with moveoutright
    show bert ind:
        linear .3 xcenter .5
    bt "Dan, what do you think?"
    show scary with dissolve:
        alpha .5
    n "Me? Hmm..."
    menu:
        n "{i}How did we get here?{/i}"

        "Maybe we got on board ourselves.":
            n "Maybe we got on board ourselves."
            hide scary with dissolve
            hide bert with moveoutright
            show drac ind with moveinleft
            play sfx "audio/popwow.mp3" volume .5
            show popwow:
                xcenter .4
                ycenter .25
                zoom .75
            d "I refuse to accept that."
            hide popwow
            show drac ind:
                linear .3 xcenter .75
            show stella ind with dissolve:
                xcenter .25
            t "The vampire's right, there's no way we got onboard ourselves."
            t "We'd obviously remember that."
            t "We must have been knocked out and moved here somehow."
            n "But how did they knock all of us out like that?"

        "We must have been moved here.":
            n "We must have been moved here."
            hide scary with dissolve
            hide bert with moveoutright
            show drac ind with moveinleft
            play sfx "audio/popwow.mp3" volume .5
            show popwow:
                xcenter .4
                ycenter .25
                zoom .75
            d "Yes, the culprit must have knocked us out and moved us here."
            hide popwow
            d "Otherwise we'd remember it."
            show drac ind:
                linear .3 xcenter .75
            show stella ind with dissolve:
                xcenter .25
            t "I don't remember boarding myself, that's for sure."
            t "How did they manage to knock all of us out though?"


    hide stella ind
    hide drac ind
    with moveoutright
    show kaiser ind with moveinleft
    k "It seems obvious enough, yes?"
    n "You know how we got knocked out?"
    n "What do you mean?"
    show kaiser ind:
        xcenter .5
        linear 0.3 xcenter .75
    show lauren ind with dissolve:
        xcenter .25
    o "Kaiser's probably right... think back to what the monitor told us."
    show start2
    show sepia:
        alpha .5
    with dissolve
    scr "A chip has been planted in each of your heads, capable of killing you instantly."
    scr "The chip will also be used to keep you unconscious as you are transported between locations."
    hide start2
    hide sepia
    with dissolve
    o "As terrifying as that is, it seems like the only explanation..."
    $mood = "shock"
    n "You really think the chips knocked us out somehow?"
    n "When that screen told us about a chip in our brains, I didn't really believe it..."
    k "It seems now we have proof."
    o "Yeah, for the time being, it seems like we should take what screen told us as fact."
    hide kaiser ind
    hide lauren ind
    with moveoutright
    show sam ind with moveinleft
    s "Hmm... damn."
    s "Lot of illegal shit going on here." #Arunj: Maybe use another word for explanation here to avoid redundancy
    n "If the screen wasn't lying about the brain chips, does that mean..."
    n "Does that mean it wasn't lying about having to kill each other?"
    s "The screen called this a {i}game{/i}."
    s "How disgusting."
    $mood = "ind"
    s "Either way, I don't think that's worth spending any more time on."
    s "We're finally all awake, we should try to figure out what's going on."
    s "We can't wait around in this {i}game{/i} and twiddle our thumbs until someone dies."
    s "Maybe if we find a way out of here, we can escape and no one will have to die."
    s "So that should be our goal. And hopefully the murderer will give us some time to do that."
    ni "We know the Game Master is one of us... would they really allow that?"
    ni "Well, perhaps they have their reasons for giving us a way out."
    n "Right. We should start exploring the train."
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .75
    show bert happy with dissolve:
        xcenter .25
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .15
        ycenter .25
        zoom .75
    bt "Maybe we can find the conductor!"
    hide popwow
    bt "They could stop the train for us."
    ni "That seems a little optimistic..."
    s "It's worth a shot."
    bt "That's the spirit! Poggers!"
    s "Plus, it's not like we're going to just sit around here."
    s "If anything we'd better hurry, otherwise the murderer might have time to plan a murder before we find a way out."
    ni "..."
    show sam ind:
        xcenter .75
        linear 0.3 xcenter .85
    show bert happy:
        xcenter .25
        linear 0.15 xcenter .15
    show frog sad with moveinbottom
    f "Wh-what should I do?"
    show bert ind
    f "I'm just a frog..."
    s "I keep forgetting there's a kid here too..."
    bt "It's probably best if Freddy doesn't get involved."
    hide sam with moveoutright
    hide bert happy with moveoutleft
    show frog sad:
        xcenter .5
        linear .3 xcenter .75
    show lauren ind with dissolve:
        xcenter .25
    o "We can sit together, buddy. We'll hang out here."
    f "{i}*sniffle*{/i} Okay miss."
    hide frog sad with moveoutright
    show lauren ind:
        linear .3 xcenter .5
    o "I can watch him, I used to babysit in high school."
    o "I don't want a kid involved in... whatever this is."
    n "That's probably smart. I'm not great with kids myself."
    o "The rest of you better search every corner of this train though."
    hide lauren ind with moveoutright
###########################################
###############INVESTIGATE#################
###########################################

    show stella happy with dissolve
    t "Great point by uhh, Lauren, is it?"
    t "Time to search - The whiskey could be hiding anywhere!"
    t "I'll check behind the bar."
    hide stella ind with moveoutright
    show bert ind with dissolve
    bt "..."
    hide bert ind
    play sfx "audio/sfxmoodup.mp3"
    show bert happy
    bt "Her motives may be skewed, but it's still helpful."
    bt "There might be food back there though, and we're going to need to eat."
    bt "I'll look with her."

    hide bert happy with moveoutright
    show shahar ind with dissolve
    h "Aye, I'll check the next car up. To the front with me!"
    h "The captain aught to be at the bow!"
    hide shahar ind with moveoutleft
    $ showchibint("bert", "catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "sid", "stella", "dracula")
    show sid ind with dissolve
    i "I'll go with, the uh, pirate. Why is there a pirate here again?"
    show sid ind:
        linear .3 xcenter .75
    show kaiser ind with dissolve:
        xcenter .25
    k "Not much makes sense at the moment."
    k "No point in getting caught up in it."
    i "Tr-true. Let's go with them."
    hide sid ind
    hide kaiser ind
    with moveoutleft
    $ showchibint("bert", "catherine", "lauren", "freddy", "jenny", "sam", "stella", "dracula")
    show jenny ind with dissolve
    j "Hmm, I'm going to go with them too. We should probably try to stay in groups."
    j "Plus, going to the front seems like the best way to find out where we're going."
    show jenny ind:
        linear .2 xcenter .6
    show catherine ind with dissolve:
        xcenter .38
    c "We're coming too!"
    show jenny ind with hpunch
    j "AHHHHH!"
    j "Catherine, your dumb cat just bit me!"
    show catherine happy
    c "Oops! Sorry, that's just Sesame's way of saying he's excited!"
    j "Ow..."
    c "Hehe, sorry! Alright Sesame, we're going exploring!"
    ses "Meowwwwww!"
    ni "..."

    hide jenny ind
    hide catherine ind
    with moveoutleft
    $ showchibint("bert", "lauren", "freddy", "sam", "stella", "dracula")

    ni "What a strange bunch."
    show sam ind with dissolve
    s "Okay, the rest of us can check the next car back."
    s "It looks like it's just the three of us."
    show sam ind:
        linear .3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "Very well."
    #hide drac ind
    show scary with dissolve:
        alpha .5
    menu:
        n "{i}Should I go with them?{/i}"

        "Yes":
            n "Alright."
            hide scary with dissolve

        "No":
            n "Actually, I might just stay here."
            hide scary with dissolve
    hide drac ind with moveoutleft
    s "Hey, Dan..."
    s "I know you might not be the guy to ask but..."
    s "Between you and me, I don't feel particularly comfortable being alone with him."
    show drac ind with moveinleft:
        rotate 45
        xcenter -.1
        ycenter .5
    n "With the, uh, vampire?"
    hide drac ind with moveoutleft
    s "Yeah. It'd be smarter of us to stay in groups of three or more."
    s "I'm wary of trusting anybody too much yet, especially after what the monitor said."
    s "Granted, if two people go off on their own and one dies it'd be pretty obvious who did it."
    s "But still, better safe than sorry."
    n "Alright. Let's go."

label backcar1:
    scene black with fade
    ni "We made our way one train car back, carefully watching our step between cars."
    show bg trainback at bg
    $ statusnt("Caboose", "dan", ch = 1, sun = 3)
    $ showchibint("dracula", "sam")
    with fade
    show sam ind with dissolve:
        xcenter .5
        linear 0.3 xcenter .75
    s "Hmmm... it seems awfully run down back here."
    s "There's a little cot, a bench, a water tank..."
    n "This must be where the train hands would sleep on long trips."
    hide sam with dissolve
    show drac ind with dissolve:
        xcenter .75
    d "I'd bet nobody's used this car in decades, though."
    d "There's dust coating nearly every surface... it reminds me of an old coffin."
    n "Maybe we can open a window or something."
    hide drac ind with dissolve
    show sam ind with dissolve:
        xcenter .75
    s "It seems like the only window is on the back door."
    hide sam with dissolve
    blank "Sam checked out the back window."
    show sam ind with dissolve:
        xcenter .75
    s "No such luck - it definitely isn't designed to be opened."
    $mood = "shock"
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    s "Also, this is the back of the train."
    n "Wait, we're at the backmost car already?"
    hide popwow
    hide sam with dissolve
    ni "Dracula and I checked the window as well."
    ni "Sure enough, the window was riveted on and there was nothing behind us."
    show sam ind with dissolve:
        xcenter .75
    s "The back door might open, but there's no platform to stand on. Let's wait for the others before doing that."
    $mood = "ind"
    s "It doesn't seem like there is anything useful back here, unless you're looking for a stretcher."
    n "Well, we definitely won't be needing that."
    hide sam  with dissolve
    show drac ind with dissolve:
        xcenter .75
    d "........"
    n "........"
    show drac oh:
        xcenter .75
    show sam ind with move:
        xcenter .25
    s "Anyway."

    hide drac oh with moveoutright

    show sam ind:
        xcenter .25
        linear 0.3 xcenter .75
    s "We should head back up and tell the others it's a dead end."
    n "Wait, there's a thin closet over there as well."
    n "Maybe there's something useful in it?"
    s "Worth a check."
    hide sam  with dissolve
    ni "Dracula tried to open the closet door, but it didn't open."
    show drac ind  with dissolve:
        xcenter .75
    d "The door is locked. Maybe one of the others has found a key."
    hide drac ind  with dissolve
    show sam ind  with dissolve:
        xcenter .75
    s "It's probably only for custodians. Maybe they'd have the key?"
    s "Either way, there's nothing more for us back here."
    n "Yeah, we should go back to the bar car."

label midcar2:
    scene bg trainmid at bg with fade
    $showchibint("sam", "freddy", "lauren", "bert", "stella", "dracula")
    $ statusnt("Bar Car", "dan", ch = 1, sun = 3)
    show lauren ind with dissolve
    o "Did you find anything useful?"
    n "Not really. The next car back is the caboose."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .55
        ycenter .275
        zoom .75
    o "So you didn't run into anyone?"
    o "The situation just keeps getting more grim."
    n "Yeah..."
    n "We should probably wait for everyone else to come back before going into too much detail."
    hide poptear
    hide lauren ind  with dissolve
    show stella drunk  with dissolve
    $mood = "shock"
    play sfx "audio/pophearts.mp3" volume .25
    show pophearts:
        xcenter .5
        ycenter .5
    t "Hey cutie, is there anything harder back there? Maybe some rum?"
    show stella drunk:
        xcenter .5
        linear 0.3 xcenter .75
    hide pophearts
    show bert sad with dissolve:
        xcenter .25
    bt "Hey, woah!"
    bt "Stella might be a little drunk. I tried to tell her not to drink, but..."
    t "Anyone need a beer? There's a lot ba-"
    hide bert sad  with dissolve
    show sam ind with dissolve:
        xcenter .25
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .15
        ycenter .25
        zoom .75
    s "I don't think you're taking this seriously enough."
    s "Plus, there are kids here. You really shouldn't be getting drunk."
    hide popwow
    t "You don't like alcohol?"
    s "I don't think that's relevant."
    $mood = "ind"
    t "Oh please, you twerps are no fun."
    hide stella drunk with moveoutright
    show stellapassed at bg with dissolve
    hide sam
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    s "I can already tell she's going to get on my nerves."
    s "Anyway, it's interesting how smooth of a ride this is."
    s "This train car looks like it's from the 60s, but it's the smoothest train I've ever been on."
    n "Maybe it's a very modern car, just decorated like this?"
    play sfx "audio/beep.mp3" volume .3
    show text "Attention!" with moveintop:
        ycenter .1
    pause 1
    hide text
    play sfx "audio/beep.mp3" volume .3
    show text "Stand Clear of the Closing Doors!" with moveintop:
        ycenter .1
    pause 1
    hide text with dissolve
    s "...What was that about?"
    n "It sounded like a PA system? It must be a pre-recorded message or something."
    s "There aren't even exit doors in this car..."
    s "Oh, the others are back."
    hide sam with dissolve
    blank "The front train car door opened, and Shahar, Jenny, Sid, and Catherine walked in."
    $showchibint("sam", "freddy", "lauren", "bert", "stella", "jenny", "shahar", "sid", "catherine", "dracula",  "kaiser")
    show jenny happy with dissolve
    j "Hey, you guys are back already!"
    show jenny happy:
        xcenter .5
        linear 0.3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "What was that peculiar alert we just heard?"
    j "What do you mean?"
    n "The train just told us to stand clear of the closing doors."
    j "Oh! That must be what that button does!"
    n "Huh?"
    n "..."
    d "Regardless."
    d "I cannot say I was particularly impressed by the back car."
    blank "Dracula spent a few minutes explaining the back car to everyone else."
    hide jenny happy with moveoutright
    show sid ind with moveinright:
        xcenter .75
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .75
        xcenter .85
        ycenter .25
    i "So it's a run down little caboose? That's kind of ironic."
    hide drac ind with moveoutleft
    hide pophuh
    show sam ind with moveinleft:
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
    $mood = "shock"
    n "Should we do anything about Stella? She's passed out behind the bar."
    h "A nap might do the lass some good."
    $mood = "ind"
    n "...Okay."
    ni "I hope we don't regret that leaving her here alone."

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
    show bg trainfront1 at bg
    $ showchibint("sam", "lauren", "bert", "jenny", "shahar", "sid", "catherine", "dracula", "freddy", "kaiser")
    $ statusnt("Front Car", "dan", ch = 1, sun = 3)
    with dissolve
    show sam ind with dissolve:
        xcenter .8
    s "Wow, you guys were not joking... There are screens everywhere."
    n "There must be over 20 monitors in this train car."
    n "Is that even practical? What are they showing?"
    show kaiser ind with moveinleft:
        xcenter .25
    k "It is quite an interesting setup..."
    k "There is a lot of information, but nothing useful for us."
    hide sam with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "I'm pretty good with technology, for a high schooler at least..."
    i "Let me have a go!"
    k "Good luck."
    k "These systems are much too advanced for a kid like you."
    show sid mad
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .75
        ycenter .25
        #zoom .75
    i "Tsk..."
    i "I'll show you..."
    hide sid ind with dissolve
    hide popmad
    show sidstand at bg with dissolve:
        zoom .9 xcenter .5 ycenter .46
    show bert ind with moveinright:
        xcenter .75
    bt "What do you mean by, nothing useful?"
    k "Well, we can see some technical aspects of the train."
    k "For example, I can tell you we're going 143 MPH."
    show sidstand at bg:
        zoom .9 xzoom -1 xcenter .5 ycenter .46
    k "But the controls are all either locked or password protected."
    k "So it seems like we can't stop the train or change the course."
    k "It also doesn't seem like we have access to any information that will help us in the game."
    hide kaiser ind with moveoutleft
    show catherine ind with moveinleft:
        xcenter .25
    c "This is also the frontmost car, which means..."
    hide bert with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "Nobody else is on the train. Damn."
    s "I guess expecting the Game Master to let someone else on the train to save us was too much..."
    c "No conductor and no way to control the train ourselves."
    c "To summarize, it's just these three train cars."
label showcars:
    scene black with fade
    show bg trainback with fade:
        zoom .7 xcenter .5 ycenter .5
    c "Starting from the back, a little caboose."
    d "A run down dusty little mess."
    show bg trainmid with fade:
        zoom .7 xcenter .5 ycenter .5
    c "Followed by the bar car behind us."
    k "Which has an... upscale 1970s aesthetic."
    show bg trainfront1 with fade:
        zoom .7 xcenter .5 ycenter .5
    c "And finally this, the front car, that we're in right now."
    n "Stuffed to the brim with screens and controls."
label frontcar2:
    scene bg trainfront1 at bg:
        zoom 1
    $ showchibint("sam", "lauren", "bert", "jenny", "shahar", "sid", "catherine", "dracula", "freddy", "kaiser")
    $ statusnt("Front Car", "dan", ch = 1, sun = 3)
    show sidstand at bg:
        zoom .9 xcenter .5 ycenter .46
    with fade
    show catherine ind with dissolve:
        xcenter .8
    c "We don't have too much to work with here..."
    c "And we still don't know where we're going."
    c "If we wait long enough will we arrive somewhere we can get off at? That'd be kind of boring."
    c "Or are we doomed to crash if a murder doesn't happen... that would be spicy!"
    c "Hmm.. if I were the Game Master, what would I do... would I make it boring or spicy?"
    ses "Mrow..."
    ni "What's with this girl..."
    show shahar ind with moveinleft:
        xcenter .25
    h "Arg. I say we crack a window n' make a jump for it!"
    ni "Is everyone here crazy?"
    h "Walk the plank, as ye say."
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
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .25
        ycenter .1
    f "No driver?"
    f "What are we going to do?... I'm scared..."
    f "I miss my mom..."
    n "Well whining about it won't help, so quit being such a brat." #Arunj: Make Dan ruder
    show jenny ind with dissolve:
        xcenter .75
    j "What's wrong with you, Dan? He's just a little kid."
    hide jenny ind
    show jenny happy:
        xcenter .75
    hide poprain with dissolve
    j "Hey it's okay Freddy! It's like an adventure."
    j "Come on, let's go back to the other train car and find something to play with."
    f "Okay."
    hide frog sad with moveoutbottom
    hide jenny happy
    show jenny ind:
         xcenter .75
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    j "You punk. We're stuck in here together, you know?"
    j "It wouldn't kill you to be cooperative."
    hide jenny ind with moveoutright
    $ showchibint("sam", "lauren", "bert", "shahar", "sid", "catherine", "dracula", "kaiser")
    #Arunj: Showchibi for Jenny/Freddy leaving
    show scary with dissolve:
        alpha .5
    ni "How can I cooperate after what that screen told us..."
    ni "I can't trust these people... even a child, like Freddy."
    ni "For all I know he's a super smart kid hellbent on killing us all as the Game Master."
    ni "Best to keep my guard up."
    hide scary with dissolve
    show sam ind with moveinleft:
        xcenter .25
    s "In any case..."
    s "We should make a plan."
    s "We can't just sit here and wait to find out where we're going."
    show lauren ind with moveinright:
        xcenter .75
    o "I agree. We should spend a little more time exploring before making any plans."
    o "Some of us haven't even seen the back car yet, so we should start there."
    s "Yeah, let's make sure we're staying in groups."
    s "Especially the kids, like Freddy and Sid."
    hide sidstand with dissolve
    show lauren ind:
        xcenter .75
        linear 0.3 xcenter .85
    show sam ind:
        xcenter .25
        linear 0.15 xcenter .15
    show sid mad with moveinbottom
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .5
        ycenter .25
        #zoom .75
    i "Hey! Who are you callin' a kid?!"
    i "I'm an honors student and I work four hours after school every day!"
    i "I'm a man!"
    s "Oh yeah? Any luck with the controls panel big guy?"
    show sid ind
    i "..."
    hide poptear
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .575
        ycenter .275
        zoom .75
    i "It locked me out after five attempts at the password..."
    s "Ha!"
    i "I'm outta here! You guys suck!"
    hide sid ind with dissolve
    $ showchibint("sam", "lauren", "bert", "shahar", "catherine", "dracula", "kaiser")
    show lauren ind:
        xcenter .85
        linear 0.3 xcenter .75
    show sam ind:
        xcenter .15
        linear 0.15 xcenter .25
    o "That was a little harsh."
    s "...Yeah, maybe, fine. I'll go apologize." #Arunj: Kind of out of character
    o "I'll come too. We shouldn't be starting fights over dumb things."
    o "We need to work together."
    o "After what that screen said, giving someone more reason to kill you is bad for all of us."
    s "Whatever... I'm heading to the bar car."
    hide lauren ind
    hide sam
    with dissolve
    show kaiser ind with dissolve
    k "I'm going as well. I haven't seen the back car yet."
    hide kaiser ind with dissolve
    $ showchibint("bert", "shahar", "catherine", "dracula")
    show bert sad with dissolve
    bt "I haven't yet either, but I want to spend a little more time up here first."
    bt "This feels like where we'll find the most answers."
    n "I'd like to take a closer look too."
    show bert sad:
        xcenter .5
        linear .3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "I am quite unfamiliar with everything I'm seeing up here."
    d "Illumination trapped in such curious containers..."
    ni "Is this guy really Dracula?"
    d "Perhaps we could talk through some things together?"
    hide bert sad
    show bert happy:
        xcenter .75
    bt "Yeah, of course! I just noticed a panel over here that seemed interesting."
    bt "It seems like there are three accessible switches, and a button."
    n "Ah, that makes sense."
    n "Jenny mentioned the button earlier."
    n "She pressed it up here, and it played the \"closing doors\" message over the intercom in the bar car."
    bt "True! And these switches..."
    $mood = "shock"
    n "We probably shouldn't try them haphazardl-"
    bt "Let's try them!"
    blank "Bert flipped the first switch."
    play sfx "audio/butt.mp3"
    show bg otrainfront
    hide drac ind
    show drac oh:
        xcenter .25
    $mood = "ind"
    n "So that's the light switch... Thankfully there's still a little sunlight."
    hide drac oh
    show drac ind:
        xcenter .25
    d "Interesting. It seems this car {i}does{/i} control the rest of the train."
    bt "Yeah. I think the three light switches correspond to the three train cars."
    bt "Plus, there's this little button that must be for the PA system that Jenny mentioned."
    blank "Bert flipped the first switch back."
    play sfx "audio/butt.mp3"
    show bg trainfront1 at bg
    bt "We're making progress already! Let's keep looking around."
label frontcar3:
    scene black with fade
    $noside = True
    blank "Thirty minutes passed."
    blank "Shahar and Catherine also left the Front Car."
    #Arunj: chibis through this whole scene
    $noside = False
    $mood = "sad"
    show bg trainfront1 at bg
    $ showchibint("bert", "dracula")
    $ statusnt("Front Car", "dan", ch = 1, sun = 3)
    show bert sad:
        xcenter .75
    show drac ind:
        xcenter .25
    with fade

    bt "Well, it seems like the others were right."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .775
        ycenter .275
        zoom .75
    bt "Despite all the stuff up here, it all seems password protected."
    bt "Hmm... maybe the Game Master is using this computer to control the game?"
    d "If anyone knows the password, it's probably the Game Master."
    d "It seems unlikely they would give the password to any of us."
    d "I am particularly intrigued by something."
    d "The password screens all have another value shown."
    d "For example..."
    show welcomescreenblank with dissolve
    d "What does 'users: 0' mean?"
    bt "Yeah, I was confused about that."
    bt "Nobody is logged in, so maybe that's what it means?"
    n "But if we were logged in, we would know it, we wouldn't need it to say 'users: 1'."
    bt "Also, what is 'Tead'?"
    bt "How am I even supposed to pronounce that? Like read or {i}read?{/i}"
    n "......."
    hide welcomescreenblank with dissolve
    bt "Either way, we can't log in, so it doesn't matter much."
    $mood = "ind"
    bt "We should head back to the bar car and meet up with the others."
    d "Agreed."
    hide bert sad
    hide drac ind
    with dissolve
    $ showchibint()
    ni "......"
    ni "Now that I'm alone..."
    ni "Maybe I can figure this out before the rest of them."
    play music "audio/invest1.wav" fadein 1.0
label passwording:
    show welcomescreenblank with dissolve
    $ passattempts = 1
    while passattempts < 10:
        $ password = renpy.input("What could it be? {color=00ff00}(Try typing in a password.){/color}", length=10)
        $ password = password.strip()
        if password == "DIR":
            ni "\"DIR\"? Who would think to make that their password? That's just not worth trying."
        else:
            if not password:
                $ password = "ERROR"
            play sfx "<from 0 to 1>audio/beep.mp3" volume .5
            ni "I don't think the password is '[password]'..."
        menu:
            ni "Maybe I should try again..."
            "It can't hurt...":
                if password != "DIR":
                    $ passattempts += 1
                if passattempts > 5:
                    ni "Hmm... The screen froze up."
                    ni "I must have gotten it wrong too many times, it's not letting me enter any more passwords."
                    ni "I guess I should go meet back up with the others."
                    jump donepasswording

            "I should go meet up with the others...":
                jump donepasswording
label donepasswording:
    hide welcomescreenblank with fade
    show bg trainfront1 at bg
    ni "They're probably waiting for me."
    ni "I can come back if I figure it out, but I don't want to take too long up here."
label midcar3:
    play music "audio/rush.mp3" fadein 1.0
    scene bg trainmid at bg
    $ showchibint("stella", "freddy", "sam", "lauren", "jenny", "bert", "shahar", "sid", "catherine", "dracula", "kaiser")
    $ statusnt("Bar Car", "dan", ch = 1, sun = 3)
    with fade
    show jenny ind with dissolve
    j "Hey, Bert found some food behind the bar!"
    hide jenny ind
    show jenny happy
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
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .765
        ycenter .25
        zoom .75
    j "I feel a little bad for Catherine..."
    j "She's a vegetarian, so she's only been eating the nuts and bread."
    o "Plus, there's no cat food. Sesame's been eating the turkey from the sandwiches."
    hide lauren ind with moveoutleft
    show catherine happy with moveinleft:
        xcenter .25
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .25
        ycenter .5
    c "We're the perfect match! He eats the meat, I eat the rest!"
    ses "Mrow!"
    hide pophearts
    c "Don't worry about us!"
    c "It's still nice to relax and eat for a bit."
    ses "mewmewmewmew!"
    scene black with fade
    $mood = "happy"
    ni "It feels... surprisingly nice having a communal meal."
    $noside = True
    blank "They ate; about an hour passed."
    $noside = False
    scene bg ntrainmid at bg
    show frogsit at bg
    $ showchibint("stella", "freddy", "sam", "lauren", "jenny", "bert", "shahar", "sid", "catherine", "dracula", "kaiser")
    $ statusnt("Bar Car", "dan", ch = 1, sun = 4)
    with fade
    show kaiser ind with dissolve:
        xcenter .75
    show jenny ind with dissolve:
        xcenter .25
    $mood = "ind"
    j "Thankfully there's food on the train. It would have been an even bigger disaster otherwise."
    ni "I'll refrain from asking how many days of food we have for now..."
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
    show jenny happy
    j "Get black out drunk and pass out on the floor?"
    show jenny ind
    k "Well, sleep. It is getting late, and we've been at it all day."
    k "Both the frog kid and the pirate guy have already fallen asleep over there."
    k "We should figure out the rest of the sleeping arrangements."
    n "The train is pretty cramped, there definitely aren't nine more chairs or beds for us."
    hide jenny ind with moveoutleft
    show bert ind with moveinleft:
        xcenter .25
    bt "There are five more chairs in this car, and then a bed and a bench in the caboose."
    bt "So that leaves... two people's beds unaccounted for."
    hide kaiser ind with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "If I may add - Do not worry about my sleeping arrangements."
    d "There is no need."
    n "Why's that?"
    d "I simply do not sleep."
    n "..."
    bt "..."
    d "..."
    bt "Okay, so only one more bed to account for."
    hide drac ind with moveoutright
    $ showchibint("stella", "freddy", "sam", "lauren", "jenny", "bert", "shahar", "sid", "catherine", "kaiser")

    show kaiser ind with moveinright:
        xcenter .75
    k "I'm content sleeping on the floor in the front car, if it makes it easier for the young ones."
    n "There's probably an extra blanket or pillow around somewhere."
    k "It is fine. I am used to poor sleeping conditions."
    k "With that taken care of. Goodnight all."
    hide kaiser ind with moveoutright
    $ showchibint("stella", "freddy", "sam", "lauren", "jenny", "bert", "shahar", "sid", "catherine")

    bt "Well, as long as that's taken care of. G'night Dan!"
    hide bert with moveoutleft
    show sid ind with dissolve:
        xcenter .25
    show sam ind with dissolve:
        xcenter .75
    i "So, two of us three are in the back car?"
    s "It's so dusty back there... Maybe we should all just squeeze in here somehow?"
    n "I don't think there's enough space in here. It's just a bar car after all."
    n "I can sleep in the back car, I don't mind."
    show sid ind:
        linear .3 xcenter .35
    i "Me too! I can handle it."
    s "Sid, are you sure? If it's too dusty for you I can sleep back there."
    show sid ind: #Arunj: Sid movement kinda weird
        linear .3 xcenter .45
    i "I'm used to sharing one bed with my whole family! This is a practically an upgrade!"
    hide sid ind with moveoutleft
    show sam ind:
        linear .3 xcenter .5
    s "Well, that settles it I guess."
    s "And Dan?"
    s "Keep an eye on him back there..."
    s "I know neither of us are really kid people but, I don't want anything bad to happen to them." #Arunj: Edgier?
    n "Anything... bad?"
    s "Goodnight Dan."
    hide sam with dissolve
    n "..."
    scene black with fade
    $noside = True
    blank "Dan made his way to the back car."
    $noside = False
    show bg ntrainback at bg
    $ statusnt("Caboose", "dan", ch = 1, sun = 4)
    $ showchibint("sid")
    with dissolve
    ni "I forgot how dusty it was back here."
    show sid ind with dissolve
    i "Wow, there's even an old school water kettle back here!"
    n "This is probably where some of the train workers slept."
    n "Hence the bed, kettle, and closet."
    i "That sounds so..."
    hide sid ind
    show sid happy
    $mood = "happy"
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .5
        ycenter .5
    i "Exciting!"
    i "I wish I could travel and live on cool trains like this."
    n "You're still young, Sid, maybe you can one day."
    hide pophearts
    show sid mad
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .4
        ycenter .275
        zoom .75
    i "What do you mean, young?"
    hide popwow
    i "I work my ass off to help my family!"
    i "You don't know what I've been through."
    show scary with dissolve:
        alpha .5
    ni "It's kinda funny... this punk reminds me of myself when I was his age."
    ni "Back and forth in the snap of a finger."
    ni "Taking myself way too seriously, blatant disrespect for authority..."
    ni "Kinda badass. I can respect that."
    hide scary with dissolve
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
    $mood = "ind"
    n "Yeah, none of us could figure out the password. We can't do anything without it."
    i "Well, I got to the file directory, but it wouldn't let me open anything up."
    n "What? You got to the file directory? How did you do that?"
    i "I work with computers a lot when I'm helping my dad with the shop."
    i "A lot of computers let you check for files using the \"DIR\" command." #Make this nerdier later
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
    i "We could figure out how much time we have."
    i "If we have time, the murderer could give us time to find a way out if they're feeling nice!"
    show scary with dissolve:
        alpha .5
    ni "And... \"participants\". I wonder if that's about... us."
    ni "If it is, maybe that file could tell us why we're all here..."
    ni "Maybe the Game Master's not in the file. If so, it would tell us who's behind all this."
    ni "If I could find them... I could kill them... and end this mess."
    ni "After all, the screen never said people who weren't chosen couldn't murder people."
    ni "If I know I'm innocent, why shouldn't I try to kill someone to maximize my chances of surviving?"
    hide scary with dissolve
    i "That's not all, though!"
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
    $mood = "happy"
    n "Either way, Sid, this is a huge find!"
    hide sid ind
    show sid happy
    i "Haha, really, it's nothing..."
    n "Let's keep this between you and me for now."
    n "This might come in handy, but I don't think we should share it with everyone just yet."
    hide sid happy
    show sid ind
    i "Yeah... I don't trust some of these people."
    $mood = "ind"
    i "The pirate guy and the vampire guy scare me, and that French lady is such a drunk hag."
    i "I think the pirate and vampire are hiding something."
    i "And the rich lady would have tons of money, enough to hire people to kidnap all of us."
    ni "Hm..."
    ni "There's no chance a Game Master would reveal this kind of information to me, right?"
    ni "Building trust with someone gives me one less candidate to murder, if nothing else."
    n "I'm with you. Let's stick together Sid."
    i "D-deal!"
    play sfx "audio/butt.mp3" volume .5
    stop music fadeout 1.0
    show bg notrainback at bg
    i "Huh?"
    n "Hmm, someone must have hit the light switch."
    n "We found all three light switches in the front car earlier."
    i "That should make it a little easier to sleep."
    n "Yeah, let's hit the hay. We can figure out some more plans in the morning."
    i "You can have the bed. I'm fine sleeping on the bench."
    n "Okay, you can have the bed tomorrow night."
    ni "Damn... the thought of still being on this train tomorrow night is..."
    i "Is something wrong?"
    n "No, not at all. Goodnight Sid."
    hide sid ind with dissolve
label day2:
    scene black with fade
    pause 1
    $noside = True
    blank "The next morning..." #Big transition here?
    $noside = False
    play music "audio/rush.mp3" fadein 1.0
    scene bg trainback at bg
    $ statusnt("Caboose", "dan", ch = 1, sun = 1)
    $ showchibint("sid")
    with dissolve
#    #show chaptericon at topright:
#        zoom .4
#    show mapicon:
#        xcenter .965
#        ycenter .12
#        zoom .3
#    show evidenceicon:
#        xcenter .91
#        ycenter .12
#        zoom .3
    show sid happy with dissolve:
        xcenter .5
        linear .3 xcenter .75
    i "'Morning Dan!"
    n "Huh? Oh, Sid... What time is it?"
    i "No idea, but the sun's up. I'm heading to the bar car to the others."
    hide sid happy with moveoutright
    $ showchibint()
    ni "That kid's got a lot of energy. It must be around 7 AM."
    $noside = True
    blank "Dan walked to the back window."
    $noside = False
    show tracks with dissolve
    ni "Damn... There really isn't anything out there..."
    $mood = "sad"
    ni "It'd be a lot easier to be hopeful if there were {i}any{/i} signs of life."
    ni "But it's hard to be hopeful in the middle of nowhere..."
    ni "If nothing changes, maybe I need to take this into my own hands..."
    hide tracks with dissolve
    $mood = "ind"
    ni "But for now, I should go meet the others."
label testft:
    scene bg trainmid at bg
    $ showchibint("jenny", "stella", "lauren", "freddy", "sid", "bert", "catherine", "kaiser", "sam", "dracula")
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    with fade
    show catherine happy with dissolve:
        xcenter .5
        linear .3 xcenter .75
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .75
        ycenter .5
    c "Gooooooood morning Dan! It's another gorgeous day on the Nowhere Express!"
    hide pophearts
    show frog happy with moveinleft:
        xcenter .25
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .25
        ycenter .5
    f "Yeah! Gorgeous day!"
    hide pophearts
    c "Come get your gourmet turkey sandwiches and half-sized cans of soda!"
    f "Soda for breakfast! Wooo!"
    n "How are you guys so peppy?"
    f "Come on Sesame, let's go play!"
    ses "Merowwwwww!"
    hide frog ind with moveoutleft
    hide catherine happy
    show catherine2 happy:
        xcenter .75
    with dissolve
    c "Nothing we can do but try to enjoy ourselves a little!"
    show sid ind with moveinleft:
        xcenter .25
    c "How'd you guys sleep back there?"
    i "The bench kinda hurt my back... but I'll manage."
    hide catherine2 happy
    show catherine2 ind:
        xcenter .75
    $mood = "shock"
    c "Dan! You took the cot for yourself and made Sid sleep on the bench?"
    n "Huh? No, he insisted."
    i "I did I did!"
    c "Hmph. For shame."
    hide catherine2 ind with moveoutright
    i "..."
    hide sid ind with moveoutleft
    show sam ind with dissolve:
        xcenter .5
        linear .3 xcenter .75
    $mood = "ind"
    s "I wouldn't worry about her being upset with you."
    s "She was up late with Freddy making sure he wasn't freaking out too much."
    show bert happy with dissolve:
        xcenter .25
    bt "It was pretty heartwarming, all things considered."
    bt "I'm glad we're all still staying optimistic."
    bt "We're gonna figure this out and get off this train!"
    s "Agreed."
    ni "..."
    s "We should wait for everyone to wake up and have a meeting."
    s "We've explored the train, but we need to figure out a plan."
    bt "Let's meet back here in 30 minutes! Break!"
    hide bert happy
    hide sam
    with dissolve
    $showchibint("jenny", "stella", "lauren", "freddy", "sid")
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
   #JULIAN note to self

    tut "Throughout the game, there will be free time segments."
    tut "In these segments, you will have the opportunity to talk with other participants and get to know them better."
    tut "You can use the map icon, in the top right, to navigate around the train and find people."
    tut "Click on someone's face in the top-left corner to initiate a conversation with them."
    tut "You can spend up to three free times with each participant."
    tut "The friendship menu, accessed using the heart icon in the top right, will show how many times you've talked to each participant."
    tut "Free time segments will not impact the main story."
    tut "If you are not interested in talking to anyone, you can use the skip icon in the top-right to skip the free time event."
    tut "For the first free time segment, move to the front car and talk to Bert."
    tut "For this segment only, the skip function will be disabled."

    call screen midCar with fade
    # show stella ind with dissolve
    # t "Oh? So you've got nobody better to chat with?"
    # bt "Well, we should get to know each other."
    # t "Hmph. I don't {i}mind{/i} that, but don't get the wrong idea."
    # t "I'm not into younger men."
    # bt "Oh, I didn't mean like th-"
    # hide stella ind
    # show stella happy
    # t "Okay, okay, you caught me, so I {i}am{/i} into younger men."
    # t "But we just met! Wine and wine me a little first, huh?"
    # bt "Don't you mean wine and {i}dine{/i}?"
    # hide stella happy
    # show stella bigsmile
    # t "Deal!"
    # bt "Wait, I-"
    # t "You're a sweetheart. It's a shame someone like you is stuck in a situation like this."
    # hide stella bigsmile
    # show stella happy
    # t "It's been fun chatting. We should spend some more time together soon."
    # hide stella happy with dissolve
    # bi "I - what?"
    # scene black with fade
label postFT0:
    scene bg trainmid at bg
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    with dissolve
    ni "Hmm... that didn't take up as much time as I hoped it would."
    ni "Guess I'll keep mingling."
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    tut "For this and all future free time segments, you will have the luxury of talking to anyone or skipping."
    $ftecounter = 1
    call screen midCar with dissolve
label postFT1:
    scene black with fade
    blank "Thirty minutes had passed, so Dan went to meet the others in the bar car."

label midcar4:
    scene bg trainmid at bg
    $ statusnt("Bar Car", "dan", ch = 1, sun = 2)
    $ showchibint("bert", "catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "shahar", "sid", "stella", "dracula")
    with fade
    show bert ind with dissolve:
        xcenter .5
        linear .3 xcenter .75
    $mood = "ind"
    bt "Alright, I think everyone's here."
    bt "It's starting to seem like we've exhausted our resources."
    bt "I've searched every inch of this train and feel no closer to finding anything useful."
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
    j "Well... think back to that one message."
    show expl 3a
    show sepia:
        alpha .5
    with dissolve
    $noside = True
    scr "Eleven were unwillingly forced to participate."
    scr "The remaining person is the Game Master behind all of this, who will also participate."
    $noside = False
    hide expl 3a
    hide sepia
    with dissolve
    j "I think the implication is that whoever planned all this..."
    j "Is one of us."
    hide kaiser ind with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    o "Do you really think the person behind the messages is here right now?"
    hide jenny ind with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "I'm worried that Jenny's right."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    s "Otherwise, what's even the point of all this?"
    $mood = "shock"
    n "Huh?"
    hide popwow
    s "Well, if this is some messed up game for them, they're probably here to watch."
    s "I haven't seen a single camera on board, so if they wanted to enjoy it, that's probably the only way."
    o "They're here to 'Enjoy it?' Sam, you sound a little hysterical..."
    s "We've been kidnapped, basically twice now, and have zero information on what the hell's happening."
    s "If they wanted us dead, they could have killed us when they kidnapped us. Instead we're playing this game."
    s "Not to mention I'm stuck on a train with Dracula and a pirate."
    s "And you're telling me I'm hysterical for being confused?"
    o "..."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .28
        ycenter .25
        zoom .75
    o "Fair enough."
    o "What do you think we should do about it?"
    hide poptear
    hide sam with moveoutright
    show sid ind with moveinright:
        xcenter .75
    $mood = "ind"
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
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .75
        ycenter .7
        zoom .75
    $mood = "sad"
    t "Why do you have such chiseled abs?"
    hide stella bigsmile
    hide pophearts
    show sid ind:
        xcenter .75
    i "Shut up, Stella."
    h "Aye. Ye see, me memory in't too good."
    h "Last I remember, me and me hearties were three sheets to the wind, mindin' our own."
    h "Next minute, I come to in the little crow's nest wit' the rest of ye."
    i "I..."
    $mood = "ind"
    i "I don't really know what he just said."
    hide shahar ind with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "I find it quite curious that {i}you{/i} called {i}me{/i} suspicious."
    show drac ind:
        xcenter .25
        linear .1 xcenter .3
    d "As such a little cutpurse yourself, that is."
    show sid happy:
        xcenter .75
        linear .1 xcenter .78
    play sfx "<from 0 to 1>audio/mildshock.mp3" volume .2
    i "Wh-what? Me? No way!"
    $mood = "shock"
    d "Oh? I'm sure you'll be happy to empty your pockets then."
    i "I-I-I can't."
    d "Interesting."
    hide sid happy with moveoutright
    show drac ind:
        linear .3 xcenter .5
    d "What a silly coincidence, I put a whiskey shooter in my pocket earlier, but..."
    d "It's just so happen to go missing earlier when Sid and I were alone together in the front car."
    $mood = "ind"
    d "Regardless, I've been nothing but productive and friendly since we woke up here yesterday."
    d "I'm sure you all believe me when I say I am just as dumbfounded as the rest of you."
    hide drac ind with dissolve
    show catherine ind with dissolve
    play sfx "audio/poprain.mp3" volume .5
    show poprain:
        xcenter .5
        ycenter .1
    c "Guys, I don't think this is very productive."
    c "Throwing around accusations isn't going to get us anywhere."
    hide poprain with dissolve
    show catherine ind:
        linear .3 xcenter .75
    show jenny ind with dissolve:
        linear .3 xcenter .25
    j "If one of us is the mole though, it should be our highest priority to figure out who it is."
    c "That's true..."
    $mood = "happy"
    c "Maybe we should just... Talk more about ourselves?"
    c "Even if it doesn't help figure out who the mole is, it'd be good to learn more about each other."
    j "Yeah, we're all stuck in here together anyway."
    $mood = "ind"
    c "With that said, I don't feel particularly notable..."
    c "I'm just a worker at a shelter... I like rock climbing... Long walks on the beach..."
    hide catherine ind with moveoutright
    show bert ind with moveinright:
        xcenter .75
    bt "As interesting as that stuff is, maybe we should be focused more on... More extreme things."
    bt "Reasons why someone might want to kidnap us, for example."
    ni "..."

    #############################################################################################################################################################################

    hide jenny ind with moveoutleft
    show stella ind with moveinleft:
        xcenter .25
    t "Look, darlings... If it helps clear things up, I should probably admit..."
    t "As a wildly successful businesswoman - some might even say the René Laennec of our time - I've inevitably built up a... reputation."
    t "I've done what I had to do to get to the top, and I've made many enemies along the way."
    n "What do you mean, 'done what you had to do'?"
    $mood = "shock"
    t "I tore down competition, I burned bridges, you name it."
    t "My methods don't always see eye-to-eye with the law, but, c'est la vie."
    ni "Is this lady for real?"
    bt "That... Definitely seems like a reason to have enemies."
    $mood = "ind"
    show stella happy:
        xcenter .25
    t "It feels oddly freeing to not have my bodyguards and assistants around, saying:"
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .35
        ycenter .25
        zoom .75
    t "\"Ms. Cantoire! Put down the vodka!\" \"Ms. Cantoire, don't put your head out the limousine sunroof!\""
    bt "..."
    n "..."
    show stella ind:
        xcenter .25
    t "Of course, I am not the mole. It'd be a waste of my time."
    t "I have nothing to gain from... this."
    t "I'm only telling you all this so that you're not surprised when my past inevitably comes up."
    t "And sadly, I have no insight on who it might be."
    t "I'm rich enough to put this together, but there are... easier ways to entertain oneself with money."
    hide stella ind with moveoutleft
    bt "..."
    bt "Well at least she's being open about it."
    show sam ind with moveinleft:
        xcenter .25
    s "If we're airing out our past, I can go next."
    s "I don't have quite the same pedigree, but..."
    s "I used to sell drugs, mostly to upper-class business people and spoiled rich kids."
    $mood = "sad"
    s "I'd like to say I don't regret it, but..."
    s "The drugs weren't always safe."
    bt "Not safe? What do you mean?"
    s "A lot of the stuff I moved was untested and highly experimental."
    s "But those dumb suits didn't know that, so they bought it."
    n "Did it ever end up killing anyone?"
    s "Honestly? I don't even know."
    s "That stuff's behind me, and it's hard to think about sometimes, so I try not to."
    s "But I do know I at {i}least{/i} pissed some people off. I wouldn't be surprised if that's part of why I'm here."
    s "It's hard to come to terms with some of this stuff..."
    s "Maybe I deserve this."
    bt "Hey, don't say that! No way."
    bt "We've all made mistakes, and owning up to it now can help us figure this out."
    bt "Any information we can gather is progress."
    bt "Does anyone else have anything they want to bring up?"
    ni "..."
    show scary with dissolve:
        alpha .2
    $mood = "shock"
    ni "Should... Should I speak up?"
    #play sfx "<from 0 to 3>audio/jaws.mp3" volume .1
    show scary:
        linear .3 alpha .5
    ni "I... don't think they'd understand."
    show scary:
        linear .3 alpha .8
    ni "This might be my only opportunity though."
    show scary:
        linear .3 alpha .95
    ni "Maybe I should speak up."
    hide scary
    bt "I guess I'll go next."
    $mood = "ind"
    bt "It's not exactly the same as Stella's or Sam's, but..."
    hide sam with moveoutleft
    show bert ind:
        linear .3 xcenter .5
    bt "I guess I can't think of anything else."
    ni "This kid just bailed me out of speaking up..."
    bt "I was only twenty, too. It feels like so long ago but I think about it every day."
    bt "I was driving after tutoring, same as always."
    bt "It was spring..."
    bt "And this lady... she just... walked out..."
    bt "Into the road..."
    bt "......."
    ni "He's all choked up."
    show bert sad:
        linear .3 xcenter .75
    show lauren ind with dissolve:
        xcenter .25
    o "Alright, we're done with this."
    o "I can't sit by and watch you guys talk about stuff like this."
    o "For all we know our pasts aren't even relevant."
    hide bert sad with moveoutright
    show stella ind with moveinright:
        xcenter .75
    t "If the kid wants to talk, let him."
    t "It can't hurt."
    t "Plus, remember when that screen said our endings are deserved?"
    t "It must be something about our pasts, why else would we \"deserve\" this?"
    o "It's clearly a sensitive topic for him."
    o "We don't need to make this situation any shittier."
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .75
        ycenter .25
        #zoom .75
    t "Hmph, just when I thought we were going to get into the juicy stuff..."
    hide stella ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "I don't think we should force anyone to talk about sensitive topics, but..."
    j "I am starting to worry we're not going to get anywhere."
    j "We could just wait until we get to our destination, but we have no idea how long that'll take."
    o "We're almost out of food, too..."
    show scary:
        alpha 0
        linear .3 alpha .5
    ni "And morale."
    ni "Maybe I really do need to take this into my own hands..."
    ni "If we don't make any progress by midnight, I have some guesses..."
    ni "Maybe tomorrow morning I should..."
    hide scary with dissolve
    show jenny ind:
        xcenter .75
        linear 0.3 xcenter .80
    show lauren ind:
        xcenter .25
        linear 0.15 xcenter .2
    show frog ind with dissolve
    f "Can we go to sleep? I'm tired..."
    j "Maybe we should just call it a day."
    j "I don't see us getting anywhere with this."
    o "Alright, let's divide up the food for tonight."
    hide jenny ind
    hide lauren ind
    hide frog ind
    with dissolve
label midcar5:
    scene black with dissolve
    $noside = True
    blank "They shared the rest of their rationed non-alcoholic food and drinks amongst themselves."
    blank "There was much less talking tonight."
    $noside = False
    scene bg ntrainmid at bg
    $ showchibint("bert", "catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "shahar", "sid", "stella", "dracula")
    $ statusnt("Bar Car", "dan", ch = 1, sun = 4)
    show frogsit at bg
    with dissolve
    show lauren ind with dissolve:
        xcenter .3
        linear .3 xcenter .75
    o "I think I'm going to spend some time on the computers in the front car."
    o "Who knows, maybe with a little luck we can figure out the passwords."
    show sam ind with moveinleft:
        xcenter .25
    s "Yeah, I'll come too. I'm not very tired yet."
    hide sam
    hide lauren ind
    with moveoutleft
    $ showchibint("bert", "catherine", "freddy", "jenny", "kaiser", "shahar", "sid", "stella", "dracula")
    show kaiser ind:
        xcenter .25
    show shahar ind:
        xcenter .75
    with moveinright
    h "I feel a bit guilty, lads."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .8
        ycenter .275
        zoom .75
    h "I want to 'figure out the passwords', as ye say, but I ain't much help when it comes to techlonogy..."
    k "There's no harm in trying."
    hide poptear
    k "Random words and phrases are as good a guess as any."
    k "We might as well head up to the front as well."
    hide kaiser ind
    hide shahar ind
    with moveoutleft
    $ showchibint("bert", "catherine", "freddy", "jenny", "sid", "stella", "dracula")
    show sid ind with dissolve
    i "Hey Dan."
    i "I'm starting to get tired."
    i "I'm gunna hit the hay."
    play sfx "audio/butt.mp3" volume .1
    hide sid ind
    show sid happy
    show bg notrainmid at bg
#    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .45
        ycenter .25
        zoom .75
    n "!"
    n "I guess they hit the light switch in the front car, since everyone's going to sleep soon anyway."
    ni "It's pretty hard to see in here with the lights off."
    n "I'll come too, Sid."
    scene black with dissolve
    $noside = True
    blank "They made their way to the back car."
    $noside = False
    scene bg notrainback at bg
    $ showchibint("sid")
    $ statusnt("Caboose", "dan", ch = 1, sun = 4)
    with dissolve
    show sid ind with dissolve
    i "Well, goodnight Dan!" #Arun: Lights off
    n "Hey, Sid. Before you sleep. How are you, well, feeling? About everything."
    i "Well, it's a little scary I suppose."
    i "We're all out of food, and some of the people on board are suspicious..."
    hide sid ind
    show sid smile
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .5
        ycenter .5
    i "But I'm hopeful."
    n "Hopeful?"
    hide pophearts
    i "Yeah! I think we're gunna get off this train, safe and sound."
    i "After all, I have stuff to do! I'm gunna show my family the world!"
    $mood = "happy"
    ni "Damn right you will, kid."
    n "You can have the bed tonight."
    n "I'll sleep on the bench."
    i "Wahoo!"
    $mood = "ind"
    i "A-are you sure though? I don't mind sleeping on the bench."
    n "Yeah, I don't think I'm going to go to sleep yet anyway."
    i "Okay! Goodnight Dan."
    hide sid smile with dissolve
    ni "....."
    ni "I can already hear him snoring."
    ni "It almost makes me feel bad..."
    ni "Wait - what is that?"
    show ntracks with fade
    ni "There's something hanging outside the window, about a foot from the glass."
    ni "It looks like a coin, or maybe a cufflink?"
    ni "I don't think that was there this morning..."
    ni "I guess somebody put that out there earlier today."
    ni "It doesn't seem worth the risk to open the door and get it though..."
    ni "Whatever..."
    show start2
    show sepia:
        alpha .5
    with dissolve
    scr "Their endings are deserved."
    hide start2
    hide sepia
    with dissolve
    ni "What a shame... I just got out of the pen, and now I have to murder again..."
    ni "At least there are a lot of easy targe-{p=0.5}{nw}" #Arun: BIG NOISE, cut off music
    stop music
    show scary:
        alpha 1.0
    play sfx "audio/shatter.mp3"
#    queue sfx "audio/stab.mp3"
    $mood = "shock"
    ni "Wh-what?"
    ni "Everything's... dark."
label midcar6:
    scene black with fade
    $dan = False
    $mood = "sad"
    $noside = True
    $renpy.pause(1.0, hard = True)
    blank "..."
    blank "............."
    blank ".........................."
    $noside = False
    bi "What a sticky situation."
    bi "We've got a bunch of random people stuck on a train."
    bi "Nobody knows what's going on, and to top it all off,"
    bi "we're out of food and water... but, still..."
    bi "I can't help but think..."
    $mood = "happy"
    bi "We can get out of here. Together."
    blank "pssst!!!"
    play music "audio/invest1.wav"
    scene bg notrainmid at bg
    $ showchibint("catherine", "freddy", "jenny", "stella", "dracula")
    $ statusnt("Bar Car", "bert", ch = 1, sun = 4)
    with dissolve
    show stella happy with dissolve:
        linear .3 xcenter .75
    $mood = "ind"
    t "psssst!"
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    t "Hey Bert! Wanna take some shots with us?"
    show drac ind with moveinleft:
        xcenter .25
    d "Stella made me a bloody mary, but without tomato juice or hot sauce."
    bi "Huh?"
    t "Yeah! I call it, 'vodka'!"
    hide drac ind
    show drac happy:
        xcenter .25
    d "Marvelous, really."
    $mood = "sad"
    bi "Is it really a good idea to drink when we're out of food?"
    b "I think I'm going to try and sleep."
    hide stella happy
    show stella ind:
        xcenter .75
    hide drac happy
    show drac ind:
        xcenter .25
    t "Suit yourself."
    hide drac ind
    hide stella ind
    with dissolve
    show catherine ind with moveinleft
    $mood = "happy"
    c "Okay, Freddy is asleep. I'm going to go say goodnight to Dan and Sid in the back car and then hit the hay."
    b "Tell them I say goodnight too!"
    hide catherine ind with dissolve
    show catback at bg with dissolve:
        zoom 1.2
        xcenter .43
        ycenter .5
    show jenny ind:
        xcenter .55
    show frog ind:
        xcenter .8
    with moveinright
    j "It is getting pretty late..."
    j "Hey Bert, do you thin-{p=0.5}{nw}"
    stop music
    show scary:
        alpha 0
        linear .2 alpha 1
    $mood = "shock"
    j "W-what?"
    b "What's going on?"
    t "Who did that? Knock it off!"
    d "Where is everyone?"
    play sfx "audio/shatter.mp3"
#    blank "A sharp sound suddenly filled the train car momentarily."
    f "Ahhh! Mommy!"
    bi "It sounded like the world's biggest chandelier fell."
    j "I'm scared!"
    play sfx "audio/beep.mp3" volume .1
    z "AHHHHHH!!!"
    bi "Oh no."
    bi "Was that a... scream?"
    d "Who was that? Is everyone okay?"
    t "It came from the front car!"
    hide scary with dissolve
    play music "audio/ominous.mp3" fadein 1.0
    j "Bert! You're okay. Thank goodness."
    hide jenny ind
    hide frog ind
    with dissolve
    hide catback with dissolve
    show catherine ind with dissolve:
        xcenter .75
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        xcenter .6
        ycenter .25
        zoom .75
    c "What was that? Why couldn't we see anything?"
    $mood = "sad"
    b "I don't know, but we need to go check out the front car."
    show frog ind with moveinleft:
        xcenter .25
    c "I'll stay here with Freddy and Sesame."
    f "W-what's going on? I'm scared..."
    hide catherine ind
    hide frog ind
    with moveoutright
    show stella ind with moveinleft:
        xcenter .25
    t "The rest of us should go to the front car, together."
    b "Agreed."
    scene black with fade
    $noside = True
    blank "The four of them - Bert, Stella, Dracula, and Jenny - made their way to the front car."
    $noside = False
    scene bg notrainfront at bg
    $ showchibint("jenny", "kaiser", "lauren", "sam", "shahar", "stella", "dracula")
    $ statusnt("Front Car", "bert", ch = 1, sun = 4)
    with dissolve
    show lauren ind with moveinleft
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .45
        ycenter .25
        zoom .75
    o "What's going on?"
    hide popwow
    show lauren ind:
        linear .3 xcenter .75
    show sam ind with dissolve:
        xcenter .25
    s "Did your car go dark too?"
    hide lauren ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "Yeah, but more importantly..."
    j "What about that scream?"
    j "Who was that?"
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        xcenter .35
        ycenter .25
        zoom .75
    s "Scream? What do you mean?"
    hide sam with moveoutleft
    show kaiser ind with moveinleft:
        xcenter .25
    k "We didn't hear anything like that up here."
    b "Really? I could have sworn it came from the front car..."
    j "Maybe it was just one of us in the bar car when it got dark."
    j "Speaking of which, you said it got dark in this car too?"
    k "Yes, almost like an eclipse. But the computer screens stayed on and gave us some light."
    b "Well that's good."
    b "... But..."
    $mood = "shock"
    b "Oh no."
    j "What's wrong?"
    b "Where's Sid? And Dan?"
    $mood = "sad"
    b "Maybe we were wrong and the scream came from their car..."
    b "Plus, they were in the back car, but surely they'd be here by now."
    k "Perhaps they are asleep? Slept through the whole event."
    b "Even then... that noise. They would have heard it for sure."
    hide kaiser ind with moveoutleft
    show shahar ind with moveinleft:
        xcenter .25
    h "What are ye on about?"
    hide jenny ind with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "He's right, there's no way they slept through that noise."
    d "As well, it sounded like it came from the back car."
    b "We have to check on them."
    scene black with fade
    stop music fadeout 1.0
    $noside = True
    blank "The eight of them ran to the bar car as fast as they could."
    blank "Catherine and Freddy joined them on the way to the caboose."
    blank "But when they got there..."
    $noside = False
    $mood = "shock"
    play music "audio/sadsong.mp3" fadein 2.0
    scene bg bodytrainback at bg
    $ showchibint("catherine", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "stella", "dracula", "sid")
    $ statusnt("Caboose", "bert", ch = 1, sun = 4)
    with Dissolve(2.0)
    b "Oh no..."
    b "No no no no..."
    show sid ind with moveinleft:
        xcenter .25
    i "I... I..."
    b "Sid..."
    b "What happened..."
    show sam angry with moveinright:
        xcenter .75
    s "What the hell..."
    s "Is he... dead?"
    s "Sid, you... did you kill Dan?"
    i "No! I was asleep, I... I didn't do anything..."
    s "Everyone, back away from Sid!"
    show sam angry:
        linear .2 xcenter .8
    s "I can't believe it..."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .7
        ycenter .25
        zoom .75
    s "You digusting little..."
    i "I swear, I didn't do anything!"
    hide sam with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "Excuse me."
    hide drac ind with dissolve
    blank "Dracula walked over and inspected Dan's body for a minute."
    show drac ind with dissolve:
        xcenter .75
    d "He is dead."
    d "Very, very dead."
    d "The metal rod is going all the way through his chest."
    i "Th-this is what I woke up to! Just a minute ago!"
    d "Hmph."
    hide drac ind with moveoutright
    bi "I don't know if I believe him, but..."
    $mood = "shock"
    b "We all have to calm down!"
    b "Yelling at each other won't solve anything."
    show frog ind with moveinbottom:
        xcenter .75
    f "What happened?"
    o "Okay hey woah!"
    show lauren ind with moveinright:
        xcenter .65
    show frog ind:
        linear .2 xcenter .8
    o "Hey let's not look over there!"
    $mood = "sad"
    o "Come on Freddy, come with me!"
    f "O-okay!"
    hide frog ind with moveoutright
    show lauren ind:
        linear .2 xcenter .75
    o "I don't know what to say."
    o "I can't believe it."
    i "Lauren, I swear, I..."
    hide lauren ind with moveoutright
    $ showchibint("catherine", "jenny", "kaiser", "sam", "shahar", "stella", "dracula", "sid")
    i "I-I swear..."
    stop music fadeout 0.5
    b "Hold on!"
    bi "I need to stop and think."
    play sfx "<from 0 to 3>audio/jaws.mp3" volume .2
    hide sid ind with dissolve
    show scary with dissolve:
        alpha .95
    show dan ind with dissolve
    bi "Dan is... dead."
    bi "We've only know him for a day and a half, but..."
    bi "I can't believe he's actually dead."
    bi "Someone killed Dan."
    show dan dead with dissolve
    bi "It makes sense. We're out of food, the murderer didn't have much time to act."
    bi "And we don't know what consequences there are for the murderer not doing anything."
    bi "It's all so logical, but still so shocking..."
    bi "But... I can figure out what to do next."
    bi "Dan deserves justice."
    show dan dead:
        linear .3 xcenter .75
    show sid dead with dissolve:
        xcenter .25
    bi "Sid being the one back here with him when he died is pretty damning evidence."
    bi "Everyone's being quick to point fingers at the kid."
    bi "And... I can't really blame them. It does look like he did it."
    bi "But we have to figure out exactly what happened here."
    bi "It's not like we can call the police in a situation like this, either."
    bi "So I'll do it myself."
    $mood = "ind"
    bi "Let's figure out exactly what happened."
    bi "Okay!"
    hide sid dead
    hide dan dead
    with dissolve
    hide scary with dissolve
    play music "audio/sadsong.mp3"
    b "Alright, everyone except for Sid and Jenny - go to the bar car."
    b "Jenny and I can talk to Sid about what happened and we'll go from there."
    bi "I probably shouldn't be alone with him."
    bi "And hopefully Jenny's presence will calm him down a bit."
    show sam angry with moveinleft
    s "So who made you the leader here?"
    show sam angry:
        linear .3 xcenter .75
    show kaiser ind with dissolve:
        xcenter .25
    k "Oh please. As if Sid would even speak to you after that outburst a second ago."
    s "..."
    k "It is fine. There will be more time to investigate and discuss."
    b "Yeah! We have to start somewhere."
    s "Fine."
    hide kaiser ind
    hide sam
    with dissolve
    $ showchibint("catherine", "jenny", "shahar", "stella", "dracula", "sid")
    show catherine ind with moveinleft
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .5
        ycenter .1
    c "I didn't exactly like Dan, but he didn't deserve this..."
    hide poprain with dissolve
    hide catherine ind
    show catherine happy
    c "Bert, thank you for taking charge."
    b "O-of course!"
    ses "Meoooo!"
    c "I'll corral everyone toward the bar car."
    hide catherine happy with dissolve
    $ showchibint("jenny", "sid")
    show sid ind with dissolve:
        xcenter .25
    show jenny ind with dissolve:
        xcenter .75
    $mood = "sad"
    j "Alright, everyone else is gone."
    j "Let's just... have a chat."
    i "We were getting so close, too..."
    i "He was like... my friend. I would never hurt Dan!"
    j "Sid... We just need you to explain everything that happened."
    b "What were you guys doing before you went to sleep?"
    i "We were talking about getting out of here."
    i "I told him I missed my family, and that I can't wait to see them again."
    i "He told me I could take the bed, since he did the night before..."
    i "So I laid down, and fell asleep."
    b "..."
    b "And then what?"
    i "Well, nothing."
    i "The next thing I knew, I... he..."
    i "....."
    j "It's okay Sid, take your time."
    i "I heard a really loud noise, but when I rolled over, I couldn't see anything."
    i "I panicked for a moment, and yelled out for Dan, and then..."
    i "The next thing I saw was this."
    j "Jeez..."
    b "Did he... yell? Or say anything?"
    b "Before he couldn't anymore."
    bi "This is incredibly uncomfortable..."
    i "Well... I thought I heard him say my name, with a faint breath."
    i "But it's hard to remember."
    j "I'm sure he did."
    j "You guys were friends, like you said."
    i "Y-yeah."
    i "Excuse me..."
    hide sid ind with moveoutleft
    blank "Sid walked to the corner and began sobbing loudly."
    show jenny ind:
        linear .3 xcenter .5
    b "Jenny, I think whether or not Sid did it, we should do our best job investigating."
    b "I'm sure there's a lot we could find if we look around a bit and talk to everyone else."
    j "Yeah. I mean, for starters, where did this metal bar come from?"
    j "We searched every inch of this train and definitely didn't come across that."
    b "You're right... There's a lot to figure out."
    b "Jenny - I need a favor."
    b "Can you get everyone in the bar car to go back to where they were when the lights went off?"
    b "I think they'll listen to you."
    j "Sure. Be careful back here with him."
    b "Thanks. I'll be there in a minute."
    hide jenny ind with moveoutleft
    $ showchibint("sid")
    bi "I was worried about being alone with him at first, but..."
    bi "He seems more devastated than anything."
    show sid ind with moveinleft
    i "Bert?"
    b "Yeah Sid?"
    i "I really s-swear I'm innocent."
    bi "..."
    b "I believe you."
    bi "I don't know if I believe him."
    b "We'll get to the bottom of it."

label preinvest:
    stop music fadeout 1.0
    scene black with fade
    blank "Bert made his way to the bar car."
    scene bg notrainmid at bg
    $ showchibint("catherine", "freddy", "jenny", "stella", "dracula")
    $ statusnt("Bar Car", "bert", ch = 1, sun = 4)
    with dissolve
    show jenny ind with dissolve
    j "Okay, everyone should be back in the car they were in when the lights went off."
    b "Perfect."
    b "And thank you for helping me calm down Sid."
    j "Now to calm down Freddy... Shahar told him that \"Dan be as good as shark bait\" now."
    b "Oh jeez..."
    hide jenny ind with dissolve
    bi "Jenny is a big help, but she's also a suspect."
    bi "I can't forget that."
    bi "For now though, it's time to gather evidence."
    $mood = "ind"
    pause 1
    play music "audio/inthefaceofdeath.mp3" fadein 1.0
    pause .5
    show investstart with dissolve
    pause 1
    hide investstart with dissolve
    tut "During investigations, you'll need to find pieces of evidence by clicking on important objects and by talking to people."
    tut "When you hover the cursor over an object for the first time, a \"!\" will appear next to the cursor to indicate you can click on it."
    tut "If you've already investigated an object, a \"check mark\" will instead appear when you hover over it."
    tut "People can be talked to by clicking on their icons, just like in free time."
    tut "You can use the Evidence Folder button in the top right to review evidence you've collected,"
    tut "and once you've collected all the evidence in a room, you'll be alerted."
    #tut "If you need to review this information, it is available via the menu."
    call screen midCarInv with dissolve

################################################################################
################################################################################      JULIAN TRIAL STARTING!!! WOOT WOOT LEGO
################################################################################

label trial1a:
    $dan = False
    $mood = "sad"
    play music "audio/coming_together.mp3"
    scene black with fade
    blank "Everyone was brought to the bar car."
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    show stella ind with dissolve
    t "So what's the plan?"
    t "I think I agree with the pirate at this point, let's all just jump out a window."
    show stella ind:
        linear .3 xcenter .75
    show lauren ind with dissolve:
        xcenter .25
    o "That's not funny... we need to figure this out."
    o "For Dan's sake, and for our own."
    o "One of us IS a murderer."
    t "Hm. You say that quite confidently, do you have something you'd like to share with the group?"
    hide stella ind with moveoutright
    show kaiser ind with moveinright:
        xcenter .75
    k "I've been ignoring her and I will continue to ignore her."
    k "Anyway, Bert. Where do you think we should start?"
    b "That's a good question..."
    b "I think the most logical thing to start with is... when it happened."
    hide lauren ind with moveoutleft
    show sam ind with moveinleft:
        xcenter .25
    s "Hmm, when the four of us went to the front car, Dan was still here in the bar car."
    k "Yes, it's true."
    hide kaiser ind with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "And then a few minutes later, Sid and Dan went to the back car together."
    c "A bunch of us watched the two of them go."
    s "So it had to have happened sometime between then and when we made our way to the back car to check on them."
    s "Which honestly wasn't a very long time... maybe 20 minutes."
    $mood = "sad"
    c "Putting a time to it somehow makes this even more disturbing."
    b "Also, we did all go check up in the front car first."
    c "Yeah, so for a few minutes, this car had to have been completely empty."
    $mood = "ind"
    b "Well, Sid could have come into this car while everyone was up front, and we would have no way of knowing."
    b "But aside from that, yes."
    s "I don't think there's any time trickery going on here, it seems pretty clear-cut."
    hide sam with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I think we should talk about alibis."
    j "That's what they do in all the crime shows, at least."
    show catherine happy
    c "Haha! I love those shows."
    show catherine ind
    c "Oops. Dammit Catherine, now's not the time to fangirl."
    j "Anyway... who here can vouch, with certainty, about where someone else was during the darkness?"
    j "It's important to figure out exactly where everyone was."
    j "Freddy and I, for example, were holding hands the whole time."
    j "In fact, I think Bert even saw us holding hands before it got dark."
    hide catherine with moveoutright
    show frog ind with moveinright:
        xcenter .75
    f "Yeah! We wanted Bert to play with us."
    f "We didn't g-get to play though..."
    b "Yeah, it is true. They definitely came up to me together before it all happened."
    b "I don't think they had even moved a foot once I could see them again."
    j "I'd like to say that we can vouch for where Bert was too, but..."
    b "No, you can't. For all you know I could have been anywhere, and just went back to the same spot."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .3
        ycenter .275
        zoom .75
    j "...Yeah."
    b "So Jenny and Freddy should be cleared with alibis."
    hide poptear
    b "As well as Lauren, Kaiser, Sam, and Shahar."
    hide frog ind
    hide jenny ind
    with dissolve
    show catherine happy with moveinleft:
        xcenter .25
    c "Sesame was my alibi!"
    ses "Mrewew!"
    show sid ind with moveinright:
        xcenter .75
    i "Does that count?"
    b "Not exactly... "
    show catherine ind
    i "So it could have been Catherine?"
    i "She could have snuck into the back car and done it!"
    i "I told you it wasn't me!"
    hide catherine ind with moveoutleft
    show stella ind with moveinleft:
        xcenter .25
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .325
        ycenter .25
        zoom .75
    t "You're not the fastest learner Sid."
    b "Hey wait, slow down!"
    t "I suppose you are just a child... Think more clearly."
    stop music fadeout 1.0
    tut "You're about to take part in your first debate."
    tut "Four statements will appear. Statements with blue text can be agreed with."
    tut "To agree with a statement, click on it then press \"Agree\"."
    tut "Statements with red text can be refuted using evidence."
    tut "To refute a statement, click on it, then press \"Refute\", then select evidence."
    tut "Find the correct or incorrect statement and its refutation to proceed."
    tut "There is no penalty for choosing the wrong statement or evidence, except shame upon your family."
    tut "Good luck!"
    camera at paralloff
    $showchibint()
    python:
        startTrainTrial("stella", "Stella: It could be true, we all saw her heading to the back car in the first place{color=#55f}{/color}.", 0,
    "stella", "Stella: We have {color=#f00}no way of knowing{/color} if she actually went to the back car or not.", -1,
    "sid", "Sid: I told you it {color=#55f}wasn't me{/color}!", 1,
    "stella",  "Stella: It would also explain that perky attitude of hers... it's just a diversion.", 0,
    1, 5, "trial1b")

label trial1b:
    play music "audio/coming_together.mp3"
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    camera at parallax
    show bert happy with moveinleft
    b "Yeah, that's it!"
    hide bert happy with moveoutright
    show stella ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    b "Hey! Catherine couldn't have left the bar car."
    b "She knew about the scream!"
    t "Hmmm... and neither Sid nor those in the front car heard the scream..."
    t "So if she left the bar car, how could she have known?"
    b "Exactly!"
    b "We can't prove exactly what she was doing, but it seems pretty clear she didn't leave this car."
    show scary with dissolve:
        alpha .5
    bi "Unless of course, she was the one that caused the scream..."
    bi "Then she would know about it even if she did leave this train car."
    bi "Best to keep that in mind."
    hide scary with dissolve
    i "I-I... agree. I guess."
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .75
        ycenter .1
    i "I just don't want to be the only suspect..."
    i "I r-really didn't do it."
    hide poprain with dissolve
    hide sid ind with moveoutright
    hide stella ind with moveoutleft
    with dissolve
    show lauren ind with dissolve
    o "Well... If anything, that just made it seem even more like Sid did it."
    o "It's hard to come to terms with that though, he is just a kid..."
    o "Maybe we should pivot toward a different topic."
    b "Yeah, there's a lot to talk about."
    show lauren ind:
        linear .3 xcenter .75
    show jenny ind with dissolve:
        xcenter .25
    j "Yeah. Let's talk about the uh, stabby stick."
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .75
        xcenter .625
        ycenter .25
    o "The stabby stick?"
    j "The murder pole! Whatever we're calling it."
    b "The murder weapon?"
    j "Yeah, what is that thing? And where did it come from?"
    b "It seems to be a pretty ordinary metal pole with a sharp end to it."
    b "I don't know what it's doing on the train though."
    o "And Jenny made a good point - where did it come from?"
    o "I thought we had all searched the train, at least a little bit."
    o "Does anybody remember seeing it?"
    hide lauren ind
    hide jenny ind
    with dissolve
    blank "Nobody spoke up."
    show scary with dissolve:
        alpha .5
    bi "Nobody saw it?"
    bi "Unfortunately, that can't be true."
    bi "Someone here used it to kill Dan. Where was it hiding?"
    bi "I thought I had checked everywhere... but maybe there is one place I hadn't looked."
    play music "audio/invest1.wav"
    call screen pickSpot1 with dissolve

label trial1c:
    play music "audio/coming_together.mp3" fadein 2.0
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    show lauren ind:
        xcenter .75
    show jenny ind:
        xcenter .25
    with dissolve
    b "That's it!"
    b "It had to have been in the caboose closet."
    hide lauren ind with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "Hm? That closet was locked."
    s "Dracula checked it when we first explored the back car."
    j "He mentioned that to me too."
    b "But did anyone other than Dracula actually check the closet?"
    j "Hmm, I didn't."
    j "The bed was pushed up against it anyway, it would be annoying move the bed and fully open the door."
    j "I took his word for it being locked."
    s "Hey, what the hell? Was Dracula lying about the closet being locked?"
    hide jenny ind with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "This is an unfortunate situation..."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .3
        ycenter .275
        zoom .75
    d "I was hoping this wouldn't wind up being relevant..."
    s "What are you talking about?"
    hide poptear
    $mood = "shock"
    d "Truth be told, I was the first one to wake up on the train."
    d "I noticed everyone else was still unconscious, so I did a little exploring."
    d "That's when I noticed the, as the girl says, 'stabby stick' in the closet."
    s "Are you kidding me?! So it was unlocked?"
    d "Yes, the closet was unlocked the whole time."
    d "When I saw the metal bar, I was worried about it becoming a weapon."
    d "However, I couldn't find anywhere better to hide it. So instead, I made sure to disuade people from opening the closet."
    hide sam with moveoutright
    show kaiser ind with moveinright:
        xcenter .75
    k "And we're to simply believe that?"
    d "Well, {i}did{/i} anybody else check the closet to see if it really was locked?"
    hide drac ind
    show drac happy:
        xcenter .25
    blank "Nobody spoke up."
    k "..."
    hide drac happy
    show drac ind:
        xcenter .25
    d "Hmph. As I thought."
    b "So unless Dan himself found the murder weapon, it seems like the murderer themself was the only one who could have."
    $mood = "ind"
    b "...This is progress...!"
    b "Now we just need to figure out who went into the closet!"
    b "..."
    bi "That might be easier said than done. It feels like it could have been anyone."
    k "Well, if we're accepting this reality... it once again seems Sid is the obvious answer."
    k "Sid and Dan were sleeping in the back car every night."
    k "Sid should have had access to the weapon quite easily."
    k "In fact, he could have just done it while Dan was sleeping, and staged the scene afterwards."
    d "Yes, I do agree."
    d "The evidence seems quite damning, once again."
    hide drac ind with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "Wait, no way!"
    i "Even i-if I wanted to, I couldn't have gotten into the closet!"
    k "Why's that?"
    i "Dan! Dan was sleeping in the cot last night, and the cot blocks the closet!"
    i "It won't even open if you don't move the cot a little!"
    show drac ind with moveinleft:
        rotate 45
        xcenter -.1
        ycenter .5
    d "This is true."
    hide drac ind with moveoutleft
    hide kaiser ind with moveoutright
    show stella happy with moveinright:
        xcenter .75
    t "Oh my, this is starting to get interesting!"
    t "So you two weren't sharing the cot?"
    i "I - what? No, of course not! I slept on the bench."
    b "Stella..."
    t "Hehe, I kid darling."
    t "Regardless..."
    hide stella happy
    show stella ind:
        xcenter .75
    t "I'm not entirely sure your defense would hold up in court."
    t "How do we know you slept on the bench and not the cot?"
    t "Then you'd be able to grab the weapon while Dan was sleeping, no problem."
    i "Well, "
    extend "I don't know, I guess..."
    i "I guess I can't prove it."
    show scary:
        alpha .5
    hide stella ind
    hide sid ind
    with dissolve
    bi "Hmmm... proof that Dan slept on the cot, and Sid slept on the bench."
    bi "Who might have that?"
    play music "audio/invest1.wav"
    call screen chooseChar("catherine", "trial1d", "Who might have proof that Dan slept on the cot, and Sid slept on the bench?") with dissolve
label trial1d:
    play music "audio/coming_together.mp3"
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    show catherine ind with dissolve
    c "Huh? Me?"
    c "What do you mean?"
    b "Remember back to your conversation with Dan and Sid this morning?"
    c "Hm?"
    c "Oh! You're right!"
    hide catherine ind
    show catherine happy
    c "I completely forgot about getting mad at Dan this morning."
    c "Sorry Dan!"
    bi "He's still dead."
    c "Anyway, you're totally right! Sid mentioned that his back hurt from sleeping on the bench."
    b "Yeah, that's it!"
    b "If Sid was planning on murdering Dan, it'd make sense for him to lie."
    b "But Dan agreed and said he slept on the cot, so it seems like we have proof."
    c "So it seems like it wasn't Sid... at least not while Dan was sleeping."
    show catherine ind:
        linear .3 xcenter .75
    show sid ind with dissolve:
        xcenter .25
    i "Yeah! And and and..."
    i "I spent almost all my free time up in the front car trying to get into the computer."
    i "I was never alone in the back car, I swear!"
    b "Can anyone prove otherwise?"
    blank "Nobody spoke up."
    i "Does... does that finally prove I'm innocent?"
    hide catherine ind with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "More than anything, it shows we're not getting anywhere."
    s "You were basically our only lead."
    s "I mean, you were literally right next to him when he died."
    s "If it wasn't you, who the hell was it?"
    b "Hey! We're getting somewhere. We've learned about a lot of our alibis, and about the murder weapon."
    s "Where do we even go from here?"
    s "What are we supposed to do?"
    hide sid ind with moveoutleft
    show stella ind with moveinleft:
        xcenter .25
    t "Weren't you paying attention Sam? No?"
    t "There are a few more things to figure out."
    t "For example - those of us who were in this car - Catherine, Bert, Jenny, Freddy, and myself." #Arun Stella and myself?
    t "Recall the loud scream we heard."
    bi "...!"
    t "Who was that? There's no mistaking that it happened."
    b "You're right - I heard it too."
    s "What are you on about? Who cares if someone screamed?"
    s "Dan got stabbed through the chest, of course people are going to be screaming."
    t "Hmmm, with all due respect - which isn't much - you don't know what you're talking about."
    show sam angry:
        xcenter .75
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .75
        ycenter .25
    s "What did you just say to me?"
    hide stella ind
    show stella happy:
        xcenter .25
    t "Oh? Did that get you all riled up? Haha!"
    hide popmad
    show scary with dissolve:
        alpha .5
    bi "I need to step in... I know the answer!"
    camera at paralloff
    $showchibint()
    python:
        startTrainTrial("stella", "Isn't it obvious? Think about that scream in particular.", 0,
        "sam", "What are you even talking about? There shouldn't be {color=#f00}anything notable{/color} about someone screaming.", -1,
        "stella", "Do you think I'm {color=#55F}making up{/color} the scream? Why would I do that?", 1,
        "sam", "Maybe to cover up the murder! I don't trust you for a second.", 0,
        1, 4, "trial1e")

label trial1e:
    play music "audio/coming_together.mp3"
    camera at parallax
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    show stella ind:
        xcenter .25
    show sam ind:
        xcenter .75
    with dissolve
    b "Hey, look!"
    b "Believe it or not, Stella has a point. That scream was different."
    b "And we have a testimonial to back it up."
    hide sam with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "I'd hardly call it a testimonial, but yes, I do agree with Stella."
    d "I find it quite easy to focus in the dark, and to me, that scream felt very particular."
    b "And what do you mean by that?"
    show stella happy:
        xcenter .25
    t "Ooooooo, can I be the one to explain it? I think I figured it out."
    d "If you insist."
    $mood = "shock"
    t "It wasn't really someone screaming, it was a recording."
    b "What? What do you mean?"
    d "Yes, this is the same conclusion I reached."
    b "How do you know?"
    d "Well... it sounded strange. I immediately recognized that something was odd."
    hide stella happy with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    o "No offense, but saying it 'sounded strange' isn't enough to convince me."
    d "I agree, which is why I did not speak up sooner."
    d "Truth be told, it took me a while to piece it together."
    d "The nail in the coffin, though, was that it wasn't just a random recording."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .7
        ycenter .25
        zoom .75
    d "The scream was Jenny's."
    o "Huh?"
    hide popwow
    hide lauren ind with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "Yeah, huh? What do you mean?"
    d "Think back to yesterday, do you remember... yelling?"
    j "Ummm... I don't think so? Are you sure I did?"
    $mood = "ind"
    d "I suppose it'll be hard to convince you of something like that."
    show scary with dissolve:
        alpha .75
    bi "I will."
label trial1f:
    show bg notrainmid at bg
    show jenny ind:
        xcenter .25
    show drac ind:
        xcenter .75
    show scary:
        alpha .75
    menu:
        bi "When was it that Jenny screamed?"

        "When she saw the body.":
            bi "Actually... I don't think that's it."
            jump trial1f

        "When she first got on the train.":
            bi "No, that can't be it. "
            jump trial1f

        "When she got mad at Dan.":
            bi "Hmm, I don't think she yelled."
            jump trial1f

        "When Sesame bit her.":
            bi "That's it!"

    hide scary with dissolve
    b "Yeah, that's it! I remember Sesame biting Jenny, and she screamed."
    d "Yes, she screamed bloody murder. And the scream we heard tonight? It was the same one."
    bi "I think he's right!"
    hide drac ind with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "Now that you mention it, both did sound like they came from a little girl."
    j "Hey! I'm basically the same age as you!"
    c "Anyway, I think Dracula's right."
    b "I agree."
    c "But we do we do about it?"
    c "What does that even mean for the case?"
    j "This is getting really confusing..."
    c "Yeah, I need to collect my thoughts for a minute."
    hide jenny ind with moveoutleft
    show shahar ind with moveinleft:
        xcenter .25
    h "No time to be lollygagging."
    h "We shant let our guard down, mateys."
    hide catherine ind with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Ye-yeah. There's a dead body in the back car, no time to be messing around."
    i "I mean, damn, how am I supposed to be calm? Or even try to think at a time like this?"
    i "Half of you just accused me of murder and I just met you."
    i "Plus, I can barely even see, it's so dark in here."
    bi "!"
    hide shahar ind with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "Bert, I saw something click in your brain just now."
    d "Did you make the same realization as myself?"
    b "I think so..."
    show scary with dissolve:
        alpha .5
    bi "How foolish of us!"
    bi "It seems obvious in hindsight... something's very different about now and the time of the murder."
    bi "And that is..."
    #hide scary with dissolve
    call screen trainEvidenceTrial(-1, 3, "trial1g") with dissolve
label trial1g:
    scene bg notrainmid at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Bar Car", "bert", ch=1, sun=4)
    with dissolve
    show drac ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    b "That's it."
    b "It's the middle of the night now, and all the lights in the car are off."
    b "The only thing letting us see is the residual moonlight coming through the windows."
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .7
        xcenter .85
        ycenter .25
    i "I... I don't get it."
    i "Why does that matter?"
    d "Think back."
    d "Why was it even darker than this for a moment?"
    d "Why couldn't we see at all during the murder?"
    b "Exactly."
    hide sid ind with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    o "We were in the front car, which was pretty well lit by the computers."
    o "But this car was pitch black?"
    b "Yeah - I couldn't see an inch in front of my face, for about 30 seconds."
    b "Thinking about it more... I can only come to one conclusion."
label trial1h:
    show bg notrainmid at bg
    show drac ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    show scary:
        alpha .75
    menu:
        bi "The reason we couldn't see was because..."

        "Someone quickly hung sheets in front of all the car's windows!":
            bi "Well, technically they could have, but I don't think so..."
            jump trial1h

        "Someone threw a smoke bomb!":
            bi "Hmm, that's probably not it. It got dark, not smokey."
            jump trial1h

        "Something blocked the moonlight coming through the windows!":
            bi "That's it!"

        "We were temporarily blinded by the Game Master's brain chips!":
            bi "Hmm... It could be that, but I don't think it's right."
            bi "I feel like that would hurt a lot more..."
            jump trial1h

    hide scary with dissolve
    b "That must be it! Something blocked all the moonlight coming through the windows."
    o "Oh, maybe you're right."
    d "He's definitely right."
    d "I have no proof, but I certainly cannot think of any other alternatives."
    o "Well if that's the case, how did it happen?"
    b "How did it happen? Hmmm..."
    b "!"
    b "We must have gone through a tunnel!"
    b "We went through a tunnel, and for the minute or so we were in it, we couldn't see anything!"
    o "That makes a lot of sense... I don't think anyone who was in the front car would have noticed."
    blank "They looked around, but nobody else spoke up."
    o "Plus, this train is really quiet and smooth."
    o "It's hard to even remember we're on a train sometimes, let alone notice things like that."
    b "Exactly!"
    b "The most obvious aspect of going through a tunnel would have to be -"
    o "- the darkness."
    d "If I may interject: what is a tunnel?"
    bi "..."
    o "Freddy, I have a job for you."
    show frog ind with moveinbottom:
        xcenter .875
    f "Job for me?"
    o "Explain what a tunnel is to Mr. Dracula please. I don't have time for this."
    show shahar ind with moveinleft:
        xcenter .1
    h "Aye, me as well please."
    h "Never 'eard of such a thing."
    bi "This ten year old boy is about to explain tunnels to two grown men."
    f "O-okay!"
    hide drac ind
    hide frog ind
    hide shahar ind
    with moveoutleft
    show kaiser ind with moveinleft:
        xcenter .25
    k "So we went through a tunnel right when the murderer was going to strike?"
    k "Or did the murderer simply capitalize off of the darkness and decide to kill?"
    b "...I don't know."
    o "This also doesn't change the fact that Catherine was basically guarding the door to the back car."
    b "...That is true..."
    k "It feels like we're uncovering some things, but no closer to a real answer."
    hide lauren ind with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "I agree with Kaiser and Lauren."
    s "I don't think we're getting anywhere."
    s "Plus, it still seems pretty obvious to me that it had to have been Sid."
    hide kaiser ind with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "Hey! We already moved past that, it couldn't have been me."
    s "This is such a circular argument..."
    show scary with dissolve:
        alpha .7
    bi "Damn, are they right?"
    bi "Are we really not getting anywhere?"
    bi "So far we've learned what everyone was doing, where the weapon came from, and why it got dark."
    bi "It feels close."
    bi "It feels like if we just figure out a few more things..."
    hide scary
    f "Hey, wait a minute!"
    show sid ind:
        xcenter .25
        linear 0.15 xcenter .15
    show sam ind:
        xcenter .75
        linear 0.15 xcenter .85
    show frog ind with dissolve
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        #zoom .75
        xcenter .4
        ycenter .45
    f "This doesn't make any sense!"
    b "What's wrong Freddy?"
    hide popwow
    f "Well..."
    f "I was telling the scary men about tunnels, right."
    f "But then I realized!"
    f "If we went through a tunnel, it would probably break the flag."
    s "The flag? What do you mean?"
    f "You know, the one on the back of the train!"
    b "Freddy, what are you talking about?"
    f "Lauren knows! When I looked out the window earlier, I saw a flag on the back of the train."
    hide sid ind with moveoutleft
    show lauren ind with moveinleft:
        xcenter .18
    o "He did mention something like that this morning."
    o "We were up in the front car, and I was half paying attention, but I do remember something about a flag."
    f "Come on, I can show you guys!"
    hide frog ind with moveoutleft
    s "I'm so lost..."
    b "Me too, but it can't hurt to hear him out."

label trial1i:
    scene black with fade
    blank "The ten of them followed Freddy to the front car."
    scene bg notrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    with dissolve
    show jenny ind with dissolve:
        xcenter .5
        linear 0.3 xcenter .75
    j "I'm skeptical that this'll lead to anything..."
    j "But it's not like we were getting that much done anyway!"
    show frog ind with moveinbottom:
        xcenter .25
    f "Look!"
    hide frog ind with moveoutleft
    blank "Freddy ran over to the window."
    blank "A few others followed."
    scene black with dissolve
    image forest run2:
        contains:
            "windowviewout.png"
            xpos -9.0
            linear 555.0 xpos 0.0
        contains:
                "scary.png"
                alpha .8
    show forest run2
    show windowview2
    with fade
    b "Hmmm... looks about the same as the last time we checked."
    b "What did you say we're looking for again, Freddy?"
    f "The flag!"
    f "It's all the way on the back of the train."
    b "I'm pushing my head all the way up against the glass and I can't see that far back."
    k "Me as well..."
    hide forest run
    hide windowview2
    with fade
    show bg notrainfront at bg
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    $ showchibint("catherine", "lauren", "freddy", "jenny", "kaiser", "sam", "shahar", "sid", "stella", "dracula")
    with dissolve
    show frog ind with moveinbottom
    f "Hmm... well, nevermind I guess."
    show frog ind:
        linear .3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "Well..."
    d "There is no need to rush."
    b "Huh? Of course there is!"
    b "Dan is dead! We have to figure out what happened!"
    hide frog ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "What are you talking about, Dracula?"
    j "Freddy is just making things up now and we're not getting anywhere."
    d "I don't think he made anything up."
    d "Just because we're not able to see the flag right now, doesn't mean that he didn't before."
    j "Yeah, but we can't even see the back train car from this angle out the window."
    d "Surely, Bert, you must understand the situation now."
    bi "!"
    show scary with dissolve:
        alpha .5
    bi "A reason why he was able to see it earlier, but we can't right now..."
    bi "Something about being in the front train car..."
    bi "I... have a guess. I might get it."
label trial1ia:
    menu:
        bi "The truth is..."

        "Freddy really is lying.":
            bi "No, this can all make sense."
            jump trial1ia

        "Only Freddy is able to see the flag, because of his onesie.":
            bi "Ahh, no. That doesn't make any sense."
            jump trial1ia

        "We need to be going around a turn to see it.":
            bi "Yes, that's it!"
            jump trial1ib

        "Freddy has better vision than the rest of us.":
            bi "Hmm, on second thought, probably not..."
            jump trial1ia

label trial1ib:
    hide scary with dissolve
    $mood = "ind"
    b "That's it!"
    b "We have to wait until we're going around a turn."
    b "Then we'll be able to see the back car from the window."
    d "Yes, precisely."
    j "Hmmm."
    j "How long will we have to wait?"
    d "We don't know."
    hide jenny ind with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "Aye."
    h "I don't get it."
    h "Are ye sayin' the flag is invisible?"
    bi "..."
    hide drac ind with moveoutleft
    show catherine happy with moveinleft:
        xcenter .25
    c "I can explain!"
    c "It's pretty simple."
    hide catherine happy with moveoutleft
    blank "Catherine grabbed a piece of paper and started drawing on it."
    show catherine happy with moveinleft:
        xcenter .25
    hide shahar ind with dissolve
    show traindoodle1 with dissolve
    c "So, this is us right now."
    c "We're in the first of the 3 train cars."
    c "Since we're going straight, we can't see the back of the train out the window."
    c "Buuuut..."
    blank "Catherine flipped the paper over and drew on the back."
    c "If we're going around a turn, "
    hide traindoodle1 with dissolve
    show traindoodle2 with dissolve
    extend "we have a better field of view!"
    c "Does that make sense?"
    i "Why is he smiling now..."
    o "And you even signed it, with a heart."
    c "I think I did a pretty good job drawing it!"
    hide traindoodle2 with dissolve
    show shahar ind with dissolve:
        xcenter .75
    h "Aye! That does make sense."
    hide shahar ind with moveoutright
    hide catherine ind with moveoutleft
    show kaiser ind with moveinleft
    k "I suppose we're just waiting then."
    b "Yeah, we should just hang tight until we start going around a turn."
    k "I feel we're investing quite a bit of time into the child's theory."
    bi "He is right..."
    bi "But it's all we've really got right now."
    show kaiser ind:
        linear .3 xcenter .75
    show stella ind with dissolve:
        xcenter .25
    t "I have been meaning to ask."
    $mood = "shock"
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .75
        xcenter .35
        ycenter .25
    t "What do you plan to do if we figure out who killed Dan?"
    k "She makes a good point, for once."
    hide pophuh
    k "There {i}is{/i} a killer amongst us."
    t "Seems easy enough, no? We can just kill them."
    k "Agreed."
    b "What!? We don't need another dead body on this train."
    k "What do you suggest then?"
    b "..."
    bi "I hadn't exactly thought that far ahead."
    b "We can just... lock them in one of the cars alone or something."
    $mood = "ind"
    b "But now's not the time to worry about that, we don't know who did it yet."
    hide kaiser ind with moveoutright
    show sam ind with moveinright:
        xcenter .75
    s "Hey - we're turning."
    bi "I can barely feel it, but with a look out the window, it seems like Sam's right."
    hide sam
    hide stella ind
    with dissolve
    blank "Bert and Freddy made their way over to the window again."
    show turning at bg
    show trainturnoverlay
    with fade
    b "Dracula was right, we can see the back of the train pretty easily now."
    f "Oh! See!"
    b "..."
    b "No, I don't really see anything."
    f "Well, yeah! The flag is GONE!"
    b "It's hard when I don't know what I'm looking for."
    b "Did it really look like a flag? What was on it?"
    f "Well... I don't know! It was a long, pointy flag!"
    hide turning
    hide trainturnoverlay
    with fade
    show frog ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    i "This kid's starting to bother me..."
    b "Wait, let him keep talking."
    b "Freddy, what do you mean it was a long, pointy flag?"
    b "That doesn't sound like any flag I've seen before."
    f "Umm... can I draw it?"
    show catherine happy with moveinleft:
        rotate 45
        xcenter 0
        ycenter .5
    c "Seems like I started a trend!"
    hide catherine happy with moveoutleft
    hide frog ind with moveoutleft
    blank "Freddy grabbed another piece of paper."
    show frog ind with moveinleft:
        xcenter .25
    hide sid ind with dissolve
    show traindoodle3 with dissolve
    f "If this is the train going left, it looked kinda like this."
    c "That's a pretty good drawing..."
    bi "Why does she sound jealous..."
    b "Anyway, so Freddy. It doesn't seem very much like a flag then?"
    f "W-well that's what it looked like..."
    f "It was really thin, and mounted on a stick."
    bi "!"
    hide frog ind
    hide traindoodle3
    with dissolve
    show catherine ind with moveinleft:
        xcenter .75
    c "Hmmm... "
    c "I don't think we're going down the right path."
    show sid ind with moveinleft:
        xcenter .25
    i "Wait, no! I think we were just starting to get somewhere!"
    c "I think I'm going to go inspect the body again."
    i "Catherine, you can't! Hear me out!"
    c "Hmm... I'll give you one minute!"
    camera at paralloff
    $showchibint()
    python:
        startTrainTrial("sid", "Sid: I know it seems like a waste, but think about what Freddy just said.{color=#55f}{/color}", 0,
        "catherine", "Catherine: Look! I'll admit it, {color=#f00}his drawing was better than mine...{/color}", -1,
        "catherine", "Catherine: But this is a waste of time. There's {color=#55f}nothing useful in his picture{/color} anyway.", 1,
        "sid",  "Sid: Don't you think his flag looked... {color=#55f}awfully similar to a scythe{/color}?", 1,
        3, -1, "trial1j")

label trial1j:
    scene black with fade
    camera at parallax
    play music "audio/coming_together.mp3"
    $mood = "shock"
    bi "!"
    bi "That's it!"
    scene bg notrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    with dissolve
    show jenny ind with dissolve:
        xcenter .5
    j "What do you mean a scythe?"
    show jenny ind:
        linear .3 xcenter .75
    show sid ind with dissolve:
        xcenter .25
    i "W-well not exactly a scythe, but..."
    i "Look at his drawing!"
    i "I think I'm starting to piece it together!"
    show scary with dissolve:
        alpha .5
    bi "It does look like a scythe, but... what does that mean?"

label trial1k:
    menu:
        bi "Is it..."

        "The flag was actually the murder weapon.":
            bi "That must be it!"
            jump trial1l

        "Someone switched the flag and the scythe.":
            bi "There's an even simpler answer."
            jump trial1k

        "Freddy was probably imagining it...":
            bi "No, there's a connection here!"
            jump trial1k

        "Maybe there was a farmer on the train's roof!":
            bi "Hmm, on second thought, probably not..."
            jump trial1k

label trial1l:
    hide scary with dissolve
    j "What! How? Who? Huh?"
    i "..."
    i "It does make sense though, right?"
    hide jenny ind with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    o "What you're suggesting is pretty crazy..."
    i "But? Maybe?"
    show shahar ind with moveinleft:
        rotate 45
        xcenter -.1
        ycenter .5
    h "Ye lost me again, lads."
    hide shahar ind with moveoutleft
    i "Ugh... Gimme that piece of paper."
    hide sid ind
    hide lauren ind
    with dissolve
    blank "Sid grabbed the piece of paper that Freddy was holding."
    show sid ind with dissolve:
        xcenter .25
    show traindoodle4 with dissolve
    i "Someone could have set up a mechanism to BONK the scythe off the tunnel entrance,"
    i "and swing down to stab through the back car window!"
    hide traindoodle4 with dissolve
    show sam ind with moveinright:
        xcenter .75
    s "That is a batshit insane theory."
    i "Wait, bu-"
    s "But! If it's right, we should be able to check."
    s "The murderer would have had to set up a hinge or something to make sure it swung down correctly."
    b "You're right!"
    $mood = "ind"
    b "We should go check."
    hide sid ind with moveoutleft
    show kaiser ind with moveinleft:
        xcenter .25
    k "I agree that it seems absurd. However I also agree there is no harm in checking."
    k "We should all move to the back car, together."
    b "Maybe someone can stay up here with Freddy? So he doesn't have to see the body again..."
    s "No, I don't trust any of you at this point. Bring the kid."
    bi "..."
    b "Alright."

label trial1m:
    scene black with fade
    blank "All of them made their way to the back car, together."
    scene bg bodytrainback at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Caboose", "bert", ch=1, sun=4)
    with dissolve
    show sid ind with dissolve
    i "Damn..."
    i "I don't really want to, uh, climb over his body to check the window..."
    b "I can do it."
    bi "I don't want to, but I can."
    show btracks with fade
    hide sid ind
    bi "Stepping over a dead body like this is unnerving..."
    bi "But I have to."
    bi "Hmmm... It's hard to get a good view of the overhang outside the train..."
    bi "But if I lean up against the broken glass of the window just right..."
    show trainhinge with dissolve
    bi "!"
    bi "On second thought... This must have been where that object was hanging from..."
    bi "There really is a big hinge, right outside the back door."
    bi "Sid was right..."
    hide trainhinge
    hide btracks
    show scary:
        alpha .5
    with dissolve
    blank "Bert stepped back over the body, and explained what he saw to everyone else."
    hide scary with dissolve
    show stella ind with moveinleft
    t "Well well well... that certainly changes things."
    show stella ind:
        linear .3 xcenter .75
    show kaiser ind with dissolve:
        xcenter .25
    k "Yes, it seems we have quite the mechanic on our hands."
    t "Mechanic?"
    k "Well, to construct a mechanism that releases a scythe specifically upon hitting the tunnel..."
    k "Especially in secret, with such little time..."
    k "It's nearly impossible."
    hide stella ind
    show stella happy:
        xcenter .75
    t "In any case, it's a fun lead!"
    b "Fun?"
    t "Think about it! The whole case is changed now."
    show scary with dissolve:
        alpha .5
    bi "She has a point."
    bi "If we assume this scythe contraption was actually used, everything is different."
    hide scary with dissolve
    hide stella happy
    show stella ind:
        xcenter .75
    t "Though, our alibis may be inaccurate now..."
    t "We might not be looking for someone who was in the back car at the time of death."
    hide kaiser ind with moveoutleft
    show frog ind with moveinleft:
        xcenter .25
    f "W-what? I don't get it."
    f "Someone killed Dan even though they weren't there with him?"
    t "Well buddy, once they put the flag up there, all they had to do was wait for the tunnel."
    t "It's sort of like a cuckoo clock. Once it's installed, you don't have to do anything."
    f "B-but... no! You're missing the point!"
    t "Au contraire."
    camera at paralloff
    $showchibint()
    python:
        startTrainTrial("freddy", "Freddy: Y-you're so mean to me! You're not my mom...", 0,
        "stella", "Stella: Dear, you're too young and stupid to understand. Leave this to us for now.", 0,
        "stella", "Stella: We can explain after - {color=#f00}they didn't need to be in the car{/color}!", -1,
        "freddy",  "Freddy: B-but... Why did Dan stand at the window? {color=#f00}Didn't somebody have to hold him there{/color}?", -1,
        3, 6, "trial1n")

label trial1n:
    play music "audio/coming_together.mp3"
    scene black with fade
    camera at parallax
    scene bg bodytrainback at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Caboose", "bert", ch=1, sun=4)
    with dissolve
    show frog ind with moveinbottom
    f "W-what do you mean? What object?"
    b "When I came back here to investigate more, I noticed this hanging right outside the back window."
    show frog ind:
        linear .3 xcenter .25
    show thering with dissolve:
        xcenter .75
    b "In fact, it was hanging from that same hinge."
    b "My guess is that Dan noticed the same thing and walked over to the back window."
    f "Sh-shiny..."
    show stella ind with moveinleft:
        xcenter .35
    show frog ind:
        linear .3 xcenter .15
    t "Hey, give me that!"
    t "That is my ring!"
    show stella ind:
        linear .3 xcenter .5
    hide frog ind with moveoutleft
    hide thering with dissolve
    b "Huh? This is yours?"
    t "Why yes of course it is, now hand it over."
    t "Hmm... I don't remember losing this, or giving it to anyone."
    b "Are you... admitting to hanging it outside the back car window?"
    t "Of course not, raclure de bidet."
    t "Why would I, Stella Cantoire, do such a thing?"
    bi "More importantly, if she did do it, she probably wouldn't own up to the ring being hers..."
    t "Someone must have stolen it from me."
    show stella ind:
        linear .3 xcenter .75
    show sam ind with moveinleft:
        xcenter .25
    s "Or they just asked for it while you were blackout drunk."
    s "If you don't remember who you gave it to -"
    t "Or who took it-"
    s "Then it doesn't really matter that it's yours."
    show scary with dissolve:
        alpha .5
    $mood = "sad"
    bi "This also means..."
    bi "Based on the positioning of the body and the window, Dan must have been stabbed through his front."
    bi "Which makes me think..."
    bi "That rod went all the way through his body when he fell onto his stomach..."
    bi "Sid did say that Dan called out to him before dying,"
    bi "so it would make sense that he turned around, then fell over onto his stomach, pushing the rod through his body..."
    bi "It's... horrible, and disgusting, but... at least it all tracks."
    bi "We're making progress."
    hide scary with dissolve
    $mood = "ind"
    s "More importantly, I have a question."
    s "We're assuming the murderer used the ring as bait for someone to stand at the window."
    s "I can get on board with that, sure. But."
    s "Dan probably only stood there for a minute or two, max."
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .75
        xcenter .35
        ycenter .25
    s "How did the murderer know exactly when we'd get to the tunnel?"
    t "Oh yes... a few moments ago we didn't even know when we'd be taking a turn."
    t "How was the murderer able to so perfectly time the tunnel entrance?"
    b "That's true. We don't have access to the train route, or even a map of the area."
    hide stella ind with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    o "Yeah, we were trying to find a map on the computers in the front car, but no luck."
    s "Someone must have gotten into the computers and kept it a secret from the rest of us."
    s "Damnit, right under our noses..."
    o "Wait, hold on. I don't think anyone managed to get into the computers."
    s "Don't be so foolish."
    camera at paralloff
    $showchibint()
    python:
        startTrainTrial("lauren", "Lauren: Why are you {color=#55f}so sure about yourself{/color}?", 1,
        "sam", "Sam: Look, we don't have time to focus on the means, just focus on the fact that it resulted in a murder.", 0,
        "lauren", "Lauren: There's just {color=#f00}no way for us to know if someone got into the computers {/color}anyway, so this is a dangerous rabbit hole.", -1,
        "sam",  "Sam: You're right, but I just know someone figured out the password. It's the only solution.", 0,
        2, 0, "trial1o")

label trial1o:
    play music "audio/coming_together.mp3"
    scene black with fade
    camera at parallax
    scene bg bodytrainback at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Caboose", "bert", ch=1, sun=4)
    with dissolve
    show lauren ind with dissolve
    b "Believe it or not, Sam might be on to something."
    b "The user counter on the monitors have a different value now."
    o "Wait, really?"
    b "Yes, it went up from 1 to 3 at some point."
    o "That would mean whoever used the computer used it {i}twice,{/i} as well."
    b "Yeah... maybe once to see what they can access, and again to set up the murder."
    show lauren ind:
        linear .3 xcenter .75
    show kaiser ind with dissolve:
        xcenter .25
    k "I have an inquiry - why was the user counter at 1 in the first place?"
    k "Is this value really something we should trust?"
    hide lauren ind with moveoutright
    show sid happy with moveinright:
        xcenter .75
    i "I know this!"
    i "When we first got on the train, the value was 0."
    i "After tinkering with the inputs for a bit, I found the directory."
    hide sid happy
    show sid ind:
        xcenter .75
    i "Unfortunately, there wasn't really anything useful there..."
    i "But! Afterwards, the user counter went up to 1 and stayed there."
    k "I see..."
    k "Can anyone else back up this claim?"
    i "Yes! I talked to Dan about this!"
    i "But... Dan's dead now..."
    $mood = "sad"
    i "I-I guess not then..."
    $mood = "ind"
    b "Wait, shouldn't it be as easy as reaccessing the directory?"
    b "If we go back to the front car and put in the same input, the counter should go up again."
    k "Hmm, perhaps. And if not, it would look fairly incriminating for the boy here."
    bi "He's right - if the counter doesn't go up again, something would be fishy."
    bi "It would probably mean that Sid somehow has the password..."
    i "I-It should! Let's go check!"
    b "Only one way to find out."
    hide sid ind with moveoutleft
    scene black with fade
    blank "All 11 made their way back up to the front car."
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    with dissolve
    show jenny ind with dissolve
    j "I'll try it."
    j "Sid, what do I type again?"
    show jenny ind:
        linear .3 xcenter .75
    show sid ind with dissolve:
        xcenter .25
    i "Just type in \"DIR\", in all caps, and hit enter."
    hide jenny ind with dissolve
    blank "Jenny walked over to the keyboard and started typing."
    blank "A few others watched."
    i "It sh-should work... why am I so nervous though..."
    b "..."
    show jenny ind with dissolve:
        xcenter .75
    j "Yep, I accessed the directory, and the counter went up to 4!"
    i "Phew!"
    j "Sid, why didn't you tell anyone else about this?"
    j "It could have been useful to see the directory, even if we can't open anything."
    i "W-well, I talked to Dan about it, and he said we shouldn't..."
    i "It's kinda hard to trust anyone, ya know..."
    b "Hmmm, either way, we know now."
    j "So it seems like someone did access the computer, either using the same input, or..."
    j "with the password."
    i "It couldn't have been me - I was never in the front car alone after the first time."
    j "Hmmm... idea!"
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    j "QUICK! IF YOURE THE ONE WHO USED THE PASSWORD, SPEAK UP NOW!!!"
    hide popwow
    blank "....................................................................................................................."
    show scary with dissolve:
        alpha .5
    bi "I was not prepared for Jenny to scream like that."
    bi "Anyway, nobody's speaking up..."
    bi "It seems like this is silently someone's admission of guilt."
    bi "If the murderer said they used the \"DIR\" input, they could absolve themselves of some blame."
    bi "But they didn't - we're close to figuring this out."
    hide scary with dissolve
    b "Let's... take a step back. Retrace our steps."
    hide sid ind with moveoutleft
    show catherine ind with moveinleft:
        xcenter .25
    c "Yes please... I'm starting to get a bit confused."
    c "So is Sesame I think."
    ses "Rmrowwwwwww."
    j "Agreed."
    c "With Sesame, or with me?"
    j "Uhh, both, I suppose."
    hide jenny ind with moveoutright
    hide catherine ind with moveoutleft
    show kaiser ind with moveinleft
    k "It seems the first half of our investigation was in vain."
    k "We spent quite some time considering ways someone could have stabbed Dan."
    show kaiser ind:
        linear .3 xcenter .75
    show stella ind with dissolve:
        xcenter .25
    t "Not wasted, per se, simply not the correct solution."
    t "Now we know that nobody snuck into the back car."
    k "That is true."
    k "As well, some information about the tunnel."
    b "And the computer log in!"
    b "We don't know {i}who{/i} figured out the password, {i}what{/i} it is, or {i}how{/i}..."
    b "But, we know someone did."
    hide kaiser ind with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    o "So, the person who accessed the computer is the murderer?"
    t "It seems quite that simple."
    t "Otherwise, they wouldn't be able to time the on hitting the tunnel so accurately."
    o "I see..."
    hide stella ind with moveoutleft
    show lauren ind:
        linear .3 xcenter .5
    o "Then I can't think of any other solution:"
    o "It must have been one of the four in the front car at the time of the murder."
    o "Shahar, Sam, Kaiser, or myself."
    b "What? You can't just narrow it down so quickly!"
    o "Think about it - it's the perfect excuse."
    o "Being able to claim, \"I couldn't have done it, I was nowhere near the crime.\""
    o "Plus, if they accessed the computer twice, it's likely one of the times was during the murder."
    show lauren ind:
        linear .3 xcenter .75
    show drac ind with dissolve:
        xcenter .25
    d "Yes - I concur."
    d "If this theory is correct, it must have been one of the four in this car."
    $mood = "shock"
    b "But why?"
    d "Think back to something we concluded earlier."
    d "Something essential to the setup that could only be accomplished in this car."
    b "Hmm..."
label trial1p:
    show scary:
        alpha .75
    menu:
        bi "Something that could only be accomplished in the front car, at the time of the murder?"

        "Activating the PA system.":
            bi "Yeah, that must be the answer!"

        "Checking the maps.":
            bi "They could check the maps, but that's probably not what they were doing at the time of the murder."
            jump trial1p

        "Changing the train's route.":
            bi "We still don't know if that's even possible..."
            jump trial1p

        "Securing the murder weapon to the back of the train.":
            bi "No, that would have had to be done earlier, and from the back car."
            jump trial1p

    hide scary with dissolve
    b "They must have been... activating the PA system with the button!"
    d "Precisely."
    b "I nearly forgot about the scream."
    b "It was just to distract us during the commotion, but their plan backfired."
    o "Hmmm..."
    o "You act like you have it all figured out, Mr. Dracula."
    hide drac ind
    show drac happy:
        xcenter .25
    d "Oh, surely no faster than you do."
    d "Besides, I wasn't the one in this traincar during the murder, so this does not incriminate me."
    hide drac happy with moveoutleft
    o "..."
    show sid ind with moveinleft:
        xcenter .25
    i "Stay on task! We're so close to the answer."
    i "We know that you can't hear the PA system from the front car, Jenny already proved that."
    i "But... there's a way we can check."
    hide sid with moveoutleft
    b "Wait, Sid!"
    blank "Sid ran over to the train car door."
    blank "He opened both the front car door and the bar car door,"
    blank "so everyone could see directly into the bar car."
    i "Hit the button!!!"
    show lauren ind:
        linear .2 xcenter .8
    blank "Lauren pressed the button."
    z "AHHHHHH!!!"
    b "!"
    show catherine ind with moveinleft:
        xcenter .25
    c "Wow! Jenny's scream really is programmed onto that button!"
    c "Press it again!"
    z "AHHHHHH!!!"
    z "AHHHHHH!!!"
    z "AHHHHHH!!!"
    o "Wow..."
    hide lauren ind with moveoutright
    show sid ind with moveinright:
        xcenter .75
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .65
        ycenter .25
        zoom .75
    i "That settles it then, it really was one of the four from up here."
    i "They pressed the button when we went into the tunnel, to cause a diversion."
    hide popwow
    i "Despicable..."
    show sid mad
    i "WELL, OUT WITH IT! WHO KILLED DAN?!"
    b "Woah woah, take a step back..."
    hide sid mad
    hide catherine ind
    with dissolve
    show scary with dissolve:
        alpha .5
    $mood = "ind"
    bi "Sid's furious all of a sudden, but I can't blame him."
    bi "We're so close."
    bi "There's only one logical next step."
    bi "This could be it..."
    bi "Let's settle this!"
    hide scary with dissolve
    b "Okay! Sam, Shahar, Kaiser, and Lauren."
    show sam ind with dissolve:
        xcenter .125
    show shahar ind with dissolve:
        xcenter .38
    show kaiser ind with dissolve:
        xcenter .6
    show lauren ind with dissolve:
        xcenter .875
    b "You four were up here at the time of the murder."
    b "I need you to to each tell us exactly what you were doing up here at the time of the murder."
    b "{i}Exactly{/i} what you were doing."
    b "Sam, you first."
    s "Sheesh, it's pretty lame that I'm getting roped into this just because I was in this train car..."
    s "Whatever, I was pretty much just looking around."
    s "I wanted to see if I could find anything in the cabinets, in all the corners, etc."
    b "Okay. Shahar, you next."
    h "Aye, captain."
    h "Ya see, I was tryin' at the helm."
    h "If I could figure out 'ow to control the train, I could stop it. No such luck though, laddies."
    b "Hmmm... Kaiser."
    k "If you insist."
    k "I tried some possible passwords, starting with all of our names, to no avail."
    k "Then I searched with Sam for a bit."
    b "And you, Lauren?"
    o "I was unplugging and replugging some of the monitors, hoping maybe something would change."
    o "Nothing changed... and this is what became of it..."
    b "I see."
    hide sam
    hide shahar ind
    hide kaiser ind
    hide lauren ind
    with dissolve
    show scary with dissolve
    bi "That settles it. I know who it was."
    bi "The murderer is..."
    play music "audio/ominous.mp3"
    call screen chooseChar2("kaiser", "trial1q", "  ") with dissolve

label trial1q:
    stop music
    show kaiser dead:
        xcenter .6
    play sfx "audio/shatter.mp3" volume .8
    #pause 1
    blank "........"
    show kaiser dead:
        linear .75 xcenter .5
    blank "It... has to be Kaiser."
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    with dissolve
    show kaiser ind
    #show bg NOtrainFRONT
    with dissolve
    play music "audio/coming_together.mp3"
    k "Excuse me?"
    k "Are you insinuating that I killed Dan?"
    b "No, I'm proclaiming it. It had to have been you."
    b "We have all the evidence we need now."
    k "Excuse me, but how did you come to such a ridiculous conclusion?"
    k "Surely the four of us tell you what we were doing couldn't have been the deciding factor."
    b "It was, Kaiser!"
    b "You said you were trying everyone's names as passwords."
    k "That's exactly what happened, you fool."
    b "We know that can't be true!"
    k "Pardon me, bu-"
    b "Think back to yesterday! We have proof you couldn't have done that."
    b "Who said it..."
    show scary with dissolve
    play music "audio/invest1.wav"
    call screen chooseChar("sid", "trial1r", "Who knows the truth?") with dissolve
label trial1r:
    scene black
    play music "audio/coming_together.mp3"
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    with dissolve
    show kaiser ind with dissolve
    k "Excuse... me...?"
    b "It's true!"
    show kaiser ind:
        linear .3 xcenter .75
    show sid ind with dissolve:
        xcenter .25
    i "M-me?"
    b "Yes! Think back to what you said yesterday!"
    b "You can prove that Kaiser was the one who killed Dan!"
    i "I..."
    show sid happy:
        xcenter .25
    i "You're right! I do know!"
    i "Kaiser couldn't possibly have tested everyone's name as passwords!"
    i "After 5 attempts it locks you out!"
    hide sid happy
    show sid ind:
        xcenter .25
    show kaiser ind:
        linear .1 xcenter .775
    k "What?! Surely you're joking..."
    i "No, it's true!"
    blank "Lauren rushed over to a computer and started typing."
    show scary with dissolve:
        alpha .5
    bi "Did Kaiser really kill Dan?"
    bi "I know someone had to have done it, but..."
    bi "It's hard to actually accept the truth."
    hide scary with dissolve
    hide sid ind with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    o "It's... true."
    o "After 5 attempts it stopped me from typing anything else in."
    o "There's no pop-up or anything, but it's impossible to input any new letters."
    stop music fadeout 1.0
    o "I... can't believe it, Kaiser, did you really do this?"
    b "..."
    k "..."
    show screen killuser
    play sound "audio/ch1guilty.mp3" volume .75
    $renpy.movie_cutscene("ch1guilty.webm")
#    $ renpy.pause(3, hard=True)
    hide screen killuser
    hide movie "ch1guilty.webm" with dissolve
    play music "audio/ominous.mp3" fadein 1.0
    $mood = "shock"
    k "Yes, you've figured it all out."
    k "I'm impressed, quite frankly."
    hide lauren ind with moveoutleft
    show kaiser ind:
        linear .3 xcenter .5
    k "I killed Dan, there's no reason to claim otherwise now."
    b "But... but why?"
    b "Why would you do something like that?"
    k "A wonderful question, truly."
    k "And I wish I had a better answer."
    k "You see..."
    show doom
    #show doom #wrong spot
    with dissolve
    k "I too have been hiding some personal details."
    k "I liked to imagine I was past my crime days, but... alas."
    b "Crime?"
    k "My homeland was very dependent on trains."
    k "Be it for bourgeoisie travels, international trading, civilian errands."
    k "Everything revolved around the rails."
    k "I was personally never much of a fan of the trains."
    b "Where are you going with this?"
    k "You see, such methods are vulnerable to heists and robbery."
    k "I took great advantage of this."
    $mood = "sad"
    b "You were a train robber?"
    k "Yes. I did what I must to make ends meet for my family."
    k "I did not hurt anyone, I simply stole from those with extra resources."
    b "Until today..."
    k "Yes, until today."
    b "But why?"
    k "I didn't have a choice."
    k "I had to kill the Game Master."
    b "What? How do you know he was the Game Master?"
    k "I don't know for sure, but... his personality was..."
    k "So cold."
    show kaiser ind:
        linear .3 xcenter .75
    show sid mad with dissolve:
        xcenter .25
    i "You... you killed my friend! He didn't deserve to die!"
    show kaiser ind:
        linear .1 xcenter .7
    k "How do you know that?"
    k "Maybe he was the Game Master."
    k "For all we know, he was behind this whole thing."
    i "No way!"
    b "How did you know the password to the computer?"
    k "That is exactly how I knew it was my turn."
    b "Your turn? What do you mean?"
    k "I've been on, and robbed, trains quite similar to all three of these."

    scene black with fade
    show bg trainback at bg with fade:
        zoom .7 xcenter .5 ycenter .5
    $mood = "ind"
    k "My town had dozens of trains that closely resembled the caboose..."
    k "My family's business, as well."
    k "It reminds me of my mother, in an unfortunate way."
    show bg trainmid at bg with fade:
        zoom .7 xcenter .5 ycenter .5
    k "The bar car as well felt... familiar."
    k "Those privileged bastards always had something upscale like it when passing through."
    k "Even being in there there past few days... it makes my blood boil."
    k "Disgusting."
    scene black
    #play music "audio/coming_together.mp3"
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    show doom
    with dissolve
    show kaiser ind:
        xcenter .7
    show sid ind:
        xcenter .25
    with dissolve

    k "And then... this car."
    k "It reminds me of one heist in particular, my most famous heist."
    k "In fact, it's nearly identical to the train from then."
    b "So you tried the same password? From that heist?"
    k "Yes, and it worked."
    k "It was going to be my big break... and for a while, I thought it was."
    k "How naive of me..."
    k "Regardless, I have made my decision."
    k "I killed Dan. Whether he was the Game Master or not, there's no way for us to know yet."
    k "I had hoped to conceal my guilt, akin to the Game Master's original message..."
    scene black with fade
    scene expl 9a
    show sepia:
        alpha .5
    with dissolve
    scr "The game will then continue with the surviving participants."
    scr "However, if they can't identify who the real murderer was,"
    show text "{b}{color=#000000}Kill the Game Master. Or, kill anyone else and get away with it.{/color}{/b}" with dissolve:
        ycenter .65
        xcenter .495
    scr "everyone but the murderer and Game Master will be killed, and the game ends."
    scene black
    #play music "audio/coming_together.mp3"
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    show doom
    with dissolve
    show kaiser ind:
        xcenter .7
    show sid ind:
        xcenter .25
    with dissolve
    k "I'm not particularly well versed at hiding my guilt..."
    k "So, Game Master."
    k "Was I correct?"
    $mood = "shock"
    k "If you are still alive, punish me."
    b "What? No!"
    k "If Dan was not the Game Master, my fate is death."
    k "Show me. Show me my fa-{p=0.5}{nw}"
    stop music
    show braindeath
    pause .25
    hide kaiser ind
    show doom
    hide braindeath with dissolve
    hide sid ind
    show sid happy:
        xcenter .25
        linear .1 xcenter .2
    blank "Kaiser fell to the floor."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .3
        ycenter .25
        zoom .75
    b "Wh-what?!"
    i "No no no no no!"
    c "Oh my god oh my god oh my god oh my god!"
    i "What happened?!"
    b "He just, "
    extend "died..."
    show bg notrainfront1 at bg
    with dissolve
    pause 1.0
    show bg notrainfront2 at bg with dissolve
    pause 1.0
    b "..."
    b "He was wrong... Dan was... innocent."
    i "Dan... Kaiser..."
    b "They're both dead."
    b "I survived... we, the 10 of us, survived..."
    bi "Technically, we were closer to winning this game."
    bi "But really, we had lost more than we had won."
    b "...what n-{p=0.5}{nw}"
    scene black
    pause 1.0
    bi "A more humane person would have given us some time."
    bi "To celebrate, to reflect, to mourn."
    bi "But instead, with no warning, I passed out."
    play music "audio/ominous.mp3" fadein 3.0
    show endch1 with Dissolve(3.0)
    pause
    stop music fadeout 3.0
    hide endch1 with Dissolve (3.0)
    $ MainMenu(confirm=False)()
