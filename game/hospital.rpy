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
    bi "One end of the hallway was a dead end, the other seemed to lead towards a larger room."
    bi "Mine was the second from the larger room."
    bi "I briefly walked towards the dead end to check the cells."
    bi "All of them looked to be identical to mine."
    bi "They all looked like they were empty, but..."
    bi "From this hallway, you couldn't really see the bed."
    bi "Some of them might have had people sleeping that I just couldn't see."
    bi "I guess we'll all convene eventually..."
    bi "With those observations, I opened the door to the larger room..."
    scene black with dissolve
    scene bg hospcommons
    $showchibint("dracula", "lauren", "sid")
    $statusnt("Cafeteria", "bert", ch=3, sun=0)
    with dissolve
    bi "The hallway opened up into what looked like a middle school cafeteria."
    bi "There, I saw a few of the others gathered."
    #BEGIN REWRITE
    show lauren ind with dissolve
    l "Morning."
    b "Is his everyone who's awake?"
    l "So far, yeah."
    bi "Sam was looking at a series of... photo composites on on wall."
    bi "On another wall was a sign."
    bi "It read \"Rules of the Latimer Mental Hospital\" at the top."
    bi "...Mental hospital?"
    bi "I guess... in a demented sense, a mental hospital is like a prison."
    bi "Dracula was reading through that one."
    b "How much looking around have you all done?"
    l "Not much personally."
    b "You also just got here?"
    l "Nah, I got up about 10 minutes ago."
    l "When I got here, Sid was the only one waiting. Dracula arrived a few minutes later."
    l "I've been... thinking."
    b "Thinking?"
    l "About Sam. What to say, how this affects the rest of us, all that."
    scene bg mansiondining
    show sam
    show sepia:
        alpha .5
    with dissolve
    s "It should be me who's dead now..."
    scene bg hospcommons
    $showchibint("dracula", "lauren", "sid")
    $statusnt("Cafeteria", "bert", ch=3, sun=0)
    with dissolve
    bi "Oh, right. Sam tried to kill Stella."
    bi "And probably didn't feel very good about it now."
    bi "We didn't really have time to debrief after figuring out it was Catherine who did it."
    bi "The Game Master couldn't even spare us that brief favor."
    l "Anyway, you shouldn't worry about that."
    l "Go do your investigation thing, figure out everything for the rest of us."
    bi "...I couldn't tell if she was patronizing me or complimenting me."
    b "Sounds good, seeya Lauren."
    hide lauren with dissolve
    bi "Looking around, the room didn't really have much besides tables."
    bi "So the only things to look at were the photo composites on the wall, and the sign with the rules."
    $menuset = set()
    menu picsorrules:
        set menuset
        "What should I look at?"

        "The photo composites.":
            bi "I joined Sid by the photo composites."
            show sid ind with dissolve
            i "Hey Bert."
            b "Hey Sid. What's happening here?"
            i "It seems like every year they put up a photo of everyone who got discharged that year."
            bi "Each photo composite had about 50 or so photos on it."
            b "Must be a pretty small hospital, if only this many people cycle per year..."
            i "It's kind of nice, in a way."
            b "Nice?"
            i "Having the photos of others who've made it out there."
            i "It's like... a reminder to patients that that they could do it, and so you can you."
            b "If only we had people who escaped this game before to motivate us the same way..."
            i "...Do you think this game is recurring?"
            b "Oh no, I was just making a joke."
            i "I saw a drama on TV like this..."
            i "It was about bunch of people competing in a life-or-death versions of children's games for a lot of money."
            i "They had one every year in the show, and one of the winners of the previous games ran the game now."
            i "What if this game we're in repeats every year?"
            i "Maybe the Game Master is a past winner?"
            b "Sid... no offense, but that's just something on TV."
            b "I don't think it has anything to do with our situation."
            i "Yeah, you're probably right."
            b "Have you taken a close look at the photos yet?"
            b "Maybe someone one of us knows is one of the photos?"
            i "I haven't looked in a lot of detail, but I haven't recognized anyone, no..."
            b "Hmm okay, guess I'll take a closer look myself."
            bi "..."
            bi "No, I don't recognize anyone on this one..."
            bi "Not that I should, it's from a year before I was born..."
            bi "I read through a few more, but didn't recognize any of the names or faces."
            bi "Huh?"
            bi "There's one from four years ago, and two years ago..."
            bi "But not three years ago."
            bi "There's even an empty spot in the line where one should be..."
            b "Sid, did you see a photo composite from three years ago?"
            i "Um... no, but they're chronologically ordered, so it should be easy to find it?"
            b "I think it's missing..."
            i "Huh. Do you think one of us got rid of it?"
            b "You were the first one to get here, right?"
            i "Yeah, pretty much as soon as I woke up I came here."
            i "So I guess there wasn't time for someone to come and remove it?"
            b "Maybe, maybe not..."
            b "We don't really know anything about how us waking up in a new location works."
            b "Do we all wake up at the same time or is it like taking a nap?"
            i "Hm... maybe the person whose turn it is to murder is on the missing composite?"
            i "Or maybe it's the Game Master and they deliberately removed it!"
            b "Yeah, there's gotta be a reason that specific year's is missing..."
            i "Maybe we should ask everyone if anything significant happened three years ago?"
            show scary with dissolve:
                alpha 0.5
            bi "Three years ago? What was I doing?"
            bi "I was twenty, so, that would be the year I-"
            bi "Got in the driving accident..."
            bi "I talked to Jenny about this but..."
            bi "Am I ready to talk to everyone about it?"
            hide scary with dissolve
            b "Nah, probably not worth it."
            b "If anyone has something revealing about them from three years ago, they're just gonna lie about it."
            bi "Hopefully that stops Sid from pursuing this line of-"
            i "Well, then we can use people's reactions to gauge what's happening!"
            bi "...Or that."
            i "Besides, maybe someone who's not the murderer or Game Master has something to reveal."
            b "Like what?"
            i "I mean... I dunno, but it can't hurt to ask, right?"
            i "Maybe if we find a theme behind what we all did six years ago we can figure out why the composite's missing."
            bi "Sid seems really set on this..."
            b "Okay, guess we'll discuss this once everyone's here..."
            i "Yeah, I think we should..."
            b "..."
            b "Okay, well, I guess back to scanning through these."
            i "Uh, yeah."
            hide sid with dissolve
            bi "...Well, guess I have to talk about it a bit more now..."
            bi "Can I come up with some convincing lie?"
            bi "No, I already told them in the train something happened when I was seventeen."
            bi "..."
            bi "I spent some time staring at the photo composites."
            bi "No familiar names or faces came up."
            bi "Once I had checked all the photos, it was time to move on."
            jump picsorrules

        "The rules.":
            bi "I went over to the sign, which Dracula was reading."
            show drac ind with dissolve
            d "Hello Bert."
            b "Hey Dracula. You read the rules already?"
            d "Yes. I thought it might be leftover from when this was place wasn't being used for a killing game."
            d "But no, it seems like the rules are for us."
            b "What makes you say that?"
            d "Read them yourself, then you can arrive at the same conclusion."
            bi "Well, of course I was going to..."
            bi "Seems Dracula doesn't believe in making conversation for the sake of it."
            bi "Alright, let's read these rules..."
            blank "Rules of the Latimer Mental Hospital"
            blank "1. This floor has a guard area and a patient area, separated by cells."
            blank "Every day, two guards will be appointed."
            blank "You will know you are a guard if you wake up and the door to the guard's side of this floor is open."
            blank "Otherwise, the door to the patients' side will be open."
            blank "2. Every day, there is a daytime period, a twilight period, a nighttime period, and another twilight period."
            blank "Each twilight period lasts 30 minutes."
            blank "After the first day, you may not be in your cell during the daytime period."
            blank "You may not be out of your cell during the nighttime period."
            blank "During twilight, you are allowed to move freely, with one exception."
            blank "No one is permitted to enter the cell of another individual at any time."
            blank "If you are in an area you are not allowed to be in at any time, you will be punished."
            blank "An intercom will announce when each period begins."
            blank "There will be two more announcements when there are 5 minutes of twilight left if someone is in a soon-to-be-forbidden area."
            blank "For example, if daytime starts in 5 minutes and you are in a cell, there will be an announcement."
            blank "4. Guards are responsible for feeding the patients during the day."
            blank "They may do this however they please, using the kitchen connected to this cafeteria."
            blank "There is a window that can be used to transfer meals and dirty dishes."
            bi "..."
            bi "As if this game wasn't hard enough as is."
            bi "Is the Game Master upset we had a party? Wants to keep us in check?"
            b "Interesting."
            b "I'm assuming when this place was a mental hospital, they didn't randomly appoint patients as guards."
            d "I'd say that's a reasonable conclusion."
            bi "...Is that his version of sass?"
            d "Bert, I have a question for you."
            d "For the Game Master, what do you think is the purpose of these rules?"
            b "I mean... I don't know it seems like some crazed experiment rather than a killing game."
            b "I have no idea what this accomplishes towards their overall goals."
            d "I agree, it's almost like they're emphasizing that we're just lab rats to them."
            d "It does make killing someone much harder, however..."
            b "Huh?"
            d "Think about it. This is presumably part of the area patients have access to."
            d "This room, and the two hallways connecting it to the cells."
            d "Now, if no one stupidly walked off on their own into a hallway..."
            d "Could you easily commit a murder here?"
            b "Um, I guess not?"
            b "There would be a lot of people around to see you do it..."
            d "Precisely. Both Dan and Stella died in isolation."
            d "So a murder is going to be hard to commit in this area."
            b "Well that just means you have to commit it in the guard area, right?"
            d "And how do you propose doing that?"
            b "Um... I mean, if you really had to you could get the other guard to go somewhere out of sight with you."
            b "Then just... I guess, stab them or beat them up, whatever's easiest?"
            b "I dunno man, I don't really think about how to murder people on a daily basis."
            d "Well, suppose you did that."
            bi "Shouldn't he have responded \"I don't think about how to murder people on a daily basis either\"?"
            d "Say we're guards together. You take me to a corner where no one can see me and kill me."
            d "Once the body's found, how do you propose that you would deny being the murderer?"
            b "Um... natural causes?"
            d "Natural causes."
            b "...It was a joke."
            d "I don't get it."
            b "...Sigh. Yeah, you're right, it'd be obvious it was me because we were the only two guards."
            d "Precisely. So it seems nigh impossible to murder anyone here."
            b "But... a murder has to happen for the game to progress, right?"
            d "Well, we don't know that."
            d "What happens if no murder occurs for days on end?"
            d "Perhaps the Game Master just leaves us to starve to death."
            d "Perhaps they'll replenish our food supply, but make us decide if not murdering is worth being stuck forever."
            b "Well, I hope it doesn't come to that..."
            d "So you wish that someone dies?"
            b "What? No!"
            b "Well, I mean... I guess yeah, I'd prefer the Game Master dying to us being stuck here."
            d "But that is statistically unlikely. The murderer has a one out of seven chance."
            b "One out of seven? They can make an educated guess, right?"
            b "For example, there's no way Freddy's the Game Master."
            d "Oh Bert, so optimistically naive..."
            d "Regardless, I actually doubt it will get to that point."
            b "Didn't you just try to argue that murdering someone and getting away with it would be impossible?"
            d "I said much harder. Not impossible."
            d "For example, you could poison someone's food as a guard."
            d "That would at least give you a fifty-fifty chance of your guard partner being accused in your place."
            d "Better yet, if the poison takes a few days to act..."
            d "Then other guards will come and go before someone dies."
            d "Then you'd have a really good alibi."
            b "But that requires poison to pull off..."
            d "I'm just saying, the avenue of murder will have to be a somewhat contrived one to be successful."
            bi "Like tricking someone into completing part of a circuit attached to a generator isn't contrived enough..."
            b "Why are you telling me all this?"
            d "Having someone to hear my theories makes it more obvious if they have errors."
            b "Isn't Sam the person you'd normally talk to about this?"
            d "I have a feeling Sam's prefrontal cortex out of commission for a while."
            b "Prefrontal cortex?"
            d "The part of the brain that does critical thinking."
            b "So... I'm Sam's replacement."
            d "I guess so, yes."
            b "..."
            b "Okay, well, bye Dracula."
            hide drac with dissolve
            jump picsorrules
    bi "Well, I guess that's everything to see in this room."
    bi "Unless I want to stare at some really boring tables."
    bi "In the meantime, it seemed everyone had filtered into the cafeteria."
    $showchibint("dracula", "lauren", "sid", "sam", "shahar", "jenny", "frog")
    show jenny happy with dissolve
    j "Hey Bert! Seems like we're in a hospital now!"
    bi "That's... not really something to be cheery about."
    b "Hey Jenny. How's it going?"
    j "Oh, I'm doing as good as I can be!"
    show jenny ind
    j "But doesn't seem like everyone else is."
    b "Huh?"
    j "Well, Sam is pretty torn up about trying to kill Stella."
    j "And Shahar says he's been having a headache since we got here."
    j "You mind talking to Shahar?"
    b "Huh? Why me..."
    j "Well, you did spend a lot of time with him in the mansion, like it or not."
    j "And I think we need to keep everyone... well, as happy as they can be, you know."
    j "Not just for their sake."
    j "If we have people too sad to think or help out, well..."
    j "It's going to be harder solve a murder mystery with less brainpower."
    j "Or even just find out more about why we're here and who the Game Master is."
    bi "I don't know if I'd classify Shahar's contributions as \"brainpower\" but..."
    b "That's true... yeah, I can talk to Shahar."
    show jenny happy
    j "Great! So you'll talk to both Shahar and Sam!"
    b "Wha-"
    j "Thanks Bert, that's really nice of you!"
    hide jenny with dissolve
    bi "She left before I could even respond..."
    bi "I'm not the best at cheering people up, why can't someone like Lauren do this?"
    bi "Sigh. Okay, might as well bite the bullet."
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
    show drac ind with dissolve
    d "So, has everyone read the rules?"
    d "We should make sure we all understand them before progressing."
    show drac ind:
        xcenter .5
        linear 0.15 xcenter .75
    show jenny ind with moveinleft:
        xcenter .25
    j "I did have one question..."
    j "The rules say we'll be \"punished\" if we follow them."
    j "Do we know what punished means?"
    hide drac with moveoutright
    show frog ind with moveinright:
        xcenter .75
    f "Punished? Isn't that like time out?"
    b "Uh..."
    f "You know, when you have to go sit in the corner and face the wall."
    f "And you can't even play video games or listen to music."
    show frog sad:
        xcenter .75
    f "And your mom and dad are arguing but you're not allowed to go to your room."
    f "So you have to listen the whole time."
    b "Uhhh....."
    hide jenny with moveoutleft
    show lauren with moveinleft:
        xcenter .25
    l "That's... one kind of punishment, yeah Freddy."
    l "But I think what the sign means is something worse than that."
    f "Worse than time out? That's not possible!"
    f "What could be worse than time out?"
    l "Uhhhhhhh........"
    l "Hey guys, wasn't there something else we wanted to discuss?"
    hide frog with moveoutright
    show sid ind with moveinright:
        xcenter .75
    i "Oh yeah, I had something I wanted to discuss."
    i "There's photos of all the people who got discharged from this hospital in the past."
    i "They have one photo composite per year, but the one from three years ago is missing."
    i "Is it possible someone important was on that composite?"
    l "Like one of us?"
    i "Maybe. But it could also be somenoe related to one of us?"
    i "Or maybe that was an important year for why this game happened."
    b "Important year?"
    i "Yeah, after Bert and I talked about the photos I was thinking..."
    i "I haven't really done anything that bad in the past three years."
    i "If I was chosen to be a part of this game, it has to be for something that happened before that, right?"
    i "I was wondering..."
    i "Did any of your crimes happen in the past three years?"
    i "You don't have to say what your crimes were, I know some of you can't really talk about it."
    i "But just that one bit of info might reveal a whole lot."
    bi "Thank you, Sid..."
    l "Mine was... a long time ago, but nothing in the last three years."
    bi "One by one, the others chimed in to agree."
    bi "No one remembered committing a crime in the past three years..."
    show lauren ind:
        xcenter .25
        linear 0.15 xcenter .5
    show sam with dissolve:
        xcenter .25
    bi "Except for one person."
    s "I guess... I've been committing crimes perpetually..."
    s "Not like I ever stopped dealing drugs..."
    l "Well... when did you deal drugs to Mr. Sydell?"
    bi "Right, Sam mentioned that in the mansion."
    s "...I lost contact with him about three years ago..."
    b "Lost contact?"
    s "He just never reached out to me again..."
    s "And well, not like I personally knew the guy..."
    s "I had no reason to reach out to him..."
    b "I wonder... did something happen to him three years ago?"
    l "Maybe he disappeared to start planning this game?"
    i "I thought the Game Master was one of us?"
    i "None of us look like him..."
    i "But I think you're right Bert."
    i "There's no way what Sam said isn't related to the missing photo composite."
    i "Maybe Mr. Sydell was on it."
    i "Maybe whatever happened to him three years ago is the reason for this game!"
    bi "A noise interrupted."
    play sfx "audio/ding.mp3"
    intercom "It is now twilight. Please feel free to return to your rooms."
    intercom "You may still roam freely, but remember that you must return to your cell before night begins."
    hide sam
    hide lauren
    with dissolve
    show jenny ind:
        xcenter .25
    with dissolve
    j "I think we should all go sleep."
    i "Wait, we were making so much progress!"
    j "Yeah, but I don't really want to find out what being \"punished\" means."
    i "...Fair enough."
    hide sid with dissolve
    show frog ind:
        xcenter .75
    with dissolve
    f "I don't wanna sleep. I wanna play!"
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
    j "Oh yeah, I guess you were looking around while we discussed this."
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
    j "Never heard of it."
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
    show jenny happy
    $showchibiwindow(["jenny"], ["dracula", "sid", "shahar", "lauren", "freddy", "sam"])#copy paste
    with dissolve
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
    $ftecounter = 5
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
    play sfx "audio/ding.mp3"
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
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid", "dracula"])
    with dissolve
    b "Well, I guess I have some time to kill until lunch..."
    b "Who to talk to?"
    $ftecounter = 6
    blank "FREE TIME 6 HERE"
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["sid", "dracula"])
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
    bi "Time passed as we ate our salads quietly."
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
    show shahar ind with moveinright:
        xcenter .25
    b "And what about you Shahar?"
    h "I'm returning to the sea, lad."
    h "The smell o' salt water runnin' through your nose."
    h "The squiffy feeling from the ship rockin' port and starboard."
    h "Pirate cuisine. Sea biscuits, grog...."
    h "And me favorite, dried beans."
    b "Dried beans? There's way better ways to eat beans..."
    b "Burritos, chili, bean salad, seven layer dip..."
    h "What's a \"burrito\", lad?"
    b "Oh boy."
    b "Okay Shahar, after you get out, add eating a burrito to that list."
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
    hide lauren with dissolve
    bi "Well, have to kill time somehow."
    bi "I guess I should strike up a conversation with someone..."
    bi "Unfortunately, it seems Sid is busy, so it can't be him."
    $ftecounter = 7
    blank "FREE TIME 7 HERE"
    bi "What felt like a few hours passed with some idle chit-chat, but it was hard to tell."
    bi "It could have been minutes, or a full day."
    bi "After some time, Dracula knocked on the window to beckon us over."
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
    d "I'm six feet and five inches. That's more than 99.5 percent of men."
    bi "Damn, he is that tall."
    b "Well being five foot nine doesn't make me a manlet!"
    j "Bert, is this a sensitive topic?"
    d "Nothing wrong with that Bert."
    d "Anyway, it should be ready in roughly thirty minutes."
    show jenny happy:
        xcenter .25
    j "Thanks Dracula!"
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula", "sid"])
    with dissolve
    show sid ind at inwindow behind hospwindowoverlay2 with moveinright:
        xcenter .75
    i "Hey guys."
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
    i "I was so young and knew nothing..."
    bi "Sid's eyes noticably teared up."
    b "Sid, you can stop if you wa{nw}"
    i "So I told my dad and he told the police we were getting blackmailed but..."
    i "I dunno, these lawyers were way more than we could imagine."
    i "I... I ruined my family."
    i "I should have never downloaded that movie."
    i "I'm just a stupid child, my parents should have never had me."
    i "I deserve to be part of an evil game like this."
    hide jenny with moveoutleft
    show lauren ind with moveinleft:
        xcenter .25
    l "No, Sid..."
    l "That lawyer should have never blackmailed you."
    l "You made an innocent mistake, no one should lose their freedom over that."
    i "I guess but..."
    i "Well, I did."
    i "The real world isn't fair."
    i "It'd be nice to play fair rules, but you don't get to decide the rules."
    i "You just have to play by them."
    l "But should you feel bad for getting punished by unfair rules?"
    i "I dunno Lauren, wouldn't you feel bad if everyone here got killed because you didn't play by the rules?"
    l "..."
    i "Didn't think so."
    hide sid with dissolve
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula"])
    with dissolve
    bi "Sid walked off."
    bi "Did I push too far by asking him?"
    bi "No, I tried to stop him..."
    d "Well, the pasta will be done soon. Would you all please get ready to eat?"
    bi "Dracula, seemingly missing the mood, prepared plates for us all."
    scene bg hospcommons
    $showchibiwindow(["lauren", "freddy", "jenny", "shahar", "sam"], ["dracula"])
    with dissolve
    show scary with dissolve:
        alpha .5
    bi "We ate, this time mostly in silence."
    bi "Jenny was talking to Freddy to keep him occupied while Lauren was lost in thought."
    bi "Probably upset about how she couldn't console Sid?"
    bi "And Shahar and Sam weren't really the types to start conversations."
    bi "Despite how isolated and claustrophobic this place felt..."
    bi "Up until a few minutes ago, it seemed like we were making the best of it."
    bi "Maintaining smiles and hope by going in a circle and talking about what we want to do."
    bi "But then... Sid's story hit us like a truck."
    bi "And this was after recovering from Shahar's, and Sam's, and Lauren's experiences."
    bi "The curtains were starting to pull back."
    bi "Everyone's personal history, fears, problems..."
    bi "The nature of this game was getting harder and harder to ignore."
    bi "Not to mention..."
    bi "It's easy when you're part of a large group to believe if a rare event happens, it won't happen to you."
    bi "I should have been enjoying the novelty of pasta, after two days of simple soups and salads."
    bi "Instead I felt like, cliche as it was, the air was so thick I could cut it with a knife."
    bi "..."
    bi "If Sid weren't so upset, and the mood were different, I'd love to know..."
    bi "Was the lawyer he was talking about Shahar?"
    bi "Did Sid also see that file?"
    bi "Does Sid know Shahar, and he just failed to mention it?"
    hide scary with dissolve
    play sfx "audio/ding.mp3"
    intercom "It is now twilight. Please feel free to return to your rooms."
    intercom "You may still roam freely, but remember that you must return to your cell before night begins."
    bi "..."
    b "Guess we should go sleep."
    bi "No one really had much to say to that..."
    bi "Everyone got up and walked towards their cells."
    scene bg hosproom1 with fade
    show sesame with dissolve
    ses "Mew?"
    b "Hey Sesame, weird day, huh?"
    ses "Prrrrr."
    b "Do cats even understand what murder is?"
    ses "Ssssss."
    bi "She was leaning and bowing her head."
    b "Do you... want head scratches?"
    ses "Prrr."
    bi "I scratched Sesame's head."
    bi "..."
    bi "Maybe this is the mood-lifter I need for now."
    bi "A super cute cat."
    bi "It's like Lauren said, baby steps."
    bi "Just have to keep my spirit up for the next five minutes."
    bi "Five minutes at a time."
    b "Good night Sesame."
    ses "Mew!"
    scene black with dissolve
label laurentime:
    blank "The next day..."
    play sfx "audio/ding.mp3"
    $noside = True
    intercom "Twilight has begun. You must leave your room before daytime."
    li "C'mon Sam."
    li "Of all the times to be mopey, this isn't a good one."
    $laur = True
    $noside = False
    $rg = True
    scene bg hosphall2
    $showchibint("sam")
    with dissolve
    lf "Sam."
    lf "Get up, you can't stay in there forever."
    s "..."
    s "There's thirty minutes, I can stay in here a bit longer..."
    li "I gave Sam as disappointed but caring a look as I could."
    li "Unlike the patient hallway, you could make eye contact with someone in bed from the guard hallway."
    li "They say you can't take care of other people if you don't take care of yourself first."
    li "Well, they haven't met the me that's playing this game."
    lf "Sam, let's go. We have to make food."
    s "Sigh..."
    lf "If not for me, can you get up for Freddy?"
    lf "He'll be hungry..."
    s "Sigh... okay..."
    pause 1.0
    show scary with dissolve:
        alpha 0.5
    lf "I'm getting tired of it."
    lf "Dracula's two-faced way of asking us to open up while lying to us."
    lf "Bert trying so hard to solve everything to the point of making Freddy sad."
    lf "Jenny's need to act like a ditz in a killing game and get away with it because she's cute."
    lf "And now... Sam acting like no other innocent people tried to kill someone in this game."
    lf "At least before I could kind of ignore Sam..."
    lf "I'm glad there are some children around to keep me sane."
    lf "It feels like they're the only truly innocent ones."
    lf "Well, and Shahar."
    lf "He has the mind of a child, so I guess he counts."
    hide scary with dissolve
    show sam with dissolve
    s "Let's go..."
    scene scary with dissolve
    scene bg hospfancy
    $showchibint("sam")
    with dissolve
    lf "Wow, this room is so much nicer than the cafeteria."
    lf "Ooh, a vending machine."
    lf "None of the previous guards mentioned this..."
    show sam with dissolve
    s "..."
    lf "Sam's... not one for many words."
    lf "Hey Sam, is there a cherry soda in there?"
    s "...Can't you see for yourself?"
    lf "I uh... can't really tell."
    s "...But they're all clear, brown, or green..."
    lf "So no cherry soda?"
    lf "Bummer."
    lf "Well, you want a drink?"
    s "..."
    lf "No? More for me, I guess."
    lf "..."
    lf "Huh, it requires money."
    lf "But it seems like someone has taken a drink from here already."
    lf "Maybe from way back when this place was operational?"
    s "...Yeah, maybe..."
    lf "These sodas might be very old..."
    s "...Didn't you want to make food quickly?"
    s "...Why are we wasting time here?..."
    lf "You're right, my bad."
    lf "Let's go to the kitchen."
    scene scary with dissolve
    scene bg hospkitchen
    $showchibint("sam")
    with dissolve
    lf "Alright, let's see what there is to cook wi-{p=0.5}{nw}"
    j "Lauren! Sam!"
    li "Jenny?"
    li "Right, I should check in with people on the other side..."
    scene bg hospkitchenwindow
    show hospwindowoverlay
    show jenny ind at inwindow behind hospwindowoverlay
    $showchibiwindow(["sam"], ["jenny", "dracula", "sid", "freddy", "bert"])
    with dissolve
    lf "What's up?"
    j "Not much. Sid woke up with a pretty rough cough this morning."
    li "Wait."
    li "...There's only five of them?"
    lf "Where's Shahar?"
    j "We thought you would know..."
    lf "What?"
    j "He hasn't shown up yet."
    lf "None of you went to check his cell?"
    j "Well, if he's in bed we won't see him..."
    j "Also, we were trying to figure out how to help Sid..."
    li "Idiots..."
    li "Without thinking I ran."
    scene scary with dissolve
    li "I'm not sure why I ran."
    li "It's not like me running was going to affect anything."
    li "I felt like those idiots who speed towards a red light."
    scene bg hosphalltopright 2 with dissolve
    l "...There's something in front of Shahar's cell."
    l "What looks like glass and... either celery juice or..."
    li "I slowly approached Shahar's cell."
    li "I don't know why I thought I would see anything different when I got there."
    li "Maybe he had a cup of juice and spilled it."
    li "My brain was reaching for every other explanation."
    li "But sure enough..."
    scene bg shahardead with dissolve
    lf "No."
    lf "No no no no no no no no no no no no no no no."
    lf "Why did no one but me think to check?"
    $showchibint("sam")
    show sam:
        xcenter .75
    with dissolve
    s "...He's dead..."
    lf "...Yeah."
    s "...In some ways, he's lucky..."
    s "...Doesn't have to play this game anymore..."
    li "Really not helping right now, Sam."
    li "Keep it together Lauren."
    li "Oh god, with the smell of blood I might vomit."
    li "Hold it in, hold it in, hold it in..."
    li "I need to get away from here."
    lf "...We should go tell the others."
    s "...Kay..."
    scene scary with dissolve
    scene bg hospkitchenwindow
    show hospwindowoverlay
    show sam:
        xcenter .75
    show jenny ind at inwindow behind hospwindowoverlay:
        xcenter .5
    show bert ind at inwindow behind hospwindowoverlay:
        xcenter .25
    $showchibiwindow(["sam"], ["jenny", "dracula", "sid", "freddy", "bert"])
    with dissolve
    j "Did you find him?"
    lf "...He's dead."
    show bert sad:
        xcenter .25
    bt "...Dead?"
    lf "Yeah. He's leaning against one of the bars in his cell."
    lf "He's bleeding on his forehead where it looks like he hit the bar."
    bt "How could he have died? We saw him go into his cell yesterday."
    bt "He should have been safe in there..."
    bt "I... I can't believe it. He died before he could-"
    bt "Uh, never mind."
    li "Huh? Does Bert know something we don't?"
    bt "I'm gonna go check something."
    hide bert with moveoutleft
    $showchibiwindow(["sam"], ["jenny", "dracula", "sid", "freddy"])
    with dissolve
    lf "What could he possibly want to go check..."
    li "And where was this urgency when we thought Shahar might be dead?"
    li "Just a few seconds later, Bert returned."
    show bert sad with moveinleft:
        xcenter .75
    $showchibiwindow(["sam"], ["jenny", "dracula", "sid", "freddy", "bert"])
    with dissolve
    bt "The guard-side door in my cell is still closed."
    lf "Uh... how is that relevant to Shahar dying?"
    bt "Well, I'm guessing that means the rules haven't changed."
    bt "We can't walk into our cells, much less cross over to the other side."
    bt "Which means..."
    lf "Oh."
    lf "Sam and I are the only ones who can investigate this side."
    lf "...I guess we can do that, right Sam?"
    s "...Fine..."
    lf "In the meantime..."
    lf "Don't tell Freddy anything you don't need to."
    lf "And uh... I guess we won't be cooking anything for now."
    j "No food?!"
    li "Jenny... now's not the time."
    lf "Well, guess it's time to investigate."
    j "Sure. We'll also investigate as much as we can here."
    bt "Though I doubt it'll be a lot..."
    bt "Lauren, Sam, remember everything you find in as much detail as possible."
    bt "Once you think you've found everything you can tell us about it."
    bt "It's not ideal, but we'll have to make do."
    bt "Oh, and come back here if you want to ask us anything."
    lf "Got it."
    li "I hate that Bert talks like he's my manager..."
    lf "Come on Sam, let's go."
    scene bg hospkitchen
    $showchibiwindow(["sam"], ["jenny", "dracula", "sid", "freddy", "bert"])
    with dissolve
label hospPreInv:
    play music "audio/inthefaceofdeath.mp3"
    pause .5
    show investstart with dissolve
    pause 1
    hide investstart with dissolve
    li "We haven't even really had a chance to explore this side, and now we have to investigate it."
    li "I say \"we\" but to be honest, I'm not sure how much Sam will help."
    li "It's all on me. My life, and the life of everyone else here..."
    li "Alright Lauren, you can do this..."
    call screen hospkitchenInv with dissolve
label trial3a:
    $laur = False
    $rg = False
    $noside = True
    scene black with dissolve
    bi "..."
    bi "I've never really felt like my life was out of my control."
    bi "I guess I was lucky to be born to good parents, that wasn't under my control."
    bi "But the rest of my life was to some extent."
    bi "Stuff like college admissions are kind of random, but you have some control."
    bi "Even the accident..."
    bi "That was out of my control, but I had ways to keep it from ruining the rest of my life."
    bi "But now..."
    $noside = False
    scene bg hospcommons
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], [])
    with dissolve
    bi "It's all on Lauren."
    bi "And I guess Sam. But mostly Lauren."
    bi "If she misses a crucial piece of evidence..."
    bi "If she misspeaks and we all believe something wrong..."
    bi "Or even worse, if she did it and lies to us all..."
    bi "We're all dead.{p=1.0} Simple as that."
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "They're back. Lauren and Sam."
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    $ statusnt("Kitchen", "lauren", ch = 3, sun = 1)
    with dissolve
    show lauren ind at inwindow behind hospwindowoverlay:
        xcenter .33
    show sam at inwindow behind hospwindowoverlay:
        xcenter .67
    with dissolve
    l "I think we found everything."
    l "I uh, didn't really have a way to take notes or anything so this is all off the top of my head..."
    show scary:
        alpha .5
    with dissolve
    bi "Lauren proceeded to tell us everything she observed."
    bi "I did my best to picture everything she described."
    bi "There's a memory trick called building a memory palace, also called The Roman Room."
    bi "For some reason, humans are better at memorizing objects after visualizing them in familiar locations."
    bi "Even if those objects are totally unrelated. For example..."
    bi "If you want to memorize a long sequence of letters, it's easier if you attach each one to an object."
    bi "Then, you picture those objects laid in order around a familiar room."
    bi "By just picturing myself walking around the guard side, seeing the things Lauren described..."
    bi "I felt like I was able to remember a lot of the minor details of what Lauren said."
    bi "It took a while, but eventually Lauren had managed to tell us everything."
    hide scary with dissolve
    blank "All evidence found by Lauren has been transferred to Bert."
    bi "...Can I trust her though?"
    b "Hey Lauren, Sam..."
    b "Tell me what you did this morning on your own."
    l "Huh?"
    b "You came here earlier and asked us questions..."
    b "I'm just returning the favor."
    b "The things you did together don't really matter, just the alone parts."
    l "I... guess that makes sense."
    l "I woke up as soon as the intercom went off."
    l "Got up and immediately went to Sam's cell, and then waited there until Sam came out."
    l "And then we spent the rest of the time until now together."
    b "Sam?"
    s "...Lauren just told you."
    b "Yeah, but tell me things from your perspective."
    s "...Fine."
    s "...I woke up before the intercom."
    s "Then I just sat in bed and stared out the guard-side door until Lauren showed up."
    s "And then like she said, we spent the rest of the together."
    b "Thanks, that's useful."
    $hosp_evidence[0] = True
    show newevidencefound with dissolve
    pause 1
    hide newevidencefound with dissolve
    blank "Guards' Accounts was added to evidence."
    scene bg hospcommons
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    show jenny ind with dissolve
    b "Okay, first things first, we should try to figure out how Shahar died."
    j "Well, isn't that obvious?"
    j "I mean, if you consider the state of the body, there's really only one explanation..."
    python:
        startHospitalTrial("jenny", "Jenny: According to Lauren, {color=#f00}Shahar's body had no injuries besides the one on his head{/color}.", -1,
        "jenny",  "Jenny: So {color=#f00}Shahar must have died from whatever caused that injury{/color}.", -1,
        "jenny",  "Jenny: He was on the guard side of his cell, so a {color=#f00}guard must have killed him{/color}.", -1,
        "jenny", "Jenny: They did it by {color=#f00}striking Shahar hard in the forehead through the bars{/color} with some sort of object.", -1,
        3, 8, "trial3b")
label trial3b:
    scene bg hospcommons
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    show jenny ind
    with dissolve
    b "No, I don't think Shahar was struck in the forehead."
    j "But he has no other injuries... why would he be bleeding on his forehead if he wasn't struck there by someone?"
    b "I agree he has no other injuries, but think about the way his body is positioned."
    scene bg shaharhead with dissolve
    b "He's kneeling, and leaning forward."
    b "If someone hit him from the front, and that was the killing blow..."
    b "It's more likely he would have fell over backwards."
    b "So we would have found him on his back."
    b "Even if they hit him on the forehead, and he didn't fall, and then fell later..."
    b "What are the odds that his head would land exactly on his injury?"
    j "Hm... that's true, but..."
    j "If that isn't what killed, what else could have?"
    j "After all, Lauren said he has no other visible injuries."
    show jenny ind:
        xcenter .5
        linear 0.15 xcenter .25
    show sid ind with moveinright:
        xcenter .75
    i "Wait, but *cough* Lauren didn't see the back side of him, right?"
    i "Just because there are no other {i}visible{/i} injuries *cough* doesn't mean there aren't some we can't see."
    i "Shahar could have a *cough* injury on the back of him."
    j "Oh, that's a good point!"
    j "In which case, it's obvious what happened!"
    bi "Anytime someone says this, it usually means I'm going to have to prove them wrong..."
    python:
        startHospitalTrial("jenny", "Jenny: The injury on Shahar's forehead was {color=#f00}caused by him slamming his head into the bars{/color}.", -1,
        "jenny",  "Jenny: Which means, he must have been {color=#f00}hit from behind{/color} into the bars.", -1,
        "jenny",  "Jenny: If he was hit into the bars, {color=#f00}that would explain why his injury is exactly where he's leaning on the bar{/color}.", -1,
        "sid", "Sid: *cough* It makes sense, but {color=#55f}I don't think there was anything they could use to hit him{/color}.", 1,
        1, 3, "trial3c")
label trial3c:
    scene bg hospcommons
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    show jenny ind:
        xcenter .25
    show sid ind:
        xcenter .75
    with dissolve
    b "Jenny, if you look at the rules of the hospital..."
    b "It's pretty clear Shahar wasn't hit from behind into the bars."
    j "Really? It's not clear to me..."
    j "Then again, there are a lot of rules, I might be forgetting an important one."
    b "Well, the important rule is..."
    show scary with dissolve:
        alpha 0.5
label trial3c2:
    menu:
        bi "Which rule proves Shahar wasn't hit from behind?"

        "Two guards are appointed every day.":
            bi "Even if there was only one guard, they could have hit Shahar if not for the other rules..."
            jump trial3c2
        "During the day, we cannot be in our cells.":
            bi "Well, the crime could have happened at twilight. So this doesn't really rule anything out."
            jump trial3c2
        "At night, we must be in our cells":
            bi "Well, the crime could have happened at twilight. So this doesn't really rule anything out."
            jump trial3c2
        "No one may enter another person's cell.":
            bi "Yeah, that's it!"
        "Guards cannot be on the patients' side of the floor and vice-versa.":
            bi "This rule doesn't say anything about the cells, which aren't really on either side..."
            jump trial3c2
        "Guards are responsible for feeding patients.":
            bi "Unless Shahar sha-starved to death, I don't see how that's relevant."
            jump trial3c2
    hide scary with dissolve
    b "The rules say no one may enter another person's cell."
    b "So for someone to hit Shahar from behind into the bars, they would have to break that rule."
    b "Which means they'd be \"punished.\""
    j "Maybe they just hit him really hard from the patients' side across his cell!"
    b "...They hit him once hard enough to send him all the way across his cell?"
    j "Oh... yeah, they would have had to enter his cell and get punished..."
    i "*Cough* we don't know what the punishment is though!"
    j "Yeah! Maybe the punishment is just having to eating the end slice of a loaf of bread!"
    b "Um..."
    b "I mean, okay, maybe the punishment is something none of us would notice."
    bi "Which given how psychotic the Game Master is, probably isn't the case..."
    b "But would anyone really risk their life over figuring that out?"
    i "*cough* We're all already risking our lives by-{p=0.5}{nw}"
    hide jenny
    hide sid
    show drac ind
    d "Enough."
    d "This meaningless speculation is going nowhere."
    d "Obviously the killer is..."
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show drac ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    d "Either Lauren or Sam."
    s "...Idiot..."
    d "Call me what you wish, but..."
    d "If someone attacked Shahar in his cell from the patient's side, they would have walked past three cells."
    d "Bert, Jenny, and Sid's."
    d "Granted, Sid was on the guard's side with me."
    d "You all cannot be sure what time he returned to his cell."
    d "But if I recall, you all returned to your cells at roughly the same time last night."
    d "The cells doors are well... not doors. You can hear and see through them easily."
    d "It would have been very difficult for a patient to reach Shahar's cell during twilight..."
    d "At least, without being noticed by Jenny or Bert."
    l "That's true, but isn't the same true of me and Sam?"
    d "No, because there was some time today everyone was in the cafeteria..."
    d "Except for you, Sam, or Shahar."
    d "Furthermore, none of us could have seen movement on the guard side from the cafeteria."
    d "It would be the perfect window of opportunity to kill Shahar."
    l "It's true that Sam and I had a window to kill Shahar..."
    l "But I can prove I didn't do it!"
    python:
        startHospitalTrial("lauren", "Lauren: Sam and I were together {color=#f00}the entire time since Sam left the cell this morning.{/color}.", -1,
        "lauren",  "Lauren: Sam woke up before the intercom, so {color=#f00}I couldn't have secretly killed Shahar before meeting Sam{/color}.", -1,
        "dracula",  "Dracula: No, {color=#f00}you could have snuck off on your own{/color} while Sam was awake but still in the cell.", -1,
        "dracula", "Dracula: Sam only would have {color=#f00}only waited a few minutes{/color} while you killed Shahar.", -1,
        2, [0, 11], "trial3d")
label trial3d:
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show drac ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "Wait, according to Sam's account, Sam stared out the cell door the entire morning."
    b "From before the intercom went off, until Lauren arrived at Sam's cell."
    d "So? I already covered this, Lauren could have made her first appearance after the murder."
    d "Sam would be none the wiser as to Lauren's activities prior to her meeting Sam this morning."
    b "Well, no, Sam claimed to be staring out the cell door at the guard side the entire morning."
    b "And Lauren's cell is at the end of hall containing Sam's cell."
    l "Yeah, that's true!"
    l "For me to leave my cell and the hallway, I'd have to pass by Sam's cell."
    l "So if I killed Shahar, Sam would've seen me walk past."
    l "Me meeting Sam at the cell would've been the second time Sam saw me this morning."
    s "...Yeah, that didn't happen..."
    s "...Dumb vampire..."
    d "Hmph fine. So Lauren couldn't have left without Sam noticing..."
    d "But that means Sam could have left without Lauren noticing."
    b "No, Lauren said she went to Sam's cell basically as soon as the intercom went off..."
    b "That would mean Sam would have to go to across the floor to Shahar's cell, kill him..."
    b "And then return, all in the time it took Lauren to walk roughly ten feet over to Sam's cell."
    d "...Alright, I guess this case is not as clear-cut as I assumed."
    d "Apologies for the diversion."
    b "No, this was good."
    b "We established that Lauren and Sam couldn't have done it."
    l "But... if someone killed Shahar using the bottle, doesn't that mean Dracula or Sid did it?"
    l "If Bert or Jenny did it, Dracula or Sid would have found the broken bottle yesterday."
    l "Dracula claimed earlier that Sam and I were the only ones on the guard side since we last saw Shahar..."
    l "But that's not necessarily true. Dracula or Sid could have killed Shahar during twilight..."
    l "After we all went to our cells, including Shahar."
    d "I don't think that's a line of questioning you wish to pursue."
    l "Why not? You'd want to say that, being the accused."
    d "Well, I can prove I didn't attack Shahar last night with the bottle."
    d "Which would mean, according to your theory, Sid did it."
    show sid mad with moveinright:
        xcenter .75
    i "Hey! Screw you old man!"
    d "Don't direct your hatred at me. Direct it at Lauren."
    d "It's her theory that places guilt onto you."
    i "You don't have proof! You're lying!"
    d "If I killed him yesterday during twilight, there would have been at least one witness."
    d "Either someone who was nearby or who would have had evidence I did it."
    d "Sigh... I can't deal with your incompetence any longer."
    d "Bert, you know who I'm talking about, right?"
    d "Please explain it to the child."
    b "Why me?"
    d "So that I don't have to."
    b "..."
    bi "I hate Dracula sometimes but..."
    bi "If it's going to get us closer to the truth, I'll have to figure out what he's talking about."
    bi "Let's see, who would have been a witness to Dracula assaulting Shahar yesterday..."
    call screen chooseCharHospital("sid", trial3e, "Who would have seen Dracula murder Shahar, or seen evidence of it?") with dissolve
label trial3e:
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show drac ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .75
    show sid mad:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "...Sid, if Dracula killed Shahar during twilight yesterday..."
    b "You would have known."
    i "What?"
    b "Did you see any shards of glass in front of Shahar's cell when you returned to your cell last night?"
    show sid ind:
        xcenter .75
    i "...No."
    b "So that means he didn't kill Shahar before you went to your cell yesterday."
    i "Oh... but wait, he could have killed Shahar when I was in my cell!"
    b "Sure, but then he would have had to pass your cell."
    i "What if I wasn't looking when he walked by?"
    b "Well, you would have probably heard something too."
    b "Shahar's cell is next to yours, and the cell door lets sound through freely."
    b "Not to mention, even if somehow you missed Dracula passing twice and the sound of glass breaking..."
    b "Jenny and I are also in that hallway."
    b "Do we really think Dracula snuck past all three of us twice, and none of us heard that sound?"
    i "..."
    show sid mad:
        xcenter .75
    i "So... are you accusing me?"
    b "What?"
    i "Well Lauren said it had to either be Dracula or I..."
    i "And you just said Dracula couldn't do it..."
    i "Seems like you're accusing me..."
    i "I'm gonna die, and you're all gonna die!"
    show lauren at inwindow behind hospwindowoverlay2:
        xcenter .5
        linear 0.15 xcenter .4
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .75
        linear 0.15 xcenter .6
    s "Shut up..."
    i "What?"
    s "That's not what Bert proved..."
    s "...All he said was you're the only one that could have hit Shahar with the bottle..."
    i "Screw you! That's just accusing me again!"
    b "!"
    b "Wait... Sam, that's a great point."
    i "What? No it's not!"
    b "Sid, just listen for a second."
    b "What Sam said is true, you're the only one that could have hit Shahar with the bottle last night."
    b "At least, without anyone seeing you do it."
    b "But we don't know that the bottle was used to hit Shahar."
    b "I kind of doubt it was, because even if Jenny and I didn't see Sid walk to Shahar's cell..."
    b "Why didn't we hear the bottle break last night?"
    d "Maybe you both fell asleep before twilight ended, and Sid did it right at the end of twilight."
    b "Maybe, but that's stretching a bit..."
    b "And that would also mean you could have done it while we were asleep."
    b "Until we figure out what the bottle's connection to the murder is, we can't accuse anyone."
    show sid ind:
        xcenter .75
    i "..."
    i "Oh! I get it!"
    i "I'm gonna think really hard about what the bottle's purpose is!"
    i "..."
    b "..."
    i "...Okay, I got nothing."
    d "I don't understand... how else would a bottle be used in the murder besides as a weapon?"
    l "Maybe it was just randomly there?"
    hide drac with moveoutleft
    show jenny ind with moveinleft:
        xcenter .25
    j "Wait... something's weird about how Lauren described the glass shards she found..."
    j "I think we can rule out Shahar being hit by the bottle!"
    b "Oh?"
    show ev3 shards with dissolve:
        xcenter .5 ycenter .5
    j "Think about it, if Shahar was hit with the bottle through the cell, something is missing..."
    bi "Missing?"
    bi "Let me try to visualize what Lauren described about the scene of Shahar's death..."
    bi "If Shahar was hit with the bottle through the cell, what spot is missing something?"
    call screen pickSpot5 with dissolve
label trial3f:
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show jenny ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2:
        xcenter .4
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .6
    show sid ind:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "Lauren, where were all the glass shards when you found them?"
    l "They were all on the floor in front of Shahar's cell."
    b "So there were none inside the cell?"
    l "Not that I remember, no..."
    j "Yeah, that's what I was getting at!"
    j "If someone hit Shahar with a bottle through the cell door..."
    show drac ind with moveinright:
        rotate 315
        xcenter 1.1
        ycenter .5
    d "And by someone, you mean Sid."
    show sid mad:
        xcenter .75
    hide drac with moveoutright
    j "...If {i}Sid{/i} hit Shahar with a bottle through the cell door."
    j "That means the bottle broke inside the cell, with momentum going into the cell."
    j "So how did all the shards end up outside the cell?"
    l "Perhaps the murderer cleaned up the shards inside the cell..."
    j "Oh, you mean to like, hide the evidence?"
    l "That would be the most likely reason, yeah."
    b "I don't think that's it."
    b "Because then something else is out-of-place at the murder scene..."
    bi "This one should be obvious, but I'll spell it out anyway..."
    bi "If someone cleaned up the shards inside the cell, what doesn't make sense?"
    call screen pickSpot6 with dissolve
label trial3g:
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show jenny ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2:
        xcenter .4
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .6
    show sid ind:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "Dracula, if the murderer cleaned up the shards inside the cell..."
    b "Why are there still shards outside the cell?"
    b "It makes no sense to me. A guard could have easily cleaned those as well."
    j "Oh yeah! If someone was trying to clean up the shards to hide the evidence..."
    j "They could have easily cleaned up the shards outside as well!"
    l "I was thinking the same thing, but..."
    l "Well, there's one possible killer who wouldn't have cleaned up the shards outside."
    j "What?"
    l "Just think about it for a second..."
    call screen chooseCharHospital("shahar", trial3h, "Who wouldn't have cleaned up the shards outside the cell?") with dissolve
label trial3h:
    scene bg hospkitchenwindow2
    show hospwindowoverlay2
    show jenny ind:
        xcenter .25
    show lauren ind at inwindow behind hospwindowoverlay2:
        xcenter .4
    show sam at inwindow behind hospwindowoverlay2:
        xcenter .6
    show sid ind:
        xcenter .75
    $showchibiwindow(["jenny", "dracula", "sid", "freddy"], ["lauren", "sam"])
    with dissolve
    b "You think... Shahar did it?"
    b "He... he..."
    bi "I couldn't bring myself to say it."
    bi "The words \"killed himself.\""
    l "I mean... it would explain why the shards outside the cell couldn't be cleaned."
    l "Shahar wasn't allowed to leave his cell on the guard side."
    l "So he could move shards from inside his cell to outside, but not move them from there."
    b "But... why?"
    j "Why what?"
    b "Why would he do that?"
    j "My guess is he moved the shards to conceal the nature of how he di-"
    l "I think Bert meant why would he commit suicide."
    j "...Oh."
    b "Yeah, that..."
    bi "As usual, Lauren not afraid to do what I can't..."
    b "It's just... why would you waste your shot at stopping the Game Master?"
    b "And potentially risk everyone else's lives in the process?"
    l "Did Shahar have any reason to... well, have a negative outlook on life?"
    l "People can make... well, irrational decisions when they're pushed to the edge."
    bi "...I don't want to, but... I have to tell them."
    b "...Yeah, I think Shahar had a reason."
    b "I hid some information from the rest of you."
    b "Remember how I said the computer has some patient records?"
    b "When I first checked it out I lied when I said I didn't recognize any of the names."
    b "Shahar's name was in there. And the only thing on his record was..."
    b "\"Patient thinks he is a pirate\"."
    l "Why didn't you tell us?"
    b "I... I thought given what we learned about Catherine and the mansion..."
    b "People might wrongly accuse him of being the Game Master."
    b "It might get him killed and waste an opportunity to get out of here."
    i "But how did you know he wasn't the Game Master?"
    b "I didn't."
    b "But I thought there was no way the Game Master would leave such an obvious clue."
    b "And I felt bad for him. If he really thinks he's a pirate and it's not all an act..."
    l "That's... understandable."
    l "Regardless, you told us now when it mattered."
    l "And it explains why Shahar may have taken such extreme actions."
    l "I can't imagine any of us would feel very good if we knew our life was a lie."
    l "It also explains the locked room murder aspect of Shahar's death."
    tut "Not all players may be familiar with the term locked room murder."
    menu:
        tut "Would you like an explanation?"
        "Yes.":
            jump trial3hb
        "Yes."
            jump trial3hb
label trial3hb:
    j "Locked room murder? What's that?"
    b "Good question Jenny!"
    b "A locked room murder is a type of crime that is especially difficult to solve."
    b "It's a murder where seemingly the killer could not have committed the crime and left the scene."
    b "There are four basic types of locked room murde-"
    j "Okay, I don't think I care anymore."
    i "This sounds like the type of explanation that would be very boring if you were already a mystery fan."
    i "And even if you aren't, it's kind of obvious what it means."
    i "A locked room murder is a murder where the room is locked."
    b "..."
    b "Okay, yeah, it's a bit silly of a concept to explain..."
