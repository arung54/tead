label mansionGo:
    $ftecounter = 2
    scene black
    bi "..."
    bi "Two people died..."
    bi "And there's nothing I could do to save them..."
    show bg mansiondining with slowdissolve
    bi "I slowly came to my senses and looked to my left."
    show frog sad with dissolve
    $showchibi("freddy")
    f "nrg...."
    bi "...no, that's not how I should think about it."
    bi "There were ten people I did help save."
    bi "Well, nine excluding the mastermind."
    show frog ind
    f "Oh, Bert! Are you awake? Feeling okay?"
    bi "This kid's one of them."
    bi "And I have to keep saving them for as long as this goes."
    b "Yeah, I'm fine. Thanks for asking. How are you?"
    f "Eh, kinda sleepy like always."
    bi "For a kid he doesn't seem that shaken up about what just happened..."
    f "Wait, Bert?"
    f "I... I thought you were just someone in my dream."
    f "Does that mean..."
    show frog sad
    f "Dan... Kaiser..."
    bi "Oh no. He's audibly tearing up."
    bi "What do I do?"
    show frog sad:
        xcenter .5
        linear 0.15 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    $showchibi("freddy", "lauren")
    l "Hey Froggy, you doing okay?"
    l "You wanna look around and try to find food with me? Everyone's probably hungry after sleeping!"
    f "S-sure..."
    hide lauren with moveoutleft
    hide frog with moveoutright
    $showchibi()
    bi "Where did she come from?"
    bi "Oh, everyone else is here too, waking up like us."
    $showchibi("catherine", "dracula", "jenny", "sam", "shahar", "sid", "stella")
    show drac ind with dissolve
    d "I see Lauren and Freddy have already started exploring."
    b "Something like that. I think she's just trying to keep him from crying."
    d "Regardless, they have gone to a new area without consulting the rest of us."
    d "Seems somewhat rash."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .25
    show sam with moveinright:
        xcenter .75
    s "I agree with the vampire for once."
    s "Given the information Kaiser shared with us before his untimely end."
    s "It would be good to discuss that topic as a group."
    bi "..."
    bi "Silence followed, with no one sure how to proceed."
    s "Come on, we can talk about it. We're all criminals."
    s "There, I said it."
    s "Stella and I have already admitted to committing crimes, it's not like much has changed."
    d "Yes. It could be prudent to strategize around this information."
    hide sam with moveoutright
    show stella ind with moveinright:
        xcenter .75
    t "Strategize how exactly?"
    d "Maybe we could each admit what crimes we've committed and try to find a common link."
    d "For example, my crime was vampiric manslaughter."
    d "I think it's unfair to call my need for sustenance a crime, but I digress."
    t "Babe, you're just coming off as senile."
    t "The idea of admitting to our crimes would be much more enticing from a younger guy..."
    d "Hmph, fine. Even if we don't admit to our crime, maybe we should take precautions like mandatory travelling in pairs."
    t "Hell no!"
    show stella happy:
        xcenter .75
    t "You see the room we're in? This is a palace made for a queen like me."
    t "There's bound to be plenty of high-class booze, stuff you'd find in VIP lounges."
    bi "I hadn't fully processed it with all the confusion, but we were in what seemed to be a mansion."
    bi "Hopefully with real food and sleeping arrangements..."
    bi "Maybe a working stove to cook some meat?"
    t "I'm not going to let some old fart tell me I can't drink it because I need to watch over him."
    t "I worked hard my whole life to hire bodyguards, not to be one."
    hide drac with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "With all due respect, you're kind of derailing the conversation here."
    s "The point is we have information thanks to Kaiser, and we should use it to maximize our chance of escaping."
    s "The particulars don't really matter, though I do think admitting our crimes might help."
    bi "..."
    bi "I don't want to think about it again."
    bi "Don't want to relive that moment."
    t "Honey, as someone who has confessed crimes, is that really fair when the vampire and pirate are going to keep playing pretend?"
    hide sam with moveoutleft
    show shahar mad with moveinleft:
        xcenter .25
    h "What d'ye mean pretend? Ain't nothing pretend about me."
    t "Alright, if it means getting to see those abs I can agree that you're a pirate."
    show shahar ind:
        xcenter .25
    h "Aye, that's what I like to hear!"
    hide shahar with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I do have concerns about us all admitting to crimes."
    j "I know it will sound suspicious, but I think for some of us our crime is something very personal."
    j "One of those things that you have to keep bottled up or ignore for your own sanity."
    j "Like the awkward moment from middle school that ruins you when you think of it."
    bi "..."
    t "I agree with the chick. I'm sure some of you have fetishes you wouldn't admit to, what makes a crime so different?"
    t "That being said, are you sure you aren't just trying to get on Bert's good side?"
    bi "Suddenly, all eyes were either on me or Jenny."
    b "What?"
    j "Huh?"
    t "What? You're both young, cute, happy types."
    t "And it's obvious Bert doesn't want to talk about his crime, and you're saving him."
    show stella bigsmile:
        xcenter .75
    t "But hey, if you're not interested in Bert I'll take him."
    j "..."
    b "..."
    j "I'm just going to ignore what Stella said."
    hide stella with moveoutright
    show jenny ind:
        xcenter .25
        linear 0.15 xcenter .5
    j "Anyways, I think if we admit to our crimes it'll create more sadness and distrust than anything."
    j "Besides, look at the crimes we already know."
    j "Stella did some shady business deal, Sam dealt drugs, Bert's is something about driving."
    j "What common theme would those have that we could figure out?"
    bi "No one had a good answer to that."
    j "Exactly. So let's just keep trucking along like we have."
    bi "I looked briefly at Sam and Dracula."
    hide jenny with dissolve
    show sam:
        xcenter .25
    show drac ind:
        xcenter .75
    with dissolve
    s "..."
    d "..."
    bi "Looks like that's the end of that conversation."
    hide sam
    show drac ind:
        xcenter .75
        linear 0.15 xcenter .5
    d "Well, one more comment."
    d "It seems despite not being in a fast-moving train, escape is unlikely."
    d "The windows have been boarded closed with a thick metal sheet."
    d "Even if they were not there, the chips in our brains would likely kill us upon leaving the building."
    d "And given what happened to Kaiser, it would seem the chips are unlikely to be a hoax."
    d "That is all I wished to say. Would hate to see any more unnecessary deaths than we already have."
    hide drac with dissolve
    show sid ind with dissolve
    i "So um, are we free to go?"
    i "I... I've never been in a house this big."
    i "I was hoping we'd do what we did on the train and explore."
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .25
    show catherine happy with moveinright:
        xcenter .75
    c "Great idea Sid!"
    c "There's bound to be some new information here we can use."
    ses "Mrow!"
    c "Oh, true, and maybe mice to catch!"
    bi "I'm not sure if she actually thinks its a great idea, but..."
    bi "Sid is probably the most shaken up about Dan's death."
    b "Yeah, plus we have to figure out what there is to eat and where to sleep."
    bi "...and if nothing else, it's a chance for us all to forget about our fate for a bit."
    hide sid
    hide catherine
    with dissolve
    show jenny ind with dissolve
    bi "I approached Jenny and made sure Stella wasn't within earshot."
    b "Hey Jenny, want to explore together?"
    j "Oh?"
    b "I wanted to talk to you while we're looking around."
    show jenny happy
    j "Sure!"
    $ showchibi("jenny")
    bi "The others left as we talked."
    b "Guess no one wants to look around here?"
    show jenny ind
    j "Maybe they thought they saw everything."
    j "Which to be fair, there isn't much to see."
    j "A large dining table, some furniture..."
    j "There is an ominous portrait."
    bi "She pointed above the fireplace."
    bi "An old, ordinary-looking man dressed up quite nicely."
    b "Wait... who is that?"
    j "No clue."
    b "It must be someone relevant, right?"
    b "Unless the mastermind just took someone's mansion without a problem."
    b "But it seems like anyone rich enough to own this house wouldn't be so easily... overcome?"
    j "You might be onto something."
    j "Maybe it's the mastermind? And this is their mansion?"
    b "Well, that would contradict what the screen told us about one of us being the mastermind."
    b "But maybe we'd be naive to trust that."
    j "Unless someone's met this person before, I don't know if we'll get much information out of this."
    j "Let's look somewhere else. Looks like this room connects to the kitchen and a bedroom."
    b "Let's head to the kitchen, I'm hungry!"
    scene bg mansionkitchen with fade
    $showchibi("jenny", "freddy", "lauren")
    show lauren ind with dissolve
    l "Hey, what happened in the other room? Heard lots of chatter."
    b "Some people suggested we all admit to our crime. It wasn't received very well."
    b "Now everyone's off exploring."
    l "Ah okay. Well, good news, the kitchen is rather well-stocked."
    l "What you'd expect from a kitchen in a mansion."
    l "Plenty of fancy cutlery and cookware."
    l "Including a full knife set, which we might want to discuss..."
    l "All sorts of meats and veggies, the stove, fridge, and freezer all functioning, tap water..."
    hide lauren ind with dissolve
    show shahar happy with moveinright:
        xcenter .25
    show stella happy with moveinright:
        xcenter .75
    $showchibi("jenny", "freddy", "lauren", "shahar", "stella")
    h "I heard fridge and freezer. Is there rum fer the takin'?"
    t "If the mansion's owner has any class, there should be."
    hide shahar
    hide stella with dissolve
    show lauren ind
    l "..."
    l "Hey Freddy, Shahar and Stella want a chance to check out the kitchen, maybe let's not disturb them."
    b "We could just ask them to-"
    l "It's easier to just not bother, honestly."
    l "Freddy, wanna go claim a bed?"
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show frog ind with moveinleft:
        xcenter .25
    f "O-okay..."
    hide lauren
    hide freddy
    with dissolve
    $showchibi("jenny", "shahar", "stella")
    show shahar happy with moveinleft:
        xcenter .25
    show stella happy with moveinright:
        xcenter .75
    h "Rum, vodka, mead, they have ev'rything here!"
    t "Tequila shots! It's been so long. Bert, Jenny, want to join us?"
    hide shahar with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I'm... not old enough to drink yet."
    t "Who's gonna arrest you? The mastermind who's already broken twenty different laws?"
    t "Plus it'd be good for you and Bert to get to know each other with your inhibitions down."
    b "Alright, I think we've seen everything we need to see here."
    b "Jenny, let's go check out another room."
    t "A bedroom?"
    j "Yes please, get me out of here."
    scene black with fade
    scene bg mansionmaster with fade
    $showchibi("jenny", "dracula", "sam")
    b "The master bedroom?"
    show jenny ind with dissolve
    j "You... didn't actually intend to bring me to a bedroom right."
    b "What? No!"
    b "Besides, Sam and Dracula are here."
    hide jenny ind
    show sam:
        xcenter .25
    show drac ind:
        xcenter .75
    with dissolve
    d "Good of you to join us."
    d "Sam and I were just chatting. There's nothing particularly interesting here."
    d "Just a fancy bedroom, befitting for an old accomplished vampire."
    s "Subtle attempt to make an early claim on the nicest room."
    s "Sure you're not just saying that because your joints are giving out?"
    d "Hmph, make jokes if you must."
    d "But being a vampire means despite my age I am quite nimble."
    b "Before deciding who sleeps where, do we know what the other living arrangements are?"
    d "There are four bedrooms upstairs."
    b "So enough for everyone to sleep on a bed, if people are willing to share."
    d "Unfortunately, the above bedrooms only have beds that fit one."
    d "So as before, some of us will have to sleep elsewhere."
    d "Fortunately the couches in the living room seem rather comfy."
    b "Okay, I think in thirty minutes or so we should meet up and decide this."
    b "With a vote, rather than someone making an early claim."
    d "Hmph."
    d "Fine."
    b "Cool, make sure to mention it to anyone you bump into."
    b "By the way, can I ask what you were talking about?"
    d "..."
    s "..."
    d "We were discussing private affairs."
    d "You have secrets you're keeping about your crime, so surely you won't mind me keeping my own."
    s "Yeah, what the vampire said."
    b "Oh, yeah, of course..."
    d "And maybe you'd like to give us some privacy so we may continue speaking?"
    d "Continue going on your little adventure around the house, it'll be more fun than us."
    bi "I left, a little bit annoyed by the whole conversation."
    hide sam
    hide drac
    with dissolve
    show jenny ind with dissolve
    b "Let's move on?"
    j "Sounds good."
    scene black with fade
    scene bg mansiongarage with fade
    $showchibi( "jenny", "catherine", "sid")
    show catherine happy with dissolve
    c "Hey guys! Welcome to Catherine's garage emporium!"
    b "Catherine's garage emporium?"
    c "Just something I made up, haha."
    c "There's no car, otherwise we could make a sick getaway!"
    show catherine ind
    c "Well, you know, minus the whole chip in our head thing."
    c "Also the garage door doesn't open, though it's not surprising."
    show catherine happy
    c "In better news, there's some rope here Sesame can use as a scratching toy!"
    s "{i}Scrichhhh{/i}."
    c "He's having fun with it already!"
    b "Wow, maybe Sesame can scratch his way out of here for us!"
    c "What? Don't be silly."
    c "There's also some simple tools and supplies, like a drill, a hammer, a screwdriver, a stepstool, and some batteries."
    c "We could use these to repair anything that breaks maybe?"
    c "Not sure if anyone here's much of handyman though."
    show catherine happy:
        xcenter .5
        linear 0.15 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "I... I could repair things around here."
    i "We couldn't afford to hire people so my dad taught me how to do basic household repairs."
    c "That's nice of you to offer Sid!"
    c "But hopefully the need doesn't arise."
    c "There's also a clock and some boxes full of junk."
    c "According to the clock it's early afternoon right now."
    c "Hard to tell if that's right with the boarded windows though."
    c "There's also a light generator here, it seems like it's fully fueled."
    c "We have running power so we shouldn't need it, but it's nice to know that won't be an issue."
    show catherine ind
    c "I imagine whoever owns this house isn't paying the electricity bill."
    c "So unless the mastermind's doing us that favor..."
    b "Well, the lights were on in the dining room, and the fridge and freeze are running."
    b "So I don't think we'll need to worry about that."
    show catherine happy
    c "Oh, nice! Do you happen to know if the kitchen is well stocked?"
    c "I used to work as a chef in a kitchen, I could whip us up some nice meals."
    c "Don't have to be vegetarian meals, wouldn't want the meat to go to waste."
    b "That's very nice of you to offer!"
    i "Um... Catherine, if you're going to cook, I have an idea."
    c "Send it at me!"
    i "I... I've only lived in my parents' cramped apartment."
    i "Sustaining ourselves off budget meals."
    i "While we're here, before someone dies, I... thought it'd be nice if we had a fancy dinner party."
    c "Aww, Sid... that's such a cute idea!"
    c "Yes, let's do it!"
    c "Unfortunately I probably need at least a day to prepare, so it would have to be tomorrow evening."
    i "O-oh..."
    i "But... what if the kill happens before then?"
    c "I think that's just a chance we have to take."
    b "Oh, forgot to mention, there's a meeting soon to decide sleeping arrangements."
    b "Maybe at that meeting we can... kindly suggest the killer wait a day?"
    hide sid with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "That might be a hard sell."
    j "What if they're afraid it will become harder to kill people after the party?"
    c "This is a bit of a depressing topic."
    hide jenny with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    show jenny ind with moveinleft:
        xcenter .25
    show catherine happy:
        xcenter .75
    c "Sid, we'll have a dinner party tomorrow, you can count on it."
    i "Th-th-"
    show sid happy:
        xcenter .25
    i "Thanks Catherine. This is so exciting!"
    bi "I'm glad something good is coming out of this at least."
    hide jenny
    hide sid
    with dissolve
    show jenny ind
    b "Let's move on?"
    j "Sounds good, Catherine gave us a very good rundown of this room anyway."
    j "Seems like we've explored the entirety of this floor, let's go upstairs?"
    b "Sure."
    scene black with fade
    scene bg mansionhallway with fade
    $showchibi("jenny")
    show jenny ind
    j "Hey Bert, while we're alone..."
    j "Do the jokes everyone's making about us annoy you as much as they annoy me?"
    b "Yes. Hell yes."
    b "I don't get how people can be saying that kind of stuff while our lives are on the line."
    j "Okay, just wanted to make sure we were on the same page."
    b "I'll speak up next time it happens."
    b "..and you should join me in doing so, since I don't think they all take me seriously."
    b "Mostly Dracula, since I'm not admitting my crime."
    b "Even though he's still claiming to be a vampire..."
    j "Don't worry about him. He's just a senile old man."
    j "Thinks that when he's stuck here with a bunch of \"young\" people he's in charge."
    j "You don't need to tell anyone what your crime is, I wasn't just saying that to protect you."
    j "I think that applies to everyone."
    j "Even if someone sharing our crimes could help us..."
    j "I really do think revealing our crimes will just drive in unnecessary wedges."
    j "And it's not something everyone's ready to admit to strangers, even if they've accepted it as is."
    b "..."
    b "Can I tell you mine?"
    j "Oh?"
    b "What they said, maybe if you know it would help us get out."
    b "And... maybe if it's off my chest I won't have to think about it anymore while we're here."
    j "Only if you want to."
    j "I can tell you mine first, if you want."
    j "It's not that bad, if anything I'm a little proud of it."
    bi "..."
    bi "Jenny had been so bubbly and supportive this whole time."
    bi "It's hard to process that she could be a criminal too."
    b "Sure, we can trade secrets."
    j "Okay."
    j "To make money on the side in college I did some card counting trips with friends."
    j "Like you've seen in the movies, we'd go to casinos, some of us would find tables that were hot."
    j "Others would join those tables and play the winning odds as hard as we could."
    j "Card counting isn't technically illegal but..."
    j "The one time I got caught happened to be one of the more... shady casinos."
    j "One that used underhanded tactics to scare off card counters."
    j "So when they caught me, they made some nasty charges stick."
    j "I'm not old enough to gamble legally."
    j "I used a fake ID to get in."
    j "That alone's not a big crime."
    j "But they doctored some photos and footage and made it seem like I was drinking while driving while underage."
    j "I was lucky that my parents were able to bail me out, but it was horrifying."
    show jenny happy
    j "But like I said, ignoring how much trouble it caused everyone, I'm kinda proud."
    j "I'm a good enough gambler to make some scary, powerful businessmen scared."
    b "That is pretty impressive."
    j "Anyway, that's my crime."
    b "Guess it's my turn."
    show jenny ind
    j "Guess so. If you want to back out now that's-"
    b "No, we made a deal."
    b "Mine's much less... exciting?"
    b "Basically I was driving through the city after visiting a friend."
    b "This lady was walking on the sidewalk and suddenly turns into the road, without looking, nowhere near an intersection."
    b "The next light was green so I wasn't going that slow, and had barely any time to react."
    b "And... well, I ran into her."
    b "She died, and her family was rich and threatened to sue."
    b "Fortunately I had a dashcam with footage that convinced their lawyer it wasn't worth pressing charges."
    b "But it still haunted me... even if I was legally fine, should I have been driving slower?"
    b "If I was paying more attention would I have reacted sooner?"
    b "I... moved after that, not wanting to be near that city or that memory."
    b "Moved somewhere where I could take the train to work."
    b "Haven't driven since."
    j "..."
    j "I'm so sorry you went through that."
    j "Thank you for telling me. I won't tell anyone else."
    j "We don't have to talk about this more if you don't want to."
    b "Yeah, I'd appreciate that."
    b "..."
    j "..."
    b "We should look around more."
    b "There's a closet in this hallway, let's see what's inside."
    b "..."
    b "It won't open..."
    b "Last time there was a closet that was locked, it wasn't good news."
    j "Nothing we can do about it besides keep an eye on it though."
    b "Yeah, guess not."
    b "In that case, let's check out some of the bedrooms."
    b "We are about to have a meeting about them..."
    j "Sounds good."
    scene black with fade
    scene bg mansionbedroom with fade
    $showchibi("jenny", "freddy", "lauren")
    show lauren ind with dissolve
    l "Oh, hey guys."
    l "I thought bouncing on a bed might get Freddy's mind off things."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .25
    show frog ind with moveinbottom:
        xcenter .75
        ycenter .8
    show frog ind:
        xcenter .75
        ycenter .8
        linear .15 ycenter .2
    show frog ind:
        xcenter .75
        ycenter .2
        linear .15 ycenter .8
    show frog ind:
        xcenter .75
        ycenter .8
        linear .15 ycenter .2
    show frog ind:
        xcenter .75
        ycenter .2
        linear .15 ycenter .5
    f "It's fun!"
    l "It's probably not what he's used to in terms of fun but... it's something."
    l "Hey Freddy, how high do you think you can go?"
    b "By the way, we're meeting soon in the living room to discuss who gets to sleep where."
    b "We can bring you down with us when it's time to start."
    l "Got it."
    b "Do you mind if we look around here?"
    l "Sure, don't mind us."
    hide lauren
    hide jenny
    with dissolve
    show jenny ind with dissolve
    j "Huh. Looks like they weren't lying about having only small beds upstairs."
    b "Yeah, it's very weird for how luxurious the house is otherwise."
    b "The room isn't particularly well furnished either."
    b "Normally there'd be a dresser or something like that in here."
    j "Hm... maybe the mastermind is trying to minimize how many spots things can be hidden in?"
    j "After all, searching four fully furnished bedrooms sounds like a chore."
    b "That'd be awfully considerate for someone who, you know, wants most of us dead."
    j "That's true. But if they wanted us dead, why not just kill us instead of making us play this game?"
    b "I wish I knew."
    b "Not sure if it's worth dwelling on anyway, unless we think we can get to the right answer."
    j "If you say so."
    b "I'm assuming all the bedrooms upstairs look like this, so I think we just need to look at the bathroom."
    b "We're about to have that meeting anyway."
    j "Um... you mind checking that out without me?"
    b "Huh?"
    j "I... don't want Stella to see us walking in there together."
    b "That's... unfortunately very fair."
    j "I'll just keep Freddy and Lauren company, so no need to worry about shady business from me."
    b "Sounds good."
    bi "I headed to the bathroom by myself."
    scene black with fade
    scene bg mansionbr with fade
    b "So uh..."
    b "Guess this is the bathroom."
    bi "...who am I talking to?"
    bi "It's just me in here."
    bi "This is the nicest bathroom I've been in, I think."
    bi "Even some of the hotel bathrooms I've been in weren't quite this nice."
    bi "There's so much space, the largest bathroom mirror I've ever seen."
    bi "More drawers than I can even think of a use for..."
    bi "The knobs on the faucet and in the tub are gold-plated..."
    bi "...well, I guess I'm done admiring this bathroom."
    bi "I'll grab Jenny, Lauren, and Freddy and head downstairs, I guess."
    scene black with fade
    scene bg mansiondining with fade
    $showchibi("catherine", "dracula", "freddy", "jenny", "lauren", "sam", "shahar", "sid", "stella")
    show sam with dissolve
    s "So Bert, you called this meeting, right?"
    b "Yeah, mostly to discuss the sleeping arrangements, though Catherine might have an announcement too?"
    show sam:
        xcenter .5
        linear 0.15 xcenter .25
    show catherine happy with moveinright:
        xcenter .75
    c "Yessir! But I'll wait until you're done Bert."
    b "Alright. So there's four bedrooms upstairs, each with a twin bed, and then the master bedroom has a bigger bed."
    b "So six of us can sleep pretty easily."
    hide sam with moveoutleft
    show lauren ind with moveineftl:
        xcenter .25
    l "For what it's worth, Freddy can probably fit in a twin bed with someone, if both Freddy and that person don't mind."
    l "Freddy, that sound okay to you?"
    hide catherine with moveoutright
    show frog ind with moveinright:
        xcenter .75
    f "Yeah, okay with me!"
    f "Can Lauren be the person I share a bed with?"
    show lauren happy:
        xcenter .25
    l "Never thought you'd ask."
    bi "I could've guessed that..."
    b "Okay, so three of us need to stay somewhere that isn't a bedroom."
    b "And two people can probably share the master bedroom."
    hide frog with moveoutright
    show stella drunk with moveinright:
        xcenter .75
    t "Any young guys want to share the master bedroom with me?"
    t "I think we'd make the best use of it, if you catch my drift."
    t "Plus a house like this probably has soundproofing."
    l "Your libido isn't a valid reason to give you that room."
    t "Fine, the lovebirds should have it then?"
    l "Who?"
    b "You better not mean me and Jenny."
    b "Just because you're drunk doesn't mean it's any less callous to matchmake people in the middle of a life-or-death scenario."
    t "..."
    t "You're all such killjoys, I remember why I work long hours now."
    t "At least when I'm on the clock people have to respect my whims and fancies."
    t "Fine, if I can't have the master bedroom, I'll take the living room."
    t "I plan to stay up drinking, a couch to crash on is the perfect ending to that sort of night."
    b "I... okay, fine."
    b "I'll volunteer too, since I'm the one organizing this meeting."
    l "You sure you can handle Stella?"
    b "Can't be worse than anything I had to deal with in college."
    b "Okay, that leaves one more."
    b "Any volunteers?"
    hide stella
    hide lauren
    with dissolve
    show jenny ind with dissolve
    bi "I hoped Jenny would volunteer."
    bi "It seemed like we were closer now, it would be fun to talk to her more."
    bi "Just as I thought she was opening her mouth..."
    hide jenny
    show shahar ind
    h "Arr, I'll do it!"
    h "Stella's got a point, the living room's right next to the kitchen and the kitchen has drinks!"
    bi "...guess I'm sleeping with the drunkards."
    show shahar happy:
        xcenter .5
        linear .15 xcenter .75
    show stella drunk with moveinleft:
        xcenter .25
    t "Sleeping with two cute drunk boys? Hell yes, who needs a master bedroom?"
    b "{i}Two{/i} drunk boys?"
    t "You think we're gonna let you get away without drinking with us?"
    bi "...hopefully one of the couches will only fit me."
    b "Anyway, we also need to decide who goes in the master bedroom."
    hide stella
    hide shahar
    with dissolve
    show catherine happy
    c "Oh, I had an idea about that!"
    c "Sid, you seemed really excited to be in a nice house."
    show catherine happy:
        xcenter .5
        linear .15 xcenter .25
    show sid ind with moveinright:
        xcenter .75
    i "Oh... yeah, my family isn't that well off so... this is the nicest building I've ever been in."
    c "I say we give Sid a treat and let him take the master bedroom!"
    c "He should get to know what a bougie life is like."
    b "That's a really kind idea, Catherine."
    show sid happy:
        xcenter .75
    i "You... you're all okay with that?"
    hide catherine with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "Wait, are we really going to trust what Sid says at face value?"
    s "He could just be lying about being poor so we're nicer to him."
    show sid ind:
        xcenter .75
    i "Wh-why would I lie?"
    s "You do remember the part where we're all criminals, right?"
    s "Everyone here has a reason to lie."
    i "..."
    hide sid with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "Sam, do you have a better suggestion?"
    s "Yeah, I was-"
    c "That doesn't involve you getting the master bedroom."
    s "..."
    bi "Catherine got closer to Sam and whispered, just barely loud enough for me to hear."
    c "Do we need to bring up the fact that Sid got close to Dan before he died?"
    s "No..."
    hide sam with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    c "Room's all yours Sid."
    c "Well, yours and one other person's."
    show sid happy:
        xcenter .25
    i "Thanks Catherine!"
    i "Uh... Dracula, do you want to share the room with me?"
    i "If that's okay with everyone else."
    hide catherine with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "I'm not opposed, but do you mind explaining why me?"
    i "Well, I don't like Sam so that's not an option."
    i "Also, I don't think I can ask a girl to share a room with me."
    i "And then Shahar and Bert are already sleeping in the living room."
    i "So you're pretty much the only option I have."
    bi "Well, I wouldn't mind switching..."
    bi "Not that anyone would be down to take my spot."
    d "Reasonable enough for me."
    b "Alright, so Sam, Jenny, and Catherine get their own rooms upstairs."
    hide drac
    hide sid
    with dissolve
    show catherine happy with dissolve
    c "My own room? Don't forget Sesame!"
    ses "Sssss."
    b "Right, Catherine and Sesame get a room."
    b "Guess we've figured that out. Catherine, do you want to tell them about your announcement?"
    c "Yes!"
    c "So I was thinking tomorrow evening we could have a dinner party!"
    c "It would be a shame to not make good use of all the food in the kitchen."
    c "Plus I'm sure we could all use a mood lifter."
    c "I can do most of the cooking, but if anyone has anything to contribute they can feel free!"
    show catherine happy:
        xcenter .5
        linear .15 xcenter .75
    show stella drunk with moveinleft:
        xcenter .25
    t "Is drinking allowed at this party?"
    show catherine ind:
        xcenter .75
    c "...I guess so, it is a party."
    hide catherine with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    l "Don't overdo it."
    t "Girly, I've never drank too much in my life."
    t "I have a liver of iron."
    l "...Please just don't overdo it."
    l "There are still children here."
    t "I'm sure Freddy's parents have gotten drunk around him before."
    l "That doesn't make it any more okay for you to do it."
    l "As is I'm not very okay with you and Shahar forcing Bert to deal with your debauchery."
    hide stella with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "In her defense, the point of the party is to lift our moods, right?"
    s "A little bit of drinking isn't going to do any damage."
    s "I might drink a bit myself."
    l "...Are you even old enough to drink?"
    s "Again, did you forget the part where we're all criminals?"
    l "...Fine."
    s "So, that concludes the meeting, right?"
    b "I guess so."
    b "Uh... yeah, everyone's free to go."
    hide lauren
    hide sam
    with dissolve
    show drac ind with dissolve
    d "If I may, while everyone's here."
    d "Earlier, we had discussed sharing our crimes and there were some negative reactions."
    d "Chances are even if people did share, they might lie about it."
    d "But to build trust and provide us with information, I still think it would be prudent to share."
    d "Maybe not with the whole group, but in private with someone you trust."
    d "Sam and I have already done this, it would be nice to see others follow our initiative."
    bi "Is that what they were discussing earlier?"
    d "Some close pairs seem to have already formed anyway."
    bi "...that is true."
    bi "Lauren and Freddy are definitely very close now."
    bi "And... there's me and Jenny, though I don't know how close we are."
    bi "I guess everyone is desperate for someone they can trust in an environment like this."
    bi "Even if that person could be the mastermind, even the illusion of trust is very comforting."
    d "I will not bother trying to enforce this request, since I do not expect everyone to be fully cooperative."
    d "That is all."
    hide drac with dissolve
    show shahar ind with dissolve
    h "Is that all the business yer gonna jabber about?"
    h "On the sea we don't have meetings, we just sail with the flow."
    h "I fell asleep fer most of that discussion to be honest."
    b "...you fell asleep?"
    h "Aye! If I can sleep on a stormy sea I can sleep through anything."
    h "Plus, I'm loaded with rum and whiskey."
    bi "...I hope that doesn't stop him from sleeping tonight."
    b "Yeah, if no one else has anything to bring up everyone can go."
    hide shahar with dissolve
    bi "Everyone except Catherine and Freddy slowly left."
    $showchibi("catherine", "freddy")
    show frog ind with dissolve:
        xcenter .25
    show catherine happy with dissolve:
        xcenter .75
    f "Uh... Catherine? Can I play with Sesame again?"
    c "Sure!"
    c "In fact, do you mind taking care of Sesame while I check out the kitchen?"
    c "Sesame will eat pretty much anything left out, and there's... stuff in there cats shouldn't eat or drink."
    f "Yeah!"
    bi "Catherine turned and whispered to me."
    c "Alcohol can kill cats in small doses, and I expect Shahar and Stella might have left an open bottle around."
    bi "With that dark comment, she went to the kitchen."
    hide catherine with dissolve
    $showchibi("freddy")
    bi "Seems like there's still some time before we're going to sleep."
    bi "Guess I should find someone to talk to."
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    tut "Since you are now playing as Bert, the number of times you've talked to each participant has been reset."
    #FT2 to be inserted here.
label postFT2:
    $ftecounter = 3
    scene bg mansiondining with fade
    $showchibi("catherine", "dracula", "freddy", "shahar", "sid", "stella")
    bi "Well, guess it's time to sleep."
    bi "Or at least, try to."
    show frog happy with dissolve:
        xcenter .25
    show catherine happy with dissolve:
        xcenter .75
    c "Sorry Freddy, I think I'm gonna take Sesame up to bed now."
    show frog ind:
        xcenter .25
    f "Oh, okay..."
    c "You can play tomorrow though! And if you fall asleep quickly then tomorrow will be here soon!"
    f "Y-yeah, let's go upstairs."
    hide frog
    hide catherine
    with dissolve
    $showchibi("dracula", "shahar", "sid", "stella")
    show drac ind with dissolve
    d "We are also off to sleep."
    d "I trust that you three will not be too loud enough to bother us?"
    b "Uh..."
    d "I'll take that as a yes. And if not, Bert, you will be held personally responsible."
    b "What?"
    d "Anyway, good night."
    hide drac with dissolve
    $showchibi("shahar", "stella")
    show shahar ind with dissolve:
        xcenter .25
    show stella drunk with dissolve:
        xcenter .75
    h "Well lad, looks like it's just you, me, the lady, and the rum!"
    t "And duh vodka, tequila, and all duh other drinks."
    b "...how much have you guys had to drink already?"
    h "Oh, just-ish one shot lad."
    b "Oh, that's not that-"
    h "One shot every 15 minutes each."
    b "...and it's been roughly two hours."
    t "Math's for duh losers, not for me."
    t "Bert, you're gonna get drunk with us, right?"
    b "I was hoping to sleep soon given, you know, we might need to solve another murder case sometime soon."
    t "Come on, haven't you heard duh saying?"
    t "All work and no play makes Bert a dull-uh boy."
    h "Yeah, lad, surely y've some stress pent up in ye."
    h "Stress ye can release through the joys of alcohol!"
    b "No, we really should sleep."
    h "You can sleep when yer in Davy Jones' Locker!"
    t "If you really want to sleep, you can sneak into bed with one of duh girls upstairs..."
    t "Just don't squish the cat if you get in bed with Catherine."
    b "Why are you so obsessed with... me and romance right now."
    t "Romance is a cute for word...wait, no, that's wrong... word for it."
    b "I'm just saying, you talk a lot about me and girls but never yourself and guys."
    t "Do you want to hear about my love life?"
    b "Uh..."
    b "I guess more than I want to hear about you trying to matchmake me."
    t "Alright, but if you fall asleep we're slapping you awake."
    hide shahar with moveoutleft
    show stella drunk:
        xcenter .75
        linear .15 xcenter .5
    t "My job involves a lot of travel."
    t "Not to mention, with the stress of duh job I spend pretty much all my free time drinking."
    t "Which means I can't really keep a steady boyfriend."
    t "Or even meet a guy while sober."
    t "The number of guys I've met {i}drunk{i/} though."
    t "Oh, it helps that I'm a rich businesswoman too."
    t "Lots of guys love to be treated for once."
    t "And they're more likely to follow you to your hotel room when your hotel room is duh presidential suite."
    b "You... don't ever want to settle down?"
    t "Eh... not really. Life's so much easier and fun this way."
    t "Maybe one day if I retire."
    b "Retire? That could be so far away!"
    t "Nah, I could probably retire now if I wanted."
    t "I have millions saved up, I could live off duh interest."
    b "Millions? You're only a few years older than me..."
    t "Sorry kid, life is unfair. You should've figured that out when one percent of people own 40 percent of duh wealth."
    b "So why don't you retire now?"
    t "What is this, an interrogation? Did someone commit duh murder while we were drinking?"
    b "Sorry, just trying to make conversation."
    t "Fine. Thing is, kid, retired life's boring if you don't have a passion."
    bi "I don't really like that she keeps calling me kid..."
    t "Right now, my only passion is ruthless business."
    t "It's a sinister passion but it's the only thing I'm good at."
    t "Well, that and holding my liquor."
    t "And wrapping cute young guys around my thumb."
    t "But my body can only take so much alcohol and so many cute guys."
    t "So not like I can make a retired life out of those."
    b "Didn't you have hobbies as a kid?"
    t "My hobby was investing."
    t "...and cute guys, even in high school."
    t "I joined some school clubs but quit them when I realized I could use duh time moving stocks before duh market closed."
    t "They were honestly such a waste of time."
    bi "She took a big swig after that."
    b "Hey, can I ask..."
    b "Why are you two drinking so much?"
    b "Are you not scared about our current circumstances?"
    t "Bert, honestly, tell me."
    t "Is there anything you've done today you feel like has been useful?"
    b "Well, I figured out our sleeping situation."
    b "Explored around the mansion."
    t "Jeez, you're so vanilla."
    b "...What does that mean?"
    t "Were those things really that useful?"
    t "Did they get us any closer to getting out of here?"
    b "I... no, but."
    t "If you hadn't stepped up we would've figured out where to sleep eventually."
    t "And exploring the mansion is the bare minimum you can do."
    t "It's like saying you took a shit today."
    b "..."
    t "I'm not trying to be harsh on you, kid."
    t "You didn't do anything useful because there's very little useful to do."
    t "Someone already has been assigned to murder, someone's going to have to be their victim."
    t "It's not like we're investing, nothing you do will save them."
    t "If that's the case, why not relax?"
    b "Isn't that too fatalistic?"
    t "That's being realistic."
    t "Take it from someone who works 16 hour days."
    t "Sometimes, there's nothing you can do about a shitty thing."
    t "And so duh best thing you can do is whatever has you most ready to deal with duh fallout of duh shitty thing."
    t "And for a gal like me with a robust liver, drinking to relax is that thing."
    b "I... kind of followed until the last part."
    t "Just drink more, then you'll understand."
    show stella drunk:
        xcenter .5
        xcenter .75
    show shahar ind with moveinleft:
        xcenter .25
    t "Speaking of drinking more, Shahar, are you alright?"
    t "Can I get you a shot of something? You've been awfully quiet."
    h "Ay, was I? I kind of dozed off."
    t "Oh c'mon, you're not gonna let this little lady out-drink a buff man like you, are ya?"
    h "No, of course not! Just needed to find a second wind."
    t "I thought you needed to find one a while ago."
    t "Don't pirates drink a lot? This feels very uncharacteristic for one."
    h "Aye, I just... haven't been out to sea in a while."
    b "Oh? Why's that?"
    h "I'd rather not talk about it laddy, you don't ask a man why he hasn't had a lover in a while."
    h "And the sea is my love."
    b "That... sounds more like taking a break from a relationship than not having a lover."
    show shahar mad:
        xcenter .25
    h "Lad, what'd I tell ya, don't ask!"
    t "Ooh, duh boys are about to fight!"
    t "Catfight! Catfight! Catfight!"
    b "What? No! I don't want to fight!"
    b "Sorry, I won't say anything else about it."
    show shahar ind:
        xcenter .25
    h "Look laddy, maybe I'm getting old."
    h "Pirate life, it's long hours, good pay but asks a lot of ye."
    h "What little time you're not working you're drinking, does a toll on yer body."
    t "I'll drink to that."
    h "And the time you are working, yer putting yer whole body into it."
    b "Why'd you get into the pirate life then?"
    h "I don't remember much lad, far back as my memory goes I've been a pirate."
    h "I vaguely recall something about getting into trouble with the law and losing another job."
    h "And well, being a pirate, ye don't really care much about the law."
    h "But I don't remember how er why I got in legal trouble to begin with."
    t "Hey, maybe you were a businessman in your past life."
    t "I've gotten in plenty of legal trouble myself."
    t "Granted, when you're rich enough legal trouble is just financial trouble."
    h "Aye, I don't think a rich Shahar would choose to become a pirate."
    h "He'd probably retire and enjoy life on a yacht, or some other fancy ship."
    h "Sipping cocktails, enjoying a more intimate relation with the sea."
    h "Reading a good book, since I ne'er had time to."
    h "I bet a yacht sails much more smoothly than a wooden ship!"
    h "I get motion sickness reading on vehicles."
    b "...but you're a pirate."
    h "I only said I get motion sickness while reading, lad!"
    h "Do you think a pirate's life is being out on the sea readin' poetry?"
    b "Yeah but..."
    b "Never mind."
    bi "Not worth getting into an argument over this."
    t "Speaking of a pirate's life, don't pirates own a lot of jewelry?"
    t "Shahar I feel like you're rather... bare."
    t "Not that anyone minds."
    h "Ay, you're right about that."
    h "I do own a chestful of booty!"
    h "But booty's inconvenient to carry round."
    t "Ooh yeah, fat booty makes walking hard."
    b "I... don't think that's what he meant."
    t "Oh trust me hun, I get it."
    h "Regardless, even if I wanted to show up studded, we had nary a chance to prepare for this game!"
    t "Ooh don't worry, you're enough of a stud as is."
    h "Oh, I wonder if this mansion's got anything we can plunder?"
    b "...you want to steal something to bring with you when you get out?"
    h "Aye! Least we can do to pass the time."
    b "Again, we could pass the time while sleeping."
    t "I don't know if I can approve of stealing from duh rich given... well, you know."
    h "Aye lass, it's not like I'm pillaging your village!"
    t "Hmm, that is true."
    t "Duh guy who owns this place might be my business enemy for all we know."
    t "Alright, let's steal something!"
    t "Woo!"
    hide stella with moveoutright
    blank "Thud."
    bi "...Stella took two steps and fell over."
    show stella drunk with moveinbottom:
        xcenter .75
    t "I'm alright."
    b "I... really don't think you are."
    t "What duh hell do you know?"
    t "You probably haven't had more than two shots in your life."
    b "...sigh."
    t "C'mon, let's go steal something!"
    h "Aye, a good pirate mission!"
    b "If I join will you let me sleep after this?"
    h "Fine with me lad."
    t "Fine, buzzkill. Have it your way."
    b "So uh... what exactly are we stealing?"
    h "It oughta be something small. Gotta be able to keep it in my pocket for the rest of our time here."
    t "It should be shiny too! I love shiny!"
    b "What about something from the upstairs bathroom?"
    b "It has a lot of gold things, like the sink knobs."
    b "That would probably fit in your pocket?"
    bi "It would also probably take a lot of effort to unscrew one."
    bi "Maybe enough that it will tire them out?"
    h "Aye lad, you're finally contributing something useful!"
    bi "I mean... not like I helped us all avoid dying in the train by solving the murder or anything."
    t "Let's gooooooo!"
    hide stella with moveoutright
    bi "Stella was off before we could even get started."
    bi "Dracula's probably not going to be very happy about our noise level after this..."
    scene black with fade
    scene bg mansionhallway with fade
    $showchibi("shahar", "stella")
    show stella drunk:
        xcenter .75
    show shahar ind:
        xcenter .25
    with dissolve
    b "Be quiet, we don't want to wake up anyone sleeping."
    h "Plundering isn't about being quiet! CHAAAAAARGE!"
    t "Yay, stealing from duh rich! This must be what Robin Hood felt like."
    hide shahar
    hide stella
    with moveoutright
    $showchibi()
    $showchibi("sam")
    show sam with dissolve
    s "Didn't expect the noise out here to be you."
    b "Sorry, you probably heard Shahar yelling... they're not letting me sleep and are a bit hard to control."
    s "Think you can keep them quieter? Some of us are trying to sleep."
    b "Yeah, I'll try..."
    s "Whatever. Good night."
    hide sam with dissolve
    $showchibi()
    bi "You know, I could just go to sleep now."
    bi "But I get the feeling Stella will force me awake if I try."
    b "Sigh."
    b "Okay, to the bathroom we go."
    scene black with fade
    scene bg mansionbr with fade
    $showchibi("shahar", "stella")
    show stella drunk:
        xcenter .75
    show shahar ind:
        xcenter .25
    with dissolve
    h "Ay lad, what took ye so long!"
    b "We should really be quieter, there are people sleeping on the other side of these walls."
    t "Psh, I've fell asleep in duh corners of clubs, they can sleep through a little tomfoolery."
    b "That... doesn't sound like the safest idea, sleeping in a club."
    b "And you know someone on the other side of the walls might be trying to kill us?"
    b "Probably shouldn't give them a reason."
    t "Damn, you really are a killjoy."
    t "Maybe I'll start calling you that."
    t "Well Killjoy, do you have any idea how to steal this sink knob?"
    t "We pulled on it real hard but no luck."
    b "Did you check under the sink?"
    h "Like... in the cabinet under it?"
    b "Yeah. In a fancy house like this, the nuts and bolts of the sink are in the cabinet."
    b "It looks nicer but still lets a plumber work on the sink."
    b "...aren't you rich Stella? Why didn't you think of this?"
    t "I'm drunk, Killjoy."
    t "I'm not here for thinking, I'm here for doing."
    t "If you know what I mean."
    b "You... don't need to keep saying that."
    t "Well, it wouldn't be very ladylike of me to bend down and try to look down there."
    t "Killjoy, you mind doing it?"
    h "Why not Shahar?"
    t "I don't think his muscles will fit in the cabinet."
    bi "Hm... if I lie about it, maybe they'll give up."
    b "Okay, going in."
    b "..."
    b "Hm, I don't see any way to detach the handles from the sink down here."
    bi "That was a lie. There were some bolts holding the handles in place."
    h "By Davy Jones... this plundering mission might be over lads."
    h "Oh well, it was a noble effort! Let's go sleep."
    t "Ugh, fine. I'm starting to come down anyway."
    bi "Finally..."
    scene black with fade
    bi "With that, we headed downstairs and finally went to sleep."
    pause 1
    blank "The next morning..."
    scene bg mansiondining
    bi "..."
    bi "What time is it?"
    $showchibi("shahar", "stella")
    bi "Those two are still asleep."
    $showchibi("shahar", "stella", "catherine")
    show catherine happy with dissolve
    c "Oh, morning Bert!"
    b "How... how early is it?"
    c "I haven't checked the clock in the garage but I think most of us got eight hours of sleep."
    c "You probably had less, I heard about your adventures last night from Sam on the way down."
    b "Oh... yeah, that'd explain why I'm so tired."
    b "What are you doing so early?"
    c "I'm getting ready for the party tonight!"
    c "Going to be cooking all day pretty much, we have a feast planned."
    c "Freddy offered to \"take care\" of Sesame today, which is great since I don't want his fur or anything getting in the food."
    c "Plus there's some stuff in the kitchen he shouldn't eat..."
    b "Wait, besides alcohol?"
    c "Yeah, raw meat can contain bacteria that can kill cats."
    c "There's some other stuff that's not lethal but a little bit risky, like yeast and chocolate."
    b "Well, at least Freddy will be distracted for a bit."
    c "Yeah! Anyway, I should go get started. Have a good day Bert!"
    b "Thanks Catherine, let us know if we can help with cooking."
    c "Will do!"
    hide catherine with dissolve
    $showchibi("shahar", "stella")
    $showchibi("shahar", "stella", "dracula")
    show drac ind with dissolve
    d "Good morning, Bert."
    b "Morning."
    d "I must say, it was quite loud last night."
    b "Sorry, I can't really do much to control the drunkards."
    b "I did try to at least get them to sleep as early as I could..."
    d "Not your fault if you tried I guess."
    d "Well, that is all I wished to say. I am returning to my room to think."
    d "If you wish to talk, I will be in there, although we should perhaps wait until Sid is awake."
    b "Okay, have a good day."
    hide drac with dissolve
    $showchibi("shahar", "stella")
    bi "...he's so weird."
    bi "It feels like I'm talking to a robot, not a vampire."
    bi "Oh well, I should find some way to kill time."
    bi "Maybe I'll go upstairs and see who there is to talk to."
    bi "Wouldn't want to distract Shahar and Stella's beauty sleep..."
    scene black with fade
    scene bg mansionhallway with fade
    $showchibi("jenny", "sam")
    show jenny ind:
        xcenter .25
    show sam:
        xcenter .75
    with dissolve
    j "Oh, Bert."
    j "Good morning! Sam and I were just about to head downstairs and help out Catherine."
    b "Oh, you're both cooks?"
    j "Not as experienced as Catherine, but I like being helpful!"
    s "I'm gonna make some dessert."
    s "Some of my customers prefer to receive their product in brownies or other baked goods, so I got pretty good at baking."
    s "There's not exactly much else to do until the party tonight."
    b "Well, unless you want to get super drunk like Stella and Shahar did."
    s "Eh, day drinking's not really my thing."
    j "Oh yeah, how was last night?"
    j "I heard some noise."
    b "They uh... tried to steal the sink knob from the bathroom."
    j "...Why?"
    b "Drunken boredom, I guess?"
    b "Anyway, it wasn't too bad."
    b "Once that failed they let me go to sleep, though I'm pretty tired now from having stayed up."
    s "We really shouldn't be enabling their shenanigans."
    b "I wouldn't say we're enabling them as much as tolerating it..."
    b "Besides, I tried to talk them out of it and they seemed pretty set in their ways."
    b "Lauren tried yesterday as well."
    s "I guess so."
    s "Anyway, Jenny, shall we head down?"
    j "Sure! Have a good day Bert, feel free to stop by the kitchen if you're bored!"
    hide jenny
    hide sam
    with dissolve
    $showchibi()
    bi "Hm... while no one else is around and it doesn't look suspicious."
    pause 1
    bi "Nope, closet is still locked."
    bi "Well, I guess I have some time to kill before the party. Everyone's probably awake by now, maybe I can find someone to talk to?"
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    #FT3
label postFT3:
    $ftecounter = 4
    scene bg mansiondining with fade
    $showchibi("shahar", "stella")
    bi "Well, I still have a tiny amount of time to kill before the party."
    $showchibi("shahar", "stella", "lauren")
    show lauren ind with dissolve
    l "Hey, Bert, are you busy right now?"
    b "Uh... I guess not."
    l "Do you mind watching over Freddy, and I guess Sesame?"
    l "I've been with them all day and was hoping to take a shower while I could..."
    b "Yeah, I don't mind."
    l "Cool, thanks. They both should still be in our bedroom right now."
    l "Sorry, the only other people I'd trust are Catherine and Jenny and they're both working on the party right now."
    scene black with fade
    scene bg mansionbedroom with fade
    $showchibi("freddy")
    show frog ind with dissolve
    f "Oh, hey."
    f "Are you here to hang out with me?"
    b "Yeah, Lauren had some stuff she wanted to do."
    f "Oh, cool!"
    b "N-not that I wouldn't want to hang out with you normally."
    f "Huh?"
    b "Never mind."
    b "So uh..."
    bi "I'm still not great at making conversation with the kid..."
    bi "Maybe I can ask him for some information that's useful?"
    bi "Feel like we haven't really talked to him meaningfully yet."
    bi "Sesame is keeping him occupied, so I can think this through."
    bi "What kind of crime would a kid have done?"
    b "Hey Freddy, what hobbies do you have?"
    f "Uh... I really like frogs!"
    f "I spend a lot of time just watching videos about then and learning new frog facts."
    b "Are you in any clubs at school?"
    f "Clubs?"
    b "Yeah, like, things you do with other students for fun."
    f "Oh, I'm homeschooled."
    f "My parents pay for a guy to come to our place and teach me."
    f "They say it's so I get a better education."
    f "I think it's really because my dad got upset when I went to school with other kids."
    b "What happened?"
    f "We had a homework assignment where we had to talk about what our parents did."
    show frog sad
    f "I tried asking my dad to help and he said it was too hard to explain."
    f "So I uh, didn't turn in the homework."
    f "The teacher got angry during class and then a bunch of the kids started asking me about it at lunch."
    f "My dad wasn't happy people were bullying me so he pulled me out of that school."
    b "That's... huh. {i}Do{/i} you know what your dad does?"
    f "Nah, after that day I felt like it was better not to ask."
    f "I just know he's not around a lot and is angry all the time."
    b "Do you get to meet other kids still?"
    f "Not really, no."
    f "When I go out my mom says I should wear this hoodie and mask so that the kids from my old school don't recognize me and bully me."
    f "I don't mind because I feel like a frog when I'm in it!"
    b "That... isn't that lonely, Freddy?"
    show frog ind
    f "Maybe? It's okay though! My mom loves me a lot."
    f "And if I behave my dad gets me whatever I want!"
    b "Well, as long as you're happy..."
    bi "That sounds like a really sad existence."
    bi "I do have to wonder though... is Freddy really a criminal?"
    bi "Maybe he's lying, but if he's stuck at home what crimes could he really do?"
    b "Freddy, do you use the computer at home often?"
    f "Yeah! That's how I learned so much about frogs!"
    b "Do you do anything else on the computer?"
    f "Uh, I play games and watch other videos sometimes."
    f "I think that's what most kids do on the computer these days."
    b "Yeah, makes sense."
    f "Bert, can I ask why you're asking me all of this?"
    b "Oh uh, just trying to make small talk."
    bi "...and understand why a kid is in a group of criminals."
    bi "Maybe it's a mistake?"
    bi "Or maybe it's some very petty crime."
    bi "I don't really feel like I'm a criminal as much as someone who happened to be in the wrong place."
    bi "Maybe that's the case for Freddy too?"
    $showchibi("freddy", "lauren")
    show frog ind:
        xcenter .5
        linear 0.15 xcenter .25
    show lauren ind with moveinright:
        xcenter .75
    l "And I'm back."
    l "How are you two doing?"
    b "Oh, good, we were just making small talk."
    l "The party's about to start. We should head down if we want to eat while the food is hot."
    f "Sesame, let's go!"
    l "Oh, Sesame can't come."
    show frog sad:
        xcenter .25
    f "Wh...why?"
    l "There's gonna be a lot of stuff Sesame can't eat or drink at the party."
    f "Can't Catherine hold onto him?"
    l "She's hosting the party, she'll probably be too busy worrying about the food."
    f "But... but I wanna play with Sesame."
    f "Can't I stay here?"
    l "Sorry Freddy, I think it's safest if you're with the group."
    l "Besides, you gotta eat dinner eventually."
    l "I'm sure you'll have a great time at the party."
    f "O-okay..."
    l "Let's head downstairs?"
    f "Yeah..."
    b "Oh boy, I can't wait to eat!"
    scene black with fade
    scene bg mansionhallway with fade
    bi "..."
    bi "Should I check the closet again?"
    bi "Nah, I'm probably just being paranoid. Besides, there's food waiting for me!"
    bi "Mmmm, I can smell it from here."
    b "Dinner, I'm on my way!"
    scene black with fade
    scene bg mansiondining with fade
    $showchibi("dracula", "freddy", "lauren", "shahar", "sid", "stella")
    show sid ind:
        xcenter .25
    show drac ind:
        xcenter .75
    with dissolve
    i "My first dinner party, I'm so excited!"
    d "Hopefully your first of many. I've hosted quite a few in my lair before."
    i "Your lair?"
    d "I guess what humans call a mansion."
    i "You have a mansion?"
    d "Being a vampire pays well, in its own way."
    d "Anyways, enjoy the party Sid. Well, as much as one can without drinking."
    i "Why can't I drink? Sam's underage and is going to drink."
    d "Yes, but you are quite young. You are free to do what you wish but drinking definitely gets riskier the younger you are."
    d "Not to mention, a scrawny kid such as yourself probably has tolerance more similar to a teenage girl."
    i "Who're you calling a girl?"
    d "I'm not calling you a girl, just drawing a comparison."
    i "Screw you old man!"
    bi "This can only go poorly... let me interrupt."
    b "Hey guys, has the food been served yet?"
    d "No, I believe the chefs are putting the finishing touches on it."
    b "Oh, cool. In that case I'll go see if they need any help."
    bi "Hopefully I defused that conversation..."
    scene black with fade
    scene bg mansionkitchen with fade
    $showchibi("catherine", "jenny", "sam")
    show jenny happy with dissolve
    j "Hey Bert! Whatcha up to?"
    b "Just came to see if I could help with finishing dinner."
    j "You just want to be the first to get served, don't you."
    b "...maybe."
    b "For real though, everything going smoothly here?"
    j "Mostly yeah."
    b "Mostly?"
    j "The display for the clocks on the stove and microwave aren't working anymore for some reason."
    j "So we've been using the clock from the garage to manually time everything."
    b "Huh, that's weird. Do you know why?"
    j "Honestly haven't thought to look into it, we've been busy with prepping food."
    j "Everything else is still working so it's fine."
    j "It's probably just be a maintenance issue, who knows how long it's been since someone lived in this house."
    b "Yeah, makes sense."
    j "Anyway, first course should be out soon."
    b "First course?"
    show jenny happy:
        xcenter .5
        linear 0.15 xcenter .75
    show catherine catless:
        xcenter .25
    with moveinleft
    c "Yeah! If we're fancy people eating a fancy dinner, we gotta serve everything in courses."
    b "Isn't that a lot of work for you? Don't you want to go out and socialize?"
    c "It's fine! If everyone else is enjoying themselves I'm happy."
    c "Plus I missed cooking, it's fun to be in the kitchen!"
    c "Plus I'll be able to party once everything besides dessert is done."
    b "Oh, who's making dessert?"
    hide jenny with moveinright
    show sam with moveinright:
        xcenter .75
    s "Me, I'll be out in the living room soon."
    b "What did you make?"
    s "I made an ice cream layer cake, was about all I could manage with the ingredients we had."
    b "Still sounds pretty fancy."
    s "Well, as much fun as baking is, drinking is a bit more fun."
    s "My cake's already in the freezer so I'm going to go out and mingle, I guess."
    hide sam with dissolve
    $showchibi("catherine", "jenny")
    show jenny happy with moveinright:
        xcenter .75
    c "Anyway, Bert, I think we're good to go here."
    c "You should feel free to go out and talk to the others!"
    c "The food will be out when it's out."
    j "You know what they say, a watched pot never boils!"
    b "That's just untrue."
    j "Most idioms are."
    b "Point taken. For real though, if you need help, let me know."
    j "Thanks Bert, now go out and party!"
    scene black with fade
    scene bg mansiondining with fade
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "stella")
    bi "Hm... I guess I have nothing to do besides mingle until food gets here."
    bi "Who should I talk to?"
    play sfx "audio/beep.mp3"
    show freetime with dissolve:
        ycenter .4
        linear 4 ycenter .5
    pause 2
    hide freetime with dissolve
    bi "I don't want to miss the food getting served, so I probably should stay in the dining room and kitchen."
    #FT4 to be inserted here.
label postFT4:
    scene bg mansiondining with fade
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "stella", "catherine")
    show catherine catless:
        xcenter .25
    show sid ind:
        xcenter .75
    c "First course is served! We have a charcuterie with various crackers, cheeses, meats, and some fruit to start!"
    i "Huh... is this what rich people eat?"
    c "Only part of it! At expensive restaurants you usually do multiple rounds of food, with the main part of the meal being in the second to last round."
    c "The idea is to avoid filling you up too early so you can enjoy a variety of dishes."
    i "Oh... ok. Sorry, I'm still new to this fancy dining thing."
    show sid smile:
        xcenter .75
    i "Thanks Catherine, this looks really good!"
    c "No worries! Anyway, gotta get back to the kitchen!"
    hide catherine with moveoutleft
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "stella")
    show sid smile:
        xcenter .75
        linear .15 xcenter .5
    i "Wow, there's so many types of food here already."
    i "This is only one course?"
    b "Yeah, though if you're anything like me you're gonna eat the equivalent of four meals."
    b "But uh, if you've got a small stomach probably best to pace yourself."
    i "Hm... that sounds like a challenge!"
    b "Uh, that's not what I..."
    bi "Before I could finish, Sid was already digging in."
    bi "...Guess that's the end of my conversation with him."
    hide sid with dissolve
    show stella happy with dissolve
    t "Food's here, so the party's started right?"
    b "...Yes, but I don't like where this is going."
    t "Party started means drinking time's started!"
    b "Have you not been drinking all day?"
    t "On and off. Even someone like me needs breaks."
    b "What constitutes a break?"
    t "Oh you know, an hour-long nap to sober up."
    show stella happy:
        xcenter .25
        linear 0.15 xcenter .75
    show shahar ind with moveinright:
        xcenter .75
    h "Aye, did someone say time to start drinking?"
    b "I'm... gonna go talk to some other people."
    h "Suit yerself lad, we'll be drinking with ye tonight anyway!"
    hide shahar
    hide stella
    with dissolve
    bi "I made my way to chat with Sam and Dracula."
    show sam:
        xcenter .25
    show drac ind:
        xcenter .75
    with dissolve
    s "Hello Bert."
    b "Hey, sorry, needed to get away from the drunkards."
    b "Hope I'm not interrupting anything here."
    d "No, you're free to join us."
    s "Though you should be warned, I believe we both plan to drink at some point."
    s "If that bothers you maybe you can go see if Catherine and Jenny need help in the kitchen?"
    b "That's fine with me."
    s "In that case, maybe you wouldn't mind grabbing us a first round from the kitchen?"
    b "...I get the message."
    d "Sorry Bert, nothing personal, but trust and time are limited commodities here."
    hide sam
    hide drac
    with dissolve
    bi "I'd probably just be distracting Catherine and Jenny in the kitchen."
    bi "Well, that only really leaves me two people to talk to."
    show lauren ind with dissolve
    b "Hey, how's it going?"
    l "It's okay. Freddy's pretty torn up about not having Sesame at the party."
    l "While it's very nice of Catherine and Jenny to cook for us, they were some of the people Freddy got along better with."
    l "So, no offense, but it's pretty much is just me that he gets along with at the party right now."
    b "Huh? I thought we were getting along fine..."
    l "You asked him about his home life, right? He told me on the way down here."
    b "Oh... yeah, I was just trying to figure out why he's here."
    l "I get that you're trying to be helpful but..."
    l "Given some of the very innocent crimes people are \"admitting\" to I don't think knowing more about him will accomplish much."
    l "And from I gather his home life wasn't great so maybe it's best not to remind him of that."
    b "That's fair, sorry."
    l "Nothing to apologize for, you were just trying to get us out of here in your own way."
    l "But I don't think you need to do that constantly, we don't need to spend every moment like we did on the train."
    b "What do you mean?"
    l "It felt like every moment we spent on the train we were fighting for our lives."
    l "We're still fighting for our lives here, but not as directly, if that makes sense."
    l "I think that and events like this party are overall helping our morale."
    b "That's true, but I worry about how much of us not trying to escape is because we're losing motivation to fight our way out."
    l "Maybe it's because of that, maybe it's just that we're somewhere more relaxing."
    l "I wouldn't overthink it, not like if we find a way out we'll be able to get Shahar and Stella to help us."
    b "That is unfortunately true..."
    l "And people like Sam and Dracula only seem to be interested in very extreme ways of helping us get out."
    l "Anyway, the food is only going to keep Freddy entertained for so long."
    l "I should probably go back to talking to him before Shahar and Stella try to do anything stupid around him."
    b "I'll join you."
    bi "In part because... I somehow forgot to try out the food."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show frog ind with moveinleft:
        xcenter .25
    l "Hey Freddy, how's the food?"
    f "It's so good! So many different types of cheese."
    f "I don't think I know all of their names, some are a bit long."
    f "Like Cam... Cam... Camembert?"
    b "Hey, that's me!"
    f "Huh?"
    f "Oh, I get it."
    l "Don't eat too much cheese, gotta save some space for the rest of the meal."
    bi "As they talked I picked up a plate and took some of the cheese and meat on crackers."
    bi "..."
    b "Oh my god."
    l "Huh?"
    l "Everything okay?"
    b "It's... it's beautiful."
    f "What is?"
    b "The food."
    f "Huh? Looks normal to me."
    b "It's so tasty, after all those turkey sandwiches and bar snacks."
    b "The spices and seasoning on the sausage."
    b "The nibbles of pepper in the jack cheese."
    b "The slight saltiness of the cracker."
    l "...Are you sure you're okay?"
    b "Sorry, I'm having a bit of a moment."
    b "It feels like ages since I've had real food."
    l "You know it's only been a few days since this whole game started, right?"
    b "More like a few days too many!"
    l "..."
    l "C'mon Freddy, let's go sit on the couch and eat."
    hide lauren
    hide frog
    with dissolve
    bi "...well, seems with my hunger pangs I've alienated everyone except Sid here."
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "stella", "jenny")
    show jenny happy with dissolve
    j "The next course is ready! We have appetizers and salad."
    j "For the appetizers we have kebabs, and the salad is a kale caesar."
    b "Wow, Jenny, did you make these?"
    j "Well, Catherine prepped the meat, I just put the kebabs together."
    show jenny ind
    j "And I had a... complicated family situation so I made lots of meals for myself growing up."
    j "Salad is easy to make, so I made a lot of it."
    b "...Is a salad that filling?"
    show jenny happy
    j "If you pour on enough dressing yeah!"
    j "I love Caesar dressing... oh, but I didn't add that much this time because there's more courses coming."
    b "This all looks really good, but are you and Catherine getting a chance to eat?"
    j "We've been taste testing the food throughout the day, and we have some portions saved for ourselves."
    j "No need to worry Bert, we're taking care of ourselves too!"
    b "Well, if you want to take a break and come out here I'd be happy to swap in..."
    b "I might be saying this so I can take a break from Stella and Shahar's shenanigans."
    j "You mean their Stellanigans? Or maybe their Shahanigans?"
    show jenny happy:
        xcenter .5
        linear 0.15 xcenter .25
    show stella drunk with moveinright:
        xcenter .75
    t "Did someone say Stellanigans?"
    b "Huh? How was that a word that caught your attention?"
    t "That's what a lot of my subordinates called my drunk antics."
    j "Ha, knew it was a good word!"
    j "Stella, you look like you're having a good time! That's good to see."
    b "No, don't encourage her!"
    t "Thanks sweetie, you look good too."
    show jenny ind:
        xcenter .25
    j "Huh? That's not what I said..."
    t "Anyway, Bert, you remember our adventure last night?"
    b "...Adventure?"
    t "You know, the one upstairs."
    b "I'd hardly call that an adventure, but sure."
    t "I think I'm going to continue that adventure, want to join?"
    b "Not really... does Shahar not want to join you?"
    t "Psh, he's carrying a lot of muscle but he's a bit of a weak drunk."
    t "Says he's still tired from last night and wants to stay down here and keep drinking."
    b "I uh... no."
    t "Psh, killjoy as always."
    t "Well, I'm off!"
    j "Wait, Stella, I really don't think it's a good idea for you to..."
    t "Vroom!"
    hide stella drunk with moveoutright
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "jenny")
    show jenny ind:
        xcenter .25
        linear 0.15 xcenter .5
    j "...And she's gone."
    j "Sigh. Well, if you do want to help out Bert, do you know where I can find some batteries?"
    j "Catherine said the clock we're using died and wanted me to find some replacements."
    b "Oh, I think there's some in the garage."
    b "I'm surprised Catherine didn't tell you that, she was the one who found them yesterday."
    j "She's cooking like crazy, I'm sure she's just distracted.":
    j "But thanks! I'll go get them right now."
    hide jenny with dissolve
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid")
    show shahar ind with dissolve
    h "Ahoy lad, is Stella gone?"
    b "Uh, yeah, were you not going to join her?"
    h "Nay, there's a bounty of rum in the kitchen and I wanted to have as much as I could afore she drinks it all."
    h "That lass is stashin' a second liver somewhere in here, I swear t' Blackbeard!"
    h "If I open a bottle I'll have hardly a shotful before it's gone!"
    b "Oh, yeah, then you're good to grab it now."
    h "Aye-aye, to the kitchen, chaaaarge!"
    hide shahar with moveoutleft
    $showchibi("dracula", "freddy", "lauren", "sam", "sid")
    show sam:
        xcenter .25
    show drac ind:
        xcenter .75
    with dissolve
    d "Do tell, Bert, what was that all about?"
    b "Well, Stella went upstairs to continue trying to break apart the bathroom."
    b "And Shahar is using the opportunity to have a drink without Stella stealing some."
    d "Well, as long as the drunkards are gone, we can have peace and quiet."
    b "...Aren't you two drinking right now as well?"
    s "Yeah, you didn't get us one so we poured ourselves a round."
    b "I thought you wanted me to leave you alone, not actually get you a drink."
    s "Well yeah, but a drink would've been nice too."
    d "Regardless, I have basically infinite tolerance."
    d "Vampires' metabolism works differently than puny human metabolism."
    s "And I'm not going to drink that much, just a casual amount."
    s "Enough to loosen up without causing a ruckus."
    b "Oh yeah, isn't your course of the meal coming up?"
    s "Yeah, just the entrees are left before dessert."
    s "But again, I just need to take my dessert out of the freezer and find something to cut it into pieces with."
    b "Huh? Is there not a bunch of knives in the kitchen?"
    s "No, there's only one. According to Lauren when she searched she could only find one yesterday in the whole kitchen."
    s "And Catherine wanted to serve it with the entree so people could cut themselves a portion."
    d "Clever, the knife can't be used as a murder weapon if it's in the middle of a crowd."
    s "I'm not sure if that was her attention."
    s "She's a bit of a ditz, I don't think she thinks things nearly that far that aren't cats or food."
    b "...You know she's in the other room and could walk in any moment."
    s "I'm sure she's heard it before, or figured it out herself."

#Notes: Shahar leaves dining room to grab screwdriver to open a bottle. Jenny leaves to grab clock. Sam leaves to grab stepstool.
