#Arun

#Train 1
label frogAsk0:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show frog sad with dissolve
    f "I miss my mom..."
    ni "I should go talk to Bert instead of this kid."
    hide frog with dissolve
    call screen midCar with dissolve

#Train 2
label frogAsk1:
    scene bg trainmid
    $ statusnt("Bar Car", "dan", ch = 1, sun = 1)
    show frog sad with dissolve
    f "I wish there was another kid here..."
    ni "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "O-okay mister..."
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen midCar with dissolve

#Mansion 1
label frogAsk2:
    scene bg mansionbedroom2
    $ statusnt("Bedroom", "bert", ch = 2, sun = 4)
    show frog ind with dissolve
    f "I wonder if Sesame understands frog noises..."
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Okay, but I want to keep petting Sesame!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen bedroomFL with dissolve

#Mansion 2
label frogAsk3:
    scene bg mansionbedroom2
    $ statusnt("Bedroom", "bert", ch = 2, sun = 1)
    show frog ind with dissolve
    f "Cats jump almost as well as frogs do!"
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Okay, but we gotta keep an eye on Sesame!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen bedroomFL with dissolve

#Mansion 3
label frogAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show frog ind with dissolve
    f "I miss Sesame... but I am hungry."
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Okay, maybe my tummy will rumble less if we talk!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen dining with dissolve

#Hospital 1
label frogAsk5:
    scene bg hospkitchenwindow at bg
    show hospwindowoverlay
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show frog sad at inwindow behind hospwindowoverlay
    f "I hate vegetables..."
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Okay, I don't want to eat my veggies anyway."
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen hospKitchen

#Hospital 2
label frogAsk6:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 1)
    show frog ind with dissolve
    f "Oh hey Bert, I'm practicing my sheeshes."
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Sheeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeesh!"
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen patientcommons with dissolve

#Hospital 3
label frogAsk7:
    scene bg hospcommons
    $ statusnt("Cafeteria", "bert", ch = 3, sun = 2)
    show frog ind with dissolve
    f "Wait, isn't the MBA the sports thingy?"
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Adults sure love letters..."
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen patientcommons with dissolve

#Bank 1
label frogAsk8:
    scene bg bankoffice
    $ statusnt("Director's Office", "bert", ch = 4, sun = 2)
    show frog ind with dissolve
    f "Bert, I'm drawing a frog!"
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "If only the frog I drew was real..."
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen office with dissolve
#Bank 2
label frogAsk9:
    scene bg banklobby1
    $ statusnt("Bank Lobby", "bert", ch = 4, sun = 1)
    show frog ind with dissolve
    f "Ribbit. Ribbit. That was frog for \"Hey Bert!\""
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "Ribbbbbbbit. That was frog for \"Sure, let's talk!\""
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen lobby with dissolve

#Bank 3
label frogAsk10:
    scene bg bankvault
    $ statusnt("Bank Hallway", "bert", ch = 4, sun = 2)
    show frog ind with dissolve
    f "Whee, Jenny can't catch me, I'm too fast!"
    bi "Should I talk to Froggy?"
    menu:
        "Spend time with Froggy":
            f "But if we talk, Jenny's going to catch me! ...Okay, fine..."
            jump frogHang
        "Maybe later":
            hide frog with dissolve
            call screen hall with dissolve

label frogHang:
    #Dan FTE 1
    if fte_frog == -1:
        n "So um..."
        n "Uh..."
        f "..."
        ni "Why did I choose to spend my time talking to a kid?"
        ni "It's been years since I talked to adult civilians, much less kids."
        n "So uh... what's with the frog thing?"
        f "The... frog thing?"
        n "Yeah like... you're wearing a frog costume, and you like being called Froggy."
        f "Oh..."
        show frog happy
        play sfx "audio/pophearts.mp3" volume .25
        show pophearts:
            xcenter .5
            ycenter .5
        f "Well, I really like frogs!"
        f "My favorite is the poison dart frog!"
        hide pophearts
        f "It's deadly, but has really pretty colors."
        f "Some other frogs evolved to have similar skin to poison dart frogs."
        f "That way, even though they're not poisonous they look like they are."
        f "So predators will leave them alone."
        f "Did you know toads are also frogs?"
        f "Most people think toads and frogs are like alligators and crocodiles."
        f "Alligators and crocodiles are in different families genetically."
        f "Whereas toads and frogs exist in the same genetic families."
        f "Basically it's a toad if its skin is more warty and less slimy."
        f "There's a famous urban myth about frogs that's false!"
        f "It's called the boiling frog."
        f "The myth says a frog placed in boiling water will jump out immediately."
        f "But a frog placed in warm water that heats up gradually will boil to death."
        f "The moral of the story is to be way of seemingly small changes that turn into big ones."
        f "But really, frogs will just jump out of boiling water."
        n "Have you tested this theory on your own?"
        show frog ind
        f "What? No!"
        f "I'd never a harm an innocent frog like that."
        n "Maybe that's a good lesson for us. Maybe we're the frogs in water."
        n "Even if things feel \"warm\" now they may become boiling later."
        f "That seems like something for adults to think about, not kids like me."
        ni "...so much for trying to relate."
        show frog happy
        f "There's a pair of frogs that once mated for four months straight!"
        f "Though my parents don't want me to learn much about that right now."
        f "They say when I'm older I can."
        f "Some frogs swallow their tadpoles until they become frogs!"
        scene black with fade
        ni "Freddy went on for what felt like hours."
        ni "I didn't learn a lot about Freddy, but I think I learned a lot about frogs?"
        ni "Nothing that'll help us get out, unless the Game Master is a frog..."

    #Bert FTE 1
    if fte_frog == 0:
        f "Hey Bert! Do you like frogs?"
        b "Um... not really, sorry Freddy."
        show frog sad
        f "Oh... ok..."
        bi "...Wow, I am really bad with kids, huh?"
        bi "If Freddy was a girl I was dating I'd respond differently."
        bi "Okay, take two."
        b "...Just kidding! Who doesn't love frogs?"
        show frog happy
        play sfx "audio/pophearts.mp3" volume .25
        show pophearts:
            xcenter .5
            ycenter .5
        f "I know, right!?"
        f "Well, my dad doesn't."
        f "And my mom says she does but she never remembers the frog facts I tell her."
        f "But I think that's just because she's forgetful. Silly mom!"
        b "Hah, yeah..."
        b "So um, what's your favorite frog?"
        f "The poison dart frog!"
        f "They're so colorful, and they have so many cool designs!"
        f "It's like they have their own fashion line!"
        f "And they're aposs... aposs... uh."
        f "Opossum-matic!"
        b "Opossummatic? Like... an opossum?"
        f "No, uh, I'm bad at spelling and saying big words so I don't know how to say it."
        f "But it means they use their colors to tell predators they're poisonous."
        f "It's so cool! It's like, they're like, grrrrrr, but also look cool doing it!"
        f "I wish I could be opossum-matic! When I meet other kids they always make fun of me..."
        f "\"Who wears a frog costume like that all the time?\""
        f "They don't get how cool frogs are!"
        f "If I was a poison dart frog I'd look like this, but they'd have to be scared!"
        f "Because I could touch them and they'd get poisoned!"
        f "Then they wouldn't make fun of me for looking like a frog."
        f "Phew, talking about frogs so much made me tired..."
        f "I wanna take a nap... but we should about frogs again some time!"
        b "Oh, yeah, I'd love to learn more from an expert like you!"
        f "Yay! Bye Bert!"
        scene black with fade
        bi "...Freddy has a not-so-great past hidden in that costume of his."
        bi "But I appreciate that he can be cheery even in a scary place like this."
        bi "Talking to him is a kind of refreshing break from some of the adults here..."

    #Bert FTE 2
    if fte_frog == 1:
        f "Bert, can I ask you a question about being old?"
        bi "I'm not old..."
        bi "Well, I guess to him I am."
        b "Sure, go ahead Freddy."
        f "Um... how much ice cream do you eat every day?"
        b "Huh?"
        f "Well, like, when my mom gets ice cream from the store, there's a lot."
        f "But I can only eat one scoop at a time."
        f "I'm not tall enough to reach the freezer, otherwise I could eat more."
        f "But you're old enough to buy ice cream and tall enough to reach the freezer!"
        f "You must eat a ton of ice cream every day!"
        b "Um... I mean, I eat a little bit every few days."
        f "What?! Bert, do you not like ice cream?"
        b "I mean, I do, but if you eat too much your tummy hurts."
        b "And I know it's annoying when adults say eat your veggies, but..."
        b "Well, I feel a lot better after eating veggies than eating ice cream."
        f "Aw man... is this because you're old?"
        b "Huh?"
        f "Like, you know how old people are wrinkly?"
        f "Do old people also have weak tummies?"
        b "I mean... kind of?"
        b "But I bet if you ate a lot of ice cream you'd feel sick even as a kid."
        bi "Also, again, I wouldn't say I'm old..."
        f "But ice cream makes me so happy, no way it can make me unhappy!"
        b "Well, sometimes too much of a good thing is a bad thing..."
        b "Like um, you like poison dart frogs, right?"
        f "Yeah, they're my favorite!"
        b "Well... imagine if there were like, trillions of them on earth."
        f "Trillions? What's that?"
        b "Uh... imagine if there were hundreds of them in your house."
        f "That'd be so cool!"
        b "Yeah, but you might accidentally poison yourself on one because there's so many."
        b "But if you had only one, it'd be a lot easier to keep track of."
        b "So you'd be a lot safer, but you'd still have a poison dart frog."
        f "Hm... maybe you and your old eyes couldn't keep track of a hundred frogs."
        f "But I could! I'm a frog expert!"
        f "But that's a good idea, I'm going to ask my mom for poison dart frogs when I get home!"
        f "I want to keep a ton as a pet!"
        bi "...I'm sorry Freddy's mom, for whatever chaos I caused."
        scene black with fade
        bi "I tried a few more examples, but wasn't able to convince Freddy."
        bi "Well, I guess that's why it's fun to be an uncle."
        bi "You give the kid advice and if they don't follow it, you don't have to deal with it."

    #Bert FTE 3
    if fte_frog == 2:
        f "Hey Bert... how come you talk to me so much?"
        b "What do you mean Freddy? It's fun to talk to you."
        f "Well, a lot of the others don't talk to me."
        show frog sad
        f "Is it because they hate me?"
        b "Um, I don't think anyone here hates you."
        b "How to explain it..."
        b "Okay, you like poison dart frogs, right?"
        show frog happy
        play sfx "audio/pophearts.mp3" volume .25
        show pophearts:
            xcenter .5
            ycenter .5
        f "Yeah! They're the best!"
        b "Well... not everyone likes poison dart frogs, right?"
        f "Yeah, but that's because they're dumb!"
        f "If they knew as much about poison dart frogs as I did, well..."
        f "They'd have to admit their favorite thing ever is poison dart frogs!"
        b "Hm, well, okay, you love poison dart frogs, but..."
        b "There are other animals you don't like as much, right?"
        b "Like, what do you think about dogs or cats?"
        f "Cats are cute! I love Sesame!"
        f "Dogs can be cute, but some of them are mean..."
        f "Pitbulls scare me! And they poop everywhere in public! That's gross!"
        b "Well, it's totally fine if you think that."
        b "But the people who own dogs love them a lot."
        b "Maybe as much as you love poison dart frogs."
        f "No way, that's impossible! I love them so much!"
        b "Hm... but maybe they love them... half as much as you love poison dart frogs?"
        f "Well... okay, I could believe that!"
        f "But what does this have to why people here hate me?"
        b "Well, I don't think they hate you..."
        b "They just don't like you as much as they like talking to other people."
        b "Just like some people like frogs more than dogs, and others dogs more than frogs."
        f "I see..."
        f "So what you're saying is... they're just dumb!"
        b "Huh?"
        b "Um... what do you mean?"
        f "Well, if everyone were smart, everyone's favorite animal would be poison dart frogs."
        f "And you're saying I'm like a poison dart frog."
        f "So if everyone were smart, they'd like to talk to me, but they're not smart!"
        f "So they must be dumb."
        b "Well, there are options besides smart and dumb..."
        b "Uh, never mind, this is getting off-track."
        f "Dumb! Dumb! Everyone's dumb!"
        hide frog with moveoutleft
        bi "Freddy started walking off, chanting about how everyone's dumb..."
        bi "I'm going to have a lot of explaining to do to the others...."
        scene black with fade
        bi "I feel like Freddy's starting to trust me."
        bi "If only I could use that trust to explain things to him properly..."

    #Bert post-3
    if fte_frog >= 3:
        bi "I enjoyed some time with frog, if only because of his pirate speak."

    $fte_frog += 1
    hide frog with dissolve
    jump postFTEHandler
