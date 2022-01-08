label hospitalGo:
    $ftecounter = 5
    blank "TODO: Spicy scene from the past here."
    scene black
    bi "..."
    bi "As I slowly gained consciousness, I resisted opening my eyes."
    bi "Was I a child with no sense of object permanence?"
    bi "Maybe if I don't open my eyes this game won't continue?"
    bi "No, that's not it..."
    bi "I felt more like a student during finals week."
    bi "Exhausted from the first few, knowing I still had more to go."
    bi "Knowing hat the light at the end of the tunnel was very far away."
    bi "Wanting to cling to the relief of my bed, a temporary escape."
    bi "Except instead of exams, I had to solve the murders of people I was..."
    bi "Well, in some cases friends, others acquaintances."
    bi "Regardless, you never really know what death is like until you experience it in person."
    bi "I'm no different than anyone else growing up in the modern age of media and the internet."
    bi "I haven't seen the darkest of what's out there, but I've seen pictures of dead bodies."
    bi "Not willingly always, but I've seen them."
    bi "Didn't faze me one bit."
    bi "But in person? When it's someone you know?"
    bi "The smell, the way it looks like they're sleeping but they're not."
    bi "Feeling like you haven't seen them in a while and then the gut punch of remembering why."
    bi "I don't know how doctors, police, and morticians cope."
    bi "It's something I hope I never get used to."
    bi "..."
    ses "Mrowww!"
    bi "An angry hiss."
    bi "Right, I'm an unwilling cat owner now."
    bi "I found the energy to open my eyes."
    scene bg hosproom1 with dissolve
    $ statusnt("???", "bert", ch=3, sun=0)
    show sesame with dissolve:
        ycenter .61
    ses "Mew!"
    b  "Hey Sesame... sorry, I'm a bit tired."
    ses "Hssss!"
    bi "If I had to guess, he was motioning to the doors of the cell."
    bi "...A cell?"
    $ statusnt("Cell", "bert", ch=3, sun=0)
    bi "Are we in a prison?"
    bi "There's doors on both sides, both in front of me and behind me..."
    bi "I don't think a prison would be like that."
    b "You want me to get us out of here?"
    ses "Hsss!"
    bi "Does he... understand the fact that Catherine's dead?"
    bi "Maybe he thinks I catnapped him?"
    bi "Whatever, that's not important right now."
    bi "I approached one door and tried opening it."
    bi "...it's locked."
    bi "Am I stuck in here? Did I wake up before I was supposed to?"
    bi "...Wait, if everyone's still asleep, maybe I can find out who the Game Master is!"
    bi "Maybe I can escape!"
    bi "Those thoughts quickly faded when I tried the second door."
    blank "Click."
    b "C'mon Sesame, let's go."
    ses "..."
    b "..."
    $cat = True
    bi "Sesame wasn't moving."
    b "Lazy cat, Catherine probably carries you everywhere."
    $mood = "ind"
    b "Fine, I'll carry you around just for now. But don't get used to it."
    hide sesame with dissolve
    bi "I gently picked him up and plopped him in my backpack, scared he might scratch me."
    show bert2 with dissolve
    bi "He was gentler now though. Almost kinda cute."
    bi "Maybe hearing Catherine's name made him think we were going to her."
    bi "Eventually I'll have to get him used to me being his owner but..."
    bi "...until this game's over, there's far more important things to worry about."
    scene black with dissolve
    scene bg hosphall1 with dissolve
    $statusnt("Hallway", "bert", ch=3, sun=0)
    bi "It opened into a hallway."
    bi "There were three other cells in this hallway."
    bi "As I walked past them towards the sound of voices, I noticed they were empty."
    bi "Was I the last one to leave a cell?"
    scene black with dissolve
    scene bg hospcommons with dissolve
    $showchibi("dracula", "freddy", "jenny", "lauren", "sam", "shahar", "sid")
    $statusnt("Cafeteria", "bert", ch=3, sun=0)
    bi "The hallway opened up into what looked like a middle school cafeteria."
    bi "There, I saw everyone else gathered."
    show jenny happy with dissolve
    j "Morning Bert! Morning Sesame!"
    b "Good... morning? Do we know what time it is?"
    j "Nope! But you look like you just woke up from a long nap!"
    b "Uh... where are we?"
    j "Read the sign on the wall dummy!"
    bi "She pointed to where a few of the others were congegrating around a large sign."
    bi "They seemed to be discussing it. I walked over and joined the others around it."
    hide jenny with dissolve
    show lauren ind with dissolve
    l "Oh, hey Bert. How's Sesame treating you."
    b "I... think he thinks I stole him."
    hide lauren ind
    show lauren aw
    l "I mean, you kind of did in a certain sense."
    hide lauren aw
    show lauren ind
    l "Anyway, we were just discussing the rules, you should read them and get up to speed."
    b "Are... are we not going to discuss everything that just happened?"
    b "Catherine and Stella's... passing."
    bi "I said the last word quietly since Freddy was nearby."
    b "All the new info we learned?"
    l "Oh, we discussed that already." #idk how i feel about lauren calling him a sleepyhead LMAO
    l "If you woke up earlier you could've joined us."
    l "But the more pressing thing right now is where we are."
    bi "I turned from the group and looked at the sign."
    hide lauren with dissolve
    blank "Rules of the Latimer Mental Hospital"
    bi "...Mental hospital?"
    bi "I guess... in a demented sense, a mental hospital is like a prison."
    blank "This floor has a guard area and a patient area, separated by cells."
    blank "Every day, two guards will be appointed."
    blank "You will know you are a guard if you wake up and the door to the guard's side of this floor is open."
    blank "Otherwise, the door to the patients' side will be open."
    blank "Every day, there is a daytime period, a twilight period, a nighttime period, and another twilight period."
    blank "Each twilight period lasts 30 minutes."
    blank "After the first day, you may not be in your cell during the daytime period."
    blank "You may not be out of your cell during the nighttime period."
    blank "During twilight, you are allowed to move freely, with one exception."
    blank "No one is permitted to enter the cell of another individual at any time."
    blank "If you are in an area you are not allowed to be in at any time, you will be punished."
    blank "An intercom will announce when each period begins."
    blank "There will be two more announcements when there are 5 minutes of twilight left if someone is in a soon-to-be-forbidden area."
    blank "For example, if daytime starts in 5 minutes and you are in a cell, there will be an announcement."
    blank "Guards are responsible for feeding the patients during the day."
    blank "They may do this however they please, using the kitchen connected to this cafeteria."
    blank "There is a window that can be used to transfer meals and dirty dishes."
    bi "..."
    bi "As if this game wasn't hard enough as is."
    bi "Is the Game Master upset we had a party? Wants to keep us in check?"
    bi "Lauren called out to me from the group she was talking to."
    show lauren ind with dissolve
    l "Finished reading?"
    b "Yeah. It's a lot to process."
    l "Thoughts?"
    bi "I moved to join in on the conversation."
    show sid ind:
        xcenter .175
    show drac ind:
        xcenter .775
    with dissolve
    b "Well, one line sticks out to me."
    b "The fact that the guards are in charge of feeding people."
    b "What if they just don't feed us. Do we starve to death?"
    b "Also, it seems like a guard would never be able to commit murder."
    b "You could only get in touch with the other guard, and if you murdered them..."
    b "Well, we'd all vote for you in a heartbeat since you're the only one who could reach them."
    d "The fact that guards feed us could be the intended mechanism for guards to kill patients."
    l "Why do you say that?"
    d "Think about it."
    d "It will be hard for patients to murder each other, given this seems to be the only common area we have."
    d "That, and we can't enter each other's cells."
    d "A patient murdering another patient would likely have to do it in front of others..."
    d "So despite Bert's argument, it will likely be no easier to commit murder as a patient."
    d "But Bert is right that it is unlikely a guard will try to kill another guard."
    d "So the guards need to somehow be able to kill patients."
    d "They could poison someone's food, or starve someone to death..."
    i "Wait, I don't think starvation would be a good murder method."
    i "Unless someone gets to be the guard multiple days in a row, we could last one day without food."
    i "It sucks but... I've done it before."
    d "Fair. I'm just postulating. We should check our food carefully and such."
    bi "If the mansion is any evidence, I don't think people will stay on guard just because Dracula said to..."
    b "Dracula mentioned this is the only common area for patients. Have you all checked that?"
    l "Yeah, there's a bathroom in here but besides that..."
    l "The only rooms we can access right now are this room, the hallways, and our cells."
    l "It sounds like we won't be able to access the guards' area until tomorrow."
    i "Speaking of one day without food..."
    l "Yeah, don't think we're eating tonight."
    l "Hopefully the announcement for night is soon."
    i "Sleep for dinner..."
    ses "Mew?"
    bi "Oh, right, I have to feed Sesame too..."
    bi "I hope he doesn't hiss at me through the night because he's hungry..."
    b "So um... now that we've discussed the sign can someone catch me up on what you discussed without me?"
    d "If I must..."
    l "I can do it if you don't want to."
    d "Fine with me. I wished to check on Sam anyway."
    hide drac with dissolve
    i "I think I'll go too..."
    hide sid with dissolve
    b "Check on Sam?"
    l "Oh, I guess you and Sam haven't talked yet..."
    l "Take a look."
    bi "I looked over and saw Jenny, Sam, Shahar, and Freddy talking."
    bi "Well, Jenny and Freddy were doing all the talking."
    bi "Shahar was lost in thought."
    bi "...huh? Since when was Shahar the type to get lost in thought?"
    bi "Maybe Stella's death hit him harder than we expected."
    bi "And Sam was... sulking, it seemed."
    l "Sam's overwhelmed with guilt."
    l "I guess attempting to murder someone will do that to you."
    l "You should talk to Sam when you can. I think we really need to get Sam to open up if we can."
    l "As annoying as hearing Sam talk usually is... it's helpful in its own way."
    b "You really think so?"
    l "Yeah. Even if we don't always agree, having persistent people is probably the only way we get out of here."
    bi "I guess there are only eight of us left..."
    bi "Everyone is an even more valuable member of this \"team\" at this point."
    bi "Well, except the Game Master..."
    b "Hey um... why is Jenny taking care of Freddy right now?"
    l "Oh, uh..."
    l "Between you and me, when Dan and Kaiser died, I think the reality of the game hadn't really settled in for me."
    l "I barely talked to them, they both had kind of abrasive personalities."
    l "It was easy to process their deaths by telling myself nothing of value was lost."
    l "And even with Stella's dead, I could tell that lie to myself."
    l "She was nice sometimes, but she was still abrasive, albeit in a different way."
    l "But Catherine..."
    l "I liked her. Or at least, the version of her we knew."
    l "And it made me realize... I could be the next to go."
    l "And if that happens, Freddy needs someone else to rely on."
    l "So I'm trying to trust others to take care of him more than I have."
    b "Makes sense... and Jenny is I guess the next best person to take care of him."
    l "Maybe. But what if she goes too?"
    l "What if it's just Shahar, Sam, and Dracula taking care of Freddy?"
    l "Would any of them even give him the time of day?"
    l "Shahar's too aloof, Sam's not even talking at this point."
    l "Dracula... might suspect Freddy of being the Game Master if he makes it that far."
    b "..."
    b "Lauren, I'm going to live as long as I can in this game."
    b "And I'll make sure that Freddy lives with me too."
    l "That's nice Bert, but how can you possible guarantee that?"
    b "I... I..."
    b "I guess I can't..."
    l "Exactly."
    bi "..."
    bi "Damn. I'd never felt so useless in this game."
    bi "It's easy to feel useful while solving murder mysteries but..."
    bi "Solving them doesn't change the fact that we're dying one by one."
    bi "It just slows down the deaths for a while..."
    bi "Nothing I can do can stop one more person from dying while we're here."
    l "Anyway, we should discuss what we learned from Catherine, like I promised."
    b "...Right, yeah."
    l "So Bert, have you ever met Mr. Sydell?"
    b "No, I don't think I heard of him until we were in the mansion."
    l "Yeah, figured as much."
    l "It seems like the only people who knew him, or at least are admitting to it are..."
    l "Well, Stella, Sam, and Catherine."
    l "Shahar told us what Stella said to you while drinking at the mansion."
    l "About how her company had some lawsuit with him."
    l "So both Catherine and Stella damaged him in some way."
    l "If just Catherine knew him, it wouldn't mean a lot."
    l "It would be about as useful as knowing Kaiser robbed that train."
    l "A fact that seems totally irrelevant to where we are now."
    l "But Stella being an enemy of Mr. Sydell, but not being chosen to murder him..."
    b "You think maybe Mr. Sydell organized this game? To get revenge on all of us?"
    l "Well, Dracula had this theory."
    l "I don't know if I fully agree. After all, Sam just sold drugs to him."
    l "Is that something he would want revenge for?"
    l "I'm not a junkie, but my understanding is he'd feel like Sam was doing him a favor, no?"
    b "Hard to say without knowing more about their relationship."
    l "Yeah, well, Sam's not really talking enough for us to find out."
    b "Another thing... if Mr. Sydell is the Game Master... why isn't he here?"
    b "We were promised the Game Master was one of us."
    l "Dunno. Maybe that was a lie?"
    b "If it's a lie, doesn't that mean we can't win this game?"
    l "Maybe. It wouldn't be surprising to me if that were the case."
    l "This game isn't exactly fair even if the Game Master is here..."
    b "...do we just keep trying then?"
    b "What's the point of all this if there's no Game Master to kill and end the game?"
    l "Hey, maybe this whole Sydell theory is wrong."
    l "And not like we have anything better to do than theorize."
    b "No, don't worry, I'm not giving up just..."
    b "Seems kind of useless to consider that possibility, I guess."
    l "Maybe. It's just a possibility."
    l "Anyway, I sure as hell am not planning to murder anyone here, so it doesn't really help me."
    l "But if you're planning to murder someone, I guess that's the lead we have."
    l "Oh, we're also pretty sure there's gonna be another location-based advantage."
    l "Keep that in mind, when we get to explore the guard's side we might have a guess for what it is."
    l "If we can figure it out it might make solving the mystery easier for all of us."
    bi "She says \"all of us,\" but it's really only been a handful of us doing most of the solving..." #too cocky without others imo
    b "Sounds like a plan. Anything else I should know?"
    l "Not really, that's most of the \"strategy\" stuff we discussed as a group."
    l "There's a lot of emotions running around about Stella and Catherine but..."
    l "Well, I don't want to speak on behalf of anyone emotionally."
    l "Shahar and Sam seem to be the most affected, if you're looking to play shrink to kill some time."
    b "I... wouldn't know what to say to either."
    l "That's fine, I'm not telling you that you have to. Just something to consider."
    bi "...Well, now I feel like she really wants me to."
    b "Thanks Lauren, for catching me up."
    l "No problem. I'm gonna go join the others, ciao."
    hide lauren with dissolve
    bi "I guess even if I can't help them feel better, I should know what's going on..."
    bi "If they're going to be liabilities... no, I shouldn't think like that."
    bi "Let's see, Shahar or Sam..."
    $menuset = set()
    menu samorshahar:
        set menuset
        "Who should I talk to?"

        "Talk to Sam.":
            show sam with dissolve
            s "Oh... hey Bert."
            b "Hey Sam... how are you feeling?"
            s "I don't know, I just tried to kill someone because I thought I had to."
            s "But then I found out I didn't have to, I'm just an idiot."
            s "So now I'm someone who murdered without a good reason."
            s "So what do you think, that I'm feeling fine?"
            bi "Still sassy, even when feeling sad..."
            bi "But I guess it was a dumb question."
            b "Sam... you didn't kill Stella. Catherine did."
            s "I may as well have."
            s "Catherine got lucky that I pushed Stella into her trap."
            s "If Stella's standing one foot to the right when I stab her..."
            s "I'm the one who killed her, and Catherine has nothing to do with it."
            s "Murder isn't a card game Bert."
            s "You don't avoid murdering someone on a technicality."
            s "Even if I make it out of this hellhole, I'm a murderer for the rest of my life."
            s "My mother and father will celebrate holidays with a murderer."
            s "If I want to have kids, they'll be raised by a murderer."
            b "You didn't know."
            b "If you were the designated murderer and Stella was the mastermind, you'd have saved our lives."
            s "Bert, have you ever murdered someone?"
            b "I mean-"
            s "{i}Willingly{/i} murdered someone?"
            b "...No."
            s "Then don't try to act like anything will absolve me of being a murderer for the rest of my life."
            s "We're done talking."
            s "Just avoid me like everyone except Dracula has this whole time."
            s "I'm not worth trying to save."
            s "At best, I'm another warm body that a murderer can kill."
            b "..."
            b "Fine, I'll leave you alone."
            b "But all our lives are on the line here, not just yours."
            b "We're still relying on you to help us escape."
            b "If you're going to feel bad about Stella, don't let that happen to the rest of us."
            s "..."
            s "Whatever."
            hide sam with dissolve
            bi "Well, I guess that's that..."
            bi "Maybe I should try to get Dracula to reach out to Sam."
            show drac ind with dissolve
            d "Can I help you Bert?"
            b "Hey, I'm sure you've noticed but Sam's been feeling kind of down..."
            b "Could you maybe talk to Sam? Try to get through so Sam can help us?"
            d "To be frank, I don't see the point."
            b "What?!"
            d "Bert, you're a fine member of this \"team.\""
            d "One of the few who has worked towards getting out of here."
            d "We have limited time before the murder happens, we should use it wisely."
            d "I'm not very good with emotional matters, as is true of any vampire."
            d "My time would be better spent on problem solving, that's where my strength is."
            d "This emotional stuff, someone like Lauren would be better at it."
            b "Are you sure you can't at least give it one try?"
            b "There must be some reason Sam only really listened to you and not the rest of us."
            d "Fine, I'll talk to Sam, but if I do you owe me a favor in return in the future."
            b "A favor?"
            d "Quid pro quo, Bert."
            b "What kind of favor do you have in mind."
            d "You made me admit things to everyone while we were solving Stella's murder."
            d "Things I was blatantly trying to keep a secret."
            d "I want you to admit your crime to everyone, honestly."
            b "What?"
            bi "My heart started racing quickly, I thought I felt my palms sweat."
            bi "If even thinking about it is elliciting this reaction, then..."
            b "...No, no I can't."
            d "Interesting. Why isn't it worth it?"
            d "Surely it will come out one way or another, when we learn the truth behind this whole game."
            d "Why not rip off the bandage now, so to speak?"
            b "I... now's not the time."
            d "Well it seems we have nothing else to discuss then."
            d "Good day Bert."
            hide drac with dissolve
            bi "...am I really that weak?"
            bi "I can't make a sacrifice for the group?"
            bi "Well, it's too late now. Let me just forget this all happened."
            jump samorshahar

        "Talk to Shahar.":
            show shahar mad with dissolve
            h "Aye lad."
            b "Hey Shahar. Lauren told me you weren't feeling great?"
            h "Aye. I feel like me head is made of the ocean mist."
            b "Wait..."
            b "Because Stella died?"
            h "Oh, that lassie?"
            h "I miss her, but I've lost many compatriots on the sea."
            h "I only knew 'er for nary a week, Bert, it's not like I lost me lover or me parent."
            h "But... I feel like I'm forgetting somethin', lad."
            h "Well, nay."
            h "It's more like... I can't remember somethin'."
            h "I feel like I don't know who I am, lad."
            b "Huh."
            b "You haven't felt this way until now?"
            bi "Because I knew I didn't know who you were the whole time..."
            h "Nay lad. Something about this place..."
            h "It feels like this is a room in a pirate ship I've wandered 'round."
            b "But... it's a hospital."
            h "Aye lad, you can see my confusion."
            h "Pirates don't need hospitals, a lil' scurvy hurt nary a man of the sea!"
            bi "Uh... I don't think that's true."
            bi "Also, this is a mental hospital. Scurvy doesn't get treated here..."
            h "Anyway lad, my head's been hurtin'."
            h "Not just because I can't 'member, lad."
            h "I got a headache like I drank a gallon o' bilge water."
            h "And I'm not much of a thinker so..."
            h "I ain't got any idea what to do."
            b "That's... frustrating. I don't know what to tell you."
            b "Tomorrow let's ask the guards to see if there's any pain relievers."
            hide shahar
            show shahar ind
            h "See lad, that's the kind of thinkin' I need ye fer!"
            bi "Ah yes, the obscure idea of taking medicine to help with a headache."
            b "And maybe we can find out why you think you remember this place if we get out of here?"
            h "Aye lad, maybe. Guess I'll spend what little brain cells I have on that endeavor."
            bi "With that, I left him to think. Or not think, not sure which."
            hide shahar with dissolve
            jump samorshahar
    bi "Having talked to Sam and Shahar, I went to go join the others."
    bi "But a noise interrupted."
    play sfx "audio/ding.mp3"
    intercom "It is now twilight. Please feel free to return to your rooms."
    intercom "You may still roam freely, but remember that you must return to your cell before night begins."
    show jenny ind:
        xcenter .25
    show frog ind:
        xcenter .75
    with dissolve
    j "Well, guess we should all go sleep."
    f "But... I don't wanna. I wanna play!"
    j "C'mon Freddy, we can't stay out here forver."
    j "Plus if you don't sleep now, you'll be tired tomorrow."
    f "F-fine..."
    f "Can I at least sleep in Lauren's room?"
    j "No Freddy, we all have to sleep in our own rooms."
    f "B-but..."
    show frog sad:
        xcenter .75
    f "But I haven't played with her at all."
    f "And I'm scared someone will hurt me in my room."
    j "Don't worry Freddy, no one can go into your room."
    j "Your bed is in the same hall as Lauren's, remember?"
    j "She can pick you up in the morning and protect you."
    f "O...okay..."
    b "Oh, that reminds me."
    b "What's the room arrangement?"
    j "Oh yeah, I guess you were the last to arrive."
    show map3ui with dissolve:
        alpha 0.5
        xcenter .5
        ycenter .5
    j "So there's two hallways, one to the left of the room we're in if you're facing the kitchen."
    j "That one has Lauren, Sam, Dracula, and Froggy, going from furthest to closest to this room."
    j "The one on the right has me, you, Sid, and Shahar, going from closest to furthest."
    hide map3ui with dissolve
    show jenny happy:
        xcenter .25
    j "So you can be a gentleman and escort me to my room, Bert!"
    b "Very smooth. Sure, let's head that way."
    b "Good night Freddy. We'll see you in the morning!"
    f "G-good night..."
    scene black with fade
    bi "We all made our way back to our rooms."
    bi "I had trouble sleeping."
    bi "Mostly because Sesame didn't like the cold floor and instead insisted on laying on me."
    bi "Turns out, she wasn't declawed."
    bi "Which is good, declawing cats is pretty inhumane."
    bi "But so is constantly poking me while I try to sleep."
    scene bg hosproom1
    show sesame:
        ycenter .61
    $statusnt("Bert's Cell", "bert", ch=3, sun=1)
    with dissolve
    bi "After what felt like not sleeping at all, I woke up."
    bi "Well, I was woken up."
    bi "By a sound I hoped I wouldn't get used to."
    play sfx "audio/ding.mp3"
    intercom "Twilight has begun. You must leave your room before daytime."
    bi "I knew if I stayed in bed, I might not make it out of the room in 30 minutes."
    bi "So I begrudgingly got up and tried opening the door behind me, like I had last night."
    bi "..."
    bi "And, it wouldn't move."
    bi "Was I stuck? Am I getting indirectly murdered already?"
    ses "Mew!"
    show sesame with dissolve
    bi "Sesame was standing near the opposite door."
    bi "Right, maybe I'm one of the guards today."
    b "Thanks Sesame."
    scene black with dissolve
    bi "I stepped outside into the hallway."
    bi "Guess it's time to explore."
    scene bg hosphall1 with dissolve
    $showchibint("jenny") #copy paste
    $statusnt("Guard Hallway", "bert", ch=3, sun=1)
    show jenny happy with dissolve
    j "Oh, hey Bert! Hey Sesame!"
    j "Guess we're on guard duty today!"
    b "Oh, nice. I was kind of afraid I'd be paired with someone like Dracula..."
    j "Ha! Nope, just little old me."
    j "Don't get on my bad side though, or I'll have to make up stories about being a vampire to scare you away!"
    b "Please don't."
    j "Don't worry, I wouldn't even know how."
    j "So, whaddya wanna do first?"
    b "I think we have to make food for the others, but twilight isn't even over yet."
    b "So I was thinking we should explore and tell the others what we find."
    j "Sounds like a plan!"
    b "Okay, let's see what's at the end of this hallway..."
    scene black with dissolve
    scene bg hospfancy with dissolve
    $showchibint("jenny") #copy paste
    $statusnt("Guard Lounge", "bert", ch=3, sun=1)
    show jenny ind with dissolve:
        xcenter .5
        linear 0.3 xcenter .75
    j "Huh, what's this?"
    b "It looks like it's a common area for the guards."
    j "It's... so much nicer than the common area for the patients."
    j "A nice lighting fixture, a vending machine, some couches..."
    j "What looks like a window, except it's been boarded up..."
    b "I guess we can relax here after we've fed everyone if we want to."
    b "This kind of reminds me of that study on prisoners and guards though."
    b "Is the Game Master trying to get us to feel like we're better than them?"
    j "Oh that? I'm pretty sure the study was just egged on by the professor in charge."
    j "Crazy guy who more concerned with producing some publishable results than with being humane."
    j "Besides, we'll only be on this side for one day."
    j "Now c'mon, let's look around the room."
    j "We should probably start with these rules..."
    b "Oh god, is there stuff that can get us killed on this side too?"
    j "..."
    j "Hm, no, it's just a repeat of the rules on the other side."
    j "I guess we can't go into the common space for patients."
    j "So it makes sense to give us a copy to read in here."
    b "Psh, reading's boring, I'm tryna check out this vending machine."
    b "Maybe there's some cola in there..."
    b "I like a good classic cola, nothing beats that."
    b "Huh, this vending machine's very... old-timey."
    j "What makes you say that?"
    b "All the bottles are glass. It reminds me of how they package soda in foreign countries."
    b "But I don't think I've seen a vending machine with glass bottles where I'm from."
    j "Hm... I wonder how long ago this building was in use."
    j "Or maybe they just didn't have money to upgrade it?"
    j "Ooh, maybe the Game Master bought this place because they went bankrupt!"
    b "That's... a theory, not sure if we can infer from that, though."
    b "Besides \"The Game Master has money or influence.\""
    show jenny happy
    j "Hey, that's something!"
    bi "I... could've guessed that without seeing this vending machine."
    b "Well, there is cola in here, I'm gonna grab some!"
    play sfx "audio/beep.mp3"
    b "Huh? It's not vending..."
    show jenny ind
    j "Did you pay for the drink?"
    b "Pay? With what? Not like we have money here..."
    j "You could break the vending machine open if you really want to."
    b "That sounds dangerous..."
    b "Don't people die getting crushed by vending machines?"
    j "That's just a risk you'll have to take."
    b "..."
    j "If you get injured, you can use the first aid kit on the wall."
    b "Oh, we should probably check that out, huh..."
    j "Yeah, if someone else dies we can patch up their wounds with it!"
    b "Well... that wasn't what I had in mind."
    b "Just like, we should see if there's poison in here or anything."
    b "If there's a way to poison someone's food like Dracula said, it's probably in here."
    j "Oh. Yeah, I guess that makes sense."
    b "Okay, what do we have here..."
    b "Some band-aids, gauze, pills for treating things like headaches."
    b "A thermometer, gloves, tweezers..."
    b "...Huh, what's medical glue? There's a container of it here."
    j "Never heard of it, what does the bottle say?"
    b "Usage: Closing thin wounds."
    b "Directions: Squeeze the wound shut, then apply glue."
    b "Continue to squeeze wound until glue dries."
    b "Peel glue off in two to three days."
    b "Glue has low melting point. Avoid hot areas while glue remains on wound."
    b "If the glue needs to be removed early, take a towel and dip it in near-boiling water."
    b "Then, apply the towel to the glue. It will melt and the towel will absorb it."
    b "Wash towel afterwards in hot water to remove glue."
    j "I don't understand, why wouldn't you just use a bandage to seal a wound?"
    b "The first aid kit seems kinda old, maybe it's not used much anymore?"
    j "Shouldn't a hospital be keeping its first aid kit up to date?"
    b "Yeah, but a hospital also probably shouldn't be used for a killing game..."
    b "Anyway, doesn't seem like there's much else in here?"
    b "Just some couches we could maybe take a nap on..."
    j "What, did you want to play video games or something in here?"
    b "I mean... I wouldn't say no..."
    show jenny happy
    j "You're so silly."
    play sfx "audio/ding.mp3"
    intercom "There are 5 minutes left in twilight. You must leave your room before twilight is over."
    show jenny ind
    j "Hm, seems like someone hasn't left their room yet."
    b "How do you know that?"
    j "The rules said we'd only hear the 5 minute announcement if someone was still in their room."
    b "Oh, that's true."
    b "I wonder who it is..."
    j "Oh, that probably means we should get working on food."
    j "We didn't eat anything yesterday, people are probably starving."
    blank "Brooorgh."
    j "What was that?"
    b "That... might have been my stomach."
    j "Case in point. I'm going to go to the kitchen, you should feel free to keep exploring."
    j "That way we make the most use of our time."
    b "If you say so..."
    show jenny happy
    j "No worries Bert, I cooked for us once, I don't mind doing it again."
    j "I think this door is to the kitchen, you should get out the other two doors in here."
    b "Sounds good. Thanks Jenny, I'll let you know what I find."
    hide jenny with dissolve
    bi "Alright, let's see what's behind door number one..."
    scene black with dissolve
    $statusnt("Security Room", "bert", ch=3, sun=1)
    scene bg hospsecurity with dissolve
    b "..."
    b "What is this?"
    b "A computer system? This gives me bad flashbacks to the train..."
    bi "I don't know why I talked out loud when it was just me and Sesame."
    bi "Not like he could understand..."
    b "Let's try turning it on..."
    b "Hm, there isn't a login screen like on the train."
    b "Let's see, what's interesting..."
    b "Seems like there's a program they use to store patient information."
    b "Kind of like that program dentists use that stores your history, but it's... well, for a mental hospital."
    b "Then there's a security camera system."
    b "..."
    b "Yup, I can see the cafeteria from here."
    b "Everyone had gathered, Jenny was talking to Sid through the kitchen window."
    b "Hmm, it has an option to look at other rooms, but the button's not working."
    b "It'd be impossible to commit a murder if a guard was just looping through the cameras."
    b "The cafeteria is a hard place to pull off a murder, so it's not really too useful to have a camera there."
    b "The Game Master keeping things fair, I guess..."
    b "There's also a program that controls the utilities in the building."
    b "You can turn off the lights, there's something about cycling hot water through the plumbing system..."
    b "Change the temperature throughout the building..."
    b "Doesn't seem like there's any way to control the cell doors, the nighttime announcement, or anything useful though."
    b "It would be nice if we could roam freely..."
    b "Right now it's just me and Jenny..."
    b "..."
    b "She wouldn't kill me now, right?"
    b "Should I look out for her?"
    b "Anyone could be the murderer, including her..."
    b "No, I need to stop freaking out."
    b "If she killed me here it would be way too obvious."
    b "Plus, it's not like I can do anything about it, I'm stuck on this side with her."
    b "I should focus on being as useful as possible while I'm able to explore this side..."
    b "Speaking of which, time to move on."
    ses "Mew!"
    show sesame with moveinbottom
    hide sesame with moveoutbottom
    bi "Sesame jumped on the controls and then jumped off..."
    b "Huh? This is the program storing patient information."
    b "I guess I should take a look, maybe there's something useful here?"
    b "Maybe I should look for the name Sydell, see if he has a connection to this place too."
    b "..."
    b "No, it's just a bunch of names I don't recognize."
    b "This feels invasive... it's a lot of personal information about people I don't know."
    b "It'd be like looking at strangers' search histories, except it's their mental illnesses."
    b "..."
    b "Huh?"
    b "Why is Shahar's name in the patient records?"
    b "I had to scroll a few hundred lines to find his name. I almost missed it."
    b "Let me check the record..."
    b "..."
    b "His record is almost completely blank."
    b "All it says is \"Patient thinks he is a pirate.\""
    b "Nothing about who Shahar actually is, any contact information..."
    b "Is that the case for the other records?"
    b "Let me check one."
    b "Whoever Howard Eastnuts is, I'm sorry for looking..."
    b "..."
    b "This person has family contact information, a detailed medical history..."
    b "Date of admission, date of discharge, insurance information, prescriptions."
    b "And a bunch more details Shahar's profile here lacks."
    b "Was Shahar's profile inserted to freak me out? Was he actually a patient here?"
    b "Did someone wipe his information before we got here? Maybe the Game Master thought we'd learn too much?"
    b "Maybe Shahar is the Game Master and he's using this as a bluff?"
    b "I should check one more thing, just to be sure..."
    b "..."
    b "Nope, I've tried all of our names. Including Kaiser, Dan, Catherine, and Stella's."
    b "No one in this game except Shahar has a record here."
    b "I should talk to Shahar about this."
    b "This might have to do with his headache."
    b "Well, assuming he's not lying..."
    b "Should I tell the others though?"
    b "On the one hand, if I'm withholding information that makes me look bad."
    b "If this ties Shahar to the location, based on the past two locations doesn't that make him more likely to be the murderer?"
    b "On the other hand, this is Shahar's personal life."
    b "I guess it's not really news to anyone that this whole pirate thing is a bit crazy but..."
    b "If it's a red herring it could be problematic."
    b "Plus, with this few people remaining, it's hard to trust anyone."
    b "..."
    b "I don't think I'll tell anyone except Shahar."
    b "I feel sorry for Shahar... I don't want to give people reason to gang up their suspicions on him."
    b "There's no way the Game Master would make it this obvious who they are."
    b "So I can trust him, right?"
    b "And hopefully this way he can trust me."
    b "I guess I'm done here. Doesn't look like there's any other patients of interest in this program."
    b "Time to go check the other door in the guard common area."
    scene black with dissolve
    bi "I made my way through the common area to the other room."
    scene bg hospcloset
    $statusnt("Supply Closet", "bert", ch=3, sun=1)
    b "Huh, a supply closet."
    b "I guess even a mental hospital needs to get cleaned every now and then."
    b "It's a bit dark in here, let me turn on the lights."
    b "...actually, after reading that sign, maybe I won't."
    b "Don't want to die for forgetting to flip a light switch."
    b "Let's see. There's a box of small unzippable plastic bags on the top shelf, fairly standard."
    b "Maybe they use those to distribute medicine here?"
    b "The second shelf has a variety of cleaning supplies."
    b "Ammonia, bleach, ethanol, hydrogen peroxide..."
    b "All fairly standard stuff. I guess a mental hospital has less biohazards than a medical hospital."
    b "Below that, there's a stepstool. Maybe for maintenance workers?"
    b "And... a baseball bat."
    b "That's not ominous at all..."
    b "Should I hide it? It's such an obvious choice for a murder weapon."
    b "No, there's a rule that says it needs to be returned here."
    b "I don't really want to be the one to test if hiding it gets me \"punished\"..."
    b "I guess... I'll just leave it here and let the others know so we're all vigilant about it."
    b "It can be like the kitchen knife in the mansion. If everyone's keeping an eye on it it's not a threat."
    b "I think that's all I have to explore here, time to head to the kitchen."
label testwindow:
    scene black with dissolve
    scene bg hospkitchen with dissolve
    $showchibiwindow(["jenny"], [])#copy paste
    $statusnt("Kitchen", "bert", ch=3, sun=1)
    show jenny happy with dissolve
    bi "As I entered the kitchen, I looked through the window to the cafeteria, just to make sure..."
    $showchibiwindow(["jenny"], ["dracula", "sid", "shahar", "lauren", "freddy", "sam"])#copy paste
    with dissolve
    bi "Phew, no one's been punished yet..."
    bi "They were all there."
    j "Hey Bert, what'd you find?"
    b "Well, there's what looks like a control or security room."
    b "Giant computer, can look at the cafeteria from there."
    b "And some archives from this place."
    bi "I shouldn't tell her about Shahar..."
    b "Nothing too interesting though."
    b "And then there's a closet with various cleaning supplies."
    b "I hope we won't have to use them..."
    b "Oh, and a baseball bat."
    show jenny ind
    j "A baseball bat?"
    b "Yeah... not sure why a mental hospital has a baseball bat in a supply closet."
    j "I can uh... think of some not-so-great reasons."
    b "Oh."
    b "Ohhhhh. This place just got a lot darker."
    j "Should we take the bat and put it somewhere where everyone can see it?"
    b "There's a sign in the closet that says to return everything... I'm afraid if we move it we get punished."
    b "After all, there was a punishment for not following the rules in the cafeteria."
    j "That sucks. Well, guess we'll just tell everyone."
    b "How's cooking going?"
    j "It's okay. This kitchen is not nearly as well stocked as the mansion was."
    j "The fridge only has the bare minimum, basic veggies like tomatoes and onions, a few broths."
    j "The pots and pans are huge though, I guess because they're used to cooking for a large group."
    j "So I'm cooking a big pot of tomato soup right now."
    j "Nothing too fancy but that's about all I know how to do."
    b "Can't say I have any fancier ideas..."
    b "Anything I can do to help?"
    j "Hmm, actually, do you mind if I explore a bit now that you're here?"
    j "You'd just need to stir the pot every now and then, I can try to be back before it's done cooking."
    b "Sure, this would be a good chance for me to catch up with the others anyway."
    show jenny happy
    j "Thanks Bert! Just to be safe, if it feels like 20 minutes have passed since I've left turn off the stove then."
    b "Got it, let me know if you find anything I missed."
    j "Will do, seeya Bert!"
    hide jenny
    $showchibiwindow([], ["dracula", "sid", "shahar", "lauren", "freddy", "sam"])#copy paste
    with dissolve
    bi "I guess I haven't talked to the others yet..."
    bi "I turned to the window and started chatting with the first person I saw."
    scene bg hospkitchenwindow
    show hospwindowoverlay
    show drac ind at inwindow behind hospwindowoverlay
    $showchibiwindow([], ["dracula", "sid", "shahar", "lauren", "freddy", "sam"])#copy paste
    with dissolve
    d "Hello Bert. Are you here to brief us on the other side?"
    b "Uh... I guess I can, yeah."
    d "Let me gather the others then, so you don't have to reexplain anything."
    hide drac with dissolve
    show frog ind at inwindow behind hospwindowoverlay with dissolve
    f "Bert! Are you okay?"
    b "Oh, hey Freddy. Yeah I'm fine."
    show frog sad
    f "I got worried because Jenny showed up but you didn't."
    f "And I thought... well..."
    bi "Freddy sounded like he was on the verge of tears."
    bi "Despite us trying to keep death away from him, he might have been thinking about it as much as the rest of us."
    bi "Though maybe he didn't grasp how obvious it would be if Jenny murdered me on the first day..."
    b "I'm here Freddy, don't worry!"
    show frog ind
    f "Oh. Okay. Is the food almost ready?"
    bi "Children really are whimsical."
    show frog ind:
        xcenter .5
        linear 0.15 xcenter .25
    show drac ind at inwindow behind hospwindowoverlay:
        xcenter .75
    with fade
    bi "Dracula had gathered the others, except for Sam, and returned to the window."
    d "Bert, you may begin your explanation."
    b "Alright..."
    bi "I briefly told them about the common area, control room, and supply closet."
    f "Baseball bat? Can we play sports in here?"
    b "I uh... didn't see any baseballs or anything like that in here."
    f "Oh. Maybe we can find one!"
    d "Hush child, there are business matters to discuss."
    d "So you say you're afraid to take the baseball bat out of the closet?"
    b "Yeah, there's a sign saying to return everything."
    b "I don't want to find out if breaking that rule kills me like the other rules."
    d "It seems unlikely, you could just try taking it out and see what happens."
    bi "Easy for you to say when you're on the other side..."
    d "So there was no information in the control room of use?"
    b "Nothing I saw, no. Though there are a lot of patients in the records so I didn't scroll through them all."
    bi "That should cover my bases..."
    d "Perhaps if you feel like helping the group, you could sift through the records with the rest of your free time today?"
    b "Uh..."
    hide frog with moveoutleft
    show lauren ind at inwindow behind hospwindowoverlay with moveinleft:
        xcenter .25
    l "Don't make him waste his time, you've done enough for him already Bert."
    l "If you really wanna know, you can check on your own time Dracula."
    d "Hmph. Fine."
    b "By the way, I heard the 5 minute reminder get announced this morning..."
    b "Did everyone make it out of their cells in time?"
    l "Yeah, we had to do some... convincing to get Sam out of bed."
    b "Is Sam doing any better?"
    l "Not really. Mostly just sitting in the same seat."
    b "That's... a little concerning, to put it lightly."
    l "Yeah. Don't worry about it for now, not much you can do on that end."
    l "By the way, where's Jenny? Isn't she prepping a meal right now?"
    bi "Shoot!"
    b "Uh... yeah, I gotta go take care of that."
    b "We'll let you guys know when it's ready."
    hide lauren
    hide drac
    with dissolve
    scene bg hospkitchen with dissolve
    bi "I turned to the soup and started stirring it."
    bi "After about 10 minutes, Jenny returned."
    show jenny happy with dissolve
    j "Hey Bert! Everything okay here?"
    b "Yup! Was definitely sitting here making sure nothing burned the whole time!"
    show jenny ind
    j "...You're acting suspicious."
    b "Okay, I may have not stirred the soup until a few minutes after you left."
    j "Bert, it's tomato soup. Not a steak or anything like that."
    j "Worst case we just don't serve the burnt soup at the bottom."
    j "As long as Sesame didn't vomit in the soup or anything like that."
    b "Oh shoot, I totally forgot about Sesame!"
    bi "I quickly scanned the room to locate him."
    bi "Thankfully, Sesame was just curled up on one of the tables sleeping."
    bi "I guess cats are known for sleeping a lot..."
    b "Did you find anything?"
    j "Nope. I thought about looking through the records but then I decided it was too boring."
    j "Besides, I'm sure if there were something interesting you would have found it."
    show jenny happy
    j "Oh! But there is something secret in here!"
    b "What?"
    j "Check the fridge, second level from the top."
    bi "I opened the fridge and found..."
    bi "A cupcake."
    bi "Red velvet with what looked like cream cheese frosting..."
    show jenny ind
    j "There were two when I found them but uh..."
    show jenny happy
    j "Well, one of them magically disappeared!"
    bi "A likely story."
    j "Anyway Bert, you should have the other one."
    j "No one else will know, unless the next guards dig through the trash."
    j "And you deserve a reward for all the hard work you've put in!"
    b "Jenny... I don't know, it feels like I'd be lying to the others out there."
    b "Shouldn't we try to build trust instead of hiding something from them?"
    show jenny ind
    j "It's just a cupcake Bert, it's not a big deal."
    j "It's not like hiding our pasts or how we're criminals."
    j "You're making me feel bad for having a giant sweet tooth..."
    b "No, I'm not trying to make you feel bad!"
    bi "I hate these types of scenarios."
    bi "Where you don't personally feel like you could do something but can understand why others do."
    bi "Like being the vegetarian friend who watches their friends eat meat."
    bi "Or not caring much about social media but your friends are upset when you don't like their posts."
    menu:
        "What should I do?"

        "Eat the cupcake":
            $eat = True
            b "Okay, you're right, it's not a big deal."
            b "And I have been \"carrying the team\" so to speak."
            b "Besides, for all we know the Game Master will restock the fridge tonight."
            bi "I didn't actually believe that, but I said it to make her feel better."
            show jenny happy
            j "Yay! Dig in Bert, you deserve it!"
            bi "I unpeeled the wrapper and started biting into the cupcake."
            bi "I won't lie, if only for a split second, the taste of frosting made me feel happy."
            b "Oh Jenny, I never talked to you about the whole Mr. Sydell thing."
            b "I take it you never met him?"
            show jenny ind
            j "Nope, haven't heard the name until now."
            j "Do you know anything, Bert?"
            b "I don't, but Stella told me something while we were in the mansion."
            b "She said something about how she \"hires suits to step on guys like him.\""
            j "...What does that mean?"
            j "..."
            j "Oh! I remember once seeing on TV something about how Cantoire Holdings sued a smaller company."
            j "They failed to fulfill an order by one of their clients owned by Cantoire Holdings."
            j "So Cantoire Holdings sued them."
            j "They won the lawsuit, and the smaller company couldn't pay out so they went bankrupt."
            j "Do you think that's what she meant?"
            b "Maybe... do you think Mr. Sydell owns a company like that?"
            j "No clue. But it would make sense."
            j "Maybe this whole game is orchestrated by him as revenge on Stella?"
            j "If he owns a company he would have the money to put together something like this."
            b "Why are the rest of us here though?"
            b "Not like I helped Stella take down any company..."
            b "I'd never met her before this happened."
            b "And now Stella's dead, couldn't the game just be over."
            j "Hm... maybe this theory is wrong then?"
            b "Maybe. There's other ways to be rich enough to host this kind of game and be upset at Stella."
            b "I'd imagine many people in the world are already upset at a CEO like Stella anyway."
            b "For all we know this is some vigilante justice against random criminals with no connection..."
            j "I don't think it's a coincidence Mr. Sydell keeps coming up though."
            b "You're right, I'm just... speculating, I guess."
            j "Oh, looks like the soup is almost done!"
            j "Want to help me serve it, Bert?"
            b "Yeah, let's do it."
            jump postcupcake

        "Tell the others about the cupcake":
            $eat = False
            b "Sorry Jenny... I think I'm going to tell the others about it."
            b "See if any of them want it more than I do."
            j "Bert... they're all going to hate me if they know I ate it without telling them!"
            b "If you want I won't tell them you ate one. I'll just say there was only one."
            b "I don't think they'll have a reason to think we're lying if I give them one cupcake."
            j "Hmph. Okay."
            bi "She turned away from me and stirred the soup."
            bi "I think she was upset, but I don't feel like I did anything that merited it..."
            bi "We sat there in silence, her cooking, me staring at the wall, until she was done."
            bi "Well, hopefully this will blow over soon."
            bi "Time to serve the meal..."
            jump postcupcake
label postcupcake:
    bi "Hm... I should try to find a way to talk to Shahar discreetly while everyone's eating."
    j "Food's ready!"
    bi "The others gathered in a line to get their serving."
    scene bg hospkitchenwindow
    show hospwindowoverlay
    show jenny ind:
        xcenter .25
    with dissolve
    show sid smile at inwindow behind hospwindowoverlay with moveinright
    i "Oh wow! This smells delicious!"
    j "You don't need to flatter me Sid. It's really simple compared to our last meal..."
    i "Technically we had sleep for dinner yesterday."
    show jenny happy:
        xcenter .25
    j "I'm sure when you're a guard you'll make something even better Sid."
    i "Hmm, I only know how to make very simple stuff..."
    show sid ind behind hospwindowoverlay
    i "We didn't have a very stocked kitchen when I was growing up."
    i "Sometimes we just got fast food because my parents were too tired from working to cook..."
    j "Hm... well now's just as good a chance as any to learn to cook!"
    j "When we get out of here, it's a really useful skill to have."
    i "I guess so..."
    j "Plus, you can impress the ladies!"
    i "Um... you're being weird, Jenny."
    show jenny ind:
        xcenter .25
    j "Oh."
    j "Never mind then..."
    hide sid with moveoutleft
    show shahar ind at inwindow behind hospwindowoverlay with moveinright
    h "Aye lassy, what rations have ye prepped for us?"
    h "My head's achin', some food ought to get me metabolism back in check."
    j "Tomato soup, here you go."
    h "Ah, this reminds me of the soup me mateys would prep on the ship."
    h "The smell's almost the exact same!"
    b "Do they stock tomatoes on pirate ships?"
    b "Seems like they would spoil at sea, I thought pirates mostly ate dry food."
    h "I don't know lad, I ne'er went into the ship's kitchen."
    h "Can't defend against buccaneers if yer stuck in there, and I was the strongest man on the ship."
    bi "Like everything Shahar said, this didn't make a lot of sense, but..."
    bi "Shahar's head hurt and he got upset last time I kept questioning him."
    h "Anyway, cheers lassy, I'm off to feast!"
    hide shahar with moveoutleft
    show lauren ind at inwindow behind hospwindowoverlay:
        xcenter .5
    show frog ind at inwindow behind hospwindowoverlay:
        xcenter .75
    with moveinright
    j "Hey guys, here's your soup!"
    l "Thanks."
    f "Thanks! I'm so hungry..."
    l "Apparently Freddy growing up had a bunch of fruits to snack on."
    l "There doesn't happen to be any in the kitchen for him, is there?"
    j "I didn't see any..."
    show jenny happy:
        xcenter .25
    j "Except tomatoes! They're technically fruits!"
    j "So this soup is like a smoothie if you think about it!"
    b "..."
    l "..."
    f "..."
    bi "I don't think that was a very convincing argument."
    l "Sorry Freddy, but this is at least healthy for you."
    l "We'll need all the energy we can get, right?"
    f "Yeah... I am tired..."
    if not eat:
        bi "Hm... wait."
        bi "I think Freddy would really like this cupcake."
        bi "It probably won't give him actual energy, but..."
        b "Hey Freddy, do you want a cupcake?"
        b "We found one in the fridge, you should take it."
        b "We're all old adults, so we don't appreciate sweet food as much as you do."
        show jenny ind:
            xcenter .25
        bi "Jenny turned away as I was saying this."
        f "Cupcake?"
        b "Yeah. It's all yours."
        f "Wow. Thanks so much Bert!"
        l "Alright Freddy, let's save that for dessert, finish your soup first."
        f "But I wanna eat the cupcake!"
        l "If you eat it first you'll ruin your appetite..."
        l "Thanks Jenny and Bert. Looking forward to the meal."
        show jenny happy:
            xcenter .25
        j "You're welcome!"
    else:
        l "Thanks Jenny. Looking forward to the meal."
        j "You're welcome!"
    hide lauren
    hide frog
    with moveoutleft
    show drac ind at inwindow behind hospwindowoverlay with moveinright
    d "I am looking forward to this tomato soup."
    j "Really?"
    d "Yes, it reminds me of blood."
    d "A bit more orange than blood is, but still."
    d "It gives me some nostalgia for before this game."
    bi "I highly doubt any vampire actually thinks tomatoes look like blood..."
    d "Good day."
    j "Good day, Dracula!"
    hide drac with moveoutleft
    show jenny happy:
        xcenter .25
        linear 0.15 xcenter .5
    b "...wait, there's an extra serving."
    b "Has anyone not come up yet?"
    j "I think it's Sam."
    b "Oh..."
    bi "I hadn't noticed, but Sam hadn't even come to the windows like the others."
    bi "Sam was instead sitting in the same seat, staring at the ground."
    b "Sam needs to eat... maybe we can call Lauren over to help us help Sam?"
    j "Do you mind taking care of that Bert?"
    j "I think Sam takes you more seriously than me, and I wanted to clean up the kitchen."
    b "Uh... yeah, I guess Lauren and I are enough to help Sam out for now."
    j "Sweet! I'm gonna go to the supply closet and choose a cleaner, if you need me."
    j "Seeya Bert!"
    hide jenny with dissolve
    bi "That's... moderately suspicious."
    bi "The kitchen's not that dirty, and it's not like we'll be here that long..."
    bi "Oh well, I have a slightly more important thing... er, person to worry about."
    b "Lauren! Can you come here?"
    show lauren ind at inwindow behind hospwindowoverlay with moveinright
    l "Hey Bert, something wrong?"
    b "Sam never came to grab a bowl of soup."
    b "Can you help me bring Sam here to eat?"
    l "Sure, give me a second."
    hide lauren behind hospwindowoverlay with moveoutright
    bi "Lauren went over and somewhat forcefully got Sam to stand up and walk to the kitchen window."
    show lauren ind at inwindow behind hospwindowoverlay:
        xcenter .33
    show sam at inwindow behind hospwindowoverlay:
        xcenter .66
    with moveinright
    s "What do you want..."
    b "We wanted you to eat your meal."
    s "What's the point..."
    b "Sam, you need to eat."
    s "I'm not hungry..."
    b "It's soup, it'll go down effortlessly. We need calories in you so you can keep going."
    s "Why are you all trying to keep a murderer alive..."
    l "Sam, you're not a murderer."
    s "I might as well be."
    l "Sam, take it from someone who actaully murdered someone."
    bi "..."
    bi "What?"
    bi "This is news..."
    s "...You murdered someone?"
    l "I don't want to go into details."
    l "But I once was in a dangerous situation in public with a robber."
    l "I had a gun on me, and I thought my life was at risk, so I..."
    l "I took three shots."
    l "I still don't know if that was the right move, I never will."
    l "Two hit the target."
    s "..."
    s "Why are you telling me this?"
    s "Murdering a criminal is different from murdering a stranger."
    l "{i}Two{/i} hit the target."
    l "One hit a girl I didn't know."
    l "She died."
    l "Thankfully based on security footage I wasn't taken to court."
    l "I got to live an \"innocent\" citizen."
    l "But it took me a long time to move past that day."
    l "Every day I woke up and I'd see her face."
    l "Every night when I tried to sleep I heard her scream."
    l "About a year after it happened, someone came to our place."
    l "It was the girl's parents."
    l "The mother was there when she got shot, the father wasn't."
    l "He said at first he was angry."
    l "Wanted to press charges, send me to jail, ruin my life."
    l "But he said he didn't feel right blaming me."
    l "Knew I was someone else's daughter, who happened to be caught near a bad guy."
    l "In another world, I was the one who got shot by accident by his daughter."
    l "So he said he forgave me. And asked me to forgive myself."
    l "I never heard from him after that."
    l "I don't think I've fully forgiven myself for what happened that day."
    l "I'm not convinced her father really ever forgave me either."
    l "That he wasn't just saying what he felt was right to say."
    l "But... I'm getting there."
    l "I have no choice but to try to get there eventually."
    l "Thanks to me... no, thanks to that robber, the girl lost the chance to live her life fully."
    l "I won't let him be the reason I don't live mine fully as well."
    s "..."
    bi "Without a word, Sam took a bowl of soup and went to go sit and eat."
    hide sam with moveoutright
    show lauren ind at inwindow behind hospwindowoverlay:
        xcenter .33
        linear 0.15 xcenter .5
    bi "..."
    bi "I don't know what to say."
    l "You don't have to say anything."
    b "Huh?"
    l "That was some heavy shit. I wouldn't know what to say either."
    l "If anything it'd be worse if you had something to say."
    l "That'd mean you've been through your own desensitizing shit too."
    l "There's a reason I haven't brought it up till now."
    l "Just... don't mention it around Freddy, okay?"
    l "At this point I don't care if the others know."
    l "I just want to get out."
    l "I decided that while we were waiting for food."
    l "I've never felt so powerless in here until then."
    l "Just sitting in a single room, nowhere to look around, can't even feed my damn self."
    l "Even if it means getting judged for my past, who I am, I don't care."
    l "Some of them will probably think I'm no better than the Game Master for having killed a kid."
    l "Hell, you might be thinking that right now."
    l "I wouldn't blame you if you did. I kind of still think that."
    l "But... if Freddy knows, I don't think he'll feel safe around any of us."
    l "If we're going to get out, a crying untrusting Freddy isn't going to help."
    b "Um... yeah."
    b "Lauren?"
    l "Yeah?"
    b "Thanks. You went above and beyond, you didn't have to do that."
    l "Bert, what are we all doing here? Solving these murders and trying to figure out who the Game Master is?"
    b "Uh... we're trying to get out?"
    l "Sure, but more than that. We're trying to save each other."
    l "That includes Sam. As annoying as Sam is, or at least was..."
    l "Sam has parents, family, friends outside of here too."
    l "If it means becoming the pariah of this group instead of Sam..."
    l "I'll make that trade to give Sam a chance to get out of here."
    b "..."
    l "..."
    bi "I should've said something, but I didn't."
    bi "Taking that as a cue, Lauren walked off."
    hide lauren with moveoutright
    scene bg hospkitchen with dissolve
    show jenny ind with dissolve
    j "Hey Bert, I'm gonna start cleaning the kitchen up."
    j "You don't have to do anything, I enjoy cleaning!"
    j "It might be a good time to talk to the others if you haven't already."
    j "There's some time to go until we have to make another meal, have to kill that time somehow."
    b "I'd talked to Lauren and Sam, but I guess I could talk to them more or talk to someone else."
    hide jenny ind with dissolve
    blank "FREE TIME 5 HERE"
    show jenny ind with dissolve
    j "And, all done with cleaning!"
    j "I'm gonna go relax in the lounge, Bert."
    b "You don't want to talk to the others?"
    j "No, I'm pretty tired. Plus, I need to figure out what's for dinner..."
    j "If you want to join me feel free, but I'm fine being alone for a bit."
    show jenny happy
    j "Just don't kill me while I'm there! That'd be too obvious."
    b "Haha, I'd never do that..."
    bi "Forget Freddy, does Jenny comprehend how serious this situation is?"
    hide jenny with dissolve
    bi "Hm... this is my chance, I think."
    scene bg hospkitchenwindow
    show hospwindowoverlay
    b "Hey Shahar, can I talk to you for a second?"
    show shahar ind at inwindow behind hospwindowoverlay with dissolve
    h "Mate, what's on yer mind?"
    b "I wanted to tell you something."
    b "I think we should keep it a secret though. It's something that might make you look suspicious."
    bi "Well... more suspicious than the pirate getup already does."
    h "Suspicious? Lad, what would ye landlubbers suspect me for? Being a pirate? I am one!"
    b "Shahar, did you figure out if you've ever been here before?"
    h "Ye lad, I was in the cafeteria yesterday. What's yer point?"
    b "No, that's not what I meant..."
    h "Well then be clearer lad, else nary a soul here will understand ye!"
    b "I mean... have you been here before the game started?"
    b "In the hospital?"
    h "I... I feel like I have lad, but me memories of here don't exist."
    h "Like what ye landlubbers call... deja vu?"
    b "Okay, Shahar don't tell anyone this."
    b "But... I scrolled through the hospital records, and your name was in there."
    h "..."
    b "So I think you've been here before, it's not just deja vu."
    h "What did it say lad? What can't I remember?"
    b "It only said \"patient thinks he is a pirate,\" nothing else."
    b "It's almost like someone wiped most of your information."
    h "\"Thinks he is a pirate?\""
    show shahar mad at inwindow behind hospwindowoverlay
    h "Lad, I think I'm a pirate because I am a pirate!"
    h "How can I trust ye lad, ye might be thinkin' I'm an addle you can swindle and kill."
    b "Trust me?"
    b "..."
    if eat:
        bi "No, he's right."
        bi "I thought we could trust Catherine in the mansion, but I was wrong."
        bi "Shahar might feel the same way towards me."
        bi "I could ask others to check the records so he knows I'm not lying but..."
        bi "Then the others might not trust him."
        bi "Trust for trust..."
        bi "This isn't important enough to get Shahar potentially lynched by the others..."
        b "Yeah, you're right Shahar."
        b "Sorry to bother lad."
        h "Aye lad."
        hide shahar with dissolve
        bi "He stormed off..."
        bi "That didn't go as planned."
        bi "Was there anything I could have done to convince him to trust me?"
    else:
        b "Shahar, earlier, I gave Freddy a cupcake."
        b "I could have just eaten it myself and told no one about it..."
        b "But I didn't want to lie to people about it."
        b "Even if it was a lie by omission."
        b "If I wouldn't lie about something trivial like that, would I lie to you about this?"
        h "..."
        h "Bert, me head don't work as good as it used to."
        h "And it didn't need to work that good for me to be a pirate."
        h "I don't know me a lot, but..."
        h "Somehow I know I can trust ye Bert."
        h "The way ye speak, I can tell yer a true comrade."
        h "Yer keepin' this a secret fer me Bert, I appreciate that."
        h "So I'll tell ye something too, but ye must keep it a secret."
        h "Not that I think ye won't..."
        h "If ye wanted to maroon me, the others would've known I've been here by now."
        b "Of course, Shahar. Your secrets are safe with me."
        h "I... think you're right. I only think I was a pirate."
        h "In my pirate memories... something is weird."
        h "The others tell me to shut up, that I'm sitting at a table, not a crow's nest."
        h "I was the captain, why would I shut up?"
        b "Did you think they didn't realize it was a crow's nest?"
        h "I... I thought maybe me mateys were using pirate words I hadn't heard of."
        h "Like how ye landlubbers don't know what cackle fruit is."
        h "Maybe table means crow's nest?"
        h "That's what I thought. But like I said Bert, me head didn't need to work that good as a pirate."
        h "Should I even talk like this if I'm not a pirate, matey?"
        h "Should I just call you... pal?"
        b "..."
        b "Keep calling me matey, Shahar."
        b "The Shahar I know is a pirate. And if you're not a pirate, I don't know what you are."
        b "And I don't think you do either."
        h "Yer right matey. I remember nothing before me pirate days."
        h "Thanks Bert. Yer a real matey."
        hide shahar with dissolve
        bi "If only we knew what made Shahar this way..."
        bi "That might be an important clue. Maybe it would help him remember his past."
        bi "For now, I think this is enough."
        bi "I guess I already kind of knew when I read the records, but now I feel more sure."
        bi "Something... or someone, made Shahar think he was a pirate, and he was admitted here."
        bi "It's nowhere near figuring out who the Game Master is, but..."
        bi "It's progress."
    bi "After Shahar left, I left the kitchen."
    bi "No one seemed to keen to talk through the window, understandably."
    bi "So might as well talk to Jenny with no windows involved."
    scene black with dissolve
    scene bg hospfancy
    $showchibint("jenny")
    with dissolve
    show jenny happy with dissolve
    j "Hey Bert! Guess what I found?"
    b "A way out?"
    show jenny ind
    j "Oh... no, you're gonna be disappointed if you expected that."
    b "I was joking."
    j "Oh."
    show jenny happy
    j "Good old Bert, always a jokester!"
    j "But no, I found a chess set!"
    j "It was tucked under one of the couches, I guess we didn't search this room deeply enough."
    j "You wanna play a round to kill some time?"
    $mood = "happy"
    b "Yeah, I'm down."
    b "Feels like everything's been sad since we got here, a game would be a nice change of pace."
    bi "I'm a beast at chess, Jenny better be ready."
    hide jenny with dissolve
    show bg jennymonikaind with fade
    bi "..."
    $mood = "ind"
    bi "....."
    $mood = "sad"
    bi "Hm, a few moves in she's way better than I expected."
    j "Do you play much Bert?"
    j "You're pretty good."
    $mood = "ind"
    b "I used to play online in my free time in college."
    b "And you?"
    j "Oh, I was a tournament player in high school."
    j "Everyone needs a hobby, right?"
    bi "Tournament player? Jeez, maybe I'm outmatched."
    b "How well did you do in tournaments?"
    j "I made top five in the state for high schoolers."
    bi "Yeah, I'm outmatched."
    bi "Let's see... should I play a safe move or try something weird?"
    bi "If she's better maybe she won't expect the deviation?"
    $goodmoves = 0
    menu:
        "Play a safe move":
            bi "I stuck with the usual way this opening played out."
            j "You're playing pretty solid for someone who doesn't go to tournaments!"
            b "It's only the first few moves..."
            b "I feel like once you play enough games you know what works."
            j "Hmm, I guess that's true when we're playing something like an Italian Game."
            j "Maybe I should have chosen a more obscure opening to throw you off."
            b "No please."
            $goodmoves = goodmoves + 1
            jump chess1

        "Try a weird deviation":
            bi "I moved my f-pawn forward to protect a piece."
            j "..."
            j "Interesting..."
            bi "Did it catch her off guard?"
            j "That was an unusual move Bert, did you think it through?"
            bi "She moved a bishop in response."
            bi "Oh..."
            bi "She had pinned my knight since the pawn wasn't in the way..."
            bi "And if I try to protect it she can threaten it with a pawn next turn..."
            bi "Looks like I blundered."
            jump chess1
label chess1:
    bi "We played a few more moves..."
    bi "Hmm, okay, it's midgame, our rook pairs are protecting each other."
    bi "We both have one on the open e-file, I could force a rook trade here..."
    bi "Or just let them awkwardly stare at each other and make a move elsewhere."
    bi "What should I do?"
    menu:
        "Trade rooks":
            bi "I captured her rook, and she captured mine back."
            bi "Okay, now let me move my knight onto the e-file."
            $mood = "shock"
            bi "...wait, her rook is on the file now and mine isn't."
            bi "I think that trade just gave her free control of the file..."
            j "Frustrated?"
            $mood = "ind"
            b "Yeah, I don't think I should have made that trade."
            j "It's a common mistake, don't worry."
            jump chess2

        "Move a different piece.":
            $goodmoves = goodmoves + 1
            bi "Nah, I can take some space with my knight in that file."
            show bg jennymonikablush
            j "Ooh, that's a good move Bert."
            j "I'll have to think about this next one..."
            show bg jennymonikaind
            bi "She was complimenting me, but I was still losing slightly..."
            bi "I guess I'm holding up okay for our respective skill levels though."
            jump chess2
label chess2:
    bi "We kept playing, slowly narrowing down to endgame..."
    if goodmoves > 1:
        bi "She was threatening to back rank mate."
        bi "...Wait."
        bi "I think I see a mating sequence."
        bi "I could win this game!"
        bi "I haven't thought this through, but I should go for it, right?"
        menu:
            "Go for mate":
                bi "I made a bold sacrifice to open up her king."
                $mood = "happy"
                bi "Yes, it's going exactly as I planned."
                bi "Just one move and I win!"
                b "Aha!"
                j "Huh?"
                b "I won! Checkmate!"
                $mood = "shock"
                j "Bert... my bishop can capture your queen."
                j "When you moved your pawn my bishop started protecting that square."
                j "It was a good try though!"
                $mood = "ind"
                jump chess3

            "Stop her back rank mate":
                $goodmoves = goodmoves + 1
                bi "No, she's way too good a player."
                bi "She definitely would've seen it if I could win in three moves, right?"
                bi "I pushed a pawn that was next to my king, to at least last one more move..."
                jump chess3
label chess3:
    if goodmoves < 3:
        bi "Unfortunately, my efforts weren't enough."
        bi "She had a win in two moves."
        bi "Knowing what was coming, I made a useless move and..."
        $mood = "shock"
        b "Huh?"
        j "Everything okay?"
        $mood = "ind"
        b "Yeah, just..."
        bi "She's not going for it?"
        bi "She played what was instead a pretty useless move."
        bi "She could still beat me in two moves..."
        bi "I'm pretty sure unless she made ten mistakes in a row, I'd lost this game."
        bi "Stubborn as I am, I kept playing."
        bi "Three, four, five..."
        bi "She kept missing it."
        bi "I honestly wasn't sure why I kept playing."
        bi "In chess it's considered rude to force your opponent to play out an advantageous position."
        bi "But..."
        bi "I guess as long as there was even the slightest chance, I wanted to try."
        bi "If I resigned, I wouldn't know if I could turn it around."
        bi "This way, I know I tried and if I lost, there would be no regrets."
        bi "Was she toying with me? Like a predator making their prey run in circles?"
        bi "Seeing if I'd resign?"
        bi "Or was she just oblivious..."
        j "Oh..."
        b "Huh?"
        bi "She finally saw it."
        j "Check."
        b "Yeah, you got me, mate next move."
        show bg jennymonikablush with dissolve
        j "Good game!"
        b "Good game..."
        j "You held on a lot longer than I was expecting!"
        j "You could get pretty good with some more focus on the game I bet!"
        b "I'll keep that in mind for if we get out of here..."
    else:
        bi "Somehow, I managed to force some trades."
        bi "It was my king against her king, knight, and bishop."
        j "Shoot. I never thought this would happen."
        b "Huh?"
        j "It should be a win for me, but I don't know how to finish in fifty moves."
        j "If I can't then it's a draw."
        b "I'm down to play it out if you want to try."
        j "Nah, no need."
        j "I don't really see the value in playing out a game when we know the likely outcome."
        j "Granted, it would be kind of funny to watch your king run around the board helpless but..."
        show bg jennymonikablush with dissolve
        j "I'm not a sadist or anything, so I don't want to force that on you."
        j "Good game Bert! You did really well for someone with your experience level."
    scene bg hospfancy
    show jenny happy
    with fade
    j "Oh shoot, we really took a long time playing that game."
    j "I'm getting hungry again... maybe because lunch was just soup."
    j "I think it's time to go plan dinner."
    b "Sounds good, I can take the lead this time."
    b "I can't cook much but you shouldn't have to do all the work..."
    j "Your call Bert!"
    scene bg hospkitchen with fade
    show jenny happy with dissolve
    b "Okay, what do we have..."
    j "Well, it's just veggies like tomatoes and onions, and broths basically..."
    b "Okay, sounds like enough to make... tomato soup."
    show jenny ind
    $mood = "sad"
    j "Which we had for lunch."
    b "...Onion soup?"
    b "Is that even a thing?"
    j "Uh... it is now!"
    show jenny happy
    $mood = "ind"
    b "Onion soup it is."
    bi "We cut some veggies, boiled them in broth..."
    hide jenny happy with dissolve
    bi "About thirty minutes later we had made... something."
    bi "I took a taste and..."
    b "It's... edible."
    show jenny happy with dissolve
    b "...Maybe I should have let you cook again."
    j "It's fine Bert, not like we can make a gourmet meal in this kitchen."
    j "Let's get everyone fed before bedtime."
    j "Food's ready!"
    bi "The others gathered in a line again..."
    scene bg hospkitchenwindow
    show hospwindowoverlay
    show jenny happy:
        xcenter .25
    with dissolve
    show sid ind at inwindow behind hospwindowoverlay with moveinright
    i "Oh wow! This smells... wait, what is that smell?"
    bi "Sid took a sip."
    show sid smile at inwindow behind hospwindowoverlay
    i "Um... thanks guys."
    j "Do you like it, Sid?"
    i "Uh... yeah, I like not being hungry I guess."
    $mood = "sad"
    show jenny ind:
        xcenter .25
    i "Seeya."
    hide sid with moveoutleft
    show shahar ind at inwindow behind hospwindowoverlay with moveinright
    h "Aye, after that scrumptious soup me stomach's been rumbling for another meal!"
    h "Whatche got fer me lad?"
    h "..."
    h "Er, sorry lad, I must have confused hunger fer being full to the rim."
    hide shahar with moveoutleft
    scene black with dissolve
    bi "One by one, it was the same story."
    bi "My meal, if you could call it that, had put everyone off."
    scene bg hospfancy
    show jenny ind
    with dissolve
    b "Well, that was a disaster."
    b "I guess I'll stick to eating in the company cafeteria in the future..."
    j "Aww, at least you tried Bert."
    bi "Just then..."
    play sfx "audio/ding.mp3"
    intercom "It is now twilight. Please feel free to return to your rooms."
    intercom "You may still roam freely, but remember that you must return to your cell before night begins."
    bi "Through the window, we saw the others get up and head to their respectively hallways."
    j "I guess we should head back..."
    j "If we try to clean up again we might... well... get \"punished.\""
    b "Yeah, not exactly a risk I'm willing to take..."
    scene black with dissolve
    $mood = "ind"
    bi "We made our way back to the cells."
    scene bg hosphall1
    show jenny ind
    with dissolve
    j "Well, looks like that's it for our guard shift, Bert."
    show jenny happy
    j "I'd like to think we did a pretty good job!"
    b "Collectively maybe. I uh... may have indirectly led to one or two people starving to death."
    j "Oh, don't worry about it."
    j "Remember the train? We were barely scraping by in terms of food."
    j "Everyone will forget about it by the time we're fed tomorrow."
    j "Anyway, we should really get back into our cells. Good night Bert!"
    hide jenny with dissolve
    b "Well, Sesame, let's get some sleep."
    ses "mrrrrrrrrrrrrrowww"
    scene black with dissolve
    blank "The next day..."
    intercom "Twilight has begun. You must leave your room before daytime."
    scene bg hosproom1 with dissolve
    $ statusnt("Cell", "bert", ch=3, sun=0)
    $cat = False
    $mood = "ind"
    b "Yawn..."
    bi "The intercom wouldn't have been necessary, my stomach rumbling was about as loud..."
    b "Damn, I'm hungry."
    b "Neither meal yesterday was really that filling..."
    show sesame with dissolve:
        ycenter .61
    ses "Mew!"
    b "Morning Sesame."
    b "I'm weirdly excited for today... being on the guard side was quite lonely."
    b "Not that Jenny isn't good company, but it often felt like it was just the two of us..."
    b "Now we can actually talk to everyone without a literal wall between us."
    ses "Mew?"
    b "Um... do cats understand how windows work?"
    b "...Do you even understand what I'm saying?"
    ses "Prrr."
    b "I guess not..."
    b "Well, let's get going, don't want to get punished!"
    hide sesame with dissolve
    $cat = True
    b "Wait... is there a chance I'm a guard today?"
    b "The rules never said someone couldn't be a guard twice..."
    bi "I tried the guard door, but it was firmly in place."
    bi "Which means..."
    b "I guess we're off to the cafeteria."
    scene bg hospcommons with fade
    $showchibiwindow(["lauren", "freddy"], [])
    with dissolve
    show lauren ind:
        xcenter .25
    show frog ind:
        xcenter .75
    with dissolve
    l "Morning Bert, you're up earlier than last time."
    b "My stomach served as an alarm clock today."
    b "I'm really hungry..."
    l "Yeah, whoever made dinner yesterday didn't make a very filling meal."
    f "Sheeeeeesh!"
    b "Har har. Very funny."
    bi "Others slowly started filtering in."
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], [])
    with dissolve
    b "That's all but two of us, which means..."
    l "Dracula and Sid are the guards."
    l "Poor Sid, I wouldn't want to be alone with Dracula for an extended period of time."
    b "I mean, Sam did it for a bit and lived..."
    l "Yeah, but Sam's more... spunky."
    l "Or at least, was."
    l "Sid'll stand up for himself, don't get me wrong, but I don't think he can..."
    l "Well, control Dracula at all."
    b "Speaking of Sid..."
    bi "Sid had entered the kitchen."
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid"])
    b "Looks like he wants to talk to us."
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show sid ind at inwindow behind hospwindowoverlay2
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid"])
    with dissolve
    i "Hey guys."
    b "Where's Dracula?"
    i "Oh, is he the other guard today?"
    b "You didn't know?"
    i "I just woke up and came here because I was hungry, and assumed you all were too..."
    i "I didn't see him on my way here."
    b "Maybe he hasn't woken up yet?"
    b "You're in the same hallway as me, Dracula is in the other, so..."
    b "If he hasn't left his cell, you wouldn't have seen him."
    show lauren ind:
        xcenter .75
    with dissolve
    l "I doubt he's still asleep, we haven't heard an announcement yet..."
    l "Maybe he's exploring?"
    b "Explore? Me and Jenny checked everything..."
    l "Dracula might not trust what you said..."
    l "Or even if he does, he's the type who wants to double-check it."
    l "Remember in the trial when he knew what happened but made you say it?"
    l "So that he could be sure you arrived at that conclusion independently."
    b "I guess..."
    l "I think we should establish a system where the guards meet up in the morning."
    l "So we can keep an eye on everyone and make sure no one's planning a murder..."
    i "Anyway um... what should I make for lunch?"
    show jenny ind:
        xcenter .25
    with dissolve
    j "Have you looked in the fridge yet?"
    i "No, I wanted to talk to you guys first..."
    j "It's mostly just very basic ingredients..."
    i "I don't know if I want soup for a third meal in a row..."
    j "Well if you don't want to use the broths you basically just have veggies..."
    i "You can make a salad from just veggies, right?"
    j "I guess... it probably won't be very appetizing, but it'll be healthy."
    i "There has to be {i}something{/i} I can use to add flavor, right?"
    i "Like, I dunno, ranch dressing? Hot sauce?"
    j "If you find some by all means!"
    i "Okay, guess I'll get started."
    hide sid with dissolve
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid"])
    show jenny ind:
        xcenter .25
    show lauren ind:
        xcenter .75
    with dissolve
    j "I hope he finds something... it sounds like his salad won't have much flavor."
    l "He's just a kid from a not-so-great upbringing, we can't expect gourmet meals."
    l "Plus we're in a death game, I'm not too fussed about our meals."
    bi "Didn't she criticize my cooking?"
    l "Unless it gives me a shot to make a joke at Bert's expense, of course..."
    b "Har har."
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid", "dracula"])
    b "Oh, Dracula's here?"
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show drac ind at inwindow behind hospwindowoverlay2
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid", "dracula"])
    with dissolve
    d "Hello, all."
    b "Hey Dracula, where were you this morning?"
    d "What do you mean? I was on this side of the floor."
    b "No, I got that..."
    bi "How dumb does he think I am?"
    b "Sid said he didn't see you this morning on this way here."
    d "Oh, I was looking around, making sure you and Jenny hadn't missed anything."
    d "I'm pretty sure I checked everything."
    d "Well, except the entirety of the records."
    d "I looked through the first 30 or so records and increasingly felt it was not a good use of time."
    d "Bert, you said you saw no recognizable names in there, right?"
    d "If not I will not pursue that line of investigation further."
    bi "Right, have to keep Shahar a secret."
    bi "Better to prevent him from continuting to search..."
    b "No, I didn't see anything noticable."
    d "Alright, that settles it then."
    d "I will remain here from the time being until lunch is ready, I see Sid has started."
    d "In fairness' sake I will make dinner then."
    d "In the mean time, if you wish to talk, I will be here."
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid"])
    with dissolve
    b "Well, I guess I have some time to kill until lunch..."
    b "Who to talk to?"
    blank "FREE TIME 6 HERE"
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid"])
    with dissolve
    bi "After chatting a bit, Sid talked to us through the window."
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show sid ind at inwindow behind hospwindowoverlay2
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid", "dracula"])
    with dissolve
    i "Hey, I finished making a salad, I want to go check out that computer."
    i "I'm pretty good with tech, maybe there's some hidden files or something I can find."
    show drac ind at inwindow behind hospwindowoverlay2 with moveinright:
        xcenter .75
    d "You're awfully good at computers for someone nominally from a poor family..."
    show lauren ind:
        xcenter .25
    l "Hey, back off."
    l "Don't shame him for his past."
    d "I wasn't shaming him for being poor. There is nothing wrong with that."
    d "Just making an observation."
    l "Make less observations like that then."
    d "We need to trust each other fully to narrow down who the Game Master is, yes?"
    d "I don't trust Sid based on this seeming contradiction."
    l "And no one trusts that you're a vam{nw}"
    i "No, no, Lauren, it's okay..."
    i "I... think I should explain."
    i "Just so people don't suspect me of anything."
    l "Only if you want to, Sid"
    i "I... I do."
    i "My family was actually doing okay when I was born."
    i "Back then I had a lot of free time so I played games on the computer a lot."
    i "There was one game where you could make custom game modes."
    i "When I was playing that game, I learned to code."
    i "I wasn't very good at school but I was good at coding."
    i "I eventually started doing it on the side to make some pocket money."
    i "I got into this thing called ethical hacking."
    i "That's how I learned about coding."
    l "Ethical hacking?"
    i "Well, normally hackers are bad."
    i "Stealing credit card numbers from websites..."
    i "DDOSing servers to take down services."
    i "Ethical hacking is about finding those vulnerabilities too..."
    i "But telling developers about them and how to fix them."
    i "It was a fun challenge, like trying to invade a fortress."
    i "But I wasn't doing it to hurt people."
    i "Didn't pay as well as being a normal developer, not every company will pay you for it."
    i "Some just send you a thank you and never talk to you."
    d "I see. And this all happened before your family became poor?"
    i "Yeah, we got in some... legal trouble."
    i "We had to pay for lawyers and lost a lawsuit, so we were in a lot of debt."
    i "My dad had to sell the house and rent a small place to make the first few payments..."
    i "I started working for him for free so he could pay the debt with the money he would have paid me."
    bi "Legal trouble? Wait..."
    b "Sid, when you say legal trouble, was it with Stella's company?"
    b "She mentioned her company often sued smaller companies."
    i "No, it wasn't with her company..."
    i "It would be kind of nice if it was, then I'd know more about why I'm here..."
    i "Well, I guess Stella's not the Game Master, so maybe not..."
    l "Sid... you didn't have to say all that."
    l "Especially given how little {i}some{/i} people are saying about their pasts."
    d "Agree, I'd like to hear more about Bert's past at some point."
    l "Not who I was referring to."
    i "So uh... can I go check out the control room now?"
    l "Yeah, go ahead Sid."
    l "You've been very helpful already."
    i "Seeya! Dracula can serve you all food, I assume."
    hide sid with dissolve
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula"])
    with dissolve
    d "Hmph, I guess I've been volunteered involuntarily..."
    l "Guess that kid has more spunk than I gave him credit for..."
    d "Well, I guess I'll serve whatever he made."
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula"])
    with dissolve
    bi "We ate our salads quietly."
    bi "Thankfully, Sid had made a huge amount, I was no longer hungry."
    bi "Looking at the cafeteria, twenty or thirty people could easily fit here."
    bi "The kitchen probably had enough food and cookware to make a meal for that many people too."
    bi "Why did we only have access to eight cells?"
    bi "How powerful is this Game Master?"
    bi "They must have heavily modified this building just for this game..."
    bi "Man, after that feast in the mansion..."
    bi "I would kill for a proper meal. Hell, even the turkey sandwiches from the train sound great."
    bi "Well, maybe \"kill for\" is a poor choice of words."
    b "Man, if I make it out of here the first thing I'm doing is getting a big fat bowl of pasta."
    show frog ind with dissolve
    f "Pasta? That's what you want if you get out of here?"
    b "Oh... I mean, I guess I'd like to see my family too of course..."
    f "No silly, you should get nachos instead!"
    f "Nachos are way better than pasta!"
    b "Is that the first thing you'd do if you got out of here Freddy?"
    f "Hmm, probably not, there are bigger things than food."
    show frog ind:
        xcenter .5
        linear 0.15 xcenter .25
    show lauren ind with moveinright:
        xcenter .75
    l "Like what Freddy? Family? Friends?"
    f "There's a water park near where I live."
    l "A... a water park?"
    f "It's so fun!"
    f "There's a ride called the Frog Hopper where it launches you up and down."
    f "And up and down and up and down and up and down and up and down and up and down and..."
    l "I think we get it Freddy..."
    f "Oh and there's a wave pool!"
    f "My family doesn't have time to take me to the beach but I can pretend I'm at the beach!"
    f "Waves are fun but my mom doesn't let me get too close to the wave maker..."
    f "What about you Lauren, what do you wanna do when you get out?"
    l "Well... {i}if{/i} I get out, I think I'm going to give my parents a big hug."
    f "That's... boring."
    b "Yeah Lauren, I'm sure everyone wants to see their family."
    b "What's something only {i}you{/i} might want to do?"
    l "Something only I might want to do?"
    l "Bert, if that's the prompt your answer was cheating."
    l "Everyone wants to eat good food when they get out I'm sure."
    b "Yeah, but only I want to eat specifically at the Pagliacci Pastaria!"
    l "Sigh..."
    l "Okay, fine, your pastaria counts."
    l "I... want to apply for my MBA."
    f "What's... what's an MBA?"
    l "It's uh... school for if you want to own a business."
    f "Oh. Did my dad go to an MBA?"
    l "The MBA is the degree not the..."
    l "Never mind."
    l "Does he run a business?"
    f "He runs something, I'm not sure what it's called..."
    l "He might have one then."
    b "What kind of business do you want to run?"
    l "I want to run a day care."
    l "I have a lot of babysitting experience, I feel like I'm pretty good with kids."
    l "I can't imagine anything else I'd want to spend my life on, honestly..."
    f "Can I go to your day care Lauren?"
    show lauren happy:
        xcenter .75
    l "I think you're a bit old for that Freddy."
    hide frog with moveoutleft
    show jenny ind:
        xcenter .25
    j "Wait, Lauren... you said apply, did you not apply for one already?"
    show lauren ind:
        xcenter .75
    l "I guess... I wasn't sure until now."
    j "Why now?"
    l "Uh... I learned life is too short?"
    l "I don't know, this game has done all sorts of stuff to my head."
    l "Probably yours too. But it just feels right, I guess?"
    l "But who knows, I might leave and realize I was just being overly optimistic."
    l "Maybe I realize I hate running a business."
    show jenny happy:
        xcenter .25
    j "Ha, can't give the Game Master credit for giving you confidence, right?"
    show lauren happy:
        xcenter .75
    l "Right."
    l "What about you Jenny. What do you wanna do when you get out?"
    show jenny ind:
        xcenter .25
    j "I dunno, I haven't really thought about it."
    j "I've mentioned this before I think, but my parents aren't really around often."
    j "And I'm an only child."
    j "So it wouldn't be spending time with family really..."
    j "And we've been pretty well off so I've gotten to do most of what I want to do in life."
    j "I think I want to just sit on a couch and watch TV, honestly."
    j "I'd love to just be a normal boring person."
    hide lauren with moveoutright
    show shahar mad with moveinright:
        xcenter .25
    b "And what about you Shah-"
    b "Oh."
    bi "He doesn't even know what he has to go back to..."
    h "No, lad, it's okay."
    h "I'll have to think about it at one point or 'nother."
    h "I don't know, what do people do when they don't know who they are?"
    b "..."
    j "..."
    b "I think the rest of us don't know."
    b "But I'm sure there's resources out there."
    bi "Hell, maybe a place like this would be able to help you..."
    h "Well, I think that's what I wanna do, ladies and laddies."
    h "I'm gonna find out who the real Shahar Syed be."
    h "Figure there's nary a thing I could do before I do that."
    h "Ye all have families, I don't know if I do."
    h "Ye all have favorite foods, I don't know if I do."
    h "Or at least, if landlubbers eat me favorite foods."
    h "Do they have dried beans on land?"
    b "Um... yes, but there's better ways to eat beans."
    b "Burritos, chili, bean salad, dip..."
    h "What's a \"burrito\", lad?"
    b "Oh boy."
    b "Okay Shahar, second thing you're doing after you figure out who you are?"
    b "Eating a burrito."
    show shahar ind:
        xcenter .25
    h "I'm looking forward to it lad."
    hide jenny
    hide shahar
    with dissolve
    bi "With that, the only person we hadn't asked was..."
    show sam with dissolve
    bi "Sam."
    b "You want to join in Sam?"
    s "..."
    s "Drugs."
    b "Huh?"
    s "Going to get rid of my drugs."
    b "..."
    show sam:
        xcenter .5
        linear 0.15 xcenter .25
    show lauren ind with moveinright:
        xcenter .75
    l "Not a bad answer Sam."
    s "...Thanks."
    hide sam with moveoutleft
    show lauren ind:
        xcenter .75
        linear 0.15 xcenter .5
    bi "Lauren leaned in to whisper."
    l "It's not ideal, but it's progress."
    l "It's conversation, instead of not wanting to talk."
    b "Should I ask more? Get Sam to keep talking?"
    show lauren ind:
        xcenter .5
        linear 0.15 xcenter .75
    show sam with moveinleft:
        xcenter .25
    s "Life was fine before I tried to kill Stella."
    s "If I don't try to kill anyone else, that's the only way life will be fine after."
    s "Hard drugs can kill people."
    s "So... if I sell them to people, it's like I'm trying to kill them."
    b "..."
    s "..."
    s "Thanks for asking."
    hide sam with moveoutleft
    show lauren ind:
        xcenter .75
        linear 0.15 xcenter .5
    l "Okay, I know that last one sounded sarcastic, but I think Sam meant it."
    l "Even if... Sam's current outlook on life seems to be based on not killing people."
    l "It's still progress."
    b "I mean, that's respectable, I aspire not to kill people either."
    l "Knock it off."
    b "Sorry..."
    bi "Just then, Dracula knocked on the window to beckon us over."
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show drac ind at inwindow behind hospwindowoverlay2
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula"])
    with dissolve
    d "Hello all, just wanted to let you know I'll have dinner ready soon."
    d "I think I have something more appetizing than before."
    d "It's simple, but I'm making pasta with marinara sauce."
    d "Well, not really marinara sauce, just some crushed and cooked tomatoes."
    d "This kitchen is very stark. If I were staying here, I would leave a poor review."
    show jenny ind with dissolve:
        xcenter .25
    j "Pasta? Where did you find pasta?"
    d "There was a box on top of the fridge."
    j "A box? I didn't see a box..."
    d "It was pretty far back. I'd guess only myself and Shahar could have seen it up there."
    d "Not to insult anyone's stature, but the rest of you are average height at best."
    b "Hey man, you're not {i}that{/i} tall."
    d "I'm six feet and five inches. That's more than 99.5% of men."
    bi "Damn, he is that tall."
    b "Well being five foot nine doesn't make me a manlet!"
    j "Bert, is this a sensitive topic?"
    d "Nothing wrong with that Bert."
    d "Anyway, it should be ready in roughly thirty minutes."
    show jenny happy:
        xcenter .25
    j "Thanks Dracula!"
    show sid ind at inwindow behind hospwindowoverlay2 with moveinright:
        xcenter .75
    b "Hey Sid, you find anything interesting?"
    i "Um... well, I wasn't able to really hack into anything."
    i "It was probably made in the 90s like a lot of the software medical centers use."
    i "And the people running this place got too used to it."
    i "So there's better software out there, but the staff doesn't want to learn it."
    i "So they stick with the 90s software."
    show jenny ind:
        xcenter .25
    j "Bummer, so you didn't learn anything?"
    i "Well, I learned something."
    i "I uh... saw the name of the prosecuting attorney that got my family in trouble."
    i "They were a patient here."
    i "Their record was empty, unlike most of the others."
    i "Just a name..."
    bi "Wait."
    bi "Just like Shahar..."
    bi "It has to be related, right?"
    b "Sid, can I ask..."
    b "Is there any way that attorney is related to this game?"
    b "There's no way it's a coincidence we're in the same hospital a lawyer you knew was in, right?"
    i "..."
    j "Sid, you don't have to answer if you don't want to..."
    j "It's a very personal question."
    i "..."
    i "I think it's related, yeah."
    i "Um... when I said my family got in legal trouble, it's because of something I did."
    i "I pirated a movie online."
    b "They sent a lawyer after you for that?"
    i "Kind of..."
    i "A lawyer... {i}that lawyer{/i} sent me an email telling me he knew."
    i "And if I didn't do some work for him he'd rat me out."
    i "So... I did the dirty work."
    j "Dirty work?"
    i "It was to get some files from a private server."
    i "Belong to Inside Electronics."
    b "Inside Electronics?"
    i "Spelled with a Y. I-n-s-y-d-e."
    i "S-y-d-e like Sydell."
    i "He owned the company."
    i "That's why I think it's related."
    b "That's what caused your legal trouble?"
    i "Yeah. The lawyer said if I told anyone he'd expose me for hacking too."
    i "And well, I didn't know what to do."
    i "I'm still a child..."
    bi "Sid's eyes noticably teared up."
    b "Sid, you can stop if you wa{nw}"
    i "So I told my dad and he told the police we were getting blackmailed but..."
    i "I dunno, these lawyers were way more than we could imagine."
    i "I... I ruined my family."
    i "I should have never downloaded that movie."
