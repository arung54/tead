$dan = True

label splashscreen:
    scene black
    with Pause(1)
    show tead with dissolve
    with Pause(2)
    return

screen intros():
    imagemap:
        ground "bg startmeet.png"
        hotspot(420, 69, 10, 10) action [Hide("intros", transition=Fade), Jump("ligma")]
    add "status.png"
    add Text("{b}???{/b}") xpos 1055 ypos 5 xanchor 0 yanchor 0
    add "ch0.png" xpos 1095 ypos 65 xanchor 0 yanchor 0
    add "danchibi2.png" xpos 1225 ypos 55 xanchor 0 yanchor 0
    if meetings[0] == 1:
        imagebutton:
            xpos 20
            ypos 20
            idle "bertchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetBert")]
    if meetings[1] == 1:
        imagebutton:
            xpos 20
            ypos 20 + 50*sum(meetings[0:1])
            idle "samchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetSam")]
    if meetings[2] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:2])
            idle "stellachibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetStella")]
    if meetings[3] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:3])
            idle "sidchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetSid")]
    if meetings[4] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:4])
            idle "jennychibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetJenny")]
    if meetings[5] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:5])
            idle "catherinechibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetCatherine")]
    if meetings[6] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:6])
            idle "kaiserchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetKaiser")]
    if meetings[7] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:7])
            idle "draculachibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetDracula")]
    if meetings[8] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:8])
            idle "laurenchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetLauren")]
    if meetings[9] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:9])
            idle "freddychibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetFreddy")]
    if meetings[10] == 1:
        imagebutton:
            xpos 20
            ypos 20+50*sum(meetings[0:10])
            idle "shaharchibi.png" at chibizoom
            action [Hide("intros", transition=Fade), Jump("meetShahar")]

label ligma:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show bert happy with dissolve
    bt "Hey Dan, you ever think about removing the A from your first name?"
    n "My name would be D-N? What does that even mean?"
    bt "DEEZ NUTZ!"
    n "..."
    ni "Damn, he got me."
    hide bert with dissolve
    call screen intros with dissolve


label meetBert:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show bert happy with dissolve
    bt "Hi, my name's Bert Kim."
    n "Hey, I'm Dan."
    $menuset = set()
    show bert ind
    menu bertQuestions:
        set menuset
        "What should I ask Bert?"

        "What do you do for a living?":
            bt "I graduated pretty recently, I'm a software engineer now."
            n "Damn, you must be pretty smart."
            bt "That's nice of you to say! But I think these days most people can pick up coding if they try really hard."
            jump bertQuestions

        "What were you doing before you ended up here?":
            bt "I was at this really great Italian restaurant just enjoying some pasta."
            bt "Tortellini with pesto... man I'm sad I didn't get to finish it."
            bt "Well, I guess that's the last thing I remember."
            bt "I imagine there's more between then and now that I don't remember."
            n "Yeah, same for me..."
            jump bertQuestions

        "Why do you think we're here?":
            bt "Hmm, I honestly have no idea."
            bt "If I were still in college I'd think I was getting hazed by some frat."
            bt "Maybe everyone here knows something the government doesn't want us to."
            bt "And they brought everyone here to mind wipe us or something?"
            n "That's... a theory."
            ni "I think the government would've just left me in prison if that were the case."
            jump bertQuestions

        "Finish talking to Bert." if len(menuset) > 0:
            jump postMeetBert
label postMeetBert:
    ni "I think that's everything I want to ask Bert."
    hide bert with dissolve
    $ meetings[0] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetSam:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show sam ind with dissolve
    s "Not really one for formalities, but I'm Sam. Sam Lee."
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
            ni "Hm... sounds a lot easier than kidnapping someone from a prison."
            jump samQuestions

        "Why do you think we're here?":
            s "I don't know about everyone else, but I am pretty politically active."
            s "Maybe I made some enemies and they're using rather underhanded tactics?"
            ni "I don't even know the results of the last election, are we really all someone's political enemies?"
            jump samQuestions

        "Finish talking to Sam." if len(menuset) > 0:
            jump postMeetSam
label postMeetSam:
    ni "Hmm, I learned a little bit about Sam."
    hide sam with dissolve
    $ meetings[1] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetStella:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
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
            t "One of the largest investment firms in the world, surely you've heard of it."
            n "Ah, yeah that rings a bell."
            ni "The truth is I know her but..."
            ni "No way in hell I can let her know that."
            jump stellaQuestions

        "What were you doing before you ended up here?":
            t "I was at a cute prince's estate, spending the night."
            ni "She really has no shame..."
            t "Naturally, I can't let the boys near my home office where business secrets are, otherwise we'd be at my place."
            t "He had gone out to get us some breakfast while I was laying in bed."
            t "Next thing I can remember, I'm here."
            jump stellaQuestions

        "Why do you think we're here?":
            t "Hm. The rest of you don't look rich, otherwise the answer would be easy."
            t "Someone's holding me for ransom."
            ni "Rich people really are judgmental, aren't they..."
            jump stellaQuestions

        "Finish talking to Stella." if len(menuset) > 0:
            jump postMeetStella
label postMeetStella:
    ni "Going to have to keep my eye on her."
    ni "Hopefully she doesn't know my secret..."
    t "Don't stray too far, cutie."
    hide stella with dissolve
    $ meetings[2] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetSid:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show sid ind with dissolve
    i "Hey I'm Sid Straits. Don't forget it!"
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
            i "N-never mind, I didn't do anything wrong..."
            i "And even if I had committed a crime, they wouldn't arrest a minor like me, r-right?"
            ni "I {i}really{/i} hope this isn't a jail."
            jump sidQuestions

        "Finish talking to Sid." if len(menuset) > 0:
            jump postMeetSid
label postMeetSid:
    ni "Seems like a pretty headstrong kid."
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        xcenter .4
        ycenter .25
        zoom .75
    i "Hey, what about you? Tell me more about you."
    ni "I was hoping I wouldn't really have to talk about myself."
    hide pophuh
    n "Not much to say. I'm just a regular guy."
    i "You seem kinda like a punk."
    ni "Haha... I guess he's not wrong."
    ni "Takes one to know one."
    hide sid with dissolve
    $ meetings[3] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetJenny:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show jenny happy with dissolve
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .5
        ycenter .5
    j "Hiya! I'm Jenny Flowers."
    n "Hey, I'm Dan."
    hide pophearts
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
            j "I've seen movies where casinos beat people up who do that kind of thing in a more organized manner."
            j "Maybe this is that kind of thing? Did the rest of you make a casino upset?"
            j "I hope they know they'd be monsters if they punched a girl!"
            ni "How is she saying that with such a bubbly expression?"
            jump jennyQuestions

        "Finish talking to Jenny." if len(menuset) > 0:
            jump postMeetJenny
label postMeetJenny:
    ni "An interesting girl."
    hide jenny with dissolve
    $ meetings[4] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetCatherine:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show catherine happy with dissolve
    c "Heya! I'm Catherine Henson, and this is Sesame Henson!"
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
            ni "As a rule of thumb, I don't often label kidnappers as gentle..."
            jump cathQuestions

        "Why do you think we're here?":
            c "Honestly? No idea."
            c "Maybe I pissed off someone who I denied an adoption to?"
            ni "Somehow I doubt pet adoptions are the motivation here..."
            jump cathQuestions

        "Finish talking to Catherine." if len(menuset) > 0:
            jump postMeetCatherine
label postMeetCatherine:
    ni "She's kinda... weird? Her cat is cute though."
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .5
        ycenter .5
    c "Good to meet you Dan!"
    hide pophearts
    ni "Maybe a bit too bubbly, given the circumstances..."
    hide catherine with dissolve
    $ meetings[5] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetKaiser:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show kaiser ind with dissolve
    k "Greetings, I'm Kaiser Maden."
    n "Hey, I'm Dan."
    $menuset = set()
    menu kaisQuestions:
        set menuset
        "What should I ask Kaiser?"

        "What do you do for a living?":
            k "I'm a logistics analyst for a large retail company."
            k "Basically just work on projects to optimize the shipping and distribution side of things."
            k "It's the kind of job that most people think sounds boring but I think it's a fun challenge."
            ni "Yup, sounds boring to me."
            jump kaisQuestions

        "What were you doing before you ended up here?":
            k "I think I was in a taxi back home from a bar."
            k "That's the last thing I remember, though that's somewhat odd..."
            k "I feel like I should at least remember leaving the taxi, unless the driver is complicit in all this."
            jump kaisQuestions

        "Why do you think we're here?":
            k "I don't know, maybe a terrorist attack?"
            k "Like the Iranian hostage crisis or something?"
            k "Hard to say without meeting the people behind it."
            jump kaisQuestions

        "Finish talking to Kaiser." if len(menuset) > 0:
            jump postMeetKaiser
label postMeetKaiser:
    ni "I learned a little bit about Kaiser."
    hide kaiser with dissolve
    $ meetings[6] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetDracula:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show drac ind with dissolve
    d "Hello. I'm Dracula."
    n "...Like the vampire?"
    d "Yes."
    ni "...I don't know if I believe him."
    ni "I've never had someone introduce themselves as a famous vampire before."
    n "I'm Dan, it's... nice to meet you."
    $menuset = set()
    menu dracQuestions:
        set menuset
        "What should I ask Dracula?"

        "What do you do for a living?":
            d "Let's just say during the day I don't do a whole lot."
            d "But what I do at night is very lucrative."
            ni "...that just sounds like you're a prostitute."
            n "That... really isn't very helpful."
            d "For your sake and mine, it's better I don't give a helpful answer to that question."
            jump dracQuestions

        "What were you doing before you ended up here?":
            d "I think I'd just fallen asleep."
            d "I work odd hours, so I sleep during the day."
            d "So I've tuned my sleep environment to mute sounds and block out light."
            d "That may have made it easy for a kidnapper to approach me."
            jump dracQuestions

        "Why do you think we're here?":
            d "There's a lot of money to be made from human bodies."
            d "Ransom, organ harvesting, slavery."
            d "Wouldn't surprise me if it were one of those."
            d "But our kidnapper did put a lot of effort into this setup."
            d "Usually human trafficking is much less... elegant."
            ni "Bro?"
            n "Haha... yeah."
            jump dracQuestions

        "Finish talking to Dracula." if len(menuset) > 0:
            jump postMeetDracula
label postMeetDracula:
    ni "Is this guy really {i}the{/i} Dracula? Hmmm..."
    d "It is truly a pleasure to meet you, Dan."
    hide drac with dissolve
    $ meetings[7] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetLauren:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show lauren ind with dissolve
    o "Hi, I'm Lauren Palmer."
    n "Hey, I'm Dan."
    $menuset = set()
    menu laurenQuestions:
        set menuset
        "What should I ask Lauren?"

        "What do you do for a living?":
            o "I'm a manager for a local athletics retail store."
            o "The sports I like are not so easy to go pro in, otherwise I would be doing that."
            n "Oh, what kinds of sports?"
            o "I'd... rather not get into that."
            ni "?"
            jump laurenQuestions

        "What were you doing before you ended up here?":
            o "There's a kid I'm sort of a mentor to."
            o "Not related by blood or anything, just someone I met through a friend."
            o "I was on my way back home after spending some time with him."
            o "Thing is, I'm absurdly careful about walking around by myself."
            o "So if I got kidnapped, they must have been very precise about it..."
            jump laurenQuestions

        "Why do you think we're here?":
            o "No clue."
            o "I feel like I've lived a pretty honest and boring life."
            o "There has to be a million people in my city who'd be better kidnapping targets than me."
            jump laurenQuestions

        "Finish talking to Lauren." if len(menuset) > 0:
            jump postMeetLauren
label postMeetLauren:
    ni "She seems pretty reasonable."
    hide lauren with dissolve
    $ meetings[8] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetFreddy:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show frog ind with dissolve
    f "H-hey, I'm Freddy Ogden. But I like it when people call me Froggy!"
    n "Hey, I'm Dan."
    $menuset = set()
    menu froggyQuestions:
        set menuset
        "What should I ask Froggy?"

        "What do you do for a living?":
            f "I-I'm twelve, mister."
            f "I just go to school and my parents feed me and buy me things when I ask."
            ni "...in retrospect, that was a pretty dumb question."
            jump froggyQuestions

        "What were you doing before you ended up here?":
            f "I... I was taking a nap."
            f "I'd just had a long day of playing video games!"
            f "Uh... I ate a cookie?"
            ni "This isn't getting anywhere..."
            jump froggyQuestions

        "Why do you think we're here?":
            f "I... I dunno?"
            f "Is this... a surprise party set up by my parents?"
            f "Am- am I getting bullied?"
            f "Or... is this a dream?"
            n "I wish it was, kid."
            jump froggyQuestions

        "Finish talking to Freddy." if len(menuset) > 0:
            jump postMeetFreddy
label postMeetFreddy:
    ni "It's hard to make heads or tails of this kid."
    hide frog with dissolve
    $ meetings[9] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve

label meetShahar:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    show shahar ind with dissolve
    h "Ahoy there matey! Yer talking to Shahar Syed, the finest pirate on the seven seas."
    ni "...is this guy serious?"
    n "Hey, I'm Dan."
    $menuset = set()
    menu shaharQuestions:
        set menuset
        "What should I ask Shahar?"

        "What do you do for a living?":
            h "Didn't ye hear me lad?! I'm the finest pirate on the seven seas."
            n "...oh, I thought you were joking."
            n "Trying to lighten up the situation."
            h "No, I'm a pirate, right before yer very eyes!"
            ni "...I think I'd prefer to believe he's joking."
            jump shaharQuestions

        "What were you doing before you ended up here?":
            h "I was enjoying my love, the sea."
            n "...so you were on a ship?"
            h "Nay, lad. I was sitting on the beach, enjoying the sunset."
            ni "Wasn't expecting something like that from such a macho man."
            jump shaharQuestions

        "Why do you think we're here?":
            h "Thinking isn't exactly my strong suit, mate."
            h "Ye look like a smart guy, why don't ye be the captain here and tell me why we're here!"
            n "Uh... I don't know, have you looted or plundered any villages with angry mayors?"
            h "Mate, what do ye think this is, the 16th century? Piracy is serious business! We loot towns, not villages!"
            n "..."
            jump shaharQuestions

        "Finish talking to Shahar." if len(menuset) > 0:
            jump postMeetShahar
label postMeetShahar:
    ni "I uhh, what? Why did I just talk to a pirate..."
    hide shahar with dissolve
    $ meetings[10] = 0
    if 1 not in meetings:
        jump postMeetings
    call screen intros with dissolve


label go: #Add silhouttes here?
    scene black
    $mood = "ind"
    $dan = True
    $noside = True
    warden "Dan Scagnelli, wake up."
    mi "Another morning being woken up by the prison loudspeaker."
    mi "It's gotten to the point where the sound of a loud alarm clock would be music to my ears."
    warden "Dan Scagnelli, wake up. That is an order."
    mi "Ugh... don't want to wake up for another day of this..."
    scene bg phall
    show cellwindow
    $ statusnt("Prison", "", ch = 0, sun = 0)
    with dissolve
    #warden "Dan Scagnelli, do not make me repeat myself."
    ni "Why me specifically... what did I do wrong?"
    #n "I'm up, I'm up. Just getting used to the light."
    #ni "I realized how dumb I sounded, light was barely filtering into the cell."
    ni "Seems like it's only sunrise now."
    ni "Why am I being woken so early?"
    warden "Dan Scagnelli. You're being released."
    n "..."
    n "What!?"
    warden "Your sentence ends today."
    ni "I... I thought I was stuck here for a few more years?"
    #warden "I don't know what to tell you, just following orders."
    warden "Someone's come for you."
    warden "They're on their way to your cell."
    ni "What's going on? Who could possibly be coming to bail me out?"
    ni "Did someone get the money? There's no way."
    ni "Maybe it's a mistake?"
    show shadowyfigure ind behind cellwindow
    $ showchibint("myster")
    with dissolve
    z "Dan Scagnelli, I take it?"
    n "Wh-who are you?"
    ni "Who is this? They're completely covered up in shadow."
    z "Don't worry about who I am for now. Let's get going."
    n "Why did you do this for me?"
    z "Put your civilian clothes on."
    play sfx "audio/butt.mp3" volume .5
    hide cellwindow with dissolve
    ni "They unlocked my cell and threw my old clothes in."
    ni "I changed quickly."
    $ statusnt("Prison", "dan", ch = 0, sun = 0)
    $ showchibint("myster")
    show shadowyfigure ind:
        linear .3 xcenter .75
    show dan ind with moveinleft:
        xcenter .25
    #with dissolve
    z "Much better."
    ni "I could barely remember how long it had been since I last wore these..."
    #ni "After I'd changed, he unlocked the cell, cuffed me and we made our way out."
    #ni "A stranger was there to greet me."
    #ni "I wish I knew who it was, but they had concealed their face."
    #ni "Surely no reasonable prison would let someone like this bail a prisoner out?"
    n "Now tell me... who are you?"
    z "Look, Dan."
    hide dan ind with moveoutleft
    $noside = False
    z "I'll be the one asking the questions for now."
    show bg debatescroll:
        zoom 1.1 ycenter .3
    $ statusnt("???", "dan", ch = 0, sun = 0)
    with dissolve
    play music "audio/ominous.mp3" fadein 1.0
    show shadowyfigure scary:
        linear .3 xcenter .5
    $mood = "shock"
    ni "Wh-what's going on?"
    z "Dan... do you feel guilty?"
    n "Guilty?"
    n "I mean... yes, I feel guilty for what I did in the past."
    n "But I didn't really have a choice back then."
    n "And I'm not the same person now that I was before."
    n "So I feel guilty, but I'd like to leave it in the past, and live life as a new me who learned from my mistakes."
    n "Isn't that what the prison system's for?"
    z "I see."
    z "Was anyone harmed by your past crimes?"
    n "Well... they weren't exactly victimless crimes."
    z "Do you think the people who were harmed could leave it in the past?"
    n "...No, I guess that would be pretty difficult."
    z "What about their loved ones? People who depended on them?"
    z "Do you think they can so easily forgive and forget?"
    n "What's your point?"
    z "What makes you think you have the right to forgive yourself if those people could never forgive you?"
    n "That's... a bit of a leading question."
    z "I see."
    z "Well then, let's not waste anymore time here."
    z "You have plenty of hard work ahead of you..."
    show handextend with dissolve:
        #zoom 4
        xcenter .45
        ycenter .62
    z "Come with me."
    ni "They extended their hand."
    ni "Who... who is this?"
    ni "Should I go with them?"
    menu:
        ni "Do I take the hand?"

        "Yes.":
            n "..."
            $mood = "ind"
            n "Okay."
            ni "I reached out and grabbed the hand."

        "No.":
            $mood = "ind"
            n "I... don't trust you."
            z "I'm sorry."
            z "But it is not an option."
            ni "...Somehow I felt compelled to grab the hand, despite my brain saying otherwise."
    #n "Why did you do this for me?"
    #z "Questions later, when we're in the car."
    #z "Here's a sandwich, eat it, you'll want some energy where we're headed."
    #n "Which is?"
    #z "Questions in the car."
    #n "Surely you can explain while we're walking."
    #z "That's not really a good way to talk to someone who got you out. Eat while walking."
    #ni "I started eating."
    #ni "The stranger pushed me when they saw I was standing still."
    #z "I said eat while walking."
    #ni "What was so urgent that it needed me to be pulled out of prison and rushed to a car?"
    #ni "We headed outside, and for the first time in ages I was excited to see the glorious sun and greenery."
    scene black with fade
    stop music fadeout 0.5

    #with fade
    #ni "Like a poorly edited TV show, my vision faded to black as we stepped outside."
    #ni "Only it never faded back to light."
    #ni "I lost vision, there was something tingling in my mouth."
    #ni "Was there something in the food?"
    ni "Everything went dark."
    z "I will remember that decision."
    z "Even if you don't."
    ni "My thoughts started to fade slowly."
    ni "My consciousness, my ability to process what was happening to me."
    ni "Fading."
    ni "The last thing I can remember thinking..."
    ni "Whoever this is, they didn't come to save me."

    scene black
    play sfx "audio/heartbeat.mp3" volume 0.5
    pause 2.0
    play sfx "audio/heartbeat.mp3" volume 0.5
    pause 1.0
    blank "....."
    blank "........."
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
    $ statusnt("???", "dan", ch = 0, sun = 0)
    with fade
    ni "{i}.....!{/i}"
    $mood = "shock"
    ni "Where... am I?"
    ni "How did I get here?"
    ni "Last thing I remember... I was in my cell being told I'd get out."
    ni "The warden called for me and told me I was being released..."
    ni "...why can't I remember anything past that?"
    ni "Now I'm on the floor in what looks like a little cell."
    $mood = "ind"
    ni "Hmmm... I don't have anything with me."
    ni "Not even ID in my pockets. Someone must have taken it from me."
    ni "What's going on here?"
    play sfx "audio/beep.mp3"
    pause 1.0
    ni "What was that sound?"
    ni "Oh, it came from that door. It sounds like it unlocked..."
    ni "Let's see what's on the other side..."
    scene black with fade
    ni "I pushed the door open into a larger, circular room."
    ni "Just as I did, so did eleven other people."
    ni "It seems like they all came from their own room, like myself."
    play music "audio/coming_together.mp3"


    scene bg startmeet

    $ statusnt("???", "dan", ch = 0, sun = 0)
    with fade
    $ showchibint("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula", "lauren", "freddy", "shahar")
    ni "I quickly glanced around to familiarize myself with everyone."
    show bert ind:
        xcenter .25
    with dissolve

    ni "First was a guy with a backpack. He looked like... just a regular guy."
    ni "Nothing wrong with that. Definitely a much better first impression than I probably gave."

    ni "Not the most intimidating but not meek either, I could work with that."
    show sam ind:
        xcenter .5
    with dissolve
    ni "Second, there was someone who looked to be in their early 20s."
    ni "Their figure was somewhat petite, but their resting expression was a very stern one."
    ni "Not threatening per se, but a clear signal not to step on their toes."
    show stella ind:
        xcenter .75
    with dissolve
    ni "Next was a woman in a suit. She looked to be in her late 20s, like me. It was hard to read her expression."
    ni "Her outfit made it seem like she would be very serious, but the way her eyes flicked around..."
    ni "She was definitely checking some of the men in the room out."
    ni "I was mildly offended when she made eye contact with me and then quickly looked away."
    hide bert
    hide sam
    hide stella
    with dissolve
    show sid ind:
        xcenter .25
    with dissolve
    ni "Next to her was a kid. He seemed more confused than the rest of us."
    ni "His outfit was... unusual. Like his wardrobe was made of hand-me-downs and he was worried it would rain."
    ni "Judging by the nametag, his name was Sid. If he's wearing a name tag, he was probably at a job before this?"
    show jenny ind:
        xcenter .5
    with dissolve
    ni "Next was a fashionable girl. Probably a college student."
    ni "Unlike most of us, she seemed to be lost in thought rather than trying to make sense of the situation."
    ni "A lot of the the guys were glancing at her."
    show catherine ind:
        xcenter .75
    with dissolve
    ni "Next was a... woman? In a crop top holding a cat. Honestly, she could have been 15 or 35, it was hard to tell."
    ni "You know how they say pet owners tend to look like their pets?"
    ni "She definitely looked to me like a cat. For a second, I thought she even had narrow pupils."
    ni "Like the previous girl, she was much more preoccupied with her cat than the current situation."
    hide sid
    hide jenny
    hide catherine
    with dissolve
    show kaiser ind:
        xcenter .2
    with dissolve
    ni "Towering over the women was a blonde man. His glasses were very reflective, so it was hard to read his expression."
    ni "His posture was very confident, but besides that I couldn't really tell what to make of him."
    show drac ind:
        xcenter .5
    with dissolve
    ni "And then there was definitely the oldest one here, a... vampire looking dude?"
    ni "Not that any of us knew what was going on, but he definitely gave off a creepy vibe."
    ni "...Seriously though, what's with the outfit?"
    ni "It's like a cross between a Halloween costume and high fashion."
    show lauren ind:
        xcenter .83
    with dissolve
    ni "Moving on, another woman. She gave off much more chill vibes."
    ni "She doesn't look as airheaded as the other girls."
    ni "Her cropped hoodie says \"SAB\", very very faintly. I wonder what that means."
    hide kaiser
    hide drac
    hide lauren
    with dissolve
    show frog ind:
        xcenter .33
    with dissolve
    ni "Next was... okay, honestly I wasn't sure what that was."
    ni "Was it a robot? A child in a frog costume?"
    ni "I'm just going to assume it's a kid. But the outfit they're wearing makes it hard to tell anything else about them."
    show shahar ind:
        xcenter .67
    ni "Last was a... pretty much half-naked man. His outfit was about as out-of-place as the vampire's."
    ni "Maybe it really was Halloween before we all were gathered here."
    ni "I was hoping to get good reads on everyone, but this guy, the frog, and the vampire threw that out the window."
    hide frog
    hide shahar
    with dissolve
    ni "My people watching session was quickly interrupted by someone finally finding the courage to speak up."
    show sam ind with dissolve
    #Make this section longer/make them conclude they kidnapped
    zs "I'm assuming you're all as confused as I am, so let's get straight to figuring things out."
    zs "Anyone know where we are or why we're here?"
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with moveinright:
        xcenter .75
    zc "No clue. The last thing I remember I was out for a walk, totally fine."
    zc "After that, my memory is a haze. It's like I suddenly took a nap and woke up here."
    ni "A few people spoke up at once agreeing."
    hide catherine with moveoutright
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    zs "So no one knows how they got here, and there's probably gaps in our memory..."
    zs "Does anyone recognize anyone else in here?"
    ni "A few people were starting to raise their hands..."
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show stella ind with moveinright:
        xcenter .75
    zt "Besides the world-famous businesswoman, who I'm sure we've all seen on TV."
    ni "A bunch of people were staring at her."
    ni "After that clarification the hands shot back down."
    hide stella with moveoutright
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    zs "So no one personally knows each other, I see. Not even as friends of friends or connections of that sort."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .4
        ycenter .25
        zoom .75
    zs "In that case, I think it's fair to assume we've been placed here against our will then."
    zs "That is to say, we've probably been kidnapped by someone with an unknown motive."
    hide popwow
    ni "I think we all knew this on some level, but several people's expressions sunk upon hearing that."
    ni "Mine not so much. This wasn't much more hopeless than being in a jail cell."
    ni "But at least... some of these people seemed to be ordinary people."
    ni "This was probably the first time most of them had been trapped in a situation like this."
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    zi "Umm... does anyone have a phone? Or something else like that?"
    ni "A few people instinctively checked their pockets."
    ni "A few others made it clear they had checked a few times already."
    zi "I normally always have my phone on me..."
    zs "Yeah, same. Someone must have taken all of our belongings."
    zi "Th-that's... yeah."
    hide sid ind with moveoutleft
    show sam ind:
        xcenter .75
        linear .3 xcenter .5
    zs "Hmmm..."
    zs "Until we have more information, it's probably best to assume our lives are in some sort of danger while we are here."
    zs "In which case I think we should look around and try to find a way out or some answers."
    zs "Any objections?"
    ni "Again, silence."
    zs "Alright, let's look around then."
    hide sam with dissolve
    show scary with dissolve:
        alpha .5
    ni "We looked around for a bit."
    ni "But it quickly became clear there was nothing to find or see here."
    ni "It sounds like we all woke up in this same type of room with no notable features."
    ni "And then the central room connecting them all also had no notable features."
    ni "It was the most nondescript building I'd even been in."
    ni "Even prison had more character than this room."
    ni "The only really notable feature of this building seemed to be there was no exit."
    ni "At least, none we could use."
    hide scary with dissolve
    show sam ind with dissolve
    zs "Anyone have anything to report?"
    show sam ind:
        linear .3 xcenter .75
    show frog sad with moveinbottom:
        xcenter .25
    play sfx "audio/poprain.mp3" volume .5
    zf "Umm... kinda."
    show poprain:
        xcenter .25
        ycenter .1
    with dissolve
    zf "I'm scared... I miss my mom..."
    zs "Not sure that counts as finding something..."
    hide poprain with dissolve
    ni "So it is a little boy in the frog suit."
    n "Why are you wearing that anyway, kid?"
    zf "It makes me feel safe... I'm just a little frog."
    zs "Just try to stay calm for now and the adults will figure this out."
    zf "O-okay."
    hide frog ind with moveoutbottom
    show sam ind:
        linear .3 xcenter .5
    zs "Anyway, it doesn't seem like anyone found anything useful."
    zs "In that case, does anyone have a particularly good sense of hearing?"
    zs "Perhaps if we listen closely to the walls we will get a sense of whether we're in civilization or not."
    zs "If so, then we could reason about our chances of getting help from the authorities."
    show sam ind:
        xcenter .5
        linear 0.3 xcenter .25
    show catherine ind with moveinright:
        xcenter .75
    zc "I think first we should all introduce ourselves!"
    zc "It seems like we're stuck in here for the moment, it'd be good to know who we're stuck with."
    hide catherine with moveoutright
    show drac ind with moveinright:
        xcenter .75
    zd "I agree. I don't know how to address any of you."
    zd "It'll be hard for us to work together without some sense of camaraderie."
    hide drac with moveoutright
    show sam ind:
        xcenter .25
        linear 0.3 xcenter .5
    zs "Alright, let's take some time to talk to each other."
    ni "Hmm... I don't love making small talk, but I need to blend in at least."
    ni "Let's meet everyone."
    hide sam with dissolve
    tut "Throughout the game, when a character is present in a room, their icon will appear in the top left."
    tut "In some segments you will gain control of the story, and can choose who to talk to."
    tut "To talk to a character, click on their icon in the top left."
    tut "Ask everyone at least one question to progress the story. You can ask more if you're interested."
    $ meetings = [1] * 11
    call screen intros

label postMeetings:
    scene bg startmeet
    $ statusnt("???", "dan", ch = 0, sun = 0)
    ni "And I've met everyone. Looks like the group is reconvening to discuss now."
    $ showchibint("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula", "lauren", "freddy", "shahar")
    with dissolve
    s "Okay, now that that's done, I think we should look around and try-"
    hide sam with moveoutright
    stop music fadeout 1.0
    play sfx "audio/whirr.mp3"
    blank "A whirring noise cut Sam off."
    show bg start2
    $ statusnt("???", "dan", ch = 0, sun = 0)
    with dissolve
    stop sfx fadeout 1.0
    blank "A screen slowly lowered, and everyone's attention turned to it."
    $mood = "shock"
    scr "Welcome."
    scr "The game you all have been brought here to play will now be explained."
    ni "...game?"
    scr "Pay attention closely, as this will only be explained once."
    play music "audio/invest1.wav"
    scene expl 1a with fade
    scr "There are twelve of you here."
    show expl 2a with dissolve
    scr "Eleven were unwillingly forced to participate."
    show expl 3a with dissolve
    scr "The remaining person is the Game Master behind all of this, who will also participate."
    show expl 4a with dissolve
    scr "The identity of the Game Master will not be revealed."
    scr "The goal of the game is simple."
    show expl 5a with dissolve
    scr "Kill the Game Master."
    #show expl kill0 with dissolve
    show text "{b}{color=#000000}Kill the Game Master.{/color}{/b}" with dissolve:
        ycenter .65
        xcenter .29
    scr "The game will be played in rounds."
    show expl 6a
    scr "Each round, one of you who is not the Game Master will be chosen."
    show expl 7a
    scr "The chosen individual must kill someone who they think is the Game Master."
    scr "You may use any method to kill."
    show expl 6b
    scr "If they do successfully kill the Game Master, the game immediately ends and the remaining participants will be let free."
    show expl 7b with dissolve
    scr "If they kill someone who is not the Game Master..."
    scr "They should do their best to hide their guilt."
    show expl 8a
    scr "This is because the remaing participants will investigate and vote on who the murderer is."
    show expl 8b
    scr "If they vote for the murderer correctly, the murderer will be killed."
    scr "The game will then continue with the surviving participants."
    ###########
    scr "However, if they can't identify who the real murderer was,"
    show expl 9a
    #show expl kill1 with dissolve
    show text "{b}{color=#000000}Kill the Game Master. Or, kill anyone else and get away with it.{/color}{/b}" with dissolve:
        ycenter .65
        xcenter .495
    scr "everyone but the murderer and Game Master will be killed, and the game ends."
    show expl 10a
    hide text
    with dissolve
    scr "In short, the murderer wants to kill the Game Master, or kill anyone else, and get away with it."
    scene bg start2
    $ statusnt("???", "dan", ch = 0, sun = 0)
    $ showchibint("bert", "sam", "stella", "sid", "jenny", "catherine", "kaiser", "dracula", "lauren", "freddy", "shahar")
    with fade
    ni "..."
    ni "What the hell is all this..."
    scr "A chip has been planted in each of your heads, capable of killing you instantly."
    scr "This chip will be used to resolve the outcome of the vote."
    ni "Does technology like that really exist?"
    ni "And when did they plant the chip?"
    scr "Each round of the game will take place in a different location."
    scr "The chip will also be used to keep you unconscious as you are transported between locations."
    scr "As proof of this, you will soon be transported to the first location, to play the first round of the game."
    stop music fadeout 1.0
    ni "...what?"
    ni "How would we even know who to kill?"
    ni "This game... it's so much to process."
    ni "There's no clear path to victory."
    ni "Looking around, it was clear others were just as shocked."
    show shahar mad with dissolve
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .5
        ycenter .25
    h "A... a game where we all have to bloody kill each other?"
    h "Not me cup o' booze."
    hide popmad
    hide shahar with dissolve
    show drac oh with dissolve
    d "This is... inhumane, to say the least."
    ni "Is this really happening?"
    hide drac with dissolve
    scr "You may be scared to kill someone who isn't the mastermind."
    scr "You may feel sorry when someone dies."
    scr "Let me assure you of one thing."
    scr "Everyone who dies in the course of the game..."
label testmontage:
    #scr "Their endings are deserved."
    scene black with fade
    show text "{color=#FFFFFF}Their Endings Are Deserved.{/color}" with dissolve:
        ycenter .5
        xcenter .5
    pause(1)
    hide text with dissolve
    $_game_menu_screen = None
    show screen killuser
    play sound "<from 0.1 to 12.2>audio/welcome.mp3"
    $renpy.movie_cutscene("ch1trailer.webm")
    hide screen killuser
    $_game_menu_screen = "save_screen"
    stop sound fadeout 1
    jump trainGo
