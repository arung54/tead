#Arun

#Train 1
label jennAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show jenny happy with dissolve
    j "Hey Dan!"
    ni "I should go talk to Bert."
    hide jenny with dissolve
    call screen midCar with dissolve

#Train 2
label jennAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show jenny happy with dissolve
    j "Hey Dan!"
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar with dissolve

#Mansion 1
label jennAsk2:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 2
label jennAsk3:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Mansion 3
label jennAsk4:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 1
label jennAsk5:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 2
label jennAsk6:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Hospital 3
label jennAsk7:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 1
label jennAsk8:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar
#Bank 2
label jennAsk9:
    menu:
        "Spend time with Jenny":
            j "Sure!"
            jump jennHang
        "Maybe later":
            hide jenny with dissolve
            call screen midCar

#Bank 3
label jennAsk10:
    menu:
        "Spend time with Jenny":
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
        j "I think the answer's between 4 and 5, but I'm not sure."
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
        j "Anyway, we don't have to talk about math. But maybe I can pick your brain on something I'm wondering about..."
        show jenny ind
        j "What happens if there are four of us left and the murderer doesn't kill the Game Master?"
        n "What do you mean? Wouldn't there just be an investigation and vote?"
        j "Well, think about who'd remain after the murder."
        j "You'd have the murderer themselves, the Game Master, and a third person."
        j "The Game Master can pretty much just decide the vote on their own, since they can just vote w/ either person."
        j "The Game Master survives regardless of what happens, so there isn't really an incentive for them to vote either way."
        n "Well, after the vote it's just the Game Master and one person."
        n "I don't imagine they brought us all here with the intent of having us survive."
        n "So I'd imagine they'd just kill both people."
        j "Hmm, maybe, but if they wanted to kill us all, why not just do it directly?"
        j "At any time we were all passed out, they could've easily done it."
        j "Seems like a lot of effort to set up this game that requires all these additional resources."
        n "I've been thinking about this a bit... maybe this game is meant to be torture."
        j "Oh?"
        n "Fates worse than death... a game where {i}innocent{/i} people have to kill each other might one of them."
        ni "...did I pull off that lie convincingly enough?"
        j "But then why would they put their lives on the line?"
        ni "Seems like I did."
        n "Maybe they lied, maybe there isn't a Game Master in this group at all."
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
        ni "For someone who likes math, she's pretty ditzy..."
        ni "But she seems like a useful person to have around, at least."


    #Bert FTE 1
    if fte_jenn == 0:
        j "Bert! How are you doing?"
        b "Um... I mean, I guess as good as I can be doing in a situation like this."
        j "Ha! Good one."
        b "...Thanks?"
        bi "She's so upbeat about... well, nothing really."
        b "You seem like you're in a good mood."
        j "Yeah! One upside about being here is I have a lot of time to just think."
        j "And I've been playing a lot of mental poker and learning a lot."
        b "Mental poker?"
        j "Oh, yeah, I forget if I've told you but I'm really into poker!"
        bi "She has, but, she seems like the type whose brain moves too fast to remember these things."
        j "So mental poker is basically playing poker hands in your head."
        j "Kind of like how chess grandmasters can play chess without a board!"
        b "But... they still need somebody to play with, right?"
        b "Like, if you play poker with yourself, there's no bluffing or anything."
        b "Not to mention, with chess there's no luck or hidden information."
        b "But with mental poker, you can't randomize the hands or make sure you're not lying."
        b "I'd just say I have two aces everytime and you couldn't disprove me..."
        j "Well, I'm not playing with anyone, so I don't need two people!"
        j "And since I'm not playing with anyone there's no need to make sure I'm not lying."
        b "But... where's the sport in playing with yourself?"
        j "Well, saying I'm playing mental poker is probably a bit misleading."
        j "I'm basically just coming up with example hands, and trying to work out a play."
        j "Like, for example, if I'm big blind with a pair of twos and three people fold, two people check..."
        j "Should I raise?"
        j "Then I can try to work out how likely raising is to lead to a favorable situation."
        b "But... how do you know what your, er, opponents have?"
        j "Well, if no one raised I can make a reasonable guess what their hands are."
        j "For example, I'd always raise pre-flop with pocket aces."
        j "But given one person didn't fold who wasn't the small blind at a table of six..."
        j "They must have a reasonably strong hand. At least adjacent or suited cards."
        b "Uh..."
        bi "I realize I don't know as much poker as I thought I did."
        b "...Wouldn't it be easier to like, make a deck of cards out of something?"
        j "...Make a deck of cards?"
        b "I don't know, I imagine if we had a pen and paper you could just tear the paper up."
        b "And then write the names of the cards on all the pieces."
        b "And then some of us could play hands with you. It'd be a good way to kill the time."
        j "Eh... no offense Bert, but I don't know if playing with the people here would be good practice."
        j "Not to mention, if we didn't tear the paper perfectly, I might just memorize the shapes."
        b "The shapes?"
        j "Like, the shapes of the torn paper."
        j "It's not like we'll make perfect rectangles."
        b "..."
        j "But, pen and paper would make it easier to write down what I've figured out."
        j "That's a good idea Bert! I should go look for some."
        j "Seeya!"
        scene black with fade
        bi "I wouldn't have guessed it when I met her, but..."
        bi "Turns out Jenny's a huge nerd. Probably ten times smarter than I am."
        bi "Does that mean she'll be a useful ally? Or someone to look out for? Hm..."


    #Bert FTE 2
    #if fte_jenn == 1:
        #h "Mate! Back for more tales of the sea?"

    #Bert FTE 3
    #if fte_jenn == 2:
        #h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    #if fte_jenn >= 3:
        #bi "I enjoyed some time with Jenny, if only because of his pirate speak."

    $fte_jenn += 1
    hide jenny with dissolve
    jump postFTEHandler
