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
    bi "No, Ivan."
    bi "Despite everything, I don't hate him."
    $mood = "ind"
    bi "I can't hate him."
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
    s "Tsk... what a disaster"
    b "Is everyone okay?"
    show lauren ind with moveinleft:
        xcenter .25
    show sam:
        linear .3 xcenter .75
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
    hide frog ind with moveoutleft
    show sid mad with moveinleft:
        xcenter .25
    i "Yeah! That bastard did this to us."
    i "Treating us like damn lab rats, it's disgusting!"
    b "You're right, but think about it from his point of view."
    show sid ind
    b "What options did he have?"
    b "If he hadn't done it, who knows what the Game Master would've done to him."
    i "..."
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
    s "We need to know what we're dealing with here."
    b "Agreed."
    b "This room seems like... a lobby? For some type of business."
    s "There looks like a floor-plan on the wall over there."
    hide sam with dissolve
    show bankposter with dissolve
    b "Oh wow, this is interesting!"
    s "Why do you say?"
    b "None of the other places we've been put have given us a map."
    b "With this, we know what we're getting into, at least a little bit."
    l "That star must indicate our current location."
    l "It says we're in the \"lounge\" right now, which makes sense."
    i "Wait a minute, does that say... vault?"
    i "Like, a BANK VAULT?"
    b "Yeah, I think we must be in a bank."
    hide bankposter with dissolve
    show sid happy with dissolve
    i "So if I go out this door and down the hallway.."
    i "There's a bank vault?"
    i "That nobody's guarding, probably?"
    b "Uhhh, that is what this map says..."
    b "But-"
    i "See ya!"
    hide sid happy with moveoutright
    $ showchibint("lauren", "freddy", "jenny", "sam")
    bi "Sigh."
    bi "We should probably go after him."
    show jenny happy:
        xcenter .75
    show frog happy:
        xcenter .25
    with moveinleft
    j "Come on Freddy, let's follow Sid!"
    f "Yes ma'am!"
    j "We can't let him get all the money for himself!"
    hide jenny happy
    hide frog happy
    with moveoutright
    $ showchibint("lauren", "sam")
    show sam with moveinleft
    s "We'll need to come back to explore this room more in a bit."
    b "Agreed. We can circle back here at the end."
    b "Plus, with all the couches, this seems like a good meeting spot."
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
    l "No offense to some of our fallen friends but..."
    show lauren ind
    l "It was really difficult to work with Stella, Dracula, or Shahar..."
    l "Everyone in this core group is cooperative and pretty... normal?"
    l "Other than Sam - who's seemingly turned a corner - I'm not scared of anyone here."
    b "Yeah, you're right."
    show scary with dissolve:
        alpha .5
    bi "She's right - this group is pretty trustwrothy."
    bi "The only issue is, that makes it even harder to pick out the Game Master..."
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
    l "They're probably in that next room on the left."
    l "If the map was accurate, that should be..."
    hide lauren ind with dissolve
    show bg bankbreak with dissolve
    $ statusnt("Bank Staff Kitchen", "bert", ch=4, sun=2)
    show lauren ind with dissolve
    l "... the staff kitchen."
    $ showchibi("freddy", "jenny", "lauren", "sam")
    show lauren ind:
        linear .3 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "This room's about what I'd expect."
    j "A sink, coffee machine, some snacks."
    bi "I could go for some coffee and snacks right about now..."
    l "Not exactly a meal, but I can grab something for Freddy."
    hide lauren ind with moveoutright
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
    b "I'd agree if it wasn't for the circumstances..."
    show jenny happy
    j "Hmmm, I'm not sold."
    j "There's probably a more reasonable explanation."
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
    scene bg bankhall2
    $ statusnt("Bank Hallway", "bert", ch=4, sun=2)
    $ showchibint("sid", "sam")
    show sid mad:
        xcenter .75
    with dissolve
    show sam angry with moveinleft:
        xcenter .25
    b "Sid, we finally caught up with you!"
    i "HEY! Back off, this is gunna by MY MONEY!"
    s "What are you talking about?"
    show sid ind
    i "Sorry for snapping at you guys."
    i "I just... well think about it!"
    i "There's probably a TON of money in here..."
    s "Hmm... that's a good point."
    show sam angry
    s "Sid, let's split it all 50/50."
    i "70/30."
    s "60/40 for your finders fee, final offer before we throwing hands."
    i "Deal!"
    show sam
    b "Uhhh guys, what about me?"
    b "Wait, what am I saying? We aren't robbing the bank vault!"
    b "Besides, is it even open?"
    i "...No, I can't open it."
    i "There are numbers around the lock wheel, but I don't know the code."
    s "Maybe we can force it open?"
    b "Well, there's no harm in trying."
    b "But it is literally a bank safe, I can't imagine you can force it open."
    show sid mad
    i "Don't underestimate me!"
    i "I'm a man!"
    show sid ind
    i "S-sorry."
    i "I'll keep trying."
    s "Maybe we'll find a way to unlock it elsewhere in the bank."
    s "It's probably written down somewhere."
    b "That's possible, yeah."
    b "Let's keep exploring, Sam."
    b "Sid, call for us if you manage to open it!"
    i "Maybe after I take my share..."
    i "O-oh I mean, yes, will do."
    s "Punk..."
    hide sam with moveoutleft
    scene black with fade
    blank "Bert and Sam walked back toward the only room they passed by."
    scene bg bankoffice
    $ statusnt("???", "bert", ch=4, sun=2)
    $ showchibint("sam")
    show sam
    with dissolve
    b "So according to the map in the lobby, this should be..."
    b "the Director's Office."
    $ statusnt("Director's Office", "bert", ch=4, sun=2)
    s "What's a bank director anyway?"
    b "I have no idea."
    b "Let's snoop around, maybe we can find out."

    #is sam sad about ivan
    #jenny comes in, her and bert invest the locker room
