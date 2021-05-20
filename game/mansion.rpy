label mansionGo:
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
    s "{i}Scrichhhh{/i}"
    b "Sesame can scratch her way out of here for us!"
    c "What? Don't be silly."
    c "There's also some simple tools, like a drill, a level, a hammer, a screwdriver, and a stepstool."
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
    c "There's also a generator here, it seems like it's fully fueled."
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
    scene black
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
        xcenter .25
    show shahar ind with moveinright:
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
