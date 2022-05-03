#wake in lobby (MAP)
#go into hallway
#check out break room
#go look at safe/couch
#check out office
#check out guard room

label bankGo:
    $dan = False
    $ftecounter = 8
    scene black
    $mood = "sad"
    bi "Two more people dead..."
    bi "Shahar... and Dracula."
    bi "No, not Dracula. Ivan."
    bi "Even after his death he deserves to be called his real name."
    bi "Do I hate him? I think so."
    bi "I think I have to." #Arun: He lobotomized Shahar, they probably should kind of hate him
    bi "What he did to Shahar is horrible."
    $mood = "ind"
    bi "But..."
    bi "None of us here have options, all we can do is keep pushing forward."
    bi "I won't let them, or anyone else, die in vain."
    bi "..."
    bi "I can feel a hand on my shoulder."
    bi "Hmm?"
    show bg banklobby with dissolve
    $ statusnt("???", "bert", ch=4, sun=2)
    $ showchibint("lauren", "freddy", "jenny", "sid", "sam")
    show sid ind with dissolve
    i "Hey, wake up Bert."
    i "Help me get everyone else up."
    bi "Everyone else was still laying around on the floor."
    bi "I spent an extra moment looking around, thinking there'd be more people, but..."
    bi "This really is everyone now."
    bi "Freddy, Jenny, Sid, Sam, Lauren, and myself."
    b "Yeah, let's get them up."
    hide sid ind with dissolve
    blank "Everyone else slowly woke up."
    show sam with moveinleft
    s "You'd think waking up would stop it, but no."
    s "This nightmare continues."
    s "Tsk... what a disaster."
    b "Is everyone okay?"
    show sam:
        linear .3 xcenter .75
    show lauren ind with moveinleft: #Arun: Sam first
        xcenter .25
    l "Okay as I could be, I guess."
    l "It looks like we've been moved again."
    b "As crazy as it sounds, I am starting to get used to it."
    b "We can check in more detail, but it looks like the exits are boarded up again..."
    hide sam
    hide lauren ind
    with moveoutright
    show jenny ind:
        xcenter .75
    show frog ind:
        xcenter .25
    with moveinleft
    j "Freddy, are you alright? Do you still remember my name?"
    f "You're still Jenny, right?"
    show jenny happy
    j "Phew! Just checking!"
    f "Yay!"
    show jenny ind
    j "It can't hurt to do a quick mental check every once in a while."
    j "Besides, we are being knocked out by a chip in our brain."
    b "Yeah, I'm not exactly up to speed on the science behind that."
    b "Hardly seems safe or reliable."
    b "At the very least, now we know that Ivan is the one that set them up."
    b "I'd say it's hard to believe, but it's not like he was ever very open with us..."
    hide frog ind with moveoutleft
    show sid mad with moveinleft:
        xcenter .25
    i "That bastard did this to us..."
    i "Treating us like damn lab rats, it's disgusting!"
    b "You're right, but think about it from his point of view."
    show sid ind
    i "H-huh?"
    b "What options did he have?"
    b "If he hadn't done it, who knows what the Game Master would've done to him."
    i "..."
    b "As horrible as what he did was, we'll never know the situation he was put in."
    j "At this point in this mess, it's not worth being mad at anyone."
    j "Plus, it's actually useful information!"
    show sid happy
    j "We're slowly getting a more complete picture about why we're all here."
    b "You're right Jenny."
    ###summary of crimes that they know of so far goes here!!! arun
    hide jenny ind
    hide sid happy
    with dissolve
    show sam with dissolve
    s "In any case..."
    s "I think we should start to explore."
    s "There's no point in waiting around and wasting time."
    s "We need to know what we're dealing with here."
    b "Agreed."
    b "This room seems like... a lobby? For some type of business."
    s "There looks like a floor-plan on the wall over there, behind the counter."
    hide sam with dissolve
    show bankposter with dissolve
    b "Oh wow, this is interesting!"
    s "Why do you say?"
    b "None of the other places we've been put have given us a map." #Arun: Map shouldn't be "publicly available"
    b "With this, we know what we're getting into, at least a little bit."
    l "That star must indicate our current location."
    l "It says we're in the \"lounge\" right now, which makes sense."
    i "Wait a minute, does that say... vault?"
    i "Like, a BANK VAULT?"
    b "Yeah, I think we must be in a bank."
    b "I wonder why this is here in the first place."
    l "It's probably a safety thing? So the bank employees know where the exits are."
    s "Yeah, or it was just put here for this... situation."
    hide bankposter with dissolve
    show sid happy with dissolve
    i "So if I go out this door and down the hallway..."
    i "There's a bank vault?"
    b "Uhhh, that is what this map says..."
    i "That nobody's guarding, probably?"

    b "But-"
    i "See ya!"
    hide sid happy with moveoutright
    $ showchibi("lauren", "freddy", "jenny", "sam")
    bi "Sigh."
    bi "We should probably go after him."
    show jenny happy:
        xcenter .75
    show frog happy:
        xcenter .25
    with moveinleft
    j "Come on Freddy, let's follow Sid!"
    f "Yes ma'am!"
    b "Thanks for keeping a level head, Jenny."
    j "Yeah! We can't let him get all the money for himself!"
    hide jenny happy
    hide frog happy
    with moveoutright
    $ showchibint("lauren", "sam")
    b "Or not..."
    show sam with moveinleft
    s "We'll need to come back to explore this room more in a bit."
    b "Agreed. We can circle back here at the end."
    b "Plus, with all the couches, this seems like a good meeting and sleeping spot."
    hide sam with moveoutright
    $ showchibint("lauren")
    show lauren ind with moveinleft
    l "Bit of a hectic start here."
    b "At least everyone seems to be in decent spirits."
    l "Yeah!"
    l "Maybe this is weird to say given the situation, but..."
    show lauren aw
    l "At least I feel like I can trust most of you."
    b "Oh? What do you mean?"
    l "No offense to some of our fallen comrades but..."
    show lauren ind
    l "It was really difficult to work with Stella, Dracula, or Shahar..."
    l "Everyone in this core group is cooperative and pretty... normal?"
    l "Other than Sam - who's seemingly turned a corner - I'm not scared of anyone here."
    b "Yeah, you're right."
    show scary with dissolve:
        alpha .5
    bi "She really is right - this group is pretty trustwrothy."
    bi "I've tried my best to cooperate with everyone this whole time, but..."
    bi "It seems like now it will actually be a bit easier."
    bi "The only issue is, that makes it even harder to pick out the Game Master..."
    bi "If I feel like I can trust everyone, maybe I'm even further away from figuring out that mystery."
    bi "Maybe I shouldn't focus on the negatives."
    hide scary with dissolve
    b "You ready to go follow them?"
    l "Let's do it. They're probably already in the next room."
    hide lauren ind with dissolve
    scene bg bankhall1 with dissolve
    $ statusnt("Bank Hallway", "bert", ch=4, sun=2)
    $ showchibint("lauren")
    show lauren ind with dissolve:
        xcenter .5
        linear .3 xcenter .75
    l "I hear them chatting in that next room on the left."
    b "Hmm, Lauren? Do you see that too?"
    l "See what?"
    b "There's a red light coming from further down the hallway."
    b "It must be really bright if we can see it around the corner."
    l "Huh, you're right."
    b "Well, we'll do a full tour anyway, might as well go in order."
    b "If the map was accurate, this next room should be..."
    hide lauren ind with dissolve
    show bg bankbreak with dissolve
    $ statusnt("Staff Kitchen", "bert", ch=4, sun=2)
    show lauren ind with dissolve
    l "...the staff kitchen."
    $ showchibi("freddy", "jenny", "lauren", "sam")
    show lauren ind:
        linear .3 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "This room's about what I'd expect."
    j "A sink, coffee machine, and a fridge with some snacks."
    bi "I could go for some coffee and snacks right about now..."
    show jenny ind:
        xcenter .25
        linear .3 xcenter .3
    b "That poster on the wall seems like it's mocking us..." #Arun: Maybe move Jenny so poster is visible
    ses "Mrow..."
    l "The Game Master has some sick sense of humor."
    show jenny happy
    j "Aww, really? I think it's cute!"
    j "It's your cousin, Sesame!"
    l "Anyway, having access to food is nice."
    l "Maybe not a nutritious meal, but I'll see if I can grab something for Freddy."
    hide lauren ind with dissolve #Arun: Dissolve instead?
    show jenny ind:
        linear .3 xcenter .5
    j "Pretty dinky kitchen for how fancy the lobby was, huh?"
    j "I guess it doesn't have to look pretty if the customers don't come in here."
    b "Yeah, but any place with food is good enough for me."
    b "Still, I can't help but wonder..."
    b "Why a bank? Why did the Game Master bring us here?"
    j "What do you mean?"
    b "Well, so far, we've been brought to places that are significant to one of us."
    b "Kaiser's train heist, Catherine's burglary..."
    b "If feels like the implication is... that one of us has robbed this bank."
    j "Huh?!"
    j "No way! Nobody here is capable of that."
    b "I'd agree, if it wasn't for the circumstances..."
    b "but that's definitely my first impression."
    show jenny happy
    j "Hmmm, I'm not sold."
    j "There's probably a more reasonable explanation."
    j "Maybe someone just... stole some of the snacks from the break room!"
    j "That's a crime too, ya know!"
    hide jenny happy with moveoutright
    show scary with dissolve:
        alpha .5
    b "Jenny might be right, I don't think anyone here could have robbed a bank."
    b "But I also wouldn't have thought the others were capable of what they did..."
    b "Plus, we already know Sid and Jenny were in tough financial situations, so..."
    b "Thinking they did something extreme isn't out of the question."
    b "It's worth remembering."
    hide scary with dissolve
    show lauren ind:
        xcenter .25
    show frog ind:
        xcenter .75
    with dissolve
    b "Hey wait a minute, where's Sid?"
    l "Freddy said he ran ahead when everyone else came in here."
    f "Yup! He kept saying \"money money money money money\" and left us behind."
    b "We should really be sticking together..."
    b "I'm gunna go look for him."
    l "We'll stay here for a bit and check out all these cabinets."
    f "And snacks!"
    hide lauren ind
    hide frog ind
    with dissolve
    show sam with dissolve
    s "I'll come with you."
    b "Okay, gre- hey wait, what?"
    s "What's wrong?"
    b "I think this is the first time you've actively tried to spend time with me."
    show sam angry
    s "..."
    s "I think after everything, the least I can do is try to be helpful."
    b "I... appreciate that."
    b "We all do."
    b "You know, we still trust you."
    s "Yeah, yeah, let's go find Sid."
    hide sam with moveoutright
    bi "Well, progress."
    scene black with fade
    blank "Sam and Bert walked out into the hallway and heard Sid's voice."
    blank "They followed the voice down the hallway."
label bank2:
    scene bg bankvault
    $ statusnt("Bank Hallway", "bert", ch=4, sun=2)
    $ showchibint("sid", "sam")
    with dissolve
    b "Sid?..."
    b "Woah... this vault is massive."
    b "That door looks like a foot thick of solid steel."
    b "It must weigh at least a ton."
    i "MY vault!"
    show sid mad with moveinright:
        xcenter .75
    show sam angry with moveinleft:
        xcenter .25
    i "HEY! Back off, this is gunna be MY MONEY!"
    i "I've got sharp teeth and I WILL bite you!"
    b "Whoa, Sid, it's just us!"
    s "What are you talking about?"
    show sid ind
    i "S-sorry for snapping at you..."
    i "I'm just kinda frustrated..."
    s "Frustrated?"
    i "Well, I was hoping I'd find the vault and grab all the money, easy peasy."
    i "But, well, look for yourself."
    show sid ind:
        xcenter .75
        linear .3 xcenter .7
    bi "There's a poster on the wall next to the vault."
    show bankposter2 with dissolve
    b "Huh? What's it say..."
    b '"Each of you possesses one third of the bank vault passcode"'
    b '"the day of the month you were born on."'
    bi "!!!"
    b '"Use any three of your birthdates, in any order, to unlock the safe."'
    b "Seems easy enough..."
    b '"The vault contains not only a substantial fortune, but also the true secrets of this game."'
    b "This seems almost too good to be true?"
    b "We can finally get answers, and apparently a ton of money?"
    i "Well..."
    b "Oh, there's some fine print."
    b "Let's see..."
    show bankposter3 with dissolve
    hide bankposter2
    b "......"
    b '"Inputting an incorrect passcode will instantly kill the user."'
    b "Oh."
    b "Now I see the frustration..."
    hide bankposter3 with dissolve
    show sid ind:
        xcenter .7
        linear .3 xcenter .75
    i "I mean, it's a little scary, but all we need is three people's birthdays!"
    i "The three of us could crack this bad boy open right now!"
    s "It's not that simple..."
    s "How can I trust you to give me your correct number?"
    s "How can you trust me to give you mine?"
    b "If someone lied, the user would die..."
    s "Yeah, and we wouldn't know who the killer is."
    b "Huh?"
    s "Since you need three numbers, there are two people who could've lied about their number."
    s "So if someone died inputting the wrong code, we would have no way to know who lied."
    b "It seems like the perfect setup to kill Sid, huh..."
    i "Hey! I-I knew all that..."
    i "Maybe..."
    s "To top it all off, we don't even know if it's true."
    b "Yeah, it could just be a trick, an empty promise to get us to kill each other."
    b "For all we know, successfully opening the safe instantly kills ALL of us."
    s "What a mess..."
    i "Ummm... maybe we could... guess?"
    i "The poster says all of us have a code, and we can use any three in any order."
    i "Let's see, carry the two... multiple this by that... oh wait..."
    b "There are only six of us, which means there are... 120 correct passcodes."
    i "47! Uh, I mean, 120!"
    i "That seems like a bunch, right?"
    i "Most locks only have one correct combo, 120 is a lot of options!"
    b "There are 31 days in a month though, and you'd have to guess two numbers, so..."
    i "Two? The safe needs three numbers!"
    s "Yeah but you know your own birthday, right?"
    s "...Right?"
    i "Oh, yes! So you'd only have to guess two numbers!"
    b "In total, your odds are about 20/961 to guess correctly."
    i "WHAT?! Are you sure?!"
    i "Math is so lame dude..."
    s "I think Bert's right though. It's not something to chance."
    i "...Okay."
    i "So what do we do, just ignore it?"
    b "It can be our last resort."
    b "If we go a few days with no other progress, maybe we can try it."
    s "Even then it seems risky... Unless Sid is the one opening it."
    show sid mad
    i "Hey! What's that supposed to mean?!"
    b "Sid, if you see the others before Sam or I do, tell them what we talked about."
    show sid ind
    i "Yeah, yeah. Not opening the safe unless it's our last resort."
    i "I think I'll look around in case there's a master key or something."
    b "Good idea."
    i "Oh, also, what's up with all these lights on the walls?"
    i "There's this red light around all four walls of the vault."
    b "We noticed that too."
    i "It could just be for the vibe?"
    s "Seems like a weird design choice if it's just for looks."
    b "I agree, it's probably useful somehow."
    b "Maybe it's a way to show the vault is locked?"
    b "Or maybe that the security system is armed?"
    b "That would make it easier for workers to know the status of the vault, from any side."
    s "Maybe the lights would turn off if we managed to get into the vault?"
    b "We should keep it in mind."
    b "Let's keep exploring, Sam."
    b "Sid, don't touch the safe!"
    i "..."
    s "Punk..."
    hide sam with moveoutleft
    scene black with fade
    blank "Bert and Sam walked back toward the only room they passed by."
label bank3:
    scene bg bankoffice
    $ statusnt("???", "bert", ch=4, sun=2)
    $ showchibint("sam")
    show sam
    with dissolve
    b "So according to the map in the lobby, this should be... the Director's Office."
    $ statusnt("Director's Office", "bert", ch=4, sun=2)
    s "What's a bank director anyway?"
    b "I have no idea."
    b "Let's snoop around, maybe we can find out."
    s "You'd think there would be a computer in here..."
    b "It looks like there was one on the desk."
    b "I can see the marks where a monitor and a mousepad must have been."
    b "Surely most banking stuff is done electronically rather than with paper these days?"
    s "Your guess is as good as mine."
    s "There is a filing cabinet over there, though."
    hide sam with dissolve
    blank "Sam took a peek in the filing cabinet."
    show sam with dissolve
    s "Damn, there are a ton of records in here."
    s "Family records, transaction history, mortgage info..."
    s "You said Shahar's name showed up in the hospital's computer, right?"
    b "Yeah."
    s "Maybe there's some dirt on someone else in here."
    s "It's worth looking."
    show sam:
        xcenter .5
        linear .3 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    $ showchibint("sam", "jenny")
    j "Hey, I caught up with you guys."
    j "Anything fun I missed?"
    blank "Bert told Jenny about the bank vault."
    j "That's terrifying! Maybe we can have Sid enter the passcode."
    s "That's what I said too."
    b "We've agreed not to touch it unless it's our last resort."
    j "Gotcha!"
    b "Anyway, digging through these filing cabinets could be useful."
    b "Sounds incredibly tedious though."
    j "Oh no... paperwork."
    s "You two can go on ahead."
    s "I'll sift through this stuff."
    b "You sure?"
    s "Yeah, if there's anything important I'll let everyone know."
    s "Honestly, I'm kinda hoping there isn't anything useful."
    s "Digging up more details about people's pasts is so... messy."
    b "I agree, but if it can help us get out of here alive, it's worth it."
    s "Yeah. I guess we'll see."
    b "Only one way to find out, I suppose."
    j "There should be one more room we can get into at the end of this hallway."
    j "Come on Bert, let's go check it out."
    b "Alright."
    scene black with dissolve
    blank "Bert and Jenny walked down the hallway to the last room."
    scene bg banklocker
    $ statusnt("Locker Room", "bert", ch=4, sun=2)
    $ showchibint("jenny")
    with dissolve
    show jenny ind with moveinleft:
        xcenter .75
    b "A staff locker room, huh."
    j "It reminds me of the ones at a gym."
    j "There's even sections over there for men's and women's showers."
    j "Why does a bank need a locker room with full sized communal showers?"
    b "Yeah, it's a bit odd."
    j "Also, there are tons of lockers with keys in the locks."
    b 'It seems like a "first come, first served" situation to grab any locker you want.'
    j "I'm a bit worried about people coming here to hide stuff in a locker..."
    j "Maybe we should take out all the keys and put them somewhere?"
    b "That's a good idea."
    hide jenny ind with dissolve
    blank "Jenny grabbed all 16 locker keys."
    show jenny ind with dissolve:
        xcenter .75
    j "Bert! Look at this."
    blank "Jenny held up a grey worksuit."
    b "Huh? What is that?"
    j "It looks like there's one in each locker."
    j "They must be the security uniforms."
    b "They definitely don't look like something you'd want a customer to see."
    j "Yeah, way too tacky."
    b "No no, I mean like, they're not professional looking."
    b "Very utiliarian design."
    b "The fact that the bank has 16 of these must mean they used them a lot..."
    j "Huh. They don't seem very useful for us, so I'll put this one back."
    j "Anyway, do you want to hold onto these locker keys?"
    j "My skirt doesn't have any pockets."
    b "Me? I guess I could, but are you sure you can trust me?"
    j "More than anyone else here."
    blank "Jenny handed Bert all 16 locker keys."
    bi "I'll keep these in my backpack."
    b "Looking around, we've got showers, towels, lockers, you name it."
    b "I can't help but feel grateful to have the necessities here for us."
    b "Between this room for hygiene and the break room for food, we should be okay for now."
    j "Yeah, I suppose..."
    b "What's wrong?"
    j "Well, having food and a shower is great, but..."
    j "So far that hasn't been our issue."
    j "Our issue has been not knowing who the Game Master is, or who's planning a murder."
    j "All these amenities to me are just... a false sense of security."
    bi "It really sucks to see Jenny sad like this..."
    bi "Just a minute ago she was so upbeat."
    b "Hmm... I have an idea, but I don't want to rush anything."
    j "An idea? Is it about the safe?"
    b "Actually, no. The safe seems like a trap to me and I don't want to risk it."
    b "I'm hoping Sam finds something useful in the records."
    b "Once we finish exploring and regroup with everyone else we can discuss it."
    j "Well, like I said, I know I can trust you Bert."
    show jenny happy
    j "I'm sure we'll be fine!"
    j "Anyway, you think I have time for a quick shower?"
    bi "And she's right back to happy-go-lucky mode."
    b "Let's head back to the lobby for now, it's the last room we need to really explore."
    b "We'll have more time to shower and eat and stuff in a bit."
    j "A-OK!"
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("jenny")
    with dissolve
    show jenny ind with moveinleft:
        xcenter .5
    j "Seems like everyone else is still exploring."
    b "Or eating all the snacks in the break room..."
    j "Either way, we have some time to look around in here."
    hide jenny ind with dissolve
    blank "Bert and Jenny spent about 10 minutes looking around the lobby."
    show jenny ind with dissolve
    j "Well, I've got good news and bad news."
    j "The bad news is that there's definitely no way to get out of here."
    j "Everything's boarded up again, not very surprising."
    b "And the good news?"
    j "Oh, did I say there was good news?"
    show jenny happy
    j "My mistake! No good news."
    j "At least the benches and couches look cozy to sleep on later."
    show jenny ind
    b "..."
    bi "She is right though, there isn't much of anything in here."
    bi "Lots of insignificant office supplies."
    bi "We found paper, a small amount of cash, some pens, a few small burlap bags."
    b "This is quite a big space we're trapped in, but there's not much happening."
    b 'Also, thankfully, there\'s no convoluted "prisoner-guard" dynamic this time.'
    b "We get to all work together a bit easier."
    j "I'm beat! I'll be over here if you need me."
    hide jenny with dissolve
    bi "She plopped down on a bench across the room."
    bi "I can't blame her, this is a lot of new information to take in."
    bi "Well, it seems like everyone's doing something for a bit."
    bi "Let's make sure we stay upbeat and keep busy."
    ### FTE 1 goes here
label bank4:
    scene black with dissolve
    blank "After a while, people returned to the lobby."
    blank "Everyone rested and ate staff kitchen food if they hadn't already."
    blank "Bert shared everything he learned with the group."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=3)
    $ showchibint("freddy", "lauren", "jenny", "sam", "sid")
    with dissolve
    show lauren ind with moveinleft
    l "Based on everything we've found, this place feels like a mystery..."
    l "Sid, did you have any luck finding a vault key or code somewhere?"
    show lauren ind:
        xcenter .5
        linear .3 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "I don't think it'll open without a code."
    i "Are you all suuure you won't tell me your birthdays?"
    l "No shot."
    l "Who's to say there's even anything in there?"
    i "Alright..."
    l "And besides, there are only six of us here."
    l "It seems pretty unlikely someone plots a whole murder without us noticing."
    b "There are so few of us less."
    b "We can even all sleep in the same room now, since this place is pretty big."
    i "Huh? Do I have to? There's a cozy looking sofa out in the hallway."
    l "Where?"
    blank "Sid grabbed a pen and started drawing on the map."
    show bankposter with dissolve
    i "I think it was in this corner."
    show banksofa with dissolve:
        xcenter .725
        ycenter .22
    j "Oh, I saw that too."
    b "I didn't notice. Is there anything else worth putting on the map?"
    i "I guess the vault door, since we can't open it anyway..."
    show bankdoordoodle with dissolve:
        xcenter .605
        ycenter .635
    f "Oooo! Draw a duck!"
    b "..."
    i "Right, of course."
    show bankduck with dissolve:
        xcenter .66
        ycenter .55
    b "......"
    b "Okay cool, the map is up to date."
    hide sid ind
    hide lauren ind
    f "Mhm, mhm."
    hide bankposter
    hide banksofa
    hide bankdoordoodle
    hide bankduck
    with dissolve


    show jenny ind:
        xcenter .75
    show frog ind:
        xcenter .25
    with dissolve
    j "So Freddy, what did we talk about?"
    f "Coffee pods are bad for the environment!"
    show jenny happy
    j "Exactly! Wait, I mean, about the safe though."
    f "Oh!"
    f "Don't tell anyone my birthday."
    f "Not even Jenny mom or Lauren mom."
    f "And especially not Sid!"
    j "Exactly!"
    j "You learn so fast."
    show jenny ind
    bi "Maybe not the most elegant solution, but it's a good idea."
    bi "We don't want anyone dying because because they trust Freddy and one other person."
    bi "Having Freddy keep his birthday to himself is a good start."
    f "Bert? Can I play with Sesame?"
    ses "Mrowwwwwwwwwwww!"
    b "Sure Freddy, have fun."
    hide frog ind with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "By the way..."
    s "I didn't find anything notable in the files."
    b "Really?! Nothing useful?"
    j "No records with any of our names?"
    s "Nope. I even went through them all twice."
    b "Shoot... I was really hoping we'd know who to either protect or be wary of..."
    j "Hmm... all the more reason to keep looking around!"
    j "Wait up Freddy and Sesame!"
    hide jenny ind with moveoutright
    show sam:
        xcenter .25
        linear .3 xcenter .5
    s "..."
    show sam angry
    s "Come to the director's office with me."
    s "Alone."
    b "Huh?"

    hide sam angry with moveoutright
    $ showchibint("freddy", "lauren", "jenny", "sid")
    show scary with dissolve:
        alpha .5
    bi "Go to the director's office?"
    bi "I thought Sam didn't find anything useful?"
    bi "Why would Sam want me to be alone unless..."
    bi "..."
    bi "Could this be a trap?"
    bi "Am I going to be the next one dead?"
    bi "....."
    bi "No, no way. Sam isn't going to kill me."
    bi "I should go to the director's office."
    bi "........"
    bi "Yeah, I should."
    scene black with dissolve
    blank "Bert walked to the Director's Office."
    scene bg bankoffice with dissolve
    $ statusnt("Director's Office", "bert", ch=4, sun=4)
    $ showchibint("sam")
    show sam
    s "You're alone, right?"
    b "Umm, yeah."
    b "Why did you want me to come here? Alone?"
    s "Why do you look so uncomfortable?"
    s "Did... you think I was coming onto you?"
    b "What?! No, I thought you were going to kill me here!"
    b "Are you going to kill me?"
    s "No, of course not."
    s "Why did you come if you thought I was going to kill you?"
    b "."
    b "I want to trust that you have all of our best interests at heart."
    s "I do..."
    s "Look, I lied back there in the lounge."
    s "I did find a notable name in the records."
    b "Really!? Great!"
    b "Why didn't you tell us?"
    b "Was it... your name? Or Jenny, or Sid's...?"
    b "I had a feeling it would be one of you guys, who have all had financ-"
    show sam angry
    s "No, you're way off."
    s "It's Freddy's name."
    s "Well, kinda."
    b "Freddy?! He's just a little kid, why was his name in the bank records?"
    s 'Well, it wasn\'t exactly - There\'s someone in here with the name "Gerald Ogden"'
    b "Gerald? Not Freddy, Fred, Fredrick?"
    s "Take a look for yourself."
    blank "Sam handed me a file."
    show geraldfile with dissolve #Arun: Maybe add a pause here so they can quickly digest the file?
    pause 1
    b "Gerald Ogden... interesting."
    b "There's even a picture of him."
    b "Very... powerful eyebrows and mustache."
    b "Do you think this guy is related to Freddy?"
    s "I'd never heard the last name Ogden before, it can't be a coincidence..."
    s "Besides, I didn't see anyone else's name in the files."
    s "If they have any use to us, this is it."
    b "Hmm... Let's see what the file says about him."
    s "Let me know when you see it."
    b "It?"
    show geraldfile2 with dissolve
    hide geraldfile
    b "Wait... $10.3 million..."
    b "Is this how much money he has in his account?"
    s "No, that's how much he made last year."
    b "HE MADE $10.3 MILLION IN ONE YEAR?!"
    s "That's what the document says."
    b "Why is so much stuff crossed out?"
    s "It could be a file only used for specific things, like an audit or taxes."
    s "In cases like that, the bankers will block out everything they don't need."
    b "That makes sense..."
    b "But the $10.3 is clear as day..."
    hide geraldfile2
    b "That's... a lot of... wow."
    b "Freddy comes from a family of multimillionaires?"
    b "No wonder this was put here as motivation..."
    s "That's why I asked you to come."
    b "What do you mean?"
    s "I was worried about presenting this to everyone."
    s "I don't know how they would react."
    s "Honestly, I don't know how {i}I{/i} would have reacted to this if we found before the mansion."
    b "It's not the same for you now?"
    s "Now I'm just... going through the motions."
    s "Doing what I can."
    s "But for someone like Sid or Lauren, or even yourself..."
    s "That's more than life changing money."
    s "Plus, I think showing Freddy would scare the hell out of him."
    b "Yeah, you're right."
    b "It's smart to be hesitant about showing people."
    b "Still, I think talking to Jenny or even Lauren about it would be fine."
    b "I just... don't know what to do with this information yet."
    b "Should we confront Freddy? He's just a kid..."
    s "Well, we don't even know if they're related."
    s "They might just have the same last name."
    s "What if we just ask him his dad's name?"
    b "That's true. If he says his dad's name is Gerald, we can go from there."
    s "But I can't be the one to do it."
    b "What do you mean?"
    s "I think Freddy's scared of me."
    s "And honestly, fair enough."
    bi "Yeah..."
    s "But you, Jenny, or even Lauren could ask him."
    b "Hmm, I don't think he {i}likes{/i} me, but we can make it work."
    bi "The last time I talked to him alone was really awkward..."
    b "Maybe Jenny can help me break the ice."
    show sam:
        xcenter .5
        linear .3 xcenter .75
    show jenny happy with moveinleft:
        xcenter .25
    $ showchibint("jenny", "sam")
    j "Someone say Jenny?"
    s "Speak of the barbie."
    j "Find something juicy?"
    s "We found... something."
    #########blank "Bert and Sam told Jenny about the file."
    show jenny ind
    b "There's a file about someone who could be related to Freddy."
    b "A guy named Gerald Ogden."
    s "He's insanely rich, too."
    s "Easily one of the largest accounts in this whole bank."
    j "How big we talking?"
    b "Last year his main account gained over 10 million dollars."
    j "So Freddy might be... the richest frog ever..."
    b "We're not sure if they're actually related."
    b "Jenny, do you think you can help me talk to Freddy tomorrow?"
    b "I don't want to scare him, but it can't hurt to ask him what his dad's name is."
    j "Sounds like a plan."
    s "Great."
    s "Half of us know about this now, but I still think we should hide the file."
    j "May I take a look?"
    blank "Bert handed Jenny the file."
    show jenny scared
    j "Wait... there's a picture here."
    s "Yeah, he's got a goofy mustache and really unique facial hair color..."
    j "No, no, not that... th-this doesn't make any sense."
    b "What's wrong Jenny?"
    j "The man in this picture... it's unmistakable."
    j "Gerald Ogden? No..."
    j "He's the man that I was... I was arrested for protesting."
    bi "Jenny's story back at the mansion came streaming back to me."
    scene bg mansionbedroom2
    $showchibint("jenny")
    $ statusnt("Bedroom 2", "bert", ch=2, sun=3)
    show jenny ind
    show sepia:
        alpha .3
    with fade
    j "From day one it was so clear he was guilty."
    j "And I mean, guilty guilty."
    j "They had several eye witnesses for tons of different felonies."
    j "And then guess what happened?"
    b "I'm... kinda scared to know."
    j "He was found not guilty, walked out with not even a slap on the wrist."
    j "Everyone at townhall went ballistic... it was the craziest thing I've ever seen."
    j "People started screaming, fighting, crying."
    j "And ya know, I've always been a bit of a loudmouth..."
    j "I may or may not have... screamed some choice words at the judge and jury."

    scene bg bankoffice with dissolve
    $ statusnt("Director's Office", "bert", ch=4, sun=4)
    $ showchibint("jenny", "sam")
    show sam:
        xcenter .75
    show jenny scared:
        xcenter .25
    with fade

    j "This can't be right! His name isn't Gerald Odgen..."
    j "At least, it wasn't back then..."
    s "Slow down, what the hell are you talking about?"
    j "My crime... it after protesting a court decision about... this guy."
    b "Are you sure that's him in the picture?"
    j "I'm positive."
    b "But that's not his name?"
    j "No... he must have been under an alias for some reason."
    j "He definitely had enough money to pull some strings and hide a name."
    s "Well if this really is him, that file's proof of his wealth."
    b "So, the man you were enraged over might be... Freddy's dad."
    j "Th-that doesn't make sense either!"
    j "He didn't have a family, it was even mentioned in his defense."
    s "Maybe that's why he was using a fake name."
    s "If Freddy really is his son, maybe he used a fake name to protect Freddy."
    b "Or protect himself, using that in his defense."
    s "Yeah."
    b "Jenny, are you alright?"
    j "S-sorry, I'm just a little shook..."
    j "I never wanted to see that face again."
    j "And maybe... that's why I'm here. Stuck in this messed up game."
    j "He's taking revenge on me..."
    b "You don't need to scare yourself like that..."
    b "After all, he wasn't even found guilty."
    b "There'd be no reason to hold a grudge against some random girl."
    show jenny ind
    j "That's true, I suppose..."
    j "With all that said..."
    j "I really hope this guy isn't Freddy's dad."
    s "He'd have to be a pretty bad father to outweigh that money."
    j "He's the slimiest businessman I can think of, that's for sure."
    j "His level of corruption would put even Stella's to shame."
    bi "Stella's memory lives on, it seems."
    b "We can hope it's not his dad, but I guess we'll find out soon enough."
    b "It could be important to our situation in this game."
    b "Things just keep getting more intertwined..."
    s "Anyway, we need to do something about this file."
    s "I doubt Sid, Lauren, or Freddy will go looking through the records, but..."
    b "We don't know for sure how they'd react if they did see it."
    s "Yeah."
    s "Is there somewhere we could hide this, just for the night?"
    j "Hmm..."
    show jenny happy
    j "Oh!"
    j "Bert, we could hide the record in one of the locker room lockers!"
    b "That's true, I still have all the keys in my backpack."
    b "I'll drop it off in there when we leave here."
    j "And we can chat with Freddy in the morning."
    j "It might be awkward, but he's just a little kid after all!"
    bi "Seems like she's back in a good mood."
    bi "That's Jenny for you."
    j "Sam, let's head back to the lounge before someone else comes looking for us."
    s "Right."
    hide sam
    hide jenny
    with moveoutleft
    b "Okay, see yo- oh they left."
    b "Welp, I guess I'll go lock these files away and then head back to the lounge."
    scene bg bankhall2
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    with dissolve
    b "Huh?"
    bi "Sid's passed out on the couch over there."
    bi "Unless he's..."
    bi "...not asleep... oh no... is h-"
    i "Honk shooooooooooo!"
    i "Honk shooooooooooo!"
    bi "."
    bi "Okay, he's snoring."
    bi "He did mention that he wanted to sleep out on this couch, so whatever."
    bi "I'll try not to wake him up."
    scene bg banklocker
    $ statusnt("Bank Locker", "bert", ch=4, sun=4)
    with dissolve
    bi "Alright, I guess it doesn't matter which locker I put it in."
    bi "As long as I have the key, nobody else can get in anyway."
    bi "They keys don't say which locker they go to, so..."
    bi "I guess I'll just try one key until it works."
    blank "Bert used the same key a few times until it fit into a lock."
    blank "He shut the files in the locker and put the key back in his bag."
    bi "All locked up."
    bi "Sigh. What a weird situation."
    bi "Between the vault's three-person password and Freddy's name in the file..."
    bi "I'm hoping nobody does anything rash."
    bi "I can't help but be curious, though..."
    show bankposter2
    show sepia:
        alpha .5
    with dissolve
    b '"Use any three of your birthdates, in any order, to unlock the safe."'
    b "Seems easy enough..."
    b '"The vault contains not only a substantial fortune, but also the true secrets of this game."'
    hide bankposter2
    hide sepia
    with dissolve
    bi "What secrets?"
    bi "After all these terrible deaths, I need answers..."
    bi "Time to get back to the lobby."
    scene black with dissolve
    blank "Bert walked back to the lobby, making sure not to wake up Sid on the way."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy", "lauren", "jenny", "sam")
    show jennysleep:
        xcenter .195
        ycenter .5
    #show frogsit2: #Arun: Mask is gone here
    #    xcenter .44
    #    ycenter .48
    with dissolve
    bi "I think everyone's asleep."
    bi "It's not {i}that{/i} late, but I guess everyone's tired out."
    bi "I'm pretty tired, too"
    ses "Mow."
    bi "I guess I'll find a bench to sleep on. I think there's one over there."
    bi "I'll walk slow so I don't wake anyone up..."
    j "Bi...bird. Birdddddddddddd."
    bi "Huh?"
    j "Mmmmmmmmmmm. Bird."
    bi "Jenny's clearly asleep, but she's mumbling something?"
    j "Berttttttttttttttttt..."
    bi "Oh, I, that's me, I'm Bert."
    bi "She's having a dream about me? Or what?"
    bi "Why does my face feel so hot all of a sudden?"
    j "Ber........ shooooooooo.............."
    bi "........................................................"
    bi "Okay, I think she's done, it's time to sleep."
    scene black with dissolve
    blank "The next day..."
    f "Bert! Wake uppp! Everyone's already eating!"
    b "Food?"
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=1)
    $ showchibint("freddy", "lauren", "jenny", "sam", "sid")
    show frog ind:
        xcenter .25
    show jenny happy:
        xcenter .75
    with dissolve
    j "Goooooooooooooooood morning Bert!"
    b "Hey Jenny, Freddy. Good morning."
    j 'Say, why did you keep mumbling "Jen... Jenny..." before we woke you up?'
    b "Huh?! I was? I d-don't think I wa-"
    j "Hahaha, I'm just playing. You were sleeping like a baby."
    f "Yeah! Like a baby!"
    bi "She scared me for a second..."
    j "Here, eat up."
    j "And then let's hang out with Fr-Freddy for a while!"
    bi "Jenny stuttered a bit. I can tell she's a bit uneasy being near Freddy."
    bi "After what we learned, I can't really fault her."
    bi "Jenny handed me a peanut butter protein bar."
    b "Thanks Jenny, I love peanut butter bars."
    f "I picked it!"
    ses "Mrow!"
    hide jenny happy
    hide frog ind
    with dissolve
    bi "These peanut butter bars are pretty good..."
    bi "Anyway, I've got a little while before we're chatting with Freddy."
    bi "Maybe I'll find someone to spend the time with?"
    #FTE 2 GOES HERE
label bank45:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "lauren", "jenny", "sam", "sid")
    show jenny ind
    with dissolve
    j "Alright, you ready to talk to Freddy with me?"
    b "Yeah, let's go to the break room."
    b "A little privacy and some more snacks."
    j "Okay."
    b "Are you sure you're up for it?"
    b "We might found out Gerald is Freddy's dad..."
    j "I'll be okay. He's just a little kid."
    show jenny happy
    j "Hey Freddyyyyyyyyyyyyyyyy?"
    show jenny happy:
        xcenter .5
        linear .3 xcenter .75
    show frog happy with moveinleft:
        xcenter .25
    f "Jenny!"
    j "Want to come get more snacks with me and Bert?"
    f "Do I!"
    scene black with dissolve
    blank "The three of them walked over to the next room."
label bank5:
    show bg bankbreak
    $ statusnt("Staff Kitchen", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny")
    show jenny ind:
        xcenter .75
    show frog ind:
        xcenter .25
    with dissolve
    f "Are there any chocolate bars left!"
    j "I think so!"
    b "Say, Freddy..."
    f "Hm?"
    b "Back at the mansion, we talked a little about your family, right?"
    bi "It was really awkward, but we did."
    b "Can you tell me a little more about them?"
    f "About my family?"
    b "Yeah! Your parents, maybe."
    bi "Jenny rolled her eyes at me... I don't think I'm very good at talking to kids."
    show jenny happy
    j "Whoa! You told Bert all about your family, but not me?"
    j "I'm so jealous..."
    show frog happy
    f "Don't worry Jenny! I'll tell you about them too!"
    bi "She's a pro at this..."
    f "Well, my Mom stays at home and plays with me all the time!"
    f "She's really nice. She's the one who made me my hoodie!"
    j "Wow! No wonder it's so nice!"
    f "Hehe, thanks Jenny."
    j "What about your Dad?"
    show frog ind
    f "My Dad is good too. He's not home as often, though."
    bi "He made a pretty sudden shift in excitement when his Dad came up."
    j "What did you say his name was again?"
    f "His name? Dad!"
    show jenny ind
    j "Haha, but what's his first name?"
    f "Ummmm, isn't it just Dad?"
    j "..."
    f "That's what I call him!"
    j "That's not... Dad is..."
    b "."
    b "Well, what does your Mom call your Dad?"
    show frog happy
    f "Oh! I get it."
    f 'She calls him "Dear"!'
    j "........................."
    bi "This is an unexpected problem..."
    b "Freddy, can you take Sesame back into the lobby for me?"
    f "Always!"
    ses "Mrow!"
    hide frog happy with moveoutleft
    $ showchibint("jenny")
    show jenny ind:
        xcenter .75
        linear .3 xcenter .5
    j "He doesn't know his own Dad's name?"
    j "How is that even possible..."
    j "How are we going to figure out if they're the same Ogdens?"
    b "Hmmm..."
    b "Well, we could show him the file."
    b "There's a picture of the guy who could be his dad."
    b "If he sees it, he'd be able to tell if that's him."
    j "Oh! Great idea Bert!"
    b "But... I was hoping to avoid that."
    b "I don't want to scare him by showing him a picture of his dad in this situation."
    j "Hmm... that's fair."
    j "Maybe we should talk to the others."
    j "I know you were worried about telling them, but I think we have to."
    j "It's just Sid and Lauren."
    b "Well..."
    j "Besides, if Gerald does end up being Freddy's dad, they deserve to know."
    j "Any information that can help us piece this together all is important right now."
    b "...Alright."
    b "Let's just make sure we keep an eye on Sid."
    b "I'll go back to the lobby and fill them in."
    j "Oh! We might want to show them the file, though."
    j "I'll go grab it."
    b "Oh, you're right... okay."
    b "I have the key to the locker in my bag."
    bi "I peaked into my backpack and realized my mistake."
    b "Ummm... I don't know which key it was."
    b "But I know it was the bottom left locker on the wall."
    j "That's fine, I'll just try them until it works."
    show jenny happy
    j "Alright, Team Mystery Busters, let's meet back in the lobby in 10 minutes!"
    b "Team Mystery Busters?"
    j "That's us!"
    hide jenny with moveoutright
    scene black with dissolve
    blank "Bert walked back to the lobby."
    show bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("lauren", "sid", "sam")
    show sid ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    blank 'Bert told Sid and Lauren about the "Gerald Ogden" file.'
    b "..."
    b "... Well? Say something!"
    i "..."
    i "..........."
    show sid mad
    i "What the hell?! $10.3 million?!"
    l "In a year..."
    l "That's... an insane amount of money."
    i "This changes everything!"
    i "I say we kill the runt and use his bones to pry open the vault!"
    b "Calm down, we're going to figure this all out."
    b "We don't even know if they're related, it might just be the same last name."
    l "Plus, it's not like Freddy has the money himself."
    l "He is just a kid, after all."
    i "Well, I... I could get him to tell me his birthday!"
    i "And we could ALL open the safe!"
    i "$10.3 million... I'll even share a bit to whoever gives me the third birthday!"
    b "This is why we didn't want to tell you..."
    b "We just want to figure out if they're actually related."
    b "If they are, we'd need to put extra protection on Freddy from a murder attempt."
    l "I think Sid's the only one you'll have to protect him from."
    i "We need to get into that vault..."
    bi "This is not as productive as I'd hoped..."
    hide lauren ind with moveoutright
    show sam with moveinright:
        xcenter .75
    s "You're such an idiot, Sid..."
    s "Like Bert said, we don't even know if Freddy's related to Gerald."
    show sid happy
    i "Wait a minute - you said there's a picture of this Gerald guy?"
    b "Yeah, in the file... why?"
    i "We can just check if they look similar!"
    s "We would have to make Freddy take off his mask, though..."
    i "Only for a second! He can put it right back on after."
    b "Hmm, you do have a point."
    b "We still haven't even seen his face."
    b "Maybe he wouldn't mind showing us?"
    i "Yeah! And THEN we can whack him for his cash like a piñata!"
    b "Well, probably not that part."
    hide sid with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    b "Lauren, what do you think?"
    b "This way, maybe we wouldn't have to tell him we found his dad's file."
    l "If I ask him, he might be open to it."
    s "I guess it's worth a shot then."
    b "Jenny's grabbing the file from the locker room right now."
    b "She'll be back in a minute."
    l "Poor Freddy either way, he's just a kid... This situation is so messed up."
    s "Yeah..."
    hide lauren
    hide sam
    show scary:
        alpha .5
    with dissolve
    bi "Getting Freddy to take off his mask..."
    bi "It does seem like the most painless solution."
    bi "It's going to be so strange though... I've gotten so used to him being a frog boy."
    bi "How do we even know it's a kid under there?"
    bi "What if... he's a robot?"
    bi "Or a really smart monkey?"
    bi "I sound a bit like Jenny right now."
    bi "He's probably just a harmless little kid, but now I'm nervous..."
    bi "The most important thing is that we can protect him, whether he's related to Gerald or not."
    hide scary with dissolve
    $ showchibint("freddy", "jenny", "lauren", "sam", "sid")
    show jenny happy with moveinright
    with dissolve
    j "Mission success!"
    j "I got the file, and we made it back alive!"
    bi "Usually that expression is an exaggeration, but given the circumstances..."
    b "Great, thanks Jenny."
    b "Anyway, here's the plan."
    show jenny ind
    b "Lauren's going to ask Freddy to take his mask off."
    b "Maybe he has some distinct features that look like Gerald's."
    b "That way, we can infer if him and Gerald are related without telling him everything."
    j "What?!"
    j "That's scary... how do we know if he's even a kid under there?"
    j "What if he's a robot, or a really smart monkey?"
    b "."
    j "But you are right, it's a good plan..."
    show jenny ind:
        xcenter .5
        linear .3 xcenter .75
    show frog ind with moveinleft
    show lauren aw with moveinleft:
        xcenter .25
    l "Freddy! I was just wondering something..."
    f "What is it!"
    l "Well, you really like your frog suit, right!"
    f "Yes! I love it."
    l "Jenny and I were thinking..."
    l "Ehhh, nevermind. Forget it!"
    show lauren ind
    f "What! I want to know!"
    j "Lauren, you shouldn't..."
    f "Shouldn't what?!"
    f "please please please please pleaaaaaase tell me!"
    j "No no no, we shouldn't ask..."
    f "B-but... please?"
    bi "Curiousity really is something."
    l "Okay, okay, fine."
    l "I was wondering..."
    l "What you looked like under your mask!"
    l "You said the face portion is removable, right?"
    f "Y-yes..."
    j "If you're too shy, you don't have to show us!"
    l "But I bet you're reaaaaaaally cute!"
    f "Ummmm..."
    f "Um um um ummmm..."
    show frog happy
    f "Okay!"
    show jenny happy
    show lauren happy
    f "You guys are my friends now, after all!"
    bi "Wow, Jenny and Lauren really are pros at this..."
    j "Yay! Froggy face reveal!"
    show frog ind
    f "Okay, let me unbutton this..."
    f "And then..."
    f "3... 2... 1..."
    hide frog ind
    show frog2 ind
    with dissolve
    f "Ta-da!"
    bi "Oh boy..."
    l "Aw! Freddy, your hair is so cute!"
    show frog2 smile
    f "Hehe, thanks Lauren!"
    j "I could just pinch your little cheeks!"
    f "Hehe! You'll have to catch me first!"
    hide frog2 smile with moveoutleft
    b "..."
    show lauren ind
    show jenny ind
    j "Okay, so they're definitely related."
    l "Yeah, the hair is a dead giveaway..."
    l "Who has naturally mint colored hair..."
    show jenny scared
    j "What do we do now?"
    b "I was really hoping it would just be a coincidence..."
    b "But it doesn't seem like it."
    b "In any case, we need to protect him."
    #b "We already do a pretty good job keeping him occupied, but we have to try even harder now."
    #l "For right now, we are responsible for him, regardless of everything."
    b "I'll stick with him for the rest of the night."
    j "I can't believe I'm stuck here with that man's son..."
    j "It's like some sick joke."
    b "For all intents and purposes, he's just a kid."
    b "It doesn't even seem like he likes his father."
    show jenny happy
    j "Yeah, and at least he really is cute!"
    j "Some kids his age are butt ugly, haha!"
    j "Let's get everyone together again and meet up to talk in a bit."
    j "Say, an hour in the lounge?"
    hide jenny happy with moveoutright
    $ showchibint("lauren", "sam", "sid")
    show lauren ind:
        xcenter .25
        linear .3 xcenter .5
    l "Jenny seems pretty shaken by this."
    l "I can't blame her, but... maybe she should keep an eye on her."
    b "There's a lot to take."
    b "Two more people dead, Gerald's file, the vault..."
    l "Speaking of the vault, I guess that means Freddy really is filthy rich." #Arun: Frog boy
    l "And that means the bank records are most likely real."
    l "It makes me wonder how much money really is in the vault..."
    b "Not enough to risk dying to get into it."
    b "Anyone could lie about their birthday, and we'd have no idea it was."
    l "Yeah, I know, I know."
    l "I just can't help but be curious."
    hide lauren with moveoutright
    show sid ind with moveinleft
    i "Oy, that kid really is loaded then, huh."
    i "Little punk..."
    i "Say, what are the odds he set this whole thing up somehow?"
    b "You saw that he's like, eight, right?"
    i "Okay or he's like that movie about the guy who ages backwards!"
    i "Alright, he's eight... but with that much money, maybe he did have something to do with it?"
    i "I mean, to set all this up..."
    i "It must have been someone with boatloads of cash like that."
    b "You're not wrong... Freddy's family probably is involved somehow."
    b "The more we learn, the more it seems like we are all interconnected somehow."
    b "Stella with her business, Dracula and Shahar having a prior relationship..."
    b "Still, I don't think Freddy's the Game Master."
    b "He doesn't even know his dad's first name, and this is a bit more complex than that."
    i "Yeah, yeah..."
    i "Anyway, I don't think I can get into the vault without the birthdays."
    i "This bank tech is way too much for me."
    i "And that steel is really hard..."
    b "It's good that you tried, though."
    b "But until we run out of food we shouldn't even think about it."
    b "It's way too risky."
    i "Yeah, alright boss."
    i "But if it really is full of cash, you're getting the smallest cut."
    hide sid ind with moveoutright
    bi "He's... a good kid. Very driven, at least."
    bi "I think I was rebelious around his age too."
    bi "I've got a while until I need to meet back up with everyone."
    bi "Let's find someone to talk to."
    #FTE 3 goes here
label bank7:
    scene black
    blank "After some free time, Bert met with the others in the lobby."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("lauren", "freddy", "jenny", "sid", "sam")
    show sam
    with dissolve
    s "I think everyone's here."
    s "Do you really have any plan to protect Freddy?"
    b "Well..."
    b "It depends how strict your definition of plan is."
    b "I'll do everything in my power to protect him, it's just..."
    show sam:
        xcenter .5
        linear .3 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    l "We don't really have a lot of power."
    b "Yeah..."
    l "Still, I think at the very least we can take turns watching him very closely."
    l "Almost the level of constantly holding his hand."
    hide sam with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "That reminds me, actually..."
    j "Remember back on the train, when Dan's murder happened?"
    j "I was holding Freddy's hand the whole time the lights were out."
    b "I do remember, you two were right next to me."
    b "Maybe that's the solution we need."
    show jenny happy
    j "Or a leash!"
    b "A leash? For Freddy?"
    j "I mean, it would work!"
    show jenny ind
    b "Hmmm, mayne not the best idea."
    b "But for now, keeping him within arm's reach is a good plan."
    b "I'll keep him joined at my hip for the rest of the night."
    b "Lauren, can you take over in the morning? Then we can plan from there."
    l "Sure."
    bi "It'd be great to have a third person to watch him, but..."
    bi "Maybe I shouldn't force Jenny alone with him."
    j "Alright, if we're settled here, I'm gunna hit the locker room!"
    j "A nice hot shower would hit the spot right now."
    j "Lauren, wanna come with me?"
    l "I won't join you in the shower, but I would like to explore this place a bit more."
    hide jenny ind
    hide lauren ind
    with moveoutright
    $ showchibi("freddy", "sid", "sam")
    show sam:
        xcenter .75
    show sid ind:
        xcenter .25
    with moveinleft
    i "Why didn't Jenny invite me to go shower..."
    s "You're such a dork."
    s "Anyway, I'm going to follow Lauren."
    s "I've only gotten a quick look at the locker room."
    s "We'll try not to wake you and Freddy up if you're sleeping when we get back."
    b "Thanks Sam."
    hide sam with moveoutright
    $ showchibi("freddy", "sid")
    show sid ind:
        xcenter .25
        linear .3 xcenter .5
    i "I'm beat."
    i "Imagine, money and a solution to all this. It's so close, but out of reach..."
    i "I get this whole Gerald thing is important, but it's hard not to think about the vault."
    b "I'll tell you what, Sid."
    b "If we get into the vault, you can have my share too."
    i "Thanks Bert. I was already planning on taking it, but thanks."
    bi "This kid..."
    i "I'm gunna hit the hay."
    i "That couch in the hallway was super cozy last night, gotta go claim it again!"
    hide sid with moveoutright
    $ showchibi("freddy")
    show frog2 ind
    f "Let's do arts and crafts!"
    b "Aren't you tired?"
    b "It's pretty late Freddy!"
    f "Not tired not tired!"
    f "Bedtimes are for little kids."
    bi "I guess there's no reason to force him to bed early."
    b "Hmm... I think there are some supplies in the office."
    b "Let's go do some arts and crafts!"
    show frog2 smile
    f "Yay yay yay yay!"
    scene black
    blank "Bert and Freddy walked to the Director's Office."
    scene bg bankoffice
    $ statusnt("Director's Office", "bert", ch=4, sun=4)
    $ showchibint("freddy")
    show frog2 smile
    with dissolve
    b "Alright, there's some crayons, paper, and pencils here."
    b "Go crazy."
    f "Yay!"
    hide frog2 with moveoutleft
    bi "He's right to work, drawing something that looks like a... large chicken?"
    bi "I'm amazed how cheerful this kid can stay, given everything."
    bi "I don't think I'd be able to handle all this trauma at his age."
    bi "I... hope that doesn't mean he's used to it."
    bi "In any case, I should try to make myself useful."
    bi "Let's see..."
    blank "Bert sat down at the desk with a peice of paper."
    show bg bertmap
    bi "So. Time to arrange some thoughts."
    bi "We're learning more and more about how everyone is related."
    bi "Maybe mapping it all out can help me make a plan to keep everyone safe."
    bi "I'll start by..."
    show bg bertmap1 with dissolve
    bi "Writing everyone out."
    bi "The twelve of us that we started with."
    bi "And a spot in the middle for what might be tying us all together."
    show bg bertmap2 with dissolve
    bi "Mr. Sydell."
    bi "Too many of us have connections to him to ignore."
    bi "Alright. Freddy and Jenny."
    show bg bertmap3 with dissolve
    bi "Freddy's dad's case kinda sorta lead to Jenny's arrest."
    bi "Jenny hates Freddy's dad, and maybe his dad knows about Jenny?"
    bi "Unfortunately, that's all we really know about them."
    bi "No direct connection to Mr. Sydell that we know of."
    bi "Next up is..."
    show bg bertmap4 with dissolve
    bi "Sid."
    bi "Sid got blackmailed into hacking InSyde Electronics, Mr. Sydell's company."
    bi "I don't think he's personally met Mr. Sydell, but there's a clear connection."
    bi "The same situation had him caught up with Shahar, pre-lobotomy."
    bi "Speaking of Shahar..."
    show bg bertmap5 with dissolve
    bi "This is where it all starts to get messy."
    bi "Shahar, Ivan, and Stella were all pretty intertwined."
    bi "Stella's company was suing Insyde."
    bi "Shahar was a lawyer hired to bring down Insyde Electronics."
    bi "If Mr. Sydell is behind all this, it makes a lot of sense for them to be here..."
    bi "And of course, Ivan is responsible for Shahar's lobotomy."
    bi "I don't think she had met either of them personally at the time, though."
    bi "I think that's the most complicated bit..."
    bi "From there..."
    show bg bertmap6 with dissolve
    bi "Catherine and Sam."
    bi "Both of them had been in Mr. Sydell's mansion before."
    bi "Catherine had robbed the place, in and out only one time."
    bi "Clear connection, but not much for us to go off of."
    bi "Sam on the other hand had been there multiple times to sell him drugs."
    bi "And I think..."
    show bg bertmap7 with dissolve
    bi "That's all the prior connections."
    bi "We don't have an clear connections between myself, Lauren, Dan, or Kaiser."
    bi "Though, it's pretty easy to imagine how we could have upset Mr. Sydell..."
    bi "Lauren and I have both accidentally... killed someone."
    bi "They could have been people close to Mr. Sydell, or whoever the Game Master is."
    bi "Kaiser was responsible for a massive train heist, and Dan had just come from jail."
    bi "I'm sure we all have some type of relation, we just haven't uncovered everything yet."
    bi "Unfortunately, doing so will be hard..."
    show bg bertmap8 with dissolve
    bi "...with 6 of us dead."
    bi "The only ones still alive with connections to Mr. Sydell are Sid and Sam."
    bi "Sid's is pretty one sided though; it's not like he ever met Mr. Sydell."
    bi "He just caused the company some trouble."
    bi "Sam, however..."
    show bg bertmap9 with dissolve
    bi "...may have actually met Mr. Sydell."
    bi "We don't actually know the full extent of their relationship."
    bi "Maybe this is the missing link I've been ignoring!"
    bi "Sam might have useful information about Mr. Sydell, even if it's small."
    bi "Ever since Ivan's died, Sam's been struggling a bit, but has been helpful."
    bi "I think they'd be supportive and tell me anything they could."
    bi "Maybe this is a breakthrough!"
    bi "I'll talk to Sam ASAP, and we'll all get out of here alive."
    f "Hey Bert dad?"
    b "Oh! Freddy."
    show bg bankoffice
    show frog2 ind
    with dissolve
    f "Bert, I'm starting to get tired..."
    f "Can we go back to the sleeping room now?"
    b "Yes, of course Freddy."
    b "Thanks for hanging out with me Freddy, this time has been really helpful."
    f "Huh?"
    b "Let's head back to the lobby."
    scene black
    blank "Bert and Freddy walked back to the lobby."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy")
    show frogsit2: #Arun: Mask is gone here
        xcenter .44
        ycenter .48
    with dissolve
    bi "He passed out almost instantly when we got back in here."
    bi "...I guess, Jenny's right, he is kinda cute."
    bi "Anyway, it feels great having {i}some{/i} direction, however small."
    bi "If Sam really can give us any new information about Mr. Sydell, we'd be in a good spot."
    bi "A small weight feels lifted off my shoulders."
    bi "And there's a new feeling... almost... excitement?"
    bi "We're getting closer to learning the secrets of this game."
    bi "We're getting closer to getting out of here aliv-"
    show bg banklobby1 #music change
    show lauren pixel:
        xcenter .85
        ycenter .52
        zoom 1.3
    blank "POW POW POW POW!!!"



    #map out all interactions
    #we'll talk to sam
    #go back to lounge, wait a bit
    #BARGE IN
