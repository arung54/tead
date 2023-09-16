#Julian

#Train 1
label stelAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show stella happy with dissolve
    t "Hello."
    ni "I should go talk to Bert instead of her."
    hide stella with dissolve
    call screen midCar with dissolve

#Train 2
label stelAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show stella happy with dissolve
    t "Hello."
    ni "Should I talk to Stella?"
    menu:
        "Spend time with Stella":
            t "Sure, you're cute enough."
            call stelHang from _call_stelHang
        "Maybe later":
            hide stella ind with dissolve
    call screen midCar with dissolve

#Mansion 1
label stelAsk2:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 4)
    show stella drunk with dissolve
    t "*hic* Hey cutie, wanna chat?"
    bi "Should I talk to Stella?"
    menu:
        "Spend time with Stella":
            t "Yeah, come here handsome."
            call stelHang from _call_stelHang_1
        "Maybe later":
            hide stella with dissolve
    call screen kitchen with dissolve

#Mansion 2
label stelAsk3:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 1)
    show stella drunk with dissolve
    t "*Yawn*. Post-drinking naps are the best..."
    bi "Should I talk to Stella?"
    menu:
        "Spend time with Stella":
            t "Ooh, my day just got better!"
            call stelHang from _call_stelHang_2
        "Maybe later":
            hide stella with dissolve
    call screen dining with dissolve

#Mansion 3
label stelAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show stella drunk with dissolve
    t "Party? This is at best a tea time. I need to drink more."
    bi "Should I talk to Stella?"
    menu:
        "Spend time with Stella":
            t "*hic* You know what they say, drunk conversation is the best chaser!"
            call stelHang from _call_stelHang_3
        "Maybe later":
            hide stella with dissolve
    call screen dining with dissolve

label stelHang:
    if fte_stel >= 3:
        bi "Hm, on second thought, I've talked to Stella plenty... I should talk to someone else."
        hide stella with dissolve
        return

    #Dan FTE 1
    if fte_stel == -1:
        show stella ind
        t "Bonjour Dan."
        n "Uh, bonjar Stella."
        t "Bonj{i}ou{/i}r."
        n "Bonj{i}a{/i}r."
        t "Hmm, not quite."
        t "Regardless, I had a question for you."
        n "For me?"
        t "Yes. As you may know, I have a quite elite team of bodyguards."
        t "However, as you may also know, I have been kidnapped and taken... here."
        t "Clearly, I need a new team of bodyguards."
        n "So, what's the question?"
        show stella happy
        t "Well, you're pretty muscular and tough, yes?"
        t "Perhaps you'd make a nice addition to the team."
        $mood = "shock"
        n "You want {i}me{/i} to be one of your bodyguards?"
        ni "That's a pretty ironic request considering my history..."
        t "Well, of course you'd have to tryout like everyone else."
        n "Tryout?"
        t "Yes, of course!"
        t "A 2-acre portion of my Montpelier estate is dedicated to my team's training and recruiting."
        ni "Is this chick serious?"
        show stella ind
        t "This is, of course, all assuming we make it out of this situation alive."
        show stella happy
        t "If I die, there is nobody to guard, haha."
        n "Haha... yeah."
        ni "..."
        t "Hm, perhaps your tryouts can start early."
        n "What?"
        t "If there's any danger on this train, you can have the honor of protecting me."
        n "Umm..."
        t "Don't worry, I'll pay you back."
        ni "Did she just, wink at me?"
        t "Wonderful, thank you Dan."
        n "I don't think I agre-"
        t "What a productive meeting."
        $mood = "ind"
        t "Au revoir, Dan!"
        n "Au revwah, Stella?"
        t "Hm, close enough."
        hide screen status_screen
        scene black
        with fade
        n "..."
        ni "After a very confusing conversation with Stella, we returned to mingling with the others."

    if fte_stel == 0:
        show stella happy
        t "Bert, I'm glad you're here."
        b "...You are?"
        t "Yeah, I needed some eye candy."
        b "Um... not sure if I like being called eye candy."
        t "It's a compliment honey."
        b "Are you this... lascivious in your daily life?"
        t "Hm, more or less."
        t "When I'm not trapped in a game like this I get to enjoy my vices more."
        t "So in professional contexts I can restrain myself more easily."
        t "But when among friends... why not let loose?"
        b "Um... I don't know if I'd say we're that type of friend yet."
        show stella ind
        t "Not... yet?"
        show stella happy
        t "So there's a chance. Ooooooh I love a good chase!"
        b "No, that's not what I meant..."
        t "I must say Bert, if you're looking for a side gig..."
        t "I've gotten quite bored of the entertainment at my parties."
        t "I could use some... fresh meat."
        bi "How has this lady not been fired for sexual harassment?!"
        bi "...Probably because she's too rich to sue."
        b "...I think I'm good with my job, thanks."
        t "Aw boo."
        t "C'mon, I'll pay you enough to be worth it!"
        t "How much do you make? One million? Two million? I'll double that!"
        b "...Huh?"
        t "Ha, you hesitated!"
        t "That means you were considering it."
        b "No, I'm just shocked..."
        b "Do you think average people make a million dollars?"
        t "Oh, honey, average people don't make nearly that much, I know that."
        t "I just wanted to tempted you a bit."
        t "Which I did!"
        b "No, you didn't!"
        b "No means no!"
        show stella ind
        t "Hmph."
        t "Okay, you win this round."
        t "But there's one thing you should know about me Bert..."
        show stella bigsmile
        t "People like me always get their wishes."
        b "...Is that a threat?"
        show stella happy
        t "Huh? Oh no!"
        t "I'm just saying I'll win you over one way or another!"
        t "I just need to figure out how..."
        hide screen status_screen
        scene black
        with fade
        bi "Well, I guess I got closer to Stella..."
        bi "...Does this place have HR I can report to?"

    if fte_stel == 1:
        show stella happy
        t "Bert! My favorite little man!"
        b "...Little man?"
        b "What's got you so excited to see m-"
        b "Actually, no, I don't need to know."
        t "Nope, too late, you asked!"
        t "I figured out how we're going to become close friends!"
        b "Um... why do we need to become close friends?"
        t "Because you said we're not that type of friend yet!"
        t "So I'm gonna make us that type of friend!"
        b "Being friends is something you really \"make\" happen."
        show stella ind
        t "What do you mean?"
        b "You usually do it more organically..."
        b "Like, over time, with shared memories."
        t "Hmm, I don't have that kind of time."
        t "We're going to go the fast way!"
        b "Sigh..."
        b "Alright, I guess I feel bad saying no to someone trying to be friends."
        show stella happy
        t "Great!"
        t "Okay, let's do some icebreakers!"
        b "Icebreakers?"
        t "Yeah! That's how you befriend people in corporate land if you're not rich."
        b "...How do you befriend people if you're rich?"
        bi "...I regretted asking before hearing the answer."
        t "A loooooot of booze."
        t "And occasionally bribes."
        b "Okay, what ice breaker do you have."
        t "If a rich lady wanted to gift you like, a hundred million dollars, what would you spend it on?"
        b "...Why did the rich lady need to be a part of this question?"
        t "It's a hypothetical, don't worry about it too much."
        b "I mean... I guess I'd retire, go travel, treat my friends to nice food..."
        show stella ind
        t "Non-billionaires are so silly... Bert, the right answer is a yacht!"
        t "Bert, how are people going to know you're rich if you don't have a big yacht!"
        b "...Why would I want a yacht? I get seasick easily."
        t "It's not about riding it, it's the status."
        t "A nice house, or fancy car, or clothes, any millionaire can get those things."
        t "But a yacht... a yacht's not just a one-time purchase."
        t "It requires a ton of upkeep costs, hiring dedicated staff..."
        t "That's how you show off status symbols!"
        b "You know, ice berakers usually aren't supposed to have right answers..."
        t "Really? Hm..."
        t "Okay, let me think some more, I'll come back to you with another icebreaker then."
        hide screen status_screen
        scene black
        with fade
        bi "Well, I understand Stella a bit better now."
        bi "But I don't think she's any closer to understanding non-billionaires..."

    if fte_stel == 2:
        show stella happy
        t "Okay, Bert, I have another icebreaker. This one's good, it doesn't have a right answer."
        b "Okay, hit me."
        t "What's the best cognac you've ever had?"
        b "Um... Stella, I don't know if you understand ice breakers still."
        show stella ind
        t "What? But cognac's only like, six figures!"
        t "Surely that's more relatable..."
        b "Well, no, most people don't spend six figures on things like that."
        t "Ughhh, why can't you just take money to be my friend like everyone else..."
        bi "...I'm just going to ignore the sad implication of that question."
        b "More importantly... I don't know, this question doesn't reveal much about someone's personality."
        b "Like, if you asked what someone's hobbies were and they said drinking cognac."
        b "Then you'd have learned something about them."
        b "But you're just assuming I like cognac."
        b "Even \"do you drink cognac?\" would be a better question."
        b "Though a yes or no is still not great, it should be something more open-ended."
        t "Okay, I think I get it..."
        t "...But can you ask me an ice breaker so I uh, understand better?"
        bi "This might be the first time Stella seemed open to actually listening..."
        b "Sure, like... uh..."
        bi "...Hm, asking a billionaire an ice breaker is kind of hard."
        bi "Something billionaires do that the rest of us do... Oh!"
        b "Where's your favorite place you travelled?"
        show stella happy
        t "Ooh, Barcelona!"
        b "What did you like about Barcelona?"
        t "Well, they have the best parties of anywhere I've been to."
        t "And they take siestas... very important for when you're partying."
        t "Even a hard-working business woman needs a nap to recover."
        t "Ooh, and I love paella, and the best paella I've had is in Barcelona."
        b "See! I learned something about your personality."
        b "Well, I already knew you were a party girl, but..."
        b "I learned that you enjoy good food when travelling."
        t "Well, duh, doesn't everyone?"
        b "I mean, I do, but I've seen long lines at Cheesecake Factory in Hawaii..."
        t "Yuck! People actually eat there!"
        t "Okay, so are we close friends now?"
        b "Well, no, again, we need to work at it over time..."
        show stella ind
        t "Hmph. What was the point then?!"
        b "...But this is at least on the right path."
        t "..."
        show stella happy
        t "Okay, I'll take that."
        t "I told you I'd win you over Bert!"
        hide screen status_screen
        scene black
        with fade
        bi "Stella and I had a back-and-forth where we didn't talk about money and partying."
        bi "It was nice to actually get to know her a bit."

    #Bert post-3
    #if fte_stel >= 3:
        #bi "I enjoyed some time with sam, if only because of his pirate speak."

    $fte_stel += 1
    $persistent.fte_stel = max(persistent.fte_stel, fte_stel)
    if persistent.fte_stel >= 3:
        $achievement.grant('stel_fte')
        $achievement.sync()
    hide stella
    jump postFTEHandler
