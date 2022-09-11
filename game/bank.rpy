label bankGo:
    $noside = True
    scene black
    $ statusnt("???", "", ch=4, sun=0)
    z "Dad?"
    z "Is that you?"
    sy "Hey... yeah, it is."
    syc "You don't look so good..."
    syc "Long day at work?"
    sy "Something like that..."
    syc "Dad... I thought your company went bankrupt a few months ago, after the lawsuit."
    syc "What work are you still doing?"
    sy "Just because the lawsuit's over, doesn't mean I have to accept the result."
    sy "There's... things I can do to make things right."
    syc "Dad... we have enough money to last for decades."
    syc "You could retire and live a peaceful life."
    syc "We could... we could spend time together."
    syc "Mom..."
    syc "She... she might still be here if you were back home."
    sy "What did you say?"
    sy "How dare you blame that on me!"
    sy "I loved her, I would never-"
    syc "But... she was only in that accident because of her condition."
    syc "If you were around she would have been so much happier..."
    sy "I wish I could have been around."
    sy "But I had business to take care of."
    syc "No, dad."
    syc "I've had enough."
    syc "Stop with the lies, please."
    syc "Those businesspeople, they're evil, I get it."
    syc "But you could've spent more time with mom after the lawsuit!"
    syc "Instead you're... well, I don't know what exactly."
    syc "But it's nothing good."
    syc "And I think it has to do with drug dealers."
    syc "Mom told me. You're taking... something."
    sy "What?"
    sy "How..."
    sy "How... how did she know?"
    syc "You think we haven't noticed?"
    sy "Noticed what?"
    syc "I don't know anything about drugs."
    syc "But... you're not the same."
    syc "Even before she died, before the lawsuit..."
    syc "There's been changes in behavior."
    syc "Missing a button on your suit."
    syc "Bloodshot eyes."
    syc "Bags under them."
    sy "I've just... been tired, that's all."
    syc "Bullshit!"
    syc "When you started the company, you were working sixteen hour days, six days a week."
    syc "I remember crying so often and Mom had to tell me you were taking care of us."
    syc "But even those days, when I saw you, you weren't like this."
    sy "You're a child, you don't understand."
    sy "Those people are evil."
    sy "Sure, I could come back and live a quiet life with my loved ones."
    sy "But they'll still be out there."
    sy "When we were preparing for the lawsuit our lawyers said there was a trust-busting angle here."
    sy "That Cantoire Holdings was just trying to eliminate competition unfairly."
    sy "This isn't the first time they've done this you know."
    sy "They're destroying small businesses left and right."
    sy "Destroying the heart of the econo-"
    syc "Dad."
    syc "I get it, you hate them."
    syc "Get to the point."
    sy "The point is, if I can stop them..."
    sy "I have an obligation to."
    syc "So what are you going to do?"
    sy "..."
    syc "..."
    syc "......"
    zg "Hey, did you hear me?"
    syc "Huh, sorry?"
    zg "You were daydreaming."
    zg "I said the man who killed your father turned himself in."
    zg "His name is Dan Scagnelli."
    zg "If you want to, we can take you to the station to talk to him."
    syc "Detective... did he say why?"
    zg "Why?"
    syc "Why he did it... why he killed my dad."
    zg "Dan Scagnelli is a hitman."
    zg "He probably got the order to do it from somebody."
    zg "The business doesn't exactly involve signing contracts for obvious reasons, but..."
    zg "He probably agreed to not reveal his employer if arrested."
    zg "With the understanding they'd get him killed if he was."
    zg "That's partially why we wanted to bring you to him."
    zg "Figured he might talk if he saw that your father had a child."
    syc "...No need, I can guess who it was."
    zg "You can?"
    zg "Then tell us! We can bring them in too."
    syc "No... it's not worth it."
    zg "What do you mean?"
    zg "Surely bringing a criminal to justice is worth it?"
    syc "..."
    zg "Please, tell me what you mean."
    syci "Dad tried already."
    syci "It was one of the last things he told me before he died."
    syci "The justice system is broken."
    syci "It fails to indict criminals and arrests the innocent."
    syci "The criminals it does catch, it lets go far too soon."
    syci "The only way to stop evil... is to eliminate it outside the justice system."
    $noside = False
    scene black
    blank "In the present..."
    $ftecounter = 8
    scene black
    $mood = "sad"
    bi "Two more people dead..."
    bi "Shahar... and Dracula."
    bi "No, not Dracula. Ivan."
    bi "Even after his death he deserves to be called his real name."
    bi "Do I hate him? I think so."
    bi "I think I have to."
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
    bi "One by one, we slowly woke everyone up."
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
    b "We know Sid, Shahar, Dracula, Stella, and Mr. Sydell are all connected via this one lawsuit."
    b "Catherine robbed Mr. Sydell."
    b "And Sam has interacted with him before."
    b "Though it's still not clear how Freddy, Jenny, Kaiser, Dan, Lauren, and I are connected..."
    b "That's a whole lot of us that have seemingly no connection to the rest..."
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
    b "None of the other places we've been put have given us a map."
    b "With this, we know what we're getting into, at least a little bit."
    l "That star must indicate our current location."
    l "It says we're in the \"lounge\" right now, which makes sense."
    i "Wait a minute, does that say... vault?"
    i "Like, a BANK VAULT?"
    b "Yeah, I think we must be in a bank."
    b "I wonder why this is here in the first place."
    l "It's probably a safety thing? So the bank employees know where the exits are."
    l "You know, like how schools have maps for evacuation in case of a fire."
    b "Though as far as I can tell, there's only one exit..."
    s "Maybe it was just put here for this... situation."
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
    l "Well, Sid is normal when stuff like the safe isn't involved..."
    l "But other than Sam - who's seemingly turned a corner - I'm not scared of anyone here."
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
    l "...the kitchen."
    $ showchibi("freddy", "jenny", "lauren", "sam")
    show lauren ind:
        linear .3 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "This room's about what I'd expect."
    j "A sink, coffee machine, and a fridge with some snacks."
    b "I could go for some coffee and snacks right about now..."
    j "Well, there is some."
    b "Hm... but it might be like the train where it only will last us a few days..."
    b "We just \"woke up\" so maybe not now."
    show jenny ind:
        xcenter .25
        linear .3 xcenter .3
    b "That poster on the wall seems like it's mocking us..."
    ses "Mrow..."
    l "The Game Master has some sick sense of humor."
    show jenny happy
    j "Aww, really? I think it's cute!"
    j "It's your cousin, Sesame!"
    ses "Hssssss"
    b "He seems... a bit combative towards the cartoon cat."
    l "Anyway, having access to food is nice."
    l "Maybe not a nutritious meal, but I'll see if I can grab something for Freddy."
    hide lauren ind with dissolve
    show jenny ind:
        linear .3 xcenter .5
    j "Pretty dinky kitchen for how fancy the lobby was, huh?"
    j "I guess it doesn't have to look pretty if the customers don't come in here."
    b "The boss here probably doesn't want the workers spending too much time here..."
    b "Regardless, any place with food is good enough for me."
    b "Still, I can't help but wonder..."
    b "Why a bank? Why did the Game Master bring us here?"
    j "What do you mean?"
    b "Well, so far, we've been brought to places that are significant to one of us."
    b "Kaiser's train heist, Catherine's burglary..."
    b "If feels like the implication is... that one of us has robbed this bank."
    j "Huh?!"
    j "No way! Nobody here is capable of that."
    b "I'd agree, if it wasn't for the circumstances..."
    b "But that's definitely my first impression."
    show jenny happy
    j "Hmmm, I'm not sold."
    j "There's probably a more reasonable explanation than robbery."
    j "Maybe someone just... stole some of the snacks from the break room!"
    j "That's a crime too, ya know!"
    hide jenny happy with moveoutright
    show scary with dissolve:
        alpha .5
    bi "Jenny might be right, I don't think anyone here could have robbed a bank."
    bi "Well, except for one person..."
    bi "Sid. Just the thought of money turns him into another person."
    bi "But if he's robbed this bank before, why is he so excited?"
    bi "Is it just bad acting?"
    bi "But I also wouldn't have thought the others were capable of what they did..."
    bi "Plus, we already know Sid was in a tough financial situation, so..."
    bi "Thinking he did something extreme isn't out of the question."
    bi "It's worth remembering."
    bi "Speaking of Sid..."
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
    b "I'm gonna go look for him."
    l "We'll stay here for a bit and check out all these cabinets."
    f "And snacks!"
    bi "Hey, that's normally my job..."
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
    s "I spent some time thinking about what Lauren said to me at the hospital."
    s "I think after everything, the least I can do is try to be helpful."
    b "I... appreciate that."
    b "We all do."
    b "You know, we still trust you."
    b "We understand that you just did what you thought you had to do."
    s "Yeah, yeah, whatever. Let's just go find Sid."
    hide sam with moveoutright
    bi "Well, progress."
    scene black with dissolve
    bi "We walked out into the hallway and heard Sid's voice."
    bi "Following it led us to..."
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
    b '"Each of you possesses one third of the bank vault passcode..."'
    b '"The day of the month you were born on."'
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
    s "How can I trust you to give me your correct birthdate?"
    s "How can you trust me to give you mine?"
    b "If someone lied, the user would die..."
    s "Yeah, and we wouldn't know who the killer is."
    b "Huh?"
    s "Since you need three numbers, there are two people who could've lied about their number."
    s "So if someone died inputting the wrong code, we would have no way to know who lied."
    b "Well, if we knew whose three birthdays were used, we'd have a 50/50 shot, right?"
    s "Yeah, but with six of us left..."
    s "Well, five after a murder."
    s "50/50 isn't that much of an improvement over random guessing."
    s "Hell, given our track record of solving these murders..."
    s "50/50 is better odds for the murderer than any other setup."
    b "It seems like the perfect setup to kill Sid, huh..."
    i "Hey! I-I knew all that..."
    i "Maybe..."
    s "To top it all off, we don't even know if it's true."
    b "Yeah, it could just be a trick, an empty promise to get us to kill each other."
    b "For all we know, successfully opening the safe instantly kills ALL of us."
    s "What a mess..."
    i "Ummm... maybe we could... guess?"
    i "The poster says all of us have a code, and we can use any three in any order."
    i "Let's see, carry the two... multiply this by that... oh wait..."
    b "There are only six of us, which means there are... 120 correct passcodes."
    i "47! Uh, I mean, 120!"
    b "And that's assuming we all have different birthdates."
    i "That seems like a bunch, right?"
    i "Most locks only have one correct combo, 120 is a lot of options!"
    b "There are 31 days in a month though, and you'd have to guess two numbers, so..."
    i "Two? The safe needs three numbers!"
    s "Yeah but you know your own birthday, right?"
    s "...Right?"
    i "Oh, yes! So you'd only have to guess two numbers!"
    b "In total, your odds are 20/961 to guess correctly if I'm doing the math right."
    i "WHAT?! Are you sure?!"
    i "Math is so lame dude..."
    s "Sid, did you have a locker in school?"
    i "Yeah! That's where I hid my... um, my homework."
    s "I take it you've never messed up the locker combo before?"
    i "What? Everyone messes it up sometimes... I always scroll past the second number on accident."
    i "...Oh."
    s "Yeah, would be a real shame if you messed up this locker combo."
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
    s "Right, the same people who made that grungy kitchen want to decorate the bank."
    b "I agree, it's probably for function over form somehow."
    b "Maybe it's a way to show the vault is locked?"
    i "Oh, maybe it's in case the lights go off!"
    i "Like those lights on planes!"
    s "How do you know planes have lights?"
    i "Hey, my family wasn't always poor..."
    b "C'mon, focus."
    b "Maybe it's an indicator that the security system is armed?"
    b "That would make it easier for workers to know the status of the vault, from any side."
    s "Maybe the lights would turn off if we managed to get into the vault?"
    b "We should keep it in mind."
    b "Let's keep exploring, Sam."
    b "Sid, don't touch the safe!"
    i "..."
    s "Punk..."
    hide sam with moveoutleft
    scene black with fade
    bi "We walked back to an entrance we passed while trying to find Sid..."
label bank3:
    scene bg bankoffice
    $ statusnt("???", "bert", ch=4, sun=2)
    $ showchibint("sam")
    show sam
    with dissolve
    b "So according to the map in the lobby, this should be... the director's office."
    $ statusnt("Director's Office", "bert", ch=4, sun=2)
    s "What's a bank director anyway?"
    b "I have no idea."
    b "Not like I've ever worked at a bank before..."
    s "Sounds like something the murderer would say."
    b "Har har."
    b "Seriously though, let's look around, maybe we can find out more about this place."
    s "You'd think there would be a computer in here..."
    b "It looks like there was one on the desk."
    b "I can see the marks where a monitor and a mousepad must have been."
    b "Surely most banking stuff is done electronically rather than with paper these days?"
    s "If their business was anything like mine..."
    s "They probably had some stuff they didn't want a permanent record of."
    bi "Right. I keep forgetting Sam dealt drugs once."
    s "There is a filing cabinet over there, though."
    hide sam with dissolve
    bi "Sam took a peek in the filing cabinet."
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
    bi "I quickly got Jenny up to speed on the bank vault."
    j "That's terrifying! Maybe we can have Sid enter the passcode."
    s "That's what I said too."
    b "We've agreed not to touch it unless we can't make progress otherwise."
    j "Gotcha!"
    b "Anyway, digging through these filing cabinets could be useful."
    b "Sounds incredibly tedious though."
    j "Oh no... paperwork."
    s "You two can go on ahead."
    s "I'll sift through this stuff."
    b "You sure?"
    s "Yeah, if there's anything important I'll let everyone know."
    j "Shouldn't two of us go through it?"
    j "Dracula deleted some crucial info about Shahar in the hospital..."
    s "Do you want to dig through the cabinet with me?"
    j "..."
    j "You know what, I think I trust Sam!"
    s "Yeah, figured as much."
    b "Thanks Sam."
    s "Yeah, if you don't see me in a few hours make sure I haven't fallen asleep."
    s "It's gonna take hours to get through this..."
    b "I agree, but if it can help us get out of here alive, it's worth it."
    s "Yeah. I guess we'll see."
    j "There should be one more room we can get into at the end of this hallway."
    j "Come on Bert, let's go check it out."
    b "Alright."
    scene black with dissolve
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
    b "Maybe this building used to be a gym and they repurposed it?"
    b 'And they just used a "first come, first served" situation to grab any locker you want.'
    j "I'm a bit worried about people coming here to hide stuff in a locker..."
    j "Maybe we should take out all the keys and put them somewhere?"
    b "That's a good idea."
    hide jenny ind with dissolve
    bi "Jenny grabbed all 16 locker keys."
    show jenny ind with dissolve:
        xcenter .75
    j "Bert! Look at this."
    bi "She held up a grey worksuit."
    b "Huh? What is that?"
    j "It looks like there's one in each locker."
    j "They must be the security guards' uniforms."
    b "They definitely don't look like something you'd want a customer to see."
    j "Yeah, way too tacky."
    b "No no, I mean like, they're not professional looking."
    b "Very utiliarian design."
    b "The fact that the bank has 16 of these must mean they used them a lot..."
    j "Or they just had a lot of guards on payroll."
    b "True..."
    j "Well, they don't seem very useful for us, so I'll put this one back."
    j "Anyway, do you want to hold onto these locker keys?"
    j "My skirt doesn't have any pockets."
    b "Me? I guess I could, but are you sure you can trust me?"
    j "More than anyone else here."
    j "Here you go!"
    bi "I'll keep these in my backpack..."
    bi "..."
    b "Alright, now hopefully no one asks what's in here."
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
    bi "We spent some time looking around the lobby, then regrouped."
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
    bi "After a while, everyone returned to the lobby."
    bi "We brought some food from the kitchen and recapped what we found."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=3)
    $ showchibint("freddy", "lauren", "jenny", "sam", "sid")
    with dissolve
    b "So the big rooms are this lobby, the kitchen, a director's office, and a locker room."
    b "The keys for the lockers are missing, but they're all open anyway."
    bi "Well, not exactly, but that's effectively the truth."
    b "There's also a safe we can supposedly open using three of our birthdates."
    b "But whoever inputs a code dies if they input the wrong code."
    b "Which means someone could lie about their birthday to murder someone else."
    show lauren ind with moveinleft
    l "Sid, did you have any luck finding a vault key or code somewhere?"
    show lauren ind:
        xcenter .5
        linear .3 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "I don't think it'll open unless we use our birthdates..."
    i "Are you all suuure you won't tell me them?"
    l "No shot."
    l "If I did I'd tell you the truth, but I'm not risking anyone else lying to you."
    l "Who's to say there's even anything in there?"
    i "Alright..."
    l "And besides, there are only six of us here."
    l "It seems pretty unlikely someone plots a whole murder without us noticing."
    b "There are so few of us."
    b "We can even all sleep in the same room now, since this place is pretty big."
    i "Huh? Do I have to? There's a cozy looking sofa out in the hallway."
    l "Where?"
    bi "Sid grabbed a pen and started drawing on the map."
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
    f "Unless you use reusable ones!"
    f "But you're too lazy to do that!"
    f "So you just use a coffee maker instead!"
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
    bi "No, we were alone in there earlier."
    bi "Sam could've killed me then."
    bi "I should go there."
    scene black with dissolve
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
    b "..."
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
    s 'Well, it wasn\'t exactly - There\'s someone in here with the name "Gerald Ogden."'
    b "Gerald? Not Freddy, Fred, Fredrick?"
    s "Well, it's not Freddy."
    s "Unless Freddy is an old midget acting as a child."
    s "Take a look for yourself."
    show geraldfile with dissolve
    pause 1
    b "Gerald Ogden... interesting."
    b "There's even a picture of him."
    b "Very... powerful eyebrows and mustache."
    b "Do you think this guy is related to Freddy?"
    s "It's a very unique name, it can't be a coincidence..."
    s "Besides, I didn't see anyone else's name in the files."
    s "If they're of any use to us, this is it."
    b "Hmm... Let's see what the file says about him."
    s "Let me know when you see it."
    b "It?"
    show geraldfile2 with dissolve
    hide geraldfile
    b "Wait... 10.3 million dollars..."
    b "Is this how much money he has in his account?"
    s "No, that's how much his balance increased last year."
    b "HE MADE $10.3 MILLION IN ONE YEAR?!"
    s "That's what the document says."
    b "Why is so much stuff crossed out?"
    s "If the artist filled in those details they'd be wasting their time."
    b "Huh?"
    s "I mean, uh..."
    s "It could be a file only used for specific things, like an audit or taxes."
    s "In cases like that, the bankers will block out everything they don't need."
    b "That makes sense..."
    b "But the change in balance isn't crossed out..."
    hide geraldfile2
    b "That's... a lot of... wow."
    b "Freddy comes from a family of multimillionaires?"
    s "Honestly, the dude is probably a billionaire."
    s "He probably has multiple accounts, and other places he keeps his money for tax purposes."
    s "Not to mention whatever business assets he has that aren't liquid income."
    s "This isn't really that much money in the grand scheme of things."
    b "Sorry, you said ten million isn't that much money?"
    s "{i}In the grand scheme of things{/i}."
    s "It's a lot more than I'll ever have, that's for sure, but..."
    s "Most big bank chains hold trillions of dollars."
    b "I can't believe Freddy's dad... well, the guy we think is his dad is that kind of person."
    b "He seems like any other goofy kid to me..."
    s "That's why I asked you to come."
    b "What do you mean?"
    s "I was worried about presenting this to everyone."
    s "I don't know how they would react."
    s "Honestly, I don't know how {i}I{/i} would have reacted to this if we found before... well, Stella died."
    b "It's not the same for you now?"
    s "Now I'm just... going through the motions."
    s "Doing what I can."
    s "But for someone like Sid..."
    s "That's more than life changing money."
    s "Sid would definitely turn against Freddy if he thought he could get some of it."
    s "Plus, I think showing Freddy would scare the hell out of him."
    s "He might not even know his dad is this rich, given what he's said."
    s "Sounds like he lives a pretty sheltered life."
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
    show jenny ind
    b "There's a file about someone who could be related to Freddy."
    b "A guy named Gerald Ogden."
    s "He's insanely rich, too."
    s "Easily one of the largest accounts in this whole bank."
    j "How big we talking?"
    b "Last year his main account gained over 10 million dollars."
    j "So Freddy might be... the richest frog ever..."
    j "Well, except for maybe that prince that turned into a frog..."
    b "To be clear, we're not sure if they're actually related."
    b "We're hoping to figure that out."
    b "Jenny, do you think you can help me talk to Freddy tomorrow?"
    b "I don't want to scare him, but it can't hurt to ask him what his dad's name is."
    j "Sounds like a plan."
    s "Great."
    s "Half of us know about this now, but I still think we should hide the file."
    j "May I take a look?"
    bi "I handed her the file. After just a quick glance..."
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
    j "They had several eye witnesses for tons of different crimes."
    j "And then guess what happened?"
    b "I'm... kinda scared to know."
    j "He was found not guilty, walked out with not even a slap on the wrist."
    j "Everyone at town hall went ballistic... it was the craziest thing I've ever seen."
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

    j "This can't be right! His name isn't Gerald Ogden..."
    j "At least, it wasn't back then... his name was Jereldino Ogarian."
    s "Slow down, what the hell are you talking about?"
    j "My crime... it's after protesting a court decision about... this guy."
    b "Are you sure that's him in the picture?"
    j "I'm positive."
    s "Maybe he got a name change?"
    b "\"Jereldino Ogarian\" and \"Gerald Ogden\"... they're pretty similar."
    b "It's not uncommon for people with difficult to pronounce names to adopt a more \"normal\" name."
    b "Especially immigrants trying to improve their chances or their kids' chances in society."
    b "My birth name isn't actually \"Bert\" believe it or not..."
    j "I don't think that was why he did it..."
    j "He was already pretty successful when that court case happened."
    s "Yeah, there's a much more obvious reason."
    s "He just changed his name to avoid the bad publicity."
    j "But... but he's still the same person!"
    s "Yeah, but the public has a short attention span."
    s "Anyway, if this really is him, that file's proof of his wealth."
    b "So, the man you were enraged over might be... Freddy's dad."
    j "Th-that doesn't make sense either!"
    j "He didn't have a family, it was even mentioned in his defense."
    s "He might have been keeping them a secret."
    b "Why?"
    s "Maybe for their own safety."
    s "Being the wife and son of a well-known criminal probably makes life hard."
    b "Freddy has told us he doesn't really see his dad much."
    b "Maybe, well... you know, his dad doesn't want the public to know about them for other reasons."
    s "Maybe Freddy's mom is a mistress of his?"
    b "Um... I don't think that's the kind of thing you just lightly suggest."
    s "Hey, it's not uncommon for rich guys."
    b "Yeah, but it's still rude to Freddy, right Je-"
    b "Jenny?"
    bi "Jenny had turned noticably paler."
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
    j "Not to mention, there were tons of rumors that his company was a front for black market business."
    j "They sold guns, drugs, some people even thought they were involved in human trafficking..."
    s "Did you say drugs?"
    j "Yeah, it's just a rumor, but-"
    s "You said he was using an alias, right?"
    s "What was his name again?"
    j "Jereldino Ogarian."
    s "Is that with a G or a J?"
    j "A G as in gesundheit."
    s "JO... that..."
    s "That's the alias of the kingpin I worked under."
    s "And apparently the true initials of Gerald Ogden."
    j "You knew him?"
    s "Not directly... never met him or seen his face."
    s "He was several rungs up the ladder from me."
    s "I pretty much only needed to talk to the guy who supplied me my goods and took the organization's cut."
    s "But it's like how people who worked in the Sinaloa Cartel never met El Chapo."
    b "The what?"
    s "It's an infamous crime syndicate responsible for most of the cocaine and heroin smuggled into the states."
    j "What the hell! How could you work for a guy like that?"
    s "Don't be stupid. I never met the guy. And it might not even be Ogden."
    s "You said it yourself, they were just rumors."
    j "Hmph. Yeah, you're right."
    s "..."
    j "..."
    s "Aren't you gonna say sorry?"
    j "Yeah sorry you got caught up in drug dealing!"
    show jenny happy
    j "Suckerrrr!"
    bi "Seems like she's back in a good mood."
    s "Sigh... I don't know what I expected."
    b "Anyway, we should focus on the more direct connection this Ogden guy might have..."
    b "We can hope it's not Freddy's dad, but I guess we'll find out soon enough."
    b "It could be important to our situation in this game."
    b "Things just keep getting more intertwined..."
    s "Anyway, we need to do something about this file."
    s "I doubt Sid, Lauren, or Freddy will go looking through the records, but..."
    b "We don't know for sure how they'd react if they did see it."
    s "Yeah."
    s "No offense... well, some offense, but..."
    s "I'm not trying to tame three people reacting like Jenny might have."
    show jenny ind
    j "Hmph."
    s "Especially Sid..."
    s "Is there somewhere we could hide this, just for the night?"
    j "Hmm..."
    show jenny happy
    j "Oh!"
    j "Bert, we could hide the record in one of the locker room lockers!"
    b "That's true, I still have all the keys in my backpack."
    b "I'll drop it off in there when we leave here."
    j "And we can chat with Freddy in the morning."
    j "It might be awkward, but he's just a little kid after all!"
    j "Kids are 76% awkward!"
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
    bi "..."
    bi "Nope, not this one."
    bi "Sigh, I hate menial tasks like this..."
    bi "..."
    bi "Okay, ninth try's the charm, I guess. You go in here, and... locked."
    bi "I'll put this key in a different pocket so I don't have to figure this out again."
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
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy", "lauren", "jenny", "sam")
    show jennysleep:
        xcenter .195
        ycenter .5
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
    b "..."
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
    bi "After \"Team Mystery Busters\" split up, I made my way back to the lobby."
    show bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("lauren", "sid", "sam")
    show sid ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "Hey, I need to tell you guys something. It's about Freddy."
    l "Oh?"
    i "Is it his birthday?"
    b "No, not that..."
    b "We found some info about his dad. Well, we think it's his dad, at least."
    b "It might just be a coincidence, but..."
    b "It's a guy with the name Gerald Ogden."
    l "Just like Freddy Ogden..."
    b "Exactly. He has an account here..."
    b "And the balance increased by 10.3 million dollars in just one year."
    b "..."
    b "... Well? Say something!"
    i "..."
    i "..........."
    show sid mad
    i "What the hell?! Ten million?!"
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
    i "10.3 million dollars... I'll even share a bit to whoever gives me the third birthday!"
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
    s "Like Bert said, we don't even know if Freddy's related to Gerald. It could just be chance."
    s "Or worse... a ploy by the Game Master to confuse us."
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
    l "Speaking of the vault, I guess that means Freddy really is rich."
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
    bi "After spending some time chatting, I went back to the lobby."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=3)
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
    b "That seems like child abuse..."
    show jenny ind
    j "I mean, it would work!"
    b "Hmmm, maybe not the best idea."
    b "But for now, keeping him within arm's reach is a good plan."
    b "I'll keep him joined at my hip for the rest of the day."
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
    s "I can come back to help you watch Freddy once I've explored a bit more."
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
    i "I'm gunna go look for more clues to the safe?"
    b "More clues?"
    i "Yeah! What if the Game Master scratched the combination onto a wall somewhere?"
    bi "Sid really shouldn't be telling anyone that he'd try random numbers on a wall..."
    b "Sid, you probably shouldn't-{p=0.5}{nw}"
    i "Seeya!"
    hide sid with moveoutright
    $ showchibi("freddy")
    bi "...And he's gone."
    show frog2 ind
    bi "I'm tired..."
    bi "It's been a while since we had anything of substance to eat."
    bi "If that tomato soup I made in the hospital even counts as food..."
    f "Bert I wanna play!"
    b "Aren't you tired?"
    f "Not tired not tired!"
    f "This is the first time I've been without my parents for this long."
    f "I wanna have fun! And play with all the things I'm not allowed to touch!"
    bi "It's weird hearing him talk about his home life knowing who his dad is..."
    b "Hmm... I think there are some supplies in the office."
    b "How does arts and crafts sound?"
    show frog2 smile
    f "Yay yay yay yay!"
    bi "Ok, phew, something that doesn't require me to really supervise him."
    bi "This will give me some much needed time to think..."
    scene black
    scene bg bankoffice
    $ statusnt("Director's Office", "bert", ch=4, sun=3)
    $ showchibint("freddy")
    show frog2 smile
    with dissolve
    b "Alright, there's some paper, and pens here."
    f "Are there markers or crayons?"
    b "Um.. this room belongs to an old adult."
    b "Adults are boring so they don't like to use markers or crayons."
    f "Oh, that makes sense. Adults are boring."
    f "Why do people grow up to become adults when they could become frogs?"
    bi "...He did mention he was taken out of the school system by his parents."
    f "Anyway, I want colors!"
    b "Okay, let's compromise."
    f "Compro-... what?"
    b "Uh. Make a deal."
    b "I can't give you markers or crayons but..."
    b "You can draw for as long as you want!"
    f "Yay!"
    bi "Kids are easy, you just have to trick them into thinking they want what you want."
    bi "The longer he draws the less I have to entertain him with something else."
    hide frog2 with moveoutleft
    bi "He's right to work, drawing something that looks like a... large chicken?"
    bi "I'm amazed how cheerful this kid can stay, given everything."
    bi "I don't think I'd be able to handle all this trauma at his age."
    bi "I... hope that doesn't mean he's used to it."
    bi "In any case, I should try to make myself useful."
    bi "Let's see..."
    bi "There's some paper here."
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
    bi "I don't think Stella had met either of them personally at the time, though."
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
    bi "...with six of us dead."
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
    f "Bert, I wanna take a nap..."
    f "Can we go back to the sleeping room now?"
    b "Yes, of course Freddy."
    b "Thanks for hanging out with me Freddy, this time has been really helpful."
    f "Huh?"
    f "My turkey was helpful, yay!"
    b "Um... yeah!"
    b "Let's head back to the lobby."
    scene black
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=3)
    $ showchibint("freddy")
    show frogsit2:
        xcenter .44
        ycenter .48
    with dissolve
    bi "He passed out almost instantly when we got back in here."
    bi "...I guess, Jenny's right, he is kinda cute."
    bi "Anyway, it feels great having {i}some{/i} direction, however small."
    bi "If Sam really can give us any new information about Mr. Sydell, we'd be in a good spot."
    bi "I need to talk to Sam now."
    bi "...But is it safe to leave Freddy alone?"
    bi "Not like I can stop anyone from killing him, but I'll at least be a witness."
    bi "I could wait, but..."
    bi "Every minute I spend not working on this mystery is a minute closer to someone else dying."
    bi "I have an idea..."
    bi "I approached the hallway door, and..."
    b "HEY!"
    b "..."
    b "Shoot, I was hoping someone would come..."
    b "Maybe one more try..."
    b "HEY!"
    bi "A few seconds later..."
    $ showchibint("freddy", "jenny")
    show jenny ind
    with dissolve
    j "Bert! Is Freddy dead?"
    b "What?"
    j "You were yelling! I assumed you found a body..."
    b "Oh. Yeah, I guess that's a natural conclusion..."
    b "No, I just wanted someone to take over Freddy duty."
    j "Is there something you need to do?"
    bi "Hm... I need to be careful."
    bi "It might not be a good idea to broadcast that I'm talking to Sam..."
    b "I uh, need to use the bathroom."
    j "Oh. Yeah, makes sense, nature calls and all that."
    b "Also, do you know where Sam is?"
    j "Huh?"
    j "Why do you need to know where Sam is to use the bathroom?"
    b "Um..."
    bi "Shoot, I blew it."
    bi "Quick, I need an excuse..."
    b "Sam has shy bladder syndrome!"
    j "Huh?"
    b "If anyone is even near the bathroom Sam has trouble... you know..."
    b "So I didn't want to inter-"
    j "Bert..."
    j "You could've just made something up."
    j "Just go, I'll look over Freddy."
    bi "How is it that the most awkward conversations of my life happen while I'm at risk of death..."
    b "Great, thanks Jenny!"
    scene black with dissolve
    bi "I ran off before she could respond."
    scene bg bankhall2
    $ statusnt("Bank Hallway", "bert", ch=4, sun=3)
    $ showchibint("sam", "sid")
    with dissolve
    bi "After searching for a bit, I found Sam."
    show sam with dissolve:
        xcenter .75
    s "Bert, you look like someone spilled red paint on your cheeks."
    b "I uh... let's not talk about it."
    s "Out of shape?"
    b "Something like that..."
    bi "Sid is sleeping on the couch... we should really talk in private."
    b "Hey, can I talk to you in the office? Just us two?"
    s "Sure."
    b "You're really going along with this that easily?"
    s "I asked you to do the same earlier."
    s "Besides, I'm not the one who's out of shape."
    s "I think I can handle myself just fine against you."
    bi "I should be offended but now's not really the time..."
    b "Okay, let's talk before anyone sees us..."
    scene bg bankoffice
    $ statusnt("Director's Office", "bert", ch=4, sun=3)
    $ showchibint("sam", "sid")
    show sam
    with dissolve
    s "So, did you find anything?"
    b "No, but... I realized something."
    b "Something you haven't told us much about..."
    b "Your relationship with Mr. Sydell."
    b "And more generally, any information about him that could help us."
    s "That's because there's nothing to tell."
    s "It was strictly a business relationship."
    b "But surely you knew something about the guy!"
    b "Aren't you supposed to build rapport with customers?"
    s "What do you think I am, a mom and pop shop?"
    s "It's drugs Bert, the product does all the selling."
    s "Not to mention, it's not exactly a good idea to tell a drug dealer about your personal life."
    s "You ever watch Oughta Holler at Paul?"
    b "Oughta Holler at Paul?"
    s "It's a show about everyday crime, and the main character, Paul, is a lawyer."
    b "...Why should you holler at a lawyer?"
    s "It's meant to rhyme. Holl, Paul."
    b "Wouldn't it be better as Oughta Call Paul?"
    b "So that Call and Paul actually rhyme?"
    b "Also who says \"Oughta\" these days?"
    b "I think instead I'd say Bet-"
    s "Whoa whoa, that's trademarked."
    s "Anyway, yeah, Oughta Holler at Paul."
    s "There's a guy smuggling pills to the local cartel."
    s "One day he gets too relaxed and they find his address..."
    s "Next thing he knows, he's getting robbed."
    s "You don't mix personal and professional."
    b "Yeah but... I don't get the sense you'd rob anyone."
    s "You barely know me. And Sydell arguably knew me even less."
    s "He'd be a fool to let me know who his family was, where he lived, anything like that."
    b "Wait, but I thought you'd been to his house?"
    s "I never said that."
    b "But you knew where we were!"
    s "Yes."
    s "Because of the big painting of the guy I'd met in the living room."
    b "...Oh."
    s "I must say..."
    s "I'm trying to be less snappy and more nice but..."
    s "Things like this make it hard."
    b "Sorry, I guess the questions are annoying."
    s "No, not that."
    s "I mean, yes, that's annoying."
    s "But... remembering my past."
    s "The sort of exterior I had to put on to get through my job."
    s "I used to be such an optimistic person until I went to my first protest."
    b "What happened there?"
    s "...I don't want to relive it."
    s "It's not relevant to any of this, anyway."
    bi "Sam doesn't want to relive it..."
    bi "A moment that was probably tragic and took part of Sam's soul away..."
    bi "That's all too familiar."
    b "What if we traded stories?"
    s "Hm?"
    b "I tell you about the day I committed my crime, and..."
    b "You tell me about this protest?"
    s "..."
    s "I don't like that you're making a business transaction out of it."
    b "No, no, it's not that."
    b "I could relate to what you said."
    b "You don't want to relive it."
    s "If you don't want to relive your moment, why are you offering to share it?"
    s "And why would you ask me to relive mine, knowing that feeling?"
    s "When you were talking to Dracula in the hospital you couldn't do it."
    s "Even when it would get you a favor from Dracula."
    s "You're calculating Bert. Just like me."
    s "If you wouldn't do it then when there was something to gain..."
    s "Why would you do it now?"
    b "I don't know, I guess..."
    b "I knew thinking about it and processing it would help me move on."
    b "But I didn't want to talk about it, because it made me feel like a bad person."
    b "Just... knowing how much negative impact I could have on someone else's life."
    b "Yet... I don't know, I think hearing that someone else went through something..."
    b "Well, even remotely similar to me."
    b "It feels hypocritical."
    b "To want others to push through their trauma but not want to push through mine."
    s "..."
    b "..."
    bi "I can't tell if Sam is emotional or just thinks I'm an idiot right now."
    s "..."
    s "...If you're playing me right here, I'll never forgive you."
    b "I swear I-"
    s "I'm convinced."
    s "You mean it."
    s "I'm not sure if I agree with it or even get it, but you're not manipulating me."
    s "But it's not worth our time right now to talk about things that aren't directly related to this."
    s "If... no, when we get out of here, we can go grab a drink and {i}talk about our feelings{/i}."
    bi "Sam said that in the manner of a bratty teenager who was playing on their phone."
    bi "But I think it was less derision and moreso a desire to get to business."
    s "There's a few things I... learned about Mr. Sydell."
    s "I don't know if they're relevant but I'll tell you them."
    s "Drug dealing is not like what you see in crime dramas."
    s "Not every user is a junkie in a dirty apartment."
    b "Oh, I never-"
    s "You don't need to lie and say that wasn't your stereotype."
    b "Hey, how do you know I don't use drugs?"
    b "Aren't you stereotyping me?"
    s "Do you use drugs?"
    b "...No..."
    s "Anyway."
    s "\"Drug user\" is too wide-reaching of a term, really."
    s "Sydell wasn't the only rich man in a suit we did business with."
    s "In some sense rich men in suits are the ideal customer for a drug dealer."
    s "Most businessmen break the rules one way or another in their jobs."
    s "To them, law is moreso a guideline than a rule."
    s "They have a reputation to uphold, so they have an interest in keeping things quiet."
    s "Plus, they obviously have money."
    s "And they'll pay more for high quality."
    s "And they're often buying for a whole party, not just themselves."
    s "Anyway, I wasn't lying when I said most of my customers treat it as a professional relationship."
    b "...Most, meaning..."
    s "Yeah. Not all."
    s "Sydell was one of those exceptions."
    s "We original kept a very professional relationship and he genuinely told me nothing."
    s "But he gradually started deteriorating one day."
    b "Deteriorating?"
    s "Yeah, it's kind of hard to explain."
    s "It's not like he suddenly changed."
    s "But one day he started trying to make small talk."
    s "I didn't recriprocate."
    s "I'm not exactly the most social type of person."
    bi "Sam? Not social?"
    bi "Not... the most surprising."
    s "I didn't think much of it."
    s "Thought maybe he just warmed up to me."
    s "Business types, they're good conversationalists."
    s "They're also a bit eccentric."
    s "So I didn't think anything of it."
    s "But eventually he started letting things slip that made it clear..."
    s "Something was going wrong in his life."
    b "The lawsuit with Stella's company?"
    s "Maybe."
    s "His company wasn't large enough for the lawsuit to make the mainstream media."
    s "So I don't know when that happened."
    s "I guess we can interrogate him after this."
    s "Anyway, yeah, from my point of view, not knowing about the lawsuit..."
    s "It just seemed like Sydell's family life was getting worse but I didn't know why."
    s "He mentioned a few different things on different days that I didn't put together until later."
    s "One, he asked me not to tell his wife about what we were doing."
    s "Which was weird, because I didn't know his wife at all."
    s "Two, his wife was in the hospital."
    s "And three, that his \"obnoxious brother-in-law\" wanted him to lose custody of his kid."
    b "Sydell had a kid..."
    b "I guess we could've guessed that from his mansion."
    b "It definitely had more rooms than one man, or even one couple, could need."
    b "...Sam, did he mention the gender of the kid?"
    s "No... why do you ask?"
    b "Well, could Sydell have been Gerald Ogden's actual name?"
    b "And maybe Freddy was the kid that he was going to lose custody of."
    b "It would make sense, if Freddy's mom went into the hospital."
    b "His dad sounded somewhat negligent, so someone had to step in."
    s "...Bert, that's a stupid theory."
    s "I met Sydell and I saw Gerald Ogden's face."
    s "They look totally different."
    b "Oh..."
    b "Right..."
    b "...I dunno, maybe he got cosmetic surgery?"
    b "Assume a new identity, get a fresh start at life, that sort of thing?"
    s "That's a bit of a stretch."
    b "Hm... yeah."
    b "..."
    b "Earlier you mentioned something."
    b "Sydell mysteriously disappeared as a customer, three years ago."
    s "Yeah, what of it?"
    b "...How close was this to when he started deteriorating?"
    b "Like, a few weeks, a few months?"
    s "I'd say it was a few months."
    b "So the point when he started deteriorating was also roughly three years ago."
    s "Yeah, I guess."
    b "...Did he say what type of hospital his wife was in?"
    s "...You think..."
    b "She might have been on the missing composite in the mental hospital, yeah."
    b "Maybe she and Shahar even crossed paths."
    s "You don't think Shahar would remember the name Sydell?"
    b "Also..."
    b "If the lawsuit is what caused him to deteriorate..."
    b "Doesn't that mean it happened roughly three years ago?"
    s "Yeah, that'd make sense."
    b "But in the hospital, when we were trying to figure out the missing composite..."
    b "Everyone said they hadn't committed a crime in the last three years except you."
    s "...You think Sid and Dracula were lying?"
    b "I mean, Dracula might have been."
    b "He had reason to disassociate himself with the location."
    s "But Sid?"
    s "That twerp, I swear..."
    bi "It was kind of refreshing to hear Sam call Sid a twerp."
    bi "It was almost like... an old friend had returned."
    bi "I guess the grass is always greener on the other side, or something like that."
    b "We can go ask him."
    b "I feel like I have a ton of unanswered questions now..."
    s "You didn't before?"
    b "Well, a ton of new ones."
    s "Such as?"
    b "When did the lawsuit happen?"
    b "Are Sydell's wife and kid related to this at all?"
    b "And Dracula's theory is Mr. Sydell is running the game."
    b "But if he disappeared from your life, and he was spiralling mentally when he did..."
    b "Is he even in shape to run this game?"
    b "Or... is that why he's crazy enough to run this game?"
    b "And if not him, who is running this game?"
    b "And what's their connection to him?"
    s "So... if you have all these new questions, this conversation wasn't helpful then?"
    b "No, it was good."
    b "It's like when you start out playing a video game, you go through the tutorial."
    b "You only have one thing to do, beat the tutorial."
    b "But then once you unlock the rest of the game there's all these lingering things to do."
    b "But just because you have more things you could be doing, it doesn't mean you didn't make progress."
    s "...Nerd."
    bi "...Yeah, I kind of deserved that one."
    b "Anyway, this was helpful."
    s "You're welcome, I guess."
    s "Sorry for not saying any of this earlier."
    b "No, I get it..."
    b "Don't want to put a target on your back."
    b "And until recently the connections to Mr. Sydell were... slim."
    s "Whatever, let's go make Sid open up about those emails he planted."
    scene black with dissolve
    scene bg bankvault
    $ statusnt("Bank Hallway", "bert", ch=4, sun=3)
    $ showchibint("sid", "sam")
    show sam:
        xcenter .75
    with dissolve
    bi "It didn't take long for us to find Sid..."
    bi "As one could have guessed, he was sitting outside the safe."
    show sid ind:
        xcenter .25
    i "Hm... maybe the scratches on the surface of the vault mean something..."
    s "What are you doing?"
    i "Sam? Bert?"
    i "What are you doing here?"
    s "That's what I just asked you."
    i "What does it look like?"
    i "I'm trying to open the safe!"
    s "...The one that we said would be a bad idea to mess with."
    i "You think I'm gunna listen to some loser adults?"
    s "You understand the part where you die if you get it wrong, right?"
    i "I'm not stupid, Sam."
    i "Just because I didn't go to school as much as I should have, doesn't mean I can't read."
    i "I'm smart enough to be the next William Fences!"
    i "The next Elon Odor!"
    i "The next Mark Zuckermountain!"
    bi "I didn't realize it until Sid mentioned the famous software CEOs, but..."
    bi "They all have very stupid names."
    s "You might have the technical smarts, but..."
    s "Your street smarts are a bit lacking."
    bi "The downside to Sam recovering from \"killing\" Stella was, well..."
    bi "Sam and Sid didn't get along."
    bi "This might cause us more problems if I don't-"
    i "...You don't understand."
    i "You never could unless you lived a day in my life."
    b "...Understand what?"
    i "If this game ended right now and you went back to your normal lives..."
    i "What would you do tomorrow?"
    b "I guess... call my loved ones and let them know I'm okay..."
    b "Then probably make sure I have a job still and if so catch up on work."
    s "I'm sure if I explained to the dean I could drop all my classes and retake them later."
    i "See, you have... hopeful lives to get back to."
    i "If I make it out of here, I'm still poor."
    i "My family still has a mountain of debt to climb out of."
    i "My parents might... might..."
    bi "He was visibly tearing up."
    b "Sid... that was inconsiderate of us to answer to quickly."
    i "No it's..."
    i "I'm sure for people like you it's a reasonable answer."
    i "And for people like you it's also probably reasonable to ignore this safe."
    i "But... for me?"
    i "That brief moment in the mansion where I just got to eat a bunch of food."
    i "Even though we were in a deadly game."
    i "Even though Stella died shortly after..."
    i "I got to pretend my problems outside of here didn't exist for a bit."
    i "But that made me realize something."
    i "My life isn't much better if I escape."
    i "So yeah, maybe it gets me killed."
    i "But... if there's even a slight chance."
    i "That I can not just get out of here, but make everything alright for my family..."
    i "I have to go for it."
    b "..."
    s "..."
    bi "Sometimes when people make a big mistake they don't want to admit it."
    bi "But it's clear from looking at them that they know."
    bi "Sam had that look."
    b "Sid..."
    b "Obviously my approval doesn't matter much to you."
    b "I can't relate to what you've gone through."
    b "But... I won't judge you for trying to get whatever's in there."
    b "And I don't think Sam will either."
    bi "That was more of an order to Sam than trying to be supportive of Sid."
    s "Hmph."
    bi "I did want to tell Sid that, at the same time, it wasn't just his life at stake here."
    bi "And as sorry as I felt for him..."
    bi "Him risking his life to open this safe indirectly endangered all of us."
    bi "If he died because someone tricked him into trying to open the safe."
    bi "And worse, if we couldn't figure out who..."
    bi "We'd all die as well."
    bi "Maybe I should have told him that but..."
    bi "So far he hadn't tried it."
    bi "And if we wanted to \"win\" this game, at this point, it wasn't just enough to survive."
    bi "It's like those multiplayer team games, where you're trying to defend your-"
    s "Bert, you're not making another metaphor to video games in your head right now, are you?"
    b "...No."
    bi "...Where was I?"
    bi "Oh right."
    bi "We had to push to find out who the Game Master was as soon as possible."
    bi "We played too much defense, we had to go on the offense."
    bi "So we needed info from Sid."
    bi "And he was more likely to talk if we played along with him."
    i "..."
    i "I don't trust adults..."
    show sid mad:
        xcenter .25
    i "You're lying to me Bert, aren't you!"
    i "You want all the money for yourself and you're trying to distract me!"
    s "Ah, back to pea-brain mode I see."
    i "Grrrrrr."
    bi "I... think that means Sid has moved on?"
    b "Sid we just want some more information about that lawsuit."
    b "I feel like we're at a point where any one little thing could reveal the Game Master..."
    s "Really?"
    s "I thought you-"
    bi "I flashed Sam a look."
    s "Oh, yeah, I guess we are pretty close."
    i "Oh."
    show sid ind:
        xcenter .25
    i "So you're saying like... if I knew anything important than I'd save everyone's lives."
    b "Uh..."
    b "I guess so, yeah?"
    i "And like, you'd all probably give me money for being the hero afterwards."
    b "..."
    s "We can discuss helping you out later after we get out of here."
    i "I'm not hearing a \"yes.\""
    b "But you're also not hearing a \"no.\""
    bi "I gave him a fat grin."
    i "That's not good enough."
    b "What if... I see if I can get you a part-time job at my company."
    b "If you're actually this good a hacker we could definitely find a place for you."
    i "Hm... okay, we'll negotiate later."
    i "So, about the lawsuit..."
    i "I mean, it's still kind of a sore spot for me..."
    i "But only in relation to family. So as long as you're not asking about them I'll talk."
    i "What do you want to know?"
    b "Well, there's just one big thing..."
    b "When did you plant the file the lawyers asked you to plant?"
    i "It was... when I was eleven, I think? So about five years ago."
    bi "Eleven? The kid's seriously a computer genius..."
    bi "I didn't mean it earlier, but maybe I should actually hire him after this game..."
    b "So you weren't lying in the hospital when we asked who had committed crimes in the last three years."
    i "Yeah, I wasn't."
    i "...Wait, did you think I was?"
    b "What?"
    b "Oh no no no that isn't."
    i "I knew it! You were trying to pin me as the mastermind and get me killed!"
    i "Then you could take the money without me!"
    s "Sid, I know you don't think I have any authority, but none of that is true and you know it."
    s "We're trying to figure it out."
    i "Grrrrr."
    s "Anyway Sydell lost contact with me three years ago..."
    s "That's also roughly when Shahar was lobotomized."
    s "So if the lawsuit happened four years ago..."
    s "Did Sydell's personality change was because of something different?"
    s "And I guess, him disappearing from my life was also because of something different?"
    show sid mad:
        xcenter .25
    i "Wait, what made you say the lawsuit happened five years ago?"
    s "...Because that's when you planted the email?"
    i "Well yeah, but the lawsuit took years to go to court."
    b "{i}Years?{/i}"
    i "Yeah. At least, I think it did."
    i "I only got an email from that lawyer saying I had done my part two years later."
    s "\"Done your part?\""
    i "Yeah, like, they won the lawsuit with my help."
    b "So it was three years ago..."
    i "Yeah, unless they emailed me really late."
    i "So, did I do it?"
    i "Did I solve the mystery?"
    s "Not quite..."
    s "The lawsuit being three years ago means it's probably at least part of why Sydell disappeared."
    s "But Dracula already told us that he thought the lawsuit was the reason for this game."
    s "So we already knew it was deeply important..."
    b "I wonder if he disappeared to start planning this game then..."
    b "Perhaps he found out Shahar, Dracula, Stella, and Sid were partially responsible."
    b "Then brought in people who tangentially hurt him, like Sam and Catherine, to round it out."
    s "But why would he need to disappear to do that?"
    b "Maybe... he wanted to distance himself from everyone before trapping them?"
    i "I mean, isn't there an easier explanation for why he disappeared?"
    i "What if he died?"
    b "Died?"
    s "...Huh, I guess that would make sense, yeah."
    s "I always wondered if he moved on to a new dealer or he just quit cold turkey."
    s "But if he died that explains why he, well, no longer needed my services."
    b "Who's running the game if he died, then?"
    i "I dunno, but if I figured something out then you owe me."
    i "My consulting fee is $100,000!"
    b "That's more than I have in my bank account..."
    s "There's no way you're getting $100,000 from me."
    i "Okay, okay, maybe I was highballing you a bit."
    i "We can call it a cool $50,000 instead."
    s "For $50,000 you have to at least name who the Game Master is."
    i "Uh... you?"
    s "Bzzt. Nope, I'll give you maybe $5 for your help."
    i "Meh, I was expecting nothing so I'll take it!"
    s "Anyway, enough distraction."
    b "Yeah, we don't know who's running the game..."
    b "But if it isn't Sydell, all the connections can't be a lawsuit, right?"
    b "It has to be someone closely related to him..."
    i "Maybe someone getting revenge for him after his death."
    s "Regardless, this is all just speculation..."
    s "He could very well be alive and just sitting in a room somewhere laughing at us..."
    b "Well if that's the case we're screwed regardless."
    b "Unless there's an alternate win condition we don't know of."
    s "Seems unlikely."
    b "Right. So I'd rather assume someone here is indeed Game Master and we have a shot."
    bi "I need to think... I feel like there's some argument for who it is that's missing..."
    bi "If I could just sit down somewhere without distractions..."
    $ statusnt("Bank Hallway", "bert", ch=4, sun=4)
    $ showchibint("sid", "sam", "freddy", "jenny")
    with dissolve
    hide sid with moveoutleft
    hide sam with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    show frog ind with moveinleft:
        xcenter .25
    j "Hey guys."
    j "It's getting late... Freddy should sleep soon."
    j "I was kind of hoping I could take a shower before bed, could one of you take care of him?"
    f "*Yawn* it's Freddy bedtime... Fredtime..."
    ses "Mew!"
    show sesame with moveinbottom
    j "Oh, seems like Sesame's volunteering!"
    f "Kitty..."
    j "Yeah, you can tell he's tired if he doesn't even want to play with Sesame."
    ses "Mew..."
    j "Don't worry Sesame, he'll play with you tomorrow!"
    j "Thanks guys!"
    hide jenny with moveoutright
    $ showchibint("sid", "sam", "freddy")
    with dissolve
    f "*Yawn* so... tired..."
    hide frog with moveoutbottom
    blank "*thunk*"
    b "He's... he's so tired he just fell asleep on the floor."
    show sid with moveinleft:
        xcenter .25
    show sam with moveinright:
        xcenter .75
    i "Um... I was gonna go sleep on the couch in the hallway tonight so..."
    i "Not it!"
    hide sid with moveoutright
    $ showchibint("sam", "freddy")
    with dissolve
    s "I knew we could trust him to handle this in a mature manner..."
    s "I'll help carry Freddy to the lobby, but I don't think I'll stay with you."
    b "Got plans?"
    s "Nothing secretive, don't worry. Just checking if there's anything palatable in the kitchen before bed."
    b "Well, not like I'd be able to stop you if were doing anything..."
    s "True. I could probably stop you though."
    b "Huh?"
    s "C'mon, let's get Freddy onto a couch."
    bi "Rude."
    scene black with dissolve
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy", "sam")
    with dissolve
    show sam with dissolve
    s "Okay, Freddy is in bed, you're okay watching over him?"
    b "Yeah, I'm fine. Maybe it'll be good to have some thinking time after today..."
    s "Got it. Good luck."
    hide sam with dissolve
    $ showchibint("freddy")
    with dissolve
    bi "I sat down, hoping I would have some time to think the game through."
    ses "Mew?"
    show sesame with dissolve
    b "Aww, Sesame. How'd you know I needed a cat to sit in my lap right now?"
    ses "Mew!"
    ses "Prrrr."
    bi "He fell asleep..."
    bi "Either the adrenaline rush from today was wearing down or Sesame's warmth got to me."
    b "*Yawn*"
    bi "Maybe it would be good for me to take a break."
    bi "It'd been a few days since we had real food..."
    bi "And it's not like anything will happen tonight, right?"
    bi "Yeah, I could figure this out tomorrow..."
    bi "For now, time to go to b-{p=0.5}{nw}"
    scene black
    bi "Without even realizing it, I fell asleep."
    bi "..."
    bi "..."
    bi "What a long day of tutoring..."
    z "Playing the best of rock, pop, rap, and more, this is FM 101.7 with your host Mike."
    bi "It'll all be worth it for spring break..."
    bi "..."
    bi "Huh?"
    blank "Shrrrrrrr."
    blank "BANG" #TODO: Add sfx
    bi "That..."
    bi "That lady just walked out from nowhere into the middle of the..."
    bi "Wait..."
    bi "No, I was dreaming..."
    bi "Yeah, I'm still lying in the couch right now, with my eyes closed."
    bi "It's been a while since I dreamt about that day..."
    bi "I guess talking about Sam may have brought the repressed memories back."
    bi "Anyway, I should get back to-{p=0.5}{nw}"
    blank "Creaaaaaaaaak." #TODO: Add sfx
    bi "...Okay, I'm pretty sure I'm not dreaming anymore."
    bi "What was that?"
    bi "I forced my eyes to open and get myself out of my half-asleep state..."
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy")
    show bg banklobby1 #music change
    with dissolve
    bi "That noise... was the door opening."
    bi "And in the door was..."
    show lauren pixel:
        xcenter .85
        ycenter .52
        zoom 1.3
    $ showchibint("freddy", "myster")
    with dissolve
    bi "Someone wearing a guard uniform?"
    bi "And holding what seemed to be a gun."
    bi "Wait."
    bi "Fuck."
    bi "Without thinking, I ran towards Freddy."
    bi "As soon as I did, the inevitable happened"
    blank "BANG BANG BANG BANG BANG BANG." #TODO: Add sfx
    scene black
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    $ showchibint("freddy", "myster")
    bi "I stopped running towards Freddy and fell to the floor, closing my eyes."
    f "Ow... my ears..."
    f "Bert... what's happening..."
    bi "The gunshots made it hard to hear, but I thought I heard Freddy crying."
    bi "...Is that it?"
    blank "Clap clap cl..."
    bi "I could barely make it out, but..."
    bi "Footsteps. They're going away."
    bi "Freddy is safe, but the others..."
    bi "Before I could even process it..."
    f "Bert? Where are you going?"
    bi "I was running out the door."
    scene bg bankhall1b
    $ statusnt("Bank Lobby", "bert", ch=4, sun=4)
    with dissolve
    bi "As I went into the hallway, I saw the door to the kitchen closing."
    show bg bankhall1 with dissolve
    blank "Click."
    bi "It was quiet enough that I heard the door slowly click into place."
    bi "Someone just went in there... probably the uniformed person."
    bi "...Is Sam still in there?"
    bi "Oh no."
    bi "At this point, it was like I wasn't even in control of my body."
    bi "I was a spectator, my body acting on its own instincts."
    bi "I watched my hand grabbed the door handle and yanked it open."
    bi "I watched my legs ran in."
    scene black with dissolve
    bi "As I ran in, I was getting ready to identify the uniformed person."
    bi "I knew if they were pointing the gun at someone else in the kitchen..."
    bi "I had to act."
    bi "I'm not sure what I would have done if that were the case."
    bi "Run at them and try to win with the element of surprise?"
    bi "Jump in the way of any bullets they might fire at someone else?"
    bi "Chasing someone with a gun isn't exactly a situation you prepare for."
    bi "I could only hope I would have picked the right action instantly."
    bi "But..."
    bi "Ultimately, I didn't have to make that decision."
    bi "As I walked into the room I {i}did{/i} see the uniformed person."
    bi "But they weren't pointing the gun at anyone."
    bi "Instead..."
    scene bankbreak2
    $ statusnt("Staff Kitchen", "bert", ch=4, sun=4)
    with dissolve
    bi "They lay there on the ground, in a pool of blood."
    bi "The gun a few mere inches from their hand."
    bi "The very brief moment of relief, knowing I wouldn't have to fight..."
    bi "It was quickly overwhelmed by raw emotion."
    bi "..."
    b "No..."
    b "Not again..."
    bi "I'm tired of feeling so powerless."
    bi "I thought I had escaped that feeling."
    bi "We were coming so close..."
    bi "..."
    bi "It's crazy how strong humans are."
    bi "My mind wanted nothing more than to curl up on the floor and cry."
    bi "But my body was moving almost on its own."
    bi "Fighting to do what it thought it needed to do to survive."
    bi "I found myself walking towards the door."
    bi "My body decided the right thing to do was to gather the others and start looking for clues."
    bi "I walked towards the door, and..."
    b "HEY!"
    b "Come to the break room, there's a dead body!"
    bi "Hoping someone in the hallway could hear me, I yelled."
    bi "Partially so they knew what was happening..."
    bi "Partially so I could lean on them to get through this."
    $ showchibint("jenny")
    with dissolve
    show jenny ind with moveinright:
        xcenter .75
    j "Bert?"
    bi "She poked her head into the room."
    show jenny ind:
        xcenter .75
        linear 0.15 xcenter .5
    j "Was th-{p=0.5}{nw}"
    j "Oh my god!"
    b "Yeah... another dead body."
    j "Who is it?"
    b "Huh?"
    j "The corpse... who died?"
    b "Oh. I... didn't check."
    b "I was... kind of in shock."
    bi "I told Jenny about the events leading to me finding the body."
    j "You... ran after the person with a gun?"
    b "I was trying to stop them from hurting anyone..."
    j "You know they could have hurt you, right?"
    b "I mean, I didn't say I was rational..."
    j "Anyway, we should find out who it is."
    bi "I wasn't really ready to look a dead body in the face."
    bi "Not that I hadn't done it three times already, but..."
    bi "You never get used to it."
    j "Here goes..."
    show bg bankbreak3 with dissolve
    j "It's Sam..."
    b "Jeez..."
    bi "Anyone's face under that mask would have been terrible to see, but..."
    bi "Somehow seeing Sam's face hit me with a second feeling of defeat."
    bi "Sam was starting to really open up, contribute..."
    $ showchibint("jenny", "lauren")
    show jenny ind:
        xcenter .5
        linear 0.15 xcenter .25
    show lauren ind:
        xcenter .75
    with moveinright
    l "I heard you guys talking in here."
    l "...Oh jeez!"
    l "That..."
    l "Is that... Sam?"
    b "Yeah... Sam's dead."
    l "Oh no... it happened again."
    l "Freddy hasn't seen this, right?"
    b "No, he was with me in the lounge before I ran here."
    bi "I briefed Lauren on what happened."
    l "Bert... that was noble, but dumb of you."
    b "Yeah, I know..."
    j "If there's a silver lining... at least this murder is easy to figure out."
    b "It is?"
    j "You saw Sam with the gun in the lobby..."
    j "Next, we find Sam in here with a bullet precisely in the temple..."
    l "Yeah, it's a suicide."
    b "Are we sure no one overpowered Sam and stole the gun?"
    l "Bert, you might be the type to try to fight someone with a gun."
    l "But let's be real, if the gun was loaded and someone fought Sam..."
    bi "Yeah... Sam would just shoot them."
    bi "I tried to think of another way things could have played out..."
    bi "I wanted to believe Sam was stronger than that, but..."
    bi "It made too much sense."
    bi "At the same time, I couldn't accept it."
    b "But... why?"
    b "Why would Sam try to kill me and Freddy and then..."
    l "Sam was pretty torn up about trying to kill Stella."
    b "But... Sam was recovering from a funk..."
    l "I don't know, maybe trying to kill you and Freddy broke Sam again."
    j "It could also be a nobility thing."
    j "This way, only Sam has to die, and it kind of spares the rest of us?"
    b "..."
    bi "I was out of words."
    j "So... should we get Sid and Freddy and make sure we all agree?"
    l "I don't exactly want to bring Freddy here, maybe we can meet in the lounge?"
    j "Works for me, okay with you Bert?"
    bi "Is it really that easy?"
    bi "Are they just too tired of this game to push for the truth?"
    bi "Part of me wants to be like that."
    bi "It wants nothing more than to just lay down and accept my fate."
    bi "But another part..."
    bi "Even if we're 99% confident it was a suicide, for that part it isn't enough."
    b "No, I think we should investigate."
    b "Remember when we were sure Sam killed Stella?"
    b "If we accepted the most obvious possibility as the truth, we'd be dead."
    l "...Yeah, you're right."
    l "If only to honor Sam's life, we should be sure."
    j "Well, guess it's time to investigate!"
    j "Murder solving squad let's go!"
label hospPreInv2:
    play music "audio/inthefaceofdeath.mp3"
    pause .5
    show investstart with dissolve
    pause 1
    hide investstart with dissolve
    l "Oh, but I'm going to go the lobby and make sure Freddy's okay..."
    l "Hearing gunshots must have been super traumatic for him."
    b "Yeah, go ahead."
    b "We'll get started here."
    l "Good luck, guys. Let me know if you find anything."
    hide lauren with moveoutright
    show jenny ind:
        xcenter .25
        linear 0.15 xcenter .5
    b "Jenny, can you do me a favor?"
    j "Huh?"
    b "Can you go with Lauren? We should make sure no one is alone for too long..."
    j "Oh. Sure! I'm not the best at this anyway..."
    hide jenny with moveoutright
    bi "..."
    bi "...There's five of us left."
    bi "I know I'm innocent, and I doubt Freddy is the Game Master."
    bi "So Jenny, Lauren, Sid."
    bi "I probably can't trust any of them."
    bi "I need to ask them what they were up to prior to discovering the body."
    bi "But first, I should search this room thoroughly..."
    call screen breakInv
