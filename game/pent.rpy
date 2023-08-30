label pentGo:
    $ftecounter = 11
    #$ftecounter = 2
    #$noside = True
    #camera at paralloff
    $noside = True
    $dan = False
    camera at paralloff
    scene black
    pause 1.0
    show screen killuser
    play sound "<from 0.1 to 12.2>audio/welcome.mp3"
    $renpy.movie_cutscene("ch5trailer.webm")
    hide screen killuser
    $ statusnt("???", "", ch=5, sun=0)
    show bg flashback with dissolve
    #$ statusnt("???", "", ch=3, sun=0)
    $mood = "ind"
    play music "audio/ominous.mp3" fadein 1.0
    "A few years ago..."#febmusic
    "..."
    sy "Full custody?"
    sy "Are you kidding me?"
    sy "We're not even divorced! You're out of your mind!"
    "..."
    sy "I know I'm not around enough, alright, I've got a lot of work shit to deal with."
    sy "But Rose is in even worse shape than I am..."
    sy "We're both at the end of our ropes, you gotta understand."
    sy "Convincing her to leave me isn't what's best for-"
    "..."
    sy "This case is gunna go our way, and-"
    "..."
    sy "She told you about the pills?"
    "..."
    sy "Look, I know things look rough right now, but-"
    "..."
    sy "Screw you asshole! You're not tearing apart my family!"
    stop music fadeout 3.0


    scene bg reflecting with dissolve
    $cat = False
    play music "audio/ominous.mp3" fadein 1.0
    "In the present..."
    $noside = False
    $mood = "sad"
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
    $mood = "ind"
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
    hide frog2
    hide jenny
    hide sid
    with dissolve
    bi "We also have the hint from the vault."
    bi '"The Secret of the Game", as it said.'
    call popwowb
    bi "The Game Master's name starting with the letter 'S'."
    bi "At least getting knocked out gives me a moment to think about it."
    bi "I'm not sure if we can trust it, but we definitely can't ignore it."
    bi "If we count first and last names..."
    show lineupletters with dissolve
    bi "There are five people that fit the description."
    bi "Dan Scagnelli, Sam Lee, Shahar Syed, Sid Straits, and Stella Cantoire."
    bi "It seems like a lot, but only one of them is still alive."
    hide lineupletters
    show lineupletters15
    with dissolve
    bi "Sid."
    bi "I just said I wanted to trust him, but it's hard not to take this into account."
    bi "He fits the hint description perfectly."
    bi "Both of his names start with the letter 'S'."
    bi "The other alternative is that people lied about their names."
    bi "Accounting for Freddy, whose full name we can confirm, and myself, we have..."
    hide lineupletters15
    show lineupletters2
    with dissolve
    $mood = "sad"
    bi "Ten people whose names {i}could{/i} start with the letter 'S'."
    bi "It's not unreasonable to think even an innocent person would lie about their name."
    bi "Especially given the circumstances."
    bi "Out of everyone, the most important liar would be Jenny, who's still alive."
    call pophuhb
    bi "Is Jenny lying about her name?"
    bi "I have no way of knowing."
    hide lineupletters2
    with dissolve

    bi "I don't know what to think."
    bi "I want to find a way to save them all, but if one of them's the Game Master..."
    bi "Is it even possible to save everyone?"
    call poptearb
    bi "Jenny? Freddy? Sid?"
    $mood = "ind"
    bi "...No matter what, I have to try."
    bi "I'm going to figure everything out, and save us."
    bi "There's no time to waste, so I need to start collecting evidence as soon as possible."
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
    $ statusnt("???", "bert", ch=5, sun=0)
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
    call pophuhb
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
    bi "Sigh."
    bi "For now, I'll hang on to this flashlight."
    "Bert put the flashlight in his backpack."
    $mood = "ind"
    bi "Alright."
    b "Time to go find everyone else, Sesame."
    ses "Mep."
    scene black with dissolve
    "Bert went up the ladder and opened the hatch."
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
    $ statusnt("Bedroom", "bert", ch=5, sun=1)
    bi "And the other 3 are here and still asleep."
    i "snnnnnnnnnnnnnnnnnnnnnnnn......."
    b "Hey guys, wake up."
    f "mimimimimimimi....................."
    bi "..."
    call popwowb
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
    $popx = .7
    call popheartso
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
    $mood = "sad"
    j "Come on, he's just a kid."
    j "Lauren just died too, and you know that he really liked her."
    b "Okay... as long as he's in the room with us."
    b "Last thing we need now is for something to happen to Freddy."
label pent2:
    scene black with dissolve
    $mood = "ind"
    "They shook Sid awake."
    scene bg pentbedroom2 at bg
    $ statusnt("Bedroom", "bert", ch=5, sun=1)
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
    show sid mad
    i "It's you guys again!"
    b "Who else would it be?"
    i "Uh, I don't know!"
    i "I can't believe Lauren did Sam in like that."
    i "I can't trust anyone these days."
    call popwowb
    b "Speaking of which, it should be pretty easy for us to narrow down our {i}roles{/i} now."
    i 'What do you mean our "roles"?'
    $mood = "sad"
    b "Well, unless we've been lied to this whole time, one of us is the Game Master."
    b "And another one of us is the chosen killer for this location."
    $mood = "ind"
    show scary with dissolve:
        alpha .5
    bi "I'll tell them about the flashlight and the cellar in a minute, but..."
    bi "No need to play my hand too early."
    bi "If one of them comes forward saying THEY'RE the chosen killer, then, well..."
    bi "We'd have an interesting scenario."
    hide scary with dissolve
    j "So, two out of the four of us have some predetermined role."
    b "Right."
    show jenny happy
    $popx = .3
    call popheartso
    j "Great logic guys!"
    j "So who's who?"
    j "Speak up now or forever hold your peace!"
    b "..."
    i "Well don't look at me!"
    j "C'mon Sid, you can admit it, I'll forgive you!"
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .65
        ycenter .275
        zoom .75
    i "If I really was the Game Master, you shouldn't forgive me!"
    i "You should be tying me to the bedframe!"
    j "Oh? Sid..."
    i "THAT'S NOT WHAT I meant!!!"
    i "AND I'M NOT THE GAME MASTER ANYWAY"
    j "Sure thing, Sid Straits with two S's."
    $mood = "sad"
    bi "This went a bit more smoothly in my head..."
    hide poptear
    bi "Plus, I've been avoiding the fact that Freddy could technically be either role..."
    show sid ind
    $mood = "ind"
    b "Alright, alright."
    b "Nevermind what I said about the roles for now."
    b "We just got here, anyway."
    b "We need to explore this place before the chosen killer knows that's their role."
    b "If one of us does have a connection to this location, we need to scope it out a bit first."
    bi "It would let me figure out why they gave me this flashlight, too..."
    i "Yeah, I haven't even been outside this frou-frou bedroom yet."
    j "There are two doors out of here, which way first Baptain?"
    b "Baptain?"
    j "Ya know, like, Captain but with a B for Bert!"
    b "..."
    b "Let's just go out the east door."
    j "Aye Aye, captain Bert!"
    b "Everyone sounds like Shahar now..."
    scene black with dissolve
    $noside = True
    "The four of them went into the next room together."
    $noside = False
    scene bg pentstudy at bg
    $ statusnt("???", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    b "Wow..."
    b "This looks like a personal library, or a study."
    $ statusnt("Study", "bert", ch=5, sun=1)
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
    $popx = .3
    call popheartso
    j "Ahh, I could get used to this."
    b "We're not here to get used to this..."
    b "We should each look for anything that could connect us to this place."
    j "I'm pretty connected to being warm and cozy, so..."
    i "Looks like there's some booze too!"
    $mood = "sad"
    call poptearb
    b "Please... work with me here."
    b "We also want to look for anything tied to Sydell, or anyone who died before us."
    $mood = "ind"
    i "Yeah you're right."
    i "Well I've definitely never been here before."
    i "The only library I've been to is the public one near me, definitely nothing fancy like this."
    b "Me too... I have no memory of this place."
    b "It seems like a personal library for someone."
    j "Well, let's look around!"
    j "Maybe there are some clues for us!"
    hide jenny
    hide sid
    with dissolve
    "They spent a few minutes looking around the room."
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
    $ statusnt("Study", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show jenny happy:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    j "Oh wow! Great memory, guys."
    j "Did someone move it here?"
    $popx = .67
    call popwowo
    i "Nah, that one was way bigger."
    i 'I remember thinking "damn, is that the original?" and Stella called me stupid.'
    i "I doubt this is the original either."
    bi "I think the original is in England somewhere."
    b "I don't think it's a coincidence that the same painting is here."
    b "The decor in general is pretty similar too."
    b "There's definitely some connection to Mr. Sydell's mansion."
    j "I found something too."
    j "Everything is neat and all the books are back up on the shelves, but..."
    j "This book specifically was tucked into one of the couch cushions."
    j "It was open to this page."
    show bg journal1 at bg
    hide jenny
    hide sid
    with dissolve
    $mood = "shock"
    b "It looks like..."
    b "A journal?"
    b "This is definitely someone's handwriting."
    b "It says..."
    b '"Taking refuge in a rented penthouse..."'
    b '"this is not sustainable. But where else can I go?"'
    b '"They know where I live. I fear my days as well are numbered."'
    b '"Unless... I can turn the tables."'
    call popwowb
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
    call poptearo
    i "A little spooky."
    b "Does anyone know the handwriting?"
    b "Or know whose this might be?"
    bi "Nobody spoke up."
    hide sid happy with moveoutright
    show frog2 ind with moveinright:
        xcenter .7
    f "Is there anything else written in the book?"
    b "That's a great question, Freddy."
    bi "I thumbed through the previous pages."
    bi "There's a lot of random notes, scribbles, and some stuff in another language."
    bi "At a glance, I'm not sure how useful the rest of the journal will be."
    f "So whose is it, Bert?"
    f "I thought you're always supposed to write your name at the top of the page."
    j "Mhm, mhm. It's true."
    b "I don't think they were in the right headspace to be doing that."
    b "Still, there might be a way we can use this..."
    b "There was one criminal with us who knew where someone seemingly important lived."
    show scary with dissolve:
        alpha .5
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

    b "I'm pretty convinced about something..."
    hide frog2 with moveoutright
    show sid ind with moveinright:
        xcenter .7
    i "About what?"
    call popwowb
    b "That we should... assume this is Mr. Sydell's journal."
    b "Think about it - it seems like almost all of us have some connection to Sydell."
    b "Not to mention the decor, and the painting above the fireplace."
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
    $ statusnt("Study", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    b "She didn't know Sydell, but she knew where he lived."
    b 'That fits with what the journal says.'
    b 'Maybe he was scared Catherine, or someone else, would come back.'
    b "So he came here to take refuge."
    j "Wow, Bert, you might be right."
    j "Between the painting, the furniture, and the book, I think you're onto something."
    i "So we're in Sydell's secret apartment?"
    b "That's my best guess so far..."
    $popx = .67
    call pophuho
    i "I don't get it though - didn't Catherine just rob him?"
    i 'Why\'s he talking all like "my days as well are numbered"?'
    i "I dunno, I've been robbed before, and it's scary, but renting a place like this to hide seems like... overkill."
    j 'Also, why "as well"?'
    j "Doesn't that imply someone had already died?"
    $mood = "sad"
    b "Maybe someone close to Sydell had been murdered."
    b 'That would explain him saying "as well".'
    b "Then, when Catherine robbed his empty house, he thought he was next to die."
    i "Yeah, I guess that tracks."
    i "He got spooked and came here."
    show scary with dissolve:
        alpha .5
    $mood = "sad"
    bi "Even if this is true, it brings up even more questions..."
    bi "Why had someone died, and who was it?"
    bi "What were Sydell and that person doing to end up in this situation?"
    bi "And lastly, how does this connect to our situation?"
    hide scary with dissolve
    b "One step forward, one step back..."
    $popx = .33
    call popwowo
    j "Bert, take a look at this!"
    b "Hm? What's is it?"
    j "There's a little slip of paper tucked in a different page."
    show bg journal2 at bg
    hide jenny
    hide sid
    with dissolve
    $mood = shock
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
    call popwowb
    b "That's it!"
    show scary with dissolve:
        alpha .5
label pent26:
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
    $ statusnt("Study", "bert", ch=5, sun=0)
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
    $ statusnt("Study", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    i "What?!"
    i "So this is... Dan's number?"
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .7
        ycenter .1
    i "Dan..."
    bi "I'd forgotten how quickly Sid grew attached to Dan."
    bi "Something about a strong male figure to look up to, I suppose."
    b "Given Dan's mannerisms, attitude, and the details we knew about his history..."
    b "I'm not shocked to see he was tied up in all this."
    $popx = .3
    call popmado
    j "Bert!"
    bi "Jenny gave me a look, I don't think she wanted me badmouthing Dan in front of Sid."
    hide poprain with dissolve
    i "He's right..."
    i "One of the last things Dan said to me was about his criminal history."
    j "Oh... I see..."
    i "Dan was kind to me, but there's no reason to dance around his shady past."
    i "I appreciated his support for me on the train."
    i "I think without him, I would have started to go insane..."
    j "Sid..."
    show sid happy
    i "And he hinted toward his past to me, yeah."
    i "It seemed pretty clear he didn't think highly of himself."
    i "But... I think people can change, and I know I thought highly of Dan."
    i "I still do, regardless of his involvement here."
    bi "Every once in a while, Sid proves to me that he really is maturing..."
    $popx = .67
    call pophuho
    b "Still... why is his phone number in a place like this?"
    b "It seems like Sydell was in a position to call in a favor."
    j "That would make sense, if he was scared of Catherine and the lawyers after him."
    j "Maybe Sydell needed a bodygaurd, or-"
    call popwowo
    $mood = "shock"
    i "A hitman..."
    b "Sid, you're a genius."
    i "Huh?"
    b "If Sid was a hitman, everything would start to make sense."
    j "What do you mean? What would make sense?"
    $mood = "ind"
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

        "Her bodyguards had sent hitmen back to kill their bosses before.":
            hide scary with dissolve
            bi "I remember it clearly now!"

        "She knew it was Sydell's masion right away.":
            bi "She did say that... but that's not relevant at the moment."
            #hide scary with dissolve
            jump pent27
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
    $ statusnt("Study", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with fade
    i "So you think..."
    i "Sydell, scared for his life, called in Dan as a hitman..."
    j "...Ordered Dan to go kill Stella..."
    b "...And then Stella's bodyguards caught Dan, and made him kill Sydell."
    i "Would this guy really call a hit on Stella Cantoire over a lawsuit?"
    b "Well, he also seemed pretty shook up by Catherine's break in, given the journal entry."
    b "Plus, Sam made it sound like the guy was really going through it on all fronts..."
    i "Hmm... okay, so he's at the end of his rope, scared, pissin' his pants, hiding here."
    i "Calls in Dan, which backfires."
    i "That could only mean one thing right?"
    $mood = "shock"
    i "Sydell is dead."
    b "We can't be sure he's dead..."
    j "But if Stella's team knew about a hitman out for her head, I'm sure they'd counterattack."
    j "Whether it was her own guards, or Dan, I'd imagine Sydell was killed one way or another..."
    b "..."
    $mood = "ind"
    bi "We were all silent for a moment."
    b "You're probably right..." #ev
    b "It's just weird to think that this guy, Mr. Sydell, who seemed like the connection between us all..."
    b "Has been dead this whole time?"
    b "For years, even?"
    $popmood = .33
    call poptearo
    j "Wait..."
    show jenny scared:
        linear .2 xcenter .25
    j "Does that mean one of you three is really behind all this?"
    j "I was still holding out hope that... some bald old freak named Sydell was behind it all."
    j "But if he's been dead this whole time, then there's no way..."
    $mood = "sad"
    bi "One of us is behind all this..."
    bi "She's probably right."
    bi "But I don't want to accept that just yet."
    $mood = "ind"
    b "Let's keep exploring before we get too depressed about it."
    i "Agreed!"
    hide sid
    hide jenny
    with moveoutleft
    scene black with dissolve
    "All four of them made their way back through the other bedroom door."
label pent29:
    scene bg pentkitchen2 at bg
    $ statusnt("???", "bert", ch=5, sun=1)
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
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    b "Both, I think."
    j "Gotta love an open floorplan."
    bi "She's pretty quickly back in high spirits..."
    j "It looks like we're... really high up?"
    $popx = .67
    call popwowo
    i "Holy shit, those are windows!"
    bi "He's right..."
    bi "This is the first time since the train we've seen windows that aren't boarded up."
    i "Gang, we're makin' a jump for it!"
    hide sid with moveoutbottom
    show sidstand2 at bg with dissolve:
        xcenter .48
        ycenter .53
    "Sid ran over to the windows."
    call popwowb
    $mood = "shock"
    b "Hold on!"
    i "We can break through the glass and jump for it!"
    play sound "audio/windowknock2.mp3"
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
    $ statusnt("Dining Room", "bert", ch=5, sun=4)
    $ showchibint("freddy", "jenny", "sid")
    with dissolve
    b "..."
    $mood = "ind"
    b "It really is a window to the outside world..."
    bi "I can see a couple cars, and even some people walking..."
    bi "But... it's so foggy, and it must be the absolute middle of the night."
    bi "Still, it feels nice to know there are some other people out there."
    bi "For a moment, it feels almost peaceful."
    bi "I haven't seen a view like this in-"
    play sound "audio/windowknock2.mp3"
    "{i}BAM BAM BAM!{/i}"
    $mood = "shock"
    b "Sid! Stop hitting the windows!"
    scene bg pentkitchen2 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=0)
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
    play sound "audio/windowknock2.mp3"
    "{i}WHACK WHACK WHACK!{/i}"
    j "Well don't keep trying!"
    play sound "audio/windowknock2.mp3"
    "{i}WHACK WHACK WHACK!{/i}"
    play sound "audio/windowknock2.mp3"
    "{i}WHACK WHACK WHACK WHACK WHACK WHACK!{/i}"
    play sound "audio/windowknock2.mp3"
    play sound "audio/windowknock2.mp3"
    "{i}WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK WHACK!{/i}"
    b "..."
    $mood = "ind"
    call poptearb
    b "...I think it's fine."
    b "It doesn't seem like the window is going to break."
    j "If he falls out the window, I'm blaming you."
    hide sidstand2 with dissolve
    show sid ind with moveinbottom:
        xcenter .7
    i "I think the windows are safety glass or something fancy."
    $popx = .67
    call poptearo
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
    call pophuho
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
    $mood = "sad"
    i "I still think we should try to jump for it."
    i "If we had known what was going to happen on the train, I woulda jumped there too!"
    b "That's... understandable."
    $mood = "ind"
    b "Sid, let's look around for a bit."
    b "If we don't find anything useful, maybe we can rig something to climb down from the window."
    b "If we can even get it open..."
    i "Alright, deal."
    j "There are lots of drawers, cabinets, and tables in here."
    hide jenny with moveoutleft
    show frog2 ind with moveinleft:
        xcenter .3
    f "What should I do to help!"
    b "Ummm..."
    $popx = .3
    call popheartso
    b "You can have the most important job."
    f "Really!!!"
    b "Yup! We need someone to look between all the couch cushions!"
    show frog2 smile
    call popheartso
    f "Oh boy!"
    bi "Maybe that will distract him for a bit."
    b "Make sure you don't miss anything, Freddy!"
    f "Aye aye, sir!"
    bi "Why's everyone saying that now..."
    b "Okay, let's get started."
    scene black with dissolve
    "The four of them spent 30 minutes scavenging every corner of the room."
    scene bg pentkitchen90 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    b "While we have this time, maybe I should chat with someone to calm the nerves."
    b "It's a scary situation, but we need camaraderie."
    if fte_jenn >= 3 and fte_frog >= 3 and fte_sid >= 3:
        scene black with dissolve
        bi "I spent some time chatting with the others while searching."
        jump postFT11
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    play music "audio/cobwebs.mp3" fadein 2.0
    call screen pentDining with fade
label postFT11:
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    $mood = "ind"
    j "Okay team!"
    j "Despite a lot of places to hide stuff in here, it doesn't seem like there's a lot hidden."
    i "I can't believe we're tearing apart a rich guy's penthouse and there's no money laying around."
    $mood = "sad"
    call poptearb
    i "Leave me a little cash bro come on..."
    j "He {i}was{/i} rich."
    j "By the time he was hiding here, he was losing money and in some business troubles, remember?"
    i "Yeah, true."
    $mood = "ind"
    b "Well speaking of business, Jennny did find this folder labeled \"InSyde Electronics\"."
    b "Stella told us that that was the name of Sydell's company, so maybe there's something useful in here."
    j "I took a peek inside and it looked useful, so I set it aside for us to read through."
    b "Let's see..."
    b "W2... receipts... shipping documents..."
    call popwowb
    $mood = "shock"
    b "Woah!"
    i "What is it?!"
    b "Look, look!"
    b "There's something about an insurance claim!"
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter .33
        ycenter .275
        zoom .75
    j "That doesn't sound exciting..."
    b "Just take a look."
    hide poptear
    i "Huh, the page is torn in half."
    show scary:
        alpha .5
    show sydellfile
    with dissolve
    bi "..."
    i '"Stewart Sydell?"'
    i "Bro's first name is Stewart?"
    $mood = "ind"
    b "Come on, keep reading."
    j "It's about InSyde Electronics, his business."
    i "It says..."
    i "{i}This letter serves as a rejection for coverage of claim #092523...{/i}"
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
    hide sydellfile
    hide scary
    with dissolve
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
    b "{i}To whom it may concern, InSyde Electronics{/i}."
    b "It's not directly addressed to Mr. Sydell."
    j "If this was about a home break-in, I guess it wouldn't say that."
    hide sydellfile
    with dissolve
    b "Right, it would just be addressed to him, or a family memeber."
    show jenny happy
    $popx = .3
    call popheartso
    j "Good catch Bert!"
    i "But wait, if it's not about Catherine robbing him, is this even useful?"
    i "Who cares about some random insurance claim against his company?"
    b "..."
    j "Sid, you're pretty nonchalant about his considering it could be about you!"
    show sid mad
    i "Hey! I didn't steal from him!"
    i "I hacked him, and planted information."
    $mood = "sad"
    i "If anything, I left him with more than when I started!"
    b "..."
    $mood = "ind"
    b "Ignoring that last comment, Sid is right."
    b "He never robbed InSyde, or Sydell himself, so this isn't about him."
    $popx = .65
    call popwowo
    i "YEAH!"
    b "But he's wrong about this being useless."
    b "There's one more piece of information we can use to tie this to us."
    j "Let me see, let me see!"
    j "I want to figure it out."
    b "I'm sure you can."
    i "Me too! Hype me up man."
    b "Uhh, go Sid go."
    show sid ind
    "They looked over the document again."
    j "..."
    i "....."
    j "........"
    $popx = .35
    call popwowo
    i "I got it!"
    j "It's the date, August 6th!"
    i "That's what I was going to say!"
    i "Wait, what? The date?"
    j "It says the claim was filed on August 6th, that's useful!"
    i "Umm yeah, that's what I was going to say too..."
    b "..."
    b "Jenny's right - we can tie someone's crime to that date."
    i "I don't know any of the dates that people's crimes happened on..."
    show jenny ind
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
    #$ statusnt("Front Car", "bert", ch=1, sun=4)
    show doom
    with dissolve
    show kaiser ind:
        xcenter .7
    show sid ind:
        xcenter .25
    show sepia:
        alpha .5
    with dissolve
    k "And then... this car."
    k "It reminds me of one heist in particular, my most famous heist."
    k "I'll never forget the day, down to the most minute details."
    k "It was the coldest August 5th I've ever experienced, and one that changed my life."  #febreview
    k "It was going to be my big break... and for a while, I thought it was."
    k "How naive of me..."

    scene bg pentkitchen80 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show jenny ind:
        xcenter .3
    show sid ind:
        xcenter .7
    with dissolve
    b "Kaiser's heist was on August 5th, which is one day before the claim was made."
    i "So Kaiser's crime impacted Sydell, who then filed an insurance claim the next day..."
    j "And then that claim got shot down, leaving Sydell in the red."
    b "I think that's it, yes."
    b 'It would also explain what this form means about the "nature of the theft".'
    b "A train heist seems like an unusual thing to file for."
    j "Which probably made it easy for the insurance company to reject."
    play sfx "audio/poprain.mp3" volume .5
    show poprain with dissolve:
        xcenter .7
        ycenter .1
    i "Man..."
    i "I mean, I hate that guy right, but damn."
    i "He really went through a lot at the end there."
    j "Yeah..."
    i "Robbed by Catherine and Kaiser, on Sam's sketchy drugs, crushed by Stella's firm..."
    hide poprain with dissolve
    b "And probably even more that we haven't uncovered yet."
    j "He's why we're here though! Right?"
    j "I can't feel bad for someone like that."
    i "Tr-true..."
    show scary with dissolve:
        alpha .5
    b "It's true we're learning a lot about Sydell right now."
    b "And there's no doubt he's somehow in the middle of this whole thing."
    b "But... if he really is dead..."
    $mood = "sad"
    b "Which one of them is the Game Master, and how can I prove it?"
    b "And why haven't I found anything else here to link me to this location?"
    b "If I really am the chosen killer here, shouldn't it feel more... obvious?"

    show frog2 ind:
        xcenter .5
    show jenny ind:
        linear .2 xcenter .25
    show sid ind:
        linear .2 xcenter .75
    with moveinbottom
    f "Jenny, look what I found!"
    f "Some candy!"
    j "Huh?"
    $mood = "shock"
    call popwowb
    show jenny scared
    b "Freddy! Gimme those!"
    show frog2 sad
    bi "These are not candy..."
    show pillbag with dissolve
    b "These are..."
    j "Drugs!?"
    i "Party pills, the kids at my school call those..."
    b "The pills are small and colorful, and this type of bag doesn't make it look like candy."
    hide pillbag with dissolve
    $popx = .28
    call pophuho
    j "Freddy! Where did you find these?"
    f "It was tucked away between the couch cushions."
    bi "I can't believe that distraction actually lead to finding something."
    f "So can I have them or not?"
    b "Absolutely not. These aren't for kids."
    $popx = .47
    call poptearo
    f "What about just one?"
    j "Freddy, they could make you really sick."
    f "Uh oh, really?"
    j 'Why "uh oh" Freddy?'
    b 'Yeah why "uh oh"?'
    f "Errrrmmmmmmmm..."
    play music "audio/unity.mp3" fadein 1.0
    f "I may have already eaten one..."
    call popwowb
    b "What?!"
    f "Well they look so yummy!"
    f "But they don't really have much flavor."
    bi "If these really are drugs, the effect will start kicking in soon."
    bi "And for a kid his size, it could cause serious damage."
    b "Freddy... how long ago did you eat the first one..."
    f "Erm..."
    hide frog2 with moveoutbottom
    "Freddy fell to the ground."
    j "Freddy!"
    i "Oh no what the hell do we do!!!"
    hide jenny with moveoutbottom
    j "Stay with me little buddy!"
    i "Bert, he's out cold!"
    bi "It can't be a coincidence."
    j "He has a pulse."
    j "But he's starting to sweat like crazy..."
    i "Just a second ago it felt like we were figuring things out."
    i "And now the Freddy's gunna die!?"
    j "Sid! Don't say that!"
    j "We're going to help him."
    $mood = "sad"
    bi "I was the chosen killer, wasn't I?"
    i "Bert! Get it together!"
    i "You're smart right? Help the kid!"
    j "Bert, please!"
    j "We need some cold towels, or something!"
    i "Wait a minute..."
    i "Bert..."
    b "I..."
    $mood = "shock"
    show sid mad
    i "You told him to look between the couch cushions."
    $popx = .7
    call popwowo
    i "Did you do this on purpose?!"
    b "I...."
    i "Are you the chosen killer this round, and this is how you're doing it?!"
    i "By drugging a little kid?!"
    i "You sick fuck!"
    show jenny scared with moveinbottom:
        xcenter .3
    j "Sid! We don't know what happened!"
    b "I d-didn't!"
    b "I had no idea those pills were there!"
    call popwowo
    i "Yeah, my ass!"
    b "It's true!"
    b "We all came out into the living room together, remember?"
    i "How can I trust that?!"
    b "I..."
    j "Sid!"
    j "We need to help Freddy first!"
    j "We can question Bert afterwards."
    i "Hmph."
    i "Fine! But for now, Bert, go sit over there."
    b "Oka-"
    i "And if you move a muscle..."
    bi "Sid looked me dead in the eyes."
    $popx = .75
    call popmado
    i "I'll kill you."
    scene black with dissolve
    stop music fadeout 1.0

    "Bert sat motionless in the corner."
    hide popmad
    "Jenny and Sid cared to Freddy."
    "Only about 5 minutes passed."

    scene bg pentkitchen70 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
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
    $mood = "sad"
    j "Okay..."
    j "We got Freddy to throw up a little, and he has a cold towel."
    j "We don't know how long ago he ate the pill though."
    i "So it could still be in his bloodstream."
    call poptearb
    b "Guys..."
    i "I don't want to hear a peep out of you."
    j "Sid, we have to listen to his side of the story."
    j "We don't know if Bert actually meant to do this or if it was an accident."
    show sid mad
    i "Who cares if it was an accident?"
    i "If that kid dies, it's on Bert's hands."
    j "Sid!"
    $mood = "ind"
    b "No, it's true."
    b "I told Freddy to go looking, and didn't keep an eye on him."
    b "This is my fault."
    b "If Freddy does die, I'm the one who killed him."
    i "You..."
    play music "audio/inthefaceofdeath.mp3"
    call popwowb
    b "And that's why I'm going to do everything I can to fix it!"
    show sid ind
    i "Hm?"
    j "Fix it?"
    b "We can start with these."
    show pillbag with dissolve
    b "The pills."
    i "Why's there a flamingo on them?"
    b "It looks like a flamingo."
    b "But it's not."
    j "Huh? Looks pretty flamingo-ey to me, Bert..."
    $mood = "ind"
    b "There's a reason we've gathered so much information."
    b "It's so we can figure things like this out!"
    b "We know more about these pills than we might think."
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
    call popwowb
    b "They're some of the drugs Sam sold to Sydell."
    i "How can we know that?"
    b "You were there Sid - think back!"
    $showchibint("dracula", "lauren", "sid", "sam")
    $statusnt("Cafeteria", "bert", ch=3, sun=0)
    scene bg hospcommons at bg
    show sam ind
    show sepia:
        alpha .5
    with dissolve
    s "And well, not like I personally knew the guy..." #sam flashback
    s "He didn't even know my name, of course."
    b "He didn't know your name?"
    s "I always dealt under my middle name, Heron."
    scene bg pentkitchen55 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
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
    #sam flashback about the name Heron
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve

    j "Wow..."
    i "Y-you're right, I was there when Sam said that."
    b "Which also means these pills are probably extremely dangerous."
    i "Sam sold super experimental stuff..."
    b "You guys did a great job helping Freddy."
    b "But if he doesn't get to a hospital soon, he could die anyway."
    $popx = .67
    call poptearo
    i "D-do you really think so?"
    b "I do."
    b "And I'm not going to let him die."
    j "Bert..."
    show scary with dissolve:
        alpha .5
    bi "I'm acting strong to take command, and stop them from thinking this was intentional, but..."
    bi "Everything I'm saying is true, Freddy could die."
    bi "And I can't have a little kid die on my hands."
    bi "I need to tell them everything."
    bi "Even if it makes me look worse, and even if I don't have it all figured out yet."
    hide scary with dissolve

    b "Now that we've had time to collect our thoughts, I have something to tell you both."
    call popwowb
    b "The truth is, I woke up in the wine cellar with this flashlight."
    show theflashlight with dissolve
    b "I don't know why it a flashlight, but..."
    b "It must be a murder weapon, or some other form of advantage."
    hide theflashlight with dissolve
    stop music fadeout 1.0
    b "That's because I think I am the chosen killer for this location."
    show jenny scared
    show sid happy
    i "The chosen killer?"
    j "The same way Kaiser, Catherine, Ivan, and Lauren were."
    i "They were also given an advantage when it was their turn."
    $popx = .33
    call poptearo
    j "Bert... why are you telling us that?"
    j "I..."
    j "How can I trust you if I know you're the chosen killer?"
    play music "audio/rush.mp3"
    b "That's exactly why you can trust me!"
    i "Huh?"
    b "The chosen killer can't be the Game Master."
    call popwowb
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
    i "Hold on..."
    i "I know we gotta move quick, but I'm not convinced yet."
    $mood = "shock"
    call pophuhb
    b "What?"
    i "What if you are the Game Master, and you're just cheating in the last round?"
    b "Well, I'm the chosen killer."
    b "I can't be both the chosen killer and the Game Master."
    i "..."
    i "I need more proof you're the chosen killer, and not just the Game Master lying."
    b "Well someone has to be the chosen killer, right?"
    j "Based on everything that's happened so far, yeah."
    call pophuhb
    b "Was it either of you chosen? Were you given some hint or item?"
    j "..."
    i "..."
    b "Then that should sett-"
    call poptearo
    j "..........Freddy..."
    j "It could be Freddy..."
    j "As crazy as it sounds, Freddy could be the chosen killer."
    j "There's a chance you're just using the fact that he's unconcious for your own gain."
    b "...Jenny, you know I wouldn't do that."
    j "I want to believe it's you, Bert, but we don't have proof it's not Freddy."
    i "Yeah. We need more proof."
    $mood = "sad"
    b "More proof?"
    j "Sid's right... there is another little detail missing."
    j "You said you've never been here before, but all the other chosen killer's had some connection to that location."
    i "Yeah!"
    i "You woke up and found a flashlight, so what?"
    i "Before I can trust you again, I need proof that you have a tie to this location."
    b "Proof that I have a tie to this location..."
    b "I don't have that."
    i "Well..."
    show sid mad
    i "Figure it out."
    b "Sid..."
    i "I want to trust you, I do."
    $popx = .67
    call popwowo
    i "But I trusted Lauren, too."
    i "I just need... a little more proof that you weren't trying to kill Freddy."
    j "...Bert."
    j "Sid and I will figure out our plan and tend to Freddy."
    j "You should see if there's a way to connect yourself to this location."
    hide jenny
    hide sid
    with dissolve
    bi "Jenny looks visibly scared of me."
    bi "And Sid looked like he wants to kill me a minute ago."
    bi "I guess I can't blame them - if I had meant to poison Freddy, that's..."
    bi "Sickening."
    $mood = "ind"
    bi "Regardless..."
    bi "I didn't mean to poison him, and I know I am the chosen killer."
    bi "But how can I prove I'm the chosen killer for this location if I've never been here?"
    bi "..."
    bi "I guess I need to look around."
    bi "Something {i}has{/i} changed, at least a little, since we've been here."
    hide scary with dissolve
    call screen pickSpotpent with dissolve
label pent346:
    scene bg pentkitchen55 at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show frogsit5 at bg:
        #zoom .85
        xcenter -.05
        ycenter .675
    $cat = True
    bi "..."
    bi "It's been a little while and the sun's coming up."
    bi "It looks like the fog has cleared up since earlier, too."
    bi "I'll take another look out the window."
    scene bg pentview at bg with dissolve
    bi "It looks like rush hour."
    bi "In a vibrant, booming city."
    bi "Kids with their parents, people in a park, families heading out for the day..." #55%
    bi "What a beautiful view, right into the heart of the city."
    bi "The thing is..."
    $mood = "sad"
    call popwowb
    bi "I know exactly where I am."
    bi "This is the most bittersweet moment of my life."
    bi "I... I do have a tie to this location."
    bi "Because this location..."
    show scary with dissolve:
        alpha .5
label pent35:
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
            $mood = "sad"
            bi "That's where it happened."
    bi "That's where I killed that woman."
    bi "I want to throw up just looking at that intersection."
    bi "I've avoided this area since the accident, and to think this is how I'm seeing it again."
    bi "..."
    $mood = "ind"
    bi "One other thing makes sense now too."
    show theflashlight with dissolve
    bi "My advantage for this location, this flashlight."
    bi "Everything's clicking for me now..."
    bi "The flashlight itself isn't the important part."
    $mood = "shock"
    call popwowb
    bi "It's the back, this solid metal tip."
    bi "These points are made to crack safety glass..."
    bi "I've seen them used in cars before."
    bi "That's why Sid wasn't able to crack the window."
    bi "But with this, and a little force..."
    show scary with dissolve
    $mood = "ind"
    bi "At least I can prove it now."
    play sound "audio/shatter.mp3" volume .75
    pause 1.0
    scene bg pentkitchenbroke at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show frogsit5 at bg:
        #zoom .85
        xcenter -.05
        ycenter .675
    with dissolve
    show jenny scared:
        xcenter .3
    show sid happy:
        xcenter .7
    with dissolve
    $popx = .67
    call popwowo
    i "Bert?! What the hell?!"
    j "Are you okay?!"
    i "How did the window break? I couldn't even leave a scratch..."
    $mood = "ind"
    b "It's the flashlight."
    b "It wasn't about being a flashlight."
    b "This sharp back is a safety glass breaker."
    b "Normally, windows like this are incredibly hard to shatter, but  with this, it's easy."
    b "That advantage let's me break the window, and then..."
    bi "Well..."
    call pophuho
    i "Is that your connection to this location? Being able to break the glass?"
    b "No, that was just my advantage."
    b "I did find a connection to the location."
    b "This... is the scene of my crime."
    $mood = "sad"
    j "You ran a woman over in this apartment?"
    b "No, it happened on the road, down there."
    $mood = "ind"
    show sid mad
    i "And you just noticed now?"
    b "Well, it was dark and foggy - you weren't able to tell where we were either."
    show sid ind
    i "That's true..."
    b "But now that I know where we are, I could tell you anything about the area."
    b "Mok Park, Clepper's Clippers down the road, DaDonuts is probably about to open around now, you name it."
    b "It's burned into my mind, every store, every street sign, every crosswalk."
    $mood = "sad"
    b "Between that and my getting the flashlight, I hope that's enough proof for you both."
    i "..."
    j "I believe you, Bert."
    j "You're the chosen killer for the location, like you said."
    j "And you didn't intentionally poison Freddy."
    i "Yeah, alright, same."
    $mood = "ind"
    b "Thank you, both of you."
    bi "One of them has known this whole time."
    i "Let's get back to it then."
    j "Bert, you made it sound like you had a plan to figure out who the Game Master is."
    b "I do."
    call popwowb
    b "And it's one of you two!"
    i "..."
    j "..."
    j "Not it..."
    show sid mad
    show jenny scared
    call popwowo
    i "HEY! THAT'S NOT HOW IT WORKS!"
    i "Bert said he has a plan, so we need to help him!"
    $popx = .33
    call popwowo
    j "Yeah! And Sid, if you don't cooperate, we'll know you're the Game Master!"
    i "I'm not the Game Master! You must be!"
    j "We'll see about that, Sid."
    show sid ind
    show jenny ind


    b "We don't have time to bicker. Freddy needs treatment."
    b "And if either of you push back now, it's proof that you want him to die."
    b "So we're going to settle everything, right here and now."
    b "We're going to end this game - "
    call popwowb
    b "WIN this game."
    j "How can we do that?"
    b "We've collected data about Sydell's past from this location."
    b "About Sam's drugs, Dan's hit job, Catherine's burglary, and more."
    $mood = "ind"
    b "And... about the three of us."
    b "Now all I have to do is piece the story together."
    call popwowb
    b "And I'll know - once and for all - who the Game Master is."

    j "..."
    i "..."

    ###implanted
    show bg reflecting
    hide screen status_screen
    hide screen showchibis
    hide frogsit5
    with dissolve
    stop music fadeout 1.0
    b "So, both of you."
    b "I need you to tell me your backgrounds again."
    b "Then tell me about your crimes, and any prior connections with anyone from the game."
    b "And finally, any connections you made during the game."
    $mood = "sad"
    b "... This is it."
    b "So tell me everything."
    $mood = "ind"
    b "Sid, you first."
    hide jenny with moveoutleft
    show sid ind:
        linear .2 xcenter .5
    i "Okay, yeah."
    $popx = .47
    call popwowo
    i "I'm Sid Straits!"
    i "I'm 17 and was finishing high school before all this."
    i "I was a little bit of a trouble maker, but not a slacker!"
    i "I was helping my parents run the store, and learning about computers on the side."
    call poptearo
    show sid happy
    i "We were pretty poor."
    i "For extra money, I did a little hacking..."
    i "That's how I got caught up with Shahar."
    i "Not directly, I didn't know the guy, but there was some lawsuits and blackmail going on."
    i "Stella as involved, and Dracul-er, Ivan, knew about some of it."
    i "I... wish I could undo it all, take it all back."
    i "I just wanted to make sure my family was making enough money."
    i "When this whole game started, I knew that's why I was involved, though I didn't know the details."
    i "..."
    show sid ind
    i "Like I said, I appreciated Dan."
    i "We know a bit about his past now, and he wasn't an amazing guy, but..."
    i "That doesn't change the way he talked to me, or respected me."
    i "He was manly, headstrong, protective."
    i "We only knew him for a few days, but it was hard to really connect with anyone else here after he died."
    i "..."
    i "I know the hint in the bank incriminates me, but... my name is all I have."
    i "Even if it does start with an S, like the hint claimed."
    i "I guess... that's it."
    hide sid with dissolve
    b "Now Jenny."
    show jenny ind with dissolve
    j "Well, from the top I guess."
    call popwowo
    j "I'm Jenny Flowers, 20 year old college student."
    j "I come from a pretty normal middle-class family."
    j "It feels like so long ago..."
    show jenny scared
    j "I've always been politically active, just doing what I can, and got arrested protesting about Freddy's father."
    j "It didn't lead to much at the time, but it's my connection to Freddy for this game."
    j "I... stand by what I did."
    call poptearo
    j "Freddy's a good kid, but his father is a horrible man."
    show jenny ind
    j "As for connections I made during the game..."
    j "Well, I think you and I get along really well, Bert."
    j "I know you have to question both Sid and I, I get it."
    j "But you're the first person here I told about my arrest."
    j "And I was the first person you told about your car accident with that woman."
    j "I don't know, maybe I'm being foolish, but... I think we got pretty close, you and I."
    j "I guess... that's it."
    hide jenny with dissolve
label pentpicker:
    show bg reflecting
    b "..."
    b "......"
    play music "audio/rush.mp3" fadein 1.0
    b "I know what happened."
    call popwowb
    b "And... I know who the Game Master is."
    b "Between all the murders, investigations, clues we found here, and your stories..."
    b "There's only one thing that doesn't add up."
    b "One thing that tells me who the Game Master has to be."
    b "For Freddy's sake, we have to act now."
    b "So."
    b "The Game Master is..."
    call screen pickSpotpent with dissolve
label pentsid:
    scene bg pentkitchenbroke at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    show frogsit5 at bg:
        #zoom .85
        xcenter -.05
        ycenter .675
    show sid happy:
        xcenter .5
    with dissolve
    b "Sid."
    b "We talked about the last name hint, but it's been weighing on me."
    b "All the rules the Game Master left have been accurate so far, and I think that one is too."
    b "Anyone could be lying about their last name, but both your names definitely starts with an S."
    $popx = .47
    call popwowo
    i "Bert, I -"
    b "It's time."
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
        linear 1.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 120.0, 690.0)*RotateMatrix(0.0, 0.0, 0.0)
    stop music
    scene black with dissolve
    play sound "audio/shatter.mp3" volume .75
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    hide screen status_screen
    hide screen showchibis
    camera at paralloff
    show bg pentfall at bg
    show sidfallanim at bg
    show glassfallanim at bg
    with dissolve
    show screen killuser
    pause 6
    hide screen killuser
    scene black with dissolve
    "..."
    jump pentpicker

label pentjenny:
    show bg reflecting
    show jenny ind with dissolve
    #show jenny in void agian
    $mood = "ind"
    b "Jenny."
    b "It's true that we were close."
    b "I'll never know if that was real or not."
    call popwowb
    b "Because you're the Game Master, and you die here."
    j "Bert, are you being serious?"
    b "There's no way I could be the Game Master."
    $popx = .47
    call popwowo
    b "You slipped up, Jenny."
    b "Just a few minutes ago, you said..."


    scene bg pentkitchenbroke at bg
    show frogsit5 at bg:
        #zoom .85
        xcenter -.05
        ycenter .675
    show jenny scared:
        xcenter .3
    show sid happy:
        xcenter .7
    show sepia:
        alpha .5
    with dissolve


    b "I did find a connection to the location."
    b "This... is the scene of my crime."
    $mood = "sad"
    j "You ran a woman over in this apartment?"
    b "No, it happened on the road, down there."

    scene bg reflecting
    show jenny ind
    with dissolve

    b "I thought it was just a joke about a car crash in the apartment."
    b "That silly, lighthearted personality I've grown to love throughout this game."
    $mood = "sad"
    b "But despite how often I think about the woman I killed, and the accident..."
    $mood = "ind"
    call popwowb
    b "I could never bring myself to share any details about her."
    b "There's no way you could have known it was a woman in the accident."
    b "I figured maybe it was a lucky guess, or part of the joke, so I had you and Sid give some words."
    b "But even with this second chance... you made the same slip up."
    j "I..."
    b "So, Jenny."
    b "We can start from the beginning, person by person."
    b "Crime by crime."
    b "And by the end, I'll prove that it's you."
    show ch5evlauren with dissolve:
        ycenter .6
    b "Chronologically, the first crime to happen was Lauren's."
    b "There was bank robbery about six years ago, and she was among the people there."
    $mood = "sad"
    b "She shot the robber, but also ended up shooting and killing a young girl."
    b "We still don't know who that girl is, but..."
    $mood = "ind"
    b "Given the timeline, that girl would have been around your age, Jenny."
    b "My guess is she was a friend of yours."
    hide ch5evlauren with dissolve
    j "..."
    b "And if it was, that must have scarred you deeply."
    b "An experience like that when you're so young can warp your sense of justice and how you see life."
    b "It was the start of all of this, and..."
    b "Why everything that happened to your father sent you over the edge."
    j "My father?"
    call popwowb
    b "Mr. Sydell, your father, and the owner of InSyde Electronics."
    j "..."
    show ch5evkaiser with dissolve:
        ycenter .6
    b "The one to start it all was Kaiser"
    b "We have proof that Kaiser's train heist damaged Mr. Sydell."
    b "InSyde Electronics suffered massive losses."
    b "But more importantly, it damaged relationships with partners - namely, Cantoire." #julian
    hide ch5evkaiser
    show ch5evstella:
        ycenter .6
    with dissolve
    b "Unable to fulfill shipments, InSyde got hit with lawsuits from Stella's team."
    b "While Stella didn't personally work the cases, her team was merciless."
    b "She hired one of the best lawyers she could find to dig up dirt and ruin Sydell."
    hide ch5evstella
    show ch5evshahar:
        ycenter .6
    with dissolve
    b "That lawyer was Shahar."
    b "The man we knew was once a great lawyer..."
    b "Cantoire wanted InSyde in the dirt, and used cheap tricks to do it."
    b "The train heist wasn't Mr. Sydell's fault, but the lawyers didn't care - they did anything to win."
    b "They blackmailed a kid to hack Sydell's computers and plant information."
    b "Of course, Stella's team was full of monsters."
    b "Perhaps weary Shahar would confess, or just as an extra precaution, they..."
    hide ch5evshahar
    show ch5evdracula:
        ycenter .6
    with dissolve
    b "They hired Ivan to lobotomize Shahar."
    b "Leaving the poor lawyer as a shell of himself, thinking he was a pirate."
    b "Ivan himself was remorseful, but it didn't change what he did."
    hide ch5evdracula with dissolve
    b "And it was just to protect the fact that some kid was rigging a case for them."
    show ch5evsid with dissolve:
        ycenter .6
    b "Sid, the kid right over there."
    b "The self trained ethical hacker got forced to plant info."
    b "It ruined the case for Sydell, and he lost everything he had worked so hard for."
    b "It must have been devestating for him, and his family."
    hide ch5evsid with dissolve
    j "..."
    b "His business in shambles, Sydell turned to drugs."
    show ch5evsam with dissolve:
        ycenter .6
    b "That's where Sam came in."
    b "Sam sold Sydell experimental drugs, and Sydell didn't care."
    b "By Sam's own admission, the drugs were not safe, and probably ruined his mental state."
    b "Sam said Sydell became a regular customer."
    hide ch5evsam with dissolve
    b "It was almost rock bottom for Sydell."
    b "But there was more coming."
    show ch5evcatherine with dissolve:
        ycenter .6
    b "Catherine robbed his mansion."
    b "Losing material possessions is always awful."
    b "But the peace of mind? His safety inside his own home?"
    b "It must have been shattered."
    b "Catherine didn't give a lot of details about the burglary, but I think I've connected some dots."
    hide ch5evcatherine
    show ch5evfreddy:
        ycenter .6
    with dissolve
    call popwowb
    b "This... is where Freddy comes in."
    b "To be precise, Freddy's father, Mr. Ogden."
    b "He was a shady businessman, and you did hate him, Jenny."
    b "But not for the reason you told me."
    j "..."
    b "Ogden's must have known how dire Sydell's state was, and he decided to make a move."
    b "Freddy's father tipped off Catherine that Sydell would be an easy target."
    b "We don't know his goal, but they stripped away any last semlance of safety Sydell had."
    hide ch5evfreddy
    b "Business failing, addicted to drugs, and feeling unsafe in his own home."
    b "He fled to this apartment as a last ditch effort for safety."
    b "It must have been unbearable."
    show ch5evbert with dissolve:
        ycenter .6
    $mood = "sad"
    b "And... I only made it worse."
    b "This is where I come in."
    b "It was the worst moment of my life."
    b "I think about it almost every day, even if just for a second."
    b "Right otuside this apartment, down there in that intersection, I drove into and killed a woman."
    b "That woman was - it could only have been - Sydell's wife."
    b "The person who was by his side the whole time."
    $mood = "ind"
    b "And if she was Sydell's wife..."
    #show jenny
    hide ch5evbert
    show ch5evjenny:
        ycenter .6
    with dissolve
    call popwowb
    b "That had to have made her... your mother."
    b "You know my accident inolved a woman because... it was your mother."
    b "I didn't realize it until now, but that must be where this fake last name comes from."
    j "..."
    b "Jenny Flowers - your real name is Jenny Sydell, making the hint in the bank true."
    b "It was right under our noses the whole time."
    hide ch5evjenny with dissolve
    b "And for Mr. Sydell, the rest was history."
    b "Losing literally everything, he turned to Dan, or as he knew him,"
    show ch5evdan with dissolve:
        ycenter .6
    b "Spaghetti, the hitman."
    b "He ordered Dan to kill Stella in a fit of madness."
    b "As we know, this backfired."
    b "Stella's team caught him, and got him to kill Sydell himself."
    b "To think Dan was the one to kill Sydell this whole time..."
    b "He somehow ended up in jail - by Stella's team, the cops, or his own confession."
    b "But it wasn't enough."
    b "If there's one thing I've learned through all of this, it was never enough."
    hide ch5evdan with dissolveß
    $mood = "sad"
    b "For you, Jenny."
    b "You watched it all from the sidelines."
    b "Your father's business get destroyed."
    b "Your family's safety in jeopardy."
    b "Your father turn to drugs."
    b "And then both of them die."
    b "That's how all of this started."
    b "Revenge, anger, fear, whatever the reason was."
    b "You pulled every possible string to get back at all of us."
    b "You think we all deserved to die."
    $mood = "ind"
    b "That's why you found Ivan and made him implant all these chips in our brains."
    b "You set up this whole thing, and you're the reason everyone else is dead now."
    b "You're the Game Master."
    call popwowb
    b "And it's been you this whole time, Jenny."
    b "There was almost nothing to connect you to Sydell."
    b "But you yourself gave me the last piece of information I needed"
    b "You messed up."
    b "Or maybe, you've accepted your fate."
    show bg pentkitchenbroke at bg
    $ statusnt("Dining Room", "bert", ch=5, sun=1)
    $ showchibint("freddy", "jenny", "sid")
    with Dissolve
    $mood = "shock"
    i "Bert!"
    show sid ind with moveinleft:
        xcenter .3
    $popx = .34
    call popwowo
    i "It's Freddy, his head is burning hot, and his breathing has gotten weird!"
    i "I'm worried he's, he's..."
    i "We need to do something, now!"
    hide sid with moveoutleft
    j "Bert..."
    $mood = "ind"
    b "We need to end this game."
    b "For Freddy."
    b "And for everyone else you killed."
    b "Jenny..."
    b "You're the Game Master."
    b "And your end is deserved."
    #bert pushes jenny out the window.
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
        linear 1.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 120.0, 690.0)*RotateMatrix(0.0, 0.0, 0.0)
    stop music
    scene black with dissolve
    play sound "audio/shatter.mp3" volume .75
    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    jump jennydie

label jennydie:
    camera at paralloff
    show bg pentfall at bg
    show jennyfallanim at bg
    show glassfallanim at bg
    pause 3.0
    jump postdeath

label postdeath:
    "Jenny ironically died in the same intersection that her mother did."
    "After which, Bert and Sid no longer feared the chip in their head knocking them out or killing them."
    "They knocked down the front door of the apartment, and found help down in the apartment lobby."
    "Freddy was rushed to the hospital and made a full recovery."
    "Bert and Sid were taken to the police for questioning, and a full investigation began."
    "Ultimately, neither were tried with any crimes."
    "The bodies of Dan, Kaiser, Stella, Catherine, Shahar, Ivan, Sam, Lauren, and Jenny were recovered."
    "As well as the bodies of those assisting Jenny, who were killed via brain chip at the time of her death."
