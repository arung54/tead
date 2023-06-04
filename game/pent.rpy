label pentGo:
    #$ftecounter = 2
    #$noside = True
    #camera at paralloff
    scene bg reflecting at bg with dissolve
    $cat = False
    $ statusnt("???", "bert", ch=5, sun=0)
    $mood = "sad"
    play music "audio/rush.mp3" fadein 1.0

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
    bi "I need to go find them."
    bi "Up the ladder I go-"
    ses "Mrep!"
    $mood = "shock"
    bi "Huh?"
    bi "There's a false panel on the far wall." #febreview Might cut??? unsure
    bi "The key is in the keyslot, making it pretty obvious."
    $noside = True
    blank "Bert walked over and opened the false panel."
    blank "Inside was a shelf with one item."
    $noside = False
    show theflashlight with dissolve
    bi "It's a generic looking flashlight."
    bi "It's made of metal, with an on-off button on the shaft."
    bi "There's also a small metal tip on the opposite end."
    bi "It turns on, but it's not {i}that{/i} dark down here anyway."
    bi "Plus, I see light coming from the crack in the cellar door anyway."
    bi "I don't think I need this right now."
    $noside = True
    blank "Bert unscrewed the flashlight to find its batteries."
    $noside = False
    $mood = "ind"
    bi "Doesn't seem like anything out of the ordinary."
    hide theflashlight with dissolve
    bi "But why is a flashlight being locked away in a wine cellar?"
    bi "Speaking of which..."
    show thekey with dissolve
    bi "I will keep my hands on the key."
    bi "If anyone needs the flashlight, I can come back here and get it with this."
    hide thekey with dissolve
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
    bi "What's with that hatch?"
    bi "It's half covered by the rug."
    bi "It's as if the wine cellar is normally hidden."
    bi "Why would someone need to hide their wine cellar?"
    bi "Anyway..."
    bi "This looks like a nice bedroom."
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
            b "Hmm... On second thought..."
            jump pent23

        "model of fireplace.":
            b "Not sure why I'd say that..."
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




    i "You really sprung this on me first thing in the morning."
    b "I think it's closer to mid-day, there is a window in the other room."
    show sid happy
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter .61
        ycenter .25
        zoom .75
    i "A window?!"
    i "Bert, why didn't you say so earlier!"
    $mood = "shock"
    i "Screw all this puzzle hunting, I'm jumpin' for it!"
    b "Sid, I think we're really high u-"
    hide sid happy with moveoutleft
    show jenny scared:
        xcenter .3
        linear .3 xcenter .5
    j "We should follow him before he jumps out the window."
    j "Come on, Freddy!"
    hide jenny scared with moveoutleft
    hide frogsit3 with dissolve
    b "He better not jump out the window..."
    scene bg pentkitchen at bg
    $ statusnt("Loft", "bert", ch=5, sun=2)
    $ showchibint("freddy", "jenny", "sid")
    show sidstand2 at bg:
        xcenter .48
        ycenter .53
    show jenny scared:
        xcenter .25
    with fade
    i "This is our way out of all this!"
    i "It might involve some careful climbing, but look!"
    i "Civilization!"
    j "Bert! We're so high up."
    j "You have to stop him."
    j "If he falls and dies, I'm blaming you..."
    b "Me?!"
    i "Graaaah! Why won't this glass break!"
    scene black with fade
    bi "I ran over and pulled Sid off the window."
    bi "I was so relieved to keep him safe."
    stop music fadeout 1.0
    bi "But it only lasted a moment before everything changed."
    bi "I leaned up against the glass and looked down."
    bi "A vibrant, booming city beneath me."
    bi "Kids with their families, people in a park, women crossing the roads..."
    bi "I just wish I didn't recognize it."
    scene bg pentview at bg with dissolve
    bi "..."
    bi "Everything clicked."
label pent3:
    show scary with dissolve:
        alpha .5
    menu:
        bi "This is a view of..."

        "the road I grew up on.":
            bi "No, unfortunately it isn't."
            jump pent3

        "somewhere I've seen in a movie.":
            bi "No, I don't think it is..."
            jump pent3

        "my favorite park as a kid!":
            bi "That's true, but... not what's important here."
            jump pent3

        "where I ran over that lady.":
            bi "..."
            bi "That's where it happened."

label pent4:
    bi "That's where I killed that woman."
    bi "I recognize it too well."
    bi "St. Mok Park across the steet, the tutoring building down the block..."
    bi "A road I haven't driven on once since the incident."
    bi "..."
    bi "I hear Sid banging on the window again beside me."
    bi "The windows aren't breaking, even though he's using all his strength."
    bi "Suddenly, this makes sense too."
    bi "And my heart sank even further."
label pent5:
    menu:
        bi "He can't break the window because..."

        "he's not strong enough.":
            bi "No, it's nothing to do with Sid."
            jump pent5

        "the emergency window breaker is in the cellar.":
            bi "That flashlight..."

        "he's hitting it in the wrong spots.":
            bi "No, I don't think that's part of it."
            jump pent5

        "the window is made out of safety glass.":
            bi "This is true, but that means he would need..."
            jump pent5
label pent6:
    i "Yo yo yo!!"
    i "It's me, sid"
    #wake up first, in the cellar
    #confused??? find flashlight window breaker. leave it there
    #go up, nobody there. wtf... look aroudn, find them in bedroom
    #chat a tiny bit
    #go into kitchen, sid says holy shit a window, tries to break it
    #everyone yells to stop him, be careful
    #we go look at window
    #everything clicks......
    #3 question quiz for user 1) what was the flashlight 2) where are we 3) what does this mean (bert is person)
    if not pent_evidence[0]:
        $pent_evidence[0] = True
        show newevidencefound with dissolve
        pause 1
        hide newevidencefound with dissolve
        blank "__________ was added to evidence."
