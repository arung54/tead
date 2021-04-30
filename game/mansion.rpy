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
    hide drac
    with dissolve
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
    $showchibi("freddy", "lauren")
    show lauren ind with dissolve
    l "Hey, what happened in the other room? Heard lots of chatter."
    b "Some people suggested we all admit to our crime. It wasn't received very well."
    b "Now everyone's off exploring."
    l "Ah okay. Well, good news, the kitchen is rather well-stocked."
    l "What you'd expect from a kitchen in a mansion."
    l "All sorts of meats and veggies, the stove, fridge, and freezer all functioning, tap water's running."
    
