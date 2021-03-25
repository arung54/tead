#Arun

#Train 1
label laurAsk0:
    scene bg trainmid
    show lauren ind with dissolve
    o "You're not being mean to Sid at night, are you?"
    ni "I should go talk to Bert."
    call screen midCar

#Train 2
label laurAsk1:
    scene bg trainmid
    show lauren ind with dissolve
    o "What's up Dan, wanted to chat?"
    menu:
        "Spend time with Lauren?":
            o "Sure, not like anything else is happening."
            jump laurHang
        "Maybe later":
            hide lauren with dissolve
            call screen midCar

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
        o "Our family was well off, but they wanted to instill discipline in me."
        o "I like kids more than most high schoolers, so it was more like a hobby."
        o "Sometimes I even got lucky and found a gig wwere the kids just slept and I got paid do homework."
        n "Wait, back up, you like kids more than high schoolers?"
        o "Yeah. High schoolers think they know everything."
        o "But when you look at their sense of morality they really don't."
        o "Not to mention, they're really horny, moody, drug addicts."
        n "As opposed to kids, who are selfless intelligent creatures."
        n "{i}Never{/i} seen a kid be mean to another person."
        o "Yeah, kids aren't perfect either."
        o "And if they aren't, you can try to teach them."
        o "You know how many high school students have been pricks to me?"
        o "I know not one of them would have listened if I explained why."
        o "Some of them are pricks because they think it's funny."
        o "You think they'd all of a sudden realize their actions affect others?"
        o "I'm not saying every kid is perfect and every high school student sucks."
        o "But the kids that suck, I can teach them."
        o "The high schoolers that suck, nothing short of a kick in the ass from reality will make them learn."
        ni "I was beginning to think this was a sort spot I shouldn't have pressed on."
        n "That's understandable, though I don't think I could ever think like that."
        o "Didn't ask you to."
        n "Sorry, didn't mean to make you upset."
        n "Just wanted to get to know you better."
        o "Well, there's better ways to do that then to sass me in our first conversation."
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
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_laur == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_laur == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_laur >= 3:
        bi "I enjoyed some time with Lauren, if only because of his pirate speak."

    $fte_laur += 1
    $ftecounter += 1
    hide lauren with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
