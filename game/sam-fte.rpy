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
    menu:
        "Spend time with Sam?":
            s "Sure, I guess I can talk."
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen frontCar with dissolve

#Mansion 1
label samAsk2:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Mansion 2
label samAsk3:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Mansion 3
label samAsk4:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 1
label samAsk5:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 2
label samAsk6:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Hospital 3
label samAsk7:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Bank 1
label samAsk8:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar
#Bank 2
label samAsk9:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

#Bank 3
label samAsk10:
    menu:
        "Spend time with Sam?":
            j "Sure!"
            jump samHang
        "Maybe later":
            hide sam with dissolve
            call screen midCar

label samHang:
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

            "WHAT?! You gotta be kitten me!":
                n "...How's that?"
                s "Hmm, you'll get there."

            "Wow! You said you were a frog, but you've been lion the whole time!":
                n "...How's that?"
                s "Hmm, not bad."
        scene black with fade
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
       scene black with fade
       bi "We chatted a bit more about career ambitions."
       bi "It's nice to learn a bit about what motivates Sam."

    if fte_sam == 1:
        s "Hey Bert, what kind of fun classes did you take in college?"
        s "Like, classes you took to fill requirements rather than your major?"
        b "Hm... I took a digital writing class that was interesting."
        s "Digital writing?"
        b "It was a writing class where the assignments were are in digital formats."
        b "Like for one we had to make a tweet thread about a t


    #Bert FTE 3
    #if fte_sam == 2:
    #    h "Back again lad? You must love hearing tales of the sea."

    #Bert post-3
    #if fte_sam >= 3:
    #    bi "I enjoyed some time with sam, if only because of his pirate speak."

    $fte_sam += 1
    hide sam with dissolve
    jump postFTEHandler
