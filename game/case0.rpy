screen intros():
    add "bg startmeet.png"
    if meetings[0] == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png"
            action [Hide("intros"), Jump("meetBert")]
    if meetings[1] == 1:
        imagebutton:
            xpos 20
            ypos 20 + 50*meetings[0]
            idle "samchibi.png"
            action [Hide("frontCar"), Jump("meetSam")]
    if meetings[2] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:1])
            idle "stellachibi.png"
            action [Hide("frontCar"), Jump("meetStella")]
    if meetings[3] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:2])
            idle "sidchibi.png"
            action [Hide("frontCar"), Jump("meetSid")]
    if meetings[4] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:3])
            idle "jennychibi.png"
            action [Hide("frontCar"), Jump("meetJenny")]
    if meetings[5] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:4])
            idle "catherinechibi.png"
            action [Hide("frontCar"), Jump("meetCatherine")]
    if meetings[6] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:5])
            idle "kaiserchibi.png"
            action [Hide("frontCar"), Jump("meetKaiser")]
    if meetings[7] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:6])
            idle "draculachibi.png"
            action [Hide("frontCar"), Jump("meetDracula")]
    if meetings[8] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:7])
            idle "laurenchibi.png"
            action [Hide("frontCar"), Jump("meetLauren")]
    if meetings[9] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:8])
            idle "freddychibi.png"
            action [Hide("frontCar"), Jump("meetFreddy")]
    if meetings[10] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:9])
            idle "shaharchibi.png"
            action [Hide("frontCar"), Jump("meetShahar")]

label meetBert:
    scene bg startmeet
    show bert happy with dissolve
    b "Hi, my name's Bert."
    n "Hey, I'm Dan."
    $menuset = set()
    menu bertQuestions:
        set menuset
        "What should I ask Bert?"

        "What do you do for a living?":
            b "I graduated pretty recently, I'm a software engineer now."
            n "Damn, you must be pretty smart."
            b "That's nice of you to say! But I think these days most people can pick up coding if they try really hard."
            jump bertQuestions

        "What were you doing before you ended up here?":
            b "I was at this really great Italian restaurant just enjoying some pasta."
            b "Tortellini with pesto... man I'm sad I didn't get to finish it."
            b "Well, I guess that's the last thing I remember."
            b "I imagine there's more between then and now that I don't remember."
            n "Yeah, same for me..."
            jump bertQuestions

        "Why do you think we're here?":
            b "Hmm, I honestly have no idea."
            b "If I were still in college I'd think I was getting hazed by some frat."
            b "Maybe everyone here knows something the government doesn't want us to."
            b "And they brought everyone here to mind wipe us or something?"
            n "That's... a theory."
            ni "I think the government would've just left me in prison if that were the case."
            jump bertQuestions

        "Finish talking to Bert." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetBert
label postMeetBert:
    hide bert with dissolve
    ni "I think that's everything I want to ask Bert."
    $ meetings[0] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetSam:
    scene bg startmeet
    show sam ind with dissolve
    s "Not much of a formalities guy, but I'm Sam."
    n "Hey, I'm Dan."
    $menuset = set()
    menu samQuestions:
        set menuset
        "What should I ask Sam?"

        "What do you do for a living?":
            s "I'm still in college. Working on a degree in political science."
            s "I have some side jobs to help me pay my way through."
            n "Are you planning to work as a legislator?"
            s "Hopefully yeah. There's some political causes I'm heavily invested in."
            s "I think becoming a politician is one of the most effective ways to work on those causes."
            ni "Hope reforming the prison system is one of them..."
            jump samQuestions

        "What were you doing before you ended up here?":
            s "Last thing I remember is I was on my way back to my dorm from the campus library."
            s "I'd been up late working on an assignment, so campus was pretty empty."
            s "Maybe that's how our kidnapper was able to get me."
            ni "Hm... sounds a lot easier than breaking kidnapping someone from a prison."
            jump samQuestions

        "Why do you think we're here?":
            s "I don't know about everyone else, but I am pretty politically active."
            s "Maybe I made some enemies and they're using rather underhanded tactics?"
            ni "I don't even know the results of the last election, are we really all someone's political enemies?"
            jump samQuestions

        "Finish talking to Sam." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetSam
label postMeetSam:
    hide sam with dissolve
    ni "I think that's everything I want to ask Sam."
    $ meetings[1] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetStella:
    scene bg startmeet
    show stella ind with dissolve
    t "You're not my type, but I guess we can talk. I'm Stella Cantoire."
    n "Hey, I'm Dan."
    $menuset = set()
    menu stellaQuestions:
        set menuset
        "What should I ask Stella?"

        "What do you do for a living?":
            t "You haven't heard of me? That's somewhat refreshing."
            t "If only you were younger..."
            n "I... haven't paid much attention to the news recently."
            n "Are you famous?"
            t "I'm CEO of Cantoire Management."
            t "One of the largest investment firms in the country, surely you've heard of it."
            n "Ah, yeah that rings a bell."
            ni "I've been in prison for years now, so that does not ring a bell."
            jump stellaQuestions

        "What were you doing before you ended up here?":
            t "I was at one of my boy toys' apartments, spending the night."
            ni "{i}One of{/i} my boy toys? She really has no shame..."
            t "Naturally, I can't let the boys near my home office where business secrets are, otherwise we'd be at my place."
            t "He had gone out to get us some breakfast while I was laying in bed."
            t "Next thing I can remember, I'm here."
            jump stellaQuestions

        "Why do you think we're here?":
            t "Hm. The rest of you don't look rich, otherwise the answer would be easy."
            t "Someone's holding me for ransom."
            ni "Rich people really are judgmental, aren't they..."
            jump stellaQuestions

        "Finish talking to Stella." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetStella
label postMeetStella:
    hide stella with dissolve
    ni "I think that's everything I want to ask Stella."
    $ meetings[2] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetSid:
    scene bg startmeet
    show sid ind with dissolve
    i "Hey I'm Sid. You better take me seriously!"
    n "Hey, I'm Dan."
    $menuset = set()
    menu sidQuestions:
        set menuset
        "What should I ask Sid?"

        "What do you do for a living?":
            i "I'm still in high school, but I work at a grocery store after school."
            i "But it's not just a high school job! I work just as hard the adults!"
            ni "Defensive today, aren't we?"
            jump sidQuestions

        "What were you doing before you ended up here?":
            i "I think I just got off the bus from work back home."
            i "I was walking home, and that's the last thing I can remember."
            ni "The kid's parents don't pick him up from work? They must also work late hours."
            jump sidQuestions

        "Why do you think we're here?":
            i "I don't know, maybe we got arrested?"
            i "N-never mind, even if I had committed a crime, they wouldn't arrest a minor like me, right?"
            ni "I {i}really{/i} hope this isn't a jail."
            jump sidQuestions

        "Finish talking to Sid." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetSid
label postMeetSid:
    hide sid with dissolve
    ni "I think that's everything I want to ask Sid."
    $ meetings[3] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetJenny:
    scene bg startmeet
    show jenny happy with dissolve
    j "Hey! I'm Jenny."
    n "Hey, I'm Dan."
    $menuset = set()
    menu jennyQuestions:
        set menuset
        "What should I ask Jenny?"

        "What do you do for a living?":
            j "I'm still in college! I'm a statistics major."
            j "But on the side, I'm a competitive poker player."
            j "If I'm able to do well at some tournaments next year, I might try to go pro after graduating."
            n "Damn, there's a lot of really smart people here."
            j "Ha! That's nice of you to say."
            jump jennyQuestions

        "What were you doing before you ended up here?":
            j "I was watching a movie by myself at home."
            j "I guess in some sense, that was the perfect time for someone to kidnap me."
            j "Whoever our kidnapper is, they're a crafty one!"
            n "Yeah, maybe that compliment will convince them to let you go."
            j "Haha! You're funny Dan."
            jump jennyQuestions

        "Why do you think we're here?":
            j "Hmm... I once tried card counting with some friends at a casino."
            j "I've seen movies where casinos hire beat people up who do that kind of thing in a more organized manner."
            j "Maybe this is that kind of thing? Did the rest of you make a casino upset?"
            j "I hope they know they'd be monsters if they punched a girl!"
            ni "How is she saying that with such a bubbly expression?"
            jump jennyQuestions

        "Finish talking to Jenny." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetJenny
label postMeetJenny:
    hide jenny with dissolve
    ni "I think that's everything I want to ask Jenny."
    $ meetings[4] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetCatherine:
    scene bg startmeet
    show catherine happy with dissolve
    c "Heya! I'm Catherine, and this is Sesame!"
    ses "Mreoww!"
    n "Hey, I'm Dan."
    $menuset = set()
    menu cathQuestions:
        set menuset
        "What should I ask Catherine?"

        "What do you do for a living?":
            c "I work at a shelter for cats."
            c "Taking care of them, making sure they get adopted by good owners."
            c "I'm obsessed with cats, so it's basically my dream job!"
            ses "Prrr!"
            c "Oh, and Sesame's job is keeping me company, ehe."
            ni "Glad she's here to translate..."
            jump cathQuestions

        "What were you doing before you ended up here?":
            c "I was sitting outside my place, letting Sesame get some fresh air."
            c "Next thing we know, we ended up here."
            c "Whoever brought us here must be somewhat of a gentle soul, if they brought both of us."
            ses "Mew!"
            ni "As a rule of thumb, I don't often label kidnappers as gentleb..."
            jump cathQuestions

        "Why do you think we're here?":
            c "Honestly? No idea."
            c "Maybe I pissed off someone who I denied an adoption to?"
            ni "Somehow I doubt pet adoptions are the motivation here..."
            jump cathQuestions

        "Finish talking to Catherine." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetCatherine
label postMeetCatherine:
    hide catherine with dissolve
    ni "I think that's everything I want to ask Catherine."
    $ meetings[5] = 0
    if 1 not in meetings:
        ni "I've finally talked to everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetKaiser:
    scene bg startmeet
    show kaiser ind with dissolve
    k "Greetings, I'm Kaiser."
    n "Hey, I'm Dan."
    $menuset = set()
    menu kaisQuestions:
        set menuset
        "What should I ask Kaiser?"

        "What do you do for a living?":
            jump kaisQuestions

        "What were you doing before you ended up here?":
            jump kaisQuestions

        "Why do you think we're here?":
            jump kaisQuestions

        "Finish talking to Kaiser." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetKaiser
label postMeetKaiser:
    hide kaiser with dissolve
    ni "I think that's everything I want to ask Kaiser."
    $ meetings[6] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetDracula:
    scene bg startmeet
    show drac ind with dissolve
    d "Hey, I'm Dracula."
    n "...Like the vampire?"
    d "Yes, that's me."
    ni "...I don't know if I believe him."
    n "I'm Dan, nice to meet you."
    $menuset = set()
    menu dracQuestions:
        set menuset
        "What should I ask Dracula?"

        "What do you do for a living?":
            jump dracQuestions

        "What were you doing before you ended up here?":
            jump dracQuestions

        "Why do you think we're here?":
            jump dracQuestions

        "Finish talking to Dracula." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetDracula
label postMeetDracula:
    hide drac with dissolve
    ni "I think that's everything I want to ask Dracula."
    $ meetings[7] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetLauren:
    scene bg startmeet
    show lauren ind with dissolve
    o "Hi, I'm Lauren."
    n "Hey, I'm Dan."
    $menuset = set()
    menu laurenQuestions:
        set menuset
        "What should I ask Lauren?"

        "What do you do for a living?":
            jump laurenQuestions

        "What were you doing before you ended up here?":
            jump laurenQuestions

        "Why do you think we're here?":
            jump laurenQuestions

        "Finish talking to Lauren." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetLauren
label postMeetLauren:
    hide lauren with dissolve
    ni "I think that's everything I want to ask Lauren."
    $ meetings[8] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetFreddy:
    scene bg startmeet
    show sam ind with dissolve
    f "H-hey, I'm Freddy. But I like it when people call me Froggy!"
    n "Hey, I'm Dan."
    $menuset = set()
    menu froggyQuestions:
        set menuset
        "What should I ask Froggy?"

        "What do you do for a living?":
            jump froggyQuestions

        "What were you doing before you ended up here?":
            jump froggyQuestions

        "Why do you think we're here?":
            jump froggyQuestions

        "Finish talking to Freddy." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetFreddy
label postMeetFreddy:
    hide sam with dissolve
    ni "I think that's everything I want to ask Freddy."
    $ meetings[9] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros

label meetShahar:
    scene bg startmeet
    show shahar ind with dissolve
    h "Ahoy there matey! Y'er talking to Shahar, the finest pirate on the seven seas."
    ni "...is this guy serious?"
    n "Hey, I'm Dan."
    $menuset = set()
    menu shaharQuestions:
        set menuset
        "What should I ask Shahar?"

        "What do you do for a living?":
            jump shaharQuestions

        "What were you doing before you ended up here?":
            jump shaharQuestions

        "Why do you think we're here?":
            jump shaharQuestions

        "Finish talking to Shahar." if len(menuset) > 0 and len(menuset) < 3:
            jump postMeetShahar
label postMeetShahar:
    hide shahar with dissolve
    ni "I think that's everything I want to ask Shahar."
    $ meetings[10] = 0
    if 1 not in meetings:
        ni "And I've met everyone. Looks like the group is reconvening to discuss now."
        jump postMeetings
    call screen intros


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
    scene black
    m "........"
    m "{i}I think I passed out again...{/i}"
    m "{i}Have to... get up...{/i}"
    scene bg start
    ni "{i}.....!{/i}"
    ni "Where... am I?"
    ni "How did I get here?"
    ni "Last thing I remember... I was in my cell being told I'd get out."
    ni "...why can't I remember anything past that?"
    play sfx "audio/beep.mp3"
    ni "Oh, there's a door. Sounds like it just opened."
    ni "Let's see what's on the other side..."
    scene black
    ni "I walked into a very similar room, at the same time as eleven other people."
    scene bg startmeet
    $ showchibi("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula", "lauren", "freddy", "shahar")
    show sam ind with dissolve
    #TODO: Replace w/ everyone introducing 1-by-1
    z "Let's get straight to the point. Anyone know where we are or why we're here?"
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with moveinright:
        xcenter .75
    z "No clue. The last thing I remember I was out for a walk, totally fine."
    hide catherine with moveoutright
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    ni "A few people spoke up at once agreeing."
    z "So no one knows how they got here."
    z "I think we should look around and try to find a way out or some answers."
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with moveinright:
        xcenter .75
    z "Wait, I wanna get to know everyone."
    z "It doesn't seem like we're gonna get out of here easily, it'd be good to know who we're stuck with."
    hide catherine with moveoutright
    show drac ind with moveinleft:
        xcenter .75
    z "I agree with the girl. I don't even know any of your names."
    z "It'll be hard for us to work together without some sense of camaraderie."
    hide drac with moveoutright
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    z "Alright, let's take some time to talk to each other."
    hide sam with fade
    tut "Throughout the game, when a character is present in a room, their icon will appear in the top left."
    tut "In some segments you gain control of the story, and can choose who to talk to."
    tut "To talk to a character, click on their icon in the top left."
    tut "Ask everyone a few questions to progress the story."
    $ meetings = [1] * 11
    call screen intros

    label postMeetings:
    show sam ind with dissolve
    s "Okay, now that that's done, I think we should look around and try-"
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
    h "A... a game where we all have to bloody kill each other?"
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
    scene black with fade
