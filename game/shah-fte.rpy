
#Train 1
label shahAsk0:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show shahar ind with dissolve
    h "Y'arr, if you think about it, a train is just a pirate ship on land."
    ni "...yeah, I should go talk to Bert instead of this guy."
    hide shahar with dissolve
    call screen frontCar with dissolve

#Train 2
label shahAsk1:
    scene bg trainfront1
    $ statusnt("Front Car", "dan", ch = 1, sun = 1)
    show shahar ind with dissolve
    h "Land ho!"
    h "Wait, no, that's just a mirage..."
    ni "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "Arr laddy, you've made a good choice!"
            ni "...have I?"
            call shahHang from _call_shahHang
        "Maybe later":
            hide shahar with dissolve
    call screen frontCar with dissolve

#Mansion 1
label shahAsk2:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 4)
    show shahar ind with dissolve
    h "*Burp*... aye matey, there might be such a thing as too much rum..."
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "*Braaaap*"
            call shahHang from _call_shahHang_1
        "Maybe later":
            hide shahar with dissolve
    call screen kitchen

#Mansion 2
label shahAsk3:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 1)
    show shahar ind with dissolve
    h "Not e'ry looting can be successful lad. Have to accept failure sometime."
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "Aye lad, here for more pirate wisdom?"
            call shahHang from _call_shahHang_2
        "Maybe later":
            hide shahar with dissolve
    call screen dining

#Mansion 3
label shahAsk4:
    scene bg mansiondining
    $ statusnt("Dining Room", "bert", ch = 2, sun = 2)
    show shahar ind with dissolve
    h "Ahoy me hearty! A party means booze, and that means Shahar is happy!"
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "Yer not my usual party company, but ye'll have to do, lad."
            call shahHang from _call_shahHang_3
        "Maybe later":
            hide shahar with dissolve
    call screen dining

#Hospital 1
label shahAsk5:
    scene bg hospkitchenwindow at bg
    show hospwindowoverlay
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show shahar ind at inwindow behind hospwindowoverlay
    h "Aye matey, that meal really brought me back it did."
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "I feel even more like I'm back with me old crew."
            call shahHang from _call_shahHang_4
        "Maybe later":
            hide shahar with dissolve
    call screen hospKitchen

#Hospital 2
label shahAsk6:
    scene bg hospcommons
    $ statusnt("Kitchen", "bert", ch = 3, sun = 1)
    show shahar ind with dissolve
    h "Me head aches, matey... I just wish it cease."
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "Happy to talk, but not too loudly lad."
            call shahHang from _call_shahHang_5
        "Maybe later":
            hide shahar with dissolve
    call screen patientcommons

#Hospital 3
label shahAsk7:
    scene bg hospcommons
    $ statusnt("Kitchen", "bert", ch = 3, sun = 2)
    show shahar ind with dissolve
    h "Burrito... what an interesting-sounding grub."
    bi "Should I talk to Shahar?"
    menu:
        "Spend time with Shahar":
            h "Aye matey, tell me more about these strange grubs of yers."
            call shahHang from _call_shahHang_6
        "Maybe later":
            hide shahar with dissolve
    call screen patientcommons

label shahHang:
    if fte_shah >= 3:
        bi "Hm, on second thought, I've talked to Shahar plenty... I should talk to someone else."
        hide shahar with dissolve
        return
    #Dan FTE 1
    if fte_shah == -1:
        h "Y'arr, Dan, what can I do for ye?"
        n "Do you really have to talk like that?"
        h "Talk like what, mate?"
        n "Like... you know, not normally."
        h "Lad, this is normal talk for me!"
        n "You know you talk like a pirate, right?"
        h "Because I am a pirate!"
        n "You're not though."
        h "What do ye mean? If I'm not a pirate, why are my memories all of the seas?"
        h "Plundering ports and arguing over how to split bounties, those were the days..."
        n "Pirates don't really exist they way you seem to think they do."
        n "They usually just attack rich people's ships and take their belongings."
        h "You agree, it's a noble profession!"
        h "Take from the rich scallywags, give to the poor."
        n "I... feel like you're missing the point."
        n "No one would dress up like you do these days."
        h "Why not lad? Feeling the wind of the sea, her cold embrace on my chest..."
        h "An outfit like this is perfect for charming the lady that is the sea."
        ni "There's gotta be some way I can get him to break..."
        n "Is there a pirate you model yourself off of?"
        h "Erm, I don't understand, lad."
        n "Like, Francis Drake, or Blackbeard."
        h "Who?"
        n "...You're a pirate and don't know who they are?"
        h "Aye ye scurvy dog, being a pirate isn't about knowing things."
        h "It's about a love of the seas, ship life, and lootin'!"
        ni "This is getting nowhere."
        $mood = "mad"
        n "Look you buffoon, you're not a pirate."
        n "You might be in a pirate costume."
        n "You might use words from some children's book on pirates."
        n "But pirates that act and talk like this don't exist anymore."
        n "You're just living out some fantasy scenario."
        n "I don't know why, but it's annoying and everyone sees through it."
        h "..."
        $mood = "ind"
        h "Look matey, I'm a pirate."
        h "Ever since me first memories, I've been one."
        h "So ye better shut yer trap before I make you walk the plank."
        n "Fine, if only because I think you could take me out in one punch, I'll let you be."
        n "But in a deadly situation like this, you really shouldn't be playing around."
        n "That's all I'm saying."
        h "There's no playing when ye live a deadly life like I."
        h "...Unless there's rum to be had, then there's plenty of playing."
        hide screen status_screen
        scene black
        with fade
        ni "Without a word I stormed off."
        ni "I understand Shahar better now at least."
        ni "Understand he's a lunatic, that is."

    #Bert FTE 1
    if fte_shah == 0:
        h "Ahoy laddy! What can I do fer ye?"
        b "Hey Shahar. I guess I wanted to know more about you and your life."
        h "Aye, anything in particular?"
        b "What's it like living on a ship?"
        h "Tumultuous lad. The ocean, she's not very careful."
        h "But I love her for that. Tough love, ye savvy?"
        h "Meals are hit or miss. Civvies, they eat every day, three meals a day."
        h "Pirates? Sometimes we starve for a few days, sometimes we eat like kings."
        b "Couldn't you ration food out?"
        h "Aye, but being a pirate ain't about living like a civvy."
        h "Being a pirate's about experiencing the lowest of the lows."
        h "And then, the highest of the highs are even sweeter."
        h "Fer example, after starving a few days, a bottle of rum hits harder."
        b "That... sounds unhealthy."
        h "What'd I just tell ye lad?"
        h "I'm not trying to be healthy, I'm trying to reach the highest moments!"
        h "Have ye ever sparred with a swashbuckler while you're three sheets to the wind?"
        b "Three sheets to the wind?"
        h "It's what civvies call wasted."
        b "Have you fought someone while wasted?"
        h "That's besides the point lad."
        bi "I'm going to take that as a no."
        h "Imagine, yer getting \"wasted\" with your mates."
        h "When BAM."
        h "Intruders aboard!"
        h "You went from the taste of rum to the taste of blood."
        h "And if you're a good pirate like yers truly, soon the taste of victory."
        h "It's an emotional roller coaster like no other."
        b "So this has happened to you?"
        h "No, but imagine if it had!"
        b "I feel like most pirates would just die fighting other pirates while drunk."
        h "Perhaps laddy, but I'm not like most pirates!"
        bi "Or like most people."
        b "You're right that does sound thrilling."
        h "Aye, now yer understandin' me laddy."
        h "Why don't we go try to find some rum right now and spar!"
        b "Uh... I think I'll pass."
        h "C'mon lad, ye gotta train if ye don't want to be shark bait!"
        hide screen status_screen
        scene black
        with fade
        b "After what seemed like hours, I managed to talk him out of fighting me drunk."
        b "I can't claim I understand Shahar better, but I think I at least like him more now."

    #Bert FTE 2
    if fte_shah == 1:
        h "Mate! Back for more tales of the sea?"
        b "Sort of. I was wondering, how did you become a pirate?"
        h "That's a rough one lad. I've been a pirate pretty much as far as I can remember."
        b "Wait, since you were a kid?"
        h "Something like that, aye."
        h "My first memory is of piracy."
        h "And every since then, I've been a pirate."
        b "Piracy? Like, torrenting files illegally on the internet?"
        h "Nay lad. Like looting and plundering."
        h "I know the internet has redefined what it means to be a pirate."
        h "But the internet is nary a substitute for the maiden sea!"
        b "Wait, so you never went to school? Lived in a house?"
        h "I've gone to school, bucko! Just... a school where you learn about piracy."
        h "Me and me classmates, we spent all day together learning about the sea."
        h "I vomited a lot my first few days on sea."
        h "But it was good! Because I earned me iron stomach in me first few months as a pirate."
        h "Just like bitter coffee or a sour wine, the sea is an acquired taste."
        h "And trust me, I got plenty a taste of the ocean water."
        b "Like... the literal salty water?"
        h "Aye... but nay. Never swam with the fishes, because pirate school taught me not to!"
        b "There's no way this school is real."
        h "Nay, it is!"
        b "And you had other classmates there."
        h "Aye, I did!"
        b "Did they all graduate and become pirates too?"
        h "Nay, none of them had the fervor for the ocean like me."
        b "Why would they go to a pirate school then?"
        h "My impression was they're forced to, lad."
        h "Maybe I was forced to as well. I don't really remember how I ended up there."
        h "I remember I'd order 'em around the ship, and they wouldn't do what I said."
        h "Bunch of scurvy dogs they were."
        bi "I'm starting to think this pirate school was some sort of cult."
        bi "Is Shahar the cult leader? But that wouldn't make sense if no one listened to him."
        bi "And how did he acquire a ship to do all this on?"
        bi "Well, that's assuming this story is real to begin with."
        b "Be honest with me Shahar. Are you faking this pirate story to hide something?"
        h "Like what, lad? Yer accusin' me of being the Game Master?"
        b "No, just... this is all so hard to believe."
        h "Lad, everything I'm telling you, it's what I truly remember and believe."
        b "Got it. I'll trust you then. Thanks for telling me about it."
        h "Aye. Appreciate the sentiment, mate."
        hide screen status_screen
        scene black
        with fade
        b "I got to know Shahar better, but I think it just made more sorry for him."

    #Bert FTE 3
    if fte_shah == 2:
        h "Back again lad? You must love hearing tales of the sea."
        bi "Not really, but at this point I'm all in on trying to figure him out."
        b "Yeah, I wanted to know more about this pirate school of yours."
        b "Surely no school would let kids go out on a ship."
        h "Kids? Nay lad, there was nary a kid there."
        b "Wait, what? It was you and a bunch of adults?"
        h "I was one of the adults, lad!"
        b "So did you go to regular school? You have memories before becoming a pirate?"
        h "Nay lad, going to that school was is first memory."
        bi "That somehow explains a lot."
        h "Something the matter, lad?"
        b "Yeah, that's sort of sad. You didn't have a proper childhood?"
        h "Maybe I did lad, but I can't remember it now."
        h "All I know is the earliest I can remember, I woke up and knew I wasn't meant to be a landlubber."
        b "So, amnesia?"
        h "I guess you could call it that, aye."
        b "I'm so sorry."
        h "Nothing to be sorry 'bout lad."
        h "Think about it, what do ye 'member from your school days?"
        b "I guess, lots of homework and embarassing social situations."
        h "Aye. So I don't exactly envy ye for having those memories."
        b "That's a fair point, I guess."
        b "If I can ask, do you know what caused your amnesia?"
        h "Nay. I once tried to figure it out, but there's nary a record of me."
        h "I asked people at me pirate school, but they avoided answering me."
        h "It'd be nice to know, but seems the universe hasn't got that in store for me."
        h "Not that it matters. The sea doesn't care who you were, only who you are."
        bi "It felt like my feelings about Shahar went from confusion to sympathy instantly."
        b "Shahar... if we both get out of here, I want to help you find out about your past."
        h "Oh? What inspired that?"
        b "I feel like we're friends now, Shahar."
        b "And that just feels like something friends would do."
        h "Aye lad, that's plenty gracious."
        h "In return, if we get out, ye can be my first mate!"
        b "Gonna be honest, I don't think I'm meant for life on the sea."
        b "But the offer is appreciated."
        hide screen status_screen
        scene black
        with fade
        bi "I felt like I finally understood Shahar, at least a little bit."
        bi "I hoped I could keep my promise to help him recover his memories."

    if fte_shah >= 3:
        bi "I enjoyed some time with Shahar, if only because of his pirate speak."

    $fte_shah += 1
    $persistent.fte_shah = max(persistent.fte_shah, fte_shah)
    hide shahar with dissolve
    if persistent.fte_shah >= 3:
        $achievement.grant('shah_fte')
    jump postFTEHandler
