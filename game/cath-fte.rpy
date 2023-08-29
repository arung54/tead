
label cathAsk0:
    scene bg trainback
    $ statusnt("Caboose", "dan", ch = 1, sun = 1)
    show catherine happy with dissolve
    c "Achoo! Whew, sure is dusty back here."
    ni "I should go talk to Bert."
    call screen backCar with dissolve

label cathAsk1:
    scene bg trainback
    $ statusnt("Caboose", "dan", ch = 1, sun = 1)
    show catherine happy with dissolve
    c "Hey Dan!"
    ni "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "Cool!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
    call screen backCar with dissolve

label cathAsk2:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 4)
    show catherine nocat happy with dissolve
    c "Hey Bert, want to give me company while I look around the kitchen?"
    bi "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "Yay, company!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
    call screen kitchen with dissolve

label cathAsk3:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 1)
    show catherine happy with dissolve
    c "Did I already add a spoonful of salt?"
    bi "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "Ah, Bert, you can tell me if it's too salty!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
    call screen kitchen with dissolve

label cathAsk4:
    scene bg mansionkitchen
    $ statusnt("Kitchen", "bert", ch = 2, sun = 2)
    show catherine happy with dissolve
    c "Phew, all this cooking is making me sweat!"
    bi "Should I talk to Catherine?"
    menu:
        "Spend time with Catherine":
            c "If you can't handle the heat, don't get in the kitchen!"
            jump cathHang
        "Maybe later":
            hide catherine with dissolve
    call screen kitchen with dissolve

label cathHang:
    if fte_cath >= 3:
        b "Hm, on second thought, I've talked to Catherine plenty... I should talk to someone else."
        hide catherine with dissolve
        return
    if fte_cath == -1:
        c "Hey Dan."
        ses "Mrow!"
        c "Sesame says hi too!"
        n "Hey."
        c "This is a really lame situation, right?"
        n "Lame's definitely one way to think about it."
        c "Well, Sesame and I are trying to think about this like a vacation!"
        n "A vacation?"
        c "Yeah!"
        c "After all, we're stuck right now, so we might as well try to enjoy ourselves."
        n "Don't you think the situation is a little... grim to be trying to enjoy yourself?"
        c "Well, maybe!"
        c "But it can't hurt."
        c "I'll mostly just pretend to be sad around everyone else so I don't seem crazy, but..."
        c "Not having to study or work? And getting to hang out on this train?"
        c "Yes please! Sign me up!"
        ses "Mow mrowww!"
        ni "... is she really this happy-go-lucky?"
        show catherine ind
        c "Okay okay, don't get me wrong, I'm a bit worried."
        c "But honestly, I've learned to always take things in stride."
        c "Sesame and I have been through some sticky situations before, and they always work out!"
        n "Sticky situations?"
        c "Nothing as odd as this, but..."
        c "The life-sized foosball match definitely came close!"
        ses "*Sesame seemed to nod in agreement.*"
        n "Wait, what?"
        show catherine happy
        c "Long story!"
        c "Maybe sometime I'll go through the whole thing with you."
        c "Anyway, this has been nice. I'm glad you chose to talk with us."
        n "M-me too."
        scene black with fade
        ni "After a somewhat pleasant conversation, we returned to mingling with the others."

    if fte_cath == 0:
        show catherine nocat happy
        b "Hey Catherine, I was wondering..."
        b "Does Sesame get to ride around on your shoulder so freely outside of here?"
        c "Hm, I mean, normally if I went outside with him I would keep him in a carrier."
        c "And usually I'd only do that if I were taking him to the vet or on a trip with me."
        c "The outside world is dangerous for cats like him, hehe."
        show catherine nocat
        c "It's been kind of rough for him since the game started, to be honest."
        c "He's super well-behaved and not lashing out, but..."
        c "Cats get super stressed out changes in environment."
        c "It usually takes at least a week for them to adjust..."
        c "So far, we haven't been in a location for more than a few days."
        b "Hm, that's true,  besides biting Jenny on the train..."
        b "It doesn't seem like he's been stressed."
        c "Oh, he's stressed, I've just been uh, doing a good job hiding it from everyone."
        b "Hiding it?"
        c "Um... maybe let's talk about something more pleasant."
        show catherine nocat happy
        c "Are you interested in getting a cat Bert?"
        c "I work at a shelter so I could totally hook you up once we get out of here!"
        b "Oh, I mean, I like cats but I don't know if I'm ready for the lifestyle change."
        b "I do a lot of travelling and I feel like it'd be unfair to the cat for me to leave so often."
        c "Hm... that's true."
        c "After getting Sesame, I can't imagine travelling much."
        c "Last time I was away from Sesame for more than a day, I started having dreams about him."
        c "I missed him so much!"
        c "I'm glad Sesame gets to be here with me!"
        bi "...Sort of a weird sentiment given that it's a death game, but I get it."
        b "How long have you had Sesame?"
        c "Five years now!"
        c "That's part of why Sesame is so mellow, he's a medium-aged cat."
        c "At around two years old they start to chill out."
        show catherine nocat
        c "One of the saddest parts of working at the shelter is the older cats."
        c "A lot of people only want to adopt kittens."
        c "But even the older cats at the shelter can have nice long lives ahead of them."
        c "And they're a lot lower energy, which means they're easier to take care of."
        c "It's hard seeing a cat stay there for weeks while others get adopted in a day..."
        b "That is sad..."
        show catherine nocat happy
        c "Which is why you're going to adopt a cat, right Bert?"
        b "Um... okay, I'm still leaning no, but I'll think about it."
        c "Nice! One point for Catherine!"
        scene black with fade
        bi "Catherine and I chatted some more about cats."
        bi "I have to admit, she was starting to sell me on the idea of adopting one..."

    if fte_cath == 1:
        show catherine nocat happy
        c "Bert! Have you decided what kind of cat you're going to adopt?"
        b "Um... I haven't decided I'm going to adopt one yet."
        c "Nonsense! Everyone should have a cat."
        c "Haven't you seen all those cute videos on the internet?"
        c "Just imagine if they weren't just 2D videos!"
        b "Like... if they were virtual reality?"
        b "You know, that's a good point, I should watch cat videos in VR instead."
        c "Hm... okay, good deflection, one point to Bert!"
        b "One point? What's the score now?"
        c "Well, you have one point, that you just got, and I have..."
        c "Three million four hundred and fifty two thousand nine hundred and twelve!"
        b "Um... why do you have so many points?"
        c "Well, I'm the one who gives out the points."
        c "So naturally, I have the most opportunities to get the points!"
        c "I have a twenty something year head-start on the rest of you, so don't feel bad about it."
        b "Isn't that... I dunno, kind of unfair?"
        show catherine nocat
        c "What do you mean unfair?! It's not like I give myself points when I don't deserve them."
        c "{i}That{/i} would be unfair. Like having your high school's teacher as ref for the football game."
        b "But I mean, you got a head-start..."
        b "If someone got a head-start in a 100-meter dash, that would be unfair."
        c "Hm..."
        c "You raise a good point..."
        show catherine nocat happy
        c "Speaking of good points, that's another point for you Bert! You're at two now!"
        b "Thanks, at this rate, it'll only take me 1000 years to catch up to you..."
        c "Okay, I suppose the committee can look into more opportunities for points for people who aren't me."
        b "Is the committee just you?"
        c "Not just me! Sesame's on it too!"
        b "...I get the feeling Sesame agrees with you a lot."
        c "Always! It's good, this means the decisions the committee makes are unanimous."
        b "Is there... I dunno, anyone above the committee I can talk to?"
        c "Nope! The committee is the highest law of the land!"
        c "But the committee also acts in the interest of the people!"
        c "Fear not loyal point-earner!"
        b "Hm... is there any way I can opt out?"
        c "Opt out?"
        b "Yeah, like, just not participate in the point system."
        b "Seems like I can't get that many points anyway."
        show catherine nocat
        c "But... why wouldn't you want points?"
        c "That's no fun..."
        c "..."
        show catherine nocat happy
        c "Hm... okay Bert, the committee has decided opting out is a super-winning move, which gets you..."
        c "One billion points! More than anyone's ever heard of!"
        bi "Seems I found a way to win this game after all..."
        scene black with fade
        bi "Catherine and I participated in various activities to earn points."
        bi "If only I could cash these in for hints about this game..."

    if fte_cath == 2:
        show catherine nocat happy
        c "Bert! Come for more points, have you?"
        b "No, I think I have enough points for now."
        c "This is true... I finally understand the perspective of a low-point-haver now..."
        b "Well, I also wanted to ask you..."
        b "How did you meet Sesame?"
        c "Ah, great question!"
        show catherine nocat
        c "Unfortunately, it has a bittersweet answer..."
        c "One night, while sleeping, I thought I heard something moving in my apartment."
        c "I got up and I saw a black cat, Sesame, in the middle of my living room."
        c "He looked shocked and started making a funny noise repeatedly."
        c "I thought it was a stray cat."
        c "I left my windows partially open because of the summer heat, he must have gotten in that way."
        c "I thought maybe he wanted some food, so I went to the kitchen to get some."
        c "Then I... saw a man's head peeking through my window."
        c "I panicked, grabbed a pan from the kitchen and ran at him..."
        c "He saw that I noticed him and ran away."
        c "After calling the police, I found out... Sesame belonged to the man."
        c "The man was using Sesame to try to steal valuable objects from people."
        c "Sesame had a habit of biting onto shiny objects and bringing them to people."
        c "If Sesame got someone's key, obviously the man could just walk into the place."
        c "If he got lucky, Sesame would bring back something better like jewelry."
        c "It turns out Sesame wasn't the first cat he used..."
        b "That's... awful."
        b "To use a cat as a tool like that..."
        c "Yeah..."
        c "So it's bitter, because I kind of stole Sesame, and because..."
        c "Well, who knows what would happen if the robber was able to get into my place."
        c "But also, it's the day I met Sesame."
        c "And by making noise, Sesame might have accidentally saved my life."
        c "So... the robbery part sucks, but it was a good day overall."
        c "That's also when I decided to start eating vegetarian and work at a shelter."
        c "Coming that close to someone was willing to use animals like tools..."
        c "It made me want to protect as many animals as I could."
        b "That's... pretty noble."
        show catherine nocat happy
        c "Hehe, glad you think so."
        c "Maybe even... worthy of a million points, right?"
        b "Pfff. Yeah, a trillion even."
        c "Trillion?! I'll have to double check with the committee on that one..."
        c "...But based on the members, I think they'll approve."
        scene black with fade
        bi "I kept chatting with Catherine about her shelter work."
        bi "Knowing about her and Sesame's past changed my opinion of her."
        bi "Behind her goofy exterior, there's a strong-willed fighter in her."

    $fte_cath += 1
    $persistent.fte_cath = max(persistent.fte_cath, fte_cath)
    hide catherine with dissolve
    jump postFTEHandler
