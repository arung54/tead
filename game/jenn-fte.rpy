#Arun

#Train 1
label jennAsk0:
    scene bg trainmid
    show jenny happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert."
    call screen midCar

#Train 2
label jennAsk1:
    scene bg trainmid
    show jenny happy with dissolve
    j "Hey Dan!"
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 1
label jennAsk2:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 2
label jennAsk3:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 3
label jennAsk4:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 1
label jennAsk5:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 2
label jennAsk6:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 3
label jennAsk7:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 1
label jennAsk8:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar
#Bank 2
label jennAsk9:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 3
label jennAsk10:
    menu:
        "Spend time with Jenny?":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

label jennHang:
    #Dan FTE 1
    if fte_jenn == -1:
        j "Hey Dan! What's up?"
        n "Not much, just figured it'd be good to talk to people while we're waiting around."
        j "In that case, you want to check my work on a math problem?"
        n "Uh... I'm not very good at math, but I'm down to listen."
        j "I'm just wondering, if we can identify the murderer every time and the murderer chooses a random victim..."
        j "How many of us escape on average?"
        n "That's... a rather dark math problem."
        show jenny ind
        j "Well, I haven't really been able to stop thinking about our situation."
        j "But that was kind of stressing me out for obvious reasons."
        j "So I decided to turn it into something at least a little bit relaxing."
        n "...you think math is relaxing?"
        show jenny happy
        j "Yeah! Probability problems are basically just like figuring out games."
        j "And I love playing games."
        j "Also, I think giving myself reasonable expectations about our odds of surviving will make it easier in the long run."
        j "Haha, expectations, no pun intended."
        n "Oh yeah, good one."
        ni "I don't get it."
        j "Anyway, we don't have to talk about math. But maybe I can poke your brain for something I'm wondering."
        show jenny ind
        j "What happens if there are four of us left and the murderer doesn't kill the mastermind?"
        n "What do you mean? Wouldn't there just be an investigation and vote?"
        j "Well, think about who'd remain after the murder."
        j "You'd have the murderer themselves, the mastermind, and a third person."
        j "The mastermind can pretty much just decide the vote on their own, since they can just vote w/ either person."
        j "The mastermind survives regardless of what happens, so there isn't really an incentive for them to vote either way."
        n "Well, after the vote it's just the mastermind and one person."
        n "I don't imagine they brought us all here with the intent of having us survive."
        n "So I'd imagine they'd just kill both people."
        j "Hmm, maybe, but if they wanted to kill us all, why not just do it directly?"
        j "At any time we were all passed out, they could've easily done it."
        j "Seems like a lot of effort to set up this game that requires all these additional resources."
        n "I've been thinking about this a bit... maybe this game is meant to be torture."
        j "Oh?"
        n "Fates worse than death... a game where innocent people have to kill each other might one of them."
        ni "...did I pull off that lie convincingly enough?"
        j "But then why would they put their lives on the line?"
        ni "Seems like I did."
        n "Maybe they lied, maybe there isn't a mastermind in this group at all."
        n "They just want us to believe there is."
        j "Hm... as part of the torture? Giving us false hope?"
        n "Something like that."
        j "Interesting..."
        show jenny happy
        j "Thanks Dan! I think this was a productive conversation."
        n "So uh... did you ever solve that math problem?"
        j "What? Oh no, I started working on it, but then I thought about fashion for a bit, then it was time to eat."
        n "..."
        scene black with fade
        ni "For someone who claims to like math she's pretty ditzy..."
        ni "But she seems like a useful person to have around, at least."




    #Bert FTE 1
    if fte_jenn == 0:
        h "Ahoy laddy! What can I do fer ye?"

    #Bert FTE 2
    if fte_jenn == 1:
        h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    if fte_jenn == 2:
        h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    if fte_jenn >= 3:
        bi "I enjoyed some time with Jenny, if only because of his pirate speak."

    $fte_jenn += 1
    $ftecounter += 1
    hide jenny with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after Train FT2
