#Arun

#Train 1
label laurAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show lauren ind with dissolve
    o "You're not being mean to Sid at night, are you?"
    ni "I should go talk to Bert."
    hide lauren with dissolve
    call screen midCar with dissolve

#Train 2
label laurAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show lauren ind with dissolve
    o "What's up Dan, wanted to chat?"
    menu:
        "Spend time with Lauren?":
            o "Sure, not like anything else is happening."
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar with dissolve

#Mansion 1
label laurAsk2:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Mansion 2
label laurAsk3:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Mansion 3
label laurAsk4:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 1
label laurAsk5:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 2
label laurAsk6:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Hospital 3
label laurAsk7:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Bank 1
label laurAsk8:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar
#Bank 2
label laurAsk9:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

#Bank 3
label laurAsk10:
    menu:
        "Spend time with Lauren?":
            j "Sure!"
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

label laurHang:
    #Dan FTE 1
    if fte_laur == -1:
        n "So uh... what's up?"
        o "Oh you know, just stuck on this train."
        o "You're not much of a small talker, are you?"
        ni "No, but I can't seem like an unfriendly face in a situation like this."
        n "Not really, no. Give me a second try?"
        o "Sure."
        n "So you babysat in high school?"
        o "Yeah, hard to have a social life as a high school student without some cash."
        n "Your parents didn't give you an allowance?"
        o "My parents were well off, but pretty strict about only paying for necessary expenses."
        o "They also wanted to instill discipline in me."
        o "I liked kids more than most high schoolers, so it was more like a hobby."
        o "Sometimes I even got lucky and found a gig where the kids just slept and I got paid do homework."
        n "Wait, back up, you like kids more than high schoolers?"
        o "Yeah. High schoolers think they know everything."
        o "But when you look at their sense of morality they really don't."
        o "Not to mention, they're really horny, moody, some do drugs just to feel cool."
        n "As opposed to kids, who are selfless intelligent creatures."
        n "{i}Never{/i} seen a kid be mean to another person."
        o "Yeah, kids aren't perfect either."
        o "But if they aren't, you can try to teach them."
        o "You know how many high school students have been pricks to me?"
        o "I know not one of them would have listened if I explained why."
        o "Some of them are assholes just because they think it's funny."
        o "You think they'd all of a sudden realize their actions affect others?"
        o "I'm not saying every kid is perfect and every high school student sucks."
        o "But the kids that suck, I can teach them."
        o "The high schoolers that suck, nothing short of a kick in the ass from reality will make them learn."
        ni "I was beginning to think this was a sort spot I shouldn't have pressed on."
        n "That's understandable, though I don't think I could ever think like that."
        o "Sorry, I know I got kind of aggressive, but this brought back a lot of dark memories."
        n "Sorry, didn't mean to make you upset."
        n "Just wanted to get to know you better."
        o "I appreciate the effort, but there's better ways to do that then to sass me in our first conversation."
        n "Yeah, no disagreement there."
        ni "We stood in silence for a few seconds."
        n "Uh, I think I'll regroup with the others now."
        o "Uh huh."
        ni "I left with no particular destination, just to give her space."
        scene black with fade
        ni "I know more about Lauren now, but I can't say that conversation was a net positive."
        ni "Maybe I'll try again later."

    #Bert FTE 1
    if fte_laur == 0:
        o "Hey Bert, what can I do for you?"
        b "Oh, I wasn't looking for any favors or anything."
        o "I got that, just an expression. Wanted to chat?"
        b "Yeah, figure if we're all stuck here together for who knows how long we can get to know each other."
        b "I did want to ask, seems like you're very protective of the kids. You said you were a babysitter in high school?"
        o "Well, hard to have a social life as a high school student without some cash."
        o "My parents were well off, but pretty strict about only paying for necessary expenses."
        o "They also wanted to instill discipline in me."
        o "I liked kids more than most high schoolers, so it was more like a hobby."
        o "Sometimes I even got lucky and found a gig where the kids just slept and I got paid do homework."
        b "That's a really nice mindset to have. I've heard stories of high schoolers who mistreated kids they babysat."
        o "Yeah, I knew a few of those types in high school, and it sucks for the kid."
        o "They're usually still at an age where that can make a lasting impression."
        o "Later on when I found other ways to make money, I'd sometimes babysit for a reduced wage."
        o "Not to try to get more hours or anything, but I knew sometimes I'd undercut lazy babysitters in the process."
        b "You found other ways to make money? Like, you worked two jobs in high school?"
        o "It's... not something I'd like to talk to people I don't know that well about."
        o "Not that it's something I'm ashamed of, but people are judgmental."
        o "And I don't want to give anyone who might try to murder me reason to judge me."
        b "Fair enough, I won't push on it."
        b "Though if you undercut a lazy babysitter on one job, wouldn't they just take a different one you didn't have time for?"
        o "Well, my family was well off enough that I went to a pretty good school."
        o "Lots of old money kids, whose parents would buy them most things."
        o "So they considered themselves too dignified to work for low wages, or something like that."
        b "Why babysit in the first place then?"
        o "Well, for example, there was one kid whose parents gave him a credit card, but no way to get cash."
        o "But high schoolers usually get paid in cash, rich high schoolers have nice houses to party in."
        o "If you want to party, you need booze, and even with a fake ID if you buy booze on a credit card, your parents could see it."
        o "Trust me, I know it sounds made up, but despite going to a \"nice\" high school I had plenty of morally questionable peers."
        o "Not that drinking is morally questionable, but being a shit babysitter to party behind your parents back?"
        o "There's other ways to make money as a high schooler that don't involve leaving a kid feeling alone in their own home."
        b "Damn, I wonder how many people like that were at my school that I didn't know about..."
        b "It takes a really strong moral compass to dedicate yourself like that to protecting kids that you have no obligation to help."
        o "Thanks, though I do feel like I have some obligation."
        b "What does that mean?"
        o "I probably said more than I meant to. Sorry, another thing I don't really want to talk about with people I don't know well."
        b "That's totally fine, thanks for opening up as much as you did."
        scene black with fade
        bi "On that note, we went to meet up with the others. I can feel Lauren and I slowly growing closer."

    #Bert FTE 2
    if fte_laur == 1:
        b "Hey Lauren, what does the SAB on your hoodie mean?"
        o "Our conversations keep coming to this, don't they."
        b "Huh?"
        o "You seem genuinely interested in getting to know me so I'll tell you but..."
        o "You won't judge me and you won't tell others about it."
        bi "Is that something I'm ready for? I don't know if we know each other that well."
        b "Promise."
        o "Alright."
        o "The S is short for the town I'm from, that part's pretty innocent."
        o "The A and B stand for Arms and Bullets."
        o "It's a gun shop I was a frequent customer at."
        bi "Does... does she have a gun on her now?"
        o "You're shocked. I'll do you a favor and not count that as judging me."
        bi "I didn't think my fear was {i}that{/i} transparent."
        o "...are you gonna say something?"
        b "Sorry, I just... don't really know people who own guns."
        b "So I've never really been near one."
        o "It's fine, I'll do the talking for now."
        o "To be clear, I'm not a stereotypical gun nut. And no, I don't have a gun with me."
        o "Growing up I had... an incident with a stranger while out with friends."
        o "One that honestly fucked me up pretty badly, not something a high school student should ever go through."
        o "I grew up well off, but that doesn't mean I didn't walk past shady figures while hanging out or running errands."
        o "We live in a city where guns aren't hard to get..."
        o "...so my parents decided I shouldn't leave the house as often for safety."
        o "I protested, and after a long debate they agreed I could go out if I could protect myself."
        o "So I got a concealed carry permit when I turned 18."
        o "I ended up in another incident and... it was pretty clear just having the gun wasn't enough."
        o "Needed to know how to aim it."
        o "I started taking classes and it turns out, with a little guidance my aim is pretty good."
        o "Like, winning competitions good."
        o "Eventually it got to the point where I was winning money from entering competitions."
        o "A lot more money than teenage me knew what to do with"
        o "SAB even sponsored me and gave me discounts, which made it even more profitable."
        o "So... yeah, that's why I'm wearing a gun shop hoodie."
        b "Sorry, I don't know what to say."
        o "It's fine, I can imagine being shocked in your position."
        o "Look, I know guns are terrifying objects that have killed many people who didn't deserve it."
        o "There's a not-so-great culture surrounding them in many parts of the world."
        o "A lot of preventable violence due to guns, situations where another weapon wouldn't have time to do damage."
        o "Again, I've been involved in... incidents where I learned that all too well."
        o "So I'm a huge advocate for heavier background checks and such."
        o "I'd never pull out a gun if I didn't feel like I needed to."
        o "But after what happened, sometimes I'm just not comfortable enough to leave home without protection."
        o "I don't expect you to understand without having gone through what I've gone through."
        o "But I hope you can respect my decision and accept my claim that I'm responsible with these things."
        b "Yeah, I can respect that."
        b "Least I can do after you opened up like that."
        o "Thanks, I honestly appreciate it a lot."
        scene black with fade
        bi "After a heavy conversation, we returned to the others."
        bi "I think I understand Lauren much better now."



    #Bert FTE 3
    if fte_laur == 2:
        o "Hey Bert, gotta tell you, our conversations got real deep real fast."
        b "Yeah, sorry about that."
        b "I know you that sort of stuff is hard to talk to strangers who might want to kill you."
        b "I appreciate your openness, totally get it if you wanna talk more casually."
        o "Well, I'm pretty sure you're not going to try to kill me at this point."
        o "Not to bring up sore spots, but you're one of the few people who opened up about their crime."
        o "And we haven't exactly been anywhere with access to roads."
        o "So I don't really mind bringing it up."
        b "Well, even if you trust me, we haven't known each other that long."
        o "I mean, I've gone through some shit, but I was able to use it to become stronger."
        o "Or at least, stubborn enough to give the illusion of being strong."
        o "And it defines a lot of who I am. My main hobby came out of needing to feel safe."
        o "So really, I don't mind talking about it."
        show lauren happy
        o "But it would be nice if we could talk about something fun for once."
        b "Sure, any ideas?"
        o "Hmm... tell me about your hobbies? Since you know about mine."
        b "Well, recently I got into journaling."
        b "This is still kind of a dark topic though."
        o "Only talk about it if you want to!"
        b "Well, you opened up a ton to me, I can open up back to you."
        b "I got into it after my own... incident, as a way of therapy."
        b "It started out as a way to process emotions by turning them into words."
        b "But eventually it became a nice way to chronicle what happened during my day."
        b "It helps me keep track of my goals, I remember things people said to me more easily."
        b "Just overall helps me mentally feel like I'm part of the moment always."
        o "That's super cool!"
        o "And it seems like you also turned something born out of dark necessities into a positive hobby."
        o "So I guess that's one thing we have in common."
        scene black with fade
        bi "We talked for a bit about other hobbies we had."
        bi "I think I finally learned to talk to Lauren casually, we're much closer now."


    #Bert post-3
    if fte_laur >= 3:
        bi "I enjoyed some time with Lauren, now that we were able to speak casually."

    $fte_laur += 1
    hide lauren with dissolve
    jump postFTEHandler
