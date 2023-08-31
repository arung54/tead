#Julian

#Train 1
label samAsk0:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show sam ind with dissolve
    s "Hey."
    ni "I should go talk to Bert instead."
    hide sam with dissolve
    call screen frontCar with dissolve

#Train 2
label samAsk1:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show sam ind with dissolve
    s "Hey."
    ni "Should I time with Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, I guess I can talk."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen frontCar with dissolve

#Mansion 1
label samAsk2:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 4)
    show sam ind with dissolve
    s "A party would be nice, even if it's not like college parties."
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen masterBedroom with dissolve

#Mansion 2
label samAsk3:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 1)
    show sam ind with dissolve
    s "Hm, there's not a lot as far as baking supplies go..."
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, let's talk while I look around more."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen kitchen with dissolve

#Mansion 3
label samAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show sam ind with dissolve
    s "Hey Bert."
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, but not for too long."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen dining with dissolve

#Hospital 1
label samAsk5:
    scene bg hospkitchenwindow at bg
    show hospwindowoverlay
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show sam ind at inwindow behind hospwindowoverlay
    s "..."
    bi "Sam's probably not in the mood to talk right now..."
    bi "I should ask someone else."
    hide sam with dissolve
    call screen hospKitchen with dissolve

#Hospital 2
label samAsk6:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show sam ind with dissolve
    s "..."
    bi "Sam's probably not in the mood to talk right now..."
    bi "I should ask someone else."
    hide sam with dissolve
    call screen patientcommons with dissolve

#Hospital 3
label samAsk7:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 2)
    show sam ind with dissolve
    s "...Hey Bert..."
    bi "Sam's doing better, but still probably not in the mood to talk right now..."
    bi "I should ask someone else."
    hide sam with dissolve
    call screen patientcommons with dissolve

#Bank 1
label samAsk8:
    scene bg banklocker
    $ statusnt("Locker Room", "bert", ch = 4, sun = 2)
    show sam ind with dissolve
    s "Oh Bert. I was about to take a shower."
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, I can wait a bit."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen locker with dissolve
#Bank 2
label samAsk9:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 1)
    show sam ind with dissolve
    s "JO... never thought I'd hear that name here."
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, I need a distraction from this revelation..."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen lobby with dissolve

#Bank 3
label samAsk10:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 2)
    show sam ind with dissolve
    s "Freddy is JO's son... does he know what his dad does?"
    bi "Should I talk to Sam?"
    menu:
        "Spend time with Sam":
            s "Sure, though I might be distracted by what we just learned."
            call samHang
        "Maybe later":
            hide sam with dissolve
    call screen lobby with dissolve

label samHang:
    if fte_sam >= 3:
        bi "Hm, on second thought, I've talked to Sam plenty... I should talk to someone else."
        hide sam with dissolve
        return
    #Dan FTE 1
    if fte_sam == -1:
        s "Really?"
        n "What?"
        s "You could have bothered anyone on this train, and you chose me?"
        s "Spare me."
        n "It can't hurt for us to try to get along."
        s "Hm, sounds kinda like it would hurt."
        n "You've got a good sense of humor, ya know."
        s "I'm wasn't really making a joke, I just speak my mind."
        s "No point in beating around the bush, especially in a situation like this."
        ni "Sam's so difficult to open up..."
        n "Though I'm worried you've ostracized some of the others on board."
        s "As if you haven't?"
        n "Well, yeah, but..."
        n "I think that's less by choice. I'm just... not great at conversations."
        n "It's been a while since I've gotten to talk to someone like this."
        s "I can tell, you're super awkward dude."
        ni "..."
        s "Maybe you need a shtick."
        n "A shtick?"
        s "Yeah, like, pretending to have magic, two personalities, or being a robot."
        n "Uhhh, those seem pretty strange."
        s "Well it doesn't have to be extreme, you could try just being funny or something."
        s "Maybe you could be the \"Joke Guy.\""
        n "The \"Joke Guy?\""
        s "Like, picture this: you open the bar car mini-fridge and find a severed arm!"
        s "Perfect time for the Joke Guy to say, \"Someone come give me a hand with this!\""
        ni "..."
        s "I mean, that exact scenario seems unlikely, but you get the idea."
        n "Uh, I'd hope it's unlikely..."
        s "I'm trying to help you here, loner."
        s "Let's try it."
        s "What's your line if Freddy takes off his hoodie and he's been a baby lion this whole time?"
        n "Uhhh...."
        show scary with dissolve:
            alpha .5
        menu:
            n "{i}What's Joke Guy's line?{/i}"

            "A kitten pun.":
                hide scary with dissolve
                n "WHAT?! You gotta be kitten me!"
                n "...How's that?"
                s "Hmm, you'll get there."

            "A lion pun.":
                hide scary with dissolve
                n "Wow! You said you were a frog, but you've been lion the whole time!"
                n "...How's that?"
                s "Hmm, not bad."
        hide screen status_screen
        scene black
        with fade
        ni "After a surprisingly pleasant conversation with Sam, we both went separate ways."


    if fte_sam == 0:
       s "Bert, you went to college, right?"
       b "Oh, yeah."
       b "You're in college right now, right?"
       s "Did you ever miss class for weeks on end?"
       b "Hm... no, I missed a few days from being sick, but nothing like this."
       b "This is also the first time I'm going to gone from work this long..."
       b "Even vacations aren't much longer than a week."
       s "If we get out of here, it's going to be tough to explain to people..."
       s "\"Hey Professor, sorry for missing weeks of your class, I was busy playing a death game.\""
       s "\"Can I get a C on all the assignments I missed?\""
       b "Yeah, don't think that would fly..."
       s "Oh shit, I'm going to miss my rent payment..."
       b "Jeez, yeah, there's that..."
       b "My parents are going to wonder why I'm not returning their calls."
       b "I guess I've been so focused on trying to escape..."
       b "I haven't thought about what we'll do after we get out of here."
       s "Well, it makes sense..."
       s "There's already enough to be stressed out about in here."
       s "Thinking about the outside world might just stress us further."
       s "Hell, my normal life is stressful even without a death game."
       b "Classes?"
       s "Eh, classes are fine, can kinda bullshit your way through them."
       s "Was thinking more, you know, the drug dealing."
       b "...Oh, right."
       s "It's funny classes were the first thing you thought of."
       s "You live a pretty sheltered life, don't you Bert?"
       b "I mean... I guess you could call it that."
       bi "I'd like to think it's more structured than sheltered."
       s "I mean, good for you."
       s "I don't think anyone wants to live an unsheltered life."
       s "If I didn't need the money from drug dealing I definitely wouldn't do it."
       b "Oh um, what do you need the money for?"
       s "Mostly college tuition."
       s "I'm hoping to get into politics after graduating, and well..."
       s "Most politicians aren't exactly poor."
       s "At the local level, most politicians aren't that well paid."
       s "So most local politicians are people who have wealth accumulated."
       s "If I graduate with debt..."
       s "I'm starting off on the wrong foot."
       b "That's interesting..."
       b "Most people would want to graduate without debt for their own benefit."
       b "But you're doing it to get an edge career-wise?"
       b "That's a pretty forward-thinking mentality."
       s "I mean, that's just politics."
       s "One of the few fields where your prior income matters a lot."
       b "Still, it's admirable, even if some might disagree with how you're earning money..."
       hide screen status_screen
       scene black
       with fade
       bi "We chatted a bit more about career ambitions."
       bi "It's nice to learn a bit about what motivates Sam."

    if fte_sam == 1:
        s "Hey Bert, what kind of fun classes did you take in college?"
        s "Like, classes you took to fill requirements rather than your major?"
        b "Hm... I took a digital writing class that was interesting."
        s "Digital writing?"
        b "It was a writing class where the assignments were are in digital formats."
        b "Like for one we had to make a tweet thread about a topic."
        b "For my final project I made a storytelling game using this software called PenRy."
        s "Hm, that's a lot more interesting than the electives I took..."
        b "I got lucky, the class filled up almost instantly."
        s "That's way better than the writing class I took."
        s "I took a creative writing class thinking it'd be good for self-expression."
        s "But I got an instructor who was super rigorous and it felt more like a boot camp."
        s "I thought it would be a chill experience but it made writing feel like a chore."
        b "Oof, that sucks."
        s "Yeah, I dropped it on the last day possible."
        s "It was kind of a good learning experience."
        s "I think coming into college I thought it was about finding your passions and such..."
        s "But I realized that a lot of ways to \"explore your passions\" were really just tedious coursework."
        s "And that, well, taking thirty something classes instead of the ten or so I really needed..."
        s "They say it's so the school can be accredited, but..."
        s "It's awfully convenient that I'm paying more money to take those classes, that's all I'm saying."
        b "Hm..."
        bi "Honestly, I thought what Sam was saying was a bit too cynical..."
        bi "But I could see the point they were making."
        b "I guess that's true, I wouldn't have minded starting work a year or two earlier."
        b "Would have started making money sooner, would have less tuition to pay."
        s "Yeah, that's what I realized..."
        s "If I just took goof-off classes instead of classes where I was \"exploring my passions\"..."
        s "I could use the extra time to take more classes and graduate sooner."
        s "Or just work more on the side."
        s "So... that's what I ended up doing."
        b "And you're on track to graduate early?"
        s "Yeah, only by one semester but still."
        s "Going from paying five figures in tuition to earning any amount of money is a huge swing."
        s "Plus, I can finally get out of the drug dealing job..."
        b "Finally?"
        s "Yeah, uh, I started dealing harder drugs because it made more money..."
        s "But, well, it's a matter of higher risk for higher reward."
        s "I thought I was ready for the jump up, but eh, there have been a few close calls."
        s "Not to mention some deals I've been uncomfortable with making..."
        s "Clients I feel bad for, drugs I wasn't comfortable selling."
        b "Is it that easy to leave?"
        s "I mean, it's not like I'm leaving to snitch on them."
        s "I'll just tell them I'm moving home because I'm done with school."
        s "Plus, they know I'm a student trying to pay off tuition."
        b "I guess that makes sense..."
        b "Well, hopefully this whole death game thing doesn't get in the way of your graduating."
        s "Ha, hope so too..."
        hide screen status_screen
        scene black
        with fade
        bi "We chatted a bit more about college."
        bi "I don't see eye-to-eye with Sam about everything, but I at least understand them better."

    if fte_sam == 2:
       b "Sam, I was wondering..."
       b "What motivated you to get into politics?"
       s "Oh, um..."
       s "Politics is a bit of a touchy subject, don't you think?"
       s "Not really trying to make political enemies with anyone in a death game."
       b "Oh."
       b "Um... can't we do a no-judgment-zone kind of deal?"
       s "Just because you say you're not judging me, doesn't mean it's true."
       s "Plus, judging someone isn't really something you choose to do."
       s "It's a gut reaction, a lot of the time."
       s "Even if you say you won't judge me, internally I'm sure you will."
       b "Yeah, but externally is all that matters, right?"
       b "I have all sorts of random thoughts that I don't act on or make known."
       b "Like, I think about what would happen if I didn't move my finger while cutting veggies."
       b "But I never actually do it."
       s "Hmph... fine."
       s "I want to push for reform for laws surrounding drug use."
       s "Obviously I'm biased since, well, I could get arrested under those laws."
       s "But... I don't know, so many rich people use drugs."
       s "Trust me, I've had some clients that present as well-composed men in suits..."
       s "But they have some nasty habits no one knows about."
       s "And yet none of them will ever get caught or arrested for it."
       s "Hell, some famous people make careers out of it."
       s "There's at least one famous comedian who does hard drugs and isn't arrested for possession."
       s "But in a ton of his shows, he'll mention his habit."
       s "The sob story makes him money."
       s "And rich people can afford to go to rehab in the worst case."
       s "But people who aren't rich..."
       s "Well, it's a lot easier for them to spiral as is, even without the law."
       s "And then the law treats them as criminals rather than victims a lot of the time."
       s "So... I don't know, I just think we could use some more empathy."
       b "...Wow."
       b "I've uh, never really thought about it before."
       s "I mean, most of the rich people who do drugs keep it hidden."
       s "So it's easy to think that everyone with a drug addiction is a degenerate on the streets."
       b "Um... won't your being a drug dealer hurt your political career?"
       s "Yeah, I've thought about it..."
       s "But, well, if I get caught for drug dealing I'll probably get arrested anyway."
       s "Especially if they find out about the harder drugs..."
       s "So... I don't know, I guess I've already committed to having that in my past."
       s "Not much I can do about it now."
       b "I see..."
       b "Well, I'm sure you've put a lot more thought into this than I have, so..."
       b "I guess all I can do is wish you good luck."
       s "Thanks Bert."
       s "And uh... don't mention this to anyone else."
       s "I trust you not to treat me too differently, but the others..."
       b "Yeah, of course."
       hide screen status_screen
       scene black
       with fade
       bi "With the heavy tone of the conversation, we couldn't find much else to talk about."
       bi "Sam and I have very different outlooks on life, I've learned."
       bi "But that's not necessarily a bad thing."

    $fte_sam += 1
    $persistent.fte_sam = max(persistent.fte_sam, fte_sam)
    hide sam with dissolve
    jump postFTEHandler
