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
    bi "No, Vladimir."
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
    b "At the very least, now we know that Vladimir is the one that set them up."
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
