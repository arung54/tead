scene black
blank "....."
blank "........."
blank "..............................................................................................................."
blank "I had just gotten out, too."
blank "A shame, really."
show bg start with fade:
    alpha .1
m "{i}Where... Where am I?{/i}"
m "{i}Why can't I... Remember how I got here?{/i}"
m "{i}My head is throbbing...{/i}"
m "{i}I see some people laying down over there.{/i}"
m "{i}Or are they... Bodies?{/i}"

scene black
m "........"
m "{i}I think I passed back out...{/i}"
m "{i}I have to... Get up...{/i}"
scene bg start
m "{i}.....!{/i}"
z "It looks like he's awake."
show sam with dissolve
z "Hey - are you alright?"
m "Who are you? Where am I?"
hide sam
show bert sad with dissolve
z "I guess that means he doesn't know anything more than we do."
b "You can call me Bert."
show bertchibi:
    zoom 1.5 xpos 20 ypos 20
b "I woke here a few minutes ago, followed shortly by,"
show bert sad:
    xcenter .5
    linear 0.3 xcenter .75
show sam:
    xcenter .25
show samchibi:
    zoom 1.5 xpos 20 ypos 68
b "Sam, who was passed out over there agianst the wall."
s "We need to figure out what's going on... What's your name?"
m "My name..."
n "My name is Daniel. You can call me Dan."
b "Alright Dan, surely you know {i}something{/i} about what's going on?"
n "...I wish I did. I have no idea how I got here, or where here even is..."
n "Is there an exit?"
hide sam
hide bert sad
blank "I noticed a big steel door behind us."
blank "The door knob wouldn't turn, and there's no key hole."
show bert sad with dissolve:
    xcenter .75
show sam with dissolve:
    xcenter .25
s "Yeah, the door won't budge. Even scarier than that though,"
s "I think that's one way glass along the wall..."
b "I've been trying to whisper, there's a chance someone is watching us."
n "Well? What the hell are we going to do then?"
n "Are we just stuck in here like animals?"
play sound "beep.mp3"
centered "{size=+30}BEEP!{/size}"
play sound "butt.mp3"
centered "{size=+30}CLICK!{/size}"
n "What was that?"
s "Quick, check the door!"
b "Be careful! We don't know what's past here."
n "..."
hide sam
hide bert sad
blank "We ran to the door and sure enough, it was unlocked."
scene black
blank "We were greeted by a very similar room, but many new faces."
scene bg startmeet
show bertchibi:
    zoom 1.5 xpos 20 ypos 20
show samchibi:
    zoom 1.5 xpos 20 ypos 68
show sam with dissolve
s "Let's just get all the pleasantries out of the way."
s "Everyone, introduce yourselves and if you know anything. I'm Sam."
hide sam
show stella ind
t "Certainly. I am Stella Cartier, you may know of me from Cartier Inc."
show stellachibi:
    zoom 1.5 xpos 20 ypos 116
t "I dont know how I got here, but I have work to do, so let's finish up whatever this is quickly."
show stella ind:
    xcenter .5
    linear 0.3 xcenter .75
show sid ind:
    xcenter .25
z "I... Don't think it's our choice, ma'am? Where even are we?"
t "Don't you dare call me ma'am, I'm young enough to be your sister. Hmph."
hide stella ind with moveoutright
show jenny ind with moveinright:
    xcenter .75
j "I'm Jenny. Your nametag says Sid, can we call you that?"
show jennychibi:
    zoom 1.5 xpos 20 ypos 164
i "Yea-yeah. Sid works."
show sidchibi:
    zoom 1.5 xpos 20 ypos 212
hide jenny ind
show jenny happy:
    xcenter .75
j "Not sure where we are though! It's kinda exciting, right?"
j "Like an escape room!"
hide jenny happy with moveoutright
i "..."
hide sid ind with moveoutleft
show bert sad with dissolve
b "I mean, maybe, but we still have no idea how we ended up here..."
n "Yeah, it's more worrying than exciting."
show bert sad:
    xcenter .5
    linear 0.3 xcenter .25
show catherine ind with dissolve:
    xcenter .75
c "I'm Catherine, and this is Sesame."
show catherinechibi:
    zoom 1.5 xpos 20 ypos 260
ses "Mooeowowwwwwwwwwww!"
c "I agree, Sesame. We're scared, what's going on?"
c "We were out on a walk, and next thing we knew, we're knocked out in a dusty room."
