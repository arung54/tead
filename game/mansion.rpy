label mansionGo:
    $ftecounter = 2
    scene black
    bi "..."
    bi "Two people died..."
    bi "And there's nothing I could do to save them..."
    show bg mansiondining
    $ statusnt("???", "bert", ch=2, sun=5)
    with slowdissolve
    bi "I slowly came to my senses and looked to my left."
    show frog sad with dissolve
    $showchibi("freddy")
    f "nrg...."
    bi "...no, that's not how I should think about it."
    bi "There were ten people I did help save."
    bi "If we didn't investigate and uncover Kaiser's secrets, we..."#JJJ
    bi "...we all would have been killed." #JJJ
    bi "Though, I still feel no closer to figuring out who the game master is..." #JJJ
    bi "Either way, I need to keep my guard up and protect everyone here."
    show frog ind
    f "Oh, Bert! Are you awake? Feeling okay?"
    bi "This kid's one of them."
    bi "I have to keep him safe."
    b "Yeah, I'm fine. Thanks for asking. How are you?"
    f "Eh, kinda sleepy like always."
    f "We're in a really nice house now though!"
    bi "For a kid he doesn't seem that shaken up about what just happened..."
    bi "But looking around, I had to agree."
    $ statusnt("Dining Room", "bert", ch=2, sun=5)
    bi "It seemed like we were in a very posh dining room. A nice change of pace from the crowded train..."
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
    l "Hey Freddy, you doing okay?"
    l "You wanna look around and try to find food with me? Everyone's probably hungry after sleeping!"
    f "S-sure..."
    hide lauren with moveoutleft
    hide frog with moveoutright
    $showchibi()
    bi "Thank goodness for Lauren, she's great with the kids." #JJJ
    bi "Oh, everyone else is here too, waking up like us."
    $showchibi("catherine", "dracula", "jenny", "sam", "shahar", "sid", "stella")
    show drac ind with dissolve
    d "Hmm. I see Lauren and Freddy have already started exploring."
    b "Something like that. I think she's just trying to keep him from crying."
    d "Regardless, they have gone to a new area without consulting the rest of us."
    d "Seems somewhat rash."
    d "As well, I was hoping we could discuss what little we've learned from Kaiser before his death."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .25
    show sam with moveinright:
        xcenter .75
    s "I agree with the vampire."
    d "We may as well discuss it now, and catch those two up later."
    s "No time to waste really..."
    d "First, Kaiser mentioned the train we were in is very similar to a train he'd been in before."
    d "It seems we're in some sort of mansion. Perhaps the murderer this time has been in this mansion before?"
    hide sam with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "Woah! So you think someone here has been in this mansion before?" #JJJ
    d "It would make sense, yes?"
    b "He has a point... If there were direct ties between Kaiser and the train, maybe..."
    c "Maybe someone his direct ties to this mansion?"
    d "Precisely."
    d "In which case, while exploring let's look for clues that tie specific people to this place."
    d "That way we can identify the murderer ahead of time."
    d "Ideally they would just kill the Game Master and we all escape, but if not we can protect ourselves in this way."
    bi "Dracula's very calm and collected about this."
    bi "It seems like a pretty good plan, though maybe a bit optimistic."
    d "Secondly, we know that Kaiser, Stella, and Sam have all admitted to some sort of crime."
    bi "Stella and Sam?"
    bi "Oh right..."
    scene black
    show bg trainmid
    show stella ind
    show sepia:
        alpha .5
    with fade
    t "I tore down competition, I burned bridges, you name it."
    t "My methods don't always see eye-to-eye with the law, but, c'est la vie."
    hide stella
    scene bg trainmid
    show sam
    show sepia:
        alpha .5
    with dissolve
    s "I used to sell drugs, mostly to upper-class business people and spoiled rich kids."
    #hide bg trainmid
    #hide sam
    #hide sepia
    #with dissolve

    scene bg mansiondining
    $showchibint("catherine", "dracula", "jenny", "sam", "shahar", "sid", "stella")
    $ statusnt("Dining Room", "bert", ch=2, sun=5)
    show drac ind:
        xcenter .25
    show catherine ind:
        xcenter .75
    with fade
    d "And Bert almost admitted something on the train as well."
    d "Remember what the screen said in the first room we met in?"
    show start2
    show sepia:
        alpha .5
    with dissolve
    scr "Their endings are deserved."
    hide start2
    hide sepia
    with dissolve
    d "In other words, whoever put us here seems to think we all deserve to die."
    d "Surely you can all finish this train of thought on your own."
    s "We're all criminals."
    bi "Criminal?"
    bi "I wouldn't call myself that..."
    bi "..."
    bi "But I wasn't ready emotionally to contest that statement."
    bi "So I stayed silent."
    hide drac ind with moveoutleft
    show sid ind with moveinleft: ###JJJ v this section below
        xcenter .25
    i "No way, that doesn't make any sense."
    i "I mean, I'm only 16, I can't be a criminal."
    c "Hmm, I'm not sure if you're exempt from the law for being 16, bud."
    i "Well I didn't do anything wrong, really."
    i "Er, well, nothing {i}VERY{/i} wrong..."
    bi "..."
    i "Well, {i}MAYBE{/i} very wrong, but-"
    hide catherine ind with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "I think we get the point."
    j "Based on everyone's reaction, it seems like there's a least some truth to Dracula's point."
    j "I have some doubts though, especially considering Freddy's a literal child."
    b "Yeah, it seems unlikely Freddy is a hardened criminal."
    bi "It's also hard for me to imagine Lauren or Jenny being a criminal..."
    bi "I wonder what they did..."
    hide sid ind with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    #bi "I wasn't the only one."
    #bi "There were some looks of discomfort, but some time passed before anyone spoke again."
    d "Based on the lack of evidence against, it seems this conclusion is correct."
    d "Surely anyone who didn't view themselves as a criminal could counter this argument."
    d "So it could be prudent to strategize around this information."
    hide jenny ind with moveoutright
    show stella ind with moveinright:
        xcenter .75
    t "Strategize how exactly?"
    d "Maybe we could each continue discussing reasons we could be here and try to find a common link."
    d "And by discussing reasons, I mean confess to our crimes."
    d "That common link could then help us identify the Game Master. The Game Master might even be the common link themselves."
    d "We'd be able to identify and eliminate them, ending this all."
    #d "Then whoever is the killer this round would have better odds of killing the Game Master and ending the game."
    d "For example, I've committed vampiric manslaughter."
    d "I think it's unfair to call my need for sustenance a crime, but I digress."
    show scary with dissolve:
        alpha .5
    bi "Common link? The few things people had admitted to definitely didn't have a common link. Was Dracula really this irrational?"
    bi "No... I think I understood what Dracula was trying to do, but it was best not to say it out loud and he must know that."
    bi "We already concluded there's a reasonable chance the murderer this round is tied to the mansion."
    bi "If people honestly admitted to their pasts, we could rule out suspects who hadn't been near this mansion."
    bi "But again, the murderer has no incentive to admit to a crime that could tie them to this location."
    bi "So Dracula must be hoping the murderer isn't so wise."
    bi "Better yet, he's suggesting that the murderer's task, identifying and killing the Game Master, could be aided by this process."
    bi "If they took his words to heart, they would indirectly out themselves, and think that was the right thing to do..."
    bi "But will Dracula's plan really work?"
    hide scary with dissolve
    t "Babe, you're just coming off as senile."
    t "The idea of admitting to our crimes would be much more enticing from a younger guy..."
    t "But we've already discussed this and it seems nobody else wants to speak up."
    d "Hmph, fine. Maybe this is a conversation that should wait for all of us to be present anyway."
    d "But, even if we don't admit to our crimes, maybe we should take precautions like mandatory travelling in pairs."
    t "Rubish!"
    show stella happy:
        xcenter .75
    t "You see the room we're in? This is a palace made for a queen like me."
    t "There's bound to be plenty of high-class booze, stuff you'd find in VIP lounges."
    b "For the first time since the start of all this, Stella makes a great point." #JJJ made him say this outloud and not think it
    b "Hopefully there's some real food and sleeping arrangements..."
    t "I'm not going to let some geezer tell me what to do."
    t "I worked hard my whole life to hire bodyguards, not to be one."
    hide drac ind with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "Again... you're kind of derailing the conversation here."
    s "The point is that we have information, and we should use it to maximize our chance of escaping."
    s "The particulars don't really matter, though I do think admitting our crimes might help."
    bi "..."
    bi "I don't want to think about it again."
    bi "I don't want to relive that moment."
    t "Honey, as someone who has confessed crimes, is that really fair when the vampire and pirate are going to keep playing pretend?"
    hide sam with moveoutleft
    show shahar mad with moveinleft:
        xcenter .25
    h "What d'ye mean pretend? Ain't nothing pretend about me."
    t "Alright, if it means getting to see those abs, I can agree that you're a pirate."
    show shahar ind:
        xcenter .25
    h "Aye, that's what I like to hear!"
    hide shahar with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I do have some concerns about us all admitting to crimes..."
    j "I know it will sound suspicious, but I think for some of us, this very personal."
    j "One of those things that you have to keep bottled up or ignore for your own sanity."
    bi "Y-yeah."
    j "Like the awkward moment from middle school that ruins you when you think of it."
    bi "..."
    t "I agree with the belle. I'm sure some of you have fetishes you wouldn't admit to, what makes a crime so different?"
    t "That being said, are you sure you aren't just trying to get on Bert's good side?"
    bi "Suddenly, all eyes were either on me or Jenny."
    b "What?"
    j "Huh?"
    t "What? You're both young, doe-eyed, happy types."
    t "And it's obvious Bert doesn't want to talk about his crime, so you're bailing him out."
    bi "Is she?"
    show stella bigsmile:
        xcenter .75
    t "But hey, if you're not interested in Bert, I'll take him."
    j "..."
    b "..."
    j "I'm just going to ignore what Stella said."
    hide stella with moveoutright
    show jenny ind:
        xcenter .25
        linear 0.15 xcenter .5
    j "Anyways, I think talking about our crimes would create more sadness and distrust than anything."
    j "Besides, look at the crimes we already know."
    j "Stella did some shady business deal, Sam dealt drugs, Bert's is something about driving."
    j "What common theme would those have that we could figure out?"
    blank "Nobody spoke up."
    j "Exactly. So let's do something useful and explore this place."
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
    d "Well, one more thing."
    d "It seems that despite not being in a fast-moving train, escape is unlikely."
    d "All the windows in this room have been boarded with a metal sheet..."
    d "Even if they were not there, I have a feeling the chips in our brains would likely kill us if we escaped."
    d "And, given what happened to Kaiser, it would seem the chips are going to be hard to subvert."
    d "That is all I wished to say. Would hate to see any more unnecessary deaths than we already have."
    hide drac with dissolve
    show sid ind with dissolve
    i "So um, are we free to go explore?"
    i "I... I've never been in a house this fancy."
    i "I was hoping we'd do what we did on the train and get to explore a bit."
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .25
    show catherine happy with moveinright:
        xcenter .75
    c "Great idea Sid!"
    c "There's bound to be some new information here we can use."
    ses "Mrow!"
    c "Oh, true, and maybe mice to catch!"
    bi "She's as scatterbrained as usual, but it's probably good right now."
    bi "Sid is probably the most shaken up about Dan's death. It's good to get his mind off that."
    b "Yeah, plus we have to figure out what there is to eat and where to sleep."
    bi "I'd be happy to get my mind off it for a bit too."
    hide sid
    hide catherine
    with dissolve
    show jenny ind with dissolve
    bi "I approached Jenny and made sure Stella wasn't within earshot."
    b "Hey Jenny, want to explore together?"
    j "Oh?"
    show jenny happy
    j "Sure!"
    bi "I think after how she helped on train, I can trust her."
    bi "Was Stella actually on to something about Jenny and I? I'm not sure..."
    j "Where should we start? This is quite the upgrade from that trian!"
    $ showchibi("jenny", "shahar", "stella")
    bi "The others left as we started talking."
    b "Guess no one wants to look around here?"
    show jenny ind
    j "Maybe they thought they saw everything."
    j "And to be fair, there isn't much to see."
    j "A large dining table, some furniture..."
    j "There is that ominous portrait, though."
    bi "She pointed above the fireplace."
    bi "A middle-aged, ordinary-looking man dressed up quite nicely."
    b "Wait... who is that?"
    j "No clue."
    b "It must be someone relevant, right?"
    b "Unless the Game Master just took someone's mansion without a problem."
    b "But it seems like anyone rich enough to own this house wouldn't be so easily... overcome?"
    b "Surely they could afford some top notch security or would have police trying to help them retake their mansion non-stop."
    j "You might be onto something."
    j "Maybe it's the Game Master? And this is their mansion?"
    b "Well, that would contradict what the screen told us about one of us being the Game Master."
    b "But maybe we'd be naive to trust that."
    j "Unless someone's met this person before, I don't know if we'll get much information out of this."
    j "Let's look somewhere else. Looks like this room connects to the kitchen and a bedroom."
    b "Let's head to the kitchen, I'm hungry!"
    scene bg mansionkitchen with fade
    $showchibi("jenny", "freddy", "lauren")
    $ statusnt("Kitchen", "bert", ch=2, sun=5)
    show lauren ind with dissolve
    l "Hey, what happened in the other room? Heard lots of chatter."
    b "Well uh..."
    bi "I'm pretty curious how she'll react to the whole, \" we're all criminals\" news."
    b "we've concluded everyone here's a uh, criminal, basically."
    b "Some people suggested we all admit to our crime, but that wasn't very well received."
    l "Ah, okay. Well, good news, the kitchen is rather well-stocked."
    bi "....."
    bi "... is she not at all fazed by the fact that we're all criminals?"
    l "Basically what you'd expect from a kitchen in a mansion!"
    l "Plenty of tools, cutlery, and cookware."
    l "Though there seems to be only one knife..."
    l "Maybe the Game Master didn't want a knife murder to be too easy?"
    l "Regardless, there's also all sorts of meats and veggies, the stove, fridge, and freezer all functioning, tap water..."
    hide lauren ind with dissolve
    show shahar ind with moveinright:
        xcenter .25
    show stella happy with moveinright:
        xcenter .75
    $showchibi("jenny", "freddy", "lauren", "shahar", "stella")
    h "I heard fridge and freezer. Is there rum fer the takin'?"
    t "If the mansion's owner has any class, there should be."
    hide shahar
    hide stella
    with dissolve
    show lauren ind
    l "..."
    l "Hey Freddy, Shahar and Stella want a chance to check out the kitchen, maybe let's not disturb them."
    b "We could just ask them to-"
    l "It's easier to just not bother, honestly."
    b "True. By the way, some people brought up the idea of sleeping arrangements."
    l "Oooo, Freddy, wanna go claim a bed?"
    show lauren ind:
        xcenter .5
        linear 0.3 xcenter .75
    show frog ind with moveinleft:
        xcenter .25
    f "O-okay!"
    hide lauren
    hide frog
    with dissolve
    $showchibi("jenny", "shahar", "stella")
    show shahar ind with moveinleft:
        xcenter .25
    show stella happy with moveinright:
        xcenter .75
    h "Rum, vodka, mead, they have ev'rything here!"
    t "Tequila shots! It's been so long. Bert, Jenny, want to join us?"
    hide shahar with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I'm... not old enough to drink yet."
    t "Who's gonna arrest you? The Game Master who's already broken twenty different laws?"
    t "Plus it'd be good for you and Bert to get to know each other with your inhibitions down."
    b "Alright, I think we've seen everything we need to see here."
    b "Jenny, let's go check out another room."
    hide stella happy
    show stella bigsmile:
        xcenter .75
    t "A bedroom?"
    j "Jeez, get me out of here."
    scene black with fade
    scene bg mansiongarage
    $ statusnt("Garage", "bert", ch=2, sun=5)
    with fade
    $showchibi( "jenny", "catherine", "sid")
    show catherine happy with dissolve
    c "Hey guys! Welcome to Catherine's Garage Emporium!"
    b "Catherine's Garage Emporium?"
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
    c "What? Don't be silly. That's completely unreasonable."
    bi "."
    c "There's also some simple tools and supplies in here."
    c "We've got a drill, a hammer and nails, a screwdriver and screws, a stepstool, and some batteries."
    c "We could use these to repair anything that breaks, maybe?"
    c "Not sure if anyone here's much of handyman though."
    show catherine happy:
        xcenter .5
        linear 0.3 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "I... I could repair things around here."
    i "We couldn't afford to hire people, so my dad taught me how to do basic household repairs."
    c "That's nice of you to offer Sid!"
    c "But hopefully the need doesn't arise."
    c "There's also a clock and some boxes full of junk."
    c "According to the clock it's early afternoon right now."
    b "It's hard to tell for sure, with all the windows boarded up."
    b "We might as well use that as out time standard for now."
    $ statusnt("Garage", "bert", ch=2, sun=2)
    c "Catherine's Garage Emporium Standard time! CGEST!"
    bi "I heard Jenny giggle behind me. I'm jealous of their lightheardedness sometimes..."
    c "There's also a light generator here, it seems like it's fully fueled."
    c "We have running power so we shouldn't need it, but it's nice to know that won't be an issue."
    show catherine ind
    #c "I imagine whoever owns this house isn't paying the electricity bill."
    #c "So unless the Game Master's doing us that favor..."
    b "Yeah, the lights were on in the dining room, and the fridge and freeze are running."
    b "So I don't think we'll need to worry about that."
    show catherine happy
    c "Oh, nice! Do you happen to know if the kitchen is well stocked?"
    c "I used to work as a sous-chef in a kitchen, I could whip us up some nice meals."
    c "Don't have to be vegetarian meals, wouldn't want the meat to go to waste."
    b "Wow, thats awesome of you to offer!"

    ###########
    ########### jenny party
    ###########

    hide sid with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "Hmmm... Catherine, if you're going to cook, I have an idea."
    c "Send it at me!"
    j "Well, I think what we all really need right now is something to bring us together."
    b "Something to bring us together?"
    j "Yeah, like... a fancy dinner party!"

    c "Aww, Jenny! That's such a cute idea!"
    c "Yes, let's do it!"
    c "We'd probably need at least a day to prepare, so it would have to be tomorrow evening."
    j "That should be fine, and we can all chip in to help!"
    hide catherine ind with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Wow, a fancy party?"
    i "I... I've only ever lived in my parents' cramped apartment."
    i "Sustaining ourselves off budget meals."
    i "This is..."
    show sid smile:
        xcenter .75
    i "So exciting!"
    bi "Wow, and just like that, Sid's in high spirits."
    b "Sounds good to me!"
    bi "Honestly, anything to get Sid's mind off of Dan, and this situation as a whole, is welcome in my book."

    #i "O-oh..."
    #i "But... what if the kill happens before then?"
    #c "I think that's just a chance we have to take."
    #hide sid with moveoutleft
    #show jenny ind with moveinleft:
    #    xcenter .25
    #j "That might be a hard sell to the murderer."
    #j "What if they're afraid it will become harder to kill people after the party?"
    #c "This is a bit of a depressing topic."

    bi "I'm glad something good is coming out of this."
    hide catherine
    hide sid
    with dissolve
    show jenny ind:
        xcenter .5
    with dissolve
    b "Ready to keep exploring?"
    j "Sounds good, Catherine gave us a rundown of this room anyway."
    j "Let's see... We saw the dining room, kitchen, and garage."
    j "It seems like we've explored the entirety of this floor, so let's go upstairs?"
    b "Sure."
    scene black with fade
    scene bg mansionhall with fade
    $showchibi("jenny")
    $ statusnt("Upstairs Hallway", "bert", ch=2, sun=2)
    show jenny ind with moveinleft:
        xcenter .5
    j "Okay, so this is the upstairs, huh?"
    b "Prety spacious hallway."
    j "It seems like there are 1,2,3,4,5,6 doors up here!"
    j "Let's check them out from left to right!"
    b "I hear some murmuring coming from that room already..."
    b "Maybe don't-"
    j "Wahoo!"
    hide jenny ind with moveoutleft
    b "-barge in..."
    scene bg mansionmasterbedroom with fade
    $ statusnt("Master Bedroom", "bert", ch=2, sun=2)
    $showchibi("jenny", "dracula", "sam")
    b "The master bedroom?"
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
    d "Hmph, make age jokes if you must."
    d "But being a vampire means that despite my age, I am quite nimble."
    d "Also may I remind you, I don't need to sleep."
    d "...but if I am to spend the night thinking, this room seems ideal to do so."
    b "Before deciding where people will sleeps... or stay awake, do we know what the other living arrangements are?"
    s "There are four bedrooms, including this master bedroom."
    b "So enough for eight of us to sleep on a bed, if people are willing to share."
    d "Unfortunately, besides this room, it seems the beds will only fit one adult."
    d "Fortunately, the couches in the living room seem rather comfy."
    b "Okay, I think in thirty minutes or so we should meet up and decide this like we did in the train."
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
    d "Continue going on your little adventure around the house."
    bi "I nodded, but was a little bit annoyed by the whole conversation."
    hide sam
    hide drac
    with dissolve
    show jenny ind with dissolve
    b "Let's move on? We can check the next room over."
    j "Sounds good."
    scene black with fade

#####

    scene bg mansionbedroom with fade
    $ statusnt("Bedroom 1", "bert", ch=2, sun=2)
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
    hide frog
    with dissolve
    show jenny ind with dissolve
    j "Huh. Looks like they weren't lying about having only small beds outside of the master bedroom."
    b "Yeah, it's very weird for how luxurious the house is otherwise."
    b "The room isn't particularly well furnished either."
    b "Normally there'd be a dresser or something like that in here."
    j "Hm... maybe the Game Master is trying to minimize how many spots things can be hidden in?"
    j "After all, searching four fully furnished bedrooms sounds like a chore."
    b "That'd be awfully considerate for someone who, you know, wants most of us dead."
    j "That's true. But if they wanted us dead, why not just kill us instead of making us play this game?"
    b "I wish I knew."
    j "If you say so."
    b "...Next room?"
    j "Yeah."
    #b "I'm assuming all the bedrooms upstairs look like this, so I think we just need to look at the bathroom."
    #b "We're about to have that meeting anyway."
    scene black with fade

###

    scene bg mansionbedroom with fade
    $showchibi("jenny")
    $ statusnt("Bedroom 2", "bert", ch=2, sun=3)
    show jenny ind
    j "Hey Bert, ummm..."
    j "While we're alone..."
    j "Do the jokes everyone's making about us annoy you as much as they annoy me?"
    b "Yes. Hell yes."
    b "I don't get how people can be saying that kind of stuff while our lives are on the line."
    j "Okay, just wanted to make sure we were on the same page."
    b "I'll speak up next time it happens."
    b "..and you should join me in doing so, since I don't think they all take me seriously."
    b "Mostly Dracula, since I'm not admitting my crime."
    b "Even though he's still claiming to be a vampire..."
    j "Don't worry about him. He's just a grumpy old man."
    j "He thinks that since he's stuck here with a bunch of \"young\" people he's in charge."
    j "You don't need to tell anyone what your crime is, I wasn't just saying that to protect you."
    j "I think that applies to everyone."
    j "Even if someone sharing our crimes could help us..."
    j "I really do think revealing our crimes will just drive in unnecessary wedges."
    b "..."
    bi "I do feel close and comfortable with Jenny, though."
    bi "She has an air about her that's just feels... safe."
    show scary with dissolve:
        alpha .5
    menu:
        bi "Should I... open up to her?"

        "Yes.":
            hide scary with dissolve
            b "I agree, but... maybe I could tell you mine?"
            j "Oh?"
            b "It might help move this all forward."
            b "And... maybe if it's off my chest I won't have to think about it anymore while we're here."
            bi "I shivered a bit at the thought of speaking about it again."
            bi "It seems like Jenny saw me look a little shaken up."
            $ telljenny = 1

        "No.":
            hide scary with dissolve
            b "Yeah, you're right."
            bi "I shivered a bit at the thought of talking about it again."
            bi "It seems like Jenny saw me look a little shaken up."
            $ telljenny = 0
    j "Well, I can tell you mine, if you want."
    j "If it makes you more comfortable with me."
    j "It's not that bad, if anything I'm a little proud of it."
    bi "..."
    bi "Jenny had been so bubbly and supportive this whole time."
    bi "It's hard to process that she's a criminal too."
    if telljenny == 1:
        b "Sure, we can trade secrets."
        j "Okay."
    j "To make money in college I did some card counting trips with friends."
    j "Like you've seen in the movies, we'd go to casinos, some of us would find tables that were hot."
    j "Others would join those tables and play the winning odds as hard as we could."
    j "Card counting isn't technically illegal, but..."
    j "The one time I got caught happened to be one of the more... shady casinos."
    j "One that used underhanded tactics to scare off card counters."
    j "So when they caught me, they made some nasty charges stick."
    j "I'm not old enough to gamble legally."
    j "I used a fake ID to get in."
    j "That alone's not a big crime."
    j "But... they doctored some photos and footage of me."
    j "They blackmailed me, and made it seem like I was drinking while driving while underage."
    j "I was lucky that my parents were able to bail me out, but it was horrifying."
    show jenny happy
    j "But like I said, ignoring how much trouble it caused everyone, I'm kinda proud."
    j "I'm a good enough gambler to make some scary, powerful businessmen scared."
    b "That is pretty impressive."
    bi "...but a somewhat reckless attitude to have about it."
    j "Anyway, that's my crime."
    show jenny ind
    if telljenny == 0:
        bi "Maybe I should just tell her."
        bi "Jenny opening up definitely took some edge off."
        b "I can tell you mine, too."
        j "Oh?"
        j "Only if you want to."
        b "I do."
        bi "Wow, my heart's racing."
    if telljenny == 1:
        b "Okay. My turn."
        bi "Wow, my heart's racing."
    b "Mine's much less... exciting?"
    b "I was 17, driving home after tutoring."
    b "This lady was walking on the sidewalk and suddenly walked into the road, without looking..."
    b "The next light was green, so I was going pretty fast, and had barely any time to react."
    b "And... well, I ran into her."
    b "She didn't make it..."
    b "Fortunately, I had a dashcam with footage that convinced the court to let me off."
    b "But it still haunted me... even if I was legally fine, should I have been driving slower?"
    b "If I was paying more attention, would I have reacted sooner?"
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
    b "Umm, there isn't much to explore in here..."
    j "Oh, yeah, exploring."
    j "It's almost like a hotel; this room is nearly identical to the other bedroom."
    b "We might as well peek into the last bedroom."
    j "Mhm."
    scene black with fade
    bi "We checked the last bedroom door."
    bi "It seemed to be identical to the rooms."
    scene bg mansionhall with fade
    $showchibi("jenny")
    $ statusnt("Upstairs Hallway", "bert", ch=2, sun=3)
    show jenny ind with dissolve
    j "Alright! So three basic bedrooms, and one master bedroom."
    j "That leaves 2 more doors up here."
    j "First up is this closet door..."
    b "Let's see what's inside."
    bi "I tried to open the closet door. It was locked."
    b "It won't open..."
    b "Last time there was a closet that was locked, it wasn't good news."
    j "Nothing we can do about it besides keep an eye on it though."
    b "Yeah, guess not."
    j "I guess that just leaves the bathroom."
    j "Um... you mind checking that out without me?"
    b "Why's that?"
    j "Well, it's a bathroom."
    b "You make a good point."
    j "I'll go grab Lauren and Freddy so we can go to the meeting."
    b "Sounds good."
    bi "I headed to the bathroom by myself."
    scene black with fade
label mansion1:
    scene bg mansionbr with fade
    $ statusnt("Bathroom", "bert", ch=2, sun=3)
    b "So uh..."
    b "Guess this is the bathroom."
    bi "...who am I talking to?"
    bi "It's just me in here."
    bi "This is the nicest bathroom I've been in, I think."
    bi "Even some of the hotel bathrooms I've been in weren't quite this nice."
    bi "There's so much space, the largest bathroom mirror I've ever seen."
    bi "More drawers than I can even think of a use for..."
    bi "I think the knobs on the faucet and in the tub are gold-plated..."
    show bg mansionbr2 with dissolve
    bi "And this huge mirror."
    bi "Man, looking at myself, I feel like I've aged 20 years in the past few days."
    bi "This is such a terrifying situation, but..."
    show bg mansionbr3
    bi "I'm hopeful we can get everyone on the same page and keep everyone alive."
    bi "Especially with news of this party we're going to throw."
    bi "Maybe It'll give us a chance to chat with people and learn more about our situation."
    show bg mansionbr with fade
    bi "...Well, I'm done admiring this bathroom."
    bi "Time to head downstairs for the meeting."
    scene black with fade
    scene bg nmansiondining with fade
    $showchibi("catherine", "dracula", "freddy", "jenny", "lauren", "sam", "shahar", "sid", "stella")
    $ statusnt("Dining Room", "bert", ch=2, sun=3)
    b "It's kinda spooky in here with most of the lights off..."
    show sam with dissolve
    s "So Bert, you called this meeting, right?"
    b "Yeah, mostly to discuss the sleeping arrangements, though Catherine might have an announcement too?"
    show sam:
        xcenter .5
        linear 0.15 xcenter .25
    show catherine happy with moveinright:
        xcenter .75
    c "Yessir! But I'll wait until you're done Bert."
    b "Alright. So there's four bedrooms upstairs, each with a twin bed, except the master bedroom that has a bigger bed."
    b "So five of us can sleep pretty easily."
    hide sam with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    l "For what it's worth, Freddy can probably fit in a twin bed with someone, if both Freddy and that person don't mind."
    l "Freddy, that sound okay to you?"
    hide catherine with moveoutright
    show frog ind with moveinright:
        xcenter .75
    f "Yeah, okay with me!"
    f "Can Lauren be the person I share a bed with?"
    show lauren aw:
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
    #t "Plus a house like this probably has soundproofing."
    show lauren ind:
        xcenter .25
    l "Your libido isn't a valid reason to give you that room."
    t "Fine, the lovebirds should have it then?"
    l "Who?"
    b "You better not mean me and Jenny."
    b "Just because you're drunk doesn't mean it's any less callous to matchmake people in the middle of a life-or-death scenario."
    t "..."
    t "You're all such killjoys, I remember why I work long hours now."
    t "At least when I'm on the clock people have to respect my whims and fancies."
    t "Fine, if I can't have the master bedroom, I'll take the living room."
    #t "I plan to stay up drinking, a couch to crash on is the perfect ending to that sort of night."
    b "I... okay, fine."
    b "I'll volunteer to sleep down here too, since I organized this meeting."
    l "You sure you can deal with Stella?"
    b "Uh, no, but I'm not sure anyone here really can."
    b "Okay, that leaves one more person that needs to sleep out on a couch."
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
    show shahar ind:
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
    i "Oh... yeah, my family isn't that well off so... this is the nicest place I've ever been in."
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
    show catherine ind:
        linear .3 xcenter .45
    bi "Catherine got closer to Sam and whispered, just barely loud enough for me to hear."
    c "Do we need to bring up the fact that Sid got close to Dan before he died?"
    s "No..."
    hide sam with moveoutleft
    show catherine happy:
        xcenter .45
        linear .3 xcenter .75
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
    d "I'm not opposed, but why me?"
    i "Well, I don't like Sam, so that's not an option."
    bi "Sid started to look uncomfortable."
    show sid ind:
        xcenter .25
    i "Also, I don't think I can share a b-bed with Jenny or Catherine."
    i "Shahar and Bert are already sleeping in the living room."
    i "So you're pretty much the only option I have."
    bi "Well, I wouldn't mind switching..."
    bi "Not that anyone would be down to take my spot."
    i "Plus, you claim you don't sleep, so I'd have someone protecting me all night!"
    d "Reasonable enough for me."
    hide drac with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "Wait, if Dracula doesn't sleep, then the big bed isn't getting used."
    c "And surely a gentleman like Dracula would want to protect two of us instead of one?"
    i "Oh, that's true."
    i "Wait, I c-can't share a bed with you though!"
    i "You're a girl!"
    ses "Mrow!"
    c "Sesame's right, it's no big deal!"
    c "That bed is huge anyway, we can leave a three foot Sesame gap between us."
    i "O-okay then Catherine, you can join me!"
    show catherine happy:
        xcenter .75
    c "Woo! Party suite!"
    c "Just me, Sesame, and the boys! (^•ﻌ•^)"
    #b "...make sure she doesn't try anything funny in there."
    b "Alright, then Sam and Jenny get their own rooms upstairs."
    hide sid
    with dissolve
    show catherine happy:
        xcenter .75
        linear 0.15 xcenter .5
    b "Guess we've figured that out. Catherine, do you want to tell them about your announcement?"
    c "Oh yeah!"
    c "So I was thinking tomorrow evening we could have a dinner party!"
    c "It would be a shame to not make good use of all the food in the kitchen."
    c "Plus I'm sure we could all use a mood lifter."
    c "I can do most of the cooking, but if anyone can contribute!"
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
    l "I'm already worried about you and Shahar forcing Bert to deal with your debauchery."
    hide stella with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "In her defense, the point of the party is to lift our moods, right?"
    s "A little bit of drinking isn't going to do any damage."
    s "I might drink a bit myself."
    l "...Are you even old enough to drink?"
    s "Again, all criminals, murder game, trapped here against our will..."
    l "...Fine."
    s "So, that concludes the meeting, right?"
    b "I guess so."
    b "Uh... yeah, meeting over I guess, everyone's free to go."
    hide lauren
    hide sam
    with dissolve
    show drac ind with dissolve
    d "Before people begin to disperse..."
    d "Earlier, we had discussed sharing our crimes and there were some negative reactions."
    d "Chances are that even if people did share, they might lie about it."
    d "But to build trust and provide us with information, I still think it would be prudent to share."
    d "Maybe not with the whole group, but in private with someone you trust."
    d "Sam and I have already done this, it would be nice to see others follow our initiative."
    bi "Is that what they were discussing earlier?"
    d "Some close pairs seem to have already formed anyway."
    bi "...that is true."
    bi "Lauren and Freddy are definitely very close now."
    bi "And... there's me and Jenny, though I don't know how close we are."
    bi "I guess everyone is desperate for someone they can trust in an environment like this."
    bi "Even if that person could be the Game Master, even the illusion of trust is very comforting."
    d "I will not bother trying to enforce this request, since I do not expect everyone to be fully cooperative."
    d "That is all."
    hide drac with dissolve
    show shahar drunk with dissolve
    h "Is that all the business yer gonna jabber about?"
    h "On the sea we don't have meetings, we just sail with the flow."
    h "..."
    h "I fell asleep fer most of that discussion to be honest."
    b "...you fell asleep?"
    h "Aye! If I can sleep on a stormy sea, I can sleep through anything."
    h "Plus, I'm loaded with rum and whiskey."
    bi "...I hope that doesn't stop him from sleeping tonight."
    b "Yeah, if no one else has anything to bring up, everyone can go."
    hide shahar with dissolve
    bi "Everyone except Catherine and Freddy slowly left."
    $showchibi("catherine", "freddy")
    $ statusnt("Dining Room", "bert", ch=2, sun=4)
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
    scene bg nmansiondining
    $ statusnt("Dining Room", "bert", ch=2, sun=4)
    with fade
    $showchibi("catherine", "dracula", "freddy", "shahar", "sid", "stella")
    bi "Well, guess it's time to sleep."
    bi "Or at least, try to."
    show frog ind with dissolve:
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
    d "We are also off."
    d "I trust that you three will not be too loud enough to bother me?"
    b "Uh..."
    d "I'll take that as a yes. And if not, Bert, you will be held personally responsible."
    b "What?"
    bi "Why me..."
    d "Anyway, good night."
    hide drac with dissolve
    $showchibi("shahar", "stella")
    show shahar drunk with dissolve:
        xcenter .25
    show stella drunk with dissolve:
        xcenter .75
    h "Well lad, looks like it's just you, me, the lady, and the rum!"
    t "And duh vodka, tequila, and all duh other drinks."
    b "...how much have you guys had to drink already?"
    h "Oh, just-ish one shot lad."
    b "Oh, that's not that-"
    h "every 15 minutes, each."
    b "...and it's been roughly two hours."
    t "Math's for duh losers, not for me."
    t "Bert, you're gonna get drunk with us, right?"
    b "I was hoping to sleep soon given, you know, we might need to solve another murder case sometime soon."
    t "Come on, haven't you heard duh saying?"
    t "All work and no play makes Bert a dull boy."
    h "Yeah, lad, surely y've some stress pent up in ye."
    h "Stress ye can release through the joys of alcohol!"
    b "No, we really should sleep."
    h "You can sleep when yer in Davy Jones' Locker! Aagagagagah!"
    t "If you really want to sleep, you can sneak into bed with one of duh girls upstairs..."
    t "Just don't squish the cat if you get in bed with Catherine."
    b "Why are you so obsessed with... me and romance right now."
    t "Romance is a cute for word it!"
    b "I'm just saying, you talk a lot about me and my love-life, but never about you and yours."
    t "Do you want to hear about my love life?"
    b "Uh..."
    b "I guess more than I want to hear about you trying to matchmake me."
    t "Alright, but if you fall asleep we're slapping you awake."
    hide shahar with moveoutleft
    show stella drunk:
        xcenter .75
        linear .3 xcenter .5
    t "My job involves a lot of travel."
    t "Not to mention, with the stress of duh job I spend pretty much all my free time drinking."
    t "Which means I can't really keep a steady boyfriend."
    t "Or even meet a guy while sober."
    t "The number of guys I've met {i}drunk{/i} though."
    t "Oh, it helps that I'm a rich businesswoman too. "
    b "You... don't ever want to settle down?"
    t "Eh... not really. Life's so much easier and more fun this way."
    b "Not even if you retire?"
    t "Well, I could probably retire now if I wanted."
    t "I have billions saved up already, my bloodline will be forever wealthy."
    b "Billions? You're only a few years older than me..."
    t "Sorry kid, life is unfair. You should've figured that out when one percent of people own 40 percent of duh wealth."
    b "So why don't you retire now?"
    t "What is this, an interrogation? Did someone commit duh murder while we were drinking? Hahaha!"
    b "Sorry, just trying to make conversation."
    t "Fine. Thing is, kid, retired life's boring if you don't have a passion."
    bi "I don't really like that she keeps calling me kid..."
    t "Right now, my only passion is ruthless business."
    t "It's a sinister passion, but it's duh only thing I'm good at."
    t "Well, that and holding my liquor."
    t "And wrapping cute young guys around my thumb."
    t "But my body can only take so much alcohol and so many cute guys."
    t "So for now, my life is dedicated to my work."
    #b "Didn't you have hobbies as a kid?"
    #t "My hobby was investing."
    #t "...and cute guys, even in high school."
    #t "I joined some school clubs but quit them when I realized I could use duh time moving stocks before duh market closed."
    #t "They were honestly such a waste of time."
    bi "She took a big swig after that."
    b "Hey, can I ask..."
    b "Why are you two drinking so much?"
    b "Are you not scared about our current circumstances?"
    t "Bert, come sit with me for a minute."
    t "Just you and me."
    hide stella with dissolve
    b "Um, okay..."
    show bg stellasit1 with dissolve
    t "Tell me."
    t "Is there anything you've done today you feel like has been useful?"
    b "Well, I figured out our sleeping situation."
    b "Explored around the mansion."
    t "Jeez, you're so.. helpless."
    b "...What does that mean?"
    t "Were those things really that useful?"
    t "Did they get us any closer to getting out of here?"
    b "I... no, but."
    t "If you hadn't stepped up we would've figured out where to sleep eventually."
    t "And exploring the mansion is the bare minimum you can do."
    t "It's like saying you used the toilet today, haha!"
    b "..."
    t "Here, I'll be more useful than you were all day, with one sentence."
    t "Duh guy in the painting? His name's Mr. Sydell."
    b "Huh? Why didn't you mention this before?"
    t "I only just remembered his name."
    t "Don't know him that well, he was probably a footnote on a report I had to read or something."
    t "I hire lots of suits whose job it is to step on guys like him, I don't have time to keep up with all of them."
    t "But I think at at some point my company sunk his into duh ground."
    t "I'm surprised he still had enough left over to keep paying duh taxes for a place like this."
    t "If you want to pretend to be useful some more you can go around asking about him tomorrow."
    bi "Sydell... I don't think I've heard the name before."
    bi "Would anyone confess to knowing him?"
    show bg stellasit2
    t "Here, I'll get you started."
    show shahar peek with moveinleft:
        xcenter .08
        ycenter .378
    t "Hey Shahar, ever heard of Mr. Sydell?"
    h "Is that a fellow pirate?"
    h "Unless he's a ocean lover like myself, I reckon I don't know him lad."
    bi "As expected."
    hide shahar with moveoutleft
    t "Anyways, see, in two minutes I've done more for us while drunk than you did in a day while sober."
    t "I'm not trying to be harsh on you, kid."
    t "You didn't do anything useful because there's very little useful to do."
    t "Someone already has been assigned to murder, someone's going to have to be their victim."
    t "It's not like we're investing, nothing you do will save them."
    t "If that's the case, why not relax?"
    b "Isn't that too fatalistic?"
    show bg stellasit1
    t "That's being realistic."
    t "Take it from someone who works 16 hour days."
    t "Sometimes, there's nothing you can do about a shitty thing."
    t "And so duh best thing you can do is whatever has you most ready to deal with duh fallout of duh shitty thing."
    t "And for a gal like me with a robust liver, drinking to relax is that thing."
    b "I... kind of followed until the last part."
    t "I've given up, kiddo."
    t "I've given up."
    b "..."
    t "Hey Pirate boy, whatcha doin over there?"
    show bg nmansiondining
    show shahar drunk:
        xcenter .25
    with dissolve
    show stella drunk with dissolve:
        xcenter .75
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
    h "I vaguely recall something about trouble with the law."
    h "And well, being a pirate, ye don't really care much about the law."
    h "But I don't remember how er why I got in trouble to begin with."
    t "Hey, maybe you were a businessman in your past life."
    t "I've gotten in plenty of legal trouble myself."
    t "Granted, when you're rich enough legal trouble is just financial trouble."
    h "Aye, I don't think a rich Shahar would choose to become a pirate."
    h "He'd probably be sipping cocktails, enjoying a more intimate relation with the sea."
    h "Reading a good book, since I ne'er had time to."
    h "But I do get motion sickness reading on vehicles."
    b "...but you're a pirate."
    h "I only said I get motion sickness while reading, lad!"
    h "Do you think a pirate's life is being out on the sea readin' poetry?"
    b "Yeah, but..."
    b "Never mind."
    bi "Not worth getting into an argument over this."
    t "Speaking of a pirate's life, don't pirates own a lot of jewelry?"
    t "Shahar I feel like you're rather... bare."
    t "Not that anyone minds."
    h "Ay, you're right about that."
    h "I do own a chestful of booty!"
    h "But booty's inconvenient to carry round."
    t "Ooh yeah, a fat booty makes walking hard."
    #b "I... don't think that's what he meant."
    #t "Oh trust me hun, I get it."
    h "Regardless, we had nary a chance to prepare for this game!"
    #t "Ooh don't worry, you're enough of a stud as is."
    h "Oh, I wonder if this mansion's got any treasure we can plunder?"
    b "...you want to steal something to bring with you when you get out?"
    h "Aye! Least we can do to pass the time."
    b "Or, we could pass the time by sleeping."
    t "I don't know if I can approve of stealing from duh rich given... well, you know."
    h "Aye lass, it's not like I'm pillaging your village!"
    t "Hmm, that is true."
    t "After what my boys did this guy, he's probably too poor now to enjoy his life anyway."
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
    h "Aye, a good pirate adventure!"
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
    hide stella
    hide shahar
    with moveoutright
    bi "Stella was off before we could even get started."
    bi "Dracula's probably not going to be very happy about our noise level after this..."
    scene black with fade
    scene bg nmansionhall with fade
    $showchibi("shahar", "stella")
    show stella drunk:
        xcenter .75
    show shahar drunk:
        xcenter .25
    with moveinleft
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
    scene bg mansionbr
    show stella drunk:
        xcenter .75
    show shahar drunk:
        xcenter .25
    with fade
    $showchibi("shahar", "stella")
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
    t "I'm not here for thinking, I'm here for doing!"
    #t "If you know what I mean."
    #b "You... don't need to keep saying that."
    b "Shhh, stop screaming!"
    t "Plus, it wouldn't be very ladylike of me to bend down and try to look down there."
    t "Killjoy, you mind doing it?"
    h "Why not Shahar?"
    t "I don't think his muscles will fit in the cabinet."
    bi "Hm... if I lie about it, maybe they'll give up."
    b "Okay, going in."
    b "..."
    hide stella
    hide shahar
    show scary:
        alpha .5
    with dissolve
    bi "I peeked under the sink, in the cabinet."
    b "Hm, I don't see any way to detach the handles from the sink down here."
    bi "That was a lie. There were some bolts holding the handles in place."
    hide scary with dissolve
    show stella drunk:
        xcenter .75
    show shahar drunk:
        xcenter .25
    with dissolve
    h "By Davy Jones... this plundering mission might be over lads."
    h "Oh well, it was a noble effort! Let's go sleep."
    t "Ugh, fine. I'm starting to come down anyway."
    bi "Finally..."
    scene black with fade
    bi "With that, we headed downstairs and finally went to sleep."
    pause 1
    blank "The next morning..."
    scene bg mansiondining with fade
    bi "..."
    bi "What time is it?"
    $showchibi("shahar", "stella")
    bi "Those two are still asleep."
    $showchibi("shahar", "stella", "catherine")
    show catherine nocat happy with dissolve
    c "Oh, morning Bert!"
    b "How... how early is it?"
    c "I haven't checked the clock in the garage, but I think most of us got eight hours of sleep."
    c "You probably had less, I heard about your adventures last night from Sam on the way down."
    b "Oh... yeah, that'd explain why I'm so tired."
    b "What are you doing down here before everyone else?"
    c "I'm getting ready for the party tonight!"
    c "Going to be cooking all day pretty much, we have a feast planned."
    c "Freddy offered to \"take care\" of Sesame today, which is great since I don't want his fur or anything getting in the food."
    c "Plus there's some stuff in the kitchen he shouldn't eat..."
    b "Wait, besides alcohol?"
    c "Yeah, raw meat can contain bacteria that can kill cats."
    #c "There's some other stuff that's not lethal but a little bit risky, like yeast and chocolate."
    b "Well, at least Freddy will be distracted for a bit."
    c "Yeah! Anyway, I should go get started. Have a good day Bert!"
    b "Thanks Catherine, let us know if we can help with cooking."
    c "Will do!"
    b "Oh before you go, one more thing."
    c "Oh?"
    hide catherine
    show catherine nocat
    b "Stella said the guy in the picture is a Mr. Sydell. You ever seen or heard of him?"
    c "Hmm... no, can't say that I have. Unless he was an extra in one of the dramas I watched."
    c "But extras probably don't make enough money to live somewhere like here, right?"
    c "Damn, Hollywood is rough."
    hide catherine
    show catherine nocat happy
    c "But not as rough as being a red-headed teenager in Creekvale!"
    b "Uh... ok, was just wondering, thanks. See you later Catherine."
    c "Toodaloo!"
    hide catherine with dissolve
    $showchibi("shahar", "stella")
    bi "Hm... is it even worth asking anyone else?"
    bi "I think after Dracula suggested the murderer's been here before, no one would admit to knowing him."
    bi "Besides Stella, but she claims she barely knew him at all."
    bi "If that's the truth, what reason would she have to come to his mansion? She'd probably send a henchman."
    bi "Plus, it might make me look more suspicious if I seem to know about the guy..."
    bi "Catherine's lighthearted enough to not really care if I ask, but someone like Dracula might be."
    bi "Speaking of which..."
    $showchibi("shahar", "stella", "dracula")
    show drac ind with dissolve
    d "Good morning, Bert."
    b "Morning."
    d "I must say, it was quite loud last night."
    b "Sorry, I can't really do much to control the drunkards."
    b "I did try to at least get them to sleep as early as I could..."
    d "I suppose it's not your fault if you tried."
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
    scene bg mansionhall with fade
    $showchibi("jenny", "sam")
    show jenny happy:
        xcenter .25
    show sam:
        xcenter .75
    with dissolve
    j "Oh, Bert."
    j "Good morning! Sam and I were just about to head downstairs and help out Catherine."
    b "Oh, you're both cooks?"
    j "Not as experienced as Catherine, but I like being helpful!"
    s "I'm more of a baker. Gonna make some dessert."
    s "Some of my customers prefer to receive their product in brownies or cookies, so I got pretty good at baking."
    #s "Plus, there's not exactly much else to do until the party tonight."
    #b "Well, unless you want to get super drunk like Stella and Shahar did."
    #s "Eh, day drinking's not really my thing."
    j "Oh yeah, how was last night?"
    j "I heard some noise."
    b "They uh... tried to steal the sink knob from the bathroom."
    j "...Why?"
    b "Boredom, I guess?"
    b "Anyway, it wasn't too bad."
    b "Once that failed, they let me go to sleep, though I'm pretty tired now from having stayed up."
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
    bi "Well, I guess I have some time to kill before the party."
    bi "Everyone's probably awake by now, maybe I can find someone to talk to?"
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
    f "Oh, hi mister!"
    b "Yeah, Lauren had some stuff she wanted to do."
    f "Oh, cool!"
    b "N-not that I wouldn't want to hang out with you normally."
    f "Huh?"
    b "Never mind."
    f "Check out all these tricks Sesame can do!"
    b "Tricks?"
    f "Yeah! Catherine trained Sesame really well!"
    bi "Turns out, Sesame was trained more like a dog than a cat."
    bi "He could high five Freddy, fetch objects from across the room, even do a backflip."
    f "Sesame and Catherine are really close!"
    f "So he's much easier to train than other cats, she says."
    b "That's rather impressive."
    bi "And convenient for keeping Freddy's mind distracted."
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
    f "My parents pay for a man to come to our house and teach me."
    f "They say it's so I get a better education."
    f "I think it's really because my dad got upset when I went to school with other kids..."
    b "What happened?"
    f "We had a homework assignment where we had to talk about what our parents did."
    show frog sad
    f "I tried asking my dad to help but he said it was too hard to explain."
    f "So I uh, didn't turn in the homework."
    f "The teacher got angry during class and then a bunch of the kids started asking me about it at lunch."
    f "My dad wasn't happy people were bullying me so he pulled me out of that school."
    b "That's... huh. {i}Do{/i} you know what your dad does?"
    f "N-no... after that day I felt like it was better not to ask."
    f "I just know he's not around a lot and is angry all the time."
    b "Do you get to meet other kids still?"
    f "Not really, no."
    f "My mom says I should wear this hoodie and mask so that the kids from my old school don't recognize me..."
    f "I don't mind though, because I feel like a frog when I'm in it!"
    b "That... isn't that lonely, Freddy?"
    show frog ind
    f "Maybe? It's okay though! My mom loves me a lot."
    f "And if I behave my dad gets me whatever I want!"
    b "Well, as long as you're happy..."
    bi "That sounds like a really sad existence."
    bi "I do have to wonder though... is Freddy really a criminal?"
    bi "Maybe he's lying, but if he's stuck at home what crimes could he really do?"
    #b "Freddy, do you use the computer at home often?"
    #f "Yeah! That's how I learned so much about frogs!"
    #b "Do you do anything else on the computer?"
    #f "Uh, I play games and watch other videos sometimes."
    #f "I think that's what most kids do on the computer these days."
    #b "Yeah, makes sense."
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
    l "Oh, Sesame shouldn't come."
    show frog sad:
        xcenter .25
    f "Wh...why?"
    l "There's gonna be a lot of stuff Sesame can't eat or drink at the party."
    #l "She asked us to leave him up here."
    #f "Can't Catherine hold onto him?"
    #l "She's hosting the party, she'll probably be too busy worrying about the food."
    #f "But... but I wanna play with Sesame."
    #f "Can't I stay here?"
    #l "Sorry Freddy, I think it's safest if you're with the group."
    #l "Besides, you gotta eat dinner eventually."
    l "I'm sure you'll have a great time at the party, hanging out with us!"
    f "O-okay..."
    l "Let's head downstairs?"
    f "Yeah..."
    bi "Oh boy, I can't wait to eat!"
    scene black with fade
    scene bg mansionhall with fade
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
    #i "Why can't I drink? Sam's underage and is going to drink."
    #d "Yes, but you are quite young. You are free to do what you wish but drinking definitely gets riskier the younger you are."
    #d "Not to mention, a scrawny kid such as yourself probably has tolerance more similar to a teenage girl."
    #i "Who're you calling a girl?"
    #d "I'm not calling you a girl, just drawing a comparison."
    #i "Screw you old man!"
    #bi "This can only go poorly... let me interrupt."
    b "Hey guys, has the food been served yet?"
    d "No, I believe the chefs are putting the finishing touches on the first course."
    b "Oh, cool. In that case I'll go see if they need any help."
    #bi "Hopefully I defused that conversation..."
    scene black with fade
    scene bg mansionkitchen with fade
    $showchibi("catherine", "jenny", "sam")
    show jenny happy with dissolve
    j "Hey Bert! Whatcha up to?"
    b "Just came to see if I could help with finishing dinner."
    j "You just want to be the first to get served, don't you."
    b "...maybe."
    b "Regardless, is everything going smoothly here?"
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
    show catherine nocat:
        xcenter .25
    with moveinleft
    c "Yeah! If we're fancy people eating a fancy dinner, we gotta serve everything in courses."
    b "Isn't that a lot of work for you? Don't you want to go out and socialize?"
    c "It's fine! If everyone else is enjoying themselves I'm happy."
    c "Plus I missed cooking, it's fun to be in the kitchen!"
    c "Don't worry, I'll be able to party once everything besides dessert is done."
    b "Oh, who's making dessert?"
    hide jenny with moveinright
    show sam with moveinright:
        xcenter .75
    s "Me, I'll be out in the living room soon."
    b "What did you make?"
    s "I made an ice cream cake, was about all I could manage with the ingredients we had."
    b "Still sounds pretty tasty."
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
    b "I guess so. If you need help in here, let me know."
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
    show catherine nocat:
        xcenter .25
    show sid ind:
        xcenter .75
    c "First course is served! We have a charcuterie board with various crackers, cheeses, meats, and some fruit to start!"
    i "Huh... is this what fancy dinners are like?"
    c "Only part of it!"
    c "We're going to do multiple rounds of food, with the main part of the meal being in the second to last round."
    c "The idea is to avoid filling you up too early so you can enjoy a variety of dishes."
    i "Oh... ok. I was gonna say, this doesn't seem like a meal."
    show sid smile:
        xcenter .75
    i "Thanks Catherine, this looks really good!"
    c "No worries! Anyway, gotta get back to the kitchen!"
    hide catherine with moveoutleft
    $showchibi("dracula", "freddy", "lauren", "sam", "shahar", "sid", "stella")
    show sid smile:
        xcenter .75
        linear .15 xcenter .5
    i "Wow, there's so much food here already."
    i "It's insane to me that this is only one course."
    b "I got a big stomach, to me this is a light snack."
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
        xcenter .25
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
    #s "Though you should be warned, I believe we both plan to drink at some point."
    #s "If that bothers you maybe you can go see if Catherine and Jenny need help in the kitchen?"
    b "That's fine with me, just needed something to do."
    s "Something to do? Ooo, in that case..."
    s "Maybe you wouldn't mind grabbing us a round of drinks from the kitchen?"
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
    l "Given some of the very innocent crimes people are \"admitting\" to, I don't think knowing more about him will accomplish much."
    l "And from I gather his home life wasn't great so maybe it's best not to remind him of that."
    b "That's true..."
    #l "Nothing to apologize for, you were just trying to get us out of here in your own way."
    l "I don't think you need to do that constantly, we don't need to spend every moment like we did on the train."
    b "What do you mean?"
    l "It felt like every moment we spent on the train we were fighting for our lives."
    l "We're still fighting for our lives here, but not as directly, if that makes sense."
    l "I think events like this party are overall helping our morale and make sure there's no more... action."
    b "That's true, but I worry we're giving up, or losing motivation to find a way out of this."
    l "Maybe it's motivation, maybe it's just that we're somewhere more relaxing."
    l "I wouldn't overthink it, not like Shahar and Stella are particularly helpful sober anyway."
    b "That is unfortunately true..."
    l "And people like Sam and Dracula are reclusive, but I still think they're trying their best, in their own way."
    l "Anyway, the food is only going to keep Freddy entertained for so long."
    l "I should probably go back to talking to him before Shahar and Stella try to do anything stupid around him."
    b "I'll join you."
    bi "In part because I forgot to try out the food."
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
    l "C'mon Freddy, let's give Bert some space."
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
    j "I had a... complicated family situation so I made lots of meals for myself growing up."
    j "Salad is easy to make, so I made a lot of it."
    b "...Is a salad that filling?"
    show jenny happy
    j "If you eat enough, yeah!"
    #j "I love Caesar dressing... oh, but I didn't add that much this time because there's more courses coming."
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
    j "Stella, you look like you're having a good time."
    b "No, don't encourage her!"
    t "Thanks sweetie, you look good too."
    show jenny ind:
        xcenter .25
    j "Huh? That's not what I said..."
    t "Anyway, Bert, you remember our adventure last night?"
    #b "...Adventure?"
    #t "You know, the one upstairs."
    #b "I'd hardly call that an adventure, but sure."
    t "I think it's time for act two, want to join?"
    b "Not really... does Shahar not want to join you?"
    t "Psh, he's carrying a lot of muscle but he's a bit of a weak drinker."
    t "Says he's still tired from last night and wants to stay down here."
    b "I uh... no."
    t "Psh, Killjoy as always."
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
    j "She's cooking like crazy, I'm sure she's just distracted."
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
    h "Aye-aye, to the kitchen for a rum on the rocks, chaaaarge!"
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
    d "Well, as long as they're gone, we can have peace and quiet."
    b "...Aren't you two drinking right now as well?"
    s "Yeah, you didn't get us one so I went to the kitchen and got us a round."
    b "I thought you wanted me to leave you alone, not actually get you a drink."
    s "Well yeah, but a drink would've been nice too."
    d "Regardless, I have basically infinite alcohol tolerance."
    d "Vampires' metabolism works differently than the relatively weak human metabolism."
    s "And I'm not going to drink that much, just a casual amount."
    s "Enough to loosen up without causing a ruckus."
    b "Oh yeah, isn't your course of the meal coming up?"
    s "Yeah, just the entrees are left before dessert."
    s "But again, I just need to take my dessert out of the freezer and find something to cut it into pieces with."
    b "Huh? Is there not a bunch of knives in the kitchen?"
    s "No, there's only one. According to Lauren when she searched she could only find one yesterday in the whole kitchen."
    s "And Catherine wanted to serve it with the entree so people could cut themselves a portion."
    d "Clever, the knife can't be used as a murder weapon if it's in the middle of a crowd."
    s "I'm not sure if that was her intention."
    s "She's a bit of a ditz, I don't think she thinks nearly that far ahead unless cats or food are involved."
    b "...You know she's in the other room and could walk in any moment."
    s "I'm sure she's heard it before, or figured it out herself."
    b "Regardless, I don't really want to talk about the person selflessly cooking dinner for us behind her back..."
    s "Hmph."
    show frog ind with moveinright:
        rotate 315
        xcenter 1.1
        ycenter .5
    b "Huh?"
    s "Is something the matter?"
    hide frog with moveoutright
    b "I... nothing, I thought I saw someone over there."
    s "You haven't gone delirious already, have you?"
    b "No, I think that's my cue to leave you two alone again though."
    hide sam
    hide drac
    with dissolve
    $showchibi("dracula", "freddy", "lauren", "sam", "sid", "jenny")
    show jenny happy with dissolve
    j "Hey Bert, I found the batteries! Thanks for the help."
    j "The entree should be out soon."
    b "Ooh, what is the entree?"
    j "Meatloaf and french onion soup!"
    b "A... a giant slab of meat?"
    b "I'm so in love."
    show jenny ind
    j "With Catherine?"
    b "No, with meat."
    j "Oh."
    b "Wait..."
    b "Catherine can't eat meatloaf though, right?"
    j "She can't eat the meatloaf, but she had a pretty hearty portion of french onion soup set aside."
    j "We just need to heat it in the oven for a few minutes with the sauce on top."
    j "Anyway, I'm off to go hand the clock off to her."
    j "Seeya Bert!"
    hide jenny ind with dissolve
    $showchibi("dracula", "freddy", "lauren", "sam", "sid")
    $showchibi("dracula", "freddy", "lauren", "sam", "sid", "shahar")
    show shahar ind with dissolve
    h "Aye, Bert, I got this bottle of wine but I need help openin' it."
    h "I seem to have lost me corkscrew."
    h "Do you know if there's any screws I can use to uncork me a bottle?"
    bi "Are Catherine, Sid, and I the only ones who bothered checking the garage?"
    b "Screws?"
    h "Yes lad! All a corkscrew does is turn a screw into the cork and yank it out."
    h "I can just do that with a screwdriver and the back end of a hammer."
    h "Requires some elbow grease, but I got the greasiest elbows around!"
    b "I uh... don't think saying you have greasy elbows sounds as good as you think it does."
    b "Regardless, there's some in a toolbox in the garage."
    h "Aye, lad, I knew ye would help me out. To the booty I go!"
    hide shahar with dissolve
    $showchibi("dracula", "freddy", "lauren", "sam", "sid")
    bi "Hmmm, who should I talk t-"
    f "Pssst! Bert!"
    b "Huh?"
    bi "Freddy said my name from behind the couch."
    scene black with fade
    bi "I walked over and sat behind the couch with Freddy."
    show bg frog couch
    f "Shh! Don't let anyone see you hide back here with me!"
    b "I saw you poke your head out earlier, but I don't think anyone else did."

    f "My parents always said \"Children are best seen, not heard.\""
    f "But they lied about the seen part."
    f "At home my parents argued a lot and I would listen while hiding."
    f "My dad would get really angry at me if he found me trying to listen in on him..."
    bi "This kid really had a weird life, huh."
    f "Anyway, there's some scary people here like my dad, so I thought I should just hide and listen."
    b "You don't to tell me twice bud, parties aren't for everyone."
    #b "I know adults who lurk in the corner at parties because that's what most comfortable to them."
    f "Oh... thanks Bert. But uh, could I ask you not to tell anyone else I'm hiding back here?"
    b "Sure, but let's make a deal?"
    f "Huh?"
    b "If you hear anything that might be useful, let me know."
    f "Well, I did hear one thing."
    f "I don't know how useful it is."
    b "Oh?"
    f "Let's make sure no one is listening."
    $showchibi("dracula", "freddy", "lauren", "sam", "sid", "shahar")
    bi "Looking around, no one was really paying attention."
    bi "Shahar came back in the middle of our conversation, but was too focused on opening his bottle."
    b "I think we're good."
    bi "Freddy leaned in to whisper."
    f "I think I overheard Mr. Dracula discussing his real job with Sam."
    f "It was hard to hear much."
    f "But he said he's an expert on the human body. Knows a lot about stab wounds and blood." #checkpoint
    b "I guess that's expected of a vampire..."
    f "But not just that. He's done some... expe... expi... expire minting?"
    b "Experimenting?"
    f "Yeah, that! He did a lot of that on humans."
    f "Also uh... suff... suffer catering?"
    bi "Probably suffocating..."
    bi "That or Dracula really doesn't like Catherine's food."
    f "He... expi... expe... tried that out. Also uh... ele... Alex trickery?"
    bi "Electricity?"
    f "And uh... fire!"
    bi "That one's probably fire."
    bi "Hm... is this real, or is this just Dracula fabricating a vampire story and Sam entertaining him?"
    bi "This is... very gruesome for a kid to overhear."
    b "Thanks Freddy, that's really helpful."
    b "Did you get any more details?"
    f "No... and you can't tell anyone I told you this."
    f "Mr. Dracula reminds me of my dad, I'm scared of him."
    f "And I don't want to give anyone a reason to hurt me..."
    bi "...Does he understand what kind of situation we're in?"
    b "I won't tell anyone you told me."
    bi "...But I might bring this up without saying you told me if it's relevant information later."
    b "Your secret is safe with me."
    f "Thanks Bert..."
    show bg mansiondining
    hide frog with dissolve
    $showchibi("dracula", "freddy", "lauren", "sam", "sid", "shahar", "catherine")
    show catherine nocat with dissolve
    c "And the entree is served!"
    c "Meatloaf with french onion soup!"
    c "There should be plenty for everyone, I brought a knife from the kitchen. Use it to cut yourself as much as you want."
    c "Don't walk away with the knife though, we only have the one!"
    b "Meat?"
    b "Meeeeeeeeeeeeat."
    bi "Like a zombie, I walked to the meatloaf and cut myself a large portion."
    b "Mmmmm... so juicy."
    b "You're such a good cook Catherine!"
    c "Thanks Bert!"
    show catherine nocat:
        xcenter .5
        linear .15 xcenter .25
    show sam with dissolve:
        xcenter .75
    s "I guess that means I should get dessert ready."
    #hide sam with moveoutright
    b "Meeeeeeeeeeeeat."
    #c "Hey, you know I'm vegetarian right."
    #c "You could at least not rub it in so much."
    s "Weirdo."
    b "...Sorry"
    #show sam with moveinright:
    #    xcenter .75
    s "Hm, since there are no knives in the kitchen..."
    s "Catherine, did you see anything else we could use to cut the dessert into slices?"
    c "Hmm, not sure, though there's some cabinets that we haven't looked in because they're high up."
    c "Maybe you could try those?"
    s "Sure, I think there was a stepstool in the garage."
    s "I'll go grab that and use it to search."
    c "Sounds good! Jenny is still in there cleaning up so she can help you if needed."
    s "Got it."
    hide sam with moveoutright
    $showchibi("dracula", "freddy", "lauren", "sid", "shahar", "catherine")
    show catherine nocat:
        xcenter .25
        linear .15 xcenter .5
    c "Well, that's it for cooking."
    c "Time to party hardy!"
    hide catherine with dissolve
    show sid happy with dissolve
    i "I'm so full... how am I supposed to eat this meat loaf..."
    b "Ate too much, big guy?"
    i "I shouldn't have taken what you said as a challenge... Whoa, how are you gonna eat that big a slice?"
    b "I have lots of experience at all-you-can-eat Korean barbeque."
    b "My stomach has slowly expanded over the years through rigorous training."
    bi "By which I mean getting fast food at midnight even after having a big dinner."
    i "Well I don't wanna be outdone! I'm gonna eat a big slice of meatloaf too!"
    b "Uh, that might not be the best-"
    i "*burp*"
    b "Oh jeez... pace yourself Sid, don't go overboard."
    #b "And please let us know if you're not feeling okay, overeating is a very real thing."
    i "I... I will eat this meat loaf... just let me sit down first."
    hide sid with dissolve
    show jenny happy with dissolve
    $showchibi("dracula", "freddy", "lauren", "sid", "shahar", "catherine", "jenny")
    j "Well, I cleaned the kitchen up the best I could."
    j "How's the party been Bert?"
    b "Good, it's nice to just make conversation with people."
    b "And eat good food!"
    bi "I took yet another large slice of meat loaf."
    show jenny ind
    j "I guess I should go socialize with the others while you have your mouth full..."
    b "Hrm? Erkay, guh uhb fuh wih ereryah!"
    j "...You should learn to swallow before talking at a fancy party."
    hide jenny with dissolve
    bi "...is she upset?"
    bi "Oh well. I spent a while eating my meat loaf. My eating speed was starting to slow down, for better or worse."
    bi "As I sat and ate, Sam had come back with the stepstool and walked through to the kitchen."
    bi "After some more time had passed..."
    show sam with fade
    $showchibi("dracula", "freddy", "lauren", "sid", "shahar", "catherine", "jenny", "sam")
    s "Dessert is ready."
    s "Nothing too fancy, just an ice cream layer cake."
    b "Ice cream layer cake?"
    s "Yeah. It's like a normal layer cake, but one of the layers is ice cream."
    b "Did you find something to cut it with?"
    s "Yeah, there's no more sharp objects in the kitchen, but I found the sheath for the knife Catherine was using."
    s "It's much blunter than a knife, but it should work fine."
    bi "Just like before, I cut myself way too big a slice."
    bi "It seemed Sam had already cut one piece out, with rather clean cluts."
    bi "In contrast, my cut looked more like I beat my slice of cake to death..."
    bi "Well, good thing the shape of my slice doesn't matter, it's all getting digested anyway!"
    bi "It's so tasty, but I'm so full..."
    bi "But everyone has a dessert stomach."
    s "Well, my work here's done. I'm gonna go party."
    hide sam with dissolve
    show sid ind with dissolve
    i "I... I ate way too much."
    b "Huh?"
    i "Bert... help..."
    show sid ind:
        xcenter .5
        linear .15 xcenter .25
    show lauren ind with dissolve:
        xcenter .75
    l "Sid, you okay?"
    i "I... I think I'm gonna vomit."
    l "Come on, let's get you to the bathroom."
    i "It... it hurts to move."
    l "Bert, can you lend me a hand in getting him up the stairs?"
    bi "But... my cake's gonna melt..."
    b "Yeah, let's go."
    bi "We each got an arm under one of Sid's shoulders and lugged him up the stairs."
label mansion2:
    scene black with fade
    show bg mansionhall
    $showchibint("lauren", "sid")
    with dissolve
    show sid ind:
        xcenter .75
    show lauren ind:
        xcenter .25
    with dissolve
    b "Alright, come on buddy. Just a few more steps."
    i "I swear I'm gunna throw up everywhere."
    l "Don't throw up in the bathtub, I was hoping to use that at some point."
    i "No promises ahhhh!"
    hide sid ind with moveoutright
    bi "Sid sprinted to the bathroom door and pulled it open."
    scene black with fade
    bi "He really had to vomit... but..."
    bi "I can't blame him."
    bi "After seeing what we saw in there, I wanted to vomit too."
    scene bg mansionbr
    show stella dead:
        zoom 1.0
        xcenter .37
        ycenter .8
    with Dissolve(2.0)
    $ showchibi("lauren", "sid")
    b "..."
    b "Wh-wha?"
    bi "Stella's body lay in front of us, slumped on the sink, a stab would in the dead center of her back."
    bi "A smell that felt too familiar lingered in the air."
    show lauren ind:
        xcenter .75
    with dissolve
    l "..."
    l "Another one so soon?"
    b "H-hold on, maybe she's still alive?"
    l "I'm sorry Bert, I think she's dead."
    b "D-don't say it so casually."
    l "Sorry."
    l "Bert, maybe it'd be good if you and Sid stepped outside."
    l "Take as much as time as you need to calm down. I'm going to go let everyone else know."
    hide lauren with dissolve
    $ showchibi("bert", "sid")
    b "Y-yeah."
    show sid ind:
        xcenter .75
    with dissolve
    i "Bert?"
    i "Did it happen again?"
    b "Yeah, it did."
    i "Wh-why am I always the first person to find the body."
    i "I swear it wasn't me."
    b "I know, there wasn't a moment we weren't together we last saw Stella."
    i "O-ok."
    i "Sorry, I'm just... still shaken up from everyone accusing me of Dan's death."
    b "We're... we're gonna get through this one too Sid."
    b "Let's go outside, I can't handle being in here right now."
    scene black with fade
    blank "Arun will fill in a cleaner transition from the body discovery to the investigation later."
label mansPreInv:
    play music "audio/inthefaceofdeath.mp3"
    call screen diningInv with dissolve
label trial2a:
    play music "audio/rush.mp3"
    scene black with fade
    bi "Everyone gathered in the dining room."
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show lauren ind with dissolve
    l "Well, this murder should be easier to figure out than the previous one."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show catherine ind with moveinleft:
        xcenter .25
    c "What makes you say that?"
    #b "Uh... is it okay to have Sesame around again?"
    show catherine happy:
        xcenter .25
    #c "Yeah! Now that I'm not busy cooking I can hold onto him while we talk."
    c "Huh? What should make this murder easier to solve?"
    l "Well, there's not a tunnel for this mansion to go through that caused Stella to get stabbed."
    l "So someone had to be physically there to do it."
    l "Also, it's pretty obvious what the murder weapon was."
    show catherine ind:
        xcenter .25
    c "Is it?"
    l "Yeah, it was the skewers from the dinner party."
    c "Oh no, did the dinner party get Stella killed?"
    b "I wouldn't view it that way, the skewers would have been in the house regardless of us having a party or not."
    b "But what makes you so sure it was the skewers?"
    l "Let me explain..."
    python:
        stabwound = 0
        stabwound2 = 1
        startMansionTrial("lauren", "Lauren: The {color=#f00}knife was in the dining room the whole time{/color}.", -1,
        "lauren",  "Lauren: Plus there's {color=#f00}no evidence suggesting the knife was used{/color} to stab her.", -1,
        "lauren", "Lauren: So it must be the {color=#f00}only other sharp object{/color} we had access to, the skewers.", -1,
        "catherine",  "Catherine: Would they really have been able to stab her to death with skewers?", 0,
        1, stabwound, "trial2b")
label trial2b:
    play music "audio/rush.mp3"
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show lauren ind with dissolve
    b "Lauren, I think you missed something because you were watching over Freddy during our investigation."
    b "When we took a close look at the body, the stab wound was the shape you'd expect from using the kitchen knife."
    b "It'd be pretty hard to create that kind of shape with a skewer."
    l "Hm... what if they stabbed Stella with the skewer multiple times in a line?"
    b "They could have, but I don't think it would produce the same shape."
    b "It'd probably look more like a line of varying width."
    b "Also, why would the killer try to do that?"
    l "I guess..."
    l "But how did they use the knife then?"
    l "I'm still pretty sure it was in the dining room the whole time."
    b "..."
    bi "I looked around."
    bi "Seems no one had a good answer for that."
    bi "Despite our initial hopes, it seemed this case wasn't going to be much easier."
    hide lauren with dissolve
    show sid ind with dissolve
    i "I have something I wanna talk about."
    i "When did the murder actually happen?"
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .25
    show sam with moveinright:
        xcenter .75
    s "C'mon, Sid, isn't it obvious?"
    i "Huh?"
    s "I mean, I don't know {i}exactly{/i} when it happened."
    s "But we have a pretty good estimate."
    show scary with dissolve:
        alpha .5
label trial2c:
    menu:
        bi "When did Stella die?"

        "Before the party started.":
            bi "No, Stella was definitely alive at the party."
            jump trial2c

        "Soon after the party started.":
            bi "Hmm, Stella left the party only after the second course was served."
            bi "So I know she didn't die until after that."
            jump trial2c

        "In the middle of the party.":
            bi "That's it!"

        "Right before we found the body.":
            bi "No, I have other evidence that shows the body had been dead for a while when we found it."
            jump trial2c
    hide scary with dissolve
    b "In the middle of the party?"
    s "Yeah."
    s "She was around for the start of the party, so obviously she didn't die before that."
    s "And she definitely died a while ago."
    i "How do you know? You're not a coroner or anything like that."
    s "Maybe not, but there's evidence that shows the body's been dead for a bit."
    i "I don't believe you!"
    s "Sigh. Fine, you don't have to believe me."
    s "Bert, I don't think Sid and I will ever see eye to eye. Can you explain it to him?"
    b "Uh... let's see, evidence that shows Stella didn't die recently..."
    call screen mansionEvidenceTrial(-1, stabwound2, "trial2d") with dissolve
label trial2d:
    play music "audio/rush.mp3"
    scene bg mansiondining
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sid ind:
        xcenter .25
    with fade
    i "The blood dried?"
    b "Yeah, when we looked at the wound some of the blood had dried."
    #show sid ind:
    #    xcenter .5
    #    linear 0.15 xcenter .25
    show drac ind with moveinright:
        xcenter .75
    d "Blood normally dries after about an hour or so of exposure."
    d "But it varies due to other factors."
    i "How do you know?"
    d "In my... \"line of work\" I see a lot of human blood."
    b "...Anyway, this suggests Stella died a while ago."
    hide drac ind with moveoutright
    show sam with moveinright:
        xcenter .75
    s "It also makes it pretty clear who the killer should be."
    i "Huh?"
    s "I was thinking about this when Lauren was speaking."
    s "Our assumption is the knife wasn't used to commit the murder."
    s "But that's because the knife was in the dining room after the meatloaf was served, where everyone could see it."
    s "Before then, the knife was presumably in the kitchen."
    s "There is one person who could have taken the knife from the kitchen before the rest of us even saw it."
    i "Didn't you go to get a stepstool during the party?"
    s "Yes, but I only left after the meatloaf had been served, when the knife was in the dining room."
    i "O-oh, that's true."
    bi "In that case, the person Sam is talking about must be..."
    scene black with dissolve
    call screen chooseCharMansion("jenny", "trial2e", "Who left the party the same time as Stella, and had been in the kitchen?") with dissolve
label trial2e:
    play music "audio/rush.mp3"
    scene black with fade
    bi "...is it really Jenny?"
    bi "I... I thought we were becoming closer but..."
    bi "I guess I hadn't really kept much of an eye on her after we initially explored the mansion together."
    scene bg mansiondining
    $showchibint("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam
    with fade
    b "Sam, are you... suggesting Jenny murdered Stella?"
    show sam:
        xcenter .5
        linear 0.15 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "Me?"
    s "Is there another Jenny here I could be talking about?"
    j "Why me? I swear I didn't do it."
    s "You did leave around when Stella did to \"go grab batteries\""
    s "And you could've taken the knife with you. Unless Catherine can attest to the knife being in the kitchen the whole time."
    hide sam with moveoutright
    show catherine ind with dissolve:
        xcenter .75
    c "No, I was focusing on prepping dinner."
    c "I wasn't paying close attention to specifics like that..."
    c "So anyone who came to the kitchen when I wasn't using the knife could have taken it out without me noticing."
    j "C-catherine..."
    j "I swear I... I didn't."
    bi "Jenny was starting to tear up."
    bi "I... don't want to think she could have committed murder."
    bi "Can I believe her?"
    bi "Or would I be letting my emotions get the better of me?"
    hide catherine with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "Aye, I don't really follow what yer all discussin', but, I got a riddle for ye."
    hide jenny with moveoutleft
    show sam with moveinleft:
        xcenter .25
    s "Riddle? This isn't the time for games, we might as well move to vote Jenny."
    b "Do you mean a question Shahar?"
    h "That's what I said ye scallywag, a riddle! Don't make me repeat meself."
    h "I be already plenty exhausted weepin' o'er the death o' me drinkin' matey."
    bi "...I'm starting to think this pirate speak is just Shahar's way of coping with the situation."
    h "Why am I not a suspect?"
    h "I went to the kitchen for me rum, and I left the party to grab some tools for me makeshift corkscrew."
    h "But the scallywag seems focused on the fact that Jenny and Stella left at the same stroke of the sun."
    s "As much as calling me a scallywag makes me wish we had an excuse to pin it on you..."
    s "You didn't return to the kitchen after visiting it the first time, correct?"
    h "Ye, but how's that relevant?"
    h "I could still have grabbed the knife and shanked the lady."
    s "Hmm, is that true?"
    show scary with dissolve:
        alpha .5
label trial2f:
    menu:
        bi "No, if the murder happened as Sam described it, the murderer must have returned to the kitchen..."

        "For an alibi.":
            bi "Being in the kitchen isn't a much better alibi than being in the dining room."
            jump trial2f

        "Because of the knife.":
            bi "That's it!"

        "For another murder weapon.":
            bi "If they used the knife, why would they need another weapon?"
            jump trial2f

        "To grab a drink.":
            bi "That would be in character for Shahar or Stella, but not Jenny."
            jump trial2f
    hide scary with dissolve
    b "Sam's suggesting that the murderer had to have returned the knife to the kitchen after stabbing Stella."
    b "Catherine brought the knife from the kitchen to the dining room later."
    b "So, the knife must have been in the kitchen at some point after Stella's murder."
    s "In which case, we're looking for someone who left the dining room towards the foyer, and then was in the kitchen."
    s "The only person whose movements follow that pattern is Jenny."
    s "So she's the only one that could have reasonably stabbed Stella with a knife."
    hide shahar with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "N-no..."
    j "Bert... there must be something wrong with Sam's argument."
    j "Something to save me..."
    bi "I have to admit, Sam does have a point."
    bi "If Catherine wasn't paying attention and Jenny hid the knife on her while walking around..."
    bi "It wouldn't be that hard to get away with the murder as Sam had described it."
    bi "And Jenny would be the only one that could have done it."
    bi "Is this really it? Is the person I thought was my friend a murdere-"
    hide jenny with moveoutright
    show drac ind with moveinright:
        xcenter .75
    d "Hmm."
    d "Something doesn't make sense."
    d "Sam, I'm disappointed, I thought you were more rational than this."
    s "Care to enlighten me then, Mr. Vampire?"
    s "I think I'm being perfectly rational."
    python:
        startMansionTrial("sam", "Sam: The knife was clearly returned to the kitchen shortly after the murder, what part of that do you disagree with?", 0,
        "sam",  "Sam: There was {color=#f00}no reason for the murderer to wait upstairs after the murder{/color}.", -1,
        "sam", "Sam: And clearly the murderer {color=#f00}didn't leave the murder weapon in the body{/color}.", -1,
        "sam",  "Sam: So, what, do you think {color=#55f}the knife went straight to the dining room instead of the kitchen?{/color}", 1,
        2, stabwound2, "trial2g")
label trial2g:
    play music "audio/rush.mp3"
    scene bg mansiondining
    $showchibint("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam with dissolve
    with fade
    b "Sam, we inspected the wound during the investigation."
    b "It looks like something was used to plug the wound after Stella was stabbed..."
    b "What if it was..."
    show sam:
        xcenter .5
        linear 0.15 xcenter .75
    show catherine happy with moveinleft:
        xcenter .25
    c "Oh, I think I can take it from here, Bert!"
    bi "...man, I hate being interrupted."
    c "I watched this detective show that was super popular a few years ago."
    c "I think it's called, like... Warlock or something?"
    c "I can't remember the name, maybe because it's copyrighted."
    b "Huh?"
    c "Oh, never mind."
    c "Anyway, there's an episode where a serial killer builds blades into the belts of his victims, who were royal guards."
    c "Their victims would only die after taking off their belts, so they would die in isolation and it seemed like a ghost killed them."
    c "Can you guess why?"
    b "...Catherine, maybe it's best if we try to solve the murder in front of us instead of a contrived fictional one."
    show catherine ind:
        xcenter .25
    c "Oh, true!"
    c "Okay so, when someone is stabbed, the bleeding doesn't tend to get bad until the sharp object is removed."
    c "The idea is that while the sharp object caused the wound, while it's in the body it also clogs the wound."
    c "When you take it out, the wound is free to bleed out much faster."
    c "If your internals weren't critically damaged by the stab wound, the loss of blood tends to be the cause of death."
    b "You uh... know a lot about this."
    c "I used to be really into this show! I did a lot of searching online after each episode to learn more."
    #bi "Yet you can't remember the name..."
    show catherine happy
    c "Anyway, something similar probably happened with Stella!"
    c "Well, we can't be sure whether bleeding or damage to her internals killed her, but..."
    c "What Bert's suggesting is that whatever caused the stab wound was left in the body and helped limit the bleeding."
    s "This seems like a stretch."
    s "How can we know precisely how much blood there should or shouldn't be based on the knife being taken away?"
    s "I feel like we pinned it on Jenny and Bert's just grasping for straws to protect someone he considers a friend."
    hide catherine with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "Sam, I was the one who pointed this out initially, not Bert."
    d "...and I guess Catherine explained it in... whimsical terms."
    show catherine happy with moveinright:
        rotate 315
        xcenter 1.1
        ycenter .5
    c "I'm helping!"
    hide catherine with moveoutright
    d "Vampires understand very well how human bodies bleed, what Catherine described perfectly explains the state of Stella's corpse."
    d "Perhaps I am wrong, and the lack of blood is just due to other factors."
    d "But it won't hurt us to consider all possibilities, and it can't help to rush a vote for Jenny."
    s "...Fine."
    s "But you agree your theory is tenuous?"
    d "I suppose, yes. But I think we can do a simple test to see if the kitchen knife could even have been used for the murder."
    s "Only now? Why didn't we do this while we were investigating?"
    d "Well, during the investigation I thought it was obvious the knife wasn't the murder weapon."
    d "It was only when your theory was proposed that I began to contend with the idea."
    d "Anyway, my proposed test is to try inserting the kitchen knife into Stella's stab wound."
    d "How well it fits should be very informative."
    hide sam with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "That's... a bit inhumane, don't you think?"
    j "Shouldn't we be respecting the body?"
    d "You're not really respecting my body if you think I shouldn't maximize my chances of surviving this game."
    d "Besides, shouldn't you be in favor of this? This could be exonerating evidence for you."
    j "That is true..."
    j "But I'm not going with you. I don't want to see that happen to poor Stella."
    hide jenny with moveoutright
    show catherine ind with moveinright:
        xcenter .75
    c "Me neither. That sounds kinda gross to watch."
    c "Oh, and the stuff about respecting the dead too, I guess."
    b "Don't you watch murder mystery shows a lot?"
    show catherine happy:
        xcenter .75
    c "Yeah! They're so entertaining."
    b "..."
    d "Anyways, I don't need anyone to follow me."
    d "I'm happy to do the test on my own."
    hide catherine with moveoutright
    show sam with moveinright:
        xcenter .75
    s "Wait, someone should go with you."
    s "You could be the murderer and be lying about the results of your \"test.\""
    d "Me, the murderer? I never left the dining room."
    s "Fine, if you're not the murderer, maybe you're the Game Master trying to spice things up."
    s "I'm just saying, we should have a second person there to confirm."
    d "Sure, doesn't matter to me."
    d "Sam, I assume you're volunteering?"
    s "..."
    show sid happy with moveinleft:
        rotate 45
        xcenter -.1
        ycenter .5
    i "Ha! Not so tough after all, are you?"
    hide sid with moveoutleft
    s "Fine, yeah, I don't want to look at the body again."
    hide sam with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "I'll go, mateys."
    b "Shahar?"
    h "A stab wound isn't more gross than some of the scurvy ye see on the sea."
    d "Works for me. Let's not dilly-dally further."
    scene black with dissolve
    bi "Dracula grabbed the knife and headed upstairs with Shahar."
    bi "The rest of us sat in silence for a few minutes waiting."
    bi "I wasn't sure why."
    bi "Eventually, Dracula and Shahar returned."
    scene bg mansiondining
    $showchibint("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show drac ind:
        xcenter .25
    show shahar ind:
        xcenter .75
    with fade
    b "So? What happened?"
    d "The knife didn't fit in the wound perfectly. That is, there was a tiny amount of wiggle room."
    d "It's quite curious. Unless the killer intentionally jiggled the knife after making the initial cut,"
    d "my guess is the murder weapon is something a bit bigger than the kitchen knife."
    d "And I don't see a reason for the killer to jiggle the knife."
    s "Aye, I can verify everything the geezer's saying."
    s "He did jiggle the cutlass around a bit after shivving the lady."
    d "To clarify, I did not \"shiv\" Stella. I merely reinserted the knife in the existing wound."
    d "I will also say, there was little resistance in reinserting the knife."
    d "I think this is further evidence that the murder weapon was left in the body for an extended period of time."
    d "Had it been removed, I might expect the cavity formed by the wound to start healing, creating resistance during my test."
    d "But there was a minimal amount."
    b "Shahar wouldn't be able to verify that, right? Since he didn't put the knife back in."
    d "No, I'm merely asking you to trust me on this one."
    d "Are there any further questions or objections to my rebuttal of Sam's theory?"
    blank "There was some silence."
    d "It seems like there is none. In that case, let us proceed?"
    hide shahar with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "Proceed how exactly?"
    j "While I'm grateful Sam's theory was debunked, we don't exactly have any new ones."
    hide drac ind with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "Um... I have an idea."
    hide jenny with moveoutright
    show sam with moveinright:
        xcenter .75
    s "Here we go with another Sid idea..."
    i "Hey, screw you, your idea was wrong beforehand."
    b "Sid, ignore Sam. Tell us your idea."
    b "Discussing something is better than discussing nothing, Sam."
    s "Hmph."
    i "Dracula said the stab wound was slightly bigger than the kitchen knife."
    i "So really, we just need to identify an object that's slightly bigger than the kitchen knife, right?"
    i "There can't be that many of those in the house."
    bi "Hm... what fits that description?"
    $ sheath = 7
    call screen mansionEvidenceTrial(-1, sheath, "trial2h") with dissolve
label trial2h:
    play music "audio/rush.mp3"
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam:
        xcenter .75
    show sid ind:
        xcenter .25
    b "...the sheath?"
    s "You know the sheath is a blunt object, right?"
    s "The whole purpose is to carry a knife around without the sharp part being exposed."
    s "It'd be pretty silly for a sheath to be sharp enough to cut something."
    i "Well, what else fits the description of being slightly larger than the knife?"
    i "Since it holds the knife, the sheath obviously is slightly bigger."
    hide sid with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "Can I propose another experiment?"
    s "I thought we were in a mansion, not a laboratory."
    s "What's with all these experiments, anyway?"
    d "This one is less gruesome and involved."
    hide drac ind with dissolve
    blank "Dracula took the knife again and grabbed the sheath out of the now-melted ice cream cake."
    blank "He stuck the knife in the sheath and wiggled it around."
    show drac ind with dissolve:
        xcenter .25
    d "Hmm, there's about the same wiggle room in the sheath as there is in the stab wound."
    s "Yeah, a sheath has to have some breathing room for the knife."
    s "Otherwise it'd be hard to put the knife in the sheath and pull it out later."
    d "Sure, but my point is that maybe Sid's not too far off."
    hide sam
    hide drac
    show catherine happy
    c "Oh, I get it!"
    hide catherine
    show shahar ind
    h "Yes lass, I understand too!"
    hide shahar
    show lauren ind
    l "I think I get it as well!"
    hide lauren
    show sam
    s "I think you're all about to speak over each other and spout some crazy theories..."
    bi "...are they really all on the same page?"
    python:
        startMansionTrial("catherine", "Catherine: They clearly {color=#55f}inverted the sheath{/color} and the inside must be pointy enough to stab with!", 1,
        "shahar",  "Shahar: They used {color=#55f}something to make the sheath sharper{/color} before stabbing Stella!", 1,
        "lauren", "Lauren: The killer {color=#55f}used the sheath as a mold{/color} to make a sharp object.", 1,
        "sam",  "Sam: I found the sheath during the party in the kitchen, and then it stayed here in the dining room. {color=#f00}If you believe me, then the sheath couldn't have gone near Stella's body{/color}.", -1,
        2, -1, "trial2i")
label trial2i:
    play music "audio/rush.mp3"
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show lauren ind with dissolve
    b "Wait, everyone quiet down."
    b "Lauren, say that again?"
    l "The killer used the sheath as a mold."
    b "Hmm... it's a bit out there, I'll admit."
    b "But... it would explain why the inside of the sheath and the stab wound are roughly the same size."
    b "Plus, if the sheath was used as a mold for a weapon itself, the weapon could leave the area without the sheath leaving."
    b "So unlike Catherine and Stella's theories, Lauren's isn't invalidated by Sam's account of where the sheath was during the party."
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .25
    show frog ind with moveinright:
        xcenter .75
    f "So... Lauren is right? We figured it out!"
    bi "I always forget there's a kid here during these discussions of how someone was murdered."
    l "Freddy, are you okay with talking about this?"
    f "Oh, I was napping."
    f "I just woke up when I heard your voice."
    show lauren aw:
        xcenter .25
    l "Aww, that's cute Freddy."
    #b "Wait, I wouldn't go that far."
    #b "It's the most plausible of the theories for how the sheath ties into Stella's death."
    #b "That's all I'm saying."
    hide frog with moveoutright
    show jenny ind with moveinright:
        xcenter .75
    j "Wait, this theory still seems wild to me."
    show lauren ind:
        xcenter .25
    l "Jenny, shouldn't you be the one supporting alternate theories?"
    l "You were just accused earlier..."
    j "Look, I want to survive."
    j "But that doesn't just mean not being accused."
    j "It means finding the truth of what happened, even if I make myself look suspicious in doing so."
    b "..."
    b "That was kind of cool, Jenny."
    show jenny happy:
        xcenter .75
    j "Thanks, I thought of it while we were waiting for Dracula."
    l "Is now really the time..."
    b "Right, sorry."
    b "Jenny, your objection to Lauren's theory?"
    j "I feel like we searched the whole mansion pretty thoroughly after finding Stella's corpse."
    j "If the killer used the sheath as a mold, shouldn't we have found a stabby stick that wasn't the knife?"
    j "Also, what would they even have filled the mold with?"
    bi "Hmm... both good questions I don't know if I have a good answer to yet."
    b "Maybe it would be best if we answered these one at a time, starting with why we couldn't find this object?"
    hide lauren with moveoutleft
    show drac ind with moveinleft:
        xcenter .25
    d "No need. There's a simple solution, really."
    b "Hm?"
    d "Yes. One that can answer both of Jenny's questions."
    d "What the mold was filled it, and why we didn't find the makeshift knife during the investigation."
    b "...Do you want to tell us?"
    d "Bert, I think it's best if someone else fills in the gaps."
    d "If both of us can arrive at the same theory independently, it's more likely to be correct."
    bi "...seems like something someone would say in a mystery game to make the player figure it out on their own."
    bi "But fine."
    bi "What explains both the missing weapon and what it was made of?"
    $water = 2
    call screen mansionEvidenceTrial(-1, water, "trial2j") with dissolve
label trial2j:
    play music "audio/rush.mp3"
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show drac ind with dissolve
    b "Dracula, I assume you're referring to Stella's clothes being damp?"
    d "Yes. I believe it was water."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .75
    show shahar ind with moveinleft:
        xcenter .25
    h "Water? You sure it wasn't a splash of vodka? That'd be more in character fer the lass."
    d "No, the way the killer formed the weapon wouldn't work with alcohol due to its chemical properties."
    d "Not that the liquid itself is particularly relevant to the case. Bert, care to explain?"
    b "Is this part of your \"arriving at the same conclusion independently\" shtick?"
    d "You call it a shtick, I call it a deliberate method to maximize our odds of survival."
    #b "Fine..."
    b "Dracula's suggesting the sheath was filled with water."
    h "Water? How are you gonna stab Stella with a knife made of water?"
    h "Water ain't sharp at all."
    b "Well..."
    show scary with dissolve:
        alpha .5
label trial2k:
    menu:
        bi "I thought this was obvious, but I guess I'll spell it out..."

        "The water made the sheath heavy enough to stab with.":
            bi "Wait, we're assuming the sheath never went near Stella's body..."
            jump trial2k

        "The water cleaned off the substance the knife was made of.":
            bi "I don't have any idea what that substance would be though..."
            jump trial2k

        "The water was frozen before being used as a knife.":
            bi "Duh, maybe I should have started with that."

        "Actually, it was filled with alcohol.":
            bi "...am I still drunk from last night?"
            jump trial2k
    hide scary with dissolve
    b "Ok, let me rephrase."
    b "The sheath was filled with {i}ice{/i}."
    b "That is, the killer filled it with water, then put it in the freezer."
    show drac ind:
        xcenter .75
        linear 0.15 xcenter .5
    d "Again, not that it matters, but something like vodka has a freezing point below the temperature a household freezer is usually set to."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .75
    b "...Thank you for the science lesson."
    hide shahar with moveoutleft
    show catherine happy with moveinleft:
        xcenter .25
    c "Ooh, ice is pretty sharp!"
    c "I once read a news story about a guy who got speared in the head because he walked under an icicle right as it detached from a roof!"
    b "Um... yes, thanks for the support Catherine."
    bi "...How does she have all this esoteric knowledge about random deaths?"
    bi "Also, will I get to finish this explanation without being interrupted again?"
    b "Anyway, the point is, Dracula's theory is that the killer used the sheath to make an ice knife."
    b "Since ice melts at room temperature, we weren't able to find the ice knife."
    b "Well, I guess we did find it, but in the form of water that had been absorbed by Stella's clothing."
    b "This also explains why the wound wasn't that bloody, without the killer needing to come back and remove the knife."
    d "Yes, it is a rather clever and elegant idea, ignoring the fact that it is a murder."
    d "We had been using the murder weapon's location as a means of passing innocense."
    d "But if the murder weapon never had to move after Stella was murdered, all of those alibis need to be reexamined."
    hide catherine with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "This is still kind of a fishy theory, right?"
    i "We're assuming the existence of an ice knife we never actually saw."
    d "Well, is there another explanation for water on the back of Stella's clothes, right where the stab wound is?"
    i "Maybe the killer tried to wash off the blood?"
    d "What incentive would they have to do that?"
    i "...None, I guess."
    d "As well."
    d "Unless there are other objections, I think we can move forward with this theory."
    d "Especially because it has a clear suspect associated with it."
    show scary with dissolve:
        alpha .5
    bi "Oh... That is true..."
    bi "This invalidates one person's alibi directly."
    bi "Plus, they would have been able to pull the ice knife murder easier than everyone else here."
    bi "That person is..."
    scene black with dissolve
    call screen chooseCharMansion("sam", "trial2l", "Who used the ice knife?") with dissolve
label trial2l:
    play music "audio/rush.mp3"
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam with dissolve
    s "Me?"
    s "Bullshit, you don't have proof."
    b "True, Shahar and Jenny both could have also pulled it off."
    b "But think about it, an ice knife would have to be stored in the freezer in the kitchen."
    b "You also were the one who \"found\" the sheath in the kitchen later."
    b "Your ice cream cake gave you an excuse to frequently access the freezer."
    b "And you were the one who was adamant about the sheath not being related to the murder."
    s "So what, you're going to declare me the murderer just because you have a few vague ideas pointing to me?"
    s "By that logic you should have voted off Jenny earlier."
    b "But as far as we know, no one else used the freezer durin-{p=0.5}{nw}."
    s "No, that's not true."
    bi "Oh?"
    bi "Wasn't expecting that."
    s "Shahar. Care to tell us what drink you got?"
    show sam:
        xcenter .5
        linear 0.15 xcenter .75
    show shahar ind with moveinleft:
        xcenter .25
    h "Rum on the rocks. What's it matter to ye?"
    s "On the rocks. As in you had ice in the drink, right?"
    h "Aye, stop asking me such trifling questions."
    s "Where'd you get that ice."
    h "The freeze-{p=0.5}{nw}"
    show shahar mad:
        xcenter .25
    h "Ah. Yer blamin' me, are ye ya landlubber."
    s "Not blaming you. Just saying, you also went to the freezer."
    s "And when did you go to the freezer?"
    h "After Stella went a-plunderin'."
    s "And Bert, when do you suspect I would have killed Stella?"
    b "When you left to grab the stepstool from the garage."
    s "Right, and I was just in the kitchen, but I was in the dining room for a while before that."
    s "So if the ice knife was used in the murder, I must have grabbed it after Shahar went to the freezer."
    s "If I got it beforehand, it would have melted while I was waiting around."
    s "Shahar, did you see any ice knife in the freezer?"
    h "...Nay, can't say I did."
    h "All I saw in there was an ice cube tray and Sam's pile o' tooth rot."
    s "So there you go. If there was an ice knife used, someone else must have done it."
    s "And they must have taken it out before Shahar went to grab a drink, and then they killed Stella shortly after."
    bi "..."
    bi "Damn, that's a good point."
    bi "I really thought we figured everything out."
    bi "We had such a convincing theory, but I guess there wasn't anywhere for Sam to hide the knife."
    h "So what now. Are we lynchin' Sam?"
    s "What? Did you not pay attention>"
    h "I'm not exactly the brightest matey on the poop deck."
    s "Ugh."
    bi "..."
    bi "Wait."
    b "Sam."
    s "What now..."
    b "Just because Shahar didn't see the knife, doesn't mean you couldn't have hidden it in the freezer."
    s "Oh? Care to tell us where I magically hid the knife?"
    show scary with dissolve:
        alpha .5
    bi "Yeah... the cake had to have been hidden..."
label trial2m:
    menu:
        bi "The knife was hidden..."

        "In the cake.":
            bi "That has to be it."

        "In the ice cube tray.":
            bi "How would a knife fit in a tray with cube-shaped compartments?"
            jump trial2m

        "In a hidden compartment.":
            bi "No one mentioned anything about that."
            jump trial2m

        "In the fridge.":
            bi "The ice would melt in the fridge."
            jump trial2m
    hide scary with dissolve
    b "In the cake."
    b "You could've easily pushed the ice knife into the cake to hide it."
    h "Ay lad, wouldn't there have been an obvious hole in the cake?"
    b "Well, when you opened the freezer the hole could have been in the back."
    b "And before the cake was brought out to serve, Sam had already cut a slice."
    b "The edge of the slice could have been aligned with the hole the knife was hiding in."
    b "After the slice was cut, there wouldn't be evidence of a hole in the cake."
    b "Not to mention, the slice was cut rather cleanly, like you had used a real knife."
    b "When I tried using the sheath, the cut was much less flat."
    b "I think in your attempt to hide the fact that you hid an object in the cake..."
    b "You gave us evidence you had access to a knife of some sort."
    b "And we all saw the normal knife in the dining room the whole time."
    b "So... you must have cut the cake with the ice knife."
    s "..."
    s "Fine, just vote for me!"
    s "Time to have the Game Master kill me, I guess."
    s "Not like any of us have made any progress on figuring out who the Game Master is or how to get out."
    s "Might as well just all die swiftly by voting the wrong person."
    bi "I think in a weird way, this is Sam's way of admitting to stabbing Stella."
    bi "There's no more arguments to be had, only anger."
    hide shahar with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "I knew something was fishy with Sam! You're a jerk {i}and{/i} a murderer!"
    i "You're really cruel-hearted, you know that?"
    i "You couldn't just settle for stabbing her! You tortured her for fun, then killed her!"
    bi "...Huh?"
    s "What?"
    i "You know exactly what I'm talking about!"
    s "Umm, no, not really?"
    bi "Sam's just as confused as I am..."
    bi "What is Sid talking about?"
    $burns = 3
    call screen mansionEvidenceTrial(-1, burns, "trial2n") with dissolve
label trial2n:
    play music "audio/rush.mp3"
    scene bg mansiondining
    $showchibint("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sid ind:
        xcenter .25
    show sam:
        xcenter .75
    with fade
    b "...The burn wounds."
    i "Yeah! Sam burned Stella's hands, then killed her!"
    s "Sid, I have no idea what you're talking about."
    i "You can't lie your way out of this one!"
    bi "How did none of us bring that back up until now?"
    b "Wait, Sid, calm down."
    b "Let's not settle on the killer being Sam just yet."
    s "What Bert, realized your conclusions from before were rather silly?"
    b "If you want us to not suspect you, you should cooperate rather than making quips."
    s "...Fine."
    b "The burn wounds. We haven't discussed them at all."
    b "I need to... think for a moment."
    hide sid
    hide sam
    with dissolve
    show lauren ind:
        xcenter .25
    show jenny ind:
        xcenter .75
    with dissolve
    l "Burn wounds? What burn wounds?"
    j "Yeah, I didn't see them either!"
    show ev2 hand with dissolve:
        xcenter .5
        ycenter .5
    b "Stella's hands had what looked like burn wounds on the palms."
    b "Her corpse's hands were face down when we found her."
    b "So if you didn't go out of your way to flip her hands over, you wouldn't have seen them."
    hide ev2 hand with dissolve
    j "But is this really relevant to how she died?"
    j "For all we know they have nothing to do with the murder."
    hide lauren with moveoutleft
    show sid ind with moveinleft:
        xcenter .25
    i "Yeah! We already know Sam's the murderer! No one else is mean enough to do it!"
    bi "Oh boy, we're going to have to get Sid's emotions under control before we can make progress..."
    b "Sid, let's not jump to conclusions."
    b "We still need to figure out a lot about these burn wounds."
    b "For example, how do we know they happened before Stella was stabbed?"
    b "If someone already was planning to stab Stella, why would they put more effort into hurting her?"
    i "I... uh..."
    i "Well, if her hands were burned she couldn't defend herself!"
    b "That's assuming her hands were burned before she was stabbed, which we don't know."
    i "But do you know her hands were burned after she was stabbed?"
    b "I don't, but someone else should..."
    scene black with fade
    call screen chooseCharMansion("sam", "trial2o", "Who would know if Stella was stabbed or burned first?") with dissolve
label trial2o:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    bi "..."
    bi "It comes down to this."
    bi "Are we going to cooperate?" #JULIAN
    show sam with dissolve
    bi "Or will Sam lie and indirectly save someone else in the process..."
    b "Sam."
    s "What do you want now?"
    b "We need to ask you to cooperate with us fully."
    b "That means owning up to stabbing Stella."
    s "What reason do I have to do that? Even if I did it, I wouldn't admit to it."
    b "We have no reason to believe anyone but you was with Stella as she died."
    b "So unless you help us identify someone else who could have done it..."
    b "We're going to have to choose you as the murderer."
    b "But if you can tell us what happened honestly, and that includes evidence it wasn't you..."
    b "It could get you off the hook. And find the real murderer, saving us all."
    show sam:
        xcenter .5
        linear 0.15 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "Wait! I don't buy it."
    bi "What now..."
    i "The Game Master must have chosen Sam to be the murderer, otherwise nothing makes sense."
    $location = 8
    python:
        startMansionTrial("sid", "Sid: If the Game Master didn't choose Sam as a murderer, there's no reason for Sam to kill Stella. Unless Sam had a grudge against Stella, {color=#f00}but I don't think they did.{color=#f00}", -1,
        "sid", "Sid: Kaiser made it sound like it was pretty clear he was chosen as murderer, so there's {color=#f00}no way Sam was confused about being the murderer.{/color}", -1,
        "sid", "Sid: The only other possibility is that two people were chosen, but that {color=#f00} can't happen in this game.{/color}", -1,
        "sid", "Sid: So the fact that Sam tried to kill Stella means {color=#55f}Sam must have been chosen as murderer{/color}.", 1,
        1, location, "trial2p")
label trial2p:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam:
        xcenter .75
    show sid ind:
        xcenter .25
    with dissolve
    b "Wait, remember the discussion we had on the first day here?"
    b "We said that the murderer was likely to have been in this mansion before."
    b "We never figured anything else about how the murderer knew they were chosen, because Kaiser died before he could tell us more."
    b "So it's possible Sam wasn't chosen as the murderer by the Game Master, but has been here before."
    b "In which case, it would be easy for someone who had been here before to believe they were the murderer this time."
    b "But nothing rules out multiple people having been here before."
    b "Someone else could have actually been assigned to be the murderer."
    b "Also, I guess the Game Master never clarified who we should vote for if the designated murderer isn't actually the one who commits murder."
    b "So even if Sam was chosen as the murderer, we might still want to vote for someone else."
    i "This all seems so complicated... isn't there that saying about the simplest explanation usually being the best one?"
    i "Sam killing Stella just makes so much sense."
    b "It doesn't explain the burns on Stella's hands though."
    b "Right now, only Sam can help us find a way to explain that."
    i "...Fine, but Sam better do a good job or I'm going to vote Sam off anyway!"
    hide sid with moveoutright
    show sam:
        xcenter .75
        linear 0.15 xcenter .5
    bi "Ok, Sid's cooperating now, but will Sam confess and tell us what happened?"
    s "..."
    s "Okay, I'll talk."
    s "This... this damn game."
    s "Bert's right, I've been here before."
    s "The guy who lived here, Mr. Sydell, he was one of the people I sold drugs to."
    s "I... I didn't want to murder Stella."
    s "But I thought I had to."
    s "We don't know what happens if days go by without a murder."
    s "Do we starve to death because we run out of food?"
    s "Does the murderer get killed by the chip in their head for not complying?"
    s "No offense, but... you're all strangers to me. And now we think you're all criminals."
    s "I can't in good faith put your lives above mine."
    s "And even if I could..."
    s "What if {i}everyone{/i} gets killed if the murderer doesn't comply and kill someone?"
    bi "..."
    bi "I... I never thought about it from that perspective."
    bi "Am I... feeling bad for Sam?"
    show sam:
        xcenter .5
        linear 0.15 xcenter .75
    show lauren ind with moveinleft:
        xcenter .25
    l "Sam I... think all of understand just how messed up this whole situation is."
    l "You or whoever murdered Stella aren't the enemy. The Game Master is the enemy. I think we can agree with that."
    hide sam with moveoutright
    show shahar ind with moveinright:
        xcenter .75
    h "Nay."
    h "Ye blew a defenseless woman down."
    h "Not to protect yerself from a cutlass, not fer revenge."
    h "Just a poor defenseless lassie."
    h "Even if Sam didn't deal the killing blow, I can't fergive a murderer so becalmedly, I'm sorry lads and lassies."
    l "Shahar, can't we talk this through?"
    hide shahar with moveoutright
    show sam with moveinright:
        xcenter .75
    s "No, Shahar's right."
    s "I might as well be a murderer."
    s "I... hate what I've become."
    s "I wish it was someone else's turn to murder me instead."
    b "Look, Sam, what happened happened."
    b "We... I miss Stella, as much as she annoyed me, but we have to look past that now."
    b "Our lives are on the line. We can't save Stella now, but we can save the rest of us."
    b "But you need to tell us what happened in the bathroom."
    s "..."
    s "Okay."
    s "No emotions this time, I guess."
    hide lauren with moveoutleft
    show sam:
        xcenter .75
        linear 0.15 xcenter .5
    s "I went in there, with the ice knife."
    s "She saw me and greeted me kindly."
    s "I guess she didn't think it was weird I came up there."
    s "But then she then turned back and was messing with the sink."
    s "I took that opportunity, pulled the ice knife out, and stabbed her in the back."
    bi "Several people were starting to look away uncomfortably."
    bi "We had asked Sam to do it, we had seen the corpse but..."
    bi "...hearing a murder described so casually wasn't easy."
    s "She fell hard onto the sink after I stabbed her, trying to brace herself."
    s "But she let out a scream when she made contact with it."
    s "I think because of the pain of collapsing onto it so quickly."
    s "Then her body went limp."
    s "I checked her pulse and her heart had stopped."
    s "I thought I got lucky with where I aimed the knife."
    s "And yeah, I left the knife in her body and that's that."
    b "Hm..."
    bi "Something seems... off about Sam's story."
    bi "Could one stab wound in the back really kill someone so easily and quickly?"
    bi "I guess we can figure that out later."
    bi "For now..."
    b "I think I know precisely what caused the burn wounds."
    s "Oh?"
    b "I had a suspicion even before hearing Sam's story."
    b "But what Sam said makes me even more sure."
    b "Stella's hands were burned by..."
    call screen pickSpot2 with dissolve #pick sink handles
label trial2q:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam:
        xcenter .5
    b "Sam, you said Stella braced herself on the sink, right?"
    s "Yeah."
    b "If we look at the shape of the burn wounds, they're very rectangular."
    b "Just like the sink handles."
    b "Before hearing Sam's story, from the shape of the sink handles and the position of Stella's corpse..."
    b "We could have guessed the sink handles caused the burns."
    b "But Sam's story makes me even more sure, because Stella apparently braced herself using the sink."
    b "So the short version of events is, Sam stabs Stella, causes her to fall onto the sink."
    b "She grabs the sink handles trying to brace herself, and then the sink handles somehow burn her."
    b "Sam, if we can figure out what burned her and if it was lethal, that means you didn't murder her."
    s "..."
    bi "Why's Sam so quiet? This is a moment of hope for us..."
    s "Thanks for trying Bert, but..."
    s "I don't think the sink handles can be what burned her."
    s "So it seems like I'm not off the hook..."
    b "Care to explain?"
    s "Sure, but we may as well vote me off now..."
    bi "Sam's giving up."
    bi "I need to figure this out, and fast."
    $wires = 4
    $generator = 5
    python:
        startMansionTrial("sam", "Sam: Stella {color=#f00}was messing with the sink handles when I got there.{color=#f00}", -1,
        "sam", "Sam: If the sink handles are what burned her, {color=#55f}she should have been in pain before I stabbed her.{color=#55f}", 1,
        "sam", "Sam: So the handles would have {color=#f00}had to heat up in the few seconds after I stabbed her.{color=#f00}", -1,
        "sam", "Sam: No one else came upstairs while this was happening, so {color=#f00}nothing could have heated them up in that time.{/color}", -1,
        1, [wires, generator], "trial2r")
label trial2r:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sam:
        xcenter .5
    b "It's admittedly a bit weird, but I don't think the handles were heated until Stella fell onto them."
    b "There was a generator upstairs, anad when I looked under the sink I saw some wires fed in through a hole in the wall."
    b "It was hard to tell where the wires connected to, but it was probably the sink handles."
    b "And they were probably connected to the generator."
    b "With enough electricity running through them, I'm sure they would get hot enough to burn Stella."
    s "That still doesn't explain how they were only heated up when Stella fell onto them."
    b "I think there's someone who could maybe explain that."
    bi "But... it's not me."
    call screen chooseCharMansion("dracula", "trial2s", "Who could explain how Stella only got burnt after being stabbed?") with dissolve
label trial2s:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show drac ind:
        xcenter .5
    b "Dracula."
    d "Yes?"
    b "What do you know about electricity and the human body?"
    d "...What are you insinuating?"
    b "I know you probably know enough to explain how Stella got burnt."
    b "Since you claim to have conducted \"experiments\" about this kind of thing."
    d "And who told you that?"
    b "Let's just say you should mind your volume level at parties."
    d "Hmph, so you were eavesdropping then?"
    bi "I wasn't, but I promised Freddy I wouldn't say it was him so..."
    b "I happened to overhear it."
    d "A likely story."
    d "Fine, I'll entertain this line of thought. But no one's allowed to inquire further about what Bert mentioned."
    b "So much for everyone being an open book about their crimes, huh?"
    d "..."
    d "I don't particularly care for you right now Bert."
    d "But for the sake of escaping, I will pretend this conversation didn't happen until we have solved this mystery."
    b "Care to explain why you didn't speak up earlier?"
    d "As Jenny said, we all have reasons to avoid bringing up our past."
    d "I was hoping you all would solve this organically, without my help, so I didn't reveal more than I needed to."
    d "If that did not happen, I would have spoken up."
    bi "I don't believe him."
    d "Any more questions, or can I finally explain how this may have happened?"
    b "Fine by me."
    d "Alright, no interruptions please."
    bi "He said that in a way that made it seem like it was directed at the group, but it was definitely at me."
    d "Electrical current can only travel in closed circuits."
    d "For example, if you take a battery and attach a wire to one end only, current won't flow through the wire."
    d "But when you attach the other end of that wire to the other end of the battery, current flows."
    d "Think of the sink handles as ends of a battery, since they were connected to the generator."
    d "And Stella like a wire, with her hands being the two endpoints."
    d "The circuit isn't completed when Stella has one hand on a sink handle, so current won't flow through her from the generator."
    d "But if she grabbed both sink handles to brace herself, she would receive some amount of current."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .75
    show sid ind with moveinleft:
        xcenter .25
    i "Um... I have a question."
    d "Yes?"
    i "I've helped my dad replace car batteries before."
    i "He's grabbed both terminals of a car battery before on accident but he wasn't hurt."
    d "Well, there's two factors at play that determines how bad an electrical shock is."
    d "The first is amount of voltage coming from the source of electricity."
    d "A generator that needs to power a whole house will have a much higher voltage than a car battery."
    d "The second is the resistance of the circuit the electricity is flowing through."
    d "The resistance of a human body can vary a lot."
    d "For example, if your hands are dry, there are lots of dead skin cells on your hand that have high resistance."
    d "This means you transmit less current when you are touching a source of voltage."
    d "In contrast, if you recently washed your hands, as Stella may have, your body has very low resistance."
    i "Ohhhh. Okay, thanks Dracula!"
    hide sid with moveoutleft
    show shahar ind with moveinleft:
        xcenter .25
    h "Gonna be honest, I savvied none of that ye nerd."
    d "Did you just call me a nerd?"
    h "And what if I did, ye lily-livered hag?"
    d "..."
    d "I'm just gonna ignore that."
    d "The point is..."
    d "It makes sense Stella could have only been lethally shocked, or even shocked at all, by touching both handles."
    b "Great, so that answers that."
    b "Dracula, there's one more thing that would be good to know..."
label trial2t:
    menu:
        bi "What should I ask Dracula?"

        "Who killed Stella?":
            bi "Unless it was him or Sam, how would he know?"
            jump trial2s

        "What killed Stella?":
            bi "Yeah, that's the crucial piece of information."

        "Why kill Stella?":
            bi "Why would he know the motive?"
            jump trial2s

        "How are you so old but so hot?":
            bi "...did I really just think that?"
            jump trial2s
    b "We need to know if Stella died from the stab wound or the shock, Dracula."
    b "Otherwise, even if we learn who set up the wiring, we can't identify the murderer."
    d "Hmm, I can't answer for sure."
    d "But it was pretty likely the shock."
    d "From what I saw, a stab wound in the back like that wouldn't have killed Stella immediately."
    d "Even if Sam stabbed a vital organ, Stella would remain conscious for probably at least 15 seconds."
    d "In contrast, electrocution can kill someone nearly instantly."
    d "The fact that Stella was both stabbed and shocked, and didn't get up once stabbed..."
    d "...suggests the shock killed her before she could act while conscious."
    hide shahar with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "I have a question."
    j "How do we know Dracula and Sam aren't conspiring?"
    j "They spent a lot of time since we got to the mansion talking to each other in private."
    d "Hmph, and what would I have to gain from protecting Sam if I didn't believe there was another murderer?"
    j "I dunno. Maybe you're the Game Master and you know you won't die regardless."
    d "I sure you I am not."
    d "And if I was and wanted to kill you all, why wouldn't I just do it myself instead of through this game?"
    j "Maybe the Game Master is working for someone and has to follow their rules?"
    d "That seems silly, they aren't the Master then, just a Game Servant."
    d "If I must tell you, I was trying to persuade Sam to work with me to get out of here."
    d "But Sam claimed not to trust me since I claimed to be a vampire, so I was mostly trying to prove I was one."
    hide drac with moveoutright
    show sam with moveinright:
        xcenter .75
    s "Yeah, I didn't want to work with him because I thought if I did he would find out I was the murderer."
    s "And talking to him \"in private\" gave me an excuse to not talk to others who might find out."
    s "Plus he talks a lot, so it gave me time to think."
    b "Regardless, I think it's unlikely Dracula and Sam are conspiring for now."
    b "If the Game Master is playing such an active role in setting up a lie..."
    b "I don't think there's any way we solve this case anyway."
    b "Plus, we can't really rely on anyone besides Dracula to explain the state of the body."
    b "So we have to take the chance and trust him."
    j "..."
    j "Okay, I trust you Bert."
    j "So if you trust him, I trust him."
    bi "Jenny trusts me."
    bi "I can't let her down."
    b "Okay, for now our main priority is to figure out who set up the wiring."
    hide sam with moveoutright
    show lauren ind with moveinright:
        xcenter .75
    l "Well that's straightforward, right?"
    l "It's probably Jenny."
    b "Huh?"
    j "Huh? Me again?..."
    l "We found the generator in Jenny's room."
    l "That room also shares a wall with the bathroom, and that wall is the wall where the sink is."
    l "So it'd be easiest for her to set it up."
    b "No, I'm pretty sure the generator got moved there later, we can't blame Jenny based on that."
    b "There's something missing from that room that the murderer would have needed..."
    call screen mansionEvidenceTrial(-1, wires, "trial2u") with dissolve
label trial2u:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "If the generator was in that room when Stella died..."
    b "The wires would have needed to go from the generator to the bathroom."
    l "Well yeah, but the murderer could have just removed the wires later."
    b "No, it's not just that."
    b "When I looked under the sink and saw the wires, they fed into the bathroom through a hole in the wall."
    b "But if you look at the wall of Jenny's bedroom..."
    b "There's no holes in the wall. So there's no way to feed the wires into the bathroom from there."
    l "Hm... that makes sense. Sorry Jenny, looks like I fell for the bait of someone framing you."
    j "It's... okay. I guess I'm used to it now."
    bi "She didn't sound very okay, but that was a topic for later."
    l "I'm confused though. If the generator wasn't in Jenny's room, where was it?"
    b "Well, when you consider that the sink is on the left wall when you enter the bathroom, we can figure that out easily."
    call screen pickSpot3 with dissolve #pick closet
label trial2v:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    b "The generator was in the closet."
    l "The one in the second floor hallway?"
    b "Yeah, that's the only other room that shares that wall with the bathroom."
    j "Wait, isn't that closet locked?"
    j "How could the killer have gotten in?"
    b "I'm not sure. Maybe they found the key before the rest of us and didn't tell anyone."
    b "Maybe they were the first to try opening the closet and locked it from the inside."
    b "But that's the only place that could have a hole in the wall matching the bathroom's."
    b "We've seen every other room and found no holes, so by process of elimination that must be it."
    j "Hm... yeah, I can't think of any other solution for where it could have been."
    show jenny happy:
        xcenter .25
    j "Unless the murderer is a 2D character who can fit between walls!"
    b "Jenny, none of us are 2D characters... we're all real, 3D humans."
    j "I know, I know, just making a joke to ease the mood."
    show jenny ind:
        xcenter .25
    j "For real though, I don't see how it's useful to know the generator was in the closet..."
    j "It's not like anyone's admitted to having access to the closet."
label trial2w:
    menu:
        bi "That's true, but the generator being in the closet still could help us identify the murderer, since..."

        "The murderer moved the generator.":
            b "Yeah..."

        "The murderer had access to wires.":
            bi "This is true, but we didn't need to know the generator was in the closet to figure that out."
            jump trial2w

        "The murderer's capable of moving the generator upstairs.":
            bi "Hmm, that doesn't really rule anyone out besides Freddy."
            bi "Also, that would've been true even if the generator killed Stella from Jenny's room."
            jump trial2w

        "The murderer had access to Jenny's bedroom.":
            bi "That's something we knew before we decided the generator was in the closet."
            jump trial2w

    b "If the generator ended up in a bedroom but it was in the closet when Stella died..."
    b "It must have been moved after Stella died."
    b "So we just need to figure out who moved it between Stella's death and us finding the body."
    show sid ind with moveinbottom
    hide jenny with moveoutleft
    hide lauren with moveoutright
    i "Aha!"
    i "It was Sam all along!"
    i "Sam would be the only person who could move the generator."
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .75
    show sam with moveinleft:
        xcenter .25
    s "No, I swear it wasn't me."
    s "I knew nothing about the generator before a few minutes ago..."
    i "Liar! The murderer would say that too!"
    bi "Yet again, I'm going to have to calm Sid down..."
    $rope = 6
    python:
        startMansionTrial("sid", "Sid: {color=#f00}Sam was the last person to go upstairs{/color} before we found the body.", -1,
        "sid",  "Sid: So if the generator moved after Stella died and before we went up, {color=#55f}Sam is the only one who could have done it.{/color}", 1,
        "sid", "Sid: Sam's in good shape too, so {color=#f00}moving the generator from the closet to Jenny's room wouldn't be difficult.{/color}", -1,
        "sid",  "Sid: C'mon, admit it, {color=#f00}it makes so much sense{/color} that Sam could move the generator so easily.", -1,
        1, rope, "trial2x")
label trial2x:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show sid ind with dissolve
    b "No, actually it doesn't make sense."
    i "Huh? Are you saying Sam is a weakling?"
    i "Sam might have weak morals but morals aren't what lift objects."
    b "No, it's not that, it's the rope we found tied to the generator."
    b "Why would that be there if the murderer could have easily moved it around?"
    b "The generator even has wheels, as long as you can reach the handle you can drag it around upstairs."
    i "So do you think it was someone who couldn't have easily moved it around?"
    i "That means it must be Freddy!"
    show sid ind:
        xcenter .5
        linear 0.15 xcenter .25
    show frog sad with moveinright:
        xcenter .75
    f "M-me? But I'm just a frog..."
    show lauren ind with moveinright:
        xcenter .5
    l "Hey, leave Freddy out of this."
    i "I-I'm just saying..."
    b "No, I don't think it's Freddy."
    b "Because the murderer had to lift the generator up the stairs."
    b "No offense Freddy, but I don't think you could've done that."
    l "Hey, are you saying I helped him?"
    b "What? No, where'd you get that idea?"
    i "I... I don't get it Bert."
    i "Earlier you said the murderer couldn't move the generator from the closet to the bedroom without the rope."
    i "But now you're saying the murderer was able to move it up the stairs."
    i "How can both be true? That just seems like a contradiction."
    b "Hm, it's true they were able to move it up the stairs, but only before the murder actually happened."
    i "What, did they suddenly get weaker once the murder happened?"
    b "No, I think just the circumstances of when Stella died are the key here."
    b "Remember, we know the generator moved after Stella died."
    b "And we don't think it's Sam because Sam wouldn't need a rope to move the generator."
    b "With that in mind, it can only be..."
    call screen chooseCharMansion("catherine", "trial2y", "Who moved the generator?") with dissolve
label trial2y:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show catherine ind with dissolve
    c "Me? C'mon Bert, don't be silly."
    c "I was in the kitchen or dining room for the whole party, how could I move the generator?"
    c "C'mon, Stella's dead, now's not the time for jokes!"
    b "I'm not joking. Maybe you couldn't have directly moved the generator after Stella died..."
    b "But Sesame could have."
    c "..."
    b "It adds up. Sesame was upstairs along with Sam when the murder happened."
    b "After Sam left, Sesame was the only one up there."
    b "You would have been able to move the generator upstairs, but you needed Sesame to move it for you during the party."
    b "Sesame couldn't move the generator without some assistance since, well, he's a cat."
    b "But the rope would give Sesame something to pull the generator with."
    b "For most cats and their owners this wouldn't be possible, but as Freddy knows, Sesame is a very talented and well-trained cat."
    show frog ind with moveinright:
        rotate 315
        xcenter 1.1
        ycenter .5
    bi "Freddy quickly nodded and then started tying his shoes."
    hide frog with moveoutright
    b "I saw him fetch objects for Freddy, he could've easily \"fetched\" the generator to the bedroom."
    c "Fufufu."
    b "Huh?"
    c "That's a good theory Bert. You should try writing a mystery novel if you get out of here!"
    c "But you still haven't explained one thing."
    c "Where could I have gotten the wires from?"
    c "How do you know someone didn't put the wires there later to make it look like the generator killed her?"
    c "Without knowing that, I'd still believe it's Sam's stab wound that killed her."
    bi "Why didn't she bring this up earlier?"
    bi "No, I know why. She's on the defensive. She's grasping for straws to find a way out."
    bi "Luckily, the answer is pretty obvious."
    b "The wires... you got them from..."
    call screen pickSpot4 with dissolve #pick kitchen
label trial2z:
    scene bg mansiondining with fade
    $showchibi("bert", "catherine", "dracula", "freddy", "lauren", "jenny", "sam", "shahar", "sid")
    show catherine ind with dissolve
    b "You got them from the kitchen."
    b "During the party, the microwave and oven clocks weren't working suddenly, but you guys were still able to cook..."
    b "I thought it was kind of weird at the time, but it makes sense if you remember the murderer needed to get wires from somewhere."
    b "Why not appliances lying around the house?"
    b "It also gave the murderer a reason to send Jenny out of the party, setting her up as a potential culprit."
    b "And you, Catherine, spend the last few hours yesterday in the kitchen, and got up early today and went to the kitchen."
    b "If anyone would have had an easy time stealing those wires, it would be you."
    c "..."
    c "That makes sense, but anyone could've woken up in the middle of the night and stole the wires!"
    show catherine ind:
        xcenter .5
        linear 0.15 xcenter .25
    show sid ind with moveinright:
        xcenter .75
    i "No! You mean lady!"
    i "You... you killed Stella, and then made me yell at Sam."
    i "I'll never forgive you. I'm going to prove you did it!"
    bi "Will he? Hm, it's nice to have someone else do the work for once."
    i "Let's go check the rope! If Sesame used it, there must be bite marks or something on the end!"
    c "Wh... wha?"
    b "Hm, that's actually a really good idea Sid."
    c "Bu-but, Sesame used it as a scratching toy!"
    c "Of course there's gonna be marks on it."
    c "C'mon guys, I'm Catherine, I'm always so jolly and perky, how could I kill Stella?"
    i "There could be scratch marks sure..."
    i "But bite marks would look different!"
    b "That's true. They'd be single points and probably come in pairs."
    b "Scratch marks would come in triplets and be longer lines."
    c "..."
    b "And I bet if Sesame needed a chew toy to bite on, you would've said he used it as a chew toy, not a scratching toy."
    b "But you didn't, you've only ever said he could use it as a scratching toy."
    b "Which makes sense, he's a cat, not a dog. That's probably more his thing."
    c "..."
    c "Yeah, you got me."
    b "Huh?"
    c "I... I lost. I won't draw it out anymore."
    show catherine happy:
        xcenter .25
    c "Good job guys! You did great, I didn't think anyone would come close to figuring it out."
    c "I guess I shouldn't have tried to make it look like Jenny did it, otherwise you would've never known it was me."
    c "Silly me as usual!"
    c "Should've spent more time thinking about that and less time thinking about recipes."
    c "Oh well, I didn't live a very honest life. All those houses I burgled, I almost got shot multiple times."
    b "Burgled?"
    c "Oh, yeah, I was a burglar for a living. A cat burglar, if you will, teehee."
    c "C'mon, you really think working in a shelter pays a girl enough to live?"
    c "They barely feed the cats enough to live as is!"
