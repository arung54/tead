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
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen midCar with dissolve

#Mansion 1
label jennAsk2:
    scene bg mansionhall
    $ statusnt("Hallway", "bert", ch = 2, sun = 4)
    show jenny happy with dissolve
    j "Bert! The bedrooms here are so spacious!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Sure, let's chat!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen hallway with dissolve

#Mansion 2
label jennAsk3:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 1)
    show jenny happy with dissolve
    j "Bert! Turns out having a fancy kitchen makes cooking super easy!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Sure, I'd love some company!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen kitchen with dissolve

#Mansion 3
label jennAsk4:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 2)
    show jenny happy with dissolve
    j "Bert! Thanks for being so patient while we finish up!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Okay, but we gotta finish talking before the first course is ready!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen kitchen with dissolve

#Hospital 1
label jennAsk5:
    scene bg hospkitchen
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show jenny happy with dissolve
    j "Oh hey Bert, I don't need help with cleaning, but we can talk!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Normally I sing while doing dishes, but talking is nice too!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen hospKitchen with dissolve

#Hospital 2
label jennAsk6:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show jenny happy with dissolve
    j "I eat a lot of salad at home, so this meal might be kind of nice!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Sure!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen patientcommons with dissolve

#Hospital 3
label jennAsk7:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show jenny happy with dissolve
    j "That was a nice conversation... I feel like we're a team now!"
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Yeah! More friendship!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen patientcommons with dissolve

#Bank 1
label jennAsk8:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 1)
    show jenny ind with dissolve
    j "Phew, I'm tired."
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Well, I guess I still have energy to talk!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen lobby with dissolve
#Bank 2
label jennAsk9:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 1)
    show jenny ind with dissolve
    j "It's weird playing with Freddy knowing who his dad is..."
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Okay, but gotta keep an eye on Freddy!"
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen lobby with dissolve

#Bank 3
label jennAsk10:
    scene bg bankvault
    $ statusnt("Bank Hallway", "bert", ch = 4, sun = 2)
    show jenny ind with dissolve
    j "*Pant*... for a kid, Freddy has a lot of energy."
    bi "Should I talk to Jenny?"
    menu:
        "Spend time with Jenny":
            j "Yeah, I need to catch my breath anyway..."
            call jennHang
        "Maybe later":
            hide jenny with dissolve
    call screen hall with dissolve

label showJennyIndFTE:
    if ftecounter == 5:
        show jenny ind at inwindow behind hospwindowoverlay
    else:
        show jenny ind
    return

label showJennyHappyFTE:
    if ftecounter == 5:
        show jenny happy at inwindow behind hospwindowoverlay
    else:
        show jenny happy
    return

label jennHang:
    if fte_jenn >= 3:
        b "Hm, on second thought, I've talked to Jenny plenty... I should talk to someone else."
        hide jenny with dissolve
        return
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
        call showJennyHappyFTE
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

    if fte_jenn == 1:
        call showJennyHappyFTE
        j "Hey Bert! I feel like I talk about myself a lot when we hang out..."
        j "I want to ask you something instead!"
        b "Oh. Sure, go for it!"
        j "What's your favorite paradox?"
        b "Huh?"
        j "You know, like, a self-contradicting idea."
        b "Oh, I know what a paradox is, just... I don't know, I don't have a favorite paradox ready."
        b "Hm... I guess I like the grandfather paradox."
        j "Oh, that's a classic."
        j "Though it's not really a paradox, if you believe in parallel universes."
        b "Huh?"
        j "Well the contradiction is that you can't kill your grandfather and be born later."
        j "But if you killed him in a different universe, then there'd be no contradiction."
        b "Oh... I guess that's true."
        call showJennyIndFTE
        j "Hm... there's a lot of killing in this paradox."
        j "Kind of suspicious to ask..."
        b "What? No, it's just one of the most famous ones!"
        call showJennyHappyFTE
        j "Just kidding Bert! I don't think you're suspicious."
        j "If anything you're one of the most trustworthy guys here!"
        b "Oh... it was a joke."
        j "Anyway, ask me about my favorite paradox!"
        b "Um... okay, what's your favorite paradox?"
        j "It's kind of a boring answer, but the Banach-Tarski paradox is so cool!"
        b "Oh... yeah, that one is cool, haha."
        call showJennyIndFTE
        j "...You don't know what it is, do you?"
        b "No, that wasn't a very convincing lie, was it."
        j "Not really, no."
        call showJennyHappyFTE
        j "It's okay Bert! Most people probably don't know about it."
        b "But... you said it's a boring answer."
        b "I assume it must be pretty well-known."
        j "Oh, it's popular in math circles, but I don't think the average person knows it."
        j "And even the people who know about it probably don't fully understand it."
        j "They just know it as \"you can disassemble a ball into five parts, and make two balls out of them\"."
        b "So... it's about generating matter from thin air?"
        j "Kind of? It only works in theory."
        j "Like, I can tell you how to do it, but you'd have to be able to make infinitely small cuts to the balls."
        j "It would be cool if it worked in real life, but obviously it can't."
        bi "I could feel my eyes glazing over..."
        j "Ah, it's so refreshing to be able to talk about this stuff."
        call showJennyIndFTE
        j "I miss this from the outside, having stimulating conversations with my peers."
        bi "I wouldn't say I'm her peer, seems like she's way more knowledgeable here than I am..."
        j "Ooh, but you've at least heard of Hilbert's hotel, right?"
        b "Gabbo Hotel?"
        j "No, Hilbert's!"
        scene black with fade
        bi "Jenny gave me what was basically a lecture about infinity and paradoxes..."
        bi "I didn't understand much, but I could tell it let her escape this place for a bit, so I was happy to listen."

    if fte_jenn == 2:
        call showJennyHappyFTE
        j "Bert!"
        j "I wanted to tell you something."
        j "It's not about math this time, I swear!"
        b "Oh... yeah, I mean, always happy to talk."
        j "I just wanted to say... thanks for letting me talk to you about math and poker and stuff."
        call showJennyIndFTE
        j "Even at college, it's rare that I get to talk about this stuff."
        j "I have a bit of a... difficult home life situation."
        j "Most of my free time goes towards trying to help my parents out with whatever I can."
        j "So even though I'm lucky enough to get to go to college..."
        j "Well, I don't get to hang out with people on campus much."
        j "Much less people on campus who are willing to talk about math instead of other things."
        j "And then, well, a lot of the people who were willing to listen to me were guys, who, well..."
        j "Were more interested in hitting on me than listening to me."
        call showJennyHappyFTE
        j "So even though you pretended you knew what the Banach-Tarski paradox was..."
        j "The fact that you wanted me to feel like I wasn't boring you was really nice!"
        b "I mean... I don't feel like I really did much besides show you human decency."
        j "Well, maybe you didn't."
        j "But, even if that's all you did, it's something I don't get a lot of in my normal life."
        j "So thanks Bert."
        b "No need to thank me, haha..."
        call showJennyIndFTE
        j "..."
        b "..."
        j "So, um..."
        j "Do you happen to know anything about stochastic calculus, Bert?"
        b "I don't, but I'm sure you can teach me a lot about it."
        j "Okay, so imagine a guy taking a walk on a line, but he randomly decides which way to walk every minute..."
        scene black with fade
        bi "Jenny gave me a... well, lecture about random walks and something called Brownian motion."
        bi "I didn't understand most of it, but that wasn't important."
        bi "What was important was Jenny getting a break from this game, but also from the troubles of her normal life."

    #Bert post-3
    #if fte_jenn >= 3:
        #bi "I enjoyed some time with Jenny, if only because of his pirate speak."

    $fte_jenn += 1
    $ persistent.fte_jenn = max(persistent.fte_jenn, fte_jenn)
    hide jenny with dissolve
    jump postFTEHandler
