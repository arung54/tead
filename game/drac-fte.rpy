#Arun

#Train 1
label dracAsk0:
    scene bg trainback
    $ statusnt("Caboose", "dan", ch = 1, sun = 1)
    show drac happy with dissolve
    d "I wish it were slightly less bright in this train..."
    ni "I should go talk to Bert instead of this guy."
    hide drac with dissolve
    call screen backCar with dissolve

#Train 2
label dracAsk1:
    scene bg trainback
    $ statusnt("Caboose", "dan", ch = 1, sun = 1)
    show drac happy with dissolve
    d "Hello Dan, would you like to speak?"
    ni "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Very well. Not as if I have other plans."
            call dracHang from _call_dracHang
        "Maybe later":
            hide drac with dissolve
    call screen backCar with dissolve

#Mansion 1
label dracAsk2:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 4)
    show drac ind with dissolve
    d "This bedroom is nice, but I prefer the coffin in my estate."
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Well, I suppose I could use some stimulation."
            call dracHang from _call_dracHang_1
        "Maybe later":
            hide drac with dissolve
    call screen masterBedroom

#Mansion 2
label dracAsk3:
    scene bg mansionmasterbedroom
    $ statusnt("Master Bedroom", "bert", ch = 2, sun = 1)
    show drac ind with dissolve
    d "Shouldn't a mansion have slaves? Preferably ones with good blood."
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "I suppose conversation instead of blood will have to do."
            call dracHang from _call_dracHang_2
        "Maybe later":
            hide drac with dissolve
    call screen masterBedroom

#Mansion 3
label dracAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show drac ind with dissolve
    d "Given the circumstances, this is a good dinner party, but it's lacking Baroque music..."
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Even a string quartet would be a huge improvement."
            call dracHang from _call_dracHang_3
        "Maybe later":
            hide drac with dissolve
    call screen dining

#Hospital 1
label dracAsk5:
    scene bg hospkitchenwindow at bg
    show hospwindowoverlay
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show drac ind at inwindow behind hospwindowoverlay
    d "Bert, how do you survive eating food like what you cooked?"
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Sure, we can talk, anything besides eating more of that soup."
            call dracHang from _call_dracHang_4
        "Maybe later":
            hide drac with dissolve
    call screen hospKitchen

#Hospital 2
label dracAsk6:
    scene bg hospkitchenwindow2 at bg
    show hospwindowoverlay2
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show drac ind at inwindow behind hospwindowoverlay2
    d "Bert, after smelling Sid's cooking, I forgive you for yesterday's meal."
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Sure, I've finished investigating this side anyway."
            call dracHang from _call_dracHang_5
        "Maybe later":
            hide drac with dissolve
    call screen patientcommons

#Hospital 3
label dracAsk7:
    scene bg hospkitchenwindow2 at bg
    show hospwindowoverlay2
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 2)
    show drac ind at inwindow behind hospwindowoverlay
    d "That salad was good but unsatisfying... I crave flesh."
    bi "Should I talk to Dracula?"
    menu:
        "Spend time with Dracula":
            d "Are you volunteering your flesh, Bert?"
            call dracHang from _call_dracHang_6
        "Maybe later":
            hide drac with dissolve
    call screen patientcommons

label dracHang:
    if fte_drac >= 3:
        bi "Hm, on second thought, I've talked to Dracula plenty... I should talk to someone else."
        hide drac with dissolve
        return
    #Dan FTE 1
    if fte_drac == -1:
        n "So um... your name's not actually Dracula right?"
        d "No, it is Dracula."
        n "No last name?"
        d "If I had a full name I wanted you to know, I would have told you it."
        n "Your parents named you Dracula?"
        d "No, I took on the name after returning from death."
        n "You know Dracula's from a book, right?"
        d "If there is a book that resembles my life, that is purely coincidence."
        d "It's like those disclaimers at the start of movies."
        d "That or someone has written a book about my life without my permission."
        n "The book took place like, a hundred years ago."
        n "You're not going to tell me you're over a hundred years old, right?"
        d "What is that so hard to believe?"
        n "Humans rarely live past being a hundred."
        d "Yes, I'm not human."
        d "Admittedly, I was human at one point, and continue to maintain a young human appearance."
        d "And as I told you earlier, I've returned from death."
        d "So it shouldn't be shocking if I lived a normal human life and then another life after that."
        n "You understand how serious the situation we're in is, right?"
        n "Our lives are on the line."
        n "Putting on this whole charade at a time like this?"
        n "It seems immature for someone of your... age."
        show drac ind
        d "It seems more immature of you to assume that this is a charade."
        d "And if it were a charade, to assume it served no purpose."
        n "No, I'm pretty sure in most parts of the world pretending to be a vampire is more immature."
        d "We can agree to disagree."
        d "I assure you, Dan, I fully intend to do everything in my power to help us escape."
        d "And I hope that you are approaching the situation with the same resolve."
        d "But if you are, I don't think conversations like this are making progress in any meaningful way."
        d "I will not be taking further questions on this line of thought."
        n "...got it."
        n "So uh... got any hobbies?"
        d "Maybe I should rephrase. I will take no further questions about myself and my life."
        n "What am I supposed to talk to you about then?"
        d "Let's brainstorm escape plans. That seems to be the most prudent use of time."
        n "Sheesh, was just trying to get to know you better."
        d "If we both make it out alive, we will have plenty of time for that."
        hide screen status_screen
        scene black
        with fade
        ni "Guess Dracula and I just need to agree to coexist peacefully..."
        ni "Or maybe just not talk to each other."

    #Bert FTE 1
    if fte_drac == 0:
       d "Bert. To what do I owe the pleasure?"
       b "Um... I just wanted to talk."
       d "My time is very valuable, I was hoping for more than that."
       d "Very well, I suppose a trifling conversation like this is what humans do."
       d "So, what shall we talk about?"
       bi "Dracula's insistence on being a vampire is... upsetting."
       bi "Maybe I can try to get him to talk about it."
       bi "After all, they say liars get caught when they have to tell a consistent story."
       b "Uh... where do you live as a vampire in modern civilization?"
       d "Well, in a castle of course."
       b "How did you afford a castle?"
       d "Well, as long as I can feed on blood, I can survive forever."
       d "As a consequence, it is quite easy to accumulate wealth."
       d "After all, I've been earning for centuries."
       b "But won't most of your wealth be earned when wages were smaller than now?"
       d "Well, it's easy to beat inflation if you invest in the proper assets."
       d "There are low-risk assets that can beat inflation year-after-year."
       d "The bitter reality is inflation is a tax for being too poor to have savings."
       d "Plus, I save 10\% of my income as everyone should, and since I've lived for centuries..."
       d "It's as if I spent decades saving all my income with no living expenses."
       d "Even with a modest six-figure job, that easily makes me a millionaire."
       b "...{i}Modest{/i} six-figure job?"
       d "Ah, I forgot, humans usually get their first job after only twenty or so years of life."
       d "Again, since I am effectively immortal, I have learned much."
       d "I'd estimate I have the equivalent of four or five PhDs of knowledge."
       d "While science progresses quickly, I've had centuries to learn."
       d "So every time I enter a new field, I have a huge head start."
       b "Wow... it must be nice to not have to worry about time."
       d "Indeed, I am very burden-free."
       d "Don't misinterpret that for not working hard though."
       d "After all, there's a reason vampires are rare these days."
       d "My people have been hunted down by humans for decades now."
       b "...But only because you craved human blood, right?"
       d "The details are unimportant."
       bi "I don't know if I'd say that they are..."
       b "By the way, how are you surviving on here without human blood?"
       d "Well, human blood for vampires is only necessary to slow the aging process."
       d "As long as we make it out of here in the next few decades, I'll simply come out of this aged but alive."
       d "Tell me Bert, how do humans cope with their fragility?"
       b "Um... I don't know, I don't really think about it much."
       b "Don't you have to cope with your fragility when you... acquire blood?"
       d "I have an arrangement with a local hospital to get blood in exchange for some services."
       b "Oh..."
       b "Well, aren't you coping with your fragility in this game as well?"
       d "I am, which is why I'm asking."
       d "It's a new experience for me."
       b "I see... I'll think about it and get back to you."
       d "Very well. Good chat Bert."
       hide screen status_screen
       scene black
       with fade
       bi "Dracula didn't seem to think that conversation was a waste, and was surprisingly open."
       bi "Maybe he feels like he can confide in me now?"

    #Bert FTE 2
    if fte_drac == 1:
       d "Back again Bert? What can I tell you about this time?"
       b "Oh, I was going to tell you something actually."
       b "You asked me how humans cope with their... \"fragility.\""
       b "There's a few answers."
       b "People believe in things like the concept of reincarnation or a soul."
       b "Basically, some assurance that this life isn't all we have."
       b "I think others have the view that nothing really matters..."
       b "So, well, it doesn't matter if it ends either."
       d "Bert, I'm aware of the concepts of religion and nihilism."
       d "I'm asking on an emotional level, how come human fragility isn't paralyzing?"
       d "Like, how do you cross the street knowing a driver could mess up and hit you?"
       b "..."
       d "Oh."
       d "Sorry, I remember..."
       d "Um, different example."
       d "Okay, acts of terrorism happen somewhat frequently."
       d "How do you go to the store, or to school, not fearing for your life?"
       bi "I did my best to shake off the unwelcome reminder."
       b "Well... I don't know, I guess a life full of fear isn't really much of a life."
       b "So we just learn to accept and ignore the possibility something bad will happen."
       b "But I mean, I've lived a pretty sheltered life, so maybe that's not what everyone does."
       b "People in more unsafe areas, people with precarious health conditions..."
       b "Those are probably the people you'd want to ask."
       d "I see."
       d "So you're saying in some sense, humans have to undervalue their life in order to give it value."
       bi "This uh... got dark."
       bi "And off track, I meant to try to \"learn\" more about Dracula to get him to break."
       b "Dracula, what do you do for work these days?"
       b "Or do you just sit on your savings and not work?"
       d "Oh, have we moved on already?"
       b "I um... don't really want to think about it anymore, since... you know."
       d "Hmph. I guess humans are fragile in a different sense."
       d "No, I don't idle around. The human body requires stimulation."
       b "...{i}Human{/i} body?"
       d "Erm..."
       d "Yes, vampires are part human, we're just not fully human."
       d "It's like being a superhero, I guess."
       b "Why do you refer to non-vampires as humans then?"
       d "Most humans don't see me as human."
       d "So it's easier to use it as a shorthand for \"ordinary humans.\""
       d "While I am immortal, it's possible to live forever in a vegetative state."
       d "Both physically and mentally, I need to keep in shape."
       d "Plus, even vampires appreciate a social life."
       bi "If his skin wasn't so pale, I might think he was blushing."
       b "Well, I guess that's true."
       b "So what do you do for work then?"
       d "..."
       d "Ah, that reminds me."
       d "I had promised someone I would speak with them earlier, I should attend to that."
       b "Oh, who?"
       d "That's none of your business, I'm afraid. Goodbye Bert."
       hide screen status_screen
       scene black
       with fade
       bi "Was that Dracula breaking character?"
       bi "I'm not sure, but I might be making progress..."

    if fte_drac == 2:
       d "Bert. Do what do I owe the displeasure?"
       b "...Displeasure?"
       d "Sorry, slip of the tongue."
       d "Anyway, if there's nothing urgent to speak of, I have other matters to attend to."
       bi "I wonder if he's avoiding me because of his slip-up last time."
       bi "Anyway, I need to keep him from leaving, quick..."
       b "Um, Dracula, I believe what you said last time about you being part human!"
       d "Hm?"
       d "That's pleasant, Bert, but I'm not sure why I should care."
       b "Because... uh, I know being viewed as a vampire is important to you!"
       bi "Wow, way to keep your suspicions subtle Bert."
       d "...Viewed as?"
       d "I am a vampire, how I'm viewed by you lot doesn't matter to me."
       d "Some of us will die and the rest will never have to see each other again after this."
       d "So with that in mind, as much as I've enjoyed our little chats, I see no value in conversing."
       d "Unless it's something relevant to our escape, there is surely a more productive use of time."
       b "Do we always have to be productive?"
       d "If I'm going to die here, which I'm not by the way, then I'm dying here without regrets."
       d "I've lived far too long to lose my life over a silly little conversation."
       d "The longer we speak, the less likely it is I make a breakthrough about the corporation behind this."
       b "...The corporation?"
       d "Pardon?"
       b "You said a corporation is behind this game?"
       d "Erm..."
       d "...It's just a suspicion."
       d "Though a rather obvious one, given the scale of this game."
       d "I doubt any single human could pull this off."
       b "Do you happen to have a guess for which corporation it is?"
       d "I fear I've misled you Bert."
       b "Misled me? But I'm just asking about something you believe in..."
       d "Forget I said any of this Bert."
       d "Look Bert, if you're looking to learn something from talking to me..."
       d "I'll tell you one thing, and then we're never wasting time on this again."
       d "Someone in this game is more well-connected to others than they know."
       b "That was... vague."
       d "Maybe. Maybe it's also just something I said to placate you."
       d "A fabrication, even a red herring."
       d "With that, I bid you adieu Bert. I appreciated the conversational stimulation while it lasted."
       hide drac with dissolve
       hide screen status_screen
       scene black
       with fade
       b "..."
       bi "Well, ultimately I failed at my goal."
       bi "But I guess, if I were going to pretend to be a vampire..."
       bi "I would avoid conversations that might expose me as well."
       bi "What he said, though."
       bi "Someone more well-connected than they know... who could it be?"
    if fte_drac >= 3:
       bi "I enjoyed some time with drac, if only because of his pirate speak."

    $fte_drac += 1
    $persistent.fte_drac = max(persistent.fte_drac, fte_drac)
    hide drac with dissolve
    jump postFTEHandler
