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
    d "Unfortunately, the above bedrooms only have beds to fit one."
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
    d "Continue going on your little date around the house, it'll be more fun than us."
    bi "Is everyone going to keep bringing this up? It's getting annoying."
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
    c "There's also some simple tools, and a stepstool."
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
    i "while we're here, before someone dies, I... thought it'd be nice if we had a fancy dinner party."
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
    
