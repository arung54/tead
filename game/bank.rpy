label bankGo:
    $noside = True
    camera at paralloff
    scene black
    show bg flashback with dissolve
    #$ statusnt("???", "", ch=4, sun=0)
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
    camera at parallax
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
    $ showchibint("freddy", "jenny", "lauren", "sam")
    show lauren ind with dissolve
    l "...the kitchen."
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
    j "Kids are 76 percent awkward!"
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
    j "Alright, if we're settled here, I'm gonna hit the locker room!"
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
    bi "We don't have any clear connections between myself, Lauren, Dan, or Kaiser."
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
    s "Freddy saw Sydell's face in the mansion and didn't react."
    s "You think he wouldn't recognize his dad?"
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
    bi "He'd spent most of his time in here in one of two places."
    bi "Napping on the couch, or..."
    show sid ind with dissolve:
        xcenter .25
    bi "In front of the safe."
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
    show scary with dissolve:
        alpha .5
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
    hide scary with dissolve
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
    i "So you're saying like... if I knew anything important... I could save everyone's lives?"
    b "Uh..."
    b "I guess so, yeah?"
    i "And like, you'd all probably give me money for being the hero afterwards."
    b "..."
    s "We can discuss helping you out later after we get out of here."
    i "I'm not hearing a \"yes.\""
    b "But you're also not hearing a \"no.\""
    bi "I gave him a fat grin."
    i "So, about the lawsuit..."
    i "I mean, it's still kind of a sore spot for me..."
    i "But only in relation to family. So as long as you're not asking about them I'll talk."
    i "What do you want to know?"
    b "Well, there's just one big thing..."
    b "When did you plant the file the lawyers asked you to plant?"
    i "It was... when I was eleven, I think? So about five years ago."
    bi "Eleven? The kid's seriously a computer genius..."
    b "So you weren't lying in the hospital when we asked who had committed crimes in the last three years."
    i "Yeah, I wasn't."
    i "...Wait, did you think I was?"
    b "What?"
    i "I knew it! You were trying to pin me as the mastermind and get me killed!"
    i "Then you could take the money without me!"
    s "Sid, I know you don't think I have any authority, but none of that is true and you know it."
    s "We're trying to figure it out."
    i "Grrrrr!"
    s "Anyway, Sydell lost contact with me three years ago..."
    s "That's also roughly when Shahar was lobotomized."
    s "So if the lawsuit happened five years ago..."
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
    #i "I mean, isn't there an easier explanation for why he disappeared?"
    #i "..."
    #i "What if he died?"
    #b "Died?"
    #s "...Huh, I guess that would make sense, yeah."
    #s "I always wondered if he moved on to a new dealer or he just quit cold turkey."
    #s "But if he died that explains why he, well, no longer needed my services."
    #b "Who's running the game if he died, then?"
    #i "I dunno, but if I figured something out then you owe me."
    #i "My consulting fee is $100,000!"
    #b "That's more than I have in my bank account..."
    #s "There's no way you're getting $100,000 from me."
    #i "Okay, okay, maybe I was highballing you a bit."
    #i "We can call it a cool $50,000 instead."
    #s "For $50,000 you have to at least name who the Game Master is."
    #i "Uh... you?"
    #s "Bzzt. Nope, I'll give you maybe $5 for your help."
    #i "Meh, I was expecting nothing so I'll take it!"
    #s "Anyway, enough distraction."
    b "Yeah, we don't know who's running the game..."
    b "But if it isn't Sydell, all the connections can't be a lawsuit, right?"
    b "It has to be someone closely related to him..."
    s "Maybe someone getting revenge for him?"
    s "This is all just speculation, though..."
    #s "He could very well be alive and just sitting in a room somewhere laughing at us..."
    #b "Well if that's the case we're screwed regardless."
    #b "Unless there's an alternate win condition we don't know of."
    #s "Seems unlikely."
    b "I think we need to assume someone here is indeed the Game Master."
    bi "I need to think... I feel like there's some argument for who it is that's missing..."
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
label bank8:
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
    bi "As soon as I did, the inevitable happened."
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

    play music "audio/sadsong.mp3" fadein 2.0
    camera at paralloff
    $ showchibint()
    hide screen status_screen
    scene bg samdieslide with dissolve #kill splash
    show screen killuser
    pause 10
    hide screen killuser
    camera at parallax
    scene bg bankbreak2
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
    bi "Even if we're 99 percent confident it was a suicide, for that part it isn't enough."
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
    bi "At some point, I should ask them what they were up to prior to discovering the body."
    bi "I should start by committing to memory what I can about the series of events that just happened..."
    $ bank_evidence[0] = True
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    blank "Bert's Account was added to evidence."
    bi "Next, I should search this room thoroughly..."
    call screen breakInv
label trial4a:
    scene black
    bi "I returned to the lobby where everyone was already gathered."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    bi "They all stayed here for the entire investigation, so I caught them up to speed on everything I found."
    bi "Which wasn't much, unfortunately."
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    j "Not going to lie..."
    j "It seems like Sam committed suicide here."
    l "You're that confident already?"
    l "We haven't even discussed anything yet."
    l "Usually we need to do a whole song and dance just to come to a consensus."
    j "Well, it's different this time."
    j "When Dan, Stella, and Shahar died..."
    j "All three of them were killed remotely."
    j "So we didn't see the killer in action at all."
    j "But this time, Bert saw Sam in the guard uniform."
    j "The same one Sam's wearing now."
    b "Well, I saw {i}someone{/i} in the guard uniform in here."
    b "It wasn't necessarily Sam, right?"
    j "No, I think the person who shot you and Freddy was Sam."
    j "Don't you see it in the evidence you found?"
    bi "The evidence? Let's see, what makes it seem like they're the same person..."
    call screen bankEvidenceTrial(-1, 11, "trial4b") with dissolve
label trial4b:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "Are you talking about the uniforms?"
    j "Yeah, you said that there was only one uniform missing from the lockers."
    j "But if Sam and the person who shot at you in the lobby are different people..."
    j "Two uniforms would have been taken out, one for each of them."
    l "Couldn't the person who shot at Bert just have put the uniform on Sam after running?"
    j "Well, Bert chased the shooter after they ran away."
    j "It would have taken a long time to change Sam's clothes, enough time that Bert would have caught them."
    l "Hm... yeah, I can't argue with that."
    bi "..."
    bi "It's true that a lot of signs point to Sam committing suicide."
    bi "But it's like the black swan."
    bi "It's easy if you believe all swans are white to point at white swans and claim you're correct."
    bi "Similarly, it's easy to look at the circumstances and come to Jenny's conclusion."
    bi "But a single black swan is all that it takes to disprove that theory."
    bi "As hard as it may be to find..."
    bi "That's the only way to be certain of the truth."
    b "I think the uniform part isn't so important."
    b "There's lots of ways that could be explained..."
    b "Maybe there's another one hidden somewhere we didn't know about, who knows."
    b "But there's somethign else I want to focus on..."
    b "If Sam committed suicide, how did it happen?"
    j "How?"
    j "You mean... like, with the gun to the head?"
    b "Well, that, but when and where?"
    j "Colonel Mustard in the Ballroom with the Revolver!"
    b "...What?"
    j "I said in the break room, between the shooting in the lounge and when we found the body."
    b "Oh. Yeah, almost."
    b "We can actually narrow it down a bit more."
label trial4c:
    menu:
        b "If Sam committed suicide, the narrowest time range we can be sure it happened is..."
        "After the shooter left the lobby.":
            bi "This is true, but we can be more specific..."
            bi "If Sam committed suicide right after leaving, the corpse would be in the hallway."
            jump trial4c
        "After entering the break room.":
            bi "I think we can be more specific, Sam wasn't right next to the door."
            bi "It would have taken some time to move to the position the body was in."
            jump trial4c
        "After the door closed.":
            bi "Yes, that's it!"
        "Right before I opened the break room door.":
            bi "That's a bit too specific, it could have been earlier."
            jump trial4c
    b "If Sam committed suicide, Sam would have had to close the door first."
    j "Couldn't the door have closed on its own?"
    j "Some doors are like that, to save energy from heating and stuff."
    b "No, the door couldn't have closed on its own because..."
    call screen bankEvidenceTrial(-1, 1, "trial4c2") with dissolve
label trial4c2:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "When I was investigating in the break room, the door stayed open the entire time."
    b "So we know it's not a self-closing door."
    b "So Sam had to be the one to close the door, which Sam obviously couldn't do if they were dead at the time."
    b "Which means the suicide would have had to happen after the door closed."
    j "Bert, that's not very insightful..."
    b "No, but think about it."
    b "I don't think it's possible the gun was fired after the door closed, because..."
    call screen bankEvidenceTrial(-1, 0, "trial4d") with dissolve
label trial4d:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "I saw the door to the break room close."
    b "Which means after the door closed, I was in the hallway, very close to the break room."
    b "So I would have heard gunshots. But I didn't."
    j "But weren't you in the lobby for all the previous gunshots?"
    j "Your ears must have been ringing, maybe you just couldn't hear anything?"
    b "No, my ears were ringing but I was still able to hear the door close."
    b "That would have been way quieter than the gunshot."
    j "Hm..."
    j "Is it possible the break room is soundproofed?"
    b "Soundproofed?"
    j "Yeah, like... what if you just didn't hear the gunshot because the wall blocked the sound?"
    b "Is it even possible to soundproof a wall that well?"
    l "I doubt it... when you go to a firing range, they make you wear those noise-blocking headphones."
    l "Those only give you 25 decibels of reduction."
    l "A gunshot would still be about as loud as a car engine."
    j "Hm... okay, so the room probably wasn't soundproofed."
    j "I'm stumped then... how could Sam have committed suicide without Bert hearing?"
    b "Well, if someone-{p=0.5}{nw}"
    l "There could be another explanation for why Bert didn't hear the gunshot."
    b "Huh?"
    l "What if someone else shot Sam?"
    j "Someone else?"
    l "Yeah, I think someone could have shot Sam without the rest of us hearing."
    l "Specifically, in the window of time Bert was talking about earlier."
    bi "Oh."
    bi "The person she's talking about is..."
    call screen chooseCharBank("bert", trial4e, "Who could have shot Sam after the break room door closed?") with dissolve
label trial4e:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "You... think I did it?"
    l "Sorry Bert, I trust you a lot more than I trusted Kaiser and Dracula. And to a lesser extent, Catherine."
    l "You've been trying so hard to save the rest of us."
    l "But... hear me out, it just... makes a lot of sense."
    python:
        startBankTrial("lauren", "Lauren: I think Bert shot Sam in the break room.", 0,
        "lauren", "Lauren: Since {color=#f00}no one else had seen Sam recently{/color}, Bert was able to make up a story about the events leading up to \"finding\" Sam's body.", -1,
        "sid", "Sid: Wait, but then {color=#f00}we should have heard Bert shoot Sam!{/color}", -1,
        "lauren",  "Lauren: Not necessarily, because {color=#f00}we were all far away from the break room{/color}, so it would have sounded much more quiet to us.", -1,
        1, 5, "trial4f")
label trial4f:
    bi "I wanted to be mad, to think Lauren was insane."
    bi "To go through all the emotions that Sid went through in the train."
    bi "But..."
    bi "I have to admit, it is pretty suspicious."
    bi "I would have heard it if Sam shot themself, yet I claim I didn't..."
    bi "It makes it seems like I'm the murderer and I wasn't consistent about my story."
    bi "I can't get worked up about this..."
    bi "If I want to live, I need to approach this with a level head."
    bi "As hard as that may be under the circumstances..."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show lauren ind
    with dissolve
    b "You say no one had seen Sam recently..."
    b "But Freddy was there with me when my alibi happened."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show frog sad:
        xcenter .25
    with moveinleft
    f "Did... did someone say my name?"
    f "*sniff*"
    bi "Poor kid... he's probably still in shock."
    l "Bert... he's just a kid, don't use him as a tool."
    b "I'm... I'm not using him."
    b "Freddy saw what unfolded in here."
    f "What... unfolded?"
    b "Freddy... you remember the loud noises? And when I fell to the floor in here?"
    f "I... I don't wanna remember..."
    f "Can't it be nap time now?"
    b "Freddy, just for a few seconds, can you help us?"
    b "When the loud noises happened who was in here with you?"
    f "Uh... you were there."
    b "Anyone else?"
    f "Yeah... someone dressed up for Halloween... but they were actually scary!"
    f "I... I..."
    b "That's enough Freddy, thanks. You can take a nap now if you want."
    f "O-okay, I'll try..."
    hide frog with moveoutleft
    show sid ind:
        xcenter .25
    with moveinleft
    i "So it seems like Bert was telling the truth after all."
    i "You and me, Bert, we're one and the same."
    bi "I wouldn't say that..."
    i "Misunderstood, needlessly accused."
    show sid mad:
        xcenter .25
    i "You're a bully, Lauren, just like every other adult!"
    bi "I have to say, Sid coming to my defense isn't exactly helping."
    l "Freddy seeing Bert leave doesn't mean that Bert didn't shoot Sam."
    show sid ind:
        xcenter .25
    i "Huh?"
    l "Sure, Freddy can confirm that Sam came to the lounge, took six shots, and ran."
    l "And you're probably not lying about running out to chase Sam."
    l "But what if this is what actually happened..."
    l "Bert chased after Sam, in an act of heroism."
    l "Sam went into the break room, followed by Bert."
    l "Somehow Bert overpowered them, grabbing the gun and shooting Sam."
    l "Freddy was still in the lounge, so he didn't witness any of this."
    i "Wait... if Bert is the murderer, why was Sam trying to shoot people?"
    i "I thought every location could only have one murderer?"
    l "We don't know what happens if someone who's not the designated murderer kills someone."
    l "Also, it wouldn't be the first time Sam thought they were the killer..."
    b "Surely we all learned from that mistake."
    b "It seems unlikely both Sam and I would be trying to kill someone for any reason."
    l "Well, maybe you didn't intend to kill Sam until the events transpired."
    l "And you did it out of self defense."
    l "And now, since we don't know how the rules play out, you're trying to cover it up."
    bi "This is all just conjecture, but..."
    bi "If I say that it just seems like I'm trying to deflect."
    bi "I can't for sure say how the rules of the game play out in this case..."
    bi "Nor what I would do in the situation Lauren's describing."
    bi "I have to find an angle involving things we know about."
    b "..."
    i "...Nothing to say, Bert?"
    i "That's awfully suspicious..."
    i "Thinking up a fake story?"
    l "I have to agree with Sid, silence speaks volume here..."
    b "...Instead of speculating about what my motive would be after those events happened..."
    b "I want to hear how you think events played out in the break room again."
    l "Um... why?"
    bi "Admittedly it sounds like I'm about to incriminate myself, but..."
    b "Because I didn't do it."
    b "And the evidence should be able to prove it."
    l "Alright, whatever you say Bert..."
    python:
        startBankTrial("lauren", "Lauren: Sam {color=#f00}ran out of bullets{/color} and ran away to the break room.", -1,
        "lauren", "Lauren: You chased after Sam, who had {color=#f00}run into the break room{/color}. There was some sort of confrontation where you got control of the gun.", -1,
        "lauren", "Lauren: Then {color=#f00}you managed to shoot Sam once in the head{/color} and killed them. Afterwards, you dropped the gun.", -1,
        "lauren",  "Lauren: That way, the room {color=#f00}looked like a suicide{/color} when the rest of us arrived.", -1,
        2, 2, "trial4g")
label trial4g:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show lauren ind
    with dissolve
    l "I'm confused..."
    l "You're objecting to Sam being shot in the head once?"
    b "Sort of."
label trial4h:
    menu:
        b "More precisely, the problem is that..."

        "Sam could have shot me during the supposed confrontation.":
            bi "No, as Lauren mentioned, Sam ran out of bullets."
            bi "At some point Sam needed to reload."
            bi "If I confronted Sam during that point, it would have been a fistfight."
            jump trial4h
        "Sam wasn't shot just once.":
            bi "If that's the case, why did we only find one shell in the break room?"
            jump trial4h
        "In Lauren's story, I couldn't have shot Sam exactly once.":
            bi "I could have, I think a single bullet to the brain is pretty lethal."
            bi "So I could have killed Sam with one shot."
            bi "And if I overpowered Sam and could reload the gun, that one shot was definitely possible."
            jump trial4h
        "The evidence isn't consistent with Sam getting shot exactly once.":
            bi "Yes, that's it!"
    b "It seems like Sam died to a single bullet, but..."
    b "The evidence doesn't line up with a single bullet."
    l "What do you mean?"
    b "Think about how we found evidence in the break room."
    l "Yeah, there was a single shell on the ground."
    l "It's pretty glaringly clear Sam was just shot once."
    b "Well, yes, the shell would suggest that."
    b "But the gun seems to contradict that."
    l "The gun?"
    b "Yeah, think about it."
    b "The gun was empty when we found it."
    l "And?"
label trial4i:
    menu:
        b "If your story is accurate, the number of bullets in the gun should have been..."

        "0":
            bi "No, that's how many there were. That would just incriminate me more..."
            jump trial4i
        "1":
            bi "Okay, I think even Freddy is good enough at math to not come up with that answer."
            jump trial4i
        "2":
            bi "Okay, I think even Freddy is good enough at math to not come up with that answer."
            jump trial4i
        "3":
            bi "Okay, I think even Freddy is good enough at math to not come up with that answer."
            jump trial4i
        "4":
            bi "Okay, I think even Freddy is good enough at math to not come up with that answer."
            jump trial4i
        "5":
            bi "Yes, that's it!"
        "6":
            bi "...If I shot the gun, how would it still be full?"
            jump trial4i
    b "Five."
    b "Because the gun was empty when Sam ran."
    b "When it was reloaded, it would have had six again."
    b "And then if I shot it once, it would have five bullets."
    b "But instead..."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "There were zero!"
    b "...Yes, I was about to say that."
    hide lauren with moveoutright
    show sid ind:
        xcenter .75
    with moveinright
    i "Um, I confused... why would you have reloaded six bullets?"
    i "Wouldn't it have been faster to just load one?"
    i "It sounds like you and Sam fought... surely you didn't have time for six!"
    bi "I guess I was the only person who saw this..."
    bi "The reason I would load six bullets at once is..."
    call screen bankEvidenceTrial(-1, 10, "trial4j") with dissolve
label trial4j:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    b "I guess, it's not obvious if you haven't been in the safe yet."
    i "I haven't, I swear!"
    bi "That's... a suspicious way to respond to that."
    bi "But that's not important now."
    b "The ammo for the gun..."
    b "The only place I found any was in the safe."
    b "The ammo has a special design, where every set of six bullets is attached by a piece of metal."
    hide jenny with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    l "Oh, it's like a built-in speed reloader."
    b "Speed reloader?"
    l "It's a device you use to reload guns quickly."
    l "Basically, you can attach all the bullets to a speed reloader beforehand."
    l "Then, they're already aligned with the chamber, so you load them all it at once."
    l "Then you press a button on the speed reloader to release the bullets."
    l "But I guess here, the metal is keeping the bullets in formation instead."
    b "You've used one before?"
    l "Nah, I've seen them in video games though."
    b "Anyway, yeah, I guess it's like that."
    b "So if that's the only ammo that's available, I would have had to load six bullets at once."
    i "Couldn't you just have torn one off?"
    b "No, the metal connecting the bullets is actually surprisingly sturdy."
    i "Hm... maybe for a weak guy like you."
    bi "...Sigh, I hate that I have to do this, but..."
    b "Do you want to go and try to tear the bullets apart?"
    i "Are you challenging me?"
    show sid mad:
        xcenter .75
    i "I'll have you know I was on my school's wrestling team!"
    i "I'm more than meets the eye Bert!"
    hide sid with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Um, where is the ammo again?"
    b "In the safe."
    i "Right. See you suckers there!"
    hide sid with moveoutright
    b "...I guess we're following him, then."
    scene black with dissolve
    scene bg banklobby
    $ statusnt("Bank Safe", "bert", ch=4, sun=2)
    $ showchibint("jenny", "sid")
    with dissolve
    bi "Lauren stayed behind to make sure Freddy was okay."
    bi "The rest of us went to the safe."
    show sid ind with dissolve
    i "It's in this box, right?"
    b "Yup, that's it."
    bi "Sid grabbed some bullets and..."
    i "Hrgggggg..."
    i "Roarghhhhhhhhhhhhhhh..."
    i "RAAAAAAAAAAAAAAAAAAAAAA..."
    i "*pant*"
    i "It's not budging..."
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "Um... Sid, you said you were a wrestler..."
    j "What weight class were you in?"
    i "...{size=-10}Light flyweight.{/size}"
    j "Huh? I couldn't hear you."
    i "I said light flyweight."
    j "Isn't that one of the smallest ones?"
    show sid mad:
        xcenter .75
    i "Hey!"
    i "Minimumweight is smaller."
    j "I don't think I've ever heard of that one."
    i "Grrr."
    i "Whatever, we found out you can't separate the bullets, let's go back..."
    scene black
    bi "Sid ran off, and with nothing left to do, Jenny and I followed him."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show lauren ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    l "So?"
    i "Bert's right, it's not possible to tear the bullets apart..."
    i "Whoever loaded the gun must have loaded six in at once."
    l "Well, I was thinking about that..."
    l "What if the other five were emptied out later?"
    i "Huh?"
    l "As in, what if Bert shot Sam, and then took the other five bullets out."
    b "I mean, do you want to search my backpack?"
    l "There's no point."
    l "Even if your backpack doesn't have them, you could have hidden them anywhere."
    l "There was a conveniently long amount of time you were alone..."
    bi "She means the investigation, I guess."
    bi "Admittedly, that's also suspicious, that I'm the one relaying all the evidence..."
label trial4k:
    menu:
        bi "Thankfully, there's one flaw with Lauren's argument."

        "I wouldn't take the bullets out if I were staging a suicide.":
            bi "Yes, that's it!"
        "Jenny would have seen the bullets before I could hide them.":
            bi "No, Jenny only came when she heard me yell."
            bi "For all they know, I only called for help after hiding the bullets."
            jump trial4k
        "The safe would have had to open while I was in the lounge.":
            bi "No, Lauren's theory is consistent with Sam being the one to open it."
            jump trial4k
        "Freddy can verify that I wasn't gone long enough to hide the bullets.":
            bi "We spent a bit of time in the break room after I found Sam."
            bi "So from Freddy's point of view, I was gone for a while."
            jump trial4k
    b "Lauren, put yourself in my shoes as the murderer."
    i "So you are the murderer?"
    b "...The {i}hypothetical{/i} murderer."
    b "If I shot Sam, and then I wanted to make it look like a suicide, what would I have done?"
    l "I don't know, probably dropped the gun near Sam, maybe rearranged the body..."
    b "Right, but would I have taken out the bullets?"
    b "I think not."
    b "After all, if I wanted to make it look like a suicide, matching the story I told you..."
label trial4l:
    menu:
        b "Then the number of bullets in the gun I should have left in the gun would be..."

        "0":
            bi "Well, that's how many there were, not how many there should have been."
            jump trial4l
        "1":
            bi "Okay, I think even Freddy is good enough at math to not come up with that answer."
            jump trial4l
        "2":
            bi ""
            jump trial4l
        "3":
            bi "Maybe if the guard uniform was bulletproof, but I don't think it was..."
            jump trial4l
        "4":
            bi "Maybe if the guard uniform was bulletproof, but I don't think it was..."
            jump trial4l
        "5":
            bi "Yes, that's it!"
        "6":
            bi "If Sam commited suicide, how would the gun be reloaded to full capacity?"
            jump trial4l
    i "Five again..."
    i "For the same reason, right?"
    i "If Sam came to the break room with an empty gun, they would have had to reload it."
    i "Then, after shooting themselves the first time, I doubt they could shoot it again."
    bi "I've at least won over Sid..."
    b "Yes, exactly."
    b "If I wanted to stage a suicide, there's no reason to hide bullets."
    hide sid with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "Bert has a good point..."
    j "Not to mention, he was the one who was pushing so hard to find another explanation for Sam's death."
    j "That would be weird to do if he staged the suicide."
    j "He could have easily just agreed with us, found no evidence to the contrary..."
    bi "That... would have been a good argument to make a while ago."
    bi "Would have saved me a lot of trouble."
    l "...Yeah, I think you have a point."
    l "There's too many things that don't make sense if Bert did it."
    l "Sorry, I got caught up in it..."
    l "I guess I was getting paranoid."
    l "\"If Bert's been the one leading the effort to solve all these murders, how would we know if he did it?\""
    b "It's fine... it's not the first time we've accused someone for the sake of due diligence."
    l "But, we're back to square one now."
    l "Maybe even further back..."
    l "Square one would be if we thought Sam committed suicide."
    l "But based on the argument Bert just made, that can't be what happened, right?"
    j "Well, I'm not convinced about that either..."
    j "What if Sam is the murderer, but staged it to look like it wasn't a suicide?"
    b "Huh?"
    b "Why would anyone do that?"
    j "I don't know, but..."
    j "Maybe it was to lash out at us?"
    j "Like, \"I'm taking you all down with me!\""
    l "That seems... unlike Sam as of late."
    l "If this happened in the hospital I could maybe believe it."
    l "Here though, Sam seemed like they had been feeling... well, maybe not like themselves."
    l "But they were more optimistic recently."
    j "Sure, but what if that was just an act?"
    bi "This seems like a very elaborate theory..."
    bi "But I already have a few reasons to believe it's wrong, I think."
    bi "One is my subjective feelings about Sam, of course..."
    bi "If we debate that, we'll never come to a conclusion."
    b "I agree with Lauren, it seems unlikely..."
    b "But I don't think we'll get anywhere if we try to argue about Sam's intentions."
    j "So... what do we do then?"
    b "Look at the evidence."
    l "Bert loves his evidence..."
    b "There's one piece of evidence that I haven't figured out yet..."
    b "Something that doesn't seem to relate to Sam's death."
    bi "What I'm talking about is..."
    call screen bankEvidenceTrial(-1, 3, "trial4m") with dissolve
label trial4m:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    l "...The what?"
    b "Yeah, I barely noticed it either."
    b "It's an elastic belt, attached to the leg of a table in the break room."
    b "Part of it is torn off and missing, however..."
    l "That wasn't there before... it can't be a coincidence, right?"
    b "Appearing in the room Sam's body was in, in the span of time leading up to his death..."
    b "I'd agree, it's too good to be true."
    j "But what purpose did it serve?"
    b "I don't know... but if Sam really staged things to not look like a suicide..."
    b "It has to serve some purpose, right?"
    j "Couldn't someone else have put it there and Sam just ignored it?"
    l "Well, did anyone else here put a belt in that room?"
    j "..."
    b "..."
    l "I'll take that as a no..."
    b "Which means either Sam placed it there, or someone is lying."
    b "If someone's lying, they probably are the murderer..."
    b "So Sam didn't commit suicide."
    b "So if we want to figure out if Jenny's right..."
    b "We have to assume Sam put it there and figure out why."
    j "Hm... I have some ideas about that, actually."
    python:
        startBankTrial("jenny", "Jenny: It's a bit dark, but another method to commit suicide would be, well... {color=#f00}hanging with a rope{/color}.", -1,
        "jenny", "Jenny: There's obviously {color=#f00}no rope to be found{/color}, but the belt could be a makeshift rope.", -1,
        "jenny", "Jenny: Maybe Sam was... well, trying that method in the break room, and the {color=#f00}belt didn't have enough strength{/color} so it broke.", -1,
        "jenny", "Jenny: Sam got rid of the part of the belt attached to them, but left the other half in the break room, {color=#f00}and it fell down later{/color}.", -1,
        3, 3, "trial4n")
label trial4n:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    bi "I feel almost silly pointing this out, but..."
    b "If Sam wanted to hang... well, something with the rope, why was it attached to the table leg?"
    b "It would have to be attached somewhere high up."
    b "And if, as Jenny says, it fell down, it would have had to magically slip under the table leg."
    b "And then tied itself tightly around said leg."
    j "Hm... when you put it that way..."
    j "Yeah, I sound kinda silly, huh."
    b "But I think you're onto something for why the belt was placed there..."
    b "If the belt broke into two pieces, something must have pulled on it at some point."
    b "And this must have happened before I entered the room, because the torn piece of belt was there when I entered."
    b "Looking back at how things happened, I think I know what the other end of the belt was attached to..."
    call screen pickSpot8 with dissolve
label trial4o:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "I'm pretty sure the other of the belt was attached to the door to the break room."
    l "What makes you so sure?"
    b "For one, it's the only object near the table that you could tie the belt to."
    b "But also, if the belt was tied to the door..."
    b "There's a point where a lot of force was applied to the door, and it could have broken."
    b "That point being..."
    call screen bankEvidenceTrial(-1, 0, "trial4p") with dissolve
label trial4p:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "When I went into the break room after chasing Sam, I pulled hard on the door while opening it."
    b "I don't know why, maybe the adrenaline rush, maybe to try to catch them by surprise."
    b "But when I did, that could have easily broken the belt."
    j "Hm... that still doesn't make sense to me, though."
    j "For one, why would anyone have tied a rope to the door?"
    j "And also, why wouldn't it have broken when Sam entered the room?"
    j "And where did the other half go?"
    b "There's still a lot to figure out, I agree..."
    hide lauren with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Um... shouldn't we test this idea first?"
    b "Test... the whole idea?"
    i "Well, no, I was thinking just... does the belt even go that far?"
    i "And like, could you tear it open by just pulling on the door?"
    b "That's... actually a really good idea."
    b "Let's go grab another belt from the lockers in the locker room, and bring it to the break room."
    scene black with dissolve
    bi "We went to the locker room, grabbed a belt from a different uniform, and went to the break room."
    bi "We decided that Freddy, for obvious reasons, shouldn't come with us, and Lauren stayed with him."
    scene bg bankbreak4
    $ statusnt("Staff Kitchen", "bert", ch=4, sun=2)
    $ showchibint("jenny", "sid")
    with dissolve
    show sid ind with dissolve
    bi "Sid had taken charge, which was kind of good."
    bi "While Sid was figuring things out, I could take a break."
    bi "It felt like my brain was on a treadmill and I just turned it down to walking speed."
    i "Okay, so we tie this end here..."
    i "And then we pull gently..."
    i "And this end..."
    i "..."
    i "Yeah, it's a bit of a stretch..."
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .25
    show jenny ind with moveinright:
        xcenter .75
    j "Ha!"
    i "Huh?"
    i "Oh..."
    i "Yeah, it's a bit... of a tough one."
    i "But you can stretch the belt from the table leg to the door."
    j "Hm... we should try some other things though, right?"
    j "Like, we should see if we can open the door without the belt breaking."
    j "Because if it breaks when you open the door even slightly, then..."
    j "That means whoever tied it would be trapped in here unless they broke the belt."
    j "On the other hand, would a belt have broken when Bert pulled on the door?"
    j "Maybe there's just elastic enough to resist breaking..."
    i "Man, let's stop talking and start trying!"
    bi "Sid slowly started pushing on the door."
    i "There's some resistance from the belt, but..."
    i "It's not breaking."
    b "Okay, so it would have been possible to tie the belt and then leave the room."
    b "So if it was tied to the door, it could have been tied before I entered the brea-"
    blank "*click*"
    i "Oh, huh."
    b "What happened?"
    i "I let go of the handle and the door closed a bit later."
    b "I guess that makes sense if the belt is pulling on it enough to cause some resistance..."
    i "And now the other question..."
    hide sid with moveoutright
    bi "..."
    blank "*snap*"
    show bg bankbreak3 with dissolve
    show sid with moveinright
    i "I pulled on the door, and..."
    b "And the belt broke."
    b "Anything else we need to figure out?"
    i "No, I think that's everything."
    $ bank_extra[11] = True
    tut "Torn Elastic Belt's description has been updated in the evidence menu."
    j "Are we sure all the belts are the same?"
    j "Maybe different belts have different amounts of stretch..."
    i "I mean... we could go and try this with every belt if you want."
    j "Hm..."
    j "I'll go take a quick look and see if the belts are all the same size, at least."
    j "Just to be sure, you know..."
    j "It's not like all the guards would have been the same size."
    j "You guys can go back to the lobby, if you want."
    b "No, we should go with you just to double-check."
    j "Oki!"
    scene black with dissolve
    bi "We checked, and all the belts were in fact the same size."
    bi "Not too surprising, belts can be made one-size-fits-many."
    bi "As we walked back to the lobby, I was thinking..."
    bi "Jenny seems very hard-pressed to prove Sam committed suicide..."
    bi "On the other hand, Sid very eagerly jumped on the theory I proposed..."
    bi "Not to mention Lauren trying to accuse me earlier..."
    bi "It's all very suspicious."
    bi "Is Jenny trying to pin her murder on Sam?"
    bi "Is Lauren trying to pin her murder on me?"
    bi "Is Sid leading us down the wrong road intentionally?..."
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show sid ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    bi "Before I could finish that train of thought, we were back in the lobby."
    l "Welcome back. What'd you guys find?"
    i "The belt reaches from the table leg to the door."
    i "It pulls on it with enough force to close the door slowly."
    i "And if you tie it at both ends, you can open the door without breaking it."
    i "But a quick yank on the door does cause it to break."
    l "Interesting..."
    l "Bert may be on to something after all."
    hide sid ind with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "This seems like a dead end to me."
    j "Sure, the belt probably had something to do with the murder."
    j "But it doesn't explain other contradictions between Bert's alibi and Sam not being the killer."
    b "Other contradictions?"
    j "Yeah, I didn't bring it up earlier, but..."
    python:
        startBankTrial("jenny", "Jenny: If Sam didn't commit suicide, that means {color=#f00}you saw someone else fled the lobby{/color}.", -1,
        "jenny", "Jenny: Everyone else wasn't in the break room when Bert found Sam, {color=#f00}so the killer wasn't in the break room when the body was found{/color}.", -1,
        "jenny", "Jenny: But if the killer didn't run in there, {color=#f00}you wouldn't have seen the break room door close{/color}.", -1,
        "jenny", "Jenny: Not to mention, the gun you saw the killer holding {color=#55f}is the same one we found in the break room{/color}.", -1,
        2, 3, "trial4q")
label trial4q:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "With what we know about the belt..."
    b "It's very plausible for me to have seen the break room door close, if the belt was used to close it."
    b "Suppose the belt was attached to the door before the killer shot at Freddy and I in the lobby."
    b "Then all they would have to do is open the door while they were running past it."
    b "They had a head start on me, that's plenty of time to open the door, lob the gun..."
    b "And then get around the hallway corner before I could see them."
    j "But wait..."
    j "Earlier we said that Sam couldn't have shot the gun because it would have been while you were in the hallway."
    j "And we knew you were in the hallway because Sam would have been the one to close the door, which you saw happen."
    j "But now you're saying the belt closed the door."
    j "Which means Sam could have shot the gun while you were still far away in the lobby!"
    l "...She actually has a good point here."
    l "We just disproved what we thought must be true earlier, about when Sam would have had to shoot themself."
    l "It's now a possibility again."
    l "The belt could even have been diversion by Sam."
    l "Bert, do you remember exactly how many seconds passed before you gave chase?"
    b "Uh... no. Just that I was in shock for a bit before I did."
    l "Then maybe Sam had time to tie the belt after leaving the lobby."
    b "But we also said the number of bullets doesn't make sense if it was a suicide."
    j "Maybe there's another source of ammo we didn't find?"
    b "Okay, but why would Sam tie the belt to the door?"
    l "Maybe to lock the room so we couldn't find their corpse?"
    b "No, because I saw the door close, presumably due to the belt."
    b "That means if Sam tied the belt after reaching the break room, they opened the door at least once."
    b "They would have known it didn't lock the door."
    j "Maybe the belt messed with the other evidence somehow."
    j "Like when it broke it swept around the floor and moved the gun around!"
    bi "I could spend all day knocking down these ideas..."
    bi "I need to present a definitive point against what they're saying if I want this to end anytime soon."
    b "Okay, fine."
    b "Let's assume that Sam was the one who tied the belt."
    b "Then one of us did something that we're not confessing to."
    b "It's related to..."
    call screen bankEvidenceTrial(-1, 3, "trial4r") with dissolve
label trial4r:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "Half the belt is missing."
    b "If it was tied to the door when Sam died, then obviously Sam couldn't have removed it."
    b "Which means... one of us did."
    b "Does anyone want to own up to that?"
    l "..."
    j "..."
    b "Then I {i}really{/i} think we should consider the possibility that someone else is the murderer..."
    b "And they're not telling us that they removed the belt."
    hide lauren with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Jenny..."
    i "I think I have to agree with Bert on this one."
    i "We might be wasting a lot of time barking up the wrong tree."
    i "Just like dumb adults do!"
    i "Can't you guys be cool adults?"
    j "..."
    j "Okay, fine."
    j "I still think it was a suicide, but..."
    j "I guess we can't rule every other possibility out entirely."
    b "Great, now that we're all on the same page..."
    i "Well, let's think about who could have done it."
    i "..."
    j "..."
    i "Okay, I'm stumped."
    i "If it wasn't Sam then it seems like there's no clues about who it could be."
    j "So... you think it was a suicide?"
    i "Well, no, just..."
    i "How do we figure anything out if it isn't Sam?"
    b "Well, we can narrow it down a bit."
    b "Freddy and I were in the lobby with the shooter, so we can't have been the shooters."
    b "Plus, based on our discussion so far, we think the killer set up the belt and lobbed the gun into the break room."
    b "Then they turned the corner to the east of the building before I could see them."
    b "Which is, conveniently, where..."
    b "Well, the only candidates are one of you three."
    show sid ind:
        xcenter .75
        linear 0.15 xcenter .5
    show lauren ind with moveinright:
        xcenter .75
    b "All three of you were."
    j "Wait, all three of us were there?"
    j "I saw Sid napping but I didn't see Lauren..."
    l "Huh, I didn't see you or Sid."
    i "Yeah, I didn't see either of you..."
    bi "Right, they told me their alibis, but didn't tell them directly to each other."
    b "Now might be a good time for everyone to recap where they were before we found the body..."
    hide sid
    hide lauren
    with moveoutright
    show jenny ind:
        xcenter .25
        linear 0.5 xcenter .15
    j "Okay, so where was I..."
    j "I finished taking a shower, walked out of the locker room into the hall, saw the green lights."
    j "Oh, and the safe door was open. I saw Sid napping on the couch."
    j "Then I heard Bert yell, and went to see what happened."
    hide jenny with moveoutleft
    show sid ind with moveinleft
    i "Um, I was sleeping on the couch, like Jenny said."
    i "When I woke up, I noticed the red light in the hallway had turned green."
    i "I went to go check out the safe, then I heard Bert yell before I could go in."
    i "So I ran from the safe, past the office, to the break room."
    hide sid with moveoutleft
    show lauren ind with moveinleft
    l "I was searching for clues in the director's office."
    l "I couldn't find anything, so I went to go look for other people."
    l "I walked to the locker room, didn't find anyone there."
    b "And the safe was closed when you walked from the office to the locker room?"
    l "Yep. After that I went to the break room and found you and Jenny."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show sid ind with moveinleft
    show jenny ind with moveinleft:
        xcenter .25
    j "Hm... it's kind of inconvenient."
    j "None of us really saw each other, except me seeing Sid."
    j "So we don't really have a way to confirm each other's stories."
    i "Hey! You can confirm I was taking a nap!"
    l "Yeah, but I don't know what you were doing before or after Jenny saw you..."
    l "You could have even been fake sleeping."
    i "Hmph, like I could ever pretend to sleep on a couch as comfy as that."
    i "You've never heard the Signature Sid Siren Snore!"
    i "A sound only the most asleep man could ever make!"
    j "...The what?"
    i "No one could recreate that sound on purpose!"
    l "Well, that means Jenny can't confirm she heard the sound then."
    j "Yeah, it seemed like you were sleeping pretty lightly..."
    i "...Shoot!"
    b "Enough about the snores..."
    b "It's true that none of you can confirm each other's alibis."
    b "But that doesn't mean you can't refute them..."
    l "What do you mean by that?"
    b "There's a pair of your alibis that seem to contradict each other."
    $alibiset = set()
label trial4t:
    menu:
        set alibiset
        b "That pair is..."
        "Jenny and Lauren":
            b "Jenny and Lauren."
            j "Us?"
            j "But... I was just telling the truth."
            l "I don't understand... what about our stories doesn't add up?"
            jump trial4ti
        "Jenny and Sid":
            b "Jenny and Sid."
            j "Huh?"
            show sid mad
            j "That's surprising... I would have thought that I'd indirectly confirmed Sid's alibi."
            j "After all, I did see him sleeping."
            i "Yeah, what gives punk?"
            b "Well, what doesn't make sense is..."
            jump trial4tii
        "Lauren and Sid":
            b "Lauren and Sid."
            i "Huh?"
            show sid mad
            i "Whatchu trying to say, punk?"
            b "All I'm trying to say is, your alibi and Lauren's alibi are contradictory."
            b "The contradiction is..."
            jump trial4tiii

label trial4ti:
    menu:
        b "The contradiction is..."
        "The locker room.":
            b "Lauren would have ran into Jenny in the locker room!"
            j "...Or I left before she got there."
            b "Oh... I guess you could have missed each other, yeah..."
            jump trial4ti
        "The safe.":
            b "The safe!"
            b "Lauren said the safe was closed, but Jenny said she saw the safe opened when she left the locker room."
            b "Which means, Lauren must have passed by the safe before Jenny left the locker room."
            b "But then she would have seen Sid napping on the couch, since Jenny saw Sid sleeping and the safe opened."
            b "So we know Sid didn't wake up until after the safe was opened."
            l "What if Sid left the couch, then came back before Jenny saw him?"
            b "Well even then, either Jenny would have run into you in the locker room..."
            b "Or, you would have left the locker room before Jenny did, and heard me scream."
            j "Hm..."
            j "Yeah, there's a lot of possibilities, but all of them make Lauren's alibi and mine seem inconsistent."
            l "Wait, couldn't the safe door have just closed after Jenny left the locker room, but before I left the office?"
            l "It's not like once it's open it has to stay open."
            b "The safe door, sure, but as far as I know there's no way to lock the safe itself."
            i "Yeah, surely you would noticed the lights!"
            i "After all, who could resist the possibility of taking all that schmoney!"
            bi "...Most of us, but that's besides the point."
            l "Wait, the lights?"
            b "Yeah, they changed color from red to green, presumably because the safe opened."
            l "...Oh."
            l "Okay, this is going to seem very convenient, but you have to trust me on this."
            l "I'm red-green colorblind."
            b "...Huh?"
            l "Yeah, I know it's rare for girls but... I am."
            l "I know there's not really any way for me to prove it, but you have trust me..."
            l "Damn, if Sam was still alive they could confirm."
            l "I asked Sam if there was a cherry soda in the hospital vending machine, and they thought I was dumb."
            l "But it's because I couldn't tell..."
            l "I'd have no way of knowing who would be murderer in the bank when I was in the hospital!"
            l "So it's not like I could have done that as a convenient excuse..."
            b "Um... I'm not really sure how we can confirm or deny this."
            if len(alibiset) < 3:
                j "Bert, I think we should trust Lauren for now and see what else we can figure out."
                j "Is there anything else about our alibis that's suspicious?"
                b "Yeah, actually, there's another pair of alibis that seems fishy..."
                jump trial4t
            else:
                b "I guess, let's assume Lauren is telling the truth for now."
                bi "Anyway, that's all the contradictions..."
                jump posttrial4t
        "The screaming.":
            b "Lauren should have heard me screaming!"
            l "Not necessarily."
            l "It's possible I was in the office or locker room when it happened."
            l "Maybe the scream wasn't loud enough to be heard if you weren't in the hallway."
            b "Oh..., yeah that's true."
            b "I was on the other side of the building..."
            jump trial4ti
        "You didn't pass each other.":
            j "Well, Lauren reached you in the break room after me, right?"
            j "So maybe she just went to the locker room after I left it, then followed my path."
            l "Yeah, if anything that seems like the most consistent part of our stories..."
            b "Oh... uh, haha, slip of the tongue!"
            jump trial4ti

label trial4tii:
    b "The contradiction is..."
    menu:
        "The locker room.":
            b "The locker room!"
            i "...The locker room?"
            i "The one I never claimed to go into in my alibi?"
            b "Uh..."
            bi "Yeah, I guess nothing about the locker room really pertains to Sid's alibi..."
            jump trial4tii
        "The safe.":
            b "You have conflicting stories about the safe!"
            j "...We both said it was open."
            i "Yeah, that's us agreeing with each other..."
            show sid ind
            i "Oh, I get it."
            i "Thanks Bert! You're telling us we're innocent!"
            b "No, wait, let me rethink that."
            i "So... you still think I'm still not innocent?"
            show sid mad
            i "Grrr..."
            bi "I'd better fix my answer before Sid gets too mad..."
            jump trial4tii
        "The screaming.":
            b "Both of you claimed to hear someone yell..."
            i "Yeah, that makes sense!"
            i "After all, we were both in the hallway when you screamed."
            b "Well, it's not about where you claimed to have hear me, but when."
            b "Jenny claimed to hear me scream when Sid was asleep."
            b "But Sid also claimed to hear me scream..."
            b "After he woke up."
            b "And I don't remember screaming twice."
            i "..."
            j "Sid?"
            i "Did nobody else scream afterwards?"
            i "Maybe I heard someone else react after I woke up..."
            j "Oh, you think you heard me or Lauren?"
            i "Maybe..."
            j "I mean, we were both shocked when we saw Sam..."
            b "But... were you loud enough to be heard from across the bank?"
            b "When I found the body I was yelling into the hallway so people would hear."
            b "But Jenny and Lauren wouldn't have made a deliberate attempt to be heard..."
            i "...Wait, why's all the pressure on me?"
            i "What if Jenny's lying about the timing of the yell to incriminate me?!"
            i "Or she's lying about seeing me sleeping!"
            i "It's not like I saw her!"
            b "...Huh."
            j "Um... I mean, I wasn't lying?"
            i "That's easy for you to say punk!"
            i "I can say I wasn't lying either!"
            if len(alibiset) < 3:
                b "I don't think there's any way to tell which of you is lying..."
                b "Maybe we table this for now, and look for other contradictions."
                j "Others?"
                b "Yeah, there's another pair of alibis that bothers me..."
                jump trial4t
            else:
                b "Hmm, I don't think there's a way to figure out who's lying..."
                b "But, that's all the contradictions..."
                jump posttrial4t
        "You didn't pass each other.":
            j "...Bert, I said I passed Sid when I was going towards you screaming."
            j "How else would I see him sleeping?"
            b "Oh."
            b "...Yeah, but Sid didn't pass you!"
            b "Or see you pass him!"
            j "I mean, that's true, but it's not a contradiction..."
            b "...Yeah, you're right."
            b "Let me rethink this..."
            jump trial4tii
label trial4tiii:
    menu:
        "The locker room.":
            b "The locker room!"
            i "...The locker room?"
            i "The one I never claimed to go into in my alibi?"
            b "Uh..."
            bi "Yeah, I guess nothing about the locker room really pertains to Sid's alibi..."
            jump trial4tiii
        "The safe.":
            b "The safe!"
            b "Sid said he saw it open, but Lauren said when she passed it, it was closed!"
            j "Um... Lauren reached the break room after Sid."
            j "So presumably her alibi occurred after Sid's."
            i "Yeah punk! Maybe the safe opened between when Lauren passed it and when I did."
            b "Oh... yeah, that's true."
            bi "..."
            bi "I think there's something wrong with what we just discussed, but..."
            bi "They're right that the safe is not the most pressing part of it."
            jump trial4tiii
        "The screaming.":
            b "Sid said he heard me yelling, but Lauren didn't!"
            l "So... what's the issue?"
            l "I could have just been in the office while it happened."
            i "And I could have been in the hallway when it happened!"
            l "Yeah, we didn't see each other, so I don't see a contradiction there."
            b "Um..."
            b "Okay, that's not a contradiction, but what is a contradiction is..."
            jump trial4tiii
        "You didn't pass each other.":
            b "Sid, remind me where you went after you woke up on the couch?"
            i "To the front of the safe, then to the break room."
            b "So you passed the locker room, then the safe, then the office."
            i "Yeah, what about it?"
            b "And Lauren, you left from the office, passed the safe..."
            l "...And then checked the locker room."
            b "Right. And... you didn't see Sid on the couch."
            l "No, I didn't."
            b "So somehow, you two went around the safe in opposite directions..."
            b "And didn't run in to each other."
            i "Wait!"
            i "Couldn't Lauren have just been in the office the whole time I was walking around?"
            b "Well, maybe..."
            b "But she reached the break room before you did."
            b "So if that's what happened..."
            b "Somehow, Lauren did a whole lap around the bank in the time it took you to walk a few feet."
            b "And even if that happened..."
            b "How would you not have run into each other in the hallway after you both looped around the safe?"
            l "...Yeah, you're right."
            l "We should have run into each other."
            i "So... Lauren is lying then."
            l "I am?"
            i "Well, I'm not!"
            l "Sid... I think you're the one who's lying."
            l "Bert, surely there's a way to prove one of our alibis."
            b "Unfortunately... I don't think there is."
            b "Jenny saw Sid sleeping, but otherwise..."
            b "I mean, unless there's something else one of you hasn't told us."
            i "Nope. I'm telling the truth!"
            i "And Lauren's lying."
            if len(alibiset) < 3:
                bi "This is getting nowhere..."
                b "Okay, maybe it would help to point out another contradiction..."
                jump trial4t
            else:
                bi "This is getting nowhere..."
                b "Okay, let's ignore that for now."
                b "Accounting for all the contradictions..."
                jump posttrial4t

label posttrial4t:
    b "I think from the three of you, one of you is very likely lying about their alibi."
    b "That person is..."
    call screen chooseCharBank("sid", "trial4u", "Who is most likely lying about their alibi?") with dissolve
label trial4u:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    b "Sid."
    show sid mad
    i "Me?"
    i "But what about Lauren?"
    i "She could be lying about colorblindness!"
    i "And maybe she lied about where she went!"
    b "Well, it's true maybe Lauren is lying."
    b "But, when I pointed out the contradiction in Lauren and Jenny's alibis..."
    b "There was a plausible explanation Lauren gave."
    b "So if she's telling the truth, then that would mean you're lying."
    b "One person lying is believable."
    b "On the other hand, Sid..."
    b "Both times I found a contradiction involving your alibi, there wasn't a satisfying resolution."
    b "So in order for you to be telling the truth, both Jenny and Lauren would have to be lying."
    b "Or, there'd have to be some crazy explanation we can't think of."
    i "No! I didn't lie!"
    i "How could you think that when I was being so helpful earlier!"
    l "Sid... why would you lie..."
    l "You know how this game works..."
    j "Did... did you do it Sid?"
    j "Did you kill Sam?"
    j "I know you hated them, but..."
    i "No, I don't hate Sam!"
    i "We didn't get along, but..."
    i "I swear I didn't kill them!"
    show scary with dissolve:
        alpha .5
    bi "..."
    bi "Lauren and Jenny both sounded disappointed."
    bi "Equally willing to accept Sid was the killer."
    bi "I was hoping one of them was more willing to believe Sid."
    bi "Because..."
    bi "I think Sid's not the killer."
    bi "And I need to figure out which of Jenny and Lauren is."
    bi "Well, for now Sid's still lying in his alibi."
    bi "And I think I need to earn his trust by proving his innocence before he'll admit it."
    hide scary with dissolve
    b "Sid... I never accused you of being the murderer."
    b "In fact, I don't think you did it."
    i "Hmph."
    i "You're just saying that so I'll soften up to you!"
    bi "Yup, as I thought, I can't just say it, I'll have to prove it..."
    b "No, I believe that."
    b "I'm going to prove it... and then I need you to help me solve this murder when I do."
    b "Including telling me what your real alibi is."
    b "Deal?"
    i "..."
    show sid ind
    i "I mean, I know I'm innocent, but..."
    i "Yeah, you should definitely convince the others."
    i "It'd be best for the case, or something."
    bi "That wasn't him promising to tell me the truth, but..."
    bi "I'll take it for now."
    l "Wait, if you're claiming Sid is innocent..."
    l "That means one of me or Jenny is the killer."
    b "Yes, precisely."
    l "...And you expect both of us to go along with this?"
    l "That's a 50/50 shot I get accused as an innocent."
    j "Hey, implying I'm guilty?"
    l "Well, if it's not me..."
    j "Hmph. Well now I kind of think it is you!"
    l "Well, all the more reason why we shouldn't rule out Sid so easily."
    b "Look, let me make a convincing argument..."
    b "If you're innocent, you should believe any convincing argument."
    l "Pshh. Fine."
    l "So what makes Sid so innocent?"
    b "Well, first, we need to think about where the killer went after the murder and why."
    b "In particular, I think the murderer had to go to..."
    call screen pickSpot9 with dissolve
label trial4v:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    b "The locker room."
    i "Yeah, the locker room! I didn't go there!"
    i "...Um... why the locker room?"
    b "Well, it comes back to something I found earlier while investigating..."
    b "Something that I couldn't have found if the killer didn't go back to the locker room."
    call screen bankEvidenceTrial(-1, 11, "trial4w") with dissolve
label trial4w:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    b "When I was investigating, there was a uniform missing from the locker room."
label trial4x:
    menu:
        b "If the killer never went back to the locker room, the number of missing uniforms should have been..."
        "0":
            bi "Zero!"
            bi "...Wait, no, Sam is wearing one that wouldn't be in the locker room."
            jump trial4x
        "1":
            bi "One!"
            bi "Wait... that's consistent with what I found. I'd have nothing to prove from that."
            jump trial4x
        "2":
            b "Two!"
        "3":
            bi "Three!"
            bi "Wait... no, that's too many."
            jump trial4x
    b "One that Sam is still wearing, and the one the killer was wearing in the lobby."
    b "They can't be the same, because we already established I was closely following the killer."
    b "They wouldn't have had time to change Sam into their uniform."
    b "Sam is still wearing a uniform, so the killer's must have been returned."
    l "Okay, but how does that absolve Sid?"
    b "Well, Jenny, when you saw Sid, did he have a uniform with him?"
    j "Um... no, I don't remember seeing anything like the uniform. I don't think he had it."
    j "Unless he managed to stuff it in his pockets."
    b "Which is unlikely."
    l "But he could have just hid it elsewhere until Jenny walked by him, then moved it to the locker room."
    l "Then Jenny would give him a convenient alibi."
    b "Sure, but remember that Jenny saw Sid on the couch shortly before she heard me yell."
    b "And I yelled shortly after finding the body, and I was only a few seconds behind the criminal."
    b "So Sid would have had a very tiny window to hide the uniform."
    l "He could have just hidden it in the couch he was sleeping on."
    b "You really think he could hide an entire uniform in that small couch?"
    l "Maybe he could."
    l "I don't think we can rule it out."
    l "So unless you have any other evidence, it's your opinion against mine."
    b "Funny you mention that..."
    b "There's another piece of evidence that rules Sid out."
    b "Between when I found Sam's body and finished investigating the break room..."
    b "Jenny and Lauren were in the break room."
    b "But Sid didn't show up until after I finished investigating the break room."
    i "Bert! That just makes me sound more fishy."
    i "How is this evidence in my favor?"
    b "Well, I think the murderer had to have been by the break room before I finished investigating it."
    b "Because of this..."
    call screen bankEvidenceTrial(-1, [1, 11], "trial4y") with dissolve
label trial4y:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    i "The belt again?"
    b "Yes, remember, we think the other end was tied to the door."
    b "And that when I went into the break room, the belt snapped in two."
    b "But when I investigated the break room..."
    b "I didn't find the other half of the belt."
    b "Which means it must have been removed before I finished investigating."
    b "Lauren and Jenny came to the break room in that period of time, so they could have removed it."
    b "But Sid..."
    b "He couldn't have."
    j "But why would the person who removed it be the murderer?"
    b "Well, who else would have a reason to remove it?"
    b "That would just be concealing evidence..."
    b "Which is exactly what the murderer would want to do."
    j "Hm..."
    j "Hate to say it Lauren, but between the belt and the uniform..."
    j "It seems really hard for Sid to have been the killer."
    l "So? Really hard doesn't mean impossible."
    b "I mean, we can never know for sure who did it."
    b "Even if someone confessed, they could be lying for some reason."
    b "We just have to go with what's our best shot."
    b "And we won't know what that is unless we choose to believe in Sid, and Sid tells us the truth."
    l "..."
    l "Yeah, you're right."
    l "I'm sorry..."
    l "Once we rule out Sid, then I have to believe Jenny did it."
    l "And... I'm not ready for that."
    l "The five of us have been together the longest..."
    l "It will hurt so much to be betrayed by one of you."
    l "At least right now I have some plausible deniability for both Jenny and Sid..."
    j "Aww, it's okay Lauren."
    j "The feeling's mutual, now I know you did it!"
    l "Hmph. I guess you have to say that, even if..., no, even though you did it."
    bi "This situation hadn't arisen before..."
    bi "Usually we had a primary suspect, or none at all."
    bi "But assuming we haven't made any mistakes so far..."
    bi "We have two suspects, they both know it, and the situation means they're actively working against each other."
    bi "One of them will be trying to lie to pin it on the other..."
    bi "The other, trying to help us find the truth."
    bi "It's my job to figure out which one is which."
    b "Okay, Sid."
    b "Now it's your turn."
    b "To tell us what really happened."
    i "Okay, um..."
    i "We're 100% sure it wasn't me, right?"
    l "I mean, I'm not, but..."
    l "I'll give you 90%."
    i "Hey, that's not enough!"
    b "Sid, please..."
    b "If you tell us what happened that number can only go up."
    b "If you're withholding information and we find that out, it'll go down."
    i "...Sigh, fine."
    i "I went in the safe."
    b "Huh?"
    i "I actually woke up when I heard Bert yelling for help."
    i "I opened my eyes slightly... it's a little trick I learned at home."
    i "Sometimes my mom and dad would fight and I wouldn't want them to know I was listening."
    i "So I'd pretend to nap, but my eyes would be barely open."
    i "I saw the lights were green, and I saw Jenny moving towards Bert yelling."
    i "And I thought, if I wait for her to leave I can check out the safe and no one would be suspicious of me."
    i "I was really hoping there was money in there, and I got greedy..."
    i "So I went in. But only for a few minutes! It was pretty much empty when I went in there, so I left shortly after."
    i "If I knew a murder happened, I wouldn't have gone to the safe, I swear!"
    $ bank_extra[12] = True
    tut "Sid's Account description has been updated in the evidence menu."
    bi "I don't entirely believe that, but it'd only hurt to mention that..."
    j "Ah, so Sid's alibi and mine don't contradict anymore!"
    l "And, neither do ours."
    j "Oh."
    j "...Then what?"
    j "I mean, again, I know Lauren's the killer."
    j "But... it is true Sid just resolved all the contradictions in our alibis."
    j "So how do I prove it now?"
    l "I should be the one asking that..."
    j "How do you prove you're the killer? That should be easy!"
    l "No, that's not what I..."
    l "Never mind."
    b "Wait, explain to me why you think this resolves the contradictions I pointed out earlier?"
python:
    startBankTrial("jenny", "Jenny: Sid and I both heard you yell at different times, but Sid {color=#f00}lied about when he heard you yell{/color}.", -1,
    "jenny", "Jenny: Sid and I {color=#f00}heard the same yell{/color}, but he was pretending to be asleep.", -1,
    "lauren", "Lauren: You said it's a contradiction that Sid and I didn't pass each other. But {color=#f00}I could have passed Sid while he was in the safe{/color}.", -1,
    "lauren",  "Lauren: The {color=#f00}safe door was closed{/color}, so we didn't see each other.", -1,
    3, [9, 12], "trial4z")
label trial4z:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    b "Lauren..."
    b "The safe door can't have been closed."
    l "What? We already went over this."
    l "I know now the door was unlocked at the time, but I didn't know then because of my colorblindness."
    b "No, I'm not talking about being locked, I'm talking about being closed, like shut."
    b "Well, locked and shut are kind of the same thing, actually."
    b "On the inside, you can't actually open the safe door even if it's unlocked."
    b "Jenny and I tested this earlier."
    l "So? I was on the outside."
    l "Information about being on the inside doesn't change my alibi."
    b "Not in isolation, no..."
    b "But Sid was inside the safe when you passed by."
    b "If the safe door was really closed, Sid would have been locked in there."
    i "Hey... yeah!"
    l "Okay, but what if Jenny trapped Sid in there, and then let him out later?"
    i "You think I wouldn't hear the door close?"
    l "Maybe it closed quietly?"
    b "No, I'm pretty sure Jenny didn't trap Sid in there."
    b "If, as you say, you passed the safe, checked the locker room, and then came to the break room..."
    b "Jenny, who came to the break room before you, wouldn't have had a window to let Sid out."
    b "She would have had to come to the safe after you passed it, opened it, and then run back to the break room..."
    b "All without being seen by you while you were in the hallway, and while beating you to the break room."
    b "Even if somehow Sid had his back turned to the door the entire time and couldn't hear it close..."
    b "It seems too hard to pull off."
    l "Maybe Jenny was lying when you tested the safe door?"
    l "She's the only one who we know has tried to leave the safe while the door is closed."
    i "Okay, you test it! We'll close the safe door on you and you try to get out!"
    j "Sid, I'm not lying but... you're basically advocating for jailing her in there."
    i "Well we'd let her out, obviously!"
    l "Sid it's... it's fine, I don't need to test it."
    l "I guess Jenny wouldn't lie about something that could be checked so easily."
    l "...Okay, what if Jenny kept the door barely open?"
    l "That way he wasn't locked in, but it would be hard to tell the door was open."
    l "If Sid didn't notice it would be a great way to implicate me."
    i "I mean... I'm pretty sure the door was wide open when I left."
    i "But... maybe I'm forgetting."
    b "No, that's not possible."
    call screen bankEvidenceTrial(-1, 9, "trial4aa") with dissolve
label trial4aa:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    with dissolve
    b "The safe door opens and closes electronically, and when it does it moves a full ninety degrees."
    b "If Sid wasn't trapped in the safe when you passed it, you would've seen the door wide open."
    l "Okay, fine, maybe the safe door was open when I passed by it."
    l "Then things look pretty bad for me..."
    l "But there's something you haven't considered."
    l "Why would I lie about passing Sid? If you believe that then you must have some reason why I did it..."
    python:
        startBankTrial("lauren", "Lauren: Lying about not seeing Sid {color=#f00}only makes me more suspicious{/color}. The murderer would try to avoid suspicion.", -1,
        "lauren", "Lauren: I had {color=#f00}no way to know Sid would lie in his alibi{/color}. So I had no reason to come up with a lie that looked suspicious if Sid told the truth.", -1,
        "lauren", "Lauren: If Sid and I saw each other while he was in the safe, we could confirm each other's alibis and {color=#f00}it would only make me seem more innocent{/color}.", -1,
        "lauren",  "Lauren: Also, why wouldn't I point out Sid lied earlier if I knew he went in the safe? {color=#f00}It would make Sid seem like the murderer{/color}.", -1,
        2, 11, "trial4ab")
label trial4ab:
    scene bg banklobby
    $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
    $ showchibint("freddy", "jenny", "lauren", "sid")
    with dissolve
    show jenny ind:
        xcenter .25
    show sid ind
    show lauren ind:
        xcenter .75
    b "You say if you and Sid saw each other it would make you seem more innocent."
    b "That would be true if you weren't the murderer."
    b "But we know after running away from the lobby, the murderer was carrying something."
    b "Something we've discussed earlier."
    b "A uniform, that they needed to return to the locker room."
    b "If it was seen outside the locker room, we would have known someone besides Sam wore it."
    b "We would figure out immediately known Sam didn't commit suicide."
    l "..."
    b "It was a pretty clever murder, all things considered."
    b "You shot Sam, presumably a long time before you entered the lobby."
    b "You placed their corpse in the break room, wearing the uniform."
    b "You put on a uniform, to imitate Sam, then shot at me and Freddy."
    b "But you weren't actually trying to kill us, you were just making it seem like Sam was."
    b "After all, if we just found Sam's body, even with a gun next to it..."
    b "We might not think it was a suicide."
    b "You set up the room so the door would close on its own, as if Sam ran in there."
    b "You ran from the lobby, and then threw the gun in the break room next to Sam's corpse."
    b "To us, it looked like a suicide at first."
    b "Then, you carefully avoided being seen by Jenny and Sid with the uniform."
    b "You returned it to the locker room."
    b "That way, no one would think the person in the lobby wasn't Sam."
    l "But I made too many mistakes."
    l "I didn't think about the number of bullets in the gun at all..."
    l "I've never seen bullets you have to load six at a time before, so it never crossed my mind."
    l "I tried to hide the belt used to close the break room, but couldn't grab the other half."
    l "If I had just left the belt on the break room door, we wouldn't have absolved Sid."
    l "And I didn't realize the safe door would trap Sid inside if it were closed."
    l "After all, it's not something I could test myself..."
    l "Of course I didn't even think you would figure out Sam didn't commit suicide."
    l "So I never thought I'd have to defend myself, but even if I did, I was ready."
    l "I was going to lie and say the safe door was closed, and if Sid said it was open..."
    l "I was hoping you wouldn't be able to tell if Sid or I was lying or misremembering."
    l "So many mistakes..."
    l "Even just one less and I might have gotten away with it."
    l "But then again, one less mistake, and I might not even be in this game..."
    b "..."
    bi "I didn't know what to say."
    bi "It was like when you beat your friend in a game, and they tell you \"well I would have won if...\""
    bi "Except it was a game with our lives on the line."
    l "I bet you guys have questions, but..."
    bi "She glanced at Freddy to make sure he wasn't in earshot, then whispered."
    l "I don't want Freddy to have to listen."
    l "Not just because it's too violent for a kid, but..."
    l "The last thing he needs is to feel betrayed by me."
    scene black with dissolve
    bi "We left the lobby, giving Lauren a chance to say her goodbyes to Freddy."
    bi "Lauren asked Jenny to stay in the lobby and watch over Freddy."
    bi "Presumably because she was the most motherly person remaining, which was a fair assessment."
    bi "Jenny was happy to oblige."
    bi "Not sure how much time we had left, we reconvened in the nearby break room."
    show bg bankbreak with dissolve
    $ statusnt("Staff Kitchen", "bert", ch=4, sun=2)
    $ showchibint("lauren", "sid")
    show lauren ind with dissolve
    l "So... what do you want to know?"
    $menuset = set()
label laurAsk:
    menu:
        set menuset
        bi "What to ask..."

        "Why this bank?":
            l "Well, I told you guys about my crime..."
            l "I was in public and a witness to a robber."
            l "The robbery happened here, in the lobby."
            b "Um..."
            l "It's the story I told Sam back in the hospital, you might not remember."
            l "I was here in line to cash a check when a robber came in and started waving a gun around."
            l "He yelled at the tellers to start loading money into bags."
            l "I had a gun in my purse, so I waited for him to turn around."
            l "Firing a gun isn't as easy as they make it seem in the movies."
            l "I was doing my best to turn off the safety and load a magazine while keeping it hidden."
            l "In retrospect, it was probably an idiotic move."
            l "I don't think he was actually planning to shoot."
            l "He just needed to intimidate people and make a clean run for it."
            l "But I was panicking, couldn't think straight."
            l "And well... I eventually was ready to fire, took aim, and fired three shots."
            l "Unfortunately, for whatever reason, one of the shots missed..."
            l "And hit a girl, a few years younger than me."
            b "I hate to ask, but... what was her name?"
            l "It wasn't Sydell, if that's what you're asking."
            l "I met her parents eventually, neither of them was a Sydell."
            b "That's weird... if that's your crime, how does it connect to the rest of us?"
            b "Maybe Mr. Sydell was close to the girl somehow?"
            l "I wouldn't know, not like I could ask her."
            l "Or even would have known who Sydell was when I met her parents."
            b "There has to be some connection though..."
            l "Bert, I know you want to figure out who the Game Master is from the information I'm telling you."
            l "But... if there were a tight connection I knew of..."
            l "Then wouldn't I have shot the right person?"
            b "Hm, that's true..."
            b "I guess, we don't know that Sam {i}isn't{/i} the right person..."
            l "Well, if Sam is the Game Master, then nothing I can tell you matters anyway."
            b "Yeah, good point."
            b "Alright, I have other stuff I want to ask you, no use spending more time on this, I guess."

        "How did you open the safe?":
            l "Well, just like everyone else I've been getting an advantage."
            l "Mine was... I was told that someone here has a birthday on July 17th."
            l "With that information I was able to open the safe."
            b "You knew your birthday and the 17th... don't you need a third digit?"
            l "Oh, yeah, Freddy told me his birthday."
            b "What? But Jenny told him not to!"
            l "Well, he technically followed her instructions."
            l "He told me way back in the mansion."
            b "Why didn't he tell us that he told you?!"
            l "Bert, you're giving a lot of credit to Freddy."
            l "He's just a kid, we've been keeping most of the game secret from him."
            l "And we're all hungry, tired, missing our friends and family..."
            l "He could have easily forgotten, decided to lie about it because he likes me..."
            b "Yeah, I guess it was never a foolproof plan."
            l "Admittedly, I don't know how July 17th was chosen, but..."
            l "If it was randomly, I got lucky that it wasn't Freddy's birthday."
            l "Then I'd be stuck at two dates."
            show lauren ind:
                xcenter .5
                linear 0.15 xcenter .25
            show sid ind with moveinleft:
                xcenter .75
            i "So um, since you opened the safe..."
            i "Was there money inside?"
            i "And if so... can I have it? Since, well, you know..."
            l "..."
            b "Sid, you're being incredibly-{p=0.5}{nw}"
            l "Bert, it's fine, he's just thinking about his family."
            l "There wasn't money in there."
            l "The safe was pretty much how you guys found it, mostly empty."
            l "It almost makes me wonder if the Game Master robbed the bank to fund this whole operation..."
            i "Aw man..."
            show sid mad:
                xcenter .75
            i "Screw you Game Master! Taking my money!"
            bi "It's not your money..."
            l "Well, the money might have never been there in the first place."
            show sid ind:
                xcenter .75
            i "Never there?..."
            i "So I've been trying to crack this safe for days for nothing..."
            hide sid with moveoutleft
            show lauren ind:
                xcenter .25
                linear 0.15 xcenter .5
            bi "Sid slinked into the corner."
            bi "It's like the mention of money made him forget he was accused of murder just a few minutes ago."
            bi "Maybe it's for the better if he doesn't interrupt again..."

        "Why Sam?" if len(menuset) >= 2:
            l "Well, it has to do with the \"secret of the game.\""
            b "Oh... I guess you're still the only one who knows it."
            l "Don't worry, it's... not really {i}the{/i}secret, just {i}a{/i} secret."
            l "{i}The Game Master's last name starts with an S{/i}."
            bi "Before I fully processed that..."
            show lauren ind:
                xcenter .5
                linear 0.15 xcenter .25
            show sid mad with moveinleft:
                xcenter .75
            i "What did you say?!"
            i "You're accusing me!"
            bi "Ah. His last name is Straits."
            l "Sid, relax, if I thought it was you I'd have shot you instead."
            i "How do I know you're not just trying to throw me under the bus?"
            i "Maybe the secret is something else and you're just spiting me with your dying breath!"
            i "What kind of lame secret is that anyway?"
            i "The Game Master's last name starts with an S?"
            i "You might as well have said \"The Game Master is Sid Straits, the dumb teenager who no one listens to!\""
            l "Sid, just listen..."
            l "In Korea, the family name comes first."
            b "Right. In Korea my legal name would be Kim Bert, not Bert Kim."
            l "And Sam is also Korean. So Sam's legal name in Korea would be Lee Sam."
            show sid ind with moveinleft:
                xcenter .75
            i "...So according to the secret, Sam could also be the Game Master."
            l "Yeah. I figured the Game Master wouldn't make it so obvious, and well..."
            l "I tried to come up with a way to twist the words, and that's what I came up with."
            l "It was never going to be you, Sid."
            l "I... even if I thought it was you..."
            l "I couldn't bring myself to kill another kid."
            i
            i "Well, we better find out that Sam is the Game Master, or else-{p=0.5}{nw}"
            show braindeath
            pause .25
            hide lauren
            show doom
            hide braindeath with dissolve
            i "..."
            b "..."
            b "Lauren died, which means..."
            b "Sam wasn't the Game Master."
            bi "And that means..."
            i "Bert, it's not me, I swear!"
            i "Lauren must have been lying, or Jenny or Freddy are lying, or..."
            i "It's not me! It's not me!"
            bi "Lauren's gone, I..."
            bi "I want to rip my hair out and scream, but someone has to be the adult in the room."
            b "Sid, calm down."
            b "No one's going to try to kill you right now."
            b "We need to... tell Jenny what Lauren told us."
            b "So we're all on even ground."
            i "So she also thinks it's me!"
            b "Sid if you're the Game Master, it's suspicious if you don't let me tell her..."
            b "Since after all, if Jenny is the killer next round, it would help the Game Master if she doesn't know a lot."
            i "...Ugh, fine."
            i "But I get to have time to convince her it's not me."
            bi "Kind of hard for me to agree to, because if it's not Sid..."
            bi "Well, Jenny's either accusing a kid dressed in a frog costume, or me."
            bi "But that's not important right now."
            b "You can tell her whatever you want Sid."
            b "Now I'm going, who knows how much time we have..."
            scene black
            bi "I sprinted back to the lobby."
            bi "To be honest, it was for a somewhat selfish reason."
            bi "One I didn't let slip to Sid."
            bi "If Sid was the Game Master, and Jenny's the next murderer..."
            bi "I don't want Jenny to wake up wherever we went next and try to kill me."
            bi "Was I being truthful to Sid?"
            bi "Did I believe what I said to convince him to let me go to the lobby?"
            bi "Or I was just playing the game to the best of my ability?"
            bi "Manipulating a little kid to increase my chances of winning?"
            bi "Saying whatever I felt he needed to hear?"
            show bg banklobby with dissolve
            $ statusnt("Bank Lobby", "bert", ch=4, sun=2)
            $ showchibint("freddy", "jenny")
            bi "I was bit taller than Sid, so he was still catching up as I burst into the lobby."
            show jenny ind with dissolve
            j "Bert? Is everything okay?"
            b "Jenny!"
            b "Lauren's-"
            bi "I glanced at Freddy."
            b "Well... you know."
            j "Oh... so it wasn't Sam?"
            b "No. But more importantly, Lauren told us something about the safe."
            b "She said-{p=0.5}{/nw}"
            scene black
            pause 1.0
            bi "Damn you, Game Master."
            bi "Is this your way of toying with me?"
            bi "Is watching eight people die in front of me not enough?"
            bi "Depriving me of food, water, my family?"
            bi "Despite all the emotional damage this game had inevitably caused, I was still \"playing\" my hardest."
            bi "But as my body slowly fell unconscious, I could tell I was nearing my wit's end."
            bi "I was almost ready to surrender."
            bi "I could only wonder, if I woke up, would I have the energy to survive?"
            bi "Or would one simple mistake mean the end?"
            play music "audio/ominous.mp3" fadein 3.0
            show endch4 with Dissolve(3.0) #febreview
            pause
            stop music fadeout 3.0
            hide endch4 with Dissolve(3.0)
