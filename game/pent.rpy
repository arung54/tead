label pentGo:
    #$ftecounter = 2
    #$noside = True
    #camera at paralloff
    scene bg reflecting at bg with dissolve
    $cat = False
    $ statusnt("???", "bert", ch=5, sun=0)
    $mood = "sad"
    play music "audio/ominous.mp3" fadein 1.0

    bi "So many people..."
    bi "Dead."
    bi "A week ago there were 12 people stuck in this game."
    show dan ind with dissolve
    bi "Dan..."
    hide dan ind with dissolve
    show stella ind with dissolve
    bi "Stella..."
    hide stella ind with dissolve
    show catherine2 ind with dissolve
    bi "Catherine..."
    hide catherine2 ind with dissolve
    show shahar ind with dissolve
    bi "Shahar..."
    hide shahar ind with dissolve
    show drac ind with dissolve
    bi "Ivan..."
    hide drac ind with dissolve
    show sam ind with dissolve
    bi "And now even Sam..."
    hide sam ind with dissolve
    show lauren ind with dissolve
    bi "And Lauren..."
    hide lauren ind with dissolve
    bi "All dead."
    bi "I know we've all commit crimes in the past, but this just isn't right."
    bi "I didn't even know them that well, but I can't believe they're gone."
    bi "It's not directly my fault, but it's hard not to feel guilty..."
    bi "If I could just stop the Game Master."
    bi "Speaking of which, there are only four of us left."
    show jenny ind with dissolve:
        xcenter .5
    bi "Jenny, the bubbly outspoken activist."
    bi "She's who I've felt closest to this whole time."
    bi "She was the first one to tell me her secrets, and it feels wrong to suspect her."
    show jenny ind:
        linear .3 xcenter .25
    show sid ind with dissolve
    bi "Sid..."
    bi "A bright teenager with a poor past, caught up in some legal issues."
    bi "He was the first one to really get hit with the weight of this game, finding Dan's body..."
    bi "In my heart I think he's just doing everything he thinks is right, but... I don't know."
    show sid ind:
        linear .3 xcenter .75
    show frog2 ind with dissolve
    bi "And then there's Freddy."
    bi "I just feel awful for this kid..."
    bi "He had a terrible life, and now he's stuck in here probably because of his father."
    bi "And now it's just the four of us."
    bi "I trust all of them, but... maybe I shouldn't?"

    bi "We also have the hint from the vault."
    bi '"The Secret of the Game", as it said.'

    bi "I don't know what to think."
    bi "I want to find a way to save them all, but if one of them's the Game Master..."
    bi "Is it even possible to save everyone?"
    bi "Jenny? Freddy? Sid?"
    bi "...No matter what, I have to try."
    bi "I'm going to figure everything out, and save us."
    bi "There's no time to waste, so I need to start collecting evidence as soon as possible."
    hide frog2 ind
    hide jenny ind
    hide sid ind
    with dissolve
    bi "..."
    bi "I feel the weight of Sesame laying on my chest."
    bi "My head hurts..."
    bi "It's hard to tell why."
    bi "Maybe it's the brain chip that keeps knocking me out."
    bi "Maybe it's all this trauma..."
    bi "Or it could just be this hard ground."
    bi "If I move a bit I hear a creaking noise."
    bi "Hardwood floors."
    bi "It smells like... dust."
    show bg pentcellar at bg
    show scary:
        alpha .6
    with dissolve
    $mood = "shock"
    $cat = True
    bi "I immediately feel claustrophobic."
    bi "There's it's dark."
    bi "But there are clearly bottles of wine all over the walls."
    bi "I'm in a big closet?"
    bi "No, there's a ladder going up, and no other way out."
    hide scary with dissolve
    bi "My eyes are adjusting a bit."
    bi "It seems like... a wine cellar?"
    $ statusnt("Wine Cellar", "bert", ch=5, sun=0)
    bi "Of all places, why am I stuck in a wine cellar this time?"
    ses "Mrep."
    $mood = "ind"
    bi "And more importantly, where is everyone else?"
    bi "It's weird that I'm waking up alone..."
    bi "I need to go find them."
    bi "Up the ladder I go-"
    ses "Mrep!"
    $mood = "shock"
    bi "Huh?"
    bi "There's a drawer on the far wall."
    blank "Bert walked over and opened the false panel."
    blank "Inside was a shelf with one item."
    $noside = False
    show theflashlight with dissolve
    bi "It's a flashlight."
    bi "It's made of metal, with an on-off button on the shaft."
    bi "There's also a small metal tip on the opposite end."
    bi "It turns on, but it's not {i}that{/i} dark down here anyway."
    $noside = True
    blank "Bert unscrewed the flashlight to find its batteries."
    $noside = False
    $mood = "ind"
    bi "Doesn't seem like anything out of the ordinary."
    hide theflashlight with dissolve
    bi "But why is a flashlight being locked away in a wine cellar?"
    bi "..."
    bi "......"
    bi "I woke up alone in a wine cellar with access to an item, this flashlight."
    bi "Does that mean what I think it means?"
    $mood = "shock"
    bi "Have I... been chosen as the killer for this round?"
    bi "It's a horrible thought."
    bi "If so, why was I given this flashlight specifically?"
    bi "And shouldn't I have a connection to this location?"
    $mood = "sad"
    bi "I've definitely never been in this wine cellar before..."
    bi "And I don't know what I'm supposed to do with a flashlight."
    bi "..."
    bi "Maybe it's good if I'm the one picked as the killer..."
    bi "I know for certain I would never resort to that... but..."
    bi "I wouldn't be able to say the same for the others."
    bi "Plus, it was a 1 in 3 chance to get chosen, assuming the Game Master is here with us."
    bi "..."
    bi "Despite that, it's hard not to feel a looming pressure."
    bi "I imagine this is how Kaiser, Catherine, Ivan, and Lauren must have felt."
    "Bert sighed."
    bi "For now, I'll hang on to this flashlight."
    $noside = True
    blank "Bert put the flashlight in his backpack."
    $noside = False
    bi "Alright."
    b "Time to go find everyone else, Sesame."
    ses "Mep."
    scene black with dissolve
    $noside = True
    blank "Bert went up the ladder and opened the hatch."
    $noside = False
    scene bg pentbedroom2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    play music "audio/rush.mp3" fadein 3.0
    show sidsleep at bg:
        xcenter .5
        ycenter .63
        zoom 1.5
    show frogsit4 at bg:
        xcenter .96
        ycenter .74
        zoom 1.3
    show jennyfeet at bg:
        xcenter .715
        ycenter .77
    with fade
    bi "The hatch to the wine cellar is half covered by the rug."
    bi "It's as if the wine cellar is normally hidden."
    bi "Why would someone need to hide their wine cellar?"
    bi "Anyway..."
    bi "It looks like a bedroom."
    $ statusnt("Bedroom", "bert", ch=5, sun=0)
    bi "And the other 3 are here and still asleep."
    i "snnnnnnnnnnnnnnnnnnnnnnnn......."
    b "Hey guys, wake up."
    f "mimimimimimimi....................."
    bi "..."
    b "HEY!!!"
    b "WAKE UP!!!"
    show jenny scared:
        xcenter .3
    show frog2 ind:
        xcenter .7
    hide frogsit4
    hide jennyfeet
    with dissolve
    j "Bert! Was that you screaming?"
    j "Yaaaaaaaaaaaaaaaaaaaaaawn."
    f "Good morning Bert!"
    b "Thank goodness you guys are safe..."
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .35
        ycenter .275
        zoom .75
    j "You woke us up though..."
    bi "..."
    f "Not Sid though, he's still napping."
    hide poptear
    j "It seems like it."
    j "I have a horrible kink in my neck, probably from sleeping on the floor..."
    show jenny happy
    j "Why couldn't they have put me on the bed, and Sid on the floor?"
    bi "How is she so nonchalant..."
    j "The Game Master finally got some taste!"
    j "This looks like a penthouse or hotel or something."
    #b "The other room has a nice kitchen, I think it's a highrise apartment."
    j "This big fancy bed, that flatscreen TV, wow!"
    j "We're living the life now."
    show frog2 smile
    f "Yeah! Living the life!"
    bi "..."
    b "Anyway, we should all chat."
    b "It's just the four of us now."
    show jenny ind
    j "That's a bit... sad."
    show frog2 sad
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .7
        ycenter .1
    f "*sniffle* L-Lauren..."
    b "Yeah..."
    b "We've got each other though, Freddy."
    b "I'll make sure you're safe."
    j "Me too, and so will Sid."
    b "Speaking of which, let's wake that guy up so we can all talk."
    hide poprain with dissolve
    f "Ummm..."
    f "Miss Jenny, do I have to listen?"
    f "All this stuff makes me really sad..."
    b "It's important for you to be here, Freddy."
    j "Bert..."
    show frog2 smile
    j "Freddy, just stay in the room with us so we can keep an eye on you, okay?"
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter .7
        ycenter .5
    f "Yay! Thank's Jenny."
    hide frog2 with moveoutright
    show frogsit3 at bg:
        xcenter .96
        ycenter .74
        zoom 1.3
    with dissolve
    show jenny ind:
        xcenter .3
        linear .3 xcenter .5
    j "Come on, he's just a kid."
    j "Lauren just died too, and you know that he really liked her."
    b "Okay... as long as he's in the room with us."
    b "Last thing we need now is for something to happen to Freddy."
label pent2:
    scene black with dissolve
    $noside = True
    blank "They shook Sid awake."
    $noside = False
    scene bg pentbedroom2 at bg
    $ statusnt("Bedroom", "bert", ch=5, sun=0)
    show frogsit3 at bg:
        xcenter .96
        ycenter .74
        zoom 1.3
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    i "Ugh..."
    j "Morning sleepyhead."
    i "Morning guys."
    i "So it's just the four of us now, huh."
    i "I can't believe Lauren did Sam in like that."
    i "Guess you really can't trust anyone these days."
    b "Speaking of which, it should be pretty easy for us to narrow down our {i}roles{/i} now."
    i 'What do you mean our "roles"?'
    b "Well, unless we've been lied to this whole time, one of us is the Game Master."
    b "And another one of us is the chosen killer for this location."
    j "So, two out of the four of us have some predetermined role."
    b "Right."
    b "Surely, the Game Master won't speak up now and say they're the Game Master, but..."
    i "...since it's just the four of us now, maybe the chosen killer would speak up."
    b "Exactly."
    b "We need to work together."
    b "If we all know which one of us is the chosen killer, we can break this all down and end this."
    j "Oh! And if the chosen killer speaks up, we know they're not the Game Master."
    j "So then it's just 1/3 for who the bad guy really is."
    i "Yeah, sure, but if I was the Game Master right now I'd lie my ass off, like:"
    i "\"Yo guys I'm the killer this round!\""
    b "But then the {i}real{/i} chosen killer could speak up, and we'd know one of them is the Game Master."
    i "Hmm... I guess that's true."
    show jenny happy
    j "Great logic guys!"
    j "So who's who?"
    j "Speak up now or forever hold your peace!"
    b "..."
    i "Well don't look at me!"
    j "C'mon Sid, you can admit it, I'll forgive you!"
    show sid mad
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .65
        ycenter .275
        zoom .75
    i "If I really was the Game Master, you shouldn't forgive me!"
    show scary with dissolve:
        alpha .5
    bi "This went a bit more smoothly in my head..."
    hide poptear
    bi "Plus, I've been avoiding the fact that Freddy could technically be either role..."
    bi "As unlikely as it is, it throws a bit of a wrench in my logic."
    bi "Maybe we're rushing this."
    bi "As long as we all keep eyes on each other we should be fine, and there's only four of us anyway."
    hide scary with dissolve
    b "Hmm, alright, at least we all know the plan for now."
    show sid ind
    b "Maybe we should explore a bit so chosen killer knows that's their role."
    b "If one of us does have a connection to this location, we need to scope it out a bit first."
    i "Yeah, I haven't even been outside this frou-frou bedroom yet."
    j "It seems like there are two doors out of here, which room should we check out first?"
    show scary with dissolve:
        alpha .5
    menu:
        bi "Let's check out the door on the..."

        "South wall.":
            hide scary with dissolve
            b "Let's go this way."


        "East wall.":
            hide scary with dissolve
            b "Let's go this way."
    j "Aye Aye, captain Bert!"
    b "You sound like Shahar..."
    scene black with dissolve
    $noside = True
    blank "The four of them went into the next room together."
    $noside = False
    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    b "Wow..."
    b "This looks like a personal library, or a study."
    $ statusnt("Study", "bert", ch=5, sun=0)
    show jenny happy:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    j "Look at this place!"
    j "All these books, it's so cozy!"
    i "Looks like a real nerd lives here..."
    j "There's even an electric fireplace."
    hide jenny happy with dissolve
    bi "She turned it on."
    #ADD FIREPLACE ON BACKGROUND HERE!!!!!!!!!!! SHE TURN THAT SHIT ON FR
    #JULIAN
    show jenny happy:
        xcenter .3
    with dissolve
    j "Ahh, I could get used to this."
    b "We're not here to get used to this..."
    b "We should look for anything that could connect us to this place."
    j "I'm pretty connected to being warm and cozy, so..."
    i "Looks like there's some booze too!"
    $mood = "sad"
    b "Please... work with me here."
    i "Yeah you're right."
    i "Well I've definitely never been here before."
    i "The only library I've been to is the public one near me, definitely nothing fancy like this."
    b "Me too... I have no memory of this place."
    #b "It seems a very personal nook for someone."
    j "Well, let's look around!"
    j "Maybe there are some clues for us!"
    hide jenny
    hide sid
    with dissolve
    $noside = True
    blank "They spent a few minutes looking around the room."
    $noside = False
    b "Hey, guys."
    b "One thing does look familiar."
    i "Hm?"
label pent23:
    show scary with dissolve:
        alpha .5
    menu:
        b "Look at that..."

        "picture on the wall.":
            hide scary with dissolve
            b "Yeah, that painting over the fireplace."
            b "Haven't we seen it before?"

        "selection of drinks over there.":
            bi "Hmm... On second thought..."
            jump pent23

        "model of fireplace.":
            bi "Not sure why I'd say that..."
            jump pent23

    show jenny ind with moveinleft:
        xcenter .3
    show sid ind with moveinright:
        xcenter .7
    i "Oh! You're right! It's the same one that was in the mansion!"
    scene bg mansiondining at bg
    $ statusnt("Dining Room", "bert", ch=2, sun=1)
    $showchibint("freddy")
    show frog sad
    show sepia:
        alpha .5
    with fade

    f "Oh, Bert! Are you awake? Feeling okay?"
    b "Yeah, I'm fine."

    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show jenny happy:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    j "Oh wow! Great memory, guys."
    j "Did someone move it here?"
    i "Nah, that one was way bigger."
    i 'I remember thinking "damn, is that the original?" and Stella called me stupid.'
    i "I doubt this is the original either."
    bi "I think the original is in England somewhere."
    b "Anyway, I don't think it's a coincidence that the same painting is here."
    b "The decor in general is pretty similar too."
    b "There's definitely some connection to Mr. Sydell's mansion."
    j "I found something too."
    j "Everything is neat and all the books are back up on the shelves, but..."
    j "This book specifically was tucked one of the couch cushions."
    j "It was open to this page."
    show bg journal1 at bg
    hide jenny
    hide sid
    with dissolve
    b "It looks like..."
    b "A journal?"
    b "This is definitely someone's handwriting."
    b "It says..."
    b '"Taking refuge in a rented penthouse..."'
    b '"this is not sustainable. But where else can I go?"'
    b '"They know where I live. I fear my days as well are numbered."'
    b '"Unless... I can turn the tables."'
    b "Huh?!"
    b "What the hell... this was written by whoever was living in this penthouse..."
    b "Or taking refuge, as they said."
    b 'Refuge from what? Who are they scared of, who is the person that "knows where they live?"'
    j "Bert, this is scary..."
    j "Not a big fan of this book..."
    show bg pentstudy at bg
    show jenny scared:
        xcenter .3
    show sid happy:
        xcenter .7
    with dissolve
    j "Going through this journal, I feel like a detective or something..."
    j "But not in a fun way."
    i "Yeah, why do I have feeling it didn't end well for this guy?"
    i 'The part about his "days being numbered" and then the next page being blank is...'
    i "A little spooky."
    b "Does anyone know the handwriting?"
    bi "Nobody spoke up."
    hide sid happy with moveoutright
    show frog2 ind with moveinright:
        xcenter .7
    f "Is there anything else written in the book?"
    b "That's a great question, Freddy."
    bi "I thumbed through the previous pages."
    bi "There's a lot of business information, and some stuff in another language."
    bi "At a glance, I'm not sure how useful the rest of the journal will be."
    f "So whose is it, Bert?"
    f "I thought you're always supposed to write your name at the top of the page."
    j "Mhm, mhm. It's true."
    b "I don't think they were in the right headspace to be doing that."
    show scary with dissolve:
        alpha .5
    bi "Still, there might be a way we can use this..."
    bi "There was one criminal who knew where someone seemingly important lived."
    bi "Maybe the writer was that person... and they were worried the criminal would come back."

label pent25:
    show scary with dissolve:
        alpha .5
    menu:
        bi "That criminal was..."

        "Dracula.":
            bi "No, we don't know that for sure."
            jump pent25

        "Catherine.":
            bi "Yeah... that's it!"
            hide scary with dissolve

        "Lauren.":
            bi "I don't think she mentioned anything like that."
            jump pent25

    b "I think that settles it."
    i "Settles what?"
    b "Lets assume this really is Mr. Sydell's journal."
    b "Think about it - it seems like almost all of us have some connection to Sydell."
    b "And importantly, Catherine said she had robbed his house before."
    scene bg nmansiondining at bg
    show catherine ind
    show sepia:
        alpha .5
    with fade
    b "Did you commit a crime here?"
    c "Oh yeah, I burgled this mansion before while the owner was out."
    b "Does that mean you knew Mr. Sydell?"
    c "Eh, never met the guy. I just overheard from an acquaintance that he was in court that day."
    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show frog2 ind:
        xcenter .7
    with fade
    b "She didn't know Sydell, but she knew where he lived."
    b 'That fits with what the journal says.'
    b 'Maybe he was scared Catherine, or someone else, would come back.'
    b "So he came here to take refuge."
    j "Wow, Bert, you might be right."
    j "Between the painting, the furniture, and the book, I think you're onto something."
    if not pent_evidence[0]:
        $pent_evidence[0] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "Sydell's Apartment was added to evidence."
    hide frog2 with moveoutright
    show sid ind with moveinright:
        xcenter .7
    i "So we're in Sydell's secret apartment?"
    b "That's my best guess so far..."
    i "I don't get it though - didn't Catherine just rob him?"
    i 'Why\'s he talking all like "my days as well are numbered"?'
    i "I dunno, I've been robbed before, and it's scary, but renting a place like this to hide seems like... overkill."
    i "Pun intended."
    j 'Also, why "as well"?'
    j "Doesn't that imply someone had already died?"
    b "Maybe someone close to Sydell had been murdered."
    b 'That would explain him saying "as well".'
    b "Then, when Catherine robbed his empty house, he thought he was next to die."
    i "Yeah, I guess that tracks."
    i "He got spooked and came here."
    show scary with dissolve:
        alpha .5
    bi "Even if this is true, it brings up even more questions..."
    bi "Why was someone killed before him?"
    bi "What were Sydell and that person doing to end up in this situation?"
    bi "And lastly, how does this connect to our situation?"
    hide scary with dissolve
    b "One step forward, one step back..."
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .41
        ycenter .25
        zoom .75
    $mood = "shock"
    j "Bert, take a look at this!"
    b "Hm? What's is it?"
    hide popwow
    j "There's a little slip of paper tucked in a different page."
    show bg journal2 at bg
    hide jenny
    hide sid
    with dissolve
    b "This looks like a phone number."
    b "It's scribbled down in the same handwriting on a scrap of paper..."
    b 'And the word "spaghetti", for whatever reason.'
    b 'Maybe... this phone number has to do with "turning the tables."'
    i "Why's it say spaghetti?"
    i "Was he ordering takeout?"
    j "If we had a phone, we could just call it. But we don't have one..."
    b "Spaghetti... spaghetti..."
    b "I feel like I should know someone by that name..."
    i "You know someone named Spaghetti?"
    b "Kinda... someone that was trapped with us."
    b "That's it!"
label pent26:
    show scary with dissolve:
        alpha .5
    menu:
        bi "That person was..."

        "Kaiser.":
            bi "No, it definitely wasn't Kaiser..."
            jump pent26

        "Dracula.":
            bi "I don't think he mentioned anything like that..."
            hide scary with dissolve
            jump pent26

        "Dan.":
            bi "It was Dan!"
            hide scary with dissolve


    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    i "What are you talking about?"
    b "Dan must be Spaghetti - there's no other explanation."
    b "On the first day on the train, Dan talked to me in private."
    scene bg trainfront at bg
    show dan ind
    show sepia:
        alpha .5
    with dissolve
    n "Speaking of Italian food, some of the people I used to roll with would call me Spaghetti." #febreview
    b "Spaghetti?"
    n "I think they were teasing me about my last name, Scagnelli."
    n "It's long, Italian, and has a bunch of letters, kinda like Spaghetti."
    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    i "What?!"
    i "So this is... Dan's number?"
    i "Dan..."
    bi "I'd forgotten how quickly Sid grew attached to Dan."
    bi "Something about a strong male figure to look up to, I suppose."
    b "Given Dan's history especially, I'm not shocked to see he was tied up in all this."
    j "Bert!"
    bi "Jenny gave me a look, I don't think she wanted me badmouthing Dan in front of Sid."
    i "He's right..."
    i "One of the last things Dan said to me was about his criminal history."
    j "Oh... I see..."
    i "Dan was kind to me, but there's no reason to dance around his shady past."
    b "Still, why is his phone number in a place like this?"
    b "Maybe Sydell was looking to call in a favor."
    j "That would make sense, if he was scared of Catherine and the lawyers after him."
    j "Maybe Sydell needed a bodygaurd, or-"
    i "A hitman..."
    bi "Sid looks like he's piecing together Dan's past."
    b "If Sid was a hitman, everything would start to make sense."
    j "What do you mean? What would make sense?"
    b "Sydell wanted Stella gone, right?"
    b "He was being sued into the ground, and was scared for his life after Catherine's robbery."
    b "Back in the mansion Stella said something that stuck with me."
    j "Well? What was it?"

label pent27:
    show scary with dissolve:
        alpha .5
    menu:
        bi "Stella told us that..."

        "She knew Dan as a hitman.":
            bi "No, she definitely never met Dan prior to this..."
            jump pent27

        "Her bodyguards have sent hitmen back to kill their bosses before.":
            hide scary with dissolve
            bi "I remember it clearly now!"

        "She knew it was Sydell's masion right away.":
            bi "She did say that... but that's not relevant at the moment."
            #hide scary with dissolve
            jump pent28
label pent28:
    b "It was me, Stella, and Shahar in the dining room."
    b "She said..."
    scene bg nmansiondining at bg
    show stella drunk
    show sepia:
        alpha .5
    with fade
    t "What a jarring change from my day-to-day this all is..."
    t "I used to be so powerful that there'd be assassination attempts on me weekly."
    t "My team got so used to it they'd even turn hitmen back around to kill their bosses." #febreview
    bi "That's insane..."
    t "But now, here, we're all equally powerless."
    scene bg pentstudy at bg
    $ statusnt("Study", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    b "Maybe Dan was hired by Sydell as the hitman... to take out Stella."
    b "Then, Stella's bodyguards caught Dan, and made him kill Sydell."
    b "That would explain this note being here."
    i "And it might explain why Dan was in jail prior to this game."
    j "It also make it seem more likely that Sydell is dead."
    $mood = "shock"
    b "We can't be sure he's dead."
    j "But if Stella's team knew about a hitman out for her head, I'm sure they'd counterattack."
    j "Whether it was her own guards, or Dan, I'd imagine Sydell was killed..."
    b "..."
    $mood = "ind"
    bi "We were all silent for a moment."
    b "You're probably right." #ev
    b "We should assume Sydell was killed in response."
    show jenny:
        linear .2 xcenter .25
    j "Does that mean one of you three is really behind all this?"
    j "I was still holding out hope that... some bald old freak named Sydell was behind it all."
    j "But if he's been dead this whole time, then there's no way..."
    bi "One of us is behind all this..."
    bi "She's probably right."
    bi "But I don't want to accept that just yet."
    b "Let's keep exploring before we get too depressed about it."
    i "Agreed!"
    hide sid with moveoutleft
    scene black with fade
    "All four of them made their way back through the other bedroom door."
label pent29:
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    b "This looks like..."
    show jenny ind:
        xcenter .3
    show sid smile:
        xcenter .7
    with moveinright
    i "A kitchen!"
    j "A living room!"
    $ statusnt("Dining Room", "bert", ch=5, sun=0)
    b "Both, I think."
    j "Gotta love an open floorplan."
    bi "She's pretty quickly back in high spirits..."
    j "It looks like we're... really high up?"
    i "Holy shit, those are windows!"
    bi "He's right..."
    bi "This is the first time since the train we've seen windows that aren't boarded up."
    i "Gang, we're makin' a jump for it!"
    hide sid with moveoutbottom
    show sidstand2 at bg with dissolve:
        xcenter .48
        ycenter .53
    "Sid ran over to the windows."
    b "Hold on!"
    i "We can break through the glass and jump for it!"
    "Sid started banging on the window as hard as he could."
    b "At least try to {i}open{/i} the windows first..."
    show jenny scared
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter .3
        ycenter .3
        #zoom .75
    j "Bert!"
    j "Bert! Make sure he doesn't fall!"
    b "Oh! You're right!"
    scene black with fade
    "Bert ran over to the window and pulled Sid away."
    "Bert looked out the window."
    scene bg pentview2 at bg
    show fogscroll at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    b "..."
    b "It really is a window to society..."
    bi "I can see a couple cars, and even some people walking..."
    bi "But... it's so foggy, and it must be the absolute middle of the night."
    bi "Still, it feels nice to know there are some other people out there."
    "{i}BAM BAM BAM!{/i}"
    b "Sid! Stop hitting the windows!"
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    show jenny ind:
        xcenter .3
    show sidstand2 at bg:
        xcenter .48
        ycenter .53
    with dissolve
    i "It won't budge!"
    i "I can't even make a crack in it."
    "{i}WHACK WHACK WHACK!{/i}"
    j "Well don't keep trying!"
    "{i}WHACK WHACK WHACK!{/i}"
    "{i}WHACK WHACK WHACK WHACK WHACK WHACK!{/i}"
    "{i}WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK!{/i}"
    b "...I think it's fine."
    j "If he falls out the window, I'm blaming you."
    hide sidstand2 with dissolve
    show sid ind with moveinbottom:
        xcenter .7
    i "I think the windows are safety glass or something fancy."
    i "They're really hard, my hand hurts now..."
    b "Help Jenny and I look around for a bit."
    b "If we can't find anything useful, I'll help make something to break through the glass."
    bi "Maybe."
    j "It does feel weird..."
    i "Weird?"
    j "Well, it really is the first time since we were on the train to have a window."
    i "Yeah... we got to have windows on the train because nobody was suspicious yet."
    i "It didn't feel like anyone would {i}kill each other{/i}."
    show scary with dissolve:
        alpha .5
    bi "It's true that we were less skeptical on the train, but..."
    bi "I'm not sure that's why the windows weren't boarded up."
    bi "In fact, there's even a similarity between then and now."
    bi "There's only one reason the Game Master wouldn't have covered them."
label pent30:
    menu:
        bi "The reason that the train windows and these penthouse windows aren't covered is..."

        "It was too difficult to secure the covers over the windows.":
            bi "After everything we've been put through, I doubt that would be an issue..."
            jump pent30

        "Opening the windows was a means of murder.":
            bi "That must be it..."
            bi "On the train, jumping out the window at such a high speed would kill you."
            bi "And here, falling from such a height would do the same."
            bi "And in either situation, being pushed out the window..."
            bi "That would be murder."
            hide scary with dissolve

        "The Game Master would kill us with the brain chips either way.":
            bi "We're pretty certain the Game Master would kill us if we tried to escape."
            bi "But I don't think that's why they left the windows uncovered."
            jump pent30

label pent31:
    b "I think..."
    b "The windows aren't covered for a reason."
    i "Huh?"
    b "Think about it."
    b "On the train, the windows were the easiest way to kill someone."
    j "That's true..."
    b "In fact, Kaiser's murder method did involve the window, the one in the caboose."
    i "Y-yeah..."
    b "This is a little different, because we're not moving."
    i "But being tossed out this window would for sure kill you."
    j "Tossed?"
    i "Thrown, tossed, chucked, ya know."
    b "Pushed, probably..."
    i "So the Game Master wants us to hurl each other out the window?"
    b "Well, it seems like they're leaving that possibility on the table..."
    i "I still think we should try to jump for it."
    i "If we had known what was going to happen on the train, I woulda jumped there too!"
    b "That's... understandable."
    b "Sid, let's look around for a bit."
    b "If we don't find anything useful, maybe we can rig something up get out the window."
    i "Alright, deal."
    j "There are lots of drawers, cabinets, and tables in here."
    hide jenny with moveoutleft
    show frog2 ind with moveinleft:
        xcenter .3
    f "What should I do to help!"
    b "Ummm..."
    b "You can have the most important job."
    f "Really!!!"
    b "Yup! We need someone to look between all the couch cushions!"
    f "Oh boy!"
    bi "Maybe that will distract him for a bit."
    b "Make sure you don't miss anything, Freddy!"
    f "Aye aye, sir!"
    bi "Why's everyone saying that now..."
    b "Okay, let's get started."
    scene black with dissolve
    "The four of them spent 30 minutes scavenging every corner of the room."
    "LAST FREETIME???"
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    j "Okay team!"
    j "Despite a lot of places to hide stuff in here, it doesn't seem like there's a lot of hidden stuff."
    i "I can't believe we're tearing apart a rich guy's penthouse and there's no money laying around."
    i "Leave me a little cash bro come on..."
    j "He {i}was{/i} rich."
    j "By the time he was hiding here, he was losing money and in some business troubles, remember?"
    i "Yeah, true."
    b "Well speaking of business, Jennny did find this folder labeled \"InSyde Electronics\"."
    b "Stella told us that that was the name of Sydell's company, so maybe there's something useful in here."
    j "I took a peek inside and it looked useful, so I set it aside for us to read through."
    b "Let's see..."
    b "W2... receipts... shipping documents..."
    b "Woah!"
    i "What is it?!"
    b "Look, look!"
    b "There's something about an insurance claim!"
    j "That doesn't sound exciting..."
    b "Just take a look."
    i "Huh, the page is torn in half."
    show scary:
        alpha .5
    show sydellfile
    with dissolve
    bi "..."
    i '"Stewart Sydell?"'
    i "Bro's first name is Stewart?"
    b "Come on, keep reading."
    j "It's about InSyde Electronics, his business."
    i "It says..."
    i "{i}This letter serves as a rejection for coverag e of claim #092523...{/i}"
    i "Rejection?"
    i "So his insurance company flaked on him?"
    b "Basically, yeah..."
    j "Wait, but what was this insurance claim about in the first place?"
    b "Let's keep reading..."
    b "{i}Thank you for your business...{/i} yada yada..."
    b "{i}Due to the nature of the theft we’re unable to assist at this time.{/i}"
    b "Theft?"
    j "Maybe this is about Catherine again?"
    j "She robbed Sydell's house, maybe this is about that."
    i "Yeah, I bet."
    i "She took some stuff and he wanted the money back for it."
    b "Hmm..."
    b "It's true Catherine robbed him, but if the claim is about that, something doesn't add up."
    hide sydellfile with dissolve
    i "You think this is about a different theft?"
    j "What makes you think this isn't about Catherine?"
label pent32:
    show scary with dissolve:
        alpha .5
    menu:
        b "If it's about Catherine, then..."

        "why is this addressed to his company?":
            hide scary with dissolve

        "why isn't her name anywhere on it?":
            bi "Hmm, well, I guess the robber's name isn't on it at all."
            bi "So that doesn't really indicate anything here."
            jump pent32

        "why did he use Week Air Insurance?":
            bi "On second thought, it is a pretty big brand."
            bi "I don't think that tells us anything useful."
            jump pent32

label pent33:
    j "What do you mean?"
    b "At the top it says..."
    show sydellfile
    with dissolve
    b "{i}To whom it may concern, InSyde Electronics{/i}"
    b "It's not directly addressed to Mr. Sydell."
    j "If this was about a home break-in, I guess it wouldn't say that"
    hide sydellfile
    with dissolve
    b "Right, it would just be addressed to him."
    j "Good catch Bert!"
    i "But wait, if it's not about Catherine robbing him, is this even useful?"
    i "Who cares about some random insurance claim against his company?"
    b "..."
    j "Sid, you're pretty nonchalant about his considering it could be able you!"
    i "Hey! I didn't steal from him!"
    i "I hacked him, and planted information."
    i "If anything, I left him with more than when I started!"
    b "..."
    b "Ignoring that last comment, Sid is right."
    b "He never robbed InSyde, so this isn't about him."
    i "YEAH!"
    b "But he's wrong about this being useless."
    b "There's one more piece of information we can use to tie this to us."
    j "Let me see, let me see!"
    j "I want to figure it out."
    b "I'm sure you can."
    i "Me too! Hype me up man."
    b "Uhh, go Sid go."
    "They looked over the document again."
    j "..."
    i "....."
    j "........"
    i "I got it!"
    j "It's the date, August 6th!"
    i "That's what I was going to say!"
    i "Wait, what? The date?"
    j "It says the claim was filed on August 6th, that's useful!"
    i "Umm yeah, that's what I was going to say too..."
    b "..."
    b "Jenny's right - we can tie someone's crime to that date."
    i "I don't know any of the dates the crimes happened on..."
    j "I don't either, except my own I guess."
    b "I remember the one that matters right now."
    show scary with dissolve
    call screen chooseCharPent("kaiser", "pent34", "The person whose crime happened on this date is...") with dissolve
label pent34:
    hide scary with dissolve
    j "Kaiser's train heist was on August 6th?"
    b "Technically, no."
    b "Think back."
    scene bg ntrainfront at bg
    $ showchibint("catherine", "dracula", "freddy", "jenny", "kaiser", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Front Car", "bert", ch=1, sun=4)
    show doom
    with dissolve
    show kaiser ind:
        xcenter .7
    show sid ind:
        xcenter .25
    with dissolve
    show sepia:
        alpha .5
    k "And then... this car."
    k "It reminds me of one heist in particular, my most famous heist."
    k "I'll never forget the day, down to the most minute details."
    k "It was the coldest August 5th I've ever experienced, and one that changed my life."  #febreview
    k "It was going to be my big break... and for a while, I thought it was."
    k "How naive of me..."

    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7

    b "Kaiser's heist was on August 5th, which is one day before the claim was made."
    i "So Kaiser's crime impacted Sydell, who then filed an insurance claim the next day..."
    j "And then that claim got shot down, leaving Sydell in the red."
    b "I think that's it, yes."
    b 'It would also explain what this form means about the "nature of the theft".'
    b "A train heist seems like an unusual thing to file for."
    j "Which probably made it easy for the insurance company to reject."
    i "Man..."
    i "I mean, I hate that guy right, but damn."
    i "He really went through a lot at the end there."
    j "Yeah..."
    i "Robbed by Catherine and Kaiser, on Sam's sketchy drugs, crushed by Stella's firm..."
    b "And probably even more that we haven't uncovered yet."
    j "He's why we're here though! Right?"
    j "I can't feel bad for someone like that."
    i "Tr-true..."
    show scary with dissolve:
        alpha .5
    bi "If he's dead, he can't be the Game Master though."
    bi "It has to be someone here."
    bi "And based on the hint from the bank, their last name starts with S..."
    hide scary with dissolve

    show frog2 ind with moveinbottom:
        xcenter .5
    show jenny ind:
        linear .2 xcenter.25
    show sid ind:
        linear .2 xcenter .75
    f "Jenny, look what I found!"
    f "Some candy!"
    j "Huh?"
    $mood = "shock"
    b "Freddy! Gimme those!"
    bi "These are not candy..."
    show pillbag with dissolve
    b "These are..."
    j "Drugs?"
    show frog2 ind:
        xcenter .5
    i "Party pills, the kids at my school call em..."
    b "The pills are small and colorful, and this type of bag doesn't make it look like candy."
    hide pillbag with dissolve
    j "Freddy! Where did you find these?"
    f "It was tucked away between the couch cushions."
    bi "I can't believe that distraction actually lead to finding something."
    f "So can I have them or not?"
    b "Absolutely not. These aren't for kids."
    f "What about just one?"
    j "Freddy, they could make you really sick."
    f "Uh oh, really?"
    j 'Why "uh oh" Freddy?'
    b 'Yeah why "uh oh"?'
    f "Errrrmmmmmmmm..."
    f "I may have already eaten one..."
    b "What?!"
    f "Well they look so yummy!"
    f "But they don't really have much flavor."
    bi "If these really are drugs, the effect will start kicking in soon."
    bi "And for a kid his size, it could cause serious damage."
    b "Freddy... how long ago did you eat the first one..."
    f "Erm..."
    hide frog2 ind with moveoutbottom
    #scary music
    "Freddy fell to the ground."
    j "Freddy!"
    i "Oh no what the hell do we do!!!"
    j "Stay with me little buddy!"
    i "Bert, he's out cold!"
    bi "It can't be a coincidence."
    j "He has a pulse."
    j "But he's starting to sweat like crazy..."
    i "Just a second ago it felt like we were figuring things out."
    i "And now the Freddy's gunna die!?"
    j "Sid! Don't say that!"
    j "We're going to help him."
    bi "I was the chosen killer, wasn't I?"
    i "Bert! Get it together!"
    i "You're smart right? Help the kid!"
    j "Bert, please!"
    j "We need some cold towels, or something!"
    i "Wait a minute..."
    i "Bert..."
    b "I..."
    i "You told him to look between the couch cushions."
    bi "Sid said what I coulnd't bring myself to say."
    i "Did you do this on purpose?!"
    b "I...."
    i "Are you the chosen killer this round, and this is how you're doing it?!"
    i "By drugging a little kid?!"
    i "You sick fuck!"
    j "Sid! We don't know what happened!"
    b "I d-didn't!"
    b "I had no idea those pills were there!"
    i "Yeah, my ass!"
    b "It's true!"
    b "We all came out into the living room together, remember?"
    i "How can I trust that?!"
    b "I..."
    j "Sid!"
    j "We need to help Freddy first!"
    j "We can question Bert afterwards."
    i "Hmph."
    i "Fine. But for now, Bert, go sit over there."
    b "Oka-"
    i "And if you move a muscle..."
    bi "Sid looked me dead in the eyes."
    i "I'll kill you."
    scene black with dissolve
    "Bert sat motionless in the corner."
    "Jenny and Sid cared to Freddy."
    "Only about 5 minutes passed."

    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    show frogsit5 at bg:
        #zoom .85
        xcenter -.05
        ycenter .675
    with dissolve
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    j "Okay..."
    j "We got Freddy to throw up a little, and he has a cold towel."
    j "We don't know how long ago he ate the pill though."
    i "So it could still be in his bloodstream."
    b "Guys..."
    i "I don't want to hear a peep out of you."
    j "Sid, we have to listen to his side of the story."
    j "We don't know if Bert actually meant to do this or if it was an accident."
    i "Who cares if it was an accident?"
    i "If that kid dies, it's on Bert's hands."
    j "Sid!"
    b "No, it's true."
    b "I told Freddy to go looking, and didn't keep an eye on him."
    b "This is my fault."
    i "Hmph."
    b "And that's why I'm going to do everything I can to fix it."
    i "Hm?"
    j "Fix it?"
    b "We can start with these."
    show pillbag with dissolve
    b "The pills."
    i "Why's there a flamingo on them?"
    b "It looks like a flamingo."
    b "But it's not."
    j "Huh? Looks pretty flamingo-ey to me, Bert..."
    b "There's a reason we've gathered so much information."
    b "It's so we can figure things like this out!"
label pent345:
    show scary with dissolve:
        alpha .5
    menu:
        b "The birds on these pills are..."

        "Herons.":
            hide scary with dissolve
            bi "That's it."
            b "The birds are herons."

        "Egrets.":
            bi "Er, I'm surprised I even know that an egret is..."
            jump pent345

        "Cranes.":
            bi "They look like cranes, but that's not it."
            jump pent345

        "Flamingos.":
            bi "I just told Sid they're not flamingos."
            jump pent345

    i "What the hell are you talking about?"
    b "These pills..."
    b "They're some of the drugs Sam sold to Sydell."
    i "How can we know that?"
    b "You were there Sid - think back!"
    $showchibint("dracula", "lauren", "sid", "sam")
    $statusnt("Cafeteria", "bert", ch=3, sun=0)
    scene bg hospcommons at bg
    show sam ind
    show sepia:
        alpha .5
    s "And well, not like I personally knew the guy..." #sam flashback
    s "He didn't even know my name, of course."
    b "He didn't know your name?"
    s "I always dealt under my middle name, Heron."
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    #sam flashback about the name Heron
    #evidence found
    j "Wow..."
    i "Y-you're right, I was there when Sam said that."
    b "Which also means these pills are probably extremely dangerous."
    i "Sam sold super experimental stuff..."
    b "You guys did a great job helping Freddy."
    b "But if he doesn't get to a hospital soon, he could die anyway."
    i "D-do you really think so?"
    b "I do."
    b "And I'm not going to let him die."
    j "Bert..."
    b "Now that we've had time to collect our thoughts, I have something to tell you both."
    b "The truth is, I woke up in the wine cellar with this flashlight."
    show theflashlight with dissolve
    b "It must be a murder weapon, or some other form of advantage."
    b "That's because I think I am the chosen killer for this location."
    i "The chosen killer?"
    j "The same way Kaiser, Catherine, Ivan, and Lauren were."
    i "They were also given an advantage when it was their turn."
    hide theflashlight with dissolve
    j "Bert... why are you telling us that?"
    j "I..."
    j "How can I trust you if I know you're the chosen killer?"
    b "That's exactly why you can trust me!"
    i "Huh?"
    b "The chosen killer can't be the Game Master."
    b "This flashlight proves - to both of you - that I'm not the Game Master!"
    i "Holy..."
    j "So, you're the chosen killer, but..."
    b "I won't kill anyone!"
    b "Being the chosen killer is a blessing in disguise for me."
    b "It means you can both trust me."
    show scary with dissolve:
        alpha .5
    bi "I say they can both trust me, but I know full well I can't trust both of them."
    bi "One of them is the Game Master."
    bi "I just need the other one to cooperate until I can figure it out."
    bi "I have all the information I need..."
    bi "I just need to uncover them!"
    hide scary with dissolve
    i "I know we gotta move quick, but I'm not convinced yet."
    b "What?"
    i "What if you are the Game Master, and you're just cheating in the last round?"
    b "Well, I'm the chosen killer."
    b "I can't be both the chosen killer and the Game Master."
    i "..."
    i "I need more proof you're the chosen killer, and not just the Game Master lying."
    b "Well someone has to be the chosen killer, right?"
    j "Based on everything that's happened so far, yeah."
    b "Was it either of you chosen? Were you given some hint or item?"
    j "..."
    i "..."
    b "Then that should sett-"
    j "It could have been Freddy..."
    j "As crazy as it sounds, Freddy could be the chosen killer."
    j "There's a chance you're just using the fact that he's unconcious for your own gain."
    b "...Jenny, you know I wouldn't do that."
    j "I want to believe it's you, Bert, but we don't have proof it's not Freddy."
    i "Yeah. We need more proof."
    b "More proof?"
    j "Sid's right... there is another little detail missing."
    j "You said you've never been here before, but all the other chosen killer's had some connection to that location."
    i "Yeah!"
    i "You woke up and found a flashlight, so what?"
    i "Before I can trust you again, I need proof that you have a tie to this location."
    b "Proof that I have a tie to this location..."
    b "I don't have that."
    i "Well..."
    i "Figure it out."
    b "Sid..."
    i "I want to trust you, I do."
    i "But I trusted Lauren, too."
    i "I just need... a little more proof that you weren't trying to kill Freddy."
    j "...Bert."
    j "Sid and I will figure out our plan and tend to Freddy."
    j "You should see if there's a way to connect yourself to this location."
    hide jenny
    hide sid
    with dissolve
    show scary with dissolve:
        alpha .5
    bi "Jenny looks visibly scared of me."
    bi "And Sid looked like he wants to kill me a minute ago."
    bi "I guess I can't blame them - if I had meant to poison Freddy, that's..."
    bi "Sickening."
    bi "Regardless..."
    bi "I didn't mean to poison him, and I know I am the chosen killer."
    bi "But how can I prove I'm the chosen killer for this location if I've never been here?"
    bi "..."
    bi "I guess I need to look around."
    bi "Something {i}has{/i} changed, at least a little, since we've been here."
    hide scary with dissolve
    #pick the spot
    bi "..."
    bi "It's been a little while and the sun's coming up."
    bi "It looks like the fog has cleared up since earlier, too."
    #move to window
    scene bg pentview at bg with dissolve
    bi "It looks like rush hour."
    bi "In a vibrant, booming city."
    bi "Kids with their parents, people in a park, families heading out for the day..."
    bi "What a beautiful view, right into the heart of the city."
    bi "..."
    bi "I know exactly where I am."
    bi "This is the most bittersweet moment of my life."
    bi "Do have a tie to this location."
    bi "Because this location..."
label pent35:
    show scary with dissolve:
        alpha .25
    menu:
        bi "This is a view of..."

        "the road I grew up on.":
            bi "No, unfortunately it isn't."
            jump pent35

        "somewhere I've seen in a movie.":
            bi "No, I don't think it is..."
            jump pent35

        "my favorite park as a kid!":
            bi "That's true, but... not what's important here."
            jump pent35

        "where I ran over that lady.":
            hide scary with dissolve
            bi "..."
            bi "That's where it happened."
    bi "That's where I killed that woman."
    bi "I want to throw up just looking at that intersection."
    bi "I've avoided this area since the accident, and to think this is how I'm seeing it again."
    bi "..."
    bi "One other thing makes sense now too."
    show theflashlight with dissolve
    bi "My advantage for this location, the flashlight."
    bi "The flashlight itself isn't the important part."
    bi "it's the back, this solid metal tip."
    bi "These points are made to crack safety glass..."
    bi "I've seen them used in cars before."
    bi "That's why Sid wasn't able to crack the window."
    bi "But with this, and a little force..."
    #cracking noise
    show scary with dissolve
    #broken glass

    bi "At least I can prove it now."
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=0)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    i "Bert?! What the hell?!"
    j "Are you okay?!"
    i "How did the window break? I couldn't even leave a scratch..."
    b "It's the flashlight."
    b "It wasn't about being a flashlight, it was about the safety glass breaker."
    b "That advantage let's me break the window, and then..."
    bi "Well..."
    i "Is that your connection to this location? Being able to break the glass?"
    b "No, that was just my advantage."
    b "I did find a connection to the location."
    b "This is the scene of my crime."
    j "You ran someone over in this apartment?"
    b "No, I ran someone over on the road, down there."
    i "And you just noticed now?"
    b "Well, it was dark and foggy - you weren't able to tell where we were either."
    i "That's true..."
    b "But now that I know where we are, I could tell you anything about the area."
    b "It's burned into my mind, every store, every street sign, every crosswalk."
    b "Between that and my getting the flashlight, I hope that's enough proof for you both."
    i "..."
    j "I believe you, Bert."
    j "You're the chosen killer for the location, like you said."
    j "And you didn't intentionally poison Freddy."
    i "Yeah, alright, same."
    b "Thank you, both of you."
    bi "One of them has known this whole time."
    i "Let's get back to it then."
    j "Bert, you made it sound like you had a plan to figure out who the Game Master is."
    b "I do."
    b "And it's one of you two."
    i "..."
    j "..."
    j "Not it..."
    #sid point
    i "HEY! THAT'S NOT HOW IT WORKS!"
    i "Bert said he has a plan, so we need to help him!"
    j "Yeah! And Sid, if you don't cooperate, we'll know you're the Game Master."
    i "I'm not the Game Master! You must be!"
    j "We'll see about that, Sid."

    ###implanted


    b "We don't have time to bicker. Freddy needs treatment."
    b "So we're going to settle everything, right here and now."
    b "We're going to end this game - WIN this game."
    j "How can we do that?"
    b "We've collected data about almost everyone involved in the game from this location."
    b "Dan."
    b "Kaiser."
    b "Setlla."
    b "Catherine."
    b "Shahar."
    b "Ivan."
    b "Sam."
    b "Lauren."
    b "Freddy..."
    b "And the three of us."
    b "One of us is the Game Master"
    b "No, one of you two."
    b "I've proven that it can't be me."

    j "..."
    i "..."


    ###implanted
    b "So, both of you."
    b "I need you to tell me your backgrounds again."
    b "Then tell me about your crimes, and any prior connections with anyone from the game."
    b "And finally, any connections you made during the game."
    b "... This is it."
    b "So tell me everything."
    b "Sid, you first."
    #transition to background screen and only one character
    i "Okay, yeah."
    i "I'm Sid Straits!"
    i "I'm 17 and was finishing high school before all this."
    i "I was a little bit of a trouble maker, but not a slacker!"
    i "I was helping my parents run the store, and learning about computers on the side."
    i "We were pretty poor."
    i "For extra money, I did a little hacking..."
    i "That's how I got caught up with Shahar."
    i "Not directly, I didn't know the guy, but there was some lawsuits and blackmail going on."
    i "Stella as involved, and Dracul-er, Ivan, knew about some of it."
    i "I... wish I could undo it all, take it all back."
    i "I just wanted to make sure my family was making enough money."
    i "When this whole game started, I knew that's why I was involved, though I didn't know the details."
    i "..."
    i "I appreciated Dan."
    i "We know his past now, and he wasn't an amazing guy, but..."
    i "That doesn't change the way he talked to me, or respected me."
    i "He was manly, headstrong, protective."
    i "We only knew him for a few days, but it was hard to really connect with anyone else here after he died."
    i "I guess... that's it."
    hide sid with dissolve
    b "Now Jenny."
    show jenny ind with dissolve
    j "Well, from the top I guess."
    j "I'm Jenny Flowers, 20 year old college student."
    j "I come from a pretty normal middle-class family."
    j "It feels like so long ago..."
    j "I've always politically active, just doing what I can, and got arrested protesting about Freddy's father."
    j "It didn't lead to much at the time, but it's my connection to Freddy for this game."
    j "I... stand by what I did."
    j "Freddy's a good kid, but his father is a horrible man."
    j "As for connections I made during the game..."
    j "Well, I think you and I get along really well, Bert."
    j "I know you have to question both Sid and I, I get it."
    j "But you're the first person here I told about my arrest."
    j "And I was the first person you told about the woman you hit."
    j "I don't know, maybe I'm being foolish, but it's felt like there's... something here."
    j "I guess... that's it."
    #transition back to both of them in real time.
    b "..."
    b "I know who the Game Master is."
    b "Between all the murders, investigations, clues we found here, and your stories..."
    b "There's only one thing that doesn't add up."
    b "One thing that tells me who the Game Master has to be."
    b "For Freddy's sake, we have to act now."
    b "So."
    b "The Game Master is..."
    #lineup 2 people "Who is the Game Master?"
        #show sid in void again
    b "Sid."
    b "We talked about the last name hint, but it's been weighing on me."
    b "All the rules the Game Master left have been accurate so far, and I think that one is too."
    b "Anyone could be lying about their last name, but both your names definitely starts with an S."

    #show jenny in void agian
    b "Jenny."
    b "It's true that we were close."
    b "I'll never know if that was real or not."
    b "Because you're the Game Master, and you die here."
    j "Bert, are you being serious?"
    b "There's no way I could be the Game Master."
    b "I've been thinking about it a lot:"
    b "Every time I brought up my car accident, I never mentioned the victim's gender."
    b "It wasn't a trap, it's just hard to get into the details."
    b "But you... a minute ago, said that it was a woman."
    j "Bert..."
    b "And you were right."
    b "It was a woman, I killed a woman."
    b "And based on everything we know now, I think that woman was..."
    b "Mrs. Sydell - your mother!"
    b "It's the only explanation for why I'm here..."
    b "This whole time... you've been Sydell's daughter."
    b 'This "Flowers" name, it must be your mother\'s maiden name.'
    b "Which would explain the hint in the bank - your last name starts with S, for Sydell."


    #PERSON BERT HIT, NOT WOMAN!!! JENNY WILL SAY ITS A WOMAN




    ############################################
    if not pent_evidence[0]:
        $pent_evidence[0] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "__________ was added to evidence."
